import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import runpy
import tempfile
from types import SimpleNamespace
import unittest
from unittest import mock


FOLDER = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('variant_release_base', FOLDER / 'apply_variant_repair.py')
repair = importlib.util.module_from_spec(spec)
spec.loader.exec_module(repair)


class VariantReleaseTests(unittest.TestCase):
    def test_ascii_transport_reconstructs_both_reviewed_patch_modules_exactly(self):
        release = FOLDER / 'repair_variant_index.py'
        self.assertTrue(release.read_bytes().isascii())
        namespace = runpy.run_path(str(release))
        self.assertEqual(namespace['PATCH_SOURCES'], {
            'api': (FOLDER / 'variant_api_patch.py').read_text(),
            'worker': (FOLDER / 'variant_worker_patch.py').read_text()})

    def already_applied(self, timer, healthy=True):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / 'worker'; root.mkdir()
            live = Path(temporary) / 'api'; live.mkdir()
            (live / 'bc_sync').mkdir()
            worker_bytes = b'value = 1\n'
            api_bytes = b'def value():\n    return 2\n'
            (root / 'sync.py').write_bytes(worker_bytes)
            (live / 'app.py').write_bytes(api_bytes)
            (live / 'bc_sync/active.json').write_text(json.dumps({
                'collection': 'bc_current', 'variant_aliases_v1': True}))
            probe = lambda url: ({'ok': healthy, 'typesense_collection': 'bc_current'}, {})
            with mock.patch.multiple(repair, ROOT=root, LIVE=live,
                    TARGET_WORKER_SHA256=hashlib.sha256(worker_bytes).hexdigest(),
                    TARGET_API_AST_SHA256=repair.ast_digest(api_bytes)), \
                    mock.patch.object(repair.os, 'geteuid', return_value=0), \
                    mock.patch.object(repair, 'systemctl', return_value=(0, timer)) as control, \
                    contextlib.redirect_stdout(io.StringIO()):
                result = repair.repair(root, live, {'api': '', 'worker': ''},
                                       lambda source: SimpleNamespace(probe=probe))
                control.assert_called_once_with('is-active', repair.TIMER)
                self.assertEqual(set(root.iterdir()), {root / 'sync.py'})
                return result

    def test_already_applied_requires_live_health_and_reports_active_timer(self):
        self.assertEqual(self.already_applied('active')['status'], 'already_applied')

    def test_already_applied_preserves_inactive_timer_and_reports_scheduler_pending(self):
        result = self.already_applied('inactive')
        self.assertEqual(result['status'], 'already_applied_scheduler_pending')
        self.assertEqual(result['timer_state'], 'inactive')

    def test_already_applied_does_not_claim_success_when_live_service_is_unhealthy(self):
        with self.assertRaisesRegex(RuntimeError, 'actieve zoekservice'):
            self.already_applied('active', healthy=False)


if __name__ == '__main__':
    unittest.main()
