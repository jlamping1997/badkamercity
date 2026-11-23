#!/usr/bin/env python3
"""Prepare a separate, explicitly reviewed release of existing source holds.

Offline only. A source-bound allowlist cannot release protected/reviewed data,
missing CSV identities, new products or previously blocked creates. No prices,
body text, SEO, images, stock or collection membership are written.
"""
import argparse
import csv
import hashlib
import importlib.util
import json
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(filename))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


enrichment = module("enrichment", "wiesbaden-enrichment-plan.py")
filters = module("filters", "wiesbaden-filter-diff.py")
catalog = enrichment.catalog
PLATFORM_BLOCKED = {"20.3447", "41.3523", "41.3676"}


def reviewed_groups(product, proposal, rule):
    groups, omitted, keys = enrichment.clean_specs(product, proposal)
    allow = set(rule["allow_spec_keys"]) - set(rule.get("exclude_spec_keys", []))
    approved = rule["approved_spec_groups"]
    def flatten(values):
        result = {}
        for group in values:
            for field in group["items"]:
                if field["key"] in result:
                    raise ValueError("Duplicate reviewed specification key")
                result[field["key"]] = (field["label"], str(field["value"]))
        return result
    source_facts = flatten(groups)
    reviewed = flatten(approved)
    if set(reviewed) != allow or any(source_facts.get(key) != value for key, value in reviewed.items()):
        raise ValueError("Reviewed facts must exactly match retained source facts and the allowlist")
    if reviewed.get("fabrikantnummer", (None, None))[1] != product["sku"] or reviewed.get("merk", (None, ""))[1].casefold() != "wiesbaden":
        raise ValueError("Exact SKU and brand facts are mandatory")
    omitted.extend({"key": key, "reason": "REVIEWED_HOLD_FIELD_OMISSION"} for key in sorted(keys - allow))
    return approved, omitted, allow


def identity_ok(rule, source, target, current, csv_rows, held_skus, protected):
    sku = rule["sku"]
    if sku in protected or sku in PLATFORM_BLOCKED or sku not in held_skus:
        return False
    if rule.get("identity_verified") is not True or rule.get("disposition") != "RELEASE_WITH_FIELD_OMISSIONS":
        return False
    if len(csv_rows) != 1 or csv_rows[0].get("merk", "").strip().casefold() != "wiesbaden":
        return False
    if source["sku"] != sku or source.get("source_brand") != "Wiesbaden" or target.get("vendor", "").casefold() != "wiesbaden":
        return False
    variants = catalog.nodes(target["variants"])
    if len(variants) != 1 or target["variants"].get("pageInfo", {}).get("hasNextPage") is not False:
        return False
    if target["id"] != rule["product_id"] or variants[0]["id"] != rule["variant_id"] or variants[0]["sku"] != sku:
        return False
    if current.get("id") != target["id"] or current.get("hasOnlyDefaultVariant") is not True:
        return False
    if target.get("contentReview") is not None or target.get("completeSpecs") is not None:
        return False
    proof = source["source_evidence"]
    return proof.get("http_status") == 200 and proof.get("url") == source["source_url"] and re.fullmatch(r"[a-f0-9]{64}", proof.get("sha256", "")) is not None


