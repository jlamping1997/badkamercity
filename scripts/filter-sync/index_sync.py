#!/usr/bin/env python3
"""Read-only Shopify capture -> offline reconciliation -> isolated Typesense candidate.

No Shopify writes, no edits to existing Typesense collections/aliases, no API switch.
Python 3.10+ stdlib only. Private data and tokens must stay off public GitHub.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
import hashlib
import json
import os
from pathlib import Path
import re
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

SHOP = "fpa9hu-i3.myshopify.com"
GRAPHQL = f"https://{SHOP}/admin/api/2026-10/graphql.json"
TYPESENSE = "http://127.0.0.1:8108"
STAGE_PREFIX = "bc_wiesbaden_stage_"
QUERY = '''query($after:String){products(first:5,after:$after,query:"vendor:Wiesbaden AND status:active AND published_status:online_store_channel",sortKey:ID){
 nodes{id title vendor handle productType status updatedAt onlineStoreUrl
 featuredMedia{... on MediaImage{image{url}}}
 variants(first:3){nodes{sku price} pageInfo{hasNextPage}}
 collections(first:30){nodes{id handle} pageInfo{hasNextPage}}
 metafields(first:100){nodes{namespace key type value} pageInfo{hasNextPage}}
 } pageInfo{hasNextPage endCursor}}}'''


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def read_jsonl(path):
    with Path(path).open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def private_path(path):
    raw = Path(path).expanduser()
    if not raw.is_absolute():
        raise ValueError("Private output must have an absolute path")
    path = raw.resolve()
    if (str(path).startswith("/opt/badkamercity/") or
            any((parent / ".git").exists() for parent in (path.parent, *path.parents))):
        raise ValueError("Private output may not be written into a Git repository")
    return path


def write_private(path, content):
    path = private_path(path)
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC
    fd = os.open(path, flags, 0o600)
    os.fchmod(fd, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(content)


def request_json(url, *, method="GET", key=None, body=None, content_type="application/json", attempts=3):
    if not (url.startswith(GRAPHQL) or url.startswith(TYPESENSE + "/")):
        raise ValueError("Unexpected API URL")
    headers = {"Content-Type": content_type}
    if url.startswith(GRAPHQL):
        headers["X-Shopify-Access-Token"] = key
    else:
        headers["X-TYPESENSE-API-KEY"] = key
    for attempt in range(attempts):
        try:
            req = Request(url, data=body, method=method, headers=headers)
            with urlopen(req, timeout=40) as response:
                data = response.read(60_000_000)
            if content_type == "text/plain" or url.endswith("/documents/export"):
                return data.decode("utf-8")
            return json.loads(data)
        except HTTPError as error:
            if error.code not in (429, 500, 502, 503, 504) or attempt == attempts - 1:
                raise RuntimeError(f"{method} API HTTP {error.code}") from None
            time.sleep(min(16, 2 ** (attempt + 1)))
        except (URLError, TimeoutError):
            if attempt == attempts - 1:
                raise RuntimeError("API unreachable") from None
            time.sleep(min(16, 2 ** (attempt + 1)))


def capture(output):
    token = os.environ.get("SHOPIFY_ADMIN_ACCESS_TOKEN", "").strip()
    if not token:
        raise ValueError("SHOPIFY_ADMIN_ACCESS_TOKEN is not configured; no capture")
    rows, cursor, seen = [], None, set()
    while True:
        response = request_json(GRAPHQL, method="POST", key=token,
            body=canonical({"query": QUERY, "variables": {"after": cursor}}).encode())
        if response.get("errors"):
            raise RuntimeError("Shopify returned GraphQL errors; no snapshot accepted")
        connection = response.get("data", {}).get("products")
        if not isinstance(connection, dict):
            raise RuntimeError("Invalid Shopify product connection")
        for row in connection["nodes"]:
            if row["id"] in seen:
                raise RuntimeError("Duplicate Shopify product id while paginating")
            seen.add(row["id"])
            # Partial nested connections can silently lose collections, variants or facts.
            for name in ("variants", "collections", "metafields"):
                if row[name]["pageInfo"]["hasNextPage"]:
                    raise RuntimeError(f"Truncated {name} for product {row['id']}")
            rows.append(row)
        page = connection["pageInfo"]
        if not page["hasNextPage"]:
            break
        if not page.get("endCursor") or page["endCursor"] == cursor:
            raise RuntimeError("Shopify cursor failed to advance")
        cursor = page["endCursor"]
    if not rows:
        raise RuntimeError("Shopify snapshot is empty")
    write_private(output, "".join(canonical(row) + "\n" for row in rows))
    print(canonical({"status": "SHOPIFY_CAPTURE_COMPLETE", "products": len(rows),
                     "output": str(output), "shopify_mutations": 0}))


def cents(amount):
    try:
        value = Decimal(str(amount))
        if not value.is_finite() or value <= 0 or value.as_tuple().exponent < -2:
            raise ValueError()
        return int(value * 100)
    except (InvalidOperation, TypeError, ValueError):
        raise ValueError("Invalid positive two-decimal consumer price") from None


def typed(value, kind):
    if kind == "bool":
        if value is True or value == "true": return True
        if value is False or value == "false": return False
        raise ValueError("Invalid boolean")
    if kind in ("int32", "int64"):
        if isinstance(value, bool): raise ValueError("Invalid integer")
        val = Decimal(str(value))
        if not val.is_finite() or val != val.to_integral_value(): raise ValueError("Invalid integer")
        return int(val)
    if kind == "float":
        val = Decimal(str(value))
        if not val.is_finite(): raise ValueError("Invalid float")
        return float(val)
    if kind in ("string", "string[]"):
        if kind == "string[]":
            if not isinstance(value, list) or not all(isinstance(x, str) for x in value):
                raise ValueError("Invalid string array")
            return value
        if not isinstance(value, str) or not value.strip(): raise ValueError("Invalid string")
        return value.strip()
    raise ValueError("Unsupported field type")


def product_to_doc(row, old, policy, schema_types, issues):
    pid = row["id"].rsplit("/", 1)[-1]
    variant = row["variants"]["nodes"]
    if len(variant) != 1 or not variant[0].get("sku"):
        raise ValueError(f"Unsupported multiple/missing variants for product {pid}")
    sku = variant[0]["sku"].strip()
    if row["status"] != "ACTIVE" or not row.get("onlineStoreUrl") or row["vendor"].casefold() != "wiesbaden":
        raise ValueError(f"Unexpected status/publication/vendor for product {pid}")
    if old and old["sku"] != sku:
        raise ValueError(f"SKU changed for product {pid}; manual identity review needed")
    product_type = row["productType"].strip()
    shopping = old["general_shopping"] if old else policy.get(product_type)
    if type(shopping) is not bool:
        raise ValueError(f"No unambiguous service classification for new product type {product_type!r}")
    fields = dict(old) if old else {}
    fields.update({"id": pid, "shopify_product_id": pid, "sku": sku,
        "sku_exact": sku.casefold(), "title": row["title"], "handle": row["handle"],
        "vendor": row["vendor"], "product_type": product_type,
        "source_productsoort": product_type, "source_updated_at": row["updatedAt"],
        "url": row["onlineStoreUrl"], "image_url": ((row.get("featuredMedia") or {}).get("image") or {}).get("url") or "",
        "price_cents": cents(variant[0]["price"]), "published": True,
        "general_shopping": shopping,
        "collection_handles": sorted({x["handle"] for x in row["collections"]["nodes"]}),
        "collection_ids": sorted({x["id"].rsplit("/", 1)[-1] for x in row["collections"]["nodes"]})})
    # The October 12 verified manifest is a per-product canonical value source;
    # later independently reviewed bc_filters fields take priority when present.
    metas = {(m["namespace"], m["key"]): m for m in row["metafields"]["nodes"]}
    values = {}
    manifest = metas.get(("bc_data", "filter_manifest"))
    if manifest:
        try:
            parsed = json.loads(manifest["value"])
            if parsed.get("sku") != sku or not isinstance(parsed.get("values"), dict):
                raise ValueError("Unexpected filter manifest SKU/values")
            values.update(parsed["values"])
        except (ValueError, TypeError):
            raise ValueError(f"Invalid canonical filter manifest for {pid}") from None
    for (namespace, key), meta in metas.items():
        if namespace == "bc_filters":
            values[key] = meta["value"]
    for key, raw in values.items():
        field = "f_" + key
        if field not in schema_types:
            issues.add(key)
            continue  # A new Typesense schema mapping needs separate approval.
        try:
            fields[field] = typed(raw, schema_types[field])
        except (ValueError, InvalidOperation):
            raise ValueError(f"Invalid typed filter {field} for product {pid}") from None
    if not old and "f_productsoort" in schema_types and "f_productsoort" not in fields and product_type:
        fields["f_productsoort"] = product_type  # Explicit Shopify productType, not inferred from title.
    return {k: v for k, v in fields.items() if k in schema_types and v is not None}


def build(base, snapshot, schema, profiles, output):
    base_docs = read_jsonl(base)
    shop_rows = read_jsonl(snapshot)
    schema_doc = json.loads(Path(schema).read_text())
    profile_doc = json.loads(Path(profiles).read_text())
    types = {f["name"]: f["type"] for f in schema_doc["fields"]}
    old_by_id = {str(x["id"]): x for x in base_docs if x.get("vendor", "").casefold() == "wiesbaden"}
    if len({str(d["id"]) for d in base_docs}) != len(base_docs):
        raise ValueError("Duplicate IDs in original index")
    if len(old_by_id) != sum(d.get("vendor", "").casefold() == "wiesbaden" for d in base_docs):
        raise ValueError("Duplicate Wiesbaden IDs in original index")
    # Classify new product types only when all existing exact-type items agree.
    observed = defaultdict(set)
    for d in old_by_id.values():
        observed[d["product_type"]].add(d["general_shopping"])
    policy = {k: next(iter(v)) for k, v in observed.items() if len(v) == 1}
    existing = {str(d["id"]): d for d in base_docs if d.get("vendor", "").casefold() != "wiesbaden"}
    issues, updated, seen_skus, ids = set(), {}, set(), set()
    for row in shop_rows:
        pid = row["id"].rsplit("/", 1)[-1]
        if pid in ids:
            raise ValueError("Duplicate Shopify product IDs")
        ids.add(pid)
        if row["vendor"].casefold() != "wiesbaden":
            raise ValueError("Snapshot contains a different vendor")
        doc = product_to_doc(row, old_by_id.get(pid), policy, types, issues)
        if doc["sku"] in seen_skus:
            raise ValueError("Duplicate Wiesbaden SKUs")
        seen_skus.add(doc["sku"])
        updated[pid] = doc
    if not old_by_id.keys() <= updated.keys():
        raise ValueError("Existing Wiesbaden IDs missing from Shopify snapshot; stop instead of deleting")
    if not ids.isdisjoint(existing):
        raise ValueError("New Shopify id collides with non-Wiesbaden index record")
    docs = sorted([*existing.values(), *updated.values()], key=lambda d: (d["vendor"], d["id"]))
    raw = "".join(canonical(d) + "\n" for d in docs)
    digest = hashlib.sha256(raw.encode()).hexdigest()
    schema_doc["name"] = STAGE_PREFIX + digest[:12]
    schema_doc.setdefault("metadata", {}).update({"payload_sha256": digest, "product_count": len(docs)})
    for handle, profile in profile_doc.items():
        subset = docs if handle == "__all__" else [d for d in docs if handle in d.get("collection_handles", [])]
        profile["products"] = sum(d.get("published") is True for d in subset)
        profile["shopping_products"] = sum(d.get("published") is True and d.get("general_shopping") is True for d in subset)
        # Never alter allowed_filters or visible filters without a separate tested release.
    out = private_path(output)
    out.mkdir(parents=True, exist_ok=True, mode=0o700)
    report = {"status": "CANDIDATE_FILES_PREPARED_ONLY", "shopify_wiesbaden": len(updated),
              "old_wiesbaden": len(old_by_id), "new_wiesbaden": len(updated) - len(old_by_id),
              "candidate_documents": len(docs), "schema": schema_doc["name"],
              "unmapped_filter_keys": sorted(issues), "profiles": len(profile_doc),
              "shopify_mutations": 0, "typesense_mutations": 0, "live_api_switched": False}
    write_private(out / "documents.jsonl", raw)
    write_private(out / "schema.json", canonical(schema_doc) + "\n")
    write_private(out / "profiles.json", canonical(profile_doc) + "\n")
    write_private(out / "report.json", canonical(report) + "\n")
    print(canonical(report))
    return report


def stage(folder):
    token = os.environ.get("TYPESENSE_API_KEY", "").strip()
    if not token:
        raise ValueError("TYPESENSE_API_KEY is not configured; no stage")
    folder = Path(folder)
    schema = json.loads((folder / "schema.json").read_text())
    docs = read_jsonl(folder / "documents.jsonl")
    name = schema["name"]
    if not re.fullmatch(r"bc_wiesbaden_stage_[0-9a-f]{12}", name):
        raise ValueError("Unsafe candidate name")
    payload = "".join(canonical(d) + "\n" for d in docs).encode()
    if schema["metadata"]["payload_sha256"] != hashlib.sha256(payload).hexdigest():
        raise ValueError("Candidate data hash mismatch; no writes")
    if schema["metadata"]["product_count"] != len(docs):
        raise ValueError("Candidate count mismatch; no writes")
    collection_url = TYPESENSE + "/collections/" + quote(name)
    try:
        request_json(collection_url, key=token)
    except RuntimeError as e:
        if "HTTP 404" not in str(e): raise
    else:
        raise ValueError("Candidate collection already exists; refusing to overwrite")
    request_json(TYPESENSE + "/collections", method="POST", key=token, body=canonical(schema).encode())
    for offset in range(0, len(docs), 200):
        block = docs[offset:offset + 200]
        raw = "".join(canonical(d) + "\n" for d in block).encode()
        response = request_json(collection_url + "/documents/import?action=create&dirty_values=reject",
                                method="POST", key=token, body=raw, content_type="text/plain", attempts=1)
        receipts = [json.loads(line) for line in response.splitlines() if line.strip()]
        if len(receipts) != len(block) or any(row.get("success") is not True for row in receipts):
            raise RuntimeError("Partial Typesense import; candidate remains isolated; no switch")
    current = request_json(collection_url, key=token)
    if current.get("num_documents") != len(docs):
        raise RuntimeError("Candidate document count mismatch; no switch")
    # Export readback catches partial writes and wrong prices or facet fields.
    exported = request_json(collection_url + "/documents/export", key=token, content_type="text/plain")
    saved = {str(d["id"]): d for d in (json.loads(x) for x in exported.splitlines() if x.strip())}
    expected = {str(d["id"]): d for d in docs}
    if set(saved) != set(expected) or any(saved[pid] != d for pid, d in expected.items()):
        raise RuntimeError("Candidate readback differs from input; no switch")
    print(canonical({"status": "ISOLATED_CANDIDATE_VERIFIED", "collection": name,
                     "documents": len(docs), "live_api_switched": False, "aliases_changed": False}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="mode", required=True)
    cap = sub.add_parser("capture", help="Read Wiesbaden via Shopify Admin, no writes")
    cap.add_argument("--out", type=Path, required=True)
    prep = sub.add_parser("prepare", help="Build private candidate JSONL + profiles offline")
    for name in ("base", "snapshot", "schema", "profiles", "out"):
        prep.add_argument("--" + name, type=Path, required=True)
    st = sub.add_parser("stage", help="Create NEW Typesense collection only; never switch API")
    st.add_argument("--folder", type=Path, required=True)
    args = parser.parse_args()
    if args.mode == "capture": capture(args.out)
    elif args.mode == "prepare": build(args.base, args.snapshot, args.schema, args.profiles, args.out)
    else: stage(args.folder)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Do not print exception payloads, tokens, URLs containing customer data, or raw documents.
        print(canonical({"status": "STOP", "reason": type(e).__name__, "message": str(e)[:160]}))
        raise SystemExit(2) from None
