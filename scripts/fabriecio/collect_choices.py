#!/usr/bin/env python3
"""Collect Fabriecio's explicit linked-product selectors without account access."""

from __future__ import annotations

import argparse
import asyncio
import datetime as dt
import hashlib
import gzip
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

from lxml import etree, html
import aiohttp


ROOT = Path.cwd() / "fabriecio-work"
SITEMAP = "https://fabriecio.nl/product-sitemap.xml"
HEADERS = {"User-Agent": "Badkamercity-Fabriecio-Catalogue/1.0", "Accept": "text/html,application/xml;q=0.9,*/*;q=0.8", "Accept-Encoding": "gzip"}


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def atomic_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
    temp.replace(path)


def text(node):
    return re.sub(r"\s+", " ", " ".join(node.itertext())).strip()


def nodes_with_class(node, class_name):
    return node.xpath('.//*[contains(concat(" ",normalize-space(@class)," "), $class_name)]', class_name=" " + class_name + " ")


def component_context(node):
    return any(any(token.startswith("bundled_") for token in ancestor.get("class", "").split()) for ancestor in [node, *node.iterancestors()])


def norm_url(value, base="https://fabriecio.nl/"):
    url = urllib.parse.urljoin(base, value)
    parts = urllib.parse.urlsplit(url)
    host = parts.hostname or ""
    if host in {"fabriecio.nl", "www.fabriecio.nl", "b2b.fabriecio.nl"}:
        return urllib.parse.urlunsplit(("https", "fabriecio.nl", parts.path.rstrip("/") + "/", "", ""))
    return url


def fetch(url, attempts=3):
    errors = []
    for attempt in range(attempts):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=20) as response:
                body = response.read()
                if response.headers.get("Content-Encoding", "").lower() == "gzip":
                    body = gzip.decompress(body)
                return body, {"status": response.status, "url": response.url, "last_modified": response.headers.get("Last-Modified")}
        except Exception as error:
            errors.append(str(error))
            if isinstance(error, urllib.error.HTTPError) and error.code in {401, 403, 404}:
                break
            if attempt + 1 < attempts:
                time.sleep(0.5 * (attempt + 1))
    raise RuntimeError(" | ".join(errors))


def parse_page(raw, requested_url, response_meta=None):
    doc = html.fromstring(raw)
    canonical = doc.xpath('//link[@rel="canonical"]/@href')
    source_url = norm_url(canonical[0] if canonical else requested_url)
    summary = nodes_with_class(doc, "summary")
    summary = summary[0] if summary else doc
    sku_nodes = nodes_with_class(summary, "sku")
    if not sku_nodes:
        sku_nodes = nodes_with_class(doc, "sku")
    sku = text(sku_nodes[0]) if sku_nodes else ""
    title_nodes = nodes_with_class(summary, "product_title")
    if not title_nodes:
        title_nodes = doc.xpath("//h1")
    title = text(title_nodes[0]) if title_nodes else ""
    stock_nodes = [n for n in nodes_with_class(summary, "stock") if not component_context(n)]
    stock = [{"text": text(n), "class": n.get("class", "")} for n in stock_nodes if text(n)]
    component_stock = [{"text": text(n), "class": n.get("class", "")} for n in nodes_with_class(summary, "stock") if component_context(n) and text(n)]
    specs = {}
    for row in doc.xpath('//table[contains(@class,"shop_attributes")]//tr'):
        cells = row.xpath("./th|./td")
        if len(cells) >= 2:
            specs[text(cells[0])] = text(cells[1])
    if not sku and specs.get("Typenummer"):
        sku = specs["Typenummer"]
    menus = []
    tables = doc.xpath('//table[contains(concat(" ",normalize-space(@class)," ")," iconic-wlv-variations ")]')
    for table in tables:
        for row in table.xpath('.//tr[contains(@class,"iconic-wlv-variations__row")]'):
            labels = row.xpath('.//strong[contains(@class,"iconic-wlv-variations__label")]')
            selected = row.xpath('.//*[@data-iconic-wlv-selected-term-label]/@data-iconic-wlv-selected-term-label')
            row_class = row.get("class", "")
            key_match = re.search(r"iconic-wlv-variations__row--(?:pa_)?([^\s]+)", row_class)
            label = text(labels[0]) if labels else ""
            key = key_match.group(1) if key_match else label.lower().replace(" ", "_")
            values = []
            for term in row.xpath('.//*[@data-iconic-wlv-term-label]'):
                classes = term.get("class", "").split()
                links = term.xpath('.//a[@href]/@href')
                images = term.xpath('.//img')
                current = "iconic-wlv-terms__term--current" in classes
                target_url = norm_url(links[0], source_url) if links else (source_url if current else None)
                swatch = None
                if images:
                    image_node = images[0]
                    swatch = image_node.get("data-src") or image_node.get("src")
                    if swatch:
                        swatch = urllib.parse.urljoin(source_url, swatch)
                values.append({"value": term.get("data-iconic-wlv-term-label", "").strip(), "target_url": target_url, "current": current, "swatch_url": swatch, "source_out_of_stock": "iconic-wlv-terms__term--outofstock" in classes, "classes": classes})
            selected_value = selected[0].strip() if selected else next((v["value"] for v in values if v["current"]), "")
            menus.append({"key": key, "label": label, "selected": selected_value, "values": values})
    messages = []
    for value_node in summary.xpath('.//text()'):
        if component_context(value_node.getparent()):
            continue
        value = re.sub(r"\s+", " ", str(value_node)).strip()
        if value and len(value) < 300 and any(k in value.lower() for k in ["verwacht", "werkdag", "levertijd", "nooit meer", "niet meer leverbaar"]):
            if value not in messages:
                messages.append(value)
    return {"sku": sku, "title": title, "source_url": source_url, "requested_url": requested_url, "observed_at": now(), "response": response_meta or {}, "menus": menus, "selected_options": {m["key"]: m["selected"] for m in menus}, "specifications": specs, "stock_messages": stock, "delivery_messages": messages, "component_stock_messages": component_stock}


