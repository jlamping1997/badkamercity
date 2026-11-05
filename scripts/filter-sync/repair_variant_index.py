#!/usr/bin/env python3
"""Guarded, single-run repair of the existing BadkamerCity search worker.

The release builder embeds the two reviewed pure patch modules. This program
uses the deployed worker's existing complete staging, readback and activation
checks. It never edits Shopify product data or runs historical cleanup.
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

PATCH_SOURCES = {'worker': '"""Pure, version-guarded patch for the reviewed product-level search worker.\n\nThis module does not read or write server files and does not contact Shopify.\nThe installer supplies the reviewed worker source, then injects the separately\nreviewed ``patch_variant_api`` function before compiling the complete program.\n"""\nfrom __future__ import annotations\n\nimport ast\nimport hashlib\n\n\nBASE_WORKER_SHA256 = "2064b549e173d709fe1d5e8e5fe8cb549276e817d46b111510fcc4bc12471cf2"\nPATCH_MARKER = "# BC_MULTI_VARIANT_PRODUCTS_V1"\n\n\nHELPERS = r\'\'\'\n# BC_MULTI_VARIANT_PRODUCTS_V1\ndef _bc_variant_summary(product):\n    from decimal import InvalidOperation\n    variants = product.get(\'_variants\')\n    if not isinstance(variants, list) or not variants:\n        raise RuntimeError(\'Geen varianten in volledige productexport voor \' + product[\'id\'])\n    choices = []\n    aliases = set()\n    identities = set()\n    for variant in variants:\n        if not isinstance(variant, dict):\n            raise RuntimeError(\'Ongeldige variant voor \' + product[\'id\'])\n        identity = variant.get(\'id\')\n        if not isinstance(identity, str) or not re.fullmatch(r\'gid://shopify/ProductVariant/[0-9]+\', identity):\n            raise RuntimeError(\'Variantidentiteit ontbreekt voor \' + product[\'id\'])\n        if identity in identities:\n            raise RuntimeError(\'Dubbele variantidentiteit voor \' + product[\'id\'])\n        identities.add(identity)\n        raw_sku = variant.get(\'sku\') or \'\'\n        if not isinstance(raw_sku, str):\n            raise RuntimeError(\'Ongeldig variantartikelnummer voor \' + product[\'id\'])\n        if raw_sku.strip():\n            aliases.add(raw_sku.strip().casefold())\n        try:\n            if isinstance(variant.get(\'price\'), bool):\n                raise ValueError(\'boolean price\')\n            cents = Decimal(variant[\'price\']) * 100\n            valid = cents.is_finite() and cents >= 0 and cents == cents.to_integral_value()\n        except (InvalidOperation, ValueError, TypeError, KeyError):\n            valid = False\n        if not valid:\n            raise RuntimeError(\'Onjuiste variantprijs bij \' + product[\'id\'])\n        choices.append((int(cents), int(identity.rsplit(\'/\', 1)[-1]), variant))\n    choices.sort(key=lambda item: (item[0], item[1]))\n    return {\'variant\': choices[0][2], \'sku_aliases\': sorted(aliases),\n            \'price_varies\': len({item[0] for item in choices}) > 1,\n            \'variant_count\': len(choices)}\n\n\ndef _bc_add_variant_schema(schema):\n    fields = [dict(field) for field in schema[\'fields\']]\n    additions = [{\'name\': \'sku_aliases\', \'type\': \'string[]\', \'facet\': True, \'optional\': True},\n                 {\'name\': \'price_varies\', \'type\': \'bool\', \'optional\': True}]\n    for addition in additions:\n        current = [field for field in fields if field[\'name\'] == addition[\'name\']]\n        if current:\n            if len(current) != 1 or any(current[0].get(key) != value for key, value in addition.items()):\n                raise RuntimeError(\'Bestaand variantschemaveld wijkt af: \' + addition[\'name\'])\n        else:\n            fields.append(addition)\n    return {**schema, \'fields\': fields}\n\n\ndef _bc_variant_probe(docs):\n    for product in sorted(docs, key=lambda item: int(item[\'id\'])):\n        secondary = [sku for sku in product.get(\'sku_aliases\', []) if sku != product[\'sku_exact\']]\n        if not secondary:\n            continue\n        query = secondary[0]\n        expected = {item[\'id\']: {key: item[key] for key in\n                    (\'price_cents\', \'price_varies\', \'sku_aliases\')}\n                    for item in docs if query in item.get(\'sku_aliases\', [])}\n        return {\'query\': query, \'expected\': expected}\n    return None\n\n\ndef _bc_variant_hot_check(snapshot, base, label):\n    sample = snapshot.get(\'variant_probe\')\n    if not sample:\n        return []\n    expected = sample[\'expected\']\n    observed = {}\n    page = 1\n    good = True\n    while True:\n        data, _ = probe(base + \'/api/v1/search\', {\'collection\': \'__all__\',\n            \'q\': sample[\'query\'], \'per_page\': 100, \'page\': page, \'include_facets\': False})\n        if data.get(\'found\') != len(expected):\n            good = False\n            break\n        hits = data.get(\'products\', [])\n        for product in hits:\n            identity = product.get(\'id\')\n            if identity in observed or identity not in expected:\n                good = False\n            observed[identity] = product\n        if len(observed) >= len(expected):\n            break\n        if not hits or page > len(expected):\n            good = False\n            break\n        page += 1\n    good = good and set(observed) == set(expected) and all(\n        all(observed[identity].get(key) == value for key, value in fields.items())\n        for identity, fields in expected.items())\n    return [{\'name\': label + \' tweede variantartikelnummer vindt dezelfde productkaart\',\n             \'passed\': good, \'expected_count\': len(expected), \'actual_count\': len(observed)}]\n\'\'\'\n\n\ndef _replace_once(value: str, before: str, after: str, label: str) -> str:\n    if value.count(before) != 1:\n        raise RuntimeError("Workerfragment wijkt af: " + label)\n    return value.replace(before, after, 1)\n\n\ndef _replace_function(source: str, name: str, replacements: list[tuple[str, str]]) -> str:\n    tree = ast.parse(source)\n    matches = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == name]\n    if len(matches) != 1:\n        raise RuntimeError("Workerfunctie ontbreekt of is dubbel: " + name)\n    node = matches[0]\n    lines = source.splitlines(keepends=True)\n    text = "".join(lines[node.lineno - 1:node.end_lineno])\n    for index, (before, after) in enumerate(replacements):\n        text = _replace_once(text, before, after, name + ":" + str(index))\n    lines[node.lineno - 1:node.end_lineno] = [text]\n    return "".join(lines)\n\n\ndef patch_worker(source: str) -> str:\n    """Return a patched copy only for the exact reviewed deployed worker."""\n    if not isinstance(source, str):\n        raise TypeError("Workerbron moet tekst zijn")\n    if hashlib.sha256(source.encode("utf-8")).hexdigest() != BASE_WORKER_SHA256:\n        raise RuntimeError("Workerhash wijkt af van de gecontroleerde versie; niets gewijzigd")\n    source = _replace_function(source, "normalize_products", [\n        ("""        if len(variants) != 1:\n            raise RuntimeError(\'Meer of minder dan \xe9\xe9n variant voor \' + p[\'id\'] + \'; eerst variantlogica beoordelen\')\n        variant = variants[0]; sku = variant.get(\'sku\') or \'\'""",\n         """        variant_info = _bc_variant_summary(p)\n        variant = variant_info[\'variant\']; sku = variant.get(\'sku\') or \'\'"""),\n        ("verified = (isinstance(manifest, dict)", "verified = (len(variants) == 1 and isinstance(manifest, dict)"),\n        ("general = not (sku.upper().startswith(\'SPOM\') or discovery.get(\'general_filters\') == \'excluded\')",\n         """service_only = (sku.upper().startswith(\'SPOM\') if len(variants) == 1 else\n            bool(variant_info[\'sku_aliases\']) and all(value.startswith(\'spom\') for value in variant_info[\'sku_aliases\']))\n        general = not (service_only or discovery.get(\'general_filters\') == \'excluded\')"""),\n        ("        stats[\'verified_manifests\' if verified else \'without_verified_manifest\'] += 1",\n         """        d[\'sku_aliases\'] = variant_info[\'sku_aliases\']\n        d[\'price_varies\'] = variant_info[\'price_varies\']\n        stats[\'multi_variant_products\'] += int(len(variants) > 1)\n        stats[\'variants\'] += len(variants)\n        stats[\'verified_manifests\' if verified else \'without_verified_manifest\'] += 1"""),\n    ])\n    source = _replace_function(source, "patch_api", [\n        ("return patch_rvs_api(patch_b2c_api(patch_generation_api(source)))",\n         "return patch_variant_api(patch_rvs_api(patch_b2c_api(patch_generation_api(source))))")\n    ])\n    source = _replace_function(source, "selected", [\n        ("if d[\'sku_exact\'] != q: continue",\n         "if q not in (d.get(\'sku_aliases\', []) if snapshot.get(\'variant_aliases_v1\') else [d[\'sku_exact\']]): continue")\n    ])\n    source = _replace_function(source, "make_cases", [\n        ("    for case in cases:\\n        case[\'expected_ids\']",\n         """    variant_probe = snapshot.get(\'variant_probe\')\n    if variant_probe:\n        cases.append({\'name\': \'Tweede variantartikelnummer vindt \xe9\xe9n productdocument\',\n            \'body\': {\'collection\': \'__all__\', \'q\': variant_probe[\'query\'], \'include_facets\': False}, \'status\': 200})\n    for case in cases:\n        case[\'expected_ids\']""")\n    ])\n    source = _replace_function(source, "check_api", [\n        ("(\'price_cents\', \'title\', \'handle\', \'image_url\')",\n         "(\'price_cents\', \'title\', \'handle\', \'image_url\', \'sku_aliases\', \'price_varies\')")\n    ])\n    source = _replace_function(source, "prepare", [\n        ("    for key in (\'default_sorting_field\'", "    schema = _bc_add_variant_schema(schema)\\n    for key in (\'default_sorting_field\'"),\n        ("\'exact\': sorted({d[\'sku_exact\'] for d in docs if d[\'sku_exact\']}),",\n         """\'exact\': sorted({alias for d in docs for alias in d[\'sku_aliases\']}),\n        \'variant_aliases_v1\': True, \'variant_probe\': _bc_variant_probe(docs),"""),\n    ])\n    source = _replace_function(source, "hot_checks", [\n        ("    return checks", "        checks += _bc_variant_hot_check(snapshot, base, label)\\n    return checks")\n    ])\n    source = _replace_once(source, "def normalize_products(", HELPERS.strip() + "\\n\\n\\ndef normalize_products(", "helper insertion")\n    compile(source, "<patched-search-worker>", "exec")\n    return source\n', 'api': '"""Pure, guarded patch for the existing product-level search API.\n\nThe installer embeds ``patch_variant_api`` into the worker. It only changes\nrequest planning; the existing generation, B2C and RVS middleware stay intact.\n"""\n\n\ndef patch_variant_api(source: str) -> str:\n    """Add generation-gated SKU aliases without changing legacy requests."""\n    import ast\n    import hashlib\n\n    marker = \'# BC_VARIANT_ALIASES_V1\'\n    original_fingerprint = \'8caafe524fbe3b01b96217e7ce1c67673afd688e3d4da187b06438ea05026467\'\n    patched_fingerprint = \'275c494351dbf4152da8f18d34babd028a110be7e9739249d078b79d9fe990d6\'\n\n    def fingerprint(node):\n        # Python 3.12 adds an empty type_params field to function nodes. Ignore\n        # only that empty field so the guard also works on the VPS interpreter.\n        def canonical(value):\n            if isinstance(value, ast.AST):\n                return (type(value).__name__, tuple(\n                    (key, canonical(child)) for key, child in ast.iter_fields(value)\n                    if not (key == \'type_params\' and not child)))\n            if isinstance(value, list):\n                return tuple(canonical(child) for child in value)\n            return value\n        return hashlib.sha256(repr(canonical(node)).encode(\'utf-8\')).hexdigest()\n\n    try:\n        tree = ast.parse(source)\n    except SyntaxError:\n        raise RuntimeError(\'Zoek-API bevat ongeldige Python-code\') from None\n    plans = [node for node in tree.body\n             if isinstance(node, ast.FunctionDef) and node.name == \'plan\']\n    if len(plans) != 1:\n        raise RuntimeError(\'Zoek-API mist de verwachte unieke planfunctie\')\n    plan = plans[0]\n    current = fingerprint(plan)\n    if marker in source:\n        if source.count(marker) != 1 or current != patched_fingerprint:\n            raise RuntimeError(\'Bestaande variantpatch wijkt af; geen wijziging\')\n        return source\n    if current != original_fingerprint:\n        raise RuntimeError(\'Zoek-API planfunctie wijkt af van de beoordeelde versie\')\n\n    variable = \'_bc_variant_aliases_v1\'\n    flag = ast.parse(\n        variable + " = _bc_snapshot().get(\'variant_aliases_v1\') is True"\n    ).body[0]\n    plan.body.insert(0, flag)\n    replacements = {\'exact\': 0, \'query\': 0, \'fields\': 0}\n\n    class Rewrite(ast.NodeTransformer):\n        def visit_BinOp(self, node):\n            self.generic_visit(node)\n            if (isinstance(node.op, ast.Add) and\n                    isinstance(node.left, ast.Constant) and\n                    node.left.value == \'sku_exact:=\'):\n                node.left = ast.IfExp(\n                    test=ast.Name(id=variable, ctx=ast.Load()),\n                    body=ast.Constant(value=\'sku_aliases:=\'),\n                    orelse=ast.Constant(value=\'sku_exact:=\'))\n                replacements[\'exact\'] += 1\n            return node\n\n        def visit_Dict(self, node):\n            self.generic_visit(node)\n            for position, key in enumerate(node.keys):\n                if not isinstance(key, ast.Constant):\n                    continue\n                value = node.values[position]\n                if (key.value == \'query_by\' and isinstance(value, ast.Constant)\n                        and value.value == \'title,sku,vendor,f_productsoort\'):\n                    suffix = \',sku_aliases\'\n                    replacements[\'query\'] += 1\n                elif (key.value == \'include_fields\' and\n                      isinstance(value, ast.Constant) and value.value ==\n                      \'id,shopify_product_id,sku,title,handle,vendor,product_type,price_cents,url,image_url\'):\n                    suffix = \',sku_aliases,price_varies\'\n                    replacements[\'fields\'] += 1\n                else:\n                    continue\n                node.values[position] = ast.BinOp(\n                    left=value, op=ast.Add(), right=ast.IfExp(\n                        test=ast.Name(id=variable, ctx=ast.Load()),\n                        body=ast.Constant(value=suffix),\n                        orelse=ast.Constant(value=\'\')))\n            return node\n\n    Rewrite().visit(plan)\n    if replacements != {\'exact\': 1, \'query\': 1, \'fields\': 1}:\n        raise RuntimeError(\'Niet alle verwachte variantzoekvelden zijn gevonden\')\n    ast.fix_missing_locations(plan)\n    if fingerprint(plan) != patched_fingerprint:\n        raise RuntimeError(\'Variantzoekpatch is niet gelijk aan de beoordeelde versie\')\n    lines = source.splitlines(keepends=True)\n    start = sum(len(line) for line in lines[:plan.lineno - 1])\n    end = sum(len(line) for line in lines[:plan.end_lineno])\n    result = source[:start] + ast.unparse(plan) + \'\\n\' + source[end:]\n    result = result.rstrip() + \'\\n\\n\' + marker + \'\\n\'\n    compile(result, \'<variant-search-api>\', \'exec\')\n    return result\n'}
TARGET_WORKER_SHA256 = 'e5f3c4103266c3df1f03b855395d0d6c1711b7452a7626c91889cfc9b3ab280c'
TARGET_API_SHA256 = '7fe0b7faa2f5bf83af40edfa8d409dc382ba25453c15f6ebea4115c76e29f3b3'
TARGET_API_AST_SHA256 = '76a5ab7e741528d0aa5327b64988fd57d5f3b5fb7f54e952f76ce2bd50e0a938'
BASE_WORKER_SHA256 = '2064b549e173d709fe1d5e8e5fe8cb549276e817d46b111510fcc4bc12471cf2'
BASE_API_SHA256 = '6e4895a1ebc7937da9fbec0a92b141213320e87a382a2fcf5d479daedde0a573'
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
    fd, name = tempfile.mkstemp(prefix='.bc-variant-', dir=str(path.parent))
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
        raise RuntimeError('Worker verschilt van de aangeleverde en beoordeelde versie')
    namespace = {'__name__': 'bc_variant_worker_patch'}
    exec(compile(patch_sources['worker'], '<reviewed-worker-patch>', 'exec'), namespace)
    result = namespace['patch_worker'](source.decode('utf-8'))
    api_module = patch_sources['api']
    tree = ast.parse(result)
    hooks = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == 'patch_api']
    if len(hooks) != 1:
        raise RuntimeError('Geen unieke API-patchfunctie in worker')
    lines = result.splitlines(keepends=True)
    position = sum(len(line) for line in lines[:hooks[0].lineno - 1])
    result = result[:position] + api_module.rstrip() + '\n\n' + result[position:]
    compile(result, '<repaired-search-worker>', 'exec')
    return result.encode('utf-8')


