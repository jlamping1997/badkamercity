#!/usr/bin/env python3
"""Apply the owner-confirmed exact Acero tile color correction.

The builder embeds one catalog-free worker patch. The existing full staging,
readback, activation and rollback lifecycle stays in force. API source and
Shopify product data must remain unchanged.
"""
from __future__ import annotations

import ast
import datetime as dt
import fcntl
import hashlib
import json
import os
from pathlib import Path
import signal
import stat
import subprocess
import sys
import tempfile
import threading
import time
import types

PATCH_SOURCES = {'worker': '"""Guarded, catalog-free correction: exact Acero tile colors belong to Grijs.\n\nOnly the derived color layer changes. Source colors, other finishes, API code\nand exact numeric tile-format selection remain part of the existing worker.\n"""\nimport ast\nimport hashlib\n\nBASE_WORKER_SHA256 = \'25e8c3b1763171875bebd5b85e7099b26f87e36f3ece0b9f1f21e1d37b56dbe3\'\nPATCHED_WORKER_SHA256 = \'3c6dd21f50081f4ad8d770194dc35a97c101a09910dd8892403e51b93f1495eb\'\nMARKER = \'# BC_ACERO_GRAY_TILE_RULE_V1\'\n\nHELPERS = \'\'\'\n# BC_ACERO_GRAY_TILE_RULE_V1\ndef _bc_acero_is_tile(doc):\n    return any(HANDLE_GROUP.get(handle) == \'tile\'\n               for handle in _bc_simple_strings(doc.get(\'collection_handles\')))\n\ndef _bc_acero_targets(docs):\n    normalize_color = _BC_SIMPLE_COLORS[\'normalize\']\n    return [doc for doc in docs if _bc_acero_is_tile(doc)\n            and isinstance(doc.get(\'f_kleur_exact\'), str)\n            and normalize_color(doc[\'f_kleur_exact\']) == \'acero\']\n\ndef _bc_acero_check(docs):\n    return all(doc.get(\'f_kleur\') == [\'Grijs\'] for doc in _bc_acero_targets(docs))\n\'\'\'\n\n\ndef _sha(source):\n    return hashlib.sha256(source.encode(\'utf-8\')).hexdigest()\n\n\ndef _replace_once(source, old, new):\n    if source.count(old) != 1:\n        raise RuntimeError(\'Acero-hook ontbreekt of is niet uniek\')\n    return source.replace(old, new, 1)\n\n\ndef _offsets(source, node):\n    # AST columns are UTF-8 byte offsets, not Python character offsets.\n    lines = source.splitlines(keepends=True)\n    before = \'\'.join(lines[:node.lineno - 1])\n    after = \'\'.join(lines[:node.end_lineno - 1])\n    start = len(before) + len(lines[node.lineno - 1].encode()[:node.col_offset].decode())\n    end = len(after) + len(lines[node.end_lineno - 1].encode()[:node.end_col_offset].decode())\n    return start, end\n\n\ndef patch_acero_worker(source):\n    if not isinstance(source, str):\n        raise RuntimeError(\'Workerbron moet tekst zijn\')\n    if MARKER in source:\n        if source.count(MARKER) != 1 or _sha(source) != PATCHED_WORKER_SHA256:\n            raise RuntimeError(\'Bestaande Acero-correctie wijkt af; niets gewijzigd\')\n        compile(source, \'<existing-acero-worker>\', \'exec\')\n        return source\n    if _sha(source) != BASE_WORKER_SHA256:\n        raise RuntimeError(\'Worker wijkt af van de beoordeelde liveversie\')\n    tree = ast.parse(source)\n    color_literals = []\n    for node in ast.walk(tree):\n        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)\n                and node.func.id == \'compile\' and len(node.args) >= 3\n                and isinstance(node.args[1], ast.Constant)\n                and node.args[1].value == \'<derived-color-rules>\'\n                and isinstance(node.args[0], ast.Constant)\n                and isinstance(node.args[0].value, str)):\n            color_literals.append(node.args[0])\n    if len(color_literals) != 1:\n        raise RuntimeError(\'Geen unieke afgeleide kleurmodule\')\n    literal = color_literals[0]\n    colors = _replace_once(literal.value,\n        \'    if s in NO_COLOR:\\n\',\n        "    if s == \'acero\' and ctx.get(\'is_tile\') is True:\\n"\n        "        return _result(raw, [\'Grijs\'], \'OWNER_CONFIRMED\', \'Owner-confirmed Acero tile color grouped with gray.\')\\n"\n        \'    if s in NO_COLOR:\\n\')\n    colors = _replace_once(colors,\n        "return [{\'vendor\': vendor, \'series\': s} for s in series_values] if len(series_values) == 1 else [{\'vendor\': vendor}]",\n        "return [{\'vendor\': vendor, \'series\': s, \'is_tile\': doc.get(\'_bc_tile_color_context\') is True} for s in series_values] if len(series_values) == 1 else [{\'vendor\': vendor, \'is_tile\': doc.get(\'_bc_tile_color_context\') is True}]")\n    compile(colors, \'<acero-derived-color-rules>\', \'exec\')\n    start, end = _offsets(source, literal)\n    result = source[:start] + repr(colors) + source[end:]\n    result = _replace_once(result,\n        "color_doc = {**doc, \'f_kleur\': raw}",\n        "color_doc = {**doc, \'f_kleur\': raw, \'_bc_tile_color_context\': _bc_acero_is_tile(doc)}")\n    tree = ast.parse(result)\n    snapshots = [node for node in tree.body if isinstance(node, ast.FunctionDef)\n                 and node.name == \'_bc_simple_snapshot\']\n    profiles = [node for node in tree.body if isinstance(node, ast.FunctionDef)\n                and node.name == \'check_b2c_profiles\']\n    guards = [node for node in tree.body if isinstance(node, ast.If)\n              and ast.unparse(node.test) == "__name__ == \'__main__\'"]\n    if len(snapshots) != 1 or len(profiles) != 2 or len(guards) != 1:\n        raise RuntimeError(\'Verwachte bestaande workerhooks verschillen\')\n    snapshot = snapshots[0]\n    checks = profiles[-1]\n    returns = [node for node in checks.body if isinstance(node, ast.Return)]\n    if len(returns) != 1 or checks.body[-1] is not returns[0]:\n        raise RuntimeError(\'Geen unieke eindcontrole voor filters\')\n    lines = result.splitlines(keepends=True)\n    positions = [\n        (sum(len(line) for line in lines[:snapshot.end_lineno]),\n         "    if not _bc_acero_check(docs):\\n"\n         "        raise RuntimeError(\'Acero-tegels zijn niet uitsluitend Grijs\')\\n"\n         "    snapshot[\'acero_gray_v1\'] = True\\n"\n         "    snapshot[\'acero_gray_products\'] = len(_bc_acero_targets(docs))\\n"),\n        (sum(len(line) for line in lines[:returns[0].lineno - 1]),\n         "    checks.append({\'name\': \'Exacte Acero-tegels horen bij Grijs; bronkleur behouden\',\\n"\n         "                   \'passed\': snapshot.get(\'acero_gray_v1\') is True and _bc_acero_check(docs),\\n"\n         "                   \'products\': len(_bc_acero_targets(docs))})\\n"),\n        (sum(len(line) for line in lines[:guards[0].lineno - 1]), HELPERS.rstrip() + \'\\n\\n\'),\n    ]\n    for position, text in sorted(positions, reverse=True):\n        result = result[:position] + text + result[position:]\n    if result.count(MARKER) != 1:\n        raise RuntimeError(\'Acero-correctie niet eenduidig toegevoegd\')\n    compile(result, \'<acero-corrected-worker>\', \'exec\')\n    return result\n'}
TARGET_WORKER_SHA256 = '3c6dd21f50081f4ad8d770194dc35a97c101a09910dd8892403e51b93f1495eb'
TARGET_API_SHA256 = '3a7701134be7ac55b0a83436ceb16ebb19ac0a88aba17c283490f90047f02094'
TARGET_API_AST_SHA256 = '4b4dcf726b3f66f06d5f62bc322c8a9a236459ddf32cf56a2440e4c10147570b'
BASE_WORKER_SHA256 = '25e8c3b1763171875bebd5b85e7099b26f87e36f3ece0b9f1f21e1d37b56dbe3'
BASE_API_SHA256 = '3a7701134be7ac55b0a83436ceb16ebb19ac0a88aba17c283490f90047f02094'
BASE_API_AST_SHA256 = '4b4dcf726b3f66f06d5f62bc322c8a9a236459ddf32cf56a2440e4c10147570b'
ROOT = Path('/opt/badkamercity/filter-sync')
LIVE = Path('/home/ubuntu/bc_apiproef_20261013')
TIMER = 'bc-filter-sync.timer'
SERVICE = 'bc-filter-sync.service'
DEADLINE_SECONDS = 900
RECOVERY_SECONDS = 240


