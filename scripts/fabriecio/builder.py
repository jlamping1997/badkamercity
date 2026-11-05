#!/usr/bin/env python3
"""Build a reviewable linked-product plan without changing Shopify."""

from __future__ import annotations

import argparse
import copy
import html
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit


def text(value):
    return " ".join(html.unescape(str(value or "")).split())


def source_url(value):
    parsed = urlsplit(str(value or ""))
    if parsed.scheme != "https" or parsed.hostname not in {
        "fabriecio.nl", "www.fabriecio.nl", "b2b.fabriecio.nl"
    } or not parsed.path.startswith("/product/"):
        return None
    return "https://fabriecio.nl" + parsed.path.rstrip("/") + "/"


def option_key(value):
    value = text(value)
    return value[3:] if value.startswith("pa_") else value


def options(record):
    return {option_key(k): text(v) for k, v in record.get("selected_options", {}).items()}


def shopify_rows(value):
    if isinstance(value, list):
        return value
    return value["data"]["products"]["nodes"]


def variants(product):
    values = product.get("variants", [])
    if isinstance(values, dict):
        return values.get("nodes", [x["node"] for x in values.get("edges", [])])
    return values


def image_url(product):
    image = (product.get("featuredMedia") or {}).get("preview") or {}
    url = (image.get("image") or {}).get("url")
    if not url:
        return None
    parsed = urlsplit(url)
    return url if parsed.scheme == "https" and parsed.hostname == "cdn.shopify.com" else None


def delivery(record):
    observed = []
    for message in record.get("stock_messages", []):
        message = message if isinstance(message, dict) else {"text": message}
        value = text(message.get("text"))
        if value:
            observed.append(value)
    states, expected, warnings = set(), set(), []
    for value in observed:
        folded = value.casefold()
        if folded == "op voorraad" or re.fullmatch(r"\d+\s+op voorraad", folded):
            states.add(True)
        elif folded.startswith("verwacht:"):
            states.add(False)
            expected.add(value)
        elif folded in {"niet op voorraad", "levertijd onbekend", "nooit meer leverbaar", "uitverkocht", "insufficient stock"}:
            states.add(False)
    for value in record.get("delivery_messages", []):
        value = text(value)
        if value.casefold().startswith("verwacht:"):
            expected.add(value)
    if len(states) > 1 or len(expected) > 1:
        warnings.append("conflicting_source_stock_or_expectation")
        state, expectation = None, None
    else:
        state = next(iter(states)) if states else None
        expectation = next(iter(expected)) if expected and state is False else None
    if not states:
        warnings.append("no_explicit_source_stock_state")
    discontinued = any(value.casefold() == "nooit meer leverbaar" for value in observed)
    if discontinued:
        warnings.append("source_discontinued")
        state, expectation = False, None
    result = {
        "in_stock": state,
        "expected_text": expectation,
        "discontinued": discontinued,
        "observed_at": record.get("observed_at"),
        "source_url": record.get("source_url"),
    }
    return result, warnings


