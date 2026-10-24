#!/usr/bin/env python3
"""Read-only, reproducible Hotbath menu coverage and conservative family proposals.

No Shopify writes. Existing groups are preserved as the source of current dimensions.
New cross-model dimensions are proposed only for explicitly sourced IBS70/IBS7009.
New colour-only siblings keep the complete model code and configuration suffix.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
import unicodedata
from pathlib import Path

PALETTE = {
    "CR": ("Chroom", ["chroom", "chrome"]),
    "GN": ("Geborsteld nikkel", ["geborsteld nikkel"]),
    "BB": ("Geborsteld messing", ["geborsteld messing"]),
    "AB": ("Verouderd messing", ["verouderd messing"]),
    "WH": ("Mat wit", ["mat wit", "wit"]),
    "AI": ("Verouderd ijzer", ["verouderd ijzer"]),
    "BBP": ("Geborsteld messing PVD", ["geborsteld messing pvd"]),
    "BCP": ("Geborsteld koper PVD", ["geborsteld koper pvd"]),
    "MBP": ("Geborsteld zwart PVD", ["geborsteld zwart pvd"]),
    "PBP": ("Gepolijst zwart PVD", ["gepolijst zwart pvd"]),
    "BGP": ("Geborsteld gunmetal PVD", ["geborsteld gunmetal pvd", "geborsteld gunmetal"]),
    "TB": ("Tuscan bronze", ["tuscan bronze", "tuscany bronze"]),
    "IX": ("RVS 316", ["rvs 316", "geborsteld rvs", "rvs", "inox"]),
    # Historical codes are recognised for reconciliation, not newly approved.
    "BL": ("Mat zwart", ["mat zwart"]),
    "BK": ("Zwart chroom", ["zwart chroom"]),
    "NB": ("Gepolijst messing", ["gepolijst messing"]),
    "BC": ("Geborsteld koper", ["geborsteld koper"]),
    "RG": ("Roze goud", ["roze goud", "rosegoud", "rose goud"]),
    "BNP": ("Geborsteld nikkel PVD", ["geborsteld nikkel pvd"]),
    "GBP": ("Gepolijst messing PVD", ["gepolijst messing pvd"]),
}
CURRENT_BOOK_CODES = {"CR", "GN", "BB", "AB", "WH", "AI", "BBP", "BCP", "MBP", "PBP", "BGP", "TB", "IX"}
COLOR_RX = re.compile(r"^(.*\d[A-Z0-9.]*?)(" + "|".join(sorted(PALETTE, key=lambda s: (-len(s), s))) + r")(\d*|(?:-\d+)+)$", re.I)
BOOK_IBS = {"IBS70": {"printed_page": 200, "pdf_page": 202}, "IBS7009": {"printed_page": 199, "pdf_page": 201}}
SERIES = ["cobber @work", "cobber work", "cobber x", "guy diamond", "guy row", "gent", "archie", "chap", "guy", "cobber", "gal", "buddy", "ace", "mate", "fellow", "tron", "laddy", "friendo", "bloke", "amice", "pal"]


def norm(s):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", str(s)).lower().replace("–", "-").replace("—", "-")).strip()


def sku_of(p):
    nodes = p.get("variants", {}).get("nodes", [])
    return str(nodes[0].get("sku") or "").strip() if nodes else ""


def split_sku(sku):
    m = COLOR_RX.fullmatch(sku.upper())
    return {"model": m[1], "colour_code": m[2], "configuration_suffix": m[3], "colour": PALETTE[m[2]][0]} if m else None


def title_colours(title):
    text = norm(title)
    matches = []
    for code, (_, aliases) in PALETTE.items():
        for alias in aliases:
            match = re.search(r"(?<!\w)" + re.escape(alias) + r"(?!\w)", text)
            if match:
                matches.append((match.start(), match.end(), code, alias))
    # Keep the longest colour phrase at an overlapping position (PVD != plain).
    matches.sort(key=lambda r: (-(r[1] - r[0]), r[0], r[2]))
    selected = []
    for match in matches:
        if not any(match[0] < other[1] and other[0] < match[1] for other in selected):
            selected.append(match)
    return sorted({m[2] for m in selected})


def title_signature(p):
    text = norm(p["title"])
    sku = norm(sku_of(p))
    if sku:
        text = text.replace(sku, " ")
    # Model words are held in the SKU key; names only corroborate product type.
    text = re.sub(r"\b[a-z]+\d+[a-z0-9.\-/]*\b", " ", text)
    for _, aliases in PALETTE.values():
        for alias in sorted(aliases, key=len, reverse=True):
            text = re.sub(r"(?<!\w)" + re.escape(alias) + r"(?!\w)", " ", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    words = text.split()
    discard = {"hotbath", "pvd", "opbouw"}
    for series in SERIES:
        discard.update(series.replace("@", " ").split())
    return " ".join(word for word in words if word not in discard)


def product_kind(p):
    s = norm(p["title"])
    if "doucheset" in s or "regendouche" in s:
        return "Douchesets"
    if "wastafel" in s or "fonteinkraan" in s:
        return "Wastafel- en fonteinkranen"
    if "hoofddouche" in s or "wandarm" in s or "plafondbuis" in s:
        return "Hoofddouches en bevestiging"
    if "spiegel" in s or "led" in s:
        return "Spiegels en verlichting"
    if "afbouw" in s or "inbouwdeel" in s or "inbouwbox" in s:
        return "Afbouw- en inbouwdelen"
    if "kraan" in s or "thermostaat" in s:
        return "Overige kranen"
    return "Accessoires en overige"


def ibs_options(parsed):
    suffix = parsed["configuration_suffix"]
    if any(c not in "123457" for c in suffix) or len(set(suffix)) != len(suffix):
        return None
    if ("2" in suffix and "3" in suffix) or ("4" in suffix and "5" in suffix):
        return None
    if suffix != "".join(c for c in "123457" if c in suffix):
        return None
    return {
        "kleur": parsed["colour"],
        "type_handdouche": "Rond" if "1" in suffix else "Staaf",
        "breedte_diameter_hoofddouche": "25 cm" if "4" in suffix else "30 cm" if "5" in suffix else "20 cm",
        "type_bevestiging_hoofddouche": "Plafondbuis 15 cm" if "2" in suffix else "Plafondbuis 30 cm" if "3" in suffix else "Wandarm",
        "met_glijstang": "Ja" if "7" in suffix else "Nee",
    }


def ibs_title_conflicts(p, opts):
    s = norm(p["title"])
    seen = {}
    if re.search(r"ronde?\s*handdouche", s): seen["type_handdouche"] = "Rond"
    elif re.search(r"staaf\s*handdouche", s): seen["type_handdouche"] = "Staaf"
    diameter = re.search(r"(\d+)\s*cm\s*(?:ronde\s*)?hoofddouche", s) or re.search(r"[øØ]\s*(\d+)\s*cm", s)
    if diameter: seen["breedte_diameter_hoofddouche"] = diameter[1] + " cm"
    length = re.search(r"(\d+)\s*cm\s*plafondbuis", s) or re.search(r"plafondbuis\s*(\d+)\s*cm", s)
    if length: seen["type_bevestiging_hoofddouche"] = "Plafondbuis " + length[1] + " cm"
    elif "wandarm" in s: seen["type_bevestiging_hoofddouche"] = "Wandarm"
    if "glijstang" in s: seen["met_glijstang"] = "Ja"
    elif "wandhouder" in s or "wandsteun" in s: seen["met_glijstang"] = "Nee"
    return [{"field": k, "title_value": v, "sku_value": opts[k]} for k, v in seen.items() if opts[k] != v]


def summarize_product(p, parsed=None):
    result = {"id": p["id"], "handle": p["handle"], "sku": sku_of(p), "title": p["title"], "published": bool(p.get("publishedAt")), "current_group": (p.get("group") or {}).get("value")}
    if parsed: result.update(parsed)
    return result


def audit(snapshot, baseline, book_rules=None):
    if not snapshot.get("complete"):
        raise ValueError("Refusing a partial catalog export")
    products = snapshot["products"]
    if len({p["id"] for p in products}) != len(products):
        raise ValueError("Duplicate product IDs in export")
    by_handle = {p["handle"]: p for p in products}
    existing_groups = baseline["groups"]
    group_by_id = {g["id"]: g for g in existing_groups}
    records_by_handle = collections.defaultdict(list)
    for g in existing_groups:
        for r in g["products"]:
            records_by_handle[r["handle"]].append((g, r))
    existing_handles = set(records_by_handle)
    reviews = []
    parsed_by_id = {}
    buckets = collections.defaultdict(list)
    coverage = collections.Counter()
    tests, parts, eligible, inactive = [], [], [], []
    sku_products = collections.defaultdict(list)
    color_title_checked = 0
    for p in products:
        sku = sku_of(p)
        sku_products[sku.upper()].append(p)
        group = (p.get("group") or {}).get("value")
        recs = records_by_handle[p["handle"]]
        matching = [gr for gr, _ in recs if group and gr["id"] == group]
        state = "CONNECTED" if matching else "JSON_WITHOUT_MATCHING_GROUP" if recs else "GROUP_WITHOUT_JSON_RECORD" if group else "NO_GROUP"
        coverage[state] += 1
        if len(recs) > 1:
            reviews.append({"type": "HANDLE_IN_MULTIPLE_GROUPS", **summarize_product(p), "groups": [g["id"] for g, _ in recs]})
        if state in {"JSON_WITHOUT_MATCHING_GROUP", "GROUP_WITHOUT_JSON_RECORD"}:
            reviews.append({"type": state, **summarize_product(p), "json_groups": [g["id"] for g, _ in recs]})
        if sku.upper().startswith("TEST") or re.search(r"\btest(?:product)?\b|\bpilot\b", norm(p["title"])):
            tests.append(p)
            continue
        if sku.upper().startswith("SPOM"):
            parts.append(p)
            continue
        if p.get("status") != "ACTIVE" or not p.get("publishedAt"):
            inactive.append(p)
            reviews.append({"type": "INACTIVE_OR_UNPUBLISHED_EXCLUDED_FROM_PROPOSALS", **summarize_product(p), "status": p.get("status")})
            continue
        eligible.append(p)
        if p.get("variants", {}).get("pageInfo", {}).get("hasNextPage"):
            reviews.append({"type": "MULTI_VARIANT_PRODUCT_REQUIRES_FULL_VARIANT_EXPORT", **summarize_product(p)})
            continue
        parsed = split_sku(sku)
        if not parsed:
            continue
        parsed_by_id[p["id"]] = parsed
        buckets[(parsed["model"], parsed["configuration_suffix"])].append(p)
        found = title_colours(p["title"])
        if found:
            color_title_checked += 1
            if parsed["colour_code"] not in found:
                reviews.append({"type": "SKU_TITLE_COLOUR_CONFLICT", **summarize_product(p, parsed), "title_colour_codes": found})
        for g, r in recs:
            choice = r.get("options", {}).get("kleur")
            if choice and norm(choice) not in {norm(parsed["colour"]), *[norm(a) for a in PALETTE[parsed["colour_code"]][1]]}:
                # IX legacy RVS/RVS316 labels are accepted as aliases above.
                reviews.append({"type": "SKU_EXISTING_MENU_COLOUR_CONFLICT", **summarize_product(p, parsed), "existing_group": g["id"], "menu_colour": choice})
    for sku, ps in sku_products.items():
        if not sku or len(ps) > 1:
            reviews.append({"type": "MISSING_OR_DUPLICATE_SKU", "sku": sku, "products": [summarize_product(p) for p in ps]})

    stale = [{"group": g["id"], "handle": r["handle"]} for g in existing_groups for r in g["products"] if r["handle"] not in by_handle]
    for row in stale:
        reviews.append({"type": "STALE_JSON_HANDLE", **row})
    existing_reports = []
    for g in existing_groups:
        rs = g["products"]
        current = [by_handle[r["handle"]] for r in rs if r["handle"] in by_handle]
        combos = collections.defaultdict(list)
        for r in rs:
            combos[tuple((m["key"], str(r.get("options", {}).get(m["key"], ""))) for m in g["menus"])].append(r["handle"])
        duplicate_combos = [hs for hs in combos.values() if len(hs) > 1]
        missing_options = [r["handle"] for r in rs if any(r.get("options", {}).get(m["key"]) in (None, "") for m in g["menus"])]
        if duplicate_combos or missing_options:
            reviews.append({"type": "EXISTING_GROUP_COMBINATION_ERROR", "group": g["id"], "duplicate_combinations": duplicate_combos, "missing_options": missing_options})
        existing_reports.append({"group_id": g["id"], "action": "PRESERVE_EXISTING_GROUP", "record_count": len(rs), "current_handle_count": len(current), "connected_current_count": sum((p.get("group") or {}).get("value") == g["id"] for p in current), "menus": [{"key": m["key"], "label": m["label"], "value_count": len(m.get("values", []))} for m in g["menus"]], "single_value_menus": [m["key"] for m in g["menus"] if len(m.get("values", [])) < 2], "duplicate_combinations": len(duplicate_combos), "missing_options": len(missing_options)})

    proposals = []
    advanced_ids = set()
    for model, source in BOOK_IBS.items():
        ps = [p for p in eligible if parsed_by_id.get(p["id"], {}).get("model") == model]
        if not ps: continue
        candidates, conflicts, invalid = [], [], []
        for p in ps:
            parsed = parsed_by_id[p["id"]]
            opts = ibs_options(parsed)
            if not opts:
                invalid.append(summarize_product(p, parsed)); continue
            bad = ibs_title_conflicts(p, opts)
            if bad: conflicts.append({**summarize_product(p, parsed), "conflicts": bad})
            candidates.append({**summarize_product(p, parsed), "options": opts})
            advanced_ids.add(p["id"])
        unique_options = {tuple(c["options"].items()) for c in candidates}
        duplicate_count = len(candidates) - len(unique_options)
        status = "READY_FOR_PREVIEW" if not conflicts and not invalid and not duplicate_count else "REVIEW_REQUIRED"
        existing_ids = sorted({g["id"] for p in ps for g, _ in records_by_handle[p["handle"]]})
        proposal = {"proposal_id": "book-" + model.lower(), "model": model, "kind": "Douchesets", "action": "ADD_OR_RECONCILE_BOOK_SOURCED_GROUP", "confidence": "HIGH" if status == "READY_FOR_PREVIEW" else "REVIEW", "status": status, "book_source": source, "products_count": len(candidates), "already_in_existing_json": sum(bool(records_by_handle[c["handle"]]) for c in candidates), "existing_group_ids": existing_ids, "choice_fields": ["kleur", "breedte_diameter_hoofddouche", "type_bevestiging_hoofddouche", "type_handdouche", "met_glijstang"], "option_counts": {k: len({c["options"][k] for c in candidates}) for k in candidates[0]["options"]} if candidates else {}, "duplicate_combinations": duplicate_count, "title_conflicts": conflicts, "invalid_sku_options": invalid, "reason": "Exact family-specific finish/option codes confirmed in Hotbath Edition 18; all real catalog products retained; no combinations generated.", "products": candidates}
        proposals.append(proposal)
        for conflict in conflicts:
            reviews.append({"type": "BOOK_SKU_TITLE_CONFIGURATION_CONFLICT", "model": model, **conflict})
        for bad in invalid:
            reviews.append({"type": "UNKNOWN_BOOK_OPTION_SUFFIX", "model": model, **bad})

    singleton_bucket_products = []
    existing_bucket_count = 0
    for (model, suffix), ps in sorted(buckets.items()):
        ps = [p for p in ps if p["id"] not in advanced_ids]
        if not ps: continue
        colors = [parsed_by_id[p["id"]]["colour_code"] for p in ps]
        if len(set(colors)) < 2:
            singleton_bucket_products.extend(p["id"] for p in ps)
            continue
        existing_ids = sorted({g["id"] for p in ps for g, _ in records_by_handle[p["handle"]]})
        uncovered = [p for p in ps if not records_by_handle[p["handle"]]]
        if not uncovered:
            existing_bucket_count += 1
            continue
        code_counts = collections.Counter(colors)
        duplicates = [c for c, n in code_counts.items() if n > 1]
        stem_counts = collections.Counter(title_signature(p) for p in ps)
        conflict_products = [p for p in ps if title_colours(p["title"]) and parsed_by_id[p["id"]]["colour_code"] not in title_colours(p["title"])]
        historical = sorted(set(colors) - CURRENT_BOOK_CODES)
        reason_flags = []
        if duplicates: reason_flags.append("DUPLICATE_COLOUR_COMBINATION")
        if conflict_products: reason_flags.append("SKU_TITLE_COLOUR_CONFLICT")
        if len(existing_ids) > 1: reason_flags.append("MULTIPLE_EXISTING_GROUPS")
        if historical: reason_flags.append("HISTORICAL_FINISH_OUTSIDE_EDITION18_PALETTE")
        if len(stem_counts) > 1: reason_flags.append("TITLE_WORDING_VARIATION_REQUIRES_REVIEW")
        title_supported = all(parsed_by_id[p["id"]]["colour_code"] in title_colours(p["title"]) for p in ps)
        if not title_supported: reason_flags.append("COLOUR_NOT_CORROBORATED_IN_EVERY_TITLE")
        # Existing group dimension rules can assign options to new same-model colours.
        proposed = []
        for p in uncovered:
            parsed = parsed_by_id[p["id"]]
            options = {"kleur": parsed["colour"]}
            if len(existing_ids) == 1:
                source_options = [r["options"] for peer in ps for g, r in records_by_handle[peer["handle"]] if g["id"] == existing_ids[0]]
                noncolor = {tuple(sorted((k, v) for k, v in opts.items() if k != "kleur")) for opts in source_options}
                if len(noncolor) == 1:
                    options.update(dict(next(iter(noncolor))))
                else:
                    reason_flags.append("CANNOT_INFER_EXISTING_NONCOLOUR_OPTIONS")
            proposed.append({**summarize_product(p, parsed), "options": options})
        reason_flags = sorted(set(reason_flags))
        confidence = "HIGH" if not reason_flags else "REVIEW"
        proposals.append({"proposal_id": "colour-" + re.sub(r"[^a-z0-9]+", "-", (model + ("-" + suffix if suffix else "")).lower()), "model": model, "configuration_suffix": suffix, "kind": product_kind(ps[0]), "action": "AUGMENT_EXISTING_GROUP" if len(existing_ids) == 1 else "PROPOSE_NEW_COLOUR_GROUP", "confidence": confidence, "status": "READY_FOR_PREVIEW" if confidence == "HIGH" else "REVIEW_REQUIRED", "existing_group_ids": existing_ids, "products_count": len(ps), "new_products_count": len(uncovered), "choice_fields": ["kleur"], "colour_count": len(set(colors)), "title_signature_counts": dict(stem_counts), "reason_flags": reason_flags, "reason": "Identical complete SKU model and configuration suffix; only the finish code changes. No cross-model size/height inference.", "products": [summarize_product(p, parsed_by_id[p["id"]]) for p in ps], "new_products": proposed})
        if reason_flags:
            reviews.append({"type": "COLOUR_GROUP_REVIEW", "proposal_id": proposals[-1]["proposal_id"], "model": model, "configuration_suffix": suffix, "reason_flags": reason_flags, "sku_examples": [sku_of(p) for p in ps[:8]]})

    unmatched = [p for p in eligible if p["id"] not in parsed_by_id and not records_by_handle[p["handle"]]]
    unmatched_series = collections.defaultdict(list)
    for p in unmatched:
        sku = sku_of(p).upper()
        key = "IBS-ACE" if sku.startswith("IBS-ACE") else "COBBER numeric sets" if re.match(r"COBBER\d", sku) else "HB installation boxes" if sku.startswith("HB") else "Other unparsed"
        unmatched_series[key].append(p)
    for name, ps in unmatched_series.items():
        reviews.append({"type": "UNPARSED_PRODUCTS_FAMILY_REVIEW", "family": name, "count": len(ps), "reason": "No safe finish token found or SKU uses a numeric composition system; needs source-specific mapping.", "products": [summarize_product(p) for p in ps]})

    book_model_sources = collections.defaultdict(list)
    explicit_book_models = set()
    for family in (book_rules or {}).get("families", []):
        for model in family.get("members", []):
            explicit_book_models.add(model)
            book_model_sources[model].extend(family.get("sources", []))
    for row in (book_rules or {}).get("candidate_model_index", []):
        book_model_sources[row["model"]].extend(row.get("sources", []))
    for proposal in proposals:
        sources = book_model_sources[proposal["model"]]
        proposal["book_model_sources"] = [dict(t) for t in sorted({tuple(sorted(s.items())) for s in sources})]
        proposal["book_model_status"] = "EXPLICIT_FAMILY_RULE" if proposal["model"] in explicit_book_models else "MODEL_TOKEN_IN_CATALOGUE" if sources else "NOT_MATCHED_IN_CANDIDATE_INDEX"
        proposal["confidence_basis"] = "BOOK_OPTION_CODES_AND_CURRENT_SKU_TITLE" if proposal["action"] == "ADD_OR_RECONCILE_BOOK_SOURCED_GROUP" else "CURRENT_IDENTICAL_MODEL_SKU_AND_TITLE; BOOK_MODEL_INDEX_IS_SEPARATE_EVIDENCE"

    batches = []
    order = ["Douchesets", "Wastafel- en fonteinkranen", "Hoofddouches en bevestiging", "Overige kranen", "Afbouw- en inbouwdelen", "Spiegels en verlichting", "Accessoires en overige"]
    for kind in order:
        gs = [g for g in proposals if g["kind"] == kind]
        if not gs: continue
        batches.append({"kind": kind, "proposal_count": len(gs), "high_confidence_proposals": sum(g["confidence"] == "HIGH" for g in gs), "review_proposals": sum(g["confidence"] != "HIGH" for g in gs), "products_in_proposals": len({p["id"] for g in gs for p in g["products"]}), "new_products_in_proposals": len({p["id"] for g in gs for p in (g.get("new_products") or g["products"] if g["action"] == "ADD_OR_RECONCILE_BOOK_SOURCED_GROUP" else g.get("new_products", []))})})
    augmentation = [g for g in proposals if g["action"] == "AUGMENT_EXISTING_GROUP"]
    high_augmentation = [g for g in augmentation if g["confidence"] == "HIGH"]
    proposed_new_ids = {p["id"] for g in proposals for p in (g.get("new_products", g["products"]) if g["action"] == "ADD_OR_RECONCILE_BOOK_SOURCED_GROUP" else g.get("new_products", []))}
    high_new_ids = {p["id"] for g in proposals if g["confidence"] == "HIGH" for p in (g.get("new_products", g["products"]) if g["action"] == "ADD_OR_RECONCILE_BOOK_SOURCED_GROUP" else g.get("new_products", []))}
    uncovered = [p for p in eligible if not records_by_handle[p["handle"]]]
    summary = {
        "schema": "hotbath-menu-audit-v1", "captured_at": snapshot.get("captured_at"), "shop": snapshot.get("shop"),
        "source_sha256": hashlib.sha256(json.dumps(snapshot, sort_keys=True).encode()).hexdigest(),
        "catalog_products": len(products), "active_products": sum(p.get("status") == "ACTIVE" for p in products), "published_products": sum(bool(p.get("publishedAt")) for p in products),
        "excluded_test_products": len(tests), "service_parts_separate_scope": len(parts), "inactive_or_unpublished_excluded": len(inactive), "eligible_real_non_service_products": len(eligible),
        "existing_groups": len(existing_groups), "existing_json_records": sum(len(g["products"]) for g in existing_groups), "existing_json_unique_handles": len(existing_handles),
        "existing_handles_in_current_hotbath_catalog": sum(h in by_handle for h in existing_handles), "stale_json_handles": len(stale),
        "coverage": dict(coverage), "parsed_colour_model_products": len(parsed_by_id), "colour_titles_checked": color_title_checked,
        "real_non_service_uncovered_products": len(uncovered),
        "uncovered_with_no_detected_colour_sibling": sum(p["id"] in singleton_bucket_products for p in uncovered),
        "existing_menu_title_drift_records": sum(r.get("title") != by_handle[r["handle"]]["title"] for g in existing_groups for r in g["products"] if r["handle"] in by_handle),
        "existing_groups_with_detected_augmentation": len({group for g in augmentation for group in g["existing_group_ids"]}),
        "existing_groups_without_detected_augmentation": len(existing_groups) - len({group for g in augmentation for group in g["existing_group_ids"]}),
        "existing_augmentation_new_products": len({p["id"] for g in augmentation for p in g["new_products"]}),
        "high_confidence_existing_augmentation_groups": len({group for g in high_augmentation for group in g["existing_group_ids"]}),
        "high_confidence_existing_augmentation_products": len({p["id"] for g in high_augmentation for p in g["new_products"]}),
        "color_buckets_already_covered": existing_bucket_count, "single_colour_bucket_products": len(set(singleton_bucket_products)),
        "new_or_augmentation_proposals": len(proposals), "high_confidence_proposals": sum(g["confidence"] == "HIGH" for g in proposals), "review_proposals": sum(g["confidence"] != "HIGH" for g in proposals),
        "distinct_model_codes_in_proposals": len({g["model"] for g in proposals}),
        "proposed_product_count": len({p["id"] for g in proposals for p in g["products"]}),
        "proposed_new_product_count": len(proposed_new_ids), "high_confidence_proposed_new_product_count": len(high_new_ids),
        "unparsed_uncovered_products": len(unmatched), "review_types": dict(collections.Counter(r["type"] for r in reviews)),
        "batches": batches,
        "limits": ["Read-only analysis; proposals are not deployed or merchant approved.", "Proposal counts refer to colour/configuration buckets, not a final count of logical product families.", "Current code availability flags are not supplier stock and were not used to invent stock.", "Title-only inference is a proposal, not a verified technical specification.", "Single-colour buckets can still be members of a wider source-confirmed size/height family; they are not declared menu-unnecessary globally.", "Only IBS70 and IBS7009 cross-model option decoding is explicitly implemented here; book_rules.json may contain additional reviewed rules for subsequent batches."]
    }
    return summary, {"schema": "hotbath-family-proposals-v1", "existing_groups": existing_reports, "proposals": proposals}, {"schema": "hotbath-menu-review-v1", "excluded_tests": [summarize_product(p) for p in tests], "cases": reviews}


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot", type=Path, default=here / "catalog_snapshot.json")
    parser.add_argument("--baseline", type=Path, default=here / "baseline" / "product-switcher-data.json")
    parser.add_argument("--output", type=Path, default=here)
    parser.add_argument("--book-rules", type=Path, default=here / "book_rules.json")
    args = parser.parse_args()
    snapshot = json.loads(args.snapshot.read_text())
    baseline = json.loads(args.baseline.read_text())
    book_rules = json.loads(args.book_rules.read_text()) if args.book_rules.exists() else None
    summary, proposals, reviews = audit(snapshot, baseline, book_rules)
    args.output.mkdir(parents=True, exist_ok=True)
    for filename, data in [("audit_summary.json", summary), ("family_proposals.json", proposals), ("review_cases.json", reviews)]:
        (args.output / filename).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
