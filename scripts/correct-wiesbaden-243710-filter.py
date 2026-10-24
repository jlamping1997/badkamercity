#!/usr/bin/env python3
"""One-document Typesense correction. Python standard library; run with sudo.

No Shopify writes, bulk import, schema changes, credentials in output or files.
See docs/product-content/wiesbaden/24.3710-filter-correction.md.
"""
import argparse
import copy
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import urllib.error
import urllib.request

INDEX = "bc_verified_full_20261013_874e415c15"
DOC_ID = "10657256210698"
SKU = "24.3710"
FIELD = "f_aantal_kraangaten"
CONTAINER = "badkamercity-filter-api-verified-candidate"
TS = "http://127.0.0.1:8108"
APIS = ("http://127.0.0.1:8082", "https://vps-7ffd625d.vps.ovh.net/verified")
PROFILE = "opbouw-wastafelkranen"
COLLECTIONS = {
    "kranen": "gid://shopify/Collection/569428181258",
    "wastafels": "gid://shopify/Collection/569428246794",
    "wastafelkranen": "gid://shopify/Collection/570058506506",
    PROFILE: "gid://shopify/Collection/570059522314",
}
BACKUP_ROOT = Path("/var/backups/badkamercity-243710")
DEFAULT_BACKUP = BACKUP_ROOT / "filterfix-20261020.json"
DOC_PATH = f"/collections/{INDEX}/documents/{DOC_ID}"


class Blocked(Exception):
    """Only deliberate, sanitized messages may be passed here."""


def require(condition, message):
    if not condition:
        raise Blocked(message)


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def same(left, right):
    # Unlike Python ==, this distinguishes bool from int.
    return canonical(left) == canonical(right)


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise Blocked("HTTP redirect geweigerd; endpoints moeten ongewijzigd blijven.")


def request_json(url, method="GET", body=None, key=None):
    allowed = ((TS + f"/collections/{INDEX}", {"GET"}),
               (TS + DOC_PATH, {"GET", "PATCH"}))
    if key is not None:
        require(any(url.split("?")[0] == endpoint and method in methods
                    for endpoint, methods in allowed), "Typesense-doel buiten scope.")
    else:
        require(any(url == base + path and method == verb for base in APIS
                    for path, verb in (("/health", "GET"),
                                       (f"/api/v1/profile/{PROFILE}", "GET"),
                                       ("/api/v1/search", "POST"))),
                "API-doel buiten scope.")
    headers = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
    if key is not None:
        headers["X-TYPESENSE-API-KEY"] = key
    req = urllib.request.Request(url, data=canonical(body) if body is not None else None,
                                 headers=headers, method=method)
    # No environment proxy for requests carrying the local Typesense key.
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    try:
        with opener.open(req, timeout=35) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        hint = ("authenticatie/rechten geweigerd" if exc.code in (401, 403)
                else "HTTP-aanvraag mislukt")
        raise Blocked(f"{method}: {hint} (HTTP {exc.code}); responsinhoud verborgen.") from None
    except (urllib.error.URLError, TimeoutError):
        raise Blocked(f"{method}: verbinding/TLS/time-out; geen automatische write-retry.") from None
    except (ValueError, UnicodeError):
        raise Blocked("Geen geldige JSON-respons; inhoud verborgen.") from None


def container_key():
    try:
        result = subprocess.run(["docker", "inspect", CONTAINER], capture_output=True,
                                text=True, timeout=20, check=False)
        require(result.returncode == 0, "docker inspect mislukt; controleer sudo/container.")
        data = json.loads(result.stdout)
        require(len(data) == 1 and data[0]["State"]["Running"], "API-container draait niet.")
        env = dict(item.split("=", 1) for item in data[0]["Config"]["Env"] if "=" in item)
        require(env.get("TYPESENSE_COLLECTION") == INDEX, "Container gebruikt andere index.")
        key = env.get("TYPESENSE_API_KEY")
        require(isinstance(key, str) and bool(key), "Typesense-sleutel ontbreekt in container.")
        return key
    except Blocked:
        raise
    except Exception:
        raise Blocked("Containerconfiguratie niet leesbaar; details verborgen.") from None


class Live:
    def __init__(self):
        self.key = container_key()

    def schema(self):
        return request_json(TS + f"/collections/{INDEX}", key=self.key)

    def document(self):
        return request_json(TS + DOC_PATH, key=self.key)

    def patch(self, value):
        return request_json(TS + DOC_PATH + "?dirty_values=reject", method="PATCH",
                            body={FIELD: value}, key=self.key)

    def api(self, base, path, body=None):
        return request_json(base + path, method="POST" if body is not None else "GET",
                            body=body)