def build_plan(catalogue, products):
    records = copy.deepcopy(catalogue.get("products", []))
    products = shopify_rows(products)
    sources_by_sku, sources_by_url, stores_by_sku = defaultdict(list), defaultdict(list), defaultdict(list)
    for record in records:
        sources_by_sku[text(record.get("sku"))].append(record)
        sources_by_url[source_url(record.get("source_url"))].append(record)
    for product in products:
        if text(product.get("vendor")).casefold() == "fabriecio":
            for variant in variants(product):
                stores_by_sku[text(variant.get("sku"))].append(product)

    holds, warnings, skipped = [], [], []
    reasons_by_group = defaultdict(list)
    normalized = {text(r.get("sku")): options(r) for r in records}
    group_by_sku = {text(r.get("sku")): r.get("group_id") or "single:" + text(r.get("sku")) for r in records}

    def hold(record, reason, detail=None):
        issue = {"sku": text(record.get("sku")), "reason": reason}
        if detail is not None:
            issue["detail"] = detail
        reasons_by_group[group_by_sku[text(record.get("sku"))]].append(issue)

    def target_for(record, menu, choice):
        resolved = source_url(choice.get("target_url"))
        matches = sources_by_url.get(resolved, []) if resolved else []
        if len(matches) != 1:
            hold(record, "unresolved_or_ambiguous_source_target", {
                "key": option_key(menu.get("key")), "value": text(choice.get("value")),
                "url": choice.get("target_url"), "matches": len(matches),
            })
            return None
        target = matches[0]
        if choice.get("target_sku") and text(choice["target_sku"]) != text(target.get("sku")):
            hold(record, "source_target_sku_mismatch", choice.get("target_url"))
            return None
        return target

    for record in records:
        sku = text(record.get("sku"))
        if not sku or len(sources_by_sku[sku]) != 1:
            hold(record, "missing_or_duplicate_source_sku")
        matches = stores_by_sku.get(sku, [])
        if len(matches) != 1 or (matches and len(variants(matches[0])) != 1):
            hold(record, "missing_ambiguous_or_multi_variant_shopify_product", len(matches))
        if matches and not re.fullmatch(r"[a-z0-9][a-z0-9-]*", str(matches[0].get("handle", ""))):
            hold(record, "invalid_shopify_handle")
        if not source_url(record.get("source_url")) or len(sources_by_url[source_url(record.get("source_url"))]) != 1:
            hold(record, "duplicate_or_invalid_source_url")
        menus = record.get("menus", [])
        keys = [option_key(m.get("key")) for m in menus]
        current = normalized[sku]
        if len(keys) != len(set(keys)) or any(not key for key in keys):
            hold(record, "duplicate_or_empty_menu_key")
        if menus and (set(keys) != set(current) or any(not v for v in current.values())):
            hold(record, "incomplete_current_options", {"keys": keys, "options": current})
        for menu in menus:
            key = option_key(menu.get("key"))
            values = [text(v.get("value")) for v in menu.get("values", [])]
            if not text(menu.get("label")) or not values or len(values) != len(set(values)) or any(not v for v in values):
                hold(record, "invalid_menu_values", key)
            if text(menu.get("selected")) != current.get(key) or current.get(key) not in values:
                hold(record, "current_menu_selection_mismatch", key)
            for choice in menu.get("values", []):
                target = target_for(record, menu, choice)
                if target is None:
                    continue
                expected = {**current, key: text(choice.get("value"))}
                actual = options(target)
                if actual != expected:
                    hold(record, "source_link_changes_other_option", {
                        "key": key, "value": text(choice.get("value")),
                        "target_sku": target["sku"], "expected": expected, "actual": actual,
                    })

    members_by_group = defaultdict(list)
    for record in records:
        if record.get("menus"):
            members_by_group[group_by_sku[text(record.get("sku"))]].append(record)
    for group_id, members in members_by_group.items():
        tuples = defaultdict(list)
        for record in members:
            tuples[tuple(sorted(options(record).items()))].append(record["sku"])
        for combination, skus in tuples.items():
            if len(skus) > 1:
                reasons_by_group[group_id].append({"reason": "duplicate_complete_combination", "skus": skus, "options": dict(combination)})

    updates, max_payload_products, choice_count, delivery_count = [], 0, 0, 0
    active_without_choices, active_without_active_sibling = 0, 0
    for record in records:
        sku = text(record.get("sku"))
        canonical = source_url(record.get("source_url"))
        if not sku or len(sources_by_sku[sku]) != 1 or not canonical or len(sources_by_url[canonical]) != 1:
            skipped.append({"sku": sku, "reason": "source_identity_not_eligible"})
            continue
        matches = stores_by_sku.get(sku, [])
        if len(matches) != 1 or len(variants(matches[0])) != 1:
            skipped.append({"sku": sku, "reason": "shopify_identity_not_eligible"})
            continue
        product = matches[0]
        if product.get("status") != "ACTIVE":
            skipped.append({"sku": sku, "reason": "shopify_not_active", "status": product.get("status")})
            continue
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", str(product.get("handle", ""))):
            skipped.append({"sku": sku, "reason": "invalid_shopify_handle"})
            continue
        row = {"sku": sku, "product_id": product["id"], "handle": product["handle"], "source_url": record.get("source_url")}
        delivery_value, delivery_warnings = delivery(record)
        row["delivery"] = delivery_value
        delivery_count += 1
        for warning in delivery_warnings:
            warnings.append({"sku": sku, "reason": warning})
        inventory = variants(product)[0]
        if delivery_value["in_stock"] is True and inventory.get("inventoryQuantity") == 0 and inventory.get("inventoryPolicy") == "DENY":
            warnings.append({"sku": sku, "reason": "source_available_shopify_quantity_zero_deny"})
        group_id = group_by_sku[sku]
        if reasons_by_group[group_id]:
            row["choices_hold"] = group_id
        elif record.get("menus"):
            destinations = {sku: record}
            menu_data = []
            for order, menu in enumerate(record["menus"], 1):
                menu_data.append({
                    "key": option_key(menu["key"]), "label": text(menu["label"]), "order": order,
                    "values": [text(c["value"]) for c in menu["values"]],
                    "display_type": "buttons",
                })
                for choice in menu["values"]:
                    target = sources_by_url[source_url(choice["target_url"])][0]
                    target_sku = text(target["sku"])
                    target_products = stores_by_sku.get(target_sku, [])
                    if len(target_products) == 1 and target_products[0].get("status") == "ACTIVE" and len(variants(target_products[0])) == 1:
                        destinations[target_sku] = target
                    else:
                        warnings.append({"sku": sku, "reason": "excluded_non_active_destination", "target_sku": target_sku})
            destination_data = []
            for order, (target_sku, target) in enumerate(destinations.items(), 1):
                stored = stores_by_sku[target_sku][0]
                destination_value = {
                    "handle": stored["handle"], "url": "/products/" + stored["handle"],
                    "title": stored["title"], "sort_order": order, "options": options(target),
                }
                image = image_url(stored)
                if image:
                    destination_value["swatch_url"] = image
                destination_data.append(destination_value)
            if len(destination_data) > 1:
                row["choices"] = {"groups": [{"id": group_id, "menus": menu_data, "products": destination_data}]}
                max_payload_products = max(max_payload_products, len(destination_data))
                choice_count += 1
            else:
                warnings.append({"sku": sku, "reason": "no_active_sibling_destination"})
                active_without_active_sibling += 1
        else:
            active_without_choices += 1
        updates.append(row)

    for group_id, issues in reasons_by_group.items():
        if issues:
            holds.append({"group_id": group_id, "skus": [r["sku"] for r in records if group_by_sku[text(r.get("sku"))] == group_id], "issues": issues})
    source_skus = set(sources_by_sku)
    missing = sorted(sku for sku, values in stores_by_sku.items() if len(values) == 1 and values[0].get("status") == "ACTIVE" and sku not in source_skus)
    summary = {
        "source_products": len(records), "shopify_products": len(products),
        "eligible_products": len(updates), "choice_products": choice_count,
        "delivery_products": delivery_count, "products_without_source_choices": sum(not r.get("menus") for r in records),
        "active_products_without_source_choices": active_without_choices,
        "active_products_without_active_sibling": active_without_active_sibling,
        "active_held_choice_products": sum(bool(row.get("choices_hold")) for row in updates),
        "held_groups": len(holds), "held_products": sum(len(h["skus"]) for h in holds),
        "max_source_group_products": max((len(g.get("skus", [])) for g in catalogue.get("groups", [])), default=0),
        "max_payload_products": max_payload_products,
        "missing_active_shopify_source_skus": missing,
        "warnings": dict(Counter(w["reason"] for w in warnings)),
        "skipped": dict(Counter(w["reason"] for w in skipped)),
        "malmo_pilot_skus": [r["sku"] for r in updates if r["sku"] in {"VSB_2001", "VSB_2002", "VSB_2003", "VSB_2004"} and r.get("choices")],
    }
    return {
        "schema_version": 1, "created_at": datetime.now(timezone.utc).isoformat(),
        "source_catalogue_created_at": catalogue.get("created_at"),
        "method": "Exact SKU join and observed one-step source links; every click loads the destination product's own menu.",
        "summary": summary, "updates": updates, "holds": holds, "warnings": warnings, "skipped": skipped,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--shopify", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    plan = build_plan(json.loads(args.source.read_text()), json.loads(args.shopify.read_text()))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(plan["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
