#!/usr/bin/env python3
"""Map existing numeric-set titles to V2 options; never decode unknown SKU digits.

The numeric identifiers are catalogue identities. Product titles corroborate every
choice. The book corroborates the control/component distinctions, not the complete
IBS-ACE/COBBER numeric SKU scheme.
"""
from __future__ import annotations

import argparse
import collections
import json
import re
from pathlib import Path


PALETTE = [
    "Chroom", "Geborsteld nikkel", "Geborsteld messing", "Verouderd messing",
    "Mat wit", "Verouderd ijzer", "Gepolijst zwart PVD", "Geborsteld zwart PVD",
    "Geborsteld messing PVD", "Geborsteld koper PVD", "Geborsteld gunmetal PVD",
    "Tuscan bronze", "RVS 316", "Zwart chroom", "Mat zwart", "Gepolijst messing",
]
MENU_INFO = {
    "kleur": ("Kleur", "dropdown"),
    "breedte_diameter_hoofddouche": ("Hoofddouche", "buttons"),
    "type_bevestiging_hoofddouche": ("Bevestiging hoofddouche", "buttons"),
    "type_handdouche": ("Handdouche", "buttons"),
    "bevestiging_handdouche": ("Handdouchehouder", "buttons"),
}
VALUE_ORDER = {
    "kleur": PALETTE,
    "breedte_diameter_hoofddouche": ["20 cm", "23 cm Velvet", "30 cm"],
    "type_bevestiging_hoofddouche": ["Wandarm", "Plafondbuis 15 cm", "Plafondbuis 30 cm"],
    "type_handdouche": ["Staafmodel", "Rond model", "3 standen"],
    "bevestiging_handdouche": ["Wandhouder", "Glijstang"],
}


