#!/usr/bin/env python3
"""Read-only, resumable Wiesbaden source collection. Never writes to Shopify.

Raw third-party pages and shop snapshots belong outside this public repository.
Python 3.10+ and lxml are required. Run --help for commands.
"""
from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import html as html_std
import json
import re
import sys
import time
import unicodedata
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urljoin, urlparse
from urllib.request import Request, urlopen

from lxml import html

BASE = "https://www.wiesbaden.nl/"
VERSION = "2026-10-19.2"
UA = "BadkamerCity-productdata-audit/1.0"
PRODUCT_FIELDS = """__typename uid sku name url_key url_suffix canonical_url status visibility
description{html} short_description{html} meta_title meta_description
image{url label} media_gallery{url label disabled position}
price_range{minimum_price{regular_price{value currency} final_price{value currency}}}
categories{uid name url_path path level
breadcrumbs{category_uid category_name category_url_path category_level}}"""


def now():
    return datetime.now(timezone.utc).isoformat()


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
    temp.replace(path)


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def key(value):
    return hashlib.sha256(value.encode()).hexdigest()


def clean(value):
    return " ".join(str(value or "").split())


def slug(value):
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "_", value).strip("_")


def sku_key(value):
    # Do not remove punctuation or leading zeroes. Never use an EAN/barcode.
    return str(value or "").strip().upper()


def source_url(product):
    if product.get("canonical_url"):
        candidate = urljoin(BASE, product["canonical_url"])
    else:
        candidate = urljoin(BASE, product["url_key"] + (product.get("url_suffix") or ""))
    if urlparse(candidate).hostname != "www.wiesbaden.nl" or urlparse(candidate).scheme != "https":
        raise ValueError("Unexpected product page host")
    return candidate


class Source:
    def __init__(self, root):
        self.root = Path(root)

    def fetch(self, url, kind):
        if urlparse(url).hostname != "www.wiesbaden.nl" or urlparse(url).scheme != "https":
            raise ValueError("Only public manufacturer URLs are fetched")
        stem = self.root / "raw" / kind / key(url)
        body_path, meta_path = stem.with_suffix(".gz"), stem.with_suffix(".json")
        if body_path.exists() and meta_path.exists():
            meta = load_json(meta_path)
            data = gzip.decompress(body_path.read_bytes())
            if hashlib.sha256(data).hexdigest() != meta["sha256"]:
                raise ValueError("Corrupt cached source snapshot")
            return data, meta
        error = None
        for attempt in range(3):
            try:
                req = Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
                with urlopen(req, timeout=45) as response:
                    data = response.read(25_000_001)
                    if len(data) > 25_000_000:
                        raise ValueError("Source response exceeds 25 MB")
                    if response.headers.get("Content-Encoding") == "gzip":
                        data = gzip.decompress(data)
                    meta = {"url": url, "fetched_at": now(), "http_status": response.status,
                            "content_type": response.headers.get("Content-Type"),
                            "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data),
                            "raw_path": str(body_path.relative_to(self.root))}
                body_path.parent.mkdir(parents=True, exist_ok=True)
                body_path.write_bytes(gzip.compress(data, mtime=0))
                write_json(meta_path, meta)
                return data, meta
            except HTTPError as exc:
                error = exc
                if exc.code not in (429, 500, 502, 503, 504):
                    raise
                retry_after = str(exc.headers.get("Retry-After", "0"))
                pause = min(30, int(retry_after)) if retry_after.isdigit() else 0
                time.sleep(max(pause, 2 ** attempt))
            except (URLError, TimeoutError, OSError) as exc:
                error = exc
                time.sleep(2 ** attempt)
        raise RuntimeError(f"Source fetch failed after retries: {error}")

    def graphql(self, query):
        data, meta = self.fetch(BASE + "graphql?" + urlencode({"query": query}), "api")
        result = json.loads(data)
        if result.get("errors"):
            raise ValueError(json.dumps(result["errors"], ensure_ascii=False)[:1500])
        return result["data"], meta