def validate_document(doc):
    require(doc.get("id") == DOC_ID and doc.get("sku") == SKU
            and doc.get("sku_exact") == SKU
            and doc.get("shopify_product_id") == "gid://shopify/Product/" + DOC_ID,
            "Documentidentiteit/SKU wijkt af.")
    require(set(doc.get("collection_handles", [])) == set(COLLECTIONS)
            and set(doc.get("collection_ids", [])) == set(COLLECTIONS.values()),
            "Collecties wijken af van Shopify-readback 20 oktober; eerst opnieuw vergelijken.")
    require(FIELD not in doc or (type(doc[FIELD]) is int and 0 <= doc[FIELD] <= 2147483647),
            "Bestaande veldwaarde is geen herstelbaar optioneel int32.")


def validate_schema(schema):
    require(schema.get("name") == INDEX, "Schema hoort bij een andere index.")
    fields = [f for f in schema.get("fields", []) if f.get("name") == FIELD]
    require(len(fields) == 1, "Kraangatenveld ontbreekt of is dubbel in schema.")
    field = fields[0]
    require(field.get("type") == "int32" and field.get("optional") is True
            and field.get("facet") is True and field.get("index", True) is True
            and field.get("store", True) is True, "Kraangatenveld heeft afwijkend schema.")
    return field


def validate_api(api):
    for base in APIS:
        health = api.api(base, "/health")
        require(health.get("ok") is True and health.get("typesense_collection") == INDEX
                and health.get("service") == CONTAINER, "API-health/index wijkt af.")
        profile = api.api(base, f"/api/v1/profile/{PROFILE}")
        fields = [f for f in profile.get("filters", []) if f.get("field") == FIELD]
        require(len(fields) == 1 and fields[0].get("type") == "number_decimal"
                and fields[0].get("data_type") == "int32", "API-bereikfilter wijkt af.")


def search_checks(api, value):
    evidence = {}
    for base in APIS:
        cases = {}
        for holes in (None, 1, 2):
            body = {"collection": PROFILE, "q": SKU, "page": 1, "per_page": 24,
                    "sort": "relevance", "filters": {},
                    "ranges": {} if holes is None else {FIELD: {"min": holes, "max": holes}}}
            result = api.api(base, "/api/v1/search", body)
            expected = holes is None or value == holes
            products = result.get("products", [])
            wanted = [DOC_ID] if expected else []
            require(result.get("exact_sku") is True
                    and result.get("collection", {}).get("handle") == PROFILE
                    and result.get("found") == len(wanted)
                    and [p.get("id") for p in products] == wanted
                    and all(p.get("sku") == SKU for p in products),
                    f"Filtercontrole mislukt: {'publiek' if base.startswith('https') else 'lokaal'}, "
                    f"{'zonder bereik' if holes is None else str(holes) + ' kraangat(en)'}.")
            cases["baseline" if holes is None else str(holes)] = {
                "found": result["found"], "ids": wanted, "passed": True}
        evidence["public" if base.startswith("https") else "local"] = cases
    return evidence