def text_normalize(value: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[–—-]", " ", value.casefold())).strip()


def color_from_title(title: str) -> str:
    text = text_normalize(title)
    candidates = [c for c in PALETTE if re.search(r"(?<!\w)" + re.escape(c.casefold()) + r"(?!\w)", text)]
    candidates.sort(key=len, reverse=True)
    if not candidates:
        raise ValueError("COLOR_NOT_IN_TITLE")
    longest = candidates[0]
    # A shorter label nested in the full PVD name is harmless; unrelated colors
    # in one title would be an unsafe conflict.
    if any(c.casefold() not in longest.casefold() for c in candidates[1:]):
        raise ValueError("MULTIPLE_COLORS_IN_TITLE")
    return longest


def numeric_family(sku: str) -> str | None:
    if re.fullmatch(r"IBS-ACE1\d{3}", sku):
        return "ace_thermostatic_2way"
    if re.fullmatch(r"IBS-ACE2\d{3}", sku):
        return "ace_mixer_2way"
    if re.fullmatch(r"IBS-ACE3\d{3}", sku):
        return "ace_3way_velvet"
    if re.fullmatch(r"COBBER3\d{3}", sku):
        return "cobber_slidebar_set"
    if re.fullmatch(r"COBBER4\d{3}", sku):
        return "cobber_beam_mixer_set"
    return None


def parse_options(sku: str, title: str) -> tuple[str, dict[str, str]]:
    family = numeric_family(sku)
    if not family:
        raise ValueError("UNKNOWN_NUMERIC_FAMILY")
    text = text_normalize(title)
    opts = {"kleur": color_from_title(title)}
    if family in {"ace_thermostatic_2way", "ace_mixer_2way"}:
        if not re.search(r"\b2\s+weg\b", text):
            raise ValueError("CONTROL_2WAY_NOT_IN_TITLE")
        expected_thermostat = family == "ace_thermostatic_2way"
        if expected_thermostat != ("thermostatisch" in text):
            raise ValueError("CATALOGUE_CODE_CONTROL_TITLE_CONFLICT")
        if not expected_thermostat and "mengkraan" not in text:
            raise ValueError("MIXER_CONTROL_NOT_IN_TITLE")
        diameter = re.search(r"(20|23|30)\s*cm\s*(velvet\s*)?hoofddouche", text)
        if not diameter:
            raise ValueError("HEAD_SIZE_NOT_IN_TITLE")
        if (diameter.group(1) == "23") != bool(diameter.group(2)):
            raise ValueError("VELVET_HEAD_TITLE_CONFLICT")
        opts["breedte_diameter_hoofddouche"] = diameter.group(1) + " cm" + (" Velvet" if diameter.group(2) else "")
        ceiling = re.search(r"plafondbuis\s*(15|30)\s*cm", text)
        if ceiling:
            opts["type_bevestiging_hoofddouche"] = "Plafondbuis " + ceiling.group(1) + " cm"
        elif "wandarm" in text:
            opts["type_bevestiging_hoofddouche"] = "Wandarm"
        else:
            raise ValueError("HEAD_MOUNT_NOT_IN_TITLE")
        if "staafhanddouche" in text or "staaf handdouche" in text:
            opts["type_handdouche"] = "Staafmodel"
        elif re.search(r"3\s+standen\s+handdouche", text):
            opts["type_handdouche"] = "3 standen"
        else:
            raise ValueError("HANDSHOWER_NOT_IN_TITLE")
        if "wandhouder" in text or "wandsteun" in text:
            opts["bevestiging_handdouche"] = "Wandhouder"
        elif "glijstang" in text:
            opts["bevestiging_handdouche"] = "Glijstang"
        else:
            raise ValueError("HANDSHOWER_MOUNT_NOT_IN_TITLE")
    elif family == "ace_3way_velvet":
        if not re.search(r"\b3\s+weg\b", text) or "inbouw hoofddouche velvet" not in text:
            raise ValueError("THREE_WAY_VELVET_NOT_IN_TITLE")
    elif family == "cobber_slidebar_set":
        if "glijstangset" not in text:
            raise ValueError("SLIDEBAR_SET_NOT_IN_TITLE")
        if "staafhanddouche" in text or "staaf handdouche" in text:
            opts["type_handdouche"] = "Staafmodel"
        elif "ronde handdouche" in text:
            opts["type_handdouche"] = "Rond model"
        else:
            raise ValueError("HANDSHOWER_NOT_IN_TITLE")
    elif family == "cobber_beam_mixer_set":
        if "mengkraan" not in text or "beam hoofddouche" not in text or "inbouw doucheset" not in text:
            raise ValueError("BEAM_MIXER_SET_NOT_IN_TITLE")
    return family, opts


FAMILIES = {
    "ace_thermostatic_2way": ("hotbath-ace-numeric-2weg-thermostatische-inbouw-doucheset", "Hotbath Ace 2-weg thermostatische inbouwdoucheset"),
    "ace_mixer_2way": ("hotbath-ace-numeric-2weg-mengkraan-inbouw-doucheset", "Hotbath Ace 2-weg inbouwdoucheset met mengkraan"),
    "ace_3way_velvet": ("hotbath-ace-numeric-3weg-velvet-inbouw-doucheset", "Hotbath Ace 3-weg inbouwdoucheset met Velvet hoofddouche"),
    "cobber_slidebar_set": ("hotbath-cobber-numeric-glijstangsets", "Hotbath Cobber glijstangset"),
    "cobber_beam_mixer_set": ("hotbath-cobber-numeric-beam-mengkraan-inbouw-doucheset", "Hotbath Cobber inbouwdoucheset met Beam hoofddouche en mengkraan"),
}


def fixed_title_signature(row: dict) -> str:
    """Remove only the choices actually represented by this row's option fields."""
    text = text_normalize(row["title"])
    text = re.sub(r"(?<!\w)" + re.escape(text_normalize(row["sku"])) + r"(?!\w)", " ", text)
    options = row["options"]
    text = re.sub(r"(?<!\w)" + re.escape(options["kleur"].casefold()) + r"(?!\w)", " ", text)
    if "breedte_diameter_hoofddouche" in options:
        head = options["breedte_diameter_hoofddouche"]
        size = head.split()[0]
        velvet = r"velvet\s*" if "Velvet" in head else ""
        text = re.sub(r"(?<!\w)" + re.escape(size) + r"\s*cm\s*" + velvet + r"hoofddouche\b", " ", text)
    if "type_bevestiging_hoofddouche" in options:
        mount = options["type_bevestiging_hoofddouche"]
        pattern = r"\bwandarm\b" if mount == "Wandarm" else r"\bplafondbuis\s*" + re.escape(mount.split()[1]) + r"\s*cm\b"
        text = re.sub(pattern, " ", text)
    if "type_handdouche" in options:
        pattern = {
            "Staafmodel": r"\bstaaf\s*handdouche\b",
            "Rond model": r"\bronde\s+handdouche\b",
            "3 standen": r"\b3\s+standen\s+handdouche\b",
        }[options["type_handdouche"]]
        text = re.sub(pattern, " ", text)
    if "bevestiging_handdouche" in options:
        pattern = r"\b(?:wandhouder|wandsteun)\b" if options["bevestiging_handdouche"] == "Wandhouder" else r"\bglijstang\b"
        text = re.sub(pattern, " ", text)
    return re.sub(r"\s+", " ", text).strip()


def analyse(catalog: dict, existing: dict) -> dict:
    if catalog.get("complete") is not True:
        raise ValueError("Complete snapshot required")
    rows_by_family = collections.defaultdict(list)
    review, excluded = [], []
    handle_groups = collections.defaultdict(set)
    for group in existing["groups"]:
        for product in group["products"]:
            handle_groups[product["handle"]].add(group["id"])
    for p in catalog["products"]:
        vc = p.get("variants") or {}
        vs = vc.get("nodes") or []
        if len(vs) != 1:
            continue
        sku = (vs[0].get("sku") or "").strip()
        family = numeric_family(sku)
        if not family:
            continue
        ident = {"sku": sku, "id": p["id"], "handle": p["handle"], "title": p["title"]}
        if "SPOM" in " ".join([sku, p["title"], p["handle"]]).upper() or "TEST" in sku.upper() or p["title"].upper().startswith("TEST"):
            excluded.append({**ident, "reason": "SPOM_OR_TEST"})
            continue
        if p.get("status") != "ACTIVE" or not p.get("publishedAt") or vc.get("pageInfo", {}).get("hasNextPage"):
            excluded.append({**ident, "reason": "INACTIVE_UNPUBLISHED_OR_INCOMPLETE_VARIANTS"})
            continue
        try:
            parsed_family, opts = parse_options(sku, p["title"])
        except ValueError as e:
            review.append({**ident, "reason": str(e)})
            continue
        groups = set(handle_groups[p["handle"]])
        current = (p.get("group") or {}).get("value")
        if current:
            groups.add(current)
        rows_by_family[parsed_family].append({**ident, "url": "/products/" + p["handle"], "options": opts, "existing_groups": sorted(groups)})
    groups, records, family_results = [], [], []
    for family, rows in sorted(rows_by_family.items()):
        group_id, label = FAMILIES[family]
        keys = [key for key in MENU_INFO if any(key in row["options"] for row in rows)]
        tuples, duplicates = {}, []
        existing_ids = sorted({g for row in rows for g in row["existing_groups"]})
        for row in rows:
            key = tuple(row["options"].get(k) for k in keys)
            if key in tuples:
                duplicates.append([tuples[key], row["sku"]])
            tuples[key] = row["sku"]
        reasons = []
        if duplicates:
            reasons.append("DUPLICATE_CHOICE_TUPLES")
        if existing_ids:
            reasons.append("EXISTING_GROUP_RECONCILIATION_REQUIRED")
        if any(set(r["options"]) != set(keys) for r in rows):
            reasons.append("MISSING_OPTION_FIELDS")
        signatures = {fixed_title_signature(row) for row in rows}
        if len(signatures) != 1:
            reasons.append("UNMODELED_FIXED_TITLE_DIFFERENCE")
        if len(rows) < 2:
            reasons.append("SINGLE_ARTICLE_NO_MENU")
        status = "REVIEW" if reasons else "TITLE_CONFIRMED_READY_FOR_PREVIEW"
        family_results.append({"family": family, "group_id": group_id, "label": label, "count": len(rows), "status": status, "reason_flags": reasons, "existing_group_ids": existing_ids, "duplicate_tuples": duplicates, "fixed_title_signature_count":len(signatures), "fixed_title_signatures":sorted(signatures), "option_counts": {k:len({r["options"].get(k) for r in rows}) for k in keys}, "book_scope": "COMPONENT_AND_CONTROL_DISTINCTIONS_ONLY; NUMERIC_SET_SCHEME_NOT_FOUND_IN_EDITION18"})
        if reasons:
            continue
        def order(row):
            return tuple(VALUE_ORDER[k].index(row["options"][k]) for k in keys)
        rows.sort(key=order)
        menus = []
        for i, key in enumerate(keys):
            values = [x for x in VALUE_ORDER[key] if any(r["options"][key] == x for r in rows)]
            label_key, display = MENU_INFO[key]
            menus.append({"key": key, "label": label_key, "order": i+1, "display_type":display, "hide_if_single_value":True, "values":values})
        products = [{"handle":r["handle"], "url":r["url"], "title":r["title"], "sort_order":i, "options":r["options"]} for i,r in enumerate(rows)]
        groups.append({"id":group_id, "label":label, "menus":menus, "products":products})
        records.extend([{**r,"group_id":group_id,"evidence":"EVERY_CHOICE_EXPLICIT_IN_CURRENT_PRODUCT_TITLE; NO_NUMERIC_DIGIT_DECODING"} for r in rows])
    return {"schema":"hotbath-numeric-set-analysis-v1", "source":"Current complete Shopify snapshot; 2026-10-24", "book_corroboration":[{"printed_page":307,"pdf_page":309,"models":["AC129"],"fact":"Concealed mixer with 2-way diverter"},{"printed_page":308,"pdf_page":310,"models":["AC009","AC039"],"fact":"Thermostats with 2-way and 3-way stop/diverter; control distinction only"}],"families":family_results,"groups":groups,"records":records,"review":review,"excluded":excluded,"metrics":{"selected_numeric_rows":sum(len(x) for x in rows_by_family.values())+len(review)+len(excluded),"ready_groups":len(groups),"ready_records":len(records),"review_records":len(review),"excluded_records":len(excluded)}}


def main():
    ap=argparse.ArgumentParser();ap.add_argument("--base-dir",type=Path,default=Path('/workspace/scratch/6866aa3baeaf/hotbath-menu-20261024'));ap.add_argument("--output-dir",type=Path,default=Path(__file__).resolve().parent)
    args=ap.parse_args();catalog=json.loads((args.base_dir/'catalog_snapshot.json').read_text());existing=json.loads((args.base_dir/'baseline/product-switcher-data.json').read_text())
    result=analyse(catalog,existing);args.output_dir.mkdir(parents=True,exist_ok=True)
    (args.output_dir/'numeric_set_analysis.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({"metrics":result['metrics'],"families":result['families']},ensure_ascii=False))


if __name__=='__main__':main()