def product_query(page, size):
    return ("{products(search:\"\",pageSize:" + str(size) + ",currentPage:" + str(page)
            + ",sort:{sku:ASC}){total_count page_info{current_page total_pages page_size} items{"
            + PRODUCT_FIELDS + "}}}")


def catalogue(root, workers=3):
    source = Source(root)
    for size in (100, 50, 25):
        try:
            first, first_meta = source.graphql(product_query(1, size))
            break
        except ValueError as exc:
            if "complexity" not in str(exc).lower():
                raise
    else:
        raise ValueError("Manufacturer catalogue query exceeds permitted complexity")
    p = first["products"]
    pages = p["page_info"]["total_pages"]
    items, sources = list(p["items"]), [first_meta]
    print(f"API catalogue: {p['total_count']} products, {pages} pages, page size {size}", flush=True)
    def page(i):
        result, meta = source.graphql(product_query(i, size))
        if result["products"]["total_count"] != p["total_count"]:
            raise ValueError("Catalogue size changed during this snapshot; rerun in a fresh run directory")
        return result["products"]["items"], meta
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(page, i): i for i in range(2, pages + 1)}
        for f in as_completed(futures):
            rows, meta = f.result()
            items.extend(rows)
            sources.append(meta)
            print(f"API page {futures[f]}/{pages}: {len(items)} records collected", flush=True)
    identities = [x["uid"] for x in items]
    if len(identities) != len(set(identities)) or len(items) != p["total_count"]:
        raise ValueError("Incomplete or overlapping catalogue pagination")
    items.sort(key=lambda x: (sku_key(x["sku"]), x["uid"]))
    write_json(Path(root) / "manufacturer-catalogue.json", {
        "schema_version": 1, "collector_version": VERSION, "observed_at": now(),
        "scope": "Public manufacturer products(search:empty), not a supplier stock feed",
        "declared_count": p["total_count"], "pagination_complete": True,
        "sources": sources, "products": items})
    for label, filters in (("attributes", ""), ("filters", ",filters:{is_filterable:true}")):
        result, meta = source.graphql("{attributesList(entityType:CATALOG_PRODUCT" + filters
                                      + "){items{code label frontend_input options{label value}}}}")
        write_json(Path(root) / ("manufacturer-" + label + ".json"), {
            "source": meta, "items": result["attributesList"]["items"]})
    return items


def image_records(raw):
    result, seen = [], set()
    for match in re.finditer(r'\{[^{}]*"imageUrl"\s*:[^{}]*\}', raw):
        try:
            record = json.loads(match.group())
        except (ValueError, TypeError):
            continue
        url = str(record.get("imageUrl", "")).replace("\\/", "/")
        if not url.startswith("https://") or "placeholder" in url or url in seen:
            continue
        seen.add(url)
        result.append({"url": url, "label": record.get("imageLabel"),
                       "kind": record.get("type", "image"), "is_main": bool(record.get("isMainImage"))})
    return result


def price_tax_basis(raw_text, displayed_price):
    # Inspect selected keys in the main product-price configuration, not the
    # presence of generic tax helper functions elsewhere in HTML.
    config = re.search(r"regularPriceKey:\s*(\w+)\s*,\s*finalPriceKey:\s*(\w+)\s*,\s*"
                       r"activeProductsPriceData:\s*false\s*,\s*initialFinalPrice:\s*([\d.]+)", raw_text)
    if not config or displayed_price is None or Decimal(config[3]) != Decimal(displayed_price):
        return "NOT_VERIFIED", None
    pair = (config[1], config[2])
    if pair == ("regularPriceExclTaxKey", "finalPriceExclTaxKey"):
        mode = "EXCL_TAX_SELECTED_BY_MANUFACTURER_COMPONENT"
    elif pair == ("regularPriceInclTaxKey", "finalPriceInclTaxKey"):
        mode = "INCL_TAX_SELECTED_BY_MANUFACTURER_COMPONENT"
    else:
        return "NOT_VERIFIED", None
    return mode, {"regular_price_key": config[1], "final_price_key": config[2], "initial_price": config[3]}


