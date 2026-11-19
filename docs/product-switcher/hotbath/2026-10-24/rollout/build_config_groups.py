#!/usr/bin/env python3
"""Build complete shower-set menus from exact Hotbath Edition 18 family rules.

This is a read-only generator. It never invents articles or writes Shopify data.
"""
from __future__ import annotations

import argparse
import copy
import json
import re
from collections import Counter
from pathlib import Path

FAMILIES = ("IBS70", "IBS7009", "IBS20", "IBS20A", "IBS1", "IBS1A", "IBS12", "IBS12A")
COLORS = {
    "CR": "Chroom", "GN": "Geborsteld nikkel", "BB": "Geborsteld messing",
    "AB": "Verouderd messing", "WH": "Mat wit", "AI": "Verouderd ijzer",
    "PBP": "Gepolijst zwart PVD", "MBP": "Geborsteld zwart PVD",
    "BBP": "Geborsteld messing PVD", "BCP": "Geborsteld koper PVD",
}
KEYS = ("kleur", "breedte_diameter_hoofddouche", "type_bevestiging_hoofddouche", "type_handdouche", "bevestiging_handdouche")
LABELS = ("Kleur", "Diameter hoofddouche", "Bevestiging hoofddouche", "Handdouche", "Handdouchehouder")


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.casefold()).strip()


def eligible(product: dict) -> tuple[bool, str | None]:
    variants = product.get("variants", {}).get("nodes", [])
    text = " ".join([product.get("title", ""), product.get("handle", ""), *[str(v.get("sku") or "") for v in variants]]).upper()
    if "SPOM" in text:
        return False, "SPOM_EXCLUDED"
    if any("TEST" in str(v.get("sku") or "").upper() for v in variants) or product.get("title", "").upper().startswith("TEST") or product.get("handle", "").startswith("test"):
        return False, "TEST_EXCLUDED"
    if product.get("status") != "ACTIVE" or not product.get("publishedAt"):
        return False, "NOT_ACTIVE_AND_PUBLISHED"
    if len(variants) != 1 or product.get("variants", {}).get("pageInfo", {}).get("hasNextPage"):
        return False, "VARIANT_SNAPSHOT_INCOMPLETE"
    if not re.fullmatch(r"[a-z0-9-]+", product.get("handle", "")):
        return False, "UNSAFE_HANDLE"
    return True, None


def family_for_sku(sku: str) -> tuple[str, str, str] | None:
    for family in sorted(FAMILIES, key=len, reverse=True):
        match = re.fullmatch(re.escape(family) + "(" + "|".join(sorted(COLORS, key=len, reverse=True)) + r")([0-9]*)", sku)
        if match:
            return family, match.group(1), match.group(2)
    return None


def hand_values(rule: dict) -> tuple[str, str]:
    if rule["id"] in {"IBS12", "IBS12A"}:
        return "Rond ABS (Ø13 cm)", "Rond, 3 standen (Ø13 cm)"
    if rule["id"] in {"IBS70", "IBS7009"}:
        return "Staafmodel", "Rond model"
    return "Staafmodel", "Rond, 3 standen (Ø10 cm)"


def decode(family: str, color: str, suffix: str, rules: dict) -> dict:
    rule = rules[family]
    if color not in rule["finish_codes_shown_in_book"]:
        raise ValueError("FINISH_NOT_CONFIRMED_FOR_FAMILY")
    digits = set(suffix)
    if len(digits) != len(suffix) or suffix != "".join(sorted(suffix)) or not digits <= set(rule["option_codes"]):
        raise ValueError("UNKNOWN_OR_NONCANONICAL_OPTION_SUFFIX")
    if any(set(pair) <= digits for pair in rule["suffix_contradictions"]):
        raise ValueError("CONTRADICTORY_OPTION_SUFFIX")
    hand_default, hand_alternate = hand_values(rule)
    return {
        "kleur": COLORS[color],
        "breedte_diameter_hoofddouche": "25 cm" if "4" in digits else "30 cm" if "5" in digits else rule["default"]["overhead_diameter"],
        "type_bevestiging_hoofddouche": "Plafondbuis 15 cm" if "2" in digits else "Plafondbuis 30 cm" if "3" in digits else rule["default"]["overhead_mount"],
        "type_handdouche": hand_alternate if "1" in digits else hand_default,
        "bevestiging_handdouche": "Glijstang" if "7" in digits else rule["default"]["handshower_mount"],
    }


