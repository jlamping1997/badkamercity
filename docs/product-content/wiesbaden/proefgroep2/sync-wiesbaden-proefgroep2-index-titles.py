#!/usr/bin/env python3
"""Bounded Wiesbaden title sync: seven existing Typesense documents only.

Run on the existing VPS with sudo. No Shopify writes, import, schema changes,
service restarts, credential output, or changes to any field other than title.
The embedded plan is fixed to the verified 2026-10-20 Shopify readback.
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
CONTAINER = "badkamercity-filter-api-verified-candidate"
TS = "http://127.0.0.1:8108"
APIS = ("http://127.0.0.1:8082", "https://vps-7ffd625d.vps.ovh.net/verified")
BACKUP_ROOT = Path("/var/backups/badkamercity-wiesbaden-proefgroep2")
BACKUP = BACKUP_ROOT / "index-titles-20261020.json"
PLAN = [{'sku': '20.3755', 'id': '10657252147466', 'old_title': 'Wiesbaden Graffic inloopdouche 800 x 2000 x 10 mm nano safety glass folie helder glas/chroom', 'title': 'Wiesbaden Graffic inloopdouche 80 × 200 cm – helder glas/chroom', 'collections': ['douches', 'douchewanden', 'inloopdouches'], 'profile': 'inloopdouches', 'q': 'Graffic inloopdouche 80'}, {'sku': '20.3756', 'id': '10657273643274', 'old_title': 'Wiesbaden Graffic inloopdouche 900 x 2000 x 10 mm nano safety glass folie helder glas/chroom', 'title': 'Wiesbaden Graffic inloopdouche 90 × 200 cm – helder glas/chroom', 'collections': ['douches', 'douchewanden', 'inloopdouches'], 'profile': 'inloopdouches', 'q': 'Graffic inloopdouche 90'}, {'sku': '32.3411', 'id': '10657255489802', 'old_title': 'Wiesbaden Barco waskom ovaal 40 x 33 x 14,5 cm keramiek glans wit', 'title': 'Wiesbaden Barco ovale waskom 40 × 33 cm – glans wit', 'collections': ['opzetwastafels', 'wastafels'], 'profile': 'opzetwastafels', 'q': 'Barco ovale waskom'}, {'sku': '32.3594', 'id': '10657255653642', 'old_title': 'Wiesbaden one-pack Porta fontein + Metro kraan', 'title': 'Wiesbaden Porta fonteinset met Metro kraan', 'collections': ['fonteinen', 'fonteinsets', 'toiletten', 'wastafels'], 'profile': 'fonteinsets', 'q': 'Porta fonteinset'}, {'sku': '32.2510', 'id': '10657255686410', 'old_title': 'Wiesbaden Vesta Tornado flush wandcloset rimless met nano coating met Shade slim toiletzitting softclose en quick release glans wit', 'title': 'Wiesbaden Vesta Tornado hangtoilet met Shade Slim zitting – glans wit', 'collections': ['hangtoiletten', 'toilet-zonder-spoelrand', 'toiletten'], 'profile': 'hangtoiletten', 'q': 'Vesta Tornado hangtoilet'}, {'sku': '32.3670', 'id': '10657255751946', 'old_title': 'Wiesbaden Marmaris onderkast met 2 laden 60 x 45 cm mat zwart', 'title': 'Wiesbaden Marmaris onderkast 60 cm met 2 laden – mat zwart', 'collections': ['badkamermeubels', 'losse-onderkasten'], 'profile': 'losse-onderkasten', 'q': 'Marmaris onderkast 60'}, {'sku': '38.4125', 'id': '10657255817482', 'old_title': 'Wiesbaden Ambi one spiegel rechthoek met LED, dimbaar en spiegelverwarming 140 x 60 cm', 'title': 'Wiesbaden Ambi One LED-spiegel 140 × 60 cm met verwarming', 'collections': ['badkamermeubels', 'badkamerspiegels', 'rechthoekige-spiegels', 'spiegels-en-spiegelkasten', 'spiegels-met-verlichting', 'spiegels-met-verwarming'], 'profile': 'spiegels-met-verlichting', 'q': 'Ambi One LED spiegel'}]


class Blocked(Exception):
    pass


def require(condition, message):
    if not condition:
        raise Blocked(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")


def same(left, right):
    return canonical(left) == canonical(right)


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        raise Blocked("Redirect geweigerd; geen sleutel naar een ander doel sturen.")


def request_json(url, method="GET", body=None, key=None):
    if key is not None:
        clean = url.split("?")[0]
        schema = TS + "/collections/" + INDEX
        doc_paths = {schema + "/documents/" + item["id"] for item in PLAN}
        require((clean == schema and method == "GET") or
                (clean in doc_paths and method in ("GET", "PATCH")), "Doel buiten scope.")
        if method == "PATCH":
            require(isinstance(body, dict) and set(body) == {"title"}
                    and isinstance(body["title"], str), "Alleen titel-PATCH toegestaan.")
    else:
        require(any(url == base + path and method == verb for base in APIS
                    for path, verb in (("/health", "GET"), ("/api/v1/search", "POST"))),
                "API-doel buiten scope.")
    headers = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
    if key is not None:
        headers["X-TYPESENSE-API-KEY"] = key
    req = urllib.request.Request(url, data=None if body is None else canonical(body),
                                 method=method, headers=headers)
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    try:
        with opener.open(req, timeout=35) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        raise Blocked(f"HTTP {exc.code}; responsdetails verborgen, geen write-retry.") from None
    except (urllib.error.URLError, TimeoutError, OSError):
        raise Blocked("Verbinding/time-out; geen automatische write-retry.") from None
    except (ValueError, UnicodeError):
        raise Blocked("Ongeldige JSON-respons; details verborgen.") from None


class Live:
    def __init__(self):
        try:
            result = subprocess.run(["docker", "inspect", CONTAINER], capture_output=True,
                                    text=True, timeout=20, check=False)
            require(result.returncode == 0, "Container niet leesbaar; controleer sudo.")
            data = json.loads(result.stdout)
            require(len(data) == 1 and data[0]["State"]["Running"], "Container draait niet.")
            env = dict(value.split("=", 1) for value in data[0]["Config"]["Env"] if "=" in value)
            require(env.get("TYPESENSE_COLLECTION") == INDEX, "Actieve index wijkt af.")
            self.key = env.get("TYPESENSE_API_KEY")
            require(isinstance(self.key, str) and self.key, "Bestaande sleutel ontbreekt.")
        except Blocked:
            raise
        except Exception:
            raise Blocked("Containerconfiguratie onleesbaar; details verborgen.") from None

    def schema(self):
        return request_json(TS + "/collections/" + INDEX, key=self.key)

    def document(self, item):
        return request_json(TS + "/collections/" + INDEX + "/documents/" + item["id"], key=self.key)

    def patch(self, item, title):
        return request_json(TS + "/collections/" + INDEX + "/documents/" + item["id"]
                            + "?dirty_values=reject", method="PATCH", body={"title": title}, key=self.key)

    def api(self, base, path, body=None):
        return request_json(base + path, method="GET" if body is None else "POST", body=body)


def validate_identity(item, doc):
    require(doc.get("id") == item["id"] and doc.get("sku") == item["sku"]
            and doc.get("sku_exact") == item["sku"]
            and doc.get("shopify_product_id") == "gid://shopify/Product/" + item["id"],
            "Productidentiteit wijkt af: " + item["sku"])
    require(sorted(doc.get("collection_handles", [])) == item["collections"],
            "Collecties gewijzigd; eerst Shopify vergelijken: " + item["sku"])
    require(doc.get("title") in (item["old_title"], item["title"]),
            "Titel gewijzigd sinds broncontrole: " + item["sku"])


def preflight(api):
    schema = api.schema()
    fields = [f for f in schema.get("fields", []) if f.get("name") == "title"]
    require(schema.get("name") == INDEX and len(fields) == 1
            and fields[0].get("type") == "string" and fields[0].get("index", True)
            and fields[0].get("store", True), "Titelschema wijkt af.")
    for base in APIS:
        health = api.api(base, "/health")
        require(health.get("ok") is True and health.get("typesense_collection") == INDEX
                and health.get("service") == CONTAINER, "API-index/service wijkt af.")
    docs = {item["id"]: api.document(item) for item in PLAN}
    for item in PLAN:
        validate_identity(item, docs[item["id"]])
    return docs


def backup_payload(documents):
    return {"index": INDEX, "created_at": now(), "plan": PLAN, "originals": documents}


def validate_backup(data):
    payload = data["payload"]
    require(data.get("sha256") == hashlib.sha256(canonical(payload)).hexdigest(), "Back-upchecksum wijkt af.")
    require(payload.get("index") == INDEX and same(payload.get("plan"), PLAN), "Back-upscope wijkt af.")
    require(set(payload["originals"]) == {item["id"] for item in PLAN}, "Back-up is onvolledig.")
    for item in PLAN:
        doc = payload["originals"][item["id"]]
        validate_identity(item, doc)
        require(doc["title"] == item["old_title"], "Back-up bevat geen oorspronkelijke titel.")
    return payload


def load_backup():
    return validate_backup(json.loads(BACKUP.read_text(encoding="utf-8")))


def save_backup(documents):
    if BACKUP.exists():
        return load_backup()
    for item in PLAN:
        require(documents[item["id"]]["title"] == item["old_title"],
                "Nieuwe titel zonder bestaande herstelkopie; inspecteer handmatig.")
    payload = backup_payload(copy.deepcopy(documents))
    data = {"payload": payload, "sha256": hashlib.sha256(canonical(payload)).hexdigest()}
    validate_backup(data)
    BACKUP_ROOT.mkdir(mode=0o700, parents=True, exist_ok=True)
    require(not BACKUP_ROOT.is_symlink() and BACKUP_ROOT.stat().st_mode & 0o077 == 0,
            "Back-upmap moet privé zijn (0700).")
    fd = os.open(str(BACKUP), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "wb") as stream:
        stream.write(canonical(data) + b"\n")
        stream.flush()
        os.fsync(stream.fileno())
    directory_fd = os.open(str(BACKUP_ROOT), os.O_RDONLY)
    try:
        os.fsync(directory_fd)
    finally:
        os.close(directory_fd)
    return load_backup()


def expected_doc(original, item):
    return {**original, "title": item["title"]}


def check_concurrency(api, payload):
    for item in PLAN:
        original = payload["originals"][item["id"]]
        current = api.document(item)
        require(same(current, original) or same(current, expected_doc(original, item)),
                "Documentconflict; geen volgende write: " + item["sku"])


def search_checks(api, documents, text=False):
    results = []
    for base in APIS:
        for item in PLAN:
            for query in ([item["sku"], item["q"]] if text else [item["sku"]]):
                result = api.api(base, "/api/v1/search", {
                    "collection": item["profile"], "q": query, "page": 1,
                    "per_page": 24, "sort": "relevance", "filters": {}, "ranges": {}})
                matches = [p for p in result.get("products", []) if p.get("id") == item["id"]]
                require(len(matches) == 1 and matches[0].get("sku") == item["sku"]
                        and matches[0].get("title") == documents[item["id"]]["title"],
                        "Zoekcontrole mislukt: " + item["sku"])
                require(result.get("collection", {}).get("handle") == item["profile"], "Verkeerd zoekprofiel.")
                if query == item["sku"]:
                    require(result.get("exact_sku") is True and result.get("found") == 1,
                            "Exacte-SKU-controle mislukt: " + item["sku"])
                results.append({"api": "public" if base.startswith("https") else "local",
                                "sku": item["sku"], "q": query, "found": result.get("found"),
                                "product_on_page1": True})
    return results


def restore(api, payload):
    # Preflight every document first; never overwrite another writer's changes.
    check_concurrency(api, payload)
    for item in reversed(PLAN):
        original = payload["originals"][item["id"]]
        current = api.document(item)
        require(same(current, original) or same(current, expected_doc(original, item)),
                "Herstelconflict: " + item["sku"])
        if not same(current, original):
            api.patch(item, original["title"])
            require(same(api.document(item), original), "Herstelreadback mislukt: " + item["sku"])
    return search_checks(api, payload["originals"])


def execute(api, mode):
    documents = preflight(api)
    if mode == "inspect":
        checks = search_checks(api, documents)
        return {"status": "READ_ONLY", "checks": checks,
                "titles_current": sum(documents[i["id"]]["title"] == i["title"] for i in PLAN)}
    if mode == "verify":
        if BACKUP.exists():
            payload = load_backup()
            for item in PLAN:
                require(same(documents[item["id"]], expected_doc(payload["originals"][item["id"]], item)),
                        "Volledige readback wijkt af: " + item["sku"])
        else:
            for item in PLAN:
                require(documents[item["id"]]["title"] == item["title"], "Titel nog niet bijgewerkt.")
        return {"status": "VERIFIED", "checks": search_checks(api, documents, text=True),
                "full_document_compared_to_backup": BACKUP.exists()}
    if mode == "restore":
        return {"status": "RESTORED_VERIFIED", "checks": restore(api, load_backup())}
    # All seven before-states and API identities are checked before the first write.
    search_checks(api, documents)
    payload = save_backup(documents)
    check_concurrency(api, payload)
    try:
        for item in PLAN:
            original = payload["originals"][item["id"]]
            desired = expected_doc(original, item)
            current = api.document(item)
            require(same(current, original) or same(current, desired), "Conflict vóór PATCH: " + item["sku"])
            if not same(current, desired):
                api.patch(item, item["title"])
            require(same(api.document(item), desired), "Readback wijkt af: " + item["sku"])
        result = execute(api, "verify")
        result["status"] = "APPLIED_VERIFIED"
        return result
    except Exception:
        try:
            restore(api, payload)
        except Exception:
            raise Blocked("Toepassing niet voltooid; herstel niet bewezen. Bewaar back-up, inspecteer vóór verdergaan.") from None
        raise Blocked("Toepassing niet voltooid; oorspronkelijke titels hersteld en gecontroleerd.") from None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("inspect", "apply", "verify", "restore"))
    mode = parser.parse_args().mode
    try:
        result = execute(Live(), mode)
        print(json.dumps({"time": now(), "index": INDEX, "mode": mode,
                          "scope": [item["sku"] for item in PLAN], "only_mutated_field": "title",
                          "backup": str(BACKUP), **result}, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        message = str(exc) if isinstance(exc, Blocked) else "Onverwachte fout; details verborgen. Controleer herstelstatus."
        print(json.dumps({"status": "BLOCKED", "mode": mode, "reason": message}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    sys.exit(main())