def sha256(value):
    return hashlib.sha256(value).hexdigest()


def ast_digest(source):
    def canonical(value):
        if isinstance(value, ast.AST):
            return (type(value).__name__, tuple((key, canonical(child))
                for key, child in ast.iter_fields(value)
                if not (key == 'type_params' and not child)))
        if isinstance(value, list):
            return tuple(canonical(child) for child in value)
        return value
    return sha256(repr(canonical(ast.parse(source))).encode('utf-8'))


def base_api_matches(source):
    # A color-only update must not rewrite even whitespace in the API source.
    return sha256(source) == BASE_API_SHA256


def say(value):
    try:
        print(value, flush=True)
    except OSError:
        # A closed SSH/PowerShell output stream must not interrupt recovery.
        pass


def read_regular(path, optional=False):
    if any(part.is_symlink() for part in (path, *path.parents)):
        raise RuntimeError('Onverwachte bestandsverwijzing; gestopt')
    try:
        info = path.stat()
    except FileNotFoundError:
        if optional:
            return None
        raise RuntimeError('Een vereist serverbestand ontbreekt') from None
    if not stat.S_ISREG(info.st_mode) or info.st_size > 5_000_000:
        raise RuntimeError('Onverwacht bestandstype of bestandsgrootte')
    return path.read_bytes()