def title_check(title: str, family: str, options: dict, suffix: str) -> tuple[list[str], list[str]]:
    text = normalize(title)
    findings, corroborated = [], []
    expected_color = options["kleur"].casefold()
    colors_in_title = [label for label in COLORS.values() if re.search(r"(?<!\w)" + re.escape(label.casefold()) + r"(?!\w)", text)]
    colors_in_title.sort(key=len, reverse=True)
    if not colors_in_title:
        findings.append("TITLE_COLOR_MISSING")
    elif colors_in_title[0].casefold() != expected_color or any(label.casefold() not in expected_color for label in colors_in_title[1:]):
        findings.append("TITLE_COLOR_CONFLICT")
    else:
        corroborated.append("kleur")
    embedded_colors = re.findall(r"\b(?:CB|B)\d{3}(?:EXT)?(" + "|".join(sorted(COLORS, key=len, reverse=True)) + r")\b", title.upper())
    if any(COLORS[code].casefold() != expected_color for code in embedded_colors):
        findings.append("TITLE_EMBEDDED_COMPONENT_COLOR_CONFLICT")
    has_two_way = bool(re.search(r"2\s*[-–—]?\s*weg", text))
    has_stop_valves = bool(re.search(r"2\s*[-–—]?\s*stopkranen", text))
    if (family in {"IBS70", "IBS20", "IBS1", "IBS12"} and has_two_way) or (family in {"IBS7009", "IBS20A", "IBS1A", "IBS12A"} and has_stop_valves):
        findings.append("TITLE_CONTROL_CONFLICT")
    diameter = re.search(r"(\d+)\s*cm\s*hoof[d]?douche", text) or re.search(r"ø\s*(\d+)\s*cm", text)
    if not diameter:
        findings.append("TITLE_OVERHEAD_DIAMETER_MISSING")
    elif options["breedte_diameter_hoofddouche"] != diameter.group(1) + " cm":
        findings.append("TITLE_OVERHEAD_DIAMETER_CONFLICT")
    else:
        corroborated.append("breedte_diameter_hoofddouche")
    ceiling = re.search(r"(\d+)\s*cm\s*plafondbuis", text) or re.search(r"plafondbuis\s*(\d+)\s*cm", text)
    mount = f"Plafondbuis {ceiling.group(1)} cm" if ceiling else "Wandarm" if "wandarm" in text else None
    if mount is None:
        findings.append("TITLE_OVERHEAD_MOUNT_MISSING")
    elif mount != options["type_bevestiging_hoofddouche"]:
        findings.append("TITLE_OVERHEAD_MOUNT_CONFLICT")
    else:
        corroborated.append("type_bevestiging_hoofddouche")
    if "zonder glijstang" in text or "wandhouder" in text or "wandsteun" in text:
        holder = "Wandhouder"
    elif "glijstang" in text:
        holder = "Glijstang"
    else:
        holder = None
    if holder is None:
        findings.append("TITLE_HANDSHOWER_MOUNT_MISSING")
    elif holder != options["bevestiging_handdouche"]:
        findings.append("TITLE_HANDSHOWER_MOUNT_CONFLICT")
    else:
        corroborated.append("bevestiging_handdouche")
    has_staff = bool(re.search(r"staaf\s*handdouche", text))
    has_round = bool(re.search(r"ronde?\s*(?:3\s*[-–—]?\s*standen\s*)?handdouche", text))
    has_three = bool(re.search(r"3\s*[-–—]?\s*standen", text))
    alternate = "1" in suffix
    if family in {"IBS12", "IBS12A"}:
        if has_staff or (has_three and not alternate):
            findings.append("TITLE_HANDSHOWER_CONFLICT")
        elif has_round or has_three:
            corroborated.append("type_handdouche")
        else:
            findings.append("TITLE_HANDSHOWER_MISSING")
    elif family in {"IBS70", "IBS7009"}:
        if (alternate and has_staff) or (not alternate and (has_round or has_three)):
            findings.append("TITLE_HANDSHOWER_CONFLICT")
        elif (alternate and has_round) or (not alternate and has_staff):
            corroborated.append("type_handdouche")
        else:
            findings.append("TITLE_HANDSHOWER_MISSING")
    else:
        if (alternate and has_staff) or (not alternate and (has_round or has_three)):
            findings.append("TITLE_HANDSHOWER_CONFLICT")
        elif (alternate and has_three) or (not alternate and has_staff):
            corroborated.append("type_handdouche")
        else:
            findings.append("TITLE_HANDSHOWER_MISSING")
    return findings, corroborated