def load_worker(source):
    module = types.ModuleType('bc_variant_repair_candidate')
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
    if not isinstance(patch_sources, dict) or set(patch_sources) != {'api', 'worker'}:
        raise RuntimeError('Gebruik het complete gepubliceerde reparatiepakket')
    worker_path = root / 'sync.py'
    app_path = live / 'app.py'
    snapshot_path = live / 'bc_sync/active.json'
    original_worker = read_regular(worker_path)
    original_app = read_regular(app_path)
    if (TARGET_WORKER_SHA256 and sha256(original_worker) == TARGET_WORKER_SHA256 and
            TARGET_API_AST_SHA256 and ast_digest(original_app) == TARGET_API_AST_SHA256):
        snapshot = json.loads(read_regular(snapshot_path))
        if snapshot.get('variant_aliases_v1') is not True:
            raise RuntimeError('Gepatchte code gevonden zonder bevestigde nieuwe index')
        current = worker_factory(original_worker)
        health, _ = current.probe('http://127.0.0.1:8082/health')
        if health.get('ok') is not True or health.get('typesense_collection') != snapshot['collection']:
            raise RuntimeError('Gepatchte code gevonden; actieve zoekservice is nog niet bevestigd')
        _, timer_state = systemctl('is-active', TIMER)
        say('REPARATIE WAS AL TOEGEPAST | collectie: ' + snapshot['collection'])
        return {'status': 'already_applied' if timer_state == 'active' else 'already_applied_scheduler_pending',
                'collection': snapshot['collection'], 'timer_state': timer_state}
    if sha256(original_worker) != BASE_WORKER_SHA256 or sha256(original_app) != BASE_API_SHA256:
        raise RuntimeError('Servercode is inmiddels gewijzigd; geen bestanden overschreven')
    patched_worker = compose_worker(original_worker, patch_sources)
    if TARGET_WORKER_SHA256 and sha256(patched_worker) != TARGET_WORKER_SHA256:
        raise RuntimeError('Reparatiepakket heeft een afwijkende workerhash')
    worker = worker_factory(patched_worker)
    worker.log = say
    expected_api = worker.patch_api(original_app.decode()).encode()
    if TARGET_API_AST_SHA256 and ast_digest(expected_api) != TARGET_API_AST_SHA256:
        raise RuntimeError('Reparatiepakket heeft afwijkende API-logica')
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
            backups = root / 'variant-repair-backups'
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
            phase[0] = 'gecontroleerde index activeren'
            snapshot = worker.activate(shop, ts, staged)
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
                       'api_sha256': sha256(expected_api), 'variant_aliases_v1': True}
            write_atomic(backup / 'REPAIR_RESULT.json', json.dumps(summary, indent=2).encode())
            say('ZOEKINDEX HERSTELD | ' + str(report['products']) + ' producten | ' + str(report['profiles']) + ' profielen')
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
