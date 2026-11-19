#!/usr/bin/env python3
"""Offline, source-backed specification/document proposals; no network or writes to Shopify.

Reuses complete-specifications-proposal.json and filter-field-proposal.json from
wiesbaden-import-plan.py. Protects reviewed products and explicit quarantine.
Target metafield payloads remain gated on hasOnlyDefaultVariant and fresh CAS.
Filter candidates are NOT writes: current definitions, values and index route
must be checked separately. Private output only; never commit source/snapshots.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote, urlsplit
from zoneinfo import ZoneInfo

spec = importlib.util.spec_from_file_location("catalog", Path(__file__).with_name("wiesbaden-catalog-run.py"))
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)
VERSION = "2026-10-21.4"
PILOTS = {"24.3710", "20.3755", "20.3756", "32.3411", "32.3594", "32.2510", "32.3670", "38.4125"}
LEGACY_HOLDS = {"29.8007": "KNOWN_IDENTITY_AND_COLOUR_CONFLICT", "41.3540": "KNOWN_RADIATOR_TECH_CONFLICT"}
SENSITIVE = re.compile(r"\b(?:ean|gtin|barcode|inkoopprijs|adviesprijs|brutoprijs|nettoprijs|cost|voorraad|levertijd|garantieduur)\b", re.I)
UNKNOWN = {"overig", "overige", "onbekend", "nvt", "n.v.t.", ""}
MIRRORS = {"korverholland.compano.com", "kh-compano.b-cdn.net"}


def slug(value):
    return re.sub(r"[^a-z0-9]+", "_", unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()).strip("_")


def clean_specs(product, proposal, reviewed_conflicts=None):
    """Drop only unsupported/conflicting fields; retain explicit Nee/0 and units."""
    source = defaultdict(set)
    for fact in product["specifications"]:
        key = slug(fact["label"])
        source["fabrikantnummer" if key == "sku" else key].add(str(fact["value"]).strip())
    omitted, groups, kept = [], [], set()
    issues, title = set(product.get("issues", [])), product["name"].casefold()
    for group in proposal["value"]:
        fields = []
        for fact in group["items"]:
            key, value = fact["key"], str(fact["value"]).strip()
            reason = None
            if SENSITIVE.search(key.replace("_", " ") + " " + fact["label"]):
                reason = "EXCLUDED_NONPUBLIC_OR_UNVERIFIED_FIELD"
            elif key in kept:
                continue
            elif len(source.get(key, set())) != 1 or value not in source[key]:
                reason = "SOURCE_FIELD_MISSING_OR_CONFLICTING"
            elif value.casefold() in UNKNOWN:
                reason = "UNSPECIFIED_SOURCE_VALUE"
            elif (key, value) in (reviewed_conflicts or {}):
                reason = reviewed_conflicts[key, value]
            elif value.casefold() == "nee" and "compleet met hoofddouche" in title and key in {
                "geschikt_voor_douche", "met_douchegarnituur", "met_hoofddouche"
            }:
                reason = "EXPLICIT_SHOWER_SET_CONTENTS_CONFLICT"
            elif value.casefold() == "nee" and key == "met_afsluiter" and "stopkranen compleet" in title:
                reason = "EXPLICIT_STOP_VALVE_CONTENTS_CONFLICT"
            elif value.casefold() == "nee" and key == "met_uitloop" and "baduitloop" in title:
                reason = "EXPLICIT_BATH_OUTLET_CONTENTS_CONFLICT"
            elif value.casefold() == "nee" and key == "geschikt_voor_bad_inbouw_in_muur" and "inbouw" in title and "baduitloop" in title:
                reason = "EXPLICIT_BUILTIN_BATH_APPLICATION_CONFLICT"
            elif value.casefold() == "nee" and key == "met_douchegarnituur" and ("handdouche" in title or "hoofddouche" in title):
                reason = "EXPLICIT_SHOWER_COMPONENTS_CONFLICT"
            elif key == "serie" and "SOURCE_SERIES_DESCRIPTION_CONFLICT_REVIEW" in issues:
                reason = "SOURCE_SERIES_CONFLICT"
            elif "PREVIOUS_DIMENSION_CONFLICT_REVIEW" in issues and re.search("hoogte|breedte|diepte|lengte", key):
                reason = "SOURCE_DIMENSION_CONFLICT"
            elif key == "aantal_kraangaten" and (m := re.fullmatch(r"(\d+)(?:-gats)?", value, re.I)) and int(m[1]) > 8:
                reason = "IMPLAUSIBLE_HOLE_COUNT"
            elif key in ("kleur", "basiskleur") and "mat zwart" in title and value.casefold() in ("chroom", "wit", "rvs"):
                reason = "TITLE_COLOUR_CONFLICT"
            elif key == "model" and "afbouwdeel" in title and value.casefold() == "inbouwdeel":
                reason = "TITLE_MODEL_CONFLICT"
            if reason:
                omitted.append({"key": key, "reason": reason})
            else:
                fields.append({"key": key, "label": fact["label"], "value": value})
                kept.add(key)
        if fields:
            groups.append({"group": group["group"], "items": fields})
    return groups, omitted, kept


def asset_key(url):
    parts = urlsplit(url)
    return ("supplier", unquote(parts.path)) if parts.hostname in MIRRORS else (parts.hostname, unquote(parts.path), parts.query)


def document_urls(product):
    records = product.get("documents", []) + [i for i in product.get("images", []) if i.get("kind") in ("line_drawings", "exploded_views")]
    urls, seen = [], set()
    pattern = re.compile(re.escape(product["sku"]) + r"(?:[ _-].*)?\.(?:pdf|jpe?g|png|webp)$", re.I)
    for record in records:
        url = record["url"]
        parts = urlsplit(url)
        if parts.scheme != "https" or not pattern.fullmatch(Path(unquote(parts.path)).name):
            continue
        key = asset_key(url)
        if key not in seen:
            seen.add(key)
            urls.append(url)
    return urls


def filter_candidates(records, allowed_facts):
    values, rejected = [], []
    counts = Counter(x["proposed_field"] for x in records)
    for row in records:
        field, kind, value = row["proposed_field"], row["proposed_type"], row["proposed_value"]
        raw = str(row["source_value"]).strip()
        valid = (row["mapping_status"] == "TYPED_VALUE_CANDIDATE"
                 and allowed_facts.get(slug(row["source_label"])) == raw
                 and re.fullmatch(r"bc_filters\.[a-z][a-z0-9_]*", field) and counts[field] == 1)
        if kind == "number_integer":
            valid = valid and re.fullmatch(r"\d+", str(value)) is not None
            value = str(value)
            valid = valid and (raw == value or (field == "bc_filters.aantal_kraangaten" and raw.casefold() == value + "-gats"))
        elif kind == "boolean":
            valid = valid and type(value) is bool and raw.casefold() == ("ja" if value is True else "nee")
            value = "true" if value is True else "false"
        elif kind == "single_line_text_field":
            valid = valid and isinstance(value, str) and value == raw and value.casefold() not in UNKNOWN
        else:
            valid = False
        if valid:
            values.append({"namespace": "bc_filters", "key": field.split(".", 1)[1], "type": kind,
                           "value": value, "source_label": row["source_label"], "source_value": row["source_value"]})
        else:
            rejected.append({"key": field, "reason": "UNVERIFIED_OR_OMITTED_FILTER_FACT"})
    return values, rejected


def target_fields(product, groups, documents, spec_keys, omitted, source_url, category, review_date):
    """Prepare compare-and-set payloads without replacing reviewed/existing specs."""
    fields, notes = [], []
    for alias in ("completeSpecs", "technicalDocs", "contentReview"):
        if alias not in product or (product[alias] is not None and "compareDigest" not in product[alias]):
            return [], ["CURRENT_METAFIELD_OR_DIGEST_NOT_READ"]
    if product["contentReview"] is not None or product["completeSpecs"] is not None:
        return [], ["EXISTING_CONTENT_FIELD_PRESERVED"]
    def add(namespace, key, kind, value, current):
        fields.append({"ownerId": product["id"], "namespace": namespace, "key": key, "type": kind,
                       "value": json.dumps(value, ensure_ascii=False, separators=(",", ":")),
                       "compareDigest": current["compareDigest"] if current else None})
    add("custom", "complete_specificaties", "json", groups, None)
    current_docs = product["technicalDocs"]
    if current_docs is not None and current_docs["type"] != "list.url":
        notes.append("DOCUMENT_FIELD_TYPE_CONFLICT_PRESERVED")
    else:
        try:
            before = json.loads(current_docs["value"]) if current_docs else []
            if not isinstance(before, list) or any(not isinstance(u, str) for u in before):
                raise ValueError("Invalid document list")
            merged, seen = list(before), {asset_key(u) for u in before}
            for url in documents:
                if asset_key(url) not in seen:
                    merged.append(url)
                    seen.add(asset_key(url))
            if merged and merged != before:
                add("custom", "technische_documenten", "list.url", merged, current_docs)
        except (ValueError, TypeError):
            notes.append("INVALID_EXISTING_DOCUMENT_LIST_PRESERVED")
    memberships = {c["handle"] for c in catalog.nodes(product.get("collections", []))}
    handles = [h for h in category.get("proposed_collection_memberships", []) if h in memberships]
    marker = {"schema": "wiesbaden-content-v1", "status": "ready", "product_id": product["id"].rsplit("/", 1)[1],
              "sku": catalog.nodes(product["variants"])[0]["sku"], "spec_keys": sorted(spec_keys),
              "category_handles": handles, "source_urls": [source_url], "reviewed_date": review_date,
              "omitted_facts": [x["key"] + ": " + x["reason"] for x in omitted]}
    add("bc_data", "content_review", "json", marker, None)
    return fields, notes


def build(source_dir, registry, snapshot, field_review=None):
    def read(name):
        return json.loads((source_dir / name).read_text())
    master = [json.loads(line) for line in (source_dir / "product-master.jsonl").read_text().splitlines() if line.strip()]
    specs = {x["sku"]: x for x in read("complete-specifications-proposal.json")}
    categories = {x["sku"]: x for x in read("category-import-proposal.json")}
    filters = defaultdict(list)
    for row in read("filter-field-proposal.json"):
        filters[row["sku"]].append(row)
    conflicts = defaultdict(dict)
    for item in (field_review or {}).get("candidates", []):
        for conflict in item.get("field_conflicts", []):
            if conflict.get("scope") == "field_only" and conflict.get("whole_product_block") is False:
                for fact in conflict.get("raw_items", []):
                    conflicts[item["sku"]][slug(fact["label"]), str(fact["value"]).strip()] = "REVIEWED_" + conflict["code"]
    protected = PILOTS | set(registry.get("applied_2026_10_21", [])) | set(registry.get("protected_skus", []))
    holds = {sku: group for group, values in registry.get("groups", {}).items() for sku in values["skus"]}
    for sku, reason in LEGACY_HOLDS.items():
        holds.setdefault(sku, reason)
    by_sku = defaultdict(list)
    for product in snapshot["products"]:
        for variant in catalog.nodes(product["variants"]):
            by_sku[catalog.sku_key(variant["sku"])].append(product)
    source_counts = Counter(p["sku"] for p in master)
    review_date = datetime.fromisoformat(snapshot["observed_at"].replace("Z", "+00:00")).astimezone(ZoneInfo("Europe/Amsterdam")).date().isoformat()
    items, totals, source_scope = [], Counter(), [p for p in master if p.get("source_brand") == "Wiesbaden"]
    for product in source_scope:
        sku, proof = product["sku"], product["source_evidence"]
        item = {"sku": sku, "status": "SOURCE_ONLY", "metafields": [], "filter_candidates": [], "notes": [],
                "source": {"url": product["source_url"], "sha256": proof["sha256"], "fetched_at": proof["fetched_at"]}}
        matched = by_sku.get(sku, [])
        if sku in protected or any(p.get("contentReview") is not None for p in matched):
            item["status"] = "PROTECTED_REVIEWED"
        elif sku in holds:
            item["status"], item["notes"] = "HELD_REGISTER", [holds[sku]]
        elif source_counts[sku] != 1 or len(matched) > 1:
            item["status"] = "BLOCKED_DUPLICATE_IDENTITY"
        elif not (proof.get("http_status") == 200 and proof.get("url") == product["source_url"] and re.fullmatch(r"[a-f0-9]{64}", proof["sha256"])):
            item["status"] = "BLOCKED_SOURCE_PROVENANCE"
        else:
            groups, omitted, keys = clean_specs(product, specs[sku], conflicts[sku])
            docs = document_urls(product)
            flat = {f["key"]: f["value"] for g in groups for f in g["items"]}
            if flat.get("fabrikantnummer") != sku or flat.get("merk", "").casefold() != "wiesbaden":
                item["status"] = "BLOCKED_SOURCE_IDENTITY"
            else:
                item.update(source_specifications=groups, source_document_urls=docs, omitted_facts=omitted,
                            document_targets_http_checked=False)
                item["filter_candidates"], item["filter_omissions"] = filter_candidates(filters[sku], flat)
                if matched:
                    target = matched[0]
                    item["product_id"] = target["id"]
                    if target["vendor"].casefold() != "wiesbaden" or len(catalog.nodes(target["variants"])) != 1 or target["variants"].get("pageInfo", {}).get("hasNextPage"):
                        item["status"] = "BLOCKED_TARGET_IDENTITY_OR_VARIANTS"
                    else:
                        item["metafields"], item["notes"] = target_fields(target, groups, docs, keys, omitted, product["source_url"], categories[sku], review_date)
                        item["status"] = "TARGET_PROPOSAL_DEFAULT_VARIANT_CHECK_REQUIRED" if item["metafields"] else "PRESERVED_EXISTING_CONTENT"
                        item["apply_gates"] = ["HAS_ONLY_DEFAULT_VARIANT_TRUE", "CURRENT_DEFINITIONS_VERIFIED", "FRESH_COMPARE_DIGEST"]
                totals["source_spec_values_prepared"] += sum(len(g["items"]) for g in groups)
                totals["source_documents_prepared"] += len(docs)
                totals["source_filters_prepared"] += len(item["filter_candidates"])
                totals["optional_fields_omitted"] += len(omitted)
        item["operation_id"] = catalog.digest(item)
        items.append(item)
    summary = {"rules": VERSION, "source_wiesbaden": len(source_scope), "shopify_products": len(snapshot["products"]),
               "statuses": dict(Counter(i["status"] for i in items)), **totals, "executed_writes": 0,
               "filter_writes_prepared": False, "external_index_synced": False}
    return {"schema": "wiesbaden-enrichment-plan-v1", "summary": summary, "items": items}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--register", type=Path, required=True)
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--field-review", type=Path, action="append", help="Private exact-SKU field-conflict evidence; repeat for additional reviewed sources")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parent.parent
    if args.output.resolve() == repo or repo in args.output.resolve().parents:
        parser.error("Private output must be outside the public repository")
    snapshot = json.loads(args.snapshot.read_text())
    if snapshot.get("pagination_complete") is not True:
        parser.error("A complete explicit snapshot is required")
    field_review = {"candidates": [item for path in args.field_review or []
                                    for item in json.loads(path.read_text()).get("candidates", [])]}
    result = build(args.source, json.loads(args.register.read_text()), snapshot, field_review)
    result["input_sha256"] = {name: hashlib.sha256(path.read_bytes()).hexdigest() for name, path in
                              [("snapshot", args.snapshot), ("register", args.register)] +
                              [(name, args.source / name) for name in ("product-master.jsonl", "complete-specifications-proposal.json", "filter-field-proposal.json", "category-import-proposal.json")]}
    for index, path in enumerate(args.field_review or []):
        result["input_sha256"]["field_review_" + str(index) + ":" + path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
    catalog.write_private_json(args.output / "enrichment-manifest.json", result)
    catalog.write_private_json(args.output / "enrichment-summary.json", result["summary"])
    catalog.write_private_json(args.output / "default-variant-check-ids.json", [i["product_id"] for i in result["items"] if i["metafields"]])
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
