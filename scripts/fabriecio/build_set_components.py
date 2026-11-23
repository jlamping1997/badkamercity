#!/usr/bin/env python3
"""Build a private, reviewable set-contents plan; never writes to Shopify."""

from __future__ import annotations

import argparse
import html
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit


def text(value):
    return " ".join(html.unescape(str(value or "")).split())


def supplier_url(value):
    parsed = urlsplit(str(value or ""))
    return (parsed.scheme == "https"
            and parsed.hostname in {"fabriecio.nl", "www.fabriecio.nl", "b2b.fabriecio.nl"}
            and parsed.path.startswith("/product/")
            and not parsed.username and not parsed.password)


def variants(product):
    value = product.get("variants", [])
    return value.get("nodes", []) if isinstance(value, dict) else value


def public_title(value):
    title = re.sub("fabriecio", "Verlavio", text(value), flags=re.IGNORECASE)
    return title if title.casefold().startswith("verlavio ") else "Verlavio " + title


def encoded(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def build_plan(source, products):
    if not isinstance(source, dict) or not isinstance(source.get("bundles"), list):
        raise ValueError("Expected source.bundles array")
    if not isinstance(products, list):
        raise ValueError("Expected Shopify product array")
    by_sku = defaultdict(list)
    for product in products:
        for variant in variants(product):
            by_sku[text(variant.get("sku"))].append((product, variant))
    bundles = source["bundles"]
    counts = Counter(text(bundle.get("sku")) for bundle in bundles)
    updates, holds, skipped = [], [], []
    unbundled = source.get("unbundled_shower_sets", [])
    if not isinstance(unbundled, list):
        raise ValueError("Expected source.unbundled_shower_sets array")
    for record in unbundled:
        holds.append({
            "sku": text(record.get("sku")),
            "reason": "No explicit supplier component list; no set fields prepared",
            "source_status": record.get("status"), "source_url": record.get("source_url"),
            "source_html_sha256": record.get("source_html_sha256"),
        })

    def resolve(sku):
        matches = by_sku.get(sku, [])
        if len(matches) != 1:
            raise ValueError(f"SKU {sku!r}: expected exactly one Shopify match; got {len(matches)}")
        product, variant = matches[0]
        if len(variants(product)) != 1:
            raise ValueError(f"SKU {sku!r}: product must contain exactly one variant")
        if product.get("vendor") != "Verlavio":
            raise ValueError(f"SKU {sku!r}: vendor must be Verlavio")
        if product.get("status") != "ACTIVE" or not product.get("publishedAt"):
            raise ValueError(f"SKU {sku!r}: must be ACTIVE and published")
        if not re.fullmatch(r"gid://shopify/Product/\d+", str(product.get("id", ""))):
            raise ValueError(f"SKU {sku!r}: invalid product ID")
        if not re.fullmatch(r"gid://shopify/ProductVariant/\d+", str(variant.get("id", ""))):
            raise ValueError(f"SKU {sku!r}: invalid variant ID")
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", str(product.get("handle", ""))):
            raise ValueError(f"SKU {sku!r}: invalid handle")
        return product, variant

    for bundle in bundles:
        sku = text(bundle.get("sku"))
        try:
            if not sku or counts[sku] != 1:
                raise ValueError("Missing or duplicate source set SKU")
            if not supplier_url(bundle.get("source_url")):
                raise ValueError("Missing or invalid source set URL")
            if not bundle.get("source_observed_at") or not bundle.get("source_html_file"):
                raise ValueError("Missing source capture evidence")
            source_hash = bundle.get("source_html_sha256")
            if source_hash is not None and not re.fullmatch(r"[0-9a-f]{64}", source_hash):
                raise ValueError("Invalid source capture SHA-256")
            observed = datetime.fromisoformat(bundle["source_observed_at"].replace("Z", "+00:00"))
            if observed.tzinfo is None:
                raise ValueError("Source capture timestamp must include timezone")
            product, _ = resolve(sku)
            source_components = bundle.get("components")
            if not isinstance(source_components, list) or not source_components:
                raise ValueError("Missing included component rows")
            components, linked_ids, evidence = [], [], []
            seen_skus, seen_bundle_ids = set(), set()
            for component in source_components:
                component_sku = text(component.get("sku"))
                if not component_sku or component_sku == sku or component_sku in seen_skus:
                    raise ValueError("Missing, self-referencing or duplicate component SKU")
                seen_skus.add(component_sku)
                quantity = component.get("quantity")
                if type(quantity) is not int or quantity <= 0:
                    raise ValueError(f"Component {component_sku}: quantity must be a positive integer")
                if component.get("source_optional") != "no":
                    raise ValueError(f"Component {component_sku}: inclusion is not mandatory")
                item_id = text(component.get("source_bundle_item_id"))
                supplier_id = text(component.get("source_product_id"))
                if not item_id.isdigit() or item_id in seen_bundle_ids or not supplier_id.isdigit():
                    raise ValueError(f"Component {component_sku}: missing or duplicate supplier IDs")
                seen_bundle_ids.add(item_id)
                if not supplier_url(component.get("source_url")):
                    raise ValueError(f"Component {component_sku}: invalid supplier product URL")
                display_title = text(component.get("display_title"))
                if not display_title or display_title.casefold() in {
                    component_sku.casefold(), "fabriecio " + component_sku.casefold(),
                    "verlavio " + component_sku.casefold(),
                }:
                    raise ValueError(f"Component {component_sku}: missing descriptive display title")
                linked_product, linked_variant = resolve(component_sku)
                components.append({
                    "status": "VERIFIED_DESCRIPTION", "sku": component_sku,
                    "quantity": quantity, "product_id": linked_product["id"],
                    "variant_id": linked_variant["id"], "short_title": public_title(display_title),
                })
                if linked_product["id"] not in linked_ids:
                    linked_ids.append(linked_product["id"])
                evidence.append({
                    "sku": component_sku, "source_url": component["source_url"],
                    "source_product_id": supplier_id, "source_bundle_item_id": item_id,
                    "source_optional": "no", "quantity": quantity,
                })
            metafields = []
            for key, kind, wanted, alias in (
                ("set_components", "json", components, "components"),
                ("component_products", "list.product_reference", linked_ids, "links"),
            ):
                existing = product.get(alias)
                if existing is not None:
                    try:
                        same = existing.get("type") == kind and json.loads(existing["value"]) == wanted
                    except (KeyError, TypeError, ValueError):
                        same = False
                    if not same:
                        raise ValueError(f"Existing {key} differs; manual review required")
                    continue
                metafields.append({
                    "ownerId": product["id"], "namespace": "bc_data", "key": key,
                    "type": kind, "value": encoded(wanted), "compareDigest": None,
                })
            if not metafields:
                skipped.append({"sku": sku, "reason": "Both fields already exactly match"})
                continue
            updates.append({
                "sku": sku, "ownerId": product["id"], "handle": product["handle"],
                "components": components, "component_products": linked_ids,
                "metafields": metafields, "source_url": bundle["source_url"],
                "source_observed_at": bundle["source_observed_at"],
                "source_html_file": bundle["source_html_file"],
                "source_html_sha256": source_hash, "evidence": evidence,
            })
        except (KeyError, TypeError, ValueError) as error:
            holds.append({"sku": sku, "reason": str(error)})

    return {
        "schema_version": 1, "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_catalog_sha256": source.get("catalog_sha256"),
        "updates": updates, "holds": holds, "skipped": skipped,
        "summary": {
            "source_sets": len(bundles) + len(unbundled), "source_bundle_sets": len(bundles),
            "source_unbundled_sets": len(unbundled),
            "update_sets": len(updates), "held_sets": len(holds),
            "unchanged_sets": len(skipped),
            "metafield_writes": sum(len(update["metafields"]) for update in updates),
            "included_rows": sum(len(update["components"]) for update in updates),
            "unique_component_skus": len({row["sku"] for update in updates for row in update["components"]}),
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--shopify", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = build_plan(json.loads(args.source.read_text(encoding="utf-8")),
                        json.loads(args.shopify.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"]))


if __name__ == "__main__":
    main()