def parse_page(raw, api, provenance):
    raw_text = raw.decode("utf-8", errors="replace") if isinstance(raw, bytes) else raw
    doc = html.fromstring(raw_text)
    images = image_records(raw_text)
    docs = []
    for a in doc.xpath('//a[@href]'):
        url = urljoin(provenance["url"], a.get("href"))
        if ".pdf" in url.lower() and api["sku"].lower() in url.lower():
            docs.append({"url": url, "label": clean(a.text_content())})
    descriptions = doc.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," product-description ")]')
    description_html = html.tostring(descriptions[0], encoding="unicode") if descriptions else ""
    for n in doc.xpath('//script|//style|//noscript'):
        n.drop_tree()
    main = doc.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," product-info-main ")]')
    main = main[0] if main else doc
    main_text = clean(main.text_content())
    specs = []
    for table in main.xpath('.//table'):
        rows = []
        for tr in table.xpath('.//tr'):
            cells = tr.xpath('./th|./td')
            if len(cells) == 2:
                rows.append({"label": clean(cells[0].text_content()), "value": clean(cells[1].text_content())})
        if any(r["label"].casefold() == "sku" for r in rows):
            specs.extend(rows)
    table = {s["label"]: s["value"] for s in specs}
    issues = []
    if sku_key(table.get("SKU")) != sku_key(api["sku"]):
        issues.append("PAGE_SKU_MISSING_OR_MISMATCH")
    if not specs:
        issues.append("NO_SPECIFICATION_TABLE")
    prices = re.findall(r"Adviesprijs\s*:?\s*€\s*([\d.,]+)", main_text)
    price = prices[0].replace(".", "").replace(",", ".") if prices else None
    api_price = str(api["price_range"]["minimum_price"]["regular_price"]["value"])
    tax_status, tax_evidence = price_tax_basis(raw_text, price)
    if price and Decimal(price) != Decimal(api_price):
        issues.append("HTML_API_ADVICE_PRICE_CONFLICT")
    if not images:
        issues.append("NO_REAL_PRODUCT_IMAGE_FOUND")
    page_title = clean(" ".join(doc.xpath('//h1//text()')))
    description_nodes = main.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," product-description ")]')
    description_text = clean(description_nodes[0].text_content()) if description_nodes else ""
    breadcrumbs = []
    for c in api.get("categories", []):
        trail = sorted(c.get("breadcrumbs") or [], key=lambda v: v.get("category_level") or 0)
        breadcrumbs.append([{"uid": v["category_uid"], "name": clean(v["category_name"]),
                             "url_path": v.get("category_url_path")} for v in trail]
                           + [{"uid": c["uid"], "name": clean(c["name"]), "url_path": c.get("url_path")}])
    return {"schema_version": 1, "collector_version": VERSION, "manufacturer_number": api["sku"], "source_uid": api["uid"],
            "name": api["name"], "page_title": page_title, "source_brand": table.get("Merk"),
            "source": provenance, "api": api, "source_breadcrumb_paths": breadcrumbs,
            "specifications_raw": specs,
            "specifications": [s for s in specs if not re.search(r"\bean\b|barcode|gtin", s["label"], re.I)],
            "description_html_source": description_html, "description_text_source": description_text,
            "advice_price_displayed_eur": price, "advice_price_api_eur": api_price,
            "price_tax_status": tax_status, "price_tax_evidence": tax_evidence,
            "images": images, "documents": list({d["url"]: d for d in docs}.values()),
            "issues": issues, "editorial_status": "SOURCE_DATA_ONLY_NOT_REWRITTEN"}


def product_path(root, api):
    return Path(root) / "products" / (key(api["uid"])[:24] + ".json")