def build(source_dir, base, snapshot, current, rules, csv_rows):
    def read(filename):
        return json.loads((source_dir / filename).read_text())
    master = defaultdict(list)
    for line in (source_dir / "product-master.jsonl").read_text().splitlines():
        if line.strip():
            product = json.loads(line)
            master[product["sku"]].append(product)
    specs = {x["sku"]: x for x in read("complete-specifications-proposal.json")}
    categories = {x["sku"]: x for x in read("category-import-proposal.json")}
    source_filters, targets = defaultdict(list), defaultdict(list)
    for row in read("filter-field-proposal.json"):
        source_filters[row["sku"]].append(row)
    for product in snapshot["products"]:
        for variant in catalog.nodes(product["variants"]):
            targets[variant["sku"]].append(product)
    checked = {x["id"]: x for x in current["products"]}
    protected = {x["sku"] for x in base["items"] if x["status"] == "PROTECTED_REVIEWED"} | enrichment.PILOTS
    held = {x["sku"] for x in base["items"] if x["status"] == "HELD_REGISTER"}
    if len({x["sku"] for x in rules}) != len(rules):
        raise ValueError("Duplicate release rule identity")
    review_date = datetime.fromisoformat(current["observed_until"].replace("Z", "+00:00")).astimezone(ZoneInfo("Europe/Amsterdam")).date().isoformat()
    items = []
    for rule in rules:
        sku = rule["sku"]
        row = {"sku": sku, "status": "HELD_IDENTITY_NOT_CONFIRMED", "metafields": [], "filter_candidates": []}
        if len(master[sku]) == len(targets[sku]) == 1:
            source, target = master[sku][0], targets[sku][0]
            if identity_ok(rule, source, target, checked.get(target["id"], {}), csv_rows[sku], held, protected):
                groups, omissions, keys = reviewed_groups(source, specs[sku], rule)
                docs = rule["source_document_urls"]
                if not set(docs).issubset(enrichment.document_urls(source)) or len(docs) != len(set(docs)):
                    raise ValueError("Reviewed documents must remain an exact subset of source documents")
                values = {f["key"]: f["value"] for g in groups for f in g["items"]}
                candidates, rejected = enrichment.filter_candidates(source_filters[sku], values)
                excluded = set(rule.get("exclude_filter_keys", []))
                candidates = [x for x in candidates if x["key"] in rule["allow_filter_keys"] and x["key"] not in excluded and "bc_filters." + x["key"] not in excluded]
                if sorted(candidates, key=lambda x: x["key"]) != sorted(rule["approved_filter_candidates"], key=lambda x: x["key"]):
                    raise ValueError("Filter proposal differs from exact reviewed source candidates")
                fields, notes = enrichment.target_fields(target, groups, docs, keys, omissions, source["source_url"],
                    {"proposed_collection_memberships": rule["category_handles"]}, review_date)
                row.update(status="EXTRA_REVIEWED_HOLD_PROPOSAL" if fields else "EXISTING_CONTENT_PRESERVED", product_id=target["id"],
                           metafields=fields, filter_candidates=candidates, source_specifications=groups, source_document_urls=docs,
                           omitted_facts=omissions, reviewed_omission_reasons=rule.get("omission_reasons", []),
                           filter_omissions=rejected, notes=notes, document_targets_http_checked=False,
                           source={"url": source["source_url"], "sha256": source["source_evidence"]["sha256"], "fetched_at": source["source_evidence"]["fetched_at"]},
                           live_scope={"hasOnlyDefaultVariant": True}, apply_gates=["CURRENT_DEFINITIONS_VERIFIED", "COMPARE_DIGEST_CAS_REQUIRED", "INDEPENDENT_READBACK_REQUIRED"])
        row["operation_id"] = catalog.digest(row)
        items.append(row)
    return {"schema": "wiesbaden-reviewed-hold-enrichment-v1", "items": items,
            "summary": {"review_rules": len(rules), "protected_reviewed_count": len(protected), "statuses": dict(Counter(x["status"] for x in items)),
                        "source_spec_values_prepared": sum(len(g["items"]) for x in items for g in x.get("source_specifications", [])),
                        "filter_candidates": sum(len(x["filter_candidates"]) for x in items), "executed_writes": 0}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("source", "base", "snapshot", "current", "rules", "csv", "content-definitions", "filter-definitions", "output"):
        parser.add_argument("--" + name, type=Path, required=True)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parent.parent
    if args.output.resolve() == repo or repo in args.output.resolve().parents:
        parser.error("Private output must be outside public repository")
    read = lambda path: json.loads(path.read_text())
    rules_doc, snapshot, current = read(args.rules), read(args.snapshot), read(args.current)
    if snapshot.get("pagination_complete") is not True or current.get("pagination_complete") is not True:
        parser.error("Complete baseline and current filter evidence required")
    csv_digest = hashlib.sha256(args.csv.read_bytes()).hexdigest()
    if csv_digest != rules_doc["source_csv_sha256"]:
        parser.error("Reviewed supplier CSV fingerprint does not match")
    csv_rows = defaultdict(list)
    with args.csv.open(encoding="utf-8-sig", newline="") as stream:
        for row in csv.DictReader(stream):
            csv_rows[catalog.sku_key(row["productcode"])].append(row)
    result = build(args.source, read(args.base), snapshot, current, rules_doc["rules"], csv_rows)
    definitions = {(d["namespace"], d["key"]): d for d in read(args.content_definitions)["definitions"]}
    for row in result["items"]:
        for field in row["metafields"]:
            definition = definitions[field["namespace"], field["key"]]
            if (definition["ownerType"] != "PRODUCT" or definition["type"]["name"] != field["type"] or definition["validations"] != []
                    or definition["access"].get("admin") != "PUBLIC_READ_WRITE"):
                parser.error("Current content definition mismatch")
    filter_plan = filters.build(result, current, read(args.filter_definitions))
    by_id = {r["product_id"]: r for r in filter_plan["items"]}
    for row in result["items"]:
        if row["metafields"]:
            row["metafields"] += by_id[row["product_id"]]["metafields"]
            row["live_scope"].update(definitions_verified=True, filter_connection_complete=True)
            row["apply_gates"] = ["COMPARE_DIGEST_CAS_REQUIRED", "INDEPENDENT_READBACK_REQUIRED"]
            row["operation_id"] = catalog.digest({k: v for k, v in row.items() if k != "operation_id"})
    result["summary"].update(filter_diff=filter_plan["summary"], total_intended_fields=sum(len(x["metafields"]) for x in result["items"]), external_index_synced=False)
    result["input_sha256"] = {name: hashlib.sha256(getattr(args, name).read_bytes()).hexdigest() for name in ("base", "snapshot", "current", "rules", "csv", "content_definitions", "filter_definitions")}
    result["input_sha256"].update({name: hashlib.sha256((args.source / name).read_bytes()).hexdigest() for name in (
        "product-master.jsonl", "complete-specifications-proposal.json", "filter-field-proposal.json", "category-import-proposal.json")})
    catalog.write_private_json(args.output / "extra-enrichment-manifest.json", result)
    catalog.write_private_json(args.output / "extra-filter-diff.json", filter_plan)
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