def write_atomic(path, data, mode=0o600):
    if path.is_symlink():
        raise RuntimeError('Onverwachte verwijzing bij schrijven')
    fd, name = tempfile.mkstemp(prefix='.bc-filter-', dir=str(path.parent))
    try:
        with os.fdopen(fd, 'wb') as stream:
            os.fchmod(stream.fileno(), mode)
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def compose_worker(source, patch_sources):
    if sha256(source) != BASE_WORKER_SHA256:
        raise RuntimeError('Worker verschilt van de beoordeelde huidige versie')
    if set(patch_sources) != {'worker'}:
        raise RuntimeError('Acero-correctie bevat uitsluitend een workerpatch')
    namespace = {'__name__': 'bc_acero_worker_patch'}
    exec(compile(patch_sources['worker'], '<reviewed-acero-worker-patch>', 'exec'), namespace)
    result = namespace['patch_acero_worker'](source.decode('utf-8'))
    compile(result, '<acero-corrected-search-worker>', 'exec')
    return result.encode('utf-8')


def load_worker(source):
    module = types.ModuleType('bc_filter_release_candidate')
    module.__file__ = str(ROOT / 'sync.py')
    exec(compile(source, '<repaired-search-worker>', 'exec'), module.__dict__)
    return module


def systemctl(*args):
    try:
        result = subprocess.run(['systemctl', *args], capture_output=True, text=True,
                                timeout=30, check=False)
    except (OSError, subprocess.TimeoutExpired):
        raise RuntimeError('Systeemtaak reageert niet op tijd') from None
    return result.returncode, result.stdout.strip()


def change_timer(action):
    code, _ = systemctl(action, TIMER)
    if code:
        raise RuntimeError('Automatische ververstimer kon niet worden ' +
                           ('gepauzeerd' if action == 'stop' else 'hervat'))
    _, state = systemctl('is-active', TIMER)
    if state != ('active' if action == 'start' else 'inactive'):
        raise RuntimeError('Status van ververstimer is niet bevestigd na ' + action)


def restore_bytes(path, data, mode=0o600):
    current = read_regular(path, optional=True)
    if current == data:
        return
    if data is None:
        if current is not None:
            path.unlink()
    else:
        write_atomic(path, data, mode)


def restore_owned_metadata(path, previous, generation):
    """Restore our generation's bookkeeping while preserving an unrelated edit."""
    current = read_regular(path, optional=True)
    if current == previous:
        return True
    if generation is None or current is None:
        return False
    try:
        if path.name == 'prepared.txt':
            owned = current.decode('utf-8').strip() == generation
        else:
            value = json.loads(current)
            owned = isinstance(value, dict) and value.get('generation') == generation
    except (ValueError, UnicodeError):
        return False
    if not owned:
        return False
    restore_bytes(path, previous)
    return True