def load_backup(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    payload = data["payload"]
    require(data.get("sha256") == digest(payload), "Back-upchecksum klopt niet.")
    require(payload.get("index") == INDEX and payload.get("document_id") == DOC_ID
            and payload.get("field") == FIELD, "Back-up valt buiten scope.")
    validate_document(payload["original"])
    require(payload["original"].get(FIELD) != 1, "Back-up bevat geen oorspronkelijke correctie.")
    return payload


def save_backup(path, original, schema, checks):
    payload = {"created_at": now(), "index": INDEX, "document_id": DOC_ID,
               "field": FIELD, "original": copy.deepcopy(original),
               "schema": schema, "checks_before": checks,
               "patch": {FIELD: 1},
               "note": "Documentchecksum; geen Shopify-manifesthash."}
    if path.exists():
        existing = load_backup(path)
        require(same(existing["original"], original), "Bestaande back-up wijkt af; niet overschreven.")
        return existing
    fd = os.open(str(path), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "wb") as stream:
        stream.write(canonical({"sha256": digest(payload), "payload": payload}) + b"\n")
        stream.flush()
        os.fsync(stream.fileno())
    if os.name == "posix":
        directory_fd = os.open(str(path.parent), os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    return load_backup(path)


def restore(api, payload):
    original = payload["original"]
    expected = {**original, FIELD: 1}
    current = api.document()
    require(same(current, original) or same(current, expected),
            "Rollbackconflict: document intussen gewijzigd; geen herstelwrite uitgevoerd.")
    if not same(current, original):
        # null removes the optional field when it was originally absent.
        api.patch(original.get(FIELD))
    require(same(api.document(), original), "Rollback-readback wijkt af van volledige back-up.")
    return search_checks(api, original.get(FIELD))


def execute(api, mode, path):
    schema = api.schema()
    field_schema = validate_schema(schema)
    original = api.document()
    validate_document(original)
    validate_api(api)
    if mode == "rollback":
        payload = load_backup(path)
        checks = restore(api, payload)
        return {"status": "ROLLED_BACK_VERIFIED", "checks": checks}
    before = search_checks(api, original.get(FIELD))
    if mode == "inspect":
        return {"status": "READ_ONLY", "field_schema": field_schema,
                "field_present": FIELD in original, "value": original.get(FIELD),
                "collection_handles": original["collection_handles"], "checks": before}
    if mode == "verify":
        require(original.get(FIELD) == 1, "Correctie nog niet aanwezig: kraangaten is niet 1.")
        if path.exists():
            saved = load_backup(path)
            require(same(original, {**saved["original"], FIELD: 1}),
                    "Verificatie: andere documentvelden verschillen van de back-up.")
        return {"status": "VERIFIED", "checks": before}
    if original.get(FIELD) == 1:
        # Verify the entire document when retrying this particular backup.
        if path.exists():
            saved = load_backup(path)
            require(same(original, {**saved["original"], FIELD: 1}),
                    "Reeds gecorrigeerd maar andere velden gewijzigd; inspecteer eerst.")
        return {"status": "ALREADY_CORRECT_VERIFIED", "checks": before}
    payload = save_backup(path, original, schema, before)
    # No atomic compare-and-swap in this endpoint. Only PATCH this one field;
    # refuse a detected concurrent change and verify the complete document.
    require(same(api.document(), original), "Document wijzigde na back-up; geen write uitgevoerd.")
    try:
        api.patch(1)
        require(same(api.document(), {**original, FIELD: 1}),
                "Readback wijkt af: overige velden niet aantoonbaar behouden.")
        checks = search_checks(api, 1)
        require(same(api.document(), {**original, FIELD: 1}),
                "Document wijzigde tijdens filtercontroles.")
    except Exception as failure:
        reason = str(failure) if isinstance(failure, Blocked) else type(failure).__name__
        try:
            restore(api, payload)
        except Exception:
            raise Blocked(reason + " Automatisch herstel NIET bevestigd. "
                          "Bewaar back-up en voer inspect uit; niet blind opnieuw toepassen.") from None
        raise Blocked(reason + " Oorspronkelijke document en filters "
                      "zijn gecontroleerd hersteld.") from None
    return {"status": "APPLIED_VERIFIED", "changed_fields": [FIELD], "checks": checks}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("inspect", "apply", "verify", "rollback"))
    parser.add_argument("--backup", default=str(DEFAULT_BACKUP))
    args = parser.parse_args()
    report = {"time": now(), "index": INDEX, "document_id": DOC_ID, "sku": SKU,
              "mode": args.mode, "status": "BLOCKED"}
    try:
        require(os.name == "posix" and os.geteuid() == 0, "Voer dit script op de VPS uit met sudo.")
        import fcntl
        os.umask(0o077)
        BACKUP_ROOT.mkdir(mode=0o700, parents=True, exist_ok=True)
        require(not BACKUP_ROOT.is_symlink() and BACKUP_ROOT.stat().st_uid == 0
                and BACKUP_ROOT.stat().st_mode & 0o077 == 0, "Back-upmap moet root-owned en 0700 zijn.")
        path = Path(args.backup)
        require(path.is_absolute() and path.parent == BACKUP_ROOT and not path.is_symlink(),
                "Back-up moet een gewoon bestand in de vaste back-upmap zijn.")
        if path.exists():
            require(path.is_file() and path.stat().st_uid == 0
                    and path.stat().st_mode & 0o077 == 0, "Back-up moet root-owned en 0600 zijn.")
        report["backup"] = str(path)
        lock_fd = os.open(str(BACKUP_ROOT / ".lock"),
                          os.O_WRONLY | os.O_CREAT | os.O_NOFOLLOW, 0o600)
        with os.fdopen(lock_fd, "w") as lock:
            try:
                fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise Blocked("Een andere uitvoering van dit correctiescript is actief.") from None
            report.update(execute(Live(), args.mode, path))
    except Blocked as exc:
        report["reason"] = str(exc)
    except Exception as exc:
        report["reason"] = "Onverwachte fout (" + type(exc).__name__ + "); details verborgen."
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 2 if report["status"] == "BLOCKED" else 0


if __name__ == "__main__":
    sys.exit(main())