async def collect_one_async(item, session, semaphore, force=False, reparse=False):
    url = item["url"]
    slug = urllib.parse.urlsplit(url).path.rstrip("/").split("/")[-1]
    stem = slug + "-" + hashlib.sha256(url.encode()).hexdigest()[:10]
    parsed_path = ROOT / "parsed" / (stem + ".json")
    html_path = ROOT / "html" / (stem + ".html")
    previous = json.loads(parsed_path.read_text()) if parsed_path.exists() else {}
    if not force and not reparse and previous.get("sku") and "error" not in previous:
        return previous
    try:
        if html_path.exists() and not force:
            raw = html_path.read_bytes()
            meta = {"cached": True}
        else:
            async with semaphore:
                errors = []
                for attempt in range(3):
                    try:
                        async with session.get(url) as response:
                            response.raise_for_status()
                            raw = await response.read()
                            meta = {"status": response.status, "url": str(response.url), "last_modified": response.headers.get("Last-Modified")}
                        break
                    except Exception as error:
                        errors.append(str(error))
                        if isinstance(error, aiohttp.ClientResponseError) and error.status in {401, 403, 404}:
                            raise RuntimeError(" | ".join(errors)) from error
                        if attempt == 2:
                            raise RuntimeError(" | ".join(errors)) from error
                        await asyncio.sleep(0.5 * (attempt + 1))
            html_path.parent.mkdir(parents=True, exist_ok=True)
            html_path.write_bytes(raw)
        record = parse_page(raw, url, meta)
        if not force and meta.get("cached") and previous.get("observed_at"):
            record["observed_at"] = previous["observed_at"]
        evidence = previous.get("sku_evidence", {})
        if not record["sku"] and not force and evidence.get("permalink") and norm_url(evidence["permalink"]) == record["source_url"]:
            record["sku"] = evidence["sku"]
            record["sku_evidence"] = evidence
        if not record["sku"]:
            api_url = "https://b2b.fabriecio.nl/wp-json/wc/store/v1/products?" + urllib.parse.urlencode({"slug": slug})
            async with semaphore:
                async with session.get(api_url) as response:
                    response.raise_for_status()
                    candidates = await response.json(content_type=None)
            exact = [candidate for candidate in candidates if candidate.get("sku") and norm_url(candidate.get("permalink", "")) == record["source_url"]]
            if len(exact) == 1:
                candidate = exact[0]
                record["sku"] = candidate["sku"]
                record["sku_evidence"] = {"source_url": api_url, "permalink": candidate["permalink"], "sku": candidate["sku"], "source_product_id": candidate["id"]}
        if not record["sku"]:
            record["error"] = "No product SKU present in source page"
        atomic_json(parsed_path, record)
        return record
    except Exception as error:
        record = {"source_url": url, "observed_at": now(), "error": str(error)}
        atomic_json(parsed_path, record)
        return record


async def collect_all(items, args, started_at):
    records = []
    workers = max(1, min(6, args.workers))
    connector = aiohttp.TCPConnector(limit=workers, limit_per_host=workers, ttl_dns_cache=300, keepalive_timeout=45)
    timeout = aiohttp.ClientTimeout(total=25, connect=10, sock_read=20)
    semaphore = asyncio.Semaphore(workers)
    async with aiohttp.ClientSession(headers=HEADERS, connector=connector, timeout=timeout, trust_env=True) as session:
        tasks = [asyncio.create_task(collect_one_async(item, session, semaphore, args.force, args.reparse)) for item in items]
        for task in asyncio.as_completed(tasks):
            records.append(await task)
            if len(records) % 25 == 0 or len(records) == len(items):
                progress = {"stage": "collecting", "started_at": started_at, "updated_at": now(), "total": len(items), "completed": len(records), "errors": sum(bool(r.get("error")) for r in records), "with_choices": sum(bool(r.get("menus")) for r in records)}
                atomic_json(ROOT / "progress.json", progress)
                print(json.dumps(progress), flush=True)
    return records