def safe_message(error, secrets):
    message = str(error) if isinstance(error, RuntimeError) else type(error).__name__
    for secret in sorted({str(x) for x in secrets if x and len(str(x)) >= 4}, key=len, reverse=True):
        message = message.replace(secret, '[afgeschermd]')
    return message[:900]


def repair(root=ROOT, live=LIVE, patch_sources=None, worker_factory=load_worker):
    if os.geteuid() != 0:
        raise RuntimeError('Voer deze reparatie met sudo python3 uit')
    if root != ROOT or live != LIVE:
        raise RuntimeError('Dit pakket is uitsluitend voor de bestaande zoekservice')
    patch_sources = patch_sources or PATCH_SOURCES
    if not isinstance(patch_sources, dict) or set(patch_sources) != {'worker'}:
        raise RuntimeError('Gebruik het complete gepubliceerde reparatiepakket')
    worker_path = root / 'sync.py'
    app_path = live / 'app.py'
    snapshot_path = live / 'bc_sync/active.json'
    original_worker = read_regular(worker_path)
    original_app = read_regular(app_path)
    if (TARGET_WORKER_SHA256 and sha256(original_worker) == TARGET_WORKER_SHA256 and
            TARGET_API_SHA256 and sha256(original_app) == TARGET_API_SHA256):
        snapshot = json.loads(read_regular(snapshot_path))
        if (snapshot.get('variant_aliases_v1') is not True or
                snapshot.get('filter_simplification_v1') is not True or
                snapshot.get('tile_format_codes_v1') is not True or
                snapshot.get('acero_gray_v1') is not True):
            raise RuntimeError('Gepatchte code gevonden zonder bevestigde filterindex')
        current = worker_factory(original_worker)
        health, _ = current.probe('http://127.0.0.1:8082/health')
        if health.get('ok') is not True or health.get('typesense_collection') != snapshot['collection']:
            raise RuntimeError('Gepatchte code gevonden; actieve zoekservice is nog niet bevestigd')
        _, timer_state = systemctl('is-active', TIMER)
        say('ACERO-CORRECTIE WAS AL TOEGEPAST | collectie: ' + snapshot['collection'])
        return {'status': 'already_applied' if timer_state == 'active' else 'already_applied_scheduler_pending',
                'collection': snapshot['collection'], 'timer_state': timer_state}
    if sha256(original_worker) != BASE_WORKER_SHA256 or not base_api_matches(original_app):
        raise RuntimeError('Servercode is inmiddels gewijzigd; geen bestanden overschreven')
    patched_worker = compose_worker(original_worker, patch_sources)
    if TARGET_WORKER_SHA256 and sha256(patched_worker) != TARGET_WORKER_SHA256:
        raise RuntimeError('Filterpakket heeft een afwijkende workerhash')
    worker = worker_factory(patched_worker)
    worker.log = say
    expected_api = worker.patch_api(original_app.decode()).encode()
    if expected_api != original_app:
        raise RuntimeError('Acero-correctie mag de bestaande API-bron niet wijzigen')
    if TARGET_API_SHA256 and sha256(expected_api) != TARGET_API_SHA256:
        raise RuntimeError('Acero-correctie heeft een afwijkende API-hash')
    lock_path = root / 'sync.lock'
    if lock_path.is_symlink():
        raise RuntimeError('Onverwachte verwijzing in synchronisatieslot')
    with lock_path.open('a+') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise RuntimeError('Een verversing loopt al. Wacht tot die klaar is en voer opnieuw uit.') from None
        # Recheck after locking; a completed hourly run or manual deployment is preserved.
        if read_regular(worker_path) != original_worker or read_regular(app_path) != original_app:
            raise RuntimeError('Servercode veranderde tijdens controle; gestopt')
        original_snapshot = read_regular(snapshot_path, optional=True)
        metadata_paths = ['STATUS.json', 'prepared.txt', 'last_transaction.json', 'original_transaction.json']
        metadata = {name: read_regular(root / name, optional=True) for name in metadata_paths}
        old_error = read_regular(root / 'LAST_ERROR.json', optional=True)
        _, timer_state = systemctl('is-active', TIMER)
        if timer_state not in ('active', 'inactive', 'failed'):
            raise RuntimeError('Status van ververstimer is niet eenduidig')
        timer_was_active = timer_state == 'active'
        timer_stopped = False
        completed = False
        installed = False
        backup = None
        staged = None
        candidate_generation = None
        secrets = []
        stop_heartbeat = threading.Event()
        started = time.monotonic()
        phase = ['voorbereiden']

        def heartbeat():
            while not stop_heartbeat.wait(20):
                say('Nog bezig: ' + phase[0] + ' | ' + str(int(time.monotonic() - started)) + ' seconden')

        def expired(signum, frame):
            raise RuntimeError('Tijdslimiet van 15 minuten bereikt; veilige afronding/herstel gestart')

        def terminated(signum, frame):
            raise RuntimeError('Uitvoering onderbroken; veilige afronding/herstel gestart')

        old_handler = signal.signal(signal.SIGALRM, expired)
        termination_handlers = {number: signal.signal(number, terminated)
                                for number in (signal.SIGTERM, signal.SIGHUP)}
        thread = threading.Thread(target=heartbeat, daemon=True)
        try:
            if timer_was_active:
                timer_stopped = True
                change_timer('stop')
            stamp = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S') + '-' + os.urandom(3).hex()
            backups = root / 'filter-simplification-backups'
            if backups.is_symlink():
                raise RuntimeError('Onverwachte verwijzing in herstelmap')
            backups.mkdir(mode=0o700, exist_ok=True)
            backup = backups / stamp
            backup.mkdir(mode=0o700)
            for name, data in {'sync.py': original_worker, 'app.py': original_app,
                               'active.json': original_snapshot, 'LAST_ERROR.json': old_error,
                               **metadata}.items():
                if data is not None:
                    write_atomic(backup / name, data)
            write_atomic(backup / 'candidate.py', patched_worker)
            say('Back-up gereed: ' + str(backup))
            signal.alarm(DEADLINE_SECONDS)
            thread.start()
            shop = worker.Shopify()
            secrets.extend([getattr(shop, 'token', ''), *getattr(shop, 'config', {}).values()])
            ts = worker.Typesense()
            secrets.append(getattr(ts, 'key', ''))
            phase[0] = 'volledige Shopify-export en controles'
            staged = worker.prepare(shop, ts)
            candidate_snapshot = json.loads((staged / 'snapshot.json').read_text())
            candidate_generation = candidate_snapshot.get('generation')
            if candidate_snapshot.get('variant_aliases_v1') is not True:
                raise RuntimeError('Voorbereide index mist de volledige variantondersteuning')
            if candidate_snapshot.get('filter_simplification_v1') is not True:
                raise RuntimeError('Voorbereide index mist de vereenvoudigde filterlaag')
            if candidate_snapshot.get('tile_format_codes_v1') is not True:
                raise RuntimeError('Voorbereide index mist de exacte tegelformaatcodes')
            if candidate_snapshot.get('acero_gray_v1') is not True:
                raise RuntimeError('Voorbereide index mist de Acero-naar-Grijs-correctie')
            phase[0] = 'gecontroleerde index activeren'
            snapshot = worker.activate(shop, ts, staged)
            if (snapshot.get('variant_aliases_v1') is not True or
                    snapshot.get('filter_simplification_v1') is not True or
                    snapshot.get('tile_format_codes_v1') is not True or
                    snapshot.get('acero_gray_v1') is not True):
                raise RuntimeError('Actieve generatie mist vereiste variant-/filter-/formaatvlaggen')
            report = json.loads((staged / 'RESULTAAT.json').read_text())
            if report.get('passed') is not True or report.get('active_changes') is not True:
                raise RuntimeError('Activatierapport bevestigt geen volledige reparatie')
            if read_regular(worker_path) != original_worker:
                raise RuntimeError('Worker is tussentijds gewijzigd; handmatige wijziging behouden')
            if read_regular(app_path) != expected_api:
                raise RuntimeError('Actieve API wijkt af van de voorbereide reparatie')
            write_atomic(root / 'sync.previous.py', original_worker, 0o755)
            write_atomic(worker_path, patched_worker, 0o755)
            installed = True
            if read_regular(worker_path) != patched_worker:
                raise RuntimeError('Ge\xefnstalleerde worker is niet exact teruggelezen')
            systemctl('reset-failed', SERVICE)
            error_path = root / 'LAST_ERROR.json'
            if error_path.exists():
                read_regular(error_path)
                error_path.unlink()
            completed = True
            signal.alarm(0)
            summary = {'status': 'applied_verified', 'collection': snapshot['collection'],
                       'products': report['products'], 'profiles': report['profiles'],
                       'backup': str(backup), 'worker_sha256': sha256(patched_worker),
                       'api_sha256': sha256(expected_api), 'variant_aliases_v1': True,
                       'filter_simplification_v1': True, 'tile_format_codes_v1': True,
                       'acero_gray_v1': True, 'acero_gray_products': snapshot.get('acero_gray_products')}
            write_atomic(backup / 'REPAIR_RESULT.json', json.dumps(summary, indent=2).encode())
            say('ACERO GECORRIGEERD | ' + str(report['products']) + ' producten | ' + str(report['profiles']) + ' profielen')
            return summary
        except BaseException as error:
            completed = False
            signal.alarm(0)
            for number in termination_handlers:
                signal.signal(number, signal.SIG_IGN)
            phase[0] = 'herstel controleren'
            restored = False
            try:
                signal.alarm(RECOVERY_SECONDS)
                now_snapshot = read_regular(snapshot_path, optional=True)
                now_app = read_regular(app_path)
                if now_snapshot == original_snapshot and now_app == original_app:
                    restored = True
                elif staged is not None:
                    candidate_bytes = read_regular(staged / 'snapshot.json')
                    # Restore only our own activation, never a different human deployment.
                    if now_snapshot == candidate_bytes and now_app in (original_app, expected_api):
                        transaction = json.loads(read_regular(root / 'last_transaction.json'))
                        previous_collection = (json.loads(original_snapshot)['collection']
                                               if original_snapshot is not None else None)
                        if (transaction.get('generation') != json.loads(candidate_bytes)['generation'] or
                                transaction.get('had_snapshot') is not (original_snapshot is not None) or
                                (previous_collection is not None and
                                 transaction.get('previous_collection') != previous_collection)):
                            raise RuntimeError('Hersteltransactie hoort niet bij deze uitvoering')
                        worker.restore_transaction(transaction)
                        restored = (read_regular(snapshot_path, optional=True) == original_snapshot and
                                    read_regular(app_path) == original_app)
                if restored:
                    if installed and read_regular(worker_path) == patched_worker:
                        write_atomic(worker_path, original_worker, 0o755)
                        installed = False
                    for name, data in metadata.items():
                        restore_owned_metadata(root / name, data, candidate_generation)
                if backup is not None:
                    failure = {'status': 'failed', 'previous_live_restored': restored,
                               'message': safe_message(error, secrets)}
                    write_atomic(backup / 'REPAIR_RESULT.json', json.dumps(failure, indent=2).encode())
                say('REPARATIE GESTOPT | ' + safe_message(error, secrets))
                say('Vorige liveversie gecontroleerd: ' + ('hersteld/behouden' if restored else 'handmatige controle nodig'))
            except BaseException as recovery_error:
                say('HERSTELCONTROLE NIET VOLTOOID | ' + safe_message(recovery_error, secrets))
            finally:
                signal.alarm(0)
            raise RuntimeError('Reparatie niet als voltooid gemarkeerd. Plak de uitvoer terug in de chat.') from None
        finally:
            signal.alarm(0)
            for number in termination_handlers:
                signal.signal(number, signal.SIG_IGN)
            stop_heartbeat.set()
            if thread.ident is not None:
                thread.join(timeout=1)
            try:
                if timer_stopped:
                    try:
                        change_timer('start')
                        say('Automatische ververstimer hervat.')
                    except RuntimeError:
                        if completed:
                            say('INDEX EN WORKER HERSTELD; VERFRESTIMER NIET HERVAT. Plak deze uitvoer terug.')
                            if backup is not None:
                                summary['status'] = 'applied_scheduler_pending'
                                summary['timer_active'] = False
                                write_atomic(backup / 'REPAIR_RESULT.json', json.dumps(summary, indent=2).encode())
                        else:
                            say('Ververstimer niet hervat; controle nodig.')
                        raise
            finally:
                signal.signal(signal.SIGALRM, old_handler)
                for number, handler in termination_handlers.items():
                    signal.signal(number, handler)


if __name__ == '__main__':
    try:
        result = repair()
        say(json.dumps(result, ensure_ascii=False))
    except (Exception, KeyboardInterrupt) as error:
        say('STOP: ' + safe_message(error, []))
        raise SystemExit(2)
