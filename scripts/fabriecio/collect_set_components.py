#!/usr/bin/env python3
"""Read-only extraction of explicitly included supplier shower-set components.

Input is the private catalog/HTML cache produced by collect_choices.py. Output is
private source evidence, never a Shopify mutation payload. Only mandatory bundle
rows with an explicit positive integer quantity and an exact catalog URL match
are accepted. Unbundled shower sets are reported for manual source review.
"""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

from lxml import html


ROW_XPATH = '//*[contains(concat(" ", normalize-space(@class), " "), " bundled_product_summary ")]'
SHOWER_SET = re.compile(r"showerset|(?:regen)?douche\s*set", re.I)
COMPONENT_KEYS = ("source_url", "quantity", "source_optional", "source_product_id")


def now():
    return datetime.now(timezone.utc).isoformat()


def clean_text(node):
    return " ".join(node.text_content().split())


def supplier_url(url):
    parsed = urlsplit(url)
    if parsed.scheme != "https" or parsed.hostname != "fabriecio.nl" or not parsed.path.startswith("/product/"):
        raise ValueError(f"Unexpected supplier product URL: {url}")
    return url


def cached_path(product, html_dir):
    url = supplier_url(product.get("requested_url") or product["source_url"])
    slug = urlsplit(url).path.rstrip("/").split("/")[-1]
    return html_dir / f"{slug}-{hashlib.sha256(url.encode()).hexdigest()[:10]}.html"


def single(nodes, context):
    if len(nodes) != 1:
        raise ValueError(f"Expected exactly one {context}; found {len(nodes)}")
    return nodes[0]


def parse_rows(raw, by_url):
    document = html.fromstring(raw)
    parts = []
    for row in document.xpath(ROW_XPATH):
        cart = single(row.xpath('.//*[@data-bundled_item_id]'), "bundle cart")
        href = supplier_url(single(row.xpath('.//a[contains(@class,"bundled_product_permalink")]/@href'), "component link"))
        target = by_url.get(href)
        if not target:
            raise ValueError(f"Component URL has no exact source-catalog match: {href}")
        optional = cart.get("data-optional")
        if optional != "no":
            raise ValueError(f"Component is not explicitly mandatory: {href}; optional={optional!r}")
        quantity_text = single(row.xpath('.//input[contains(@class,"bundled_qty")]/@value'), "explicit bundle quantity")
        if not re.fullmatch(r"[1-9][0-9]*", quantity_text):
            raise ValueError(f"Component has no positive integer quantity: {href}; quantity={quantity_text!r}")
        source_id = cart.get("data-product_id")
        item_id = cart.get("data-bundled_item_id")
        if not source_id or not source_id.isdigit() or not item_id or not item_id.isdigit():
            raise ValueError(f"Missing supplier product/bundle item ID: {href}")
        excerpt = clean_text(single(row.xpath('.//*[contains(@class,"bundled_product_excerpt")]'), "component excerpt"))
        title = target["title"]
        specs = target.get("specifications") or {}
        if re.fullmatch(r"Fabriecio\s+" + re.escape(target["sku"]), title, re.I):
            if not excerpt:
                raise ValueError(f"Generic component title has no descriptive source excerpt: {href}")
            display_title = excerpt
            color = specs.get("Kleur")
            if color and color.lower() not in display_title.lower():
                display_title += " – " + color
        else:
            display_title = title.replace("Fabriecio", "Verlavio")
        if "fabriecio" in display_title.lower():
            raise ValueError(f"Supplier brand remained in display title: {href}")
        parts.append({
            "sku": target["sku"],
            "quantity": int(quantity_text),
            "display_title": display_title,
            "source_url": href,
            "source_product_id": source_id,
            "source_bundle_item_id": item_id,
            "source_optional": optional,
            "source_title": cart.get("data-title"),
            "source_excerpt": excerpt,
            "catalog_title": title,
            "specifications": specs,
        })
    component_skus = [part["sku"] for part in parts]
    if len(component_skus) != len(set(component_skus)):
        raise ValueError("Duplicate component SKU rows require manual quantity review")
    return parts