def normalize(records, source_index):
    by_url = {r["source_url"]: r for r in records if r.get("sku")}
    by_sku = defaultdict(list)
    for record in by_url.values():
        by_sku[record["sku"]].append(record["source_url"])
    adjacency = defaultdict(set)
    unresolved = []
    for url, record in by_url.items():
        adjacency[url]
        for menu in record["menus"]:
            for option in menu["values"]:
                target = option["target_url"]
                option["target_sku"] = by_url.get(target, {}).get("sku")
                if target and target in by_url:
                    adjacency[url].add(target)
                    adjacency[target].add(url)
                elif not option["current"]:
                    unresolved.append({"source_sku": record["sku"], "menu": menu["key"], "value": option["value"], "target_url": target})
    seen = set()
    groups = []
    duplicate_combinations = []
    inconsistent_menu_keys = []
    for start in sorted(adjacency):
        if start in seen:
            continue
        todo = [start]
        members = []
        while todo:
            url = todo.pop()
            if url in seen:
                continue
            seen.add(url)
            members.append(url)
            todo.extend(adjacency[url] - seen)
        group_records = sorted((by_url[url] for url in members), key=lambda r: r["sku"])
        if not any(r["menus"] for r in group_records):
            continue
        signature = "|".join(r["sku"] for r in group_records)
        group_id = "fabriecio-" + hashlib.sha256(signature.encode()).hexdigest()[:16]
        key_sets = {tuple(sorted(r["selected_options"])) for r in group_records}
        if len(key_sets) != 1:
            inconsistent_menu_keys.append({"group_id": group_id, "skus": [r["sku"] for r in group_records], "key_sets": [list(k) for k in sorted(key_sets)]})
        combinations = defaultdict(list)
        for record in group_records:
            record["group_id"] = group_id
            combinations[tuple(sorted(record["selected_options"].items()))].append(record["sku"])
        for combination, skus in combinations.items():
            if len(skus) > 1:
                duplicate_combinations.append({"group_id": group_id, "options": dict(combination), "skus": skus})
        groups.append({"id": group_id, "skus": [r["sku"] for r in group_records], "source_urls": [r["source_url"] for r in group_records], "menu_keys": list(key_sets.pop()) if len(key_sets) == 1 else None})
    summary = {"source_product_count": len(source_index["products"]), "parsed_product_count": len(by_url), "error_count": sum(bool(r.get("error")) for r in records), "products_with_choices": sum(bool(r["menus"]) for r in by_url.values()), "products_without_choices": sum(not r["menus"] for r in by_url.values()), "group_count": len(groups), "group_size_counts": dict(sorted(Counter(len(g["skus"]) for g in groups).items())), "menu_key_counts": dict(Counter(m["key"] for r in by_url.values() for m in r["menus"])), "unresolved_option_count": len(unresolved), "duplicate_sku_count": sum(len(v) > 1 for v in by_sku.values()), "duplicate_combination_count": len(duplicate_combinations), "inconsistent_menu_key_group_count": len(inconsistent_menu_keys)}
    return {"schema_version": 1, "created_at": now(), "source": "Explicit linked-product selectors on public Fabriecio product pages", "summary": summary, "groups": groups, "products": sorted(by_url.values(), key=lambda r: r["sku"]), "unresolved_options": unresolved, "duplicate_skus": {k: v for k, v in by_sku.items() if len(v) > 1}, "duplicate_combinations": duplicate_combinations, "inconsistent_menu_keys": inconsistent_menu_keys, "errors": [r for r in records if r.get("error")]}


def main():
    global ROOT
    parser = argparse.ArgumentParser()
    parser.add_argument("--work-dir", type=Path, default=ROOT, help="Private cache and output directory; keep outside public source control")
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--reparse", action="store_true", help="Rebuild normalized records from cached HTML without redownloading pages")
    args = parser.parse_args()
    ROOT = args.work_dir.resolve()
    ROOT.mkdir(parents=True, exist_ok=True)
    index_path = ROOT / "source-index.json"
    if index_path.exists() and not args.force:
        index = json.loads(index_path.read_text())
    else:
        raw, meta = fetch(SITEMAP)
        (ROOT / "product-sitemap.xml").write_bytes(raw)
        doc = etree.fromstring(raw)
        ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        products = []
        for node in doc.xpath("/s:urlset/s:url", namespaces=ns):
            urls = node.xpath("./s:loc/text()", namespaces=ns)
            modified = node.xpath("./s:lastmod/text()", namespaces=ns)
            if urls:
                products.append({"url": norm_url(urls[0]), "last_modified": modified[0] if modified else None})
        index = {"sitemap": SITEMAP, "observed_at": now(), "response": meta, "products": products}
        atomic_json(index_path, index)
    items = index["products"][:args.limit] if args.limit else index["products"]
    started_at = now()
    print(json.dumps({"stage": "started", "total": len(items), "workers": args.workers, "started_at": started_at}), flush=True)
    records = asyncio.run(collect_all(items, args, started_at))
    result = normalize(records, index)
    atomic_json(ROOT / "normalized-catalog.json", result)
    atomic_json(ROOT / "summary.json", result["summary"])
    atomic_json(ROOT / "progress.json", {"stage": "complete", "started_at": started_at, "completed_at": now(), **result["summary"]})
    print(json.dumps(result["summary"]), flush=True)


if __name__ == "__main__":
    main()
