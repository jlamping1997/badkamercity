#!/usr/bin/env python3
"""Build a scoped Hotbath IBS70 preview from current read-only catalog/theme inputs."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
from pathlib import Path


GROUP_ID = "hotbath-cobber-ibs70-inbouw-doucheset"
DATA_ASSET = "bc-hotbath-ibs70-switcher-data.json"
SCOPE_SNIPPET = "bc-hotbath-preview-group"
COLORS = {
    "CR": "Chroom",
    "GN": "Geborsteld nikkel",
    "BB": "Geborsteld messing",
    "AB": "Verouderd messing",
    "WH": "Mat wit",
    "AI": "Verouderd ijzer",
    "PBP": "Gepolijst zwart PVD",
    "MBP": "Geborsteld zwart PVD",
    "BBP": "Geborsteld messing PVD",
    "BCP": "Geborsteld koper PVD",
}
ALL_COLORS = {**COLORS, "BGP": "Geborsteld gunmetal PVD", "TB": "Tuscan bronze"}
COLOR_GROUPS = {
    "BAA03": {"id": "hotbath-more-handdoekhaak-verouderd-messing-baa03ab", "asset": "bc-hotbath-baa03-switcher-data.json", "label": "Hotbath &More BAA03", "augment": True},
    "BAA09": {"id": "hotbath-more-baa09-zeepdispenser-wandmodel", "asset": "bc-hotbath-baa09-switcher-data.json", "label": "Hotbath &More BAA09"},
    "BAA10": {"id": "hotbath-more-baa10-zeepdispenser-vrijstaand", "asset": "bc-hotbath-baa10-switcher-data.json", "label": "Hotbath &More BAA10"},
}
SKU_PATTERN = re.compile(r"^IBS70(BCP|BBP|MBP|PBP|CR|GN|BB|AB|WH|AI)([123457]*)$")
MENU_DEFINITIONS = [
    ("kleur", "Kleur", list(COLORS.values()), "dropdown"),
    ("breedte_diameter_hoofddouche", "Diameter hoofddouche", ["20 cm", "25 cm", "30 cm"], "buttons"),
    ("type_bevestiging_hoofddouche", "Bevestiging hoofddouche", ["Wandarm", "Plafondbuis 15 cm", "Plafondbuis 30 cm"], "buttons"),
    ("type_handdouche", "Handdouche", ["Staafmodel", "Rond model"], "buttons"),
    ("bevestiging_handdouche", "Handdouchehouder", ["Wandhouder", "Glijstang"], "buttons"),
]


def sku_options(sku: str) -> dict[str, str] | None:
    match = SKU_PATTERN.fullmatch(sku)
    if not match:
        return None
    color_code, suffix = match.groups()
    digits = set(suffix)
    if len(digits) != len(suffix) or suffix != "".join(sorted(suffix)):
        raise ValueError(f"Non-canonical IBS70 option suffix: {sku}")
    if {"2", "3"} <= digits or {"4", "5"} <= digits:
        raise ValueError(f"Contradictory IBS70 option suffix: {sku}")
    return {
        "kleur": COLORS[color_code],
        "breedte_diameter_hoofddouche": "25 cm" if "4" in digits else "30 cm" if "5" in digits else "20 cm",
        "type_bevestiging_hoofddouche": "Plafondbuis 15 cm" if "2" in digits else "Plafondbuis 30 cm" if "3" in digits else "Wandarm",
        "type_handdouche": "Rond model" if "1" in digits else "Staafmodel",
        "bevestiging_handdouche": "Glijstang" if "7" in digits else "Wandhouder",
    }


def title_options(title: str) -> dict[str, str]:
    text = re.sub(r"\s+", " ", title.casefold())
    color_matches = [label for label in COLORS.values() if re.search(r"(?<!\w)" + re.escape(label.casefold()) + r"(?!\w)", text)]
    color_matches.sort(key=len, reverse=True)
    if not color_matches:
        raise ValueError(f"No recognized color in title: {title}")
    color = color_matches[0]
    diameter = re.search(r"(\d+)\s*cm\s*hoofddouche", text) or re.search(r"ø\s*(\d+)\s*cm", text)
    ceiling = re.search(r"(\d+)\s*cm\s*plafondbuis", text) or re.search(r"plafondbuis\s*(\d+)\s*cm", text)
    hand = "Rond model" if re.search(r"ronde\s*handdouche", text) else "Staafmodel" if re.search(r"staaf\s*handdouche", text) else None
    mount = f"Plafondbuis {ceiling.group(1)} cm" if ceiling else "Wandarm" if "wandarm" in text else None
    holder = "Glijstang" if "glijstang" in text else "Wandhouder" if "wandhouder" in text else None
    if not all([diameter, hand, mount, holder]):
        raise ValueError(f"Incomplete choices in title: {title}")
    return {
        "kleur": color,
        "breedte_diameter_hoofddouche": f"{diameter.group(1)} cm",
        "type_bevestiging_hoofddouche": mount,
        "type_handdouche": hand,
        "bevestiging_handdouche": holder,
    }


def build_data(catalog: dict) -> tuple[dict, list[dict]]:
    if catalog.get("complete") is not True:
        raise ValueError("Catalog snapshot must explicitly be complete")
    rows = []
    sku_seen, handle_seen, tuple_seen = set(), set(), set()
    for product in catalog["products"]:
        variants_connection = product.get("variants") or {}
        variants = variants_connection.get("nodes") or []
        if len(variants) != 1:
            continue
        sku = (variants[0].get("sku") or "").strip()
        choices = sku_options(sku)
        if choices is None:
            continue
        if variants_connection.get("pageInfo", {}).get("hasNextPage"):
            raise ValueError(f"Unfetched variants for pilot product: {sku}")
        if product.get("status") != "ACTIVE" or not product.get("publishedAt"):
            raise ValueError(f"Pilot article is not active and published: {sku}")
        handle = product.get("handle") or ""
        if not re.fullmatch(r"[a-z0-9-]+", handle) or handle.startswith("test") or product["title"].upper().startswith("TEST"):
            raise ValueError(f"Unsafe pilot handle or test article: {sku}")
        if title_options(product["title"]) != choices:
            raise ValueError(f"SKU/title choice disagreement: {sku}")
        existing_group = product.get("group")
        if existing_group and existing_group.get("value"):
            raise ValueError(f"Pilot fallback must not replace an existing group: {sku}")
        key = tuple(choices[m[0]] for m in MENU_DEFINITIONS)
        if sku in sku_seen or handle in handle_seen or key in tuple_seen:
            raise ValueError(f"Duplicate SKU, handle or full choice tuple: {sku}")
        sku_seen.add(sku)
        handle_seen.add(handle)
        tuple_seen.add(key)
        rows.append({"sku": sku, "id": product["id"], "handle": handle, "url": f"/products/{handle}", "title": product["title"], "options": choices})
    rows.sort(key=lambda row: tuple(values.index(row["options"][key]) for key, _, values, _ in MENU_DEFINITIONS))
    menus = [{"key": key, "label": label, "order": i + 1, "display_type": display, "hide_if_single_value": True, "values": [v for v in values if any(row["options"][key] == v for row in rows)]} for i, (key, label, values, display) in enumerate(MENU_DEFINITIONS)]
    if len(rows) < 2:
        raise ValueError("Pilot needs at least two distinct valid articles")
    data = {
        "version": "hotbath-ibs70-preview-20261024",
        "generated_at": catalog["captured_at"],
        "groups": [{"id": GROUP_ID, "label": "Hotbath Cobber IBS70", "menus": menus, "products": [{"handle": row["handle"], "url": row["url"], "title": row["title"], "sort_order": i, "options": row["options"]} for i, row in enumerate(rows)]}],
    }
    return data, rows


def build_color_data(catalog: dict, model: str, existing_group: dict | None = None) -> tuple[dict, list[dict]]:
    spec = COLOR_GROUPS[model]
    pattern = re.compile(r"^" + re.escape(model) + "(" + "|".join(sorted(ALL_COLORS, key=len, reverse=True)) + r")$")
    rows, signatures, seen = [], set(), set()
    for product in catalog["products"]:
        connection = product.get("variants") or {}
        variants = connection.get("nodes") or []
        if len(variants) != 1:
            continue
        sku = (variants[0].get("sku") or "").strip()
        match = pattern.fullmatch(sku)
        if not match:
            continue
        if connection.get("pageInfo", {}).get("hasNextPage") or product.get("status") != "ACTIVE" or not product.get("publishedAt"):
            raise ValueError(f"Incomplete or unpublished color sibling: {sku}")
        handle = product.get("handle") or ""
        if not re.fullmatch(r"[a-z0-9-]+", handle) or handle.startswith("test") or product["title"].upper().startswith("TEST"):
            raise ValueError(f"Unsafe color pilot handle or test article: {sku}")
        current_group = (product.get("group") or {}).get("value")
        if current_group and (not existing_group or current_group != spec["id"]):
            raise ValueError(f"Color pilot would replace an existing group: {sku}")
        color = ALL_COLORS[match.group(1)]
        title = re.sub(r"\s+", " ", product["title"].casefold())
        if not re.search(r"(?<!\w)" + re.escape(color.casefold()) + r"(?!\w)", title):
            raise ValueError(f"SKU/title color disagreement: {sku}")
        signature = re.sub(re.escape(sku.casefold()), " ", title)
        signature = re.sub(r"(?<!\w)" + re.escape(color.casefold()) + r"(?!\w)", " ", signature)
        signature = re.sub(r"[\s–—\-,]+", " ", signature).strip()
        signatures.add(signature)
        if sku in seen or any(row["handle"] == handle or row["options"]["kleur"] == color for row in rows):
            raise ValueError(f"Duplicate color sibling: {sku}")
        seen.add(sku)
        rows.append({"sku": sku, "id": product["id"], "handle": handle, "url": f"/products/{handle}", "title": product["title"], "options": {"kleur": color}, "current_group": current_group})
    if len(rows) != 12 or len(signatures) != 1:
        raise ValueError(f"Expected 12 identical-base-title color siblings for {model}; got {len(rows)} records and {len(signatures)} base titles")
    palette = list(ALL_COLORS.values())
    rows.sort(key=lambda row: palette.index(row["options"]["kleur"]))
    data = {"version": "hotbath-color-preview-20261024", "generated_at": catalog["captured_at"], "groups": [{"id": spec["id"], "label": spec["label"], "menus": [{"key": "kleur", "label": "Kleur", "order": 1, "display_type": "dropdown", "hide_if_single_value": True, "values": [row["options"]["kleur"] for row in rows]}], "products": [{"handle": row["handle"], "url": row["url"], "title": row["title"], "sort_order": i, "options": row["options"]} for i, row in enumerate(rows)]}]}
    if existing_group:
        if existing_group["id"] != spec["id"] or len(existing_group["products"]) != 8 or len(existing_group["menus"]) != 1 or existing_group["menus"][0]["key"] != "kleur":
            raise ValueError("Expected the unchanged eight-record BAA03 color group")
        augmented = copy.deepcopy(existing_group)
        existing_handles = {product["handle"] for product in augmented["products"]}
        catalog_handles = {row["handle"] for row in rows}
        if not existing_handles <= catalog_handles:
            raise ValueError("Existing color group has products absent from the current verified family")
        for product in augmented["products"]:
            matching = next(row for row in rows if row["handle"] == product["handle"])
            if product["options"] != matching["options"] or matching["current_group"] != spec["id"]:
                raise ValueError("Existing BAA03 choices or product-group assignment disagree with catalog")
        max_order = max(product.get("sort_order", 0) for product in augmented["products"])
        for row in rows:
            if row["handle"] not in existing_handles:
                if row["current_group"]:
                    raise ValueError("New BAA03 sibling already belongs to another group")
                max_order += 10
                augmented["products"].append({"handle": row["handle"], "url": row["url"], "title": row["title"], "sort_order": max_order, "options": row["options"]})
        augmented["menus"][0]["values"] = [row["options"]["kleur"] for row in rows]
        data["groups"] = [augmented]
    return data, rows


def scope_snippet(group_rows: dict[str, list[dict]] | list[dict]) -> str:
    if isinstance(group_rows, list):
        group_rows = {GROUP_ID: group_rows}
    assignments = []
    branches = []
    for index, (group_id, rows) in enumerate(group_rows.items()):
        handles = "|" + "|".join(sorted(row["handle"] for row in rows)) + "|"
        assignments.append(f"  assign bc_hotbath_preview_handles_{index} = '{handles}'\n")
        branches.append(f"    {'if' if index == 0 else 'elsif'} bc_hotbath_preview_handles_{index} contains bc_hotbath_preview_handle\n      echo '{group_id}'\n")
    return (
        "{% doc %}\n"
        "Returns a scoped Hotbath preview group for verified published product handles.\n"
        "@param {product} product - The current product.\n"
        "@example\n"
        "{% render 'bc-hotbath-preview-group', product: product %}\n"
        "{% enddoc %}\n"
        "{%- liquid\n"
        + "".join(assignments)
        + "  assign bc_hotbath_preview_handle = product.handle | prepend: '|' | append: '|'\n"
        "  if product.vendor == 'Hotbath'\n"
        + "".join(branches)
        + "    endif\n"
        "  endif\n"
        "-%}\n"
    )


def replace_once(text: str, before: str, after: str, label: str) -> str:
    if text.count(before) != 1:
        raise ValueError(f"Expected exactly one unchanged source anchor for {label}; got {text.count(before)}")
    return text.replace(before, after, 1)


def patch_main(source: str) -> str:
    nl = "\r\n" if "\r\n" in source else "\n"
    anchor = "    assign current_switch_group = current_switch_group | strip" + nl
    addition = nl.join([
        "    assign bc_switcher_data_url = ''",
        "    if current_switch_group == blank",
        "      capture current_switch_group",
        f"        render '{SCOPE_SNIPPET}', product: product",
        "      endcapture",
        "      assign current_switch_group = current_switch_group | strip",
        "    endif",
        "    case current_switch_group",
        f"      when '{GROUP_ID}'",
        f"        assign bc_switcher_data_url = '{DATA_ASSET}' | asset_url",
        *[line for spec in COLOR_GROUPS.values() for line in [f"      when '{spec['id']}'", f"        assign bc_switcher_data_url = '{spec['asset']}' | asset_url"]],
        "    endcase",
        "",
    ])
    result = replace_once(source, anchor, anchor + addition, "group capture")
    render = "{% render 'bc-product-switcher', product: product, section: section %}"
    return replace_once(result, render, "{% render 'bc-product-switcher', product: product, section: section, switch_group: current_switch_group, data_url: bc_switcher_data_url %}", "existing V2 render")


def patch_snippet(source: str) -> str:
    nl = "\r\n" if "\r\n" in source else "\n"
    anchor = "  assign bc_switch_group = product.metafields.custom.switch_group.value | default: product.metafields.custom.switch_group | strip" + nl
    replacement = nl.join([
        "  assign bc_switch_group = switch_group | default: product.metafields.custom.switch_group.value | default: product.metafields.custom.switch_group | strip",
        "  assign bc_switcher_default_data_url = 'product-switcher-data.json' | asset_url",
        "  assign bc_switcher_data_url = data_url | default: bc_switcher_default_data_url",
        "",
    ])
    result = replace_once(source, anchor, replacement, "snippet group")
    result = replace_once(result, "data-switcher-data-url=\"{{ 'product-switcher-data.json' | asset_url }}\"", "data-switcher-data-url=\"{{ bc_switcher_data_url | escape }}\"", "snippet data URL")
    result = replace_once(result, "    data-section-id=\"{{ section.id | escape }}\"" + nl, "    data-section-id=\"{{ section.id | escape }}\"" + nl + "    {% if data_url != blank %}data-bc-preserve-position=\"true\"{% endif %}" + nl, "scoped position opt-in")
    doc = nl.join([
        "{% doc %}",
        "Renders the existing V2 product switcher with an optional scoped preview source.",
        "@param {product} product - The current product.",
        "@param {section} section - The containing section.",
        "@param {string} [switch_group] - Explicit group; defaults to the existing product field.",
        "@param {string} [data_url] - Explicit data URL; defaults to the existing shared asset.",
        "@example",
        "{% render 'bc-product-switcher', product: product, section: section %}",
        "{% enddoc %}",
        "",
    ])
    return doc + result


def patch_script(source: str) -> str:
    nl = "\r\n" if "\r\n" in source else "\n"
    helper = (Path(__file__).parent / "scroll_position.js").read_text().rstrip()
    indented = nl.join("  " + line if line else "" for line in helper.splitlines())
    result = replace_once(source, "  let dataPromise;" + nl, "  let dataPromise;" + nl + nl + indented + nl + nl + "  const switcherPosition = createSwitcherPositionKeeper(window, document);" + nl, "position keeper")
    result = replace_once(result, "    constructor(root, data) {", "    constructor(root, data, positionRestore) {", "constructor argument")
    result = replace_once(result, "      this.isNavigating = false;" + nl, "      this.isNavigating = false;" + nl + "      this.positionRestore = positionRestore;" + nl, "restore controller")
    result = replace_once(result, "      this.root.dataset.bcProductSwitcherV2Initialized = 'true';" + nl, "      this.root.dataset.bcProductSwitcherV2Initialized = 'true';" + nl + "      this.positionRestore?.activate();" + nl, "restore after rendering")
    result = replace_once(result, "    hide() {" + nl, "    hide() {" + nl + "      this.positionRestore?.cancel();" + nl, "cancel hidden restore")
    result = replace_once(result, "      this.state = nextState;" + nl, "      const positionToken = switcherPosition.remember(this.root, destination.href);" + nl + "      this.state = nextState;" + nl, "synchronous first-switch capture")
    result = replace_once(result, "      } catch (_) {" + nl + "        this.setNavigating(false);", "      } catch (_) {" + nl + "        switcherPosition.discard(positionToken);" + nl + "        this.setNavigating(false);", "failed navigation cleanup")
    result = replace_once(result, "    if (!switcherRoots.length) return;" + nl, "    if (!switcherRoots.length) return;" + nl + "    const positionRestores = new Map(switcherRoots.map((switcherRoot) => [switcherRoot, switcherPosition.prepare(switcherRoot)]));" + nl, "restore before async data")
    result = replace_once(result, "switcherRoots.forEach((switcherRoot) => new BCProductSwitcherV2(switcherRoot, data));", "switcherRoots.forEach((switcherRoot) => new BCProductSwitcherV2(switcherRoot, data, positionRestores.get(switcherRoot)));", "restore constructor")
    result = replace_once(result, "        switcherRoots.forEach((switcherRoot) => {" + nl + "          switcherRoot.innerHTML = '';", "        switcherRoots.forEach((switcherRoot) => {" + nl + "          positionRestores.get(switcherRoot)?.cancel();" + nl + "          switcherRoot.innerHTML = '';", "data error cleanup")
    return result


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content.encode("utf-8"))


def run(source_dir: Path, catalog_path: Path, output_dir: Path, shared_data_path: Path | None = None) -> dict:
    catalog = json.loads(catalog_path.read_text())
    data, rows = build_data(catalog)
    if len(rows) != 359:
        raise ValueError(f"Verified pilot expects 359 real IBS70 articles, found {len(rows)}; review a changed catalog before rebuilding")
    shared_data_path = shared_data_path or source_dir.parent / "product-switcher-data.json"
    shared_data_bytes = shared_data_path.read_bytes()
    shared_data = json.loads(shared_data_bytes)
    datasets = {GROUP_ID: {"data": data, "rows": rows, "asset": DATA_ASSET, "book": {"edition": 18, "printed_page": 200, "pdf_page": 202}}}
    for model, spec in COLOR_GROUPS.items():
        existing = next((group for group in shared_data["groups"] if group["id"] == spec["id"]), None) if spec.get("augment") else None
        if spec.get("augment") and existing is None:
            raise ValueError("Expected existing BAA03 baseline group")
        color_data, color_rows = build_color_data(catalog, model, existing)
        datasets[spec["id"]] = {"data": color_data, "rows": color_rows, "asset": spec["asset"], "book": {"edition": 18, "printed_page": 414 if model == "BAA03" else 416, "pdf_page": 416 if model == "BAA03" else 418}}
    source_files = {name: (source_dir / name).read_bytes() for name in ["sections/main-product.liquid", "snippets/bc-product-switcher.liquid", "assets/bc-product-switcher.js"]}
    outputs = {
        "sections/main-product.liquid": patch_main(source_files["sections/main-product.liquid"].decode("utf-8")),
        "snippets/bc-product-switcher.liquid": patch_snippet(source_files["snippets/bc-product-switcher.liquid"].decode("utf-8")),
        "assets/bc-product-switcher.js": patch_script(source_files["assets/bc-product-switcher.js"].decode("utf-8")),
        f"snippets/{SCOPE_SNIPPET}.liquid": scope_snippet({group_id: [row for row in value["rows"] if not row.get("current_group")] for group_id, value in datasets.items()}),
        **{f"assets/{value['asset']}": json.dumps(value["data"], ensure_ascii=False, separators=(",", ":")) + "\n" for value in datasets.values()},
    }
    for name, content in outputs.items():
        write_text(output_dir / name, content)
    old_helper = output_dir / "snippets/bc-hotbath-ibs70-preview-group.liquid"
    if old_helper.exists():
        old_helper.unlink()
    manifest = {
        "scope": "UNPUBLISHED_PREVIEW_ONLY",
        "group_id": GROUP_ID,
        "group_count": len(datasets),
        "product_count": sum(len(value["rows"]) for value in datasets.values()),
        "newly_linked_product_count": sum(not row.get("current_group") for value in datasets.values() for row in value["rows"]),
        "menu_count": sum(len(value["data"]["groups"][0]["menus"]) for value in datasets.values()),
        "groups": [{"group_id": group_id, "asset": value["asset"], "product_count": len(value["rows"]), "menu_count": len(value["data"]["groups"][0]["menus"]), "book_source": value["book"]} for group_id, value in datasets.items()],
        "source_catalog_captured_at": catalog["captured_at"],
        "catalog_sha256": sha256(catalog_path.read_bytes()),
        "book_source": {"edition": 18, "printed_page": 200, "pdf_page": 202},
        "changed_files": [{"filename": name, "source_sha256": sha256(source_files[name]) if name in source_files else None, "output_sha256": sha256((output_dir / name).read_bytes()), "size_bytes": (output_dir / name).stat().st_size} for name in outputs],
        "unchanged_files": [],
        "shared_switcher_dataset_changed": False,
        "shared_switcher_dataset_sha256": sha256(shared_data_bytes),
        "shopify_product_mutations": False,
        "scroll_preservation": {"scope": "FOUR_PILOT_GROUPS_ONLY", "opt_in": "data-bc-preserve-position=true", "ttl_ms": 30000, "max_restore_ms": 15000, "settle_after_load_ms": 2000, "consumption": "ONCE_BEFORE_ASYNC_FETCH"},
        "known_missing_combination": "IBS70AI4",
        "products": [{**row, "group_id": group_id} for group_id, value in datasets.items() for row in value["rows"]],
    }
    write_text(output_dir.parent / "preview-manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--shared-data", type=Path)
    args = parser.parse_args()
    manifest = run(args.source_dir, args.catalog, args.output_dir, args.shared_data)
    print(json.dumps({"product_count": manifest["product_count"], "menu_count": manifest["menu_count"], "changed_files": manifest["changed_files"], "unchanged_files": manifest["unchanged_files"]}, ensure_ascii=False))