def pages(root, workers=6, limit=0):
    source = Source(root)
    items = load_json(Path(root) / "manufacturer-catalogue.json")["products"]
    if limit:
        items = items[:limit]
    pending = [x for x in items if not product_path(root, x).exists()
               or load_json(product_path(root, x)).get("collector_version") != VERSION]
    errors = []
    def collect(api):
        raw, meta = source.fetch(source_url(api), "html")
        result = parse_page(raw, api, meta)
        write_json(product_path(root, api), result)
        (Path(root)/"errors"/(key(api["uid"])[:24]+".json")).unlink(missing_ok=True)
        return result
    print(f"HTML product pages: {len(items)} total, {len(pending)} pending, {workers} workers", flush=True)
    start = time.monotonic()
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(collect, x): x for x in pending}
        for done, f in enumerate(as_completed(futures), 1):
            api = futures[f]
            try:
                f.result()
            except Exception as exc:
                error = {"sku": api["sku"], "source_uid": api["uid"], "url": source_url(api),
                         "error": str(exc), "observed_at": now()}
                errors.append(error)
                write_json(Path(root) / "errors" / (key(api["uid"])[:24] + ".json"), error)
                print(f"ERROR {api['sku']}: {str(exc)[:160]}", flush=True)
            if done % 25 == 0 or done == len(futures):
                write_json(Path(root) / "page-progress.json", {"updated_at": now(),
                    "catalogue_count": len(items), "remaining_at_start": len(pending),
                    "attempted_this_session": done, "errors_this_session": len(errors),
                    "elapsed_seconds": round(time.monotonic() - start)})
                print(f"HTML {done}/{len(futures)}, errors {len(errors)}, elapsed {time.monotonic()-start:.0f}s", flush=True)
    return errors


def write_csv(path, rows, columns):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: json.dumps(v, ensure_ascii=False) if isinstance(v, (list, dict)) else v
                             for k, v in row.items() if k in columns})


def price_proposal(record, current_price, shop_taxes_included):
    mode = record.get("price_tax_status", "NOT_VERIFIED")
    raw = record.get("advice_price_displayed_eur")
    proposal = {"manufacturer_displayed_eur": raw, "manufacturer_tax_basis": mode,
        "price_component_evidence": record.get("price_tax_evidence"),
        "shop_prices_include_tax": shop_taxes_included,
        "tax_multiplier_if_excl": "1.21", "multiplier_basis": "OBSERVED_EXISTING_STORE_CONVENTION",
        "current_price_eur": current_price, "proposed_advice_incl_eur": None,
        "status": "PRICE_BASIS_REVIEW_NOT_APPLIED"}
    if raw is None or Decimal(raw) <= 0:
        proposal["status"] = "ZERO_OR_MISSING_SOURCE_PRICE_REVIEW"
        return proposal
    if not shop_taxes_included:
        return proposal
    if mode == "EXCL_TAX_SELECTED_BY_MANUFACTURER_COMPONENT":
        price = Decimal(raw)*Decimal("1.21")
    elif mode == "INCL_TAX_SELECTED_BY_MANUFACTURER_COMPONENT":
        price = Decimal(raw)
    else:
        return proposal
    price = price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    proposal["proposed_advice_incl_eur"] = str(price)
    proposal["status"] = ("MATCHES_CURRENT_STORE_PRICE" if current_price is not None and Decimal(current_price) == price
                           else "EXISTING_PRICE_DIFFERENCE_REVIEW" if current_price is not None
                           else "NEW_PRODUCT_PRICE_PROPOSAL_REVIEW")
    return proposal