def extract(catalog_path, html_dir):
    raw_catalog = catalog_path.read_bytes()
    products = json.loads(raw_catalog)["products"]
    by_url = {}
    source_skus = set()
    for product in products:
        url = supplier_url(product["source_url"])
        if url in by_url:
            raise ValueError(f"Duplicate source catalog URL: {url}")
        if not product.get("sku") or product["sku"] in source_skus:
            raise ValueError(f"Missing or duplicate source catalog SKU: {product.get('sku')!r}")
        source_skus.add(product["sku"])
        by_url[url] = product
    bundles, unbundled = [], []
    for product in products:
        if not SHOWER_SET.search(product["title"]):
            continue
        source_file = cached_path(product, html_dir)
        raw = source_file.read_bytes()
        parts = parse_rows(raw, by_url)
        entry = {
            "sku": product["sku"],
            "title": product["title"].replace("Fabriecio", "Verlavio"),
            "source_url": product["source_url"],
            "source_observed_at": product.get("observed_at"),
            "source_html_file": str(source_file.resolve()),
            "source_html_sha256": hashlib.sha256(raw).hexdigest(),
        }
        if parts:
            entry["components"] = parts
            bundles.append(entry)
        else:
            entry["status"] = "HOLD_NO_EXPLICIT_COMPONENT_LIST"
            unbundled.append(entry)
    if not bundles:
        raise ValueError("No bundled shower sets found; source scope requires review")
    return {
        "schema_version": 1,
        "created_at": now(),
        "source": "Explicit mandatory supplier bundle rows; quantities and exact catalog URL matches",
        "catalog_sha256": hashlib.sha256(raw_catalog).hexdigest(),
        "counts": {
            "shower_bundle_products": len(bundles),
            "component_rows": sum(len(bundle["components"]) for bundle in bundles),
            "unique_component_skus": len({part["sku"] for bundle in bundles for part in bundle["components"]}),
            "unbundled_shower_sets_for_manual_review": len(unbundled),
        },
        "bundles": bundles,
        "unbundled_shower_sets": unbundled,
    }, by_url


def verify_live(bundle, by_url):
    result = {"sku": bundle["sku"], "source_url": bundle["source_url"], "observed_at": now()}
    try:
        request = Request(supplier_url(bundle["source_url"]), headers={"User-Agent": "Badkamercity-Fabriecio-Catalogue/1.0"})
        with urlopen(request, timeout=20) as response:
            supplier_url(response.url)
            parts = parse_rows(response.read(), by_url)
            result["http_status"] = response.status
        actual = [{key: part[key] for key in COMPONENT_KEYS} for part in parts]
        expected = [{key: part[key] for key in COMPONENT_KEYS} for part in bundle["components"]]
        result.update(same_components=actual == expected, count=len(actual))
        if actual != expected:
            result["actual_if_mismatch"] = actual
    except Exception as error:
        result.update(same_components=False, error=str(error))
    return result


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, required=True, help="Private normalized-catalog.json")
    parser.add_argument("--html-dir", type=Path, required=True, help="Private supplier HTML cache")
    parser.add_argument("--output", type=Path, required=True, help="Private source evidence JSON; contains supplier URLs")
    parser.add_argument("--verify-live", action="store_true", help="Read each bundled source page again and require an exact inclusion match")
    args = parser.parse_args()
    result, by_url = extract(args.catalog, args.html_dir)
    if args.verify_live:
        checks = []
        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = [executor.submit(verify_live, bundle, by_url) for bundle in result["bundles"]]
            for future in as_completed(futures):
                checks.append(future.result())
        checks.sort(key=lambda check: check["sku"])
        result["live_verification"] = {"checked": len(checks), "all_match": all(check["same_components"] for check in checks), "results": checks}
    write_json(args.output, result)
    print(json.dumps({"output": str(args.output.resolve()), "counts": result["counts"], "live_all_match": result.get("live_verification", {}).get("all_match")}, ensure_ascii=False))
    if args.verify_live and not result["live_verification"]["all_match"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
