#!/usr/bin/env python3
"""Offline minimal bc_filters diffs from reviewed facts and complete live evidence.

No network or Shopify mutations. Existing definition types must agree; custom
validations require separate review. Empty source values never clear fields.
"""
import argparse
import importlib.util
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

spec = importlib.util.spec_from_file_location("catalog", Path(__file__).with_name("wiesbaden-catalog-run.py"))
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)


def value_valid(kind, value):
    if not isinstance(value, str) or not value.strip():
        return False
    if kind == "boolean":
        return value in ("true", "false")
    if kind == "number_integer":
        return re.fullmatch(r"-?(0|[1-9][0-9]*)", value) is not None and abs(int(value)) <= 9007199254740991
    if kind == "single_line_text_field":
        return len(value) <= 65536 and "\n" not in value and "\r" not in value
    return False


def build(manifest, snapshot, definitions):
    if snapshot.get("pagination_complete") is not True or definitions.get("pagination_complete") is not True:
        raise ValueError("Complete current product/filter and definition evidence required")
    by_id, defs = defaultdict(list), defaultdict(list)
    for product in snapshot["products"]:
        by_id[product["id"]].append(product)
    for definition in definitions["definitions"]:
        defs[definition["namespace"], definition["key"]].append(definition)
    rows, counts = [], Counter()
    for item in manifest["items"]:
        if not item.get("metafields"):
            continue  # Protected and held products can never acquire filter writes.
        row = {"sku": item["sku"], "product_id": item["product_id"], "metafields": [], "before": [], "skipped": []}
        matches = by_id[item["product_id"]]
        if len(matches) != 1 or matches[0].get("hasOnlyDefaultVariant") is not True:
            row["skipped"].append({"reason": "TARGET_IDENTITY_OR_DEFAULT_VARIANT_NOT_CONFIRMED"})
        else:
            connection = matches[0].get("metafields", {})
            if connection.get("pageInfo", {}).get("hasNextPage") is not False:
                row["skipped"].append({"reason": "CURRENT_FILTER_CONNECTION_INCOMPLETE"})
            else:
                current = defaultdict(list)
                for field in connection.get("nodes", []):
                    current[field["namespace"], field["key"]].append(field)
                for candidate in item["filter_candidates"]:
                    identity = candidate["namespace"], candidate["key"]
                    definition, before = defs[identity], current[identity]
                    reason = None
                    if identity[0] != "bc_filters" or not value_valid(candidate["type"], candidate["value"]):
                        reason = "BLANK_OR_UNSUPPORTED_SOURCE_VALUE"
                    elif len(definition) != 1 or definition[0]["ownerType"] != "PRODUCT":
                        reason = "MERCHANT_DEFINITION_NOT_CONFIRMED"
                    elif definition[0]["access"].get("admin") != "PUBLIC_READ_WRITE":
                        reason = "MERCHANT_DEFINITION_ACCESS_NOT_CONFIRMED"
                    elif definition[0]["type"]["name"] != candidate["type"]:
                        reason = "CURRENT_DEFINITION_TYPE_CONFLICT"
                    elif definition[0].get("validations") != []:
                        reason = "DEFINITION_VALIDATIONS_REQUIRE_SEPARATE_REVIEW"
                    elif len(before) > 1 or (before and (before[0]["type"] != candidate["type"] or not before[0].get("compareDigest"))):
                        reason = "CURRENT_VALUE_TYPE_OR_DIGEST_CONFLICT"
                    if reason:
                        row["skipped"].append({"key": candidate["key"], "reason": reason})
                    elif before and before[0]["value"] == candidate["value"]:
                        counts["unchanged_fields"] += 1
                    else:
                        row["metafields"].append({"ownerId": item["product_id"], **{k: candidate[k] for k in ("namespace", "key", "type", "value")},
                                                 "compareDigest": before[0]["compareDigest"] if before else None})
                        row["before"].append({"key": candidate["key"], "definition_id": definition[0]["id"], "current": before[0] if before else None,
                                              "source_label": candidate["source_label"], "source_value": candidate["source_value"]})
                        counts["changed_existing_fields" if before else "new_fields"] += 1
        counts["products_with_diff"] += bool(row["metafields"])
        counts["skipped_fields"] += len(row["skipped"])
        row["operation_id"] = catalog.digest(row)
        rows.append(row)
    return {"schema": "wiesbaden-filter-diff-v1", "snapshot_observed_from": snapshot.get("observed_from"),
            "snapshot_observed_until": snapshot.get("observed_until"), "definitions_observed_at": definitions.get("observed_at"),
            "input_sha256": {"source_manifest": catalog.digest(manifest), "current_snapshot": catalog.digest(snapshot), "definitions": catalog.digest(definitions)},
            "summary": {"products_checked": len(rows), **counts, "executed_writes": 0, "external_index_synced": False}, "items": rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ("manifest", "snapshot", "definitions", "output"):
        parser.add_argument("--" + key, type=Path, required=True)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parent.parent
    if args.output.resolve() == repo or repo in args.output.resolve().parents:
        parser.error("Private output must be outside public repository")
    result = build(*(json.loads(path.read_text()) for path in (args.manifest, args.snapshot, args.definitions)))
    catalog.write_private_json(args.output, result)
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