def build(root):
    root = Path(root)
    manifest = load_json(root / "shopify/snapshot-manifest.json")
    if not manifest.get("global_sku_index_complete") or not manifest.get("wiesbaden_pagination_complete"):
        raise ValueError("Incomplete Shopify snapshot cannot prove a product is new")
    catalogue_snapshot = load_json(root / "manufacturer-catalogue.json")
    api = catalogue_snapshot["products"]
    source_records = [load_json(product_path(root, x)) for x in api if product_path(root, x).exists()]
    current = [r for f in sorted((root / "shopify/pages").glob("*.json")) for r in load_json(f)]
    if not current or not (root / "shopify/all-store-skus.json").exists():
        raise ValueError("Complete current product snapshot and all-store SKU index required")
    current_by_sku, all_by_sku, source_by_sku = defaultdict(list), defaultdict(list), defaultdict(list)
    for p in current:
        for v in p["variants"]["nodes"]:
            current_by_sku[sku_key(v.get("sku"))].append((p, v))
    for v in load_json(root / "shopify/all-store-skus.json"):
        all_by_sku[sku_key(v.get("sku"))].append(v)
    for p in api:
        source_by_sku[sku_key(p["sku"])].append(p)
    records_by_uid = {r["source_uid"]: r for r in source_records}
    notes_path = root/"review-notes.json"
    review_notes = load_json(notes_path) if notes_path.exists() else {}
    price_basis_path = root/"shopify/price-basis.json"
    price_basis = load_json(price_basis_path) if price_basis_path.exists() else {}
    taxes_included = price_basis.get("shop", {}).get("taxesIncluded") is True
    rows, price_rows, price_proposals = [], [], []
    for p in api:
        s = sku_key(p["sku"])
        existing, global_matches = current_by_sku[s], all_by_sku[s]
        record = records_by_uid.get(p["uid"])
        if len(source_by_sku[s]) != 1 or len(global_matches) > 1:
            state = "DUPLICATE_SKU_REVIEW"
        elif len(existing) == 1:
            state = "EXISTING_WIESBADEN"
        elif global_matches:
            state = "EXISTS_OTHER_VENDOR_REVIEW"
        else:
            state = "NEW_CANDIDATE"
        issues = list(record["issues"]) if record else ["PRODUCT_PAGE_NOT_COLLECTED"]
        issues.extend(review_notes.get(p["sku"], {}).get("issues", []))
        if record and record.get("source_brand") and record["source_brand"].casefold() != "wiesbaden":
            issues.append("SOURCE_BRAND_REVIEW")
        if not p["categories"]:
            issues.append("SOURCE_CATEGORY_MISSING")
        if Decimal(str(p["price_range"]["minimum_price"]["regular_price"]["value"])) <= 0:
            issues.append("ZERO_OR_NEGATIVE_SOURCE_PRICE_REVIEW")
        if "bestaande uit" in p["name"].casefold():
            issues.append("SET_COMPONENTS_REQUIRE_REVIEW")
        if record:
            non_identity = [s for s in record["specifications"]
                            if slug(s["label"]) not in ("sku", "merk", "serie") and s["value"]]
            if len(non_identity) < 3:
                issues.append("SPARSE_SPECIFICATIONS_REVIEW")
            if not record.get("description_text_source"):
                issues.append("SOURCE_DESCRIPTION_MISSING")
            if not any(i["kind"] == "image" for i in record["images"]):
                issues.append("NO_PRODUCT_PHOTO_FOUND")
        row = {"sku": p["sku"], "name": p["name"], "comparison_status": state,
               "source_brand": record.get("source_brand") if record else None,
               "source_url": source_url(p), "source_categories": [c["url_path"] for c in p["categories"]],
               "product_id": existing[0][0]["id"] if len(existing) == 1 else None,
               "variant_id": existing[0][1]["id"] if len(existing) == 1 else None,
               "current_title": existing[0][0]["title"] if len(existing) == 1 else None,
               "current_vendor": existing[0][0]["vendor"] if len(existing) == 1 else None,
               "current_price_eur": existing[0][1]["price"] if len(existing) == 1 else None,
               "current_status": existing[0][0]["status"] if len(existing) == 1 else None,
               "current_online_store_url": existing[0][0]["onlineStoreUrl"] if len(existing) == 1 else None,
               "current_product_type": existing[0][0]["productType"] if len(existing) == 1 else None,
               "current_collections": [c["handle"] for c in existing[0][0]["collections"]["nodes"]] if len(existing) == 1 else [],
               "specification_count": len(record["specifications"]) if record else 0,
               "image_count": sum(x["kind"] == "image" for x in record["images"]) if record else 0,
               "drawing_count": sum(x["kind"] == "line_drawings" for x in record["images"]) if record else 0,
               "document_count": len(record["documents"]) if record else 0,
               "source_advice_eur": record.get("advice_price_displayed_eur") if record else None,
               "source_price_tax_basis": record.get("price_tax_status") if record else None,
               "review_notes": review_notes.get(p["sku"], {}).get("notes", []),
               "issues": issues, "shopify_mutation_status": "NOT_APPLIED",
               "import_status": "NEEDS_TARGET_MAPPING_AND_CONTENT_REVIEW"}
        rows.append(row)
        if record:
            price_proposals.append({"sku": p["sku"], "name": p["name"],
                "comparison_status": state, **price_proposal(record, row["current_price_eur"], taxes_included)})
        if len(existing) == 1 and record and record.get("advice_price_displayed_eur"):
            v = existing[0][1]
            try:
                old, source_price = Decimal(v["price"]), Decimal(record["advice_price_displayed_eur"])
                if old != source_price:
                    price_rows.append({"sku": p["sku"], "name": p["name"], "current_price_eur": str(old),
                        "manufacturer_advice_eur": str(source_price), "difference_eur": str(old-source_price),
                        "ratio": str(round(old/source_price, 6)) if source_price else None,
                        "near_121_percent": bool(source_price and abs(old-source_price*Decimal("1.21")) <= Decimal("0.02")),
                        "status": "RAW_SOURCE_VS_STORE_COMPARISON_SEE_TAX_NORMALIZED_PRICE_PROPOSAL"})
            except InvalidOperation:
                issues.append("INVALID_PRICE")
    missing = [{"sku": v.get("sku"), "product_id": p["id"], "name": p["title"],
                "status": "NOT_FOUND_IN_MANUFACTURER_SNAPSHOT_KEEP_EXISTING"}
               for p in current for v in p["variants"]["nodes"] if sku_key(v.get("sku")) not in source_by_sku]
    categories = {c["uid"]: c for p in api for c in p["categories"]}
    attribute_counts = Counter(s["label"] for r in source_records for s in r["specifications"])
    summary = {"schema_version": 1, "collector_version": VERSION, "built_at": now(),
        "stage": "SOURCE_COLLECTION_COMPLETE" if len(source_records) == len(api) else "SOURCE_COLLECTION_IN_PROGRESS",
        "manufacturer_products": len(api), "source_pagination_complete": catalogue_snapshot["pagination_complete"],
        "product_pages_collected": len(source_records), "product_pages_missing": len(api)-len(source_records),
        "shopify_wiesbaden_products": len(current), "global_sku_index_variants": len(load_json(root/"shopify/all-store-skus.json")),
        "comparison_counts": dict(Counter(x["comparison_status"] for x in rows)),
        "new_candidate_brands": dict(Counter(x["source_brand"] or "NOT_YET_COLLECTED" for x in rows if x["comparison_status"] == "NEW_CANDIDATE")),
        "existing_not_found_at_manufacturer": len(missing), "manufacturer_categories": len(categories),
        "specification_labels": len(attribute_counts), "total_specification_values": sum(attribute_counts.values()),
        "source_brands": dict(Counter(r.get("source_brand") or "UNKNOWN" for r in source_records)),
        "products_with_photos": sum(any(i["kind"] == "image" for i in r["images"]) for r in source_records),
        "products_with_drawings": sum(any(i["kind"] == "line_drawings" for i in r["images"]) for r in source_records),
        "products_with_documents": sum(bool(r["documents"]) for r in source_records),
        "price_differences": len(price_rows), "near_121_percent_price_differences": sum(x["near_121_percent"] for x in price_rows),
        "issues": dict(Counter(issue for r in rows for issue in r["issues"])),
        "source_price_tax_modes": dict(Counter(r.get("price_tax_status", "NOT_VERIFIED") for r in source_records)),
        "tax_normalized_price_status": dict(Counter(r["status"] for r in price_proposals)),
        "store_mutations": 0, "import_ready": False,
        "remaining": ["Review source/target category mapping and parts vs complete sets",
                      "Verify real Shopify field definitions and filter/index mapping",
                      "Verify VAT and sales-price policy against observed price differences",
                      "Write/review own product content and image alt text",
                      "Validate new-product media, exact brand and publication readiness"]}
    out = root/"output"
    write_json(out/"summary.json", summary)
    write_json(out/"comparison.json", rows)
    write_json(out/"manufacturer-categories.json", list(categories.values()))
    write_json(out/"specification-field-frequency.json", dict(attribute_counts.most_common()))
    # Compact import-source table without the API's raw HTML or barcode row.
    # Original descriptions and unmodified snapshots remain available separately.
    with (out/"product-master.jsonl").open("w", encoding="utf-8") as stream:
        for record in source_records:
            row = next(r for r in rows if r["sku"] == record["manufacturer_number"])
            master = {**row, "source_brand": record["source_brand"],
                "source_uid": record["source_uid"], "source_evidence": record["source"],
                "source_breadcrumb_paths": record["source_breadcrumb_paths"],
                "specifications": record["specifications"], "images": record["images"],
                "documents": record["documents"],
                "price_tax_status": record["price_tax_status"],
                "description_status": record["editorial_status"]}
            stream.write(json.dumps(master, ensure_ascii=False)+"\n")
    assets = []
    for record in source_records:
        for item in record["images"]:
            assets.append({"sku": record["manufacturer_number"], "kind": item["kind"],
                           "url": item["url"], "label": item["label"], "status": "LINK_COLLECTED_BINARY_NOT_DOWNLOADED"})
        for item in record["documents"]:
            assets.append({"sku": record["manufacturer_number"], "kind": "document",
                           "url": item["url"], "label": item["label"], "status": "LINK_COLLECTED_BINARY_NOT_DOWNLOADED"})
    write_csv(out/"asset-links.csv", assets, ["sku", "kind", "url", "label", "status"])
    cols = list(rows[0]) if rows else []
    write_csv(out/"all-products.csv", rows, cols)
    write_csv(out/"new-products.csv", [r for r in rows if r["comparison_status"] == "NEW_CANDIDATE"], cols)
    write_csv(out/"new-wiesbaden-products.csv", [r for r in rows if r["comparison_status"] == "NEW_CANDIDATE" and r["source_brand"] == "Wiesbaden"], cols)
    write_csv(out/"other-brands-review.csv", [r for r in rows if r["source_brand"] and r["source_brand"] != "Wiesbaden"], cols)
    write_csv(out/"existing-products.csv", [r for r in rows if r["comparison_status"] == "EXISTING_WIESBADEN"], cols)
    write_csv(out/"source-quality-review.csv", [r for r in rows if r["issues"]], cols)
    write_csv(out/"existing-not-found.csv", missing, ["sku", "product_id", "name", "status"])
    write_csv(out/"price-differences.csv", price_rows, ["sku","name","current_price_eur","manufacturer_advice_eur","difference_eur","ratio","near_121_percent","status"])
    write_json(out/"price-differences.json", price_rows)
    write_json(out/"price-import-proposal.json", price_proposals)
    write_csv(out/"price-import-proposal.csv", price_proposals, list(price_proposals[0]) if price_proposals else [])
    print(json.dumps(summary, ensure_ascii=False, indent=2), flush=True)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["catalogue", "pages", "build", "run"])
    parser.add_argument("--run-dir", required=True, type=Path)
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--limit", type=int, default=0, help="Only for a page extraction pilot")
    args = parser.parse_args()
    if not 1 <= args.workers <= 8:
        parser.error("Use between 1 and 8 workers")
    if args.command in ("catalogue", "run"):
        catalogue(args.run_dir, min(3, args.workers))
    if args.command in ("pages", "run"):
        pages(args.run_dir, args.workers, args.limit)
    if args.command in ("build", "run"):
        build(args.run_dir)


if __name__ == "__main__":
    main()