def build(snapshot: dict, book: dict, existing: dict) -> tuple[dict, dict, dict]:
    if snapshot.get("complete") is not True:
        raise ValueError("Complete catalog snapshot required")
    rules = {x["id"]: x for x in book["families"] if x["id"] in FAMILIES}
    if set(rules) != set(FAMILIES):
        raise ValueError("Eight exact book rules required")
    old_groups = {g["id"]: g for g in existing["groups"]}
    old_handle_groups = {}
    for old_group in existing["groups"]:
        for old_product in old_group["products"]:
            old_handle_groups.setdefault(old_product["handle"], set()).add(old_group["id"])
    rows = {f: [] for f in FAMILIES}
    reviews, excluded, unknown = [], [], []
    for product in snapshot["products"]:
        variants = product.get("variants", {}).get("nodes", [])
        sku = str((variants[0] if variants else {}).get("sku") or "").strip()
        parsed = family_for_sku(sku)
        if parsed is None:
            continue
        family, color, suffix = parsed
        okay, reason = eligible(product)
        if not okay:
            excluded.append({"sku": sku, "handle": product.get("handle"), "reason": reason})
            continue
        try:
            options = decode(family, color, suffix, rules)
        except ValueError as error:
            reviews.append({"family": family, "sku": sku, "handle": product["handle"], "reason": str(error)})
            continue
        findings, corroborated = title_check(product["title"], family, options, suffix)
        conflicts = [x for x in findings if x.endswith("CONFLICT")]
        if conflicts:
            reviews.append({"family": family, "sku": sku, "handle": product["handle"], "reason": "SKU_TITLE_CONFLICT", "findings": findings, "title": product["title"], "decoded_options": options})
            continue
        current = (product.get("group") or {}).get("value")
        old_ids = sorted(old_handle_groups.get(product["handle"], set()))
        row = {"id": product["id"], "sku": sku, "family": family, "handle": product["handle"], "url": "/products/" + product["handle"], "title": product["title"], "options": options, "current_group": current, "existing_json_group_ids": old_ids, "book_source": rules[family]["sources"], "title_corroborated_keys": corroborated, "title_missing_keys": findings}
        rows[family].append(row)
    groups, mapping, metrics = [], [], []
    for family in FAMILIES:
        family_rows = rows[family]
        tuple_counts = Counter(tuple(r["options"][k] for k in KEYS) for r in family_rows)
        duplicate_tuples = [list(k) for k, n in tuple_counts.items() if n > 1]
        sku_counts = Counter(r["sku"] for r in family_rows)
        group_ids = {group_id for row in family_rows for group_id in ([row["current_group"]] if row["current_group"] else []) + row["existing_json_group_ids"]}
        if group_ids - set(old_groups):
            reviews.append({"family": family, "reason": "UNKNOWN_EXISTING_GROUP_NOT_OVERRIDDEN", "existing_group_ids": sorted(group_ids)})
            metrics.append({"family": family, "status": "BLOCKED_REVIEW", "products": len(family_rows)})
            continue
        if duplicate_tuples or any(n > 1 for n in sku_counts.values()) or len(group_ids) > 1:
            reviews.append({"family": family, "reason": "DUPLICATE_OR_MIXED_EXISTING_GROUP", "duplicate_tuples": duplicate_tuples, "existing_group_ids": sorted(group_ids)})
            metrics.append({"family": family, "status": "BLOCKED_REVIEW", "products": len(family_rows)})
            continue
        series = rules[family]["series"]
        group_id = next(iter(group_ids)) if group_ids else f"hotbath-{series.casefold()}-{family.casefold()}-inbouw-doucheset"
        old = old_groups.get(group_id)
        if old:
            old_keys = [m["key"] for m in sorted(old["menus"], key=lambda m: m.get("order", 0))]
            safe_old = set(old_keys) == set(KEYS) and {p["handle"] for p in old["products"]} <= {r["handle"] for r in family_rows}
            if safe_old:
                by_handle = {r["handle"]: r for r in family_rows}
                safe_old = all(p["options"] == by_handle[p["handle"]]["options"] for p in old["products"])
            if not safe_old:
                reviews.append({"family": family, "existing_group_id": group_id, "reason": "EXISTING_GROUP_REQUIRES_ADAPTER_NOT_OVERWRITTEN"})
                metrics.append({"family": family, "status": "BLOCKED_REVIEW", "products": len(family_rows)})
                continue
        hand_default, hand_alternate = hand_values(rules[family])
        values = [list(COLORS.values()), ["20 cm", "25 cm", "30 cm"], ["Wandarm", "Plafondbuis 15 cm", "Plafondbuis 30 cm"], [hand_default, hand_alternate], ["Wandhouder", "Glijstang"]]
        menus = [{"key": key, "label": label, "order": index + 1, "display_type": "dropdown" if key == "kleur" else "buttons", "hide_if_single_value": True, "values": [v for v in vals if any(row["options"][key] == v for row in family_rows)]} for index, (key, label, vals) in enumerate(zip(KEYS, LABELS, values))]
        family_rows.sort(key=lambda r: tuple(values[i].index(r["options"][key]) for i, key in enumerate(KEYS)))
        old_records = {p["handle"]: p for p in old["products"]} if old else {}
        records = [copy.deepcopy(old_records[r["handle"]]) if r["handle"] in old_records else {"handle": r["handle"], "url": r["url"], "title": r["title"], "sort_order": i, "options": r["options"]} for i, r in enumerate(family_rows)]
        groups.append({"id": group_id, "label": f"Hotbath {series} {family}", "menus": menus, "products": records})
        for row in family_rows:
            row["group_id"] = group_id
        mapping.extend(family_rows)
        metrics.append({"family": family, "group_id": group_id, "status": "READY", "products": len(records), "colors": len(menus[0]["values"]), "book_sources": rules[family]["sources"], "partial_title_corroboration": sum(bool(r["title_missing_keys"]) for r in family_rows), "existing_records_preserved": len(old_records)})
    data = {"version": "hotbath-book-config-groups-20261024", "generated_at": snapshot["captured_at"], "groups": groups}
    review = {"schema": "hotbath-config-review-v1", "excluded": excluded, "cases": reviews, "family_metrics": metrics, "limits": ["Only exact source-confirmed family option grammars are decoded.", "No article, stock or price is invented; product records retain current handles.", "Missing title descriptions can be filled by explicit book options; contradictory descriptions are excluded.", "SPOM in title, SKU or handle is excluded independently of prefix."]}
    metadata = {"schema": "hotbath-config-mapping-v1", "groups": len(groups), "product_count": len(mapping), "families": metrics, "products": mapping}
    return data, review, metadata


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, default=Path('/workspace/scratch/6866aa3baeaf/hotbath-menu-20261024'))
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).parent)
    args = parser.parse_args()
    source = args.source_dir
    snapshot = json.loads((source / 'catalog_snapshot.json').read_text())
    book = json.loads((source / 'book_rules.json').read_text())
    existing = json.loads((source / 'baseline/product-switcher-data.json').read_text())
    data, review, mapping = build(snapshot, book, existing)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for filename, payload in [('config_groups.json', data), ('config_review.json', review), ('config_mapping.json', mapping)]:
        (args.output_dir / filename).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({"groups": len(data['groups']), "products": mapping['product_count'], "review_cases": len(review['cases']), "families": review['family_metrics']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
