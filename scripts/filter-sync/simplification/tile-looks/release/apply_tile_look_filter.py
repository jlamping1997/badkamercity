#!/usr/bin/env python3
"""Install the existing tiles.look facet using the proven complete staging lifecycle.

The builder embeds one catalog-free look worker patch. The existing full staging,
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

PATCH_SOURCES = None
TARGET_WORKER_SHA256 = None
TARGET_API_SHA256 = None
TARGET_API_AST_SHA256 = None
TARGET_LOOK_TAXONOMY = None
BASE_WORKER_SHA256 = 'ecfc142a4fb15e66df297ec20884826be1bd4e8c491fb20bdb3e17cc281ba69a'
BASE_API_SHA256 = '3a7701134be7ac55b0a83436ceb16ebb19ac0a88aba17c283490f90047f02094'
BASE_API_AST_SHA256 = '4b4dcf726b3f66f06d5f62bc322c8a9a236459ddf32cf56a2440e4c10147570b'
ROOT = Path('/opt/badkamercity/filter-sync')
LIVE = Path('/home/ubuntu/bc_apiproef_20261013')
TIMER = 'bc-filter-sync.timer'
SERVICE = 'bc-filter-sync.service'
DEADLINE_SECONDS = 900
RECOVERY_SECONDS = 240
PRIOR_FLAGS = ('variant_aliases_v1', 'filter_simplification_v1', 'tile_format_codes_v1',
               'acero_gray_v1', 'cotto_visual_colors_v1', 'tile_bone_beige_v1', 'more_tile_colors_v1')
REQUIRED_FLAGS = PRIOR_FLAGS + ('tile_looks_v1',)
LOOK_FIELD = 'f_tegel_uitstraling'


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
    # A look-only filter update must not rewrite even whitespace in API source.
    return sha256(source) == BASE_API_SHA256


def require_existing_filter_snapshot(data):
    """The current seven-layer index is a prerequisite, not a legacy fallback."""
    try:
        value = json.loads(data) if data is not None else None
    except (ValueError, TypeError):
        value = None
    if (not isinstance(value, dict) or not value.get('collection') or
            any(value.get(key) is not True for key in PRIOR_FLAGS)):
        raise RuntimeError('Actieve index mist de zeven bestaande filterlagen; niets gewijzigd')
    return value


def validate_look_snapshot(snapshot):
    """Validate dynamic source-derived counts and the generic closed look UI.

    No product identities, source counts, or collection IDs are frozen here.
    Complete membership is independently checked by the prepared worker/API.
    """
    if not isinstance(snapshot, dict) or any(snapshot.get(key) is not True for key in REQUIRED_FLAGS):
        raise RuntimeError('Uitstralingindex mist een vereiste bestaande of nieuwe filtervlag')
    taxonomy = snapshot.get('tile_look_taxonomy')
    if (snapshot.get('tile_look_source') != 'tiles.look' or not isinstance(taxonomy, list) or
            not 2 <= len(taxonomy) <= 20 or any(not isinstance(value, str) or not value for value in taxonomy) or
            len(set(taxonomy)) != len(taxonomy) or
            (TARGET_LOOK_TAXONOMY is not None and tuple(taxonomy) != tuple(TARGET_LOOK_TAXONOMY))):
        raise RuntimeError('Uitstralingindex mist de vastgelegde bron of woordenlijst')
    products = snapshot.get('tile_look_products')
    missing = snapshot.get('tile_look_missing_products')
    counts = snapshot.get('tile_look_counts')
    if (type(products) is not int or products < 0 or type(missing) is not int or missing < 0 or
            not isinstance(counts, dict) or any(value not in taxonomy for value in counts) or
            any(type(count) is not int or count < 0 for count in counts.values()) or
            sum(counts.values()) != products):
        raise RuntimeError('Uitstralingaantallen sluiten niet aan op de volledige bronindex')
    profiles = snapshot.get('profiles')
    if not isinstance(profiles, dict) or not all(handle in profiles for handle in ('tegels', 'cottoceramix')):
        raise RuntimeError('Uitstralingindex mist de bestaande tegel- of Cottoceramix-scope')
    if profiles['tegels'].get('shopping_products') != products + missing:
        raise RuntimeError('Uitstralingdekking wijkt af van het actuele tegelaanbod')
    for handle, profile in profiles.items():
        policy = profile.get('b2c_policy', {})
        if policy.get('group') != 'tile' and handle != 'cottoceramix':
            continue
        allowed = [field for field in profile.get('allowed_filters', []) if field.get('field') == LOOK_FIELD]
        visible = [field for field in profile.get('filters', []) if field.get('field') == LOOK_FIELD]
        if (policy.get('tile_looks_v1') is not True or len(allowed) != 1 or
                allowed[0].get('type') != 'choice' or allowed[0].get('data_type') != 'string' or
                len(visible) > 1 or
                any(field.get('ui', {}).get('default_open') is not False or
                    field.get('ui', {}).get('control') != 'checkbox' or
                    field.get('ui', {}).get('section') != 'primary' for field in visible) or
                sum(bool(field.get('ui', {}).get('default_open')) for field in profile.get('filters', [])) > 2):
            raise RuntimeError('Uitstralingprofiel is niet de gecontroleerde gesloten tegelkeuze')
    cotto = profiles['cottoceramix']
    if (cotto.get('b2c_policy', {}).get('group') != 'general' or
            any(field.get('field') == 'f_tegel_formaat' for field in cotto.get('filters', []))):
        raise RuntimeError('Cottoceramix-profiel verandert buiten de uitstralingopdracht')
    return True


def verify_live_look_routes(worker, snapshot):
    """Check the unchanged API's actual local/public look interface before save."""
    validate_look_snapshot(snapshot)
    checks = []
    for base, label in [('http://127.0.0.1:8082', 'Lokale'),
                        ('https://vps-7ffd625d.vps.ovh.net/verified', 'Publieke')]:
        health, _ = worker.probe(base + '/health')
        healthy = health.get('ok') is True and health.get('typesense_collection') == snapshot['collection']
        checks.append({'name': label + ' uitstralingroute gebruikt de nieuwe generatie', 'passed': healthy})
        if not healthy:
            continue
        for handle in ('tegels', 'cottoceramix'):
            data, _ = worker.probe(base + '/api/v1/profile/' + handle)
            expected = snapshot['profiles'][handle]
            actual_fields = [field.get('field') for field in data.get('filters', [])]
            expected_fields = [field['field'] for field in expected['filters']]
            looks = [field for field in data.get('filters', []) if field.get('field') == LOOK_FIELD]
            correct = (data.get('filter_policy') == expected['b2c_policy'] and
                       actual_fields == expected_fields and
                       all(field.get('ui', {}).get('default_open') is False and
                           field.get('ui', {}).get('control') == 'checkbox' for field in looks))
            checks.append({'name': label + ' gesloten uitstralingprofiel: ' + handle, 'passed': correct})
        for value in snapshot['tile_look_taxonomy']:
            body = {'collection': 'tegels', 'q': '*', 'per_page': 1, 'include_facets': False,
                    'filters': {LOOK_FIELD: [value]}}
            data, _ = worker.probe(base + '/api/v1/search', body)
            expected_count = snapshot['tile_look_counts'].get(value, 0)
            checks.append({'name': label + ' actuele uitstralingkeuze: ' + value,
                           'passed': (data.get('found') == expected_count and
                                      (data.get('collection') or {}).get('handle') == 'tegels'),
                           'expected_count': expected_count, 'actual_count': data.get('found')})
        data, _ = worker.probe(base + '/api/v1/search', {'collection': 'tegels', 'per_page': 1,
            'include_facets': False, 'filters': {LOOK_FIELD: ['__bc_unknown_look__']}})
        checks.append({'name': label + ' onbekende uitstraling geeft nul producten',
                       'passed': data.get('found') == 0})
    return checks


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
        raise RuntimeError('Uitstralingfilter bevat uitsluitend een workerpatch')
    namespace = {'__name__': 'bc_tile_look_worker_patch'}
    exec(compile(patch_sources['worker'], '<reviewed-tile-look-worker-patch>', 'exec'), namespace)
    result = namespace['patch_tile_look_worker'](source.decode('utf-8'))
    compile(result, '<tile-look-search-worker>', 'exec')
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
                snapshot.get('acero_gray_v1') is not True or
                snapshot.get('cotto_visual_colors_v1') is not True or
                snapshot.get('tile_bone_beige_v1') is not True or
                snapshot.get('more_tile_colors_v1') is not True or
                snapshot.get('tile_looks_v1') is not True):
            raise RuntimeError('Gepatchte code gevonden zonder bevestigde filterindex')
        validate_look_snapshot(snapshot)
        current = worker_factory(original_worker)
        health, _ = current.probe('http://127.0.0.1:8082/health')
        if health.get('ok') is not True or health.get('typesense_collection') != snapshot['collection']:
            raise RuntimeError('Gepatchte code gevonden; actieve zoekservice is nog niet bevestigd')
        _, timer_state = systemctl('is-active', TIMER)
        say('UITSTRALINGFILTER WAS AL TOEGEPAST | collectie: ' + snapshot['collection'])
        return {'status': 'already_applied' if timer_state == 'active' else 'already_applied_scheduler_pending',
                'collection': snapshot['collection'], 'timer_state': timer_state}
    if sha256(original_worker) != BASE_WORKER_SHA256 or not base_api_matches(original_app):
        raise RuntimeError('Servercode is inmiddels gewijzigd; geen bestanden overschreven')
    require_existing_filter_snapshot(read_regular(snapshot_path))
    patched_worker = compose_worker(original_worker, patch_sources)
    if TARGET_WORKER_SHA256 and sha256(patched_worker) != TARGET_WORKER_SHA256:
        raise RuntimeError('Filterpakket heeft een afwijkende workerhash')
    worker = worker_factory(patched_worker)
    worker.log = say
    expected_api = worker.patch_api(original_app.decode()).encode()
    if expected_api != original_app:
        raise RuntimeError('Uitstralingfilter mag de bestaande API-bron niet wijzigen')
    if TARGET_API_SHA256 and sha256(expected_api) != TARGET_API_SHA256:
        raise RuntimeError('Uitstralingfilter heeft een afwijkende API-hash')
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
        require_existing_filter_snapshot(original_snapshot)
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
            candidate_snapshot_bytes = read_regular(staged / 'snapshot.json')
            candidate_snapshot = json.loads(candidate_snapshot_bytes)
            candidate_generation = candidate_snapshot.get('generation')
            if candidate_snapshot.get('variant_aliases_v1') is not True:
                raise RuntimeError('Voorbereide index mist de volledige variantondersteuning')
            if candidate_snapshot.get('filter_simplification_v1') is not True:
                raise RuntimeError('Voorbereide index mist de vereenvoudigde filterlaag')
            if candidate_snapshot.get('tile_format_codes_v1') is not True:
                raise RuntimeError('Voorbereide index mist de exacte tegelformaatcodes')
            if candidate_snapshot.get('acero_gray_v1') is not True:
                raise RuntimeError('Voorbereide index mist de Acero-naar-Grijs-correctie')
            if candidate_snapshot.get('cotto_visual_colors_v1') is not True:
                raise RuntimeError('Voorbereide index mist de beoordeelde Cotto-kleurregels')
            if candidate_snapshot.get('tile_bone_beige_v1') is not True:
                raise RuntimeError('Voorbereide index mist de bevestigde Bone-naar-Beige-correctie')
            if candidate_snapshot.get('more_tile_colors_v1') is not True:
                raise RuntimeError('Voorbereide index mist de extra tegelkleuren en herkomstcontroles')
            validate_look_snapshot(candidate_snapshot)
            phase[0] = 'gecontroleerde index activeren'
            snapshot = worker.activate(shop, ts, staged)
            if (snapshot.get('variant_aliases_v1') is not True or
                    snapshot.get('filter_simplification_v1') is not True or
                    snapshot.get('tile_format_codes_v1') is not True or
                    snapshot.get('acero_gray_v1') is not True or
                    snapshot.get('cotto_visual_colors_v1') is not True or
                    snapshot.get('tile_bone_beige_v1') is not True or
                    snapshot.get('more_tile_colors_v1') is not True or
                snapshot.get('tile_looks_v1') is not True):
                raise RuntimeError('Actieve generatie mist vereiste variant-/filter-/formaatvlaggen')
            validate_look_snapshot(snapshot)
            report = json.loads((staged / 'RESULTAAT.json').read_text())
            if report.get('passed') is not True or report.get('active_changes') is not True:
                raise RuntimeError('Activatierapport bevestigt geen volledige reparatie')
            live_look_checks = verify_live_look_routes(worker, snapshot)
            report.setdefault('checks', []).extend(live_look_checks)
            report['passed'] = report['passed'] and all(check['passed'] for check in live_look_checks)
            write_atomic(staged / 'RESULTAAT.json', json.dumps(report, ensure_ascii=False, indent=2).encode())
            for check in live_look_checks:
                say(('GOED' if check['passed'] else 'FOUT') + ' | ' + check['name'])
            if report['passed'] is not True:
                raise RuntimeError('Lokale of publieke uitstralingroute is niet volledig bevestigd')
            if read_regular(worker_path) != original_worker:
                raise RuntimeError('Worker is tussentijds gewijzigd; handmatige wijziging behouden')
            if read_regular(app_path) != expected_api:
                raise RuntimeError('Actieve API wijkt af van de voorbereide reparatie')
            if read_regular(snapshot_path) != candidate_snapshot_bytes:
                raise RuntimeError('Actieve index is tussentijds gewijzigd; andere generatie behouden')
            write_atomic(root / 'sync.previous.py', original_worker, 0o755)
            write_atomic(worker_path, patched_worker, 0o755)
            installed = True
            if read_regular(worker_path) != patched_worker:
                raise RuntimeError('Geïnstalleerde worker is niet exact teruggelezen')
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
                       'acero_gray_v1': True, 'acero_gray_products': snapshot.get('acero_gray_products'),
                       'cotto_visual_colors_v1': True,
                       'cotto_visual_color_products': snapshot.get('cotto_visual_color_products'),
                       'tile_bone_beige_v1': True,
                       'tile_bone_beige_products': snapshot.get('tile_bone_beige_products'),
                       'more_tile_colors_v1': True,
                       'more_scoped_color_products': snapshot.get('more_scoped_color_products'),
                       'more_missing_color_products': snapshot.get('more_missing_color_products'),
                       'more_missing_color_counts': snapshot.get('more_missing_color_counts'),
                       'tile_looks_v1': True, 'tile_look_source': snapshot.get('tile_look_source'),
                       'tile_look_products': snapshot.get('tile_look_products'),
                       'tile_look_missing_products': snapshot.get('tile_look_missing_products'),
                       'tile_look_counts': snapshot.get('tile_look_counts'),
                       'tile_look_taxonomy': snapshot.get('tile_look_taxonomy')}
            write_atomic(backup / 'REPAIR_RESULT.json', json.dumps(summary, indent=2).encode())
            say('UITSTRALINGFILTER TOEGEPAST | ' + str(report['products']) + ' producten | ' + str(report['profiles']) + ' profielen')
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
