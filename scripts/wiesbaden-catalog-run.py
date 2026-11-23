#!/usr/bin/env python3
"""Prepare private Wiesbaden price deltas and missing-SKU candidates; never connect.

Python 3.10+, standard library only. Reuses the existing datarun's exact textual
SKU and atomic-JSON conventions. This complements its content/category proposals;
it does not replace them or emit an executable Shopify productSet payload.

Example: --csv supplier.csv --price-basis incl --price-evidence 'contract reference'
         --snapshot shop.json --output /private/run
Snapshot: {pagination_complete: true, products: [...]} with product.vendor and
variants (list or nodes/edges). A productVariants connection with nested product
is also accepted. Completeness must be explicitly asserted by the snapshot owner.
Only matched variant prices are proposed for updates; existing content is kept.
All output, snapshots and supplier files must remain outside the public repository.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import tempfile
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from urllib.parse import urlsplit

VERSION = "2026-10-21.1"
PRICE_COLUMN = "advertentieprijs (excl. btw)"
BRAND = "Wiesbaden"


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def sku_key(value):
    # Never convert to number, strip punctuation, infer from title, or use EAN.
    if not isinstance(value, str):
        raise ValueError("SKU must be a string; numeric conversion may have lost zeros")
    return value.strip()


def money(value):
    if not isinstance(value, (str, Decimal)):
        return None
    text = str(value).strip()
    if not re.fullmatch(r"[0-9]+(?:[.,][0-9]+)?", text):
        return None
    try:
        amount = Decimal(text.replace(",", "."))
        return amount if amount.is_finite() and amount > 0 else None
    except InvalidOperation:
        return None


def sale_price(value, basis):
    if basis not in ("incl", "ex"):
        raise ValueError("Explicit price basis incl or ex is required")
    amount = money(value)
    if amount is None:
        return None
    exact = amount * (Decimal("1.21") if basis == "ex" else Decimal("1"))
    rounded = exact.quantize(Decimal("1") if exact > 100 else Decimal("0.01"), rounding=ROUND_HALF_UP)
    return format(rounded, ".2f") if rounded > 0 else None


def media_urls(row):
    result = []
    for name in ("main_image", "afbeeldingscode", "gallery", "afbeeldingscode_2", "afbeeldingscode_3", "afbeeldingscode_4"):
        for url in (row.get(name) or "").split(";"):
            url = url.strip()
            parsed = urlsplit(url)
            if parsed.scheme in ("https", "http") and parsed.netloc and url not in result:
                result.append(url)
    return result


def nodes(value):
    if isinstance(value, list):
        return value
    if isinstance(value, dict) and "nodes" in value:
        return value["nodes"]
    if isinstance(value, dict) and "edges" in value:
        return [x["node"] for x in value["edges"]]
    raise ValueError("Expected a list or a nodes/edges connection")


def snapshot_index(snapshot):
    index = defaultdict(list)
    if snapshot is None:
        return index, False
    data = snapshot.get("data", snapshot)
    if "products" in data:
        variants = [(p, v) for p in nodes(data["products"]) for v in nodes(p.get("variants", []))]
    elif "productVariants" in data:
        variants = [(v["product"], v) for v in nodes(data["productVariants"])]
    else:
        raise ValueError("Snapshot requires products or productVariants")
    for product, variant in variants:
        sku = sku_key(variant.get("sku", ""))
        if not sku:
            continue
        index[sku].append({"product_id": product.get("id"), "variant_id": variant.get("id"),
                           "vendor": product.get("vendor", ""), "price": variant.get("price"),
                           "status": product.get("status"), "publishedAt": product.get("publishedAt")})
    return index, snapshot.get("pagination_complete") is True


def prepare(rows, source_sha, basis, evidence, snapshot=None, snapshot_sha=None):
    if basis not in ("incl", "ex") or not evidence.strip():
        raise ValueError("Explicit price basis and its evidence are required; header is not evidence")
    selected = [r for r in rows if (r.get("merk") or "").strip().casefold() == BRAND.casefold()]
    duplicate = Counter(sku_key(r.get("productcode", "")) for r in selected)
    index, complete = snapshot_index(snapshot)
    items = []
    for row in selected:
        sku = sku_key(row.get("productcode", ""))
        price = sale_price(row.get(PRICE_COLUMN, ""), basis)
        matches = [v for v in index.get(sku, []) if (v["vendor"] or "").strip().casefold() == BRAND.casefold()]
        item = {"sku": sku, "status": "UNMATCHED_UNVERIFIED", "changes": {}, "issues": []}
        if not sku or duplicate[sku] != 1:
            item["status"] = "BLOCKED_SOURCE_IDENTITY"
        elif len(matches) > 1:
            item["status"] = "BLOCKED_DUPLICATE_SHOPIFY_SKU"
        elif matches:
            current = matches[0]
            item["current"] = current
            valid_ids = all(re.fullmatch(pattern, str(current[key] or "")) for key, pattern in (
                ("product_id", r"gid://shopify/Product/\d+"), ("variant_id", r"gid://shopify/ProductVariant/\d+")))
            if not valid_ids:
                item["status"] = "BLOCKED_SHOPIFY_IDENTITY"
            elif price is None:
                item["status"] = "PRICE_UNUSABLE_PRESERVE_EXISTING"
            elif money(current["price"]) == Decimal(price):
                item["status"] = "EXISTING_UNCHANGED"
            else:
                item["status"] = "EXISTING_PRICE_DIFF"
                item["changes"] = {"variant_price": {"id": current["variant_id"], "price": price}}
        elif index.get(sku):
            item["status"] = "BLOCKED_OTHER_VENDOR_MATCH"
        elif complete:
            item["status"] = "MISSING_PRICE_UNUSABLE" if price is None else "MISSING_CANDIDATE"
        # Whitelist, never copy whole rows: cost, stock, EAN, empty attributes and
        # packaging quantities cannot leak into product updates or public copy.
        if item["status"] in ("MISSING_CANDIDATE", "UNMATCHED_UNVERIFIED"):
            item["candidate"] = {"vendor": BRAND, "sku": sku}
            for field, column in (("title", "productnaam"), ("source_description", "description"),
                                  ("category_path", "categorie"), ("series", "serie")):
                value = (row.get(column) or "").strip()
                if value:
                    item["candidate"][field] = value
            if price is not None:
                item["candidate"]["price"] = price
            images = media_urls(row)
            if images:
                item["candidate"]["media_urls"] = images
            if not images or not item["candidate"].get("title"):
                item["issues"].append("MISSING_TITLE_OR_MEDIA_REQUIRES_EXISTING_SOURCE_DATA")
            item["issues"].append("MERGE_EXISTING_CONTENT_CATEGORY_RULES_BEFORE_CREATION")
        if price is None:
            item["issues"].append("NO_USABLE_ADVICE_PRICE_NO_FALLBACK")
        item["operation_id"] = digest({"source": source_sha, "item": item, "basis": basis, "rules": VERSION})
        items.append(item)
    counts = Counter(x["status"] for x in items)
    contract = {"basis": basis, "evidence": evidence, "source_column": PRICE_COLUMN,
                "vat_multiplier_ex_only": "1.21", "whole_euros_above_exact_inclusive": "100",
                "rounding": "ROUND_HALF_UP", "intermediate_rounding": False}
    summary = {"rules": VERSION, "source_sha256": source_sha, "source_rows": len(rows),
               "wiesbaden_rows": len(items), "other_brand_rows": len(rows) - len(items),
               "usable_advice_prices": sum(sale_price(r.get(PRICE_COLUMN, ""), basis) is not None for r in selected),
               "source_duplicate_sku_groups": sum(count > 1 for count in duplicate.values()),
               "snapshot_complete": complete, "statuses": dict(sorted(counts.items())),
               "read_only": True, "executed_writes": 0}
    manifest = {"schema_version": 1, "summary": summary, "price_contract": contract,
                "snapshot_sha256": snapshot_sha, "snapshot_observed_at": (snapshot or {}).get("observed_at"),
                "fresh_identity_check_required_before_write": True, "items": items}
    manifest["manifest_id"] = digest(manifest)
    return manifest


def write_private_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Private files are 0600; atomic replacement prevents partial checkpoints.
    fd, filename = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    temp = Path(filename)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as output:
            json.dump(value, output, ensure_ascii=False, indent=2)
            output.write("\n")
            output.flush()
            os.fsync(output.fileno())
        temp.replace(path)
    finally:
        if temp.exists():
            temp.unlink()


def checkpoint(path, manifest_id, operation_id, state, evidence=None):
    """Single-writer local journal; only a real executor may attest verified writes."""
    if state not in ("planned", "attempted", "applied", "verified", "exception"):
        raise ValueError("Unknown checkpoint state")
    if state == "verified" and not evidence:
        raise ValueError("Verified state requires readback evidence")
    path = Path(path)
    journal = json.loads(path.read_text()) if path.exists() else {"manifest_id": manifest_id, "operations": {}}
    if journal["manifest_id"] != manifest_id:
        raise ValueError("Journal belongs to another manifest; reconcile before resuming")
    journal["operations"][operation_id] = {"state": state, "evidence": evidence}
    write_private_json(path, journal)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", required=True, type=Path)
    parser.add_argument("--price-basis", required=True, choices=("incl", "ex"))
    parser.add_argument("--price-evidence", required=True)
    parser.add_argument("--snapshot", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parent.parent
    output = args.output.resolve()
    if output == repo or repo in output.parents:
        parser.error("Private manifest output must be outside the public repository")
    with args.csv.open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source, strict=True)
        if not {"productcode", "merk", PRICE_COLUMN}.issubset(reader.fieldnames or []):
            parser.error("Supplier CSV schema does not match the expected columns")
        rows = list(reader)
    if any(None in row or any(v is None for v in row.values()) for row in rows):
        parser.error("Malformed CSV row width; refusing shifted columns")
    snapshot = json.loads(args.snapshot.read_text(encoding="utf-8-sig")) if args.snapshot else None
    manifest = prepare(rows, hashlib.sha256(args.csv.read_bytes()).hexdigest(), args.price_basis,
                       args.price_evidence, snapshot,
                       hashlib.sha256(args.snapshot.read_bytes()).hexdigest() if args.snapshot else None)
    write_private_json(output / "manifest.json", manifest)
    write_private_json(output / "summary.json", manifest["summary"])
    print(json.dumps(manifest["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
