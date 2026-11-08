"""Isolated lifecycle tests: no SSH, HTTP, Docker or real systemd calls."""
import contextlib
import fcntl
import importlib.util
import io
import json
from pathlib import Path
import signal
import tempfile
import types
import unittest
from unittest.mock import Mock, patch


SPEC = importlib.util.spec_from_file_location(
    'apply_filter_simplification_tested', Path(__file__).with_name('apply_filter_simplification.py'))
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class RepairLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'worker'
        self.live = Path(self.temp.name) / 'api'
        self.root.mkdir()
        (self.live / 'bc_sync').mkdir(parents=True)
        self.worker_path = self.root / 'sync.py'
        self.app_path = self.live / 'app.py'
        self.snapshot_path = self.live / 'bc_sync/active.json'
        self.old_worker, self.new_worker = b'old worker', b'new worker'
        self.old_app, self.new_app = b'old API', b'new API'
        self.old_snapshot = json.dumps({'generation': 'old', 'collection': 'old_index'}).encode()
        self.new_snapshot = json.dumps({'generation': 'new', 'collection': 'new_index',
                                        'variant_aliases_v1': True, 'filter_simplification_v1': True}).encode()
        self.worker_path.write_bytes(self.old_worker)
        self.app_path.write_bytes(self.old_app)
        self.snapshot_path.write_bytes(self.old_snapshot)
        self.original_metadata = {
            'STATUS.json': json.dumps({'generation': 'old', 'collection': 'old_index'}).encode(),
            'prepared.txt': b'old',
            'last_transaction.json': json.dumps({'generation': 'old'}).encode(),
            'original_transaction.json': json.dumps({'generation': 'original'}).encode(),
        }
        for name, data in self.original_metadata.items():
            (self.root / name).write_bytes(data)
        (self.root / 'LAST_ERROR.json').write_text('{"message":"old failure"}')
        self.timer_state = 'active'
        self.mode = 'success'
        self.system_calls = []
        self.stdout = io.StringIO()
        self.alarm = Mock()
        self.restored = Mock(side_effect=self.restore)
        self.worker = types.SimpleNamespace(
            patch_api=lambda source: self.new_app.decode(),
            Shopify=Mock(return_value=types.SimpleNamespace(
                token='sensitive-token-value', config={'client_secret': 'secret-config-value'})),
            Typesense=Mock(return_value=types.SimpleNamespace(key='ts-secret-value')),
            prepare=Mock(side_effect=self.prepare), activate=Mock(side_effect=self.activate),
            restore_transaction=self.restored, cleanup=Mock())
        self.factory = Mock(return_value=self.worker)
        stack = contextlib.ExitStack()
        self.addCleanup(stack.close)
        stack.enter_context(contextlib.redirect_stdout(self.stdout))
        for key, value in [('ROOT', self.root), ('LIVE', self.live),
                           ('BASE_WORKER_SHA256', M.sha256(self.old_worker)),
                           ('BASE_API_SHA256', M.sha256(self.old_app)),
                           ('TARGET_WORKER_SHA256', None), ('TARGET_API_SHA256', None)]:
            stack.enter_context(patch.object(M, key, value))
        stack.enter_context(patch.object(M.os, 'geteuid', return_value=0))
        stack.enter_context(patch.object(M, 'compose_worker', return_value=self.new_worker))
        stack.enter_context(patch.object(M, 'systemctl', side_effect=self.systemctl))
        stack.enter_context(patch.object(M.signal, 'signal', side_effect=self.set_signal))
        stack.enter_context(patch.object(M.signal, 'alarm', self.alarm))

    def set_signal(self, signum, handler):
        if callable(handler):
            if signum == signal.SIGALRM:
                self.expire = handler
            elif signum == signal.SIGTERM:
                self.terminate = handler
        return 'previous signal handler'

    def systemctl(self, *args):
        self.system_calls.append(args)
        if args[0] == 'is-active':
            return (0 if self.timer_state == 'active' else 3), self.timer_state
        if args[0] == 'stop':
            self.timer_state = 'inactive'
            return (1 if self.mode == 'stop_failure' else 0), ''
        if args[0] == 'start':
            if self.mode == 'timer_failure':
                return 1, ''
            self.timer_state = 'active'
        return 0, ''

    def prepare(self, shop, ts):
        if self.mode == 'prepare_failure':
            raise RuntimeError('Stage failed')
        if self.mode == 'manual_metadata':
            (self.root / 'STATUS.json').write_text('{"generation":"manual"}')
            raise RuntimeError('Stage failed')
        if self.mode == 'secret_failure':
            raise RuntimeError('secret-config-value sensitive-token-value ts-secret-value')
        if self.mode == 'timeout':
            self.expire(signal.SIGALRM, None)
        if self.mode == 'termination':
            self.terminate(signal.SIGTERM, None)
        staged = self.root / 'staged'
        staged.mkdir()
        (staged / 'snapshot.json').write_bytes(self.new_snapshot)
        (staged / 'RESULTAAT.json').write_text(json.dumps({
            'passed': True, 'active_changes': False, 'products': 2, 'profiles': 1}))
        (self.root / 'prepared.txt').write_bytes(b'new')
        return staged

    def activate(self, shop, ts, staged):
        self.snapshot_path.write_bytes(self.new_snapshot)
        self.app_path.write_bytes(self.new_app)
        transaction = {'generation': 'new', 'previous_collection': 'old_index',
                       'had_snapshot': self.old_snapshot is not None}
        (self.root / 'last_transaction.json').write_text(json.dumps(transaction))
        if self.mode == 'partial_activation':
            raise RuntimeError('Activation failed')
        (self.root / 'STATUS.json').write_text('{"generation":"new"}')
        (staged / 'RESULTAAT.json').write_text(json.dumps({
            'passed': True, 'active_changes': True, 'products': 2, 'profiles': 1}))
        if self.mode == 'manual_worker':
            self.worker_path.write_bytes(b'human worker change')
        if self.mode == 'manual_app':
            self.app_path.write_bytes(b'human API change')
        return json.loads(self.new_snapshot)

    def restore(self, transaction):
        self.app_path.write_bytes(self.old_app)
        if self.old_snapshot is None:
            self.snapshot_path.unlink()
        else:
            self.snapshot_path.write_bytes(self.old_snapshot)

    def run_repair(self):
        return M.repair(root=self.root, live=self.live,
                        patch_sources={'worker': 'fixture', 'api': 'fixture'},
                        worker_factory=self.factory)

    def assert_original_live(self):
        self.assertEqual(self.app_path.read_bytes(), self.old_app)
        self.assertEqual(self.snapshot_path.read_bytes(), self.old_snapshot)

    def test_hash_mismatch_stops_before_lock_timer_or_backup_writes(self):
        self.worker_path.write_bytes(b'unreviewed change')
        before = sorted(str(x.relative_to(self.root)) for x in self.root.rglob('*'))
        with self.assertRaisesRegex(RuntimeError, 'inmiddels gewijzigd'):
            self.run_repair()
        self.assertEqual(self.worker_path.read_bytes(), b'unreviewed change')
        self.assertEqual(self.system_calls, [])
        self.factory.assert_not_called()
        self.assertEqual(before, sorted(str(x.relative_to(self.root)) for x in self.root.rglob('*')))

    def test_busy_lock_does_not_stop_timer_or_start_worker(self):
        with (self.root / 'sync.lock').open('a+') as held:
            fcntl.flock(held, fcntl.LOCK_EX | fcntl.LOCK_NB)
            with self.assertRaisesRegex(RuntimeError, 'verversing loopt al'):
                self.run_repair()
        self.assertEqual(self.system_calls, [])
        self.worker.prepare.assert_not_called()
        self.assertFalse((self.root / 'filter-simplification-backups').exists())

    def test_success_installs_only_after_verified_activation_and_keeps_backup(self):
        result = self.run_repair()
        self.assertEqual(result['status'], 'applied_verified')
        self.assertEqual(self.worker_path.read_bytes(), self.new_worker)
        self.assertEqual(self.app_path.read_bytes(), self.new_app)
        self.assertEqual(self.snapshot_path.read_bytes(), self.new_snapshot)
        self.assertEqual(self.timer_state, 'active')
        self.assertEqual((Path(result['backup']) / 'sync.py').read_bytes(), self.old_worker)
        self.assertFalse((self.root / 'LAST_ERROR.json').exists())
        self.worker.cleanup.assert_not_called()

    def test_prepare_failure_leaves_live_and_worker_unchanged(self):
        self.mode = 'prepare_failure'
        with self.assertRaises(RuntimeError):
            self.run_repair()
        self.assert_original_live()
        self.assertEqual(self.worker_path.read_bytes(), self.old_worker)
        self.assertEqual(self.timer_state, 'active')
        self.restored.assert_not_called()

    def test_partial_activation_restores_only_this_generation(self):
        self.mode = 'partial_activation'
        with self.assertRaises(RuntimeError):
            self.run_repair()
        self.assert_original_live()
        self.restored.assert_called_once()
        for name, value in self.original_metadata.items():
            self.assertEqual((self.root / name).read_bytes(), value)

    def test_human_worker_change_is_preserved_during_live_rollback(self):
        self.mode = 'manual_worker'
        with self.assertRaises(RuntimeError):
            self.run_repair()
        self.assert_original_live()
        self.assertEqual(self.worker_path.read_bytes(), b'human worker change')
        self.restored.assert_called_once()

    def test_human_api_change_is_not_overwritten_by_rollback(self):
        self.mode = 'manual_app'
        with self.assertRaises(RuntimeError):
            self.run_repair()
        self.assertEqual(self.app_path.read_bytes(), b'human API change')
        self.restored.assert_not_called()
        self.assertIn('handmatige controle nodig', self.stdout.getvalue())

    def test_unrelated_metadata_change_is_preserved(self):
        self.mode = 'manual_metadata'
        with self.assertRaises(RuntimeError):
            self.run_repair()
        self.assertEqual(json.loads((self.root / 'STATUS.json').read_bytes())['generation'], 'manual')
        self.assert_original_live()

    def test_legacy_no_snapshot_activation_can_roll_back(self):
        self.old_snapshot = None
        self.snapshot_path.unlink()
        self.mode = 'partial_activation'
        with self.assertRaises(RuntimeError):
            self.run_repair()
        self.restored.assert_called_once()
        self.assertFalse(self.snapshot_path.exists())
        self.assertEqual(self.app_path.read_bytes(), self.old_app)
        self.assertNotIn('HERSTELCONTROLE NIET VOLTOOID', self.stdout.getvalue())

    def test_timeout_disarms_main_deadline_before_recovery(self):
        self.mode = 'timeout'
        with self.assertRaises(RuntimeError):
            self.run_repair()
        calls = [x.args[0] for x in self.alarm.call_args_list]
        self.assertEqual(calls[:3], [900, 0, 240])
        self.assert_original_live()
        self.assertEqual(self.timer_state, 'active')

    def test_timer_restart_failure_reports_partial_success_without_reverting_index(self):
        self.mode = 'timer_failure'
        with self.assertRaisesRegex(RuntimeError, 'hervat'):
            self.run_repair()
        self.assertEqual(self.worker_path.read_bytes(), self.new_worker)
        self.assertEqual(self.snapshot_path.read_bytes(), self.new_snapshot)
        reports = list((self.root / 'filter-simplification-backups').glob('*/REPAIR_RESULT.json'))
        self.assertEqual(json.loads(reports[0].read_bytes())['status'], 'applied_scheduler_pending')
        self.restored.assert_not_called()

    def test_failed_timer_stop_still_restores_prior_active_state(self):
        self.mode = 'stop_failure'
        with self.assertRaises(RuntimeError):
            self.run_repair()
        self.assertIn(('start', M.TIMER), self.system_calls)
        self.assertEqual(self.timer_state, 'active')
        self.assert_original_live()

    def test_original_inactive_timer_is_not_started(self):
        self.timer_state = 'inactive'
        self.run_repair()
        self.assertFalse(any(x[0] in ('start', 'stop') for x in self.system_calls))
        self.assertEqual(self.timer_state, 'inactive')

    def test_runtime_messages_redact_known_credentials(self):
        self.mode = 'secret_failure'
        with self.assertRaises(RuntimeError):
            self.run_repair()
        for secret in ('secret-config-value', 'sensitive-token-value', 'ts-secret-value'):
            self.assertNotIn(secret, self.stdout.getvalue())
        self.assertIn('[afgeschermd]', self.stdout.getvalue())

    def test_termination_uses_recovery_and_restores_the_timer(self):
        self.mode = 'termination'
        with self.assertRaises(RuntimeError):
            self.run_repair()
        self.assert_original_live()
        self.assertEqual(self.timer_state, 'active')
        self.assertIn('Uitvoering onderbroken', self.stdout.getvalue())

    def test_closed_output_does_not_interrupt_activation_or_recovery(self):
        class ClosedOutput:
            def write(self, value):
                raise BrokenPipeError('closed SSH output')

            def flush(self):
                raise BrokenPipeError('closed SSH output')

        with contextlib.redirect_stdout(ClosedOutput()):
            result = self.run_repair()
        self.assertEqual(result['status'], 'applied_verified')
        self.assertEqual(self.worker_path.read_bytes(), self.new_worker)
        self.assertEqual(self.timer_state, 'active')
        self.assertIs(self.worker.log, M.say)

    def test_missing_simplification_flag_stops_before_activation(self):
        value = json.loads(self.new_snapshot)
        value.pop('filter_simplification_v1')
        self.new_snapshot = json.dumps(value).encode()
        with self.assertRaises(RuntimeError):
            self.run_repair()
        self.worker.activate.assert_not_called()
        self.assert_original_live()
        self.assertEqual(self.worker_path.read_bytes(), self.old_worker)
        self.assertEqual(self.timer_state, 'active')

    def test_missing_variant_flag_stops_before_activation(self):
        value = json.loads(self.new_snapshot)
        value.pop('variant_aliases_v1')
        self.new_snapshot = json.dumps(value).encode()
        with self.assertRaises(RuntimeError):
            self.run_repair()
        self.worker.activate.assert_not_called()
        self.assert_original_live()

    def test_success_preserves_variant_support_and_records_filter_flag(self):
        result = self.run_repair()
        self.assertIs(result['variant_aliases_v1'], True)
        self.assertIs(result['filter_simplification_v1'], True)


class ApiSourceGuards(unittest.TestCase):
    def test_api_formatting_difference_allowed_only_with_same_ast(self):
        source = b'def plan(body):\n    return body\n'
        formatted = b'\ndef plan( body ):\n return body\n'
        with patch.object(M, 'BASE_API_SHA256', M.sha256(source)), patch.object(M, 'BASE_API_AST_SHA256', M.ast_digest(source)):
            self.assertTrue(M.base_api_matches(source))
            self.assertTrue(M.base_api_matches(formatted))
            self.assertFalse(M.base_api_matches(b'def plan(body):\n    return None\n'))
            self.assertFalse(M.base_api_matches(b'not valid python code !'))


if __name__ == '__main__':
    unittest.main()
