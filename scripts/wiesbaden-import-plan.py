#!/usr/bin/env python3
"""Build a reviewable target plan from frozen source/store snapshots. No mutations."""
import argparse
import importlib.util
import json
import re
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path

spec = importlib.util.spec_from_file_location("wiesbaden_source", Path(__file__).with_name("wiesbaden-data-run.py"))
source = importlib.util.module_from_spec(spec)
spec.loader.exec_module(source)

# Source paths are verified public manufacturer paths. Targets must also exist in
# the fresh store snapshot: no guessed collection IDs or automatic creations.
RULES = [
    ("kranen/wastafelkranen/opbouw", "opbouw-wastafelkranen", "Opbouw wastafelkraan"),
    ("kranen/wastafelkranen/inbouw", "inbouw-wastafelkranen", "Inbouw wastafelkraan"),
    ("kranen/wastafelkranen/inbouwuitlopen", "wastafeluitlopen", "Wastafeluitloop"),
    ("wastafels/wastafelkranen/opbouwkranen", "opbouw-wastafelkranen", "Opbouw wastafelkraan"),
    ("wastafels/wastafelkranen/inbouwkranen", "inbouw-wastafelkranen", "Inbouw wastafelkraan"),
    ("kranen/fonteinkranen/staand", "opbouw-fonteinkranen", "Opbouw fonteinkraan"),
    ("kranen/fonteinkranen/muur", "inbouw-fonteinkranen", "Inbouw fonteinkraan"),
    ("toilet/fonteinkranen/staand", "opbouw-fonteinkranen", "Opbouw fonteinkraan"),
    ("toilet/fonteinkranen/muur", "inbouw-fonteinkranen", "Inbouw fonteinkraan"),
    ("kranen/keukenkranen", "keukenkranen", "Keukenkraan"),
    ("kranen/specials/bidet", "bidetkranen", "Bidetkraan"),
    ("kranen/specials/hoekstopkranen", "hoekstopkranen", "Hoekstopkraan"),
    ("kranen/douchemengkranen/douchearmen", "hoofddouchehouders", "Douchearm"),
    ("douche/douchekranen/douchearmen", "hoofddouchehouders", "Douchearm"),
    ("kranen/douchemengkranen/douchekoppen", "hoofddouches", "Hoofddouche"),
    ("douche/douchekranen/douchekoppen", "hoofddouches", "Hoofddouche"),
    ("kranen/douchemengkranen/opbouwsets", "opbouw-douchesets", "Opbouw doucheset"),
    ("douche/douchekranen/opbouwsets", "opbouw-douchesets", "Opbouw doucheset"),
    ("douche/douchekranen/buitendouche", "buitendouches", "Buitendouche"),
    ("kranen/douchemengkranen/inbouw", "inbouw-douchekranen", "Inbouw douchekraan"),
    ("douche/douchekranen/inbouwkranen", "inbouw-douchekranen", "Inbouw douchekraan"),
    ("kranen/douchemengkranen/opbouw", "douchekranen", "Opbouw douchekraan"),
    ("douche/douchekranen/douchemengkraan", "douchekranen", "Douchekraan"),
    ("kranen/badmengkranen/inbouw", "inbouw-badkranen", "Inbouw badkraan"),
    ("bad/badkranen/inbouwkranen", "inbouw-badkranen", "Inbouw badkraan"),
    ("kranen/badmengkranen/opbouw", "badkranen", "Opbouw badkraan"),
    ("bad/badkranen/opbouwkranen", "badkranen", "Opbouw badkraan"),
    ("kranen/badmengkranen/vrijstaande-badmengkranen", "vrijstaande-badkranen", "Vrijstaande badkraan"),
    ("bad/badkranen/vrijstaande-badmengkranen", "vrijstaande-badkranen", "Vrijstaande badkraan"),
    ("bad/badkranen/inbouwbaduitlopen", "baduitlopen", "Baduitloop"),
    ("kranen/badmengkranen/baduitlopen", "baduitlopen", "Baduitloop"),
    ("douche/douchegarnituren/doucheslangen", "doucheslangen", "Doucheslang"),
    ("bad/badgarnituren/doucheslangen", "doucheslangen", "Doucheslang"),
    ("douche/douchegarnituren/glijstangen", "glijstangen", "Glijstang"),
    ("douche/douchegarnituren/handdouchehouders", "handdouchehouders", "Handdouchehouder"),
    ("bad/badgarnituren/handdouchehouders", "handdouchehouders", "Handdouchehouder"),
    ("douche/douchegarnituren/handdouches", "handdouches", "Handdouche"),
    ("bad/badgarnituren/handdouches", "handdouches", "Handdouche"),
    ("douche/inloopdouche", "inloopdouches", "Inloopdouche"),
    ("douche/nisdeuren/schuifdeur", "schuifdeuren", "Douche schuifdeur"),
    ("douche/nisdeuren/vouwdeur", "vouwdeuren", "Douche vouwdeur"),
    ("douche/nisdeuren", "douchedeuren", "Douchedeur"),
    ("douche/douchecabines", "douchecabines", "Douchecabine"),
    ("douche/douchebakken/toebehoren", "douche-accessoires", "Douchebaktoebehoren"),
    ("douche/douchebakken", "douchebakken", "Douchebak"),
    ("douche/toebehoren-douchewanden-en-cabines", "douche-accessoires", "Douchewandtoebehoren"),
    ("douche/afvoeren/doucheputten", "doucheputten", "Doucheput"),
    ("douche/afvoeren/losse-roosters-voor-de-douchegoten", "douche-accessoires", "Douchegootrooster"),
    ("douche/afvoeren", "douchegoten", "Douchegoot"),
    ("bad/badschermen", "badwanden", "Badwand"),
    ("bad/vrijstaande-baden/sifons", "sifons", "Badsifon"),
    ("bad/vrijstaande-baden", "vrijstaande-baden", "Vrijstaand bad"),
    ("bad/afvoeren", "badafvoeren-vulsystemen", "Badafvoer"),
    ("wastafels/opzetwastafels", "opzetwastafels", "Opzetwastafel"),
    ("wastafels/afvoeren/sifons", "sifons", "Wastafelsifon"),
    ("wastafels/afvoeren/wastes", "afvoerpluggen", "Afvoerplug"),
    ("toilet/afvoeren/sifons", "sifons", "Fonteinsifon"),
    ("toilet/afvoeren/wastes", "afvoerpluggen", "Afvoerplug"),
    ("badmeubels/afvoeren/sifons", "sifons", "Meubelsifon"),
    ("badmeubels/afvoeren/wastes", "afvoerpluggen", "Afvoerplug"),
    ("toilet/closets/douche-wc", "douche-wcs", "Douche-wc"),
    ("toilet/closets/drukplaten-toilet", "bedieningspanelen", "Bedieningspaneel"),
    ("toilet/closets/losse-zitting", "toiletzittingen", "Toiletzitting"),
    ("toilet/closets/wandclosets", "hangtoiletten", "Wandcloset"),
    ("toilet/fonteintjes", "losse-fonteinen", "Fontein"),
    ("badmeubels/kolomkast", "kolom-zijkasten", "Kolomkast"),
    ("badmeubels/onderkasten", "losse-onderkasten", "Onderkast"),
    ("badmeubels/modulair-systeem/onderkasten", "losse-onderkasten", "Onderkast"),
    ("badmeubels/modulair-systeem/topbladen", "wastafelbladen", "Wastafelblad"),
    ("badmeubels/modulair-systeem/beugels", "toebehoren", "Meubelbeugel"),
    ("badmeubels/meubelwastafels", "meubelwastafels", "Meubelwastafel"),
    ("badmeubels/accesoires", "toebehoren", "Meubeltoebehoren"),
    ("badkamerspiegels/spiegels/spiegelkasten", "spiegelkasten", "Spiegelkast"),
    ("badkamerspiegels/spiegels", "badkamerspiegels", "Badkamerspiegel"),
    ("badkamerspiegels/accessoires/led-lampen", "spiegelverlichting", "Spiegelverlichting"),
    ("badkamerspiegels/accessoires", "spiegelbevestiging", "Spiegeltoebehoren"),
    ("verlichting/hanglampen", "hanglampen", "Hanglamp"),
    ("verlichting/spots", "spots", "Spot"),
    ("radiatoren/elektrische-radiatoren", "elektrische-radiatoren", "Elektrische radiator"),
    ("radiatoren/radiatoren/design-radiatoren", "designradiatoren", "Designradiator"),
    ("radiatoren/radiatoren", "radiatoren", "Radiator"),
    ("radiatoren/bevestigingssets", "radiator-aansluitmateriaal", "Radiatortoebehoren"),
    ("radiatoren/vloerverwarming", "elektrische-vloerverwarming", "Elektrische vloerverwarming"),
    ("accessoires/glas-en-vloerwissers/vloerwisser", "wissers", "Vloerwisser"),
    ("accessoires/glas-en-vloerwissers", "douchewissers", "Douchewisser"),
    ("accessoires/reinigingsmiddelen", "onderhouds-en-schoonmaakmiddelen", "Onderhoudsmiddel"),
    ("accessoires/badkamer-accessoires/hulpmiddelen", "sanitaire-veiligheid", "Sanitair hulpmiddel"),
    ("accessoires/badkamer-accessoires", "accessoires", "Badkameraccessoire"),
]


def classify(p):
    name = p["name"].casefold()
    paths = [c.get("url_path", "").removeprefix("bekijk-assortiment/") for c in p["categories"]]
    # Parts cannot become a complete tap or shower set merely because of the
    # manufacturer's broad category membership.
    if "afbouwdeel" in name:
        return "afbouwdelen-voor-kranen", "Afbouwdeel kraan", "EXPLICIT_PART_NAME"
    if "inbouwdeel" in name and not re.search(r"compleet|incl|met (?:het )?inbouwdeel", name):
        return "losse-inbouwdelen", "Inbouwdeel kraan", "EXPLICIT_PART_NAME"
    if any(x in name for x in ["verlengset", "verlengstuk", "binnenwerk", "cartouche"]) and any("kranen" in c for c in paths):
        return "kraanonderdelen", "Kraanonderdeel", "EXPLICIT_PART_NAME"
    shower_context = any("douche" in x or "nisdeuren" in x for x in paths) or any(x in name for x in ["douche", "nisdeur"])
    if ("stabilisatiestang" in name or
            shower_context and any(x in name for x in ["glas voor", "los glas", "muurprofiel", "doucheprofiel", "douchebakpaneel", "voorzetpaneel"])):
        return "douche-accessoires", "Douchetoebehoren", "EXPLICIT_PART_NAME"
    if "fonteinset" in name or (re.search(r"one[ -]pack", name) and "fontein" in name):
        return "fonteinsets", "Fonteinset", "EXPLICIT_SET_NAME"
    if re.search(r"one[ -]pack", name) and "inbouwthermostaat" in name:
        return "inbouw-douchekranen", "Inbouwthermostaatset", "COMPLETE_THERMOSTAT_APPLICATION_REVIEW"
    if "accessoiresset" in name or "accessoires set" in name:
        return ("toilet-accessoires-sets" if "toilet" in name else "accessoires-sets"), "Accessoiresset", "EXPLICIT_SET_NAME"
    if "inbouwthermostaat" in name and "compleet" in name:
        if "baduitloop" in name:
            return "inbouw-badkranen", "Inbouw badkraanset", "EXPLICIT_COMPLETE_SET_NAME"
        if any(x in name for x in ["douche", "glijstang"]) or any("douche" in x for x in paths):
            return "inbouw-douchesets", "Inbouw doucheset", "EXPLICIT_COMPLETE_SET_NAME"
        return "inbouw-douchekranen", "Complete inbouwthermostaat", "COMPLETE_THERMOSTAT_APPLICATION_REVIEW"
    if "glijstangset" in name:
        return "glijstangsets", "Glijstangset", "EXPLICIT_SET_NAME"
    if "vrijstaand" in name and ("ligbad" in name or " bad " in " " + name + " "):
        if "half" in name or "tegen de wand" in name:
            return "halfvrijstaande-baden", "Halfvrijstaand bad", "EXPLICIT_NAME_AND_SOURCE"
    accessory_names = [("toiletrolhouder", "toiletrolhouders"), ("reserverolhouder", "reserverolhouders"),
        ("toiletborstelhouder", "toiletborstelhouders"), ("handdoekhaak", "handdoekhaken"),
        ("handdoekring", "handdoekringen"), ("handdoekrek", "handdoekrekken"),
        ("handdoekstang", "handdoekstangen"), ("zeepdispenser", "zeepdispensers"),
        ("zeephouder", "zeephouders"), ("glashouder", "glashouders"), ("planchet", "planchetten"),
        ("pedaalemmer", "afvalemmers"), ("douchewisserhouder", "douchewisserhouders"),
        ("inbouwnis", "inbouw-opbouw-nissen"), ("badgreep", "badgrepen")]
    if any(x.startswith("accessoires/") for x in paths):
        for word, target in accessory_names:
            if word in name:
                return target, word.capitalize(), "EXPLICIT_ACCESSORY_NAME_AND_SOURCE"
    matches = [(len(prefix), target, kind, prefix) for prefix, target, kind in RULES
               if any(path == prefix or path.startswith(prefix + "/") for path in paths)]
    if not matches:
        # An explicit manufacturer's product noun is useful where its own
        # category assignment is absent. Keep this evidence distinct from a
        # category-backed classification; review before applying.
        title_rules = [
            (r"\bregendoucheset\b|\bdoucheset\b", "douchesets", "Doucheset"),
            (r"\bbadmengkraan\b|\bbadkraan\b", "badkranen", "Badkraan"),
            (r"\bdouchemengkraan\b|\bdouchekraan\b", "douchekranen", "Douchekraan"),
            (r"\bnis schuifdeur\b|\bschuifdeur\b", "schuifdeuren", "Douche schuifdeur"),
            (r"\bvouwdeur\b", "vouwdeuren", "Douche vouwdeur"),
            (r"\bnisdeur\b", "douchedeuren", "Douchedeur"),
            (r"\binloopdouche\b", "inloopdouches", "Inloopdouche"),
            (r"\b(?:douche)?cabine\b", "douchecabines", "Douchecabine"),
            (r"\bdouchebak\b", "douchebakken", "Douchebak"),
            (r"\bwaskom\b|\bopzetwastafel\b", "opzetwastafels", "Opzetwastafel"),
            (r"\bkolomkast\b", "kolom-zijkasten", "Kolomkast"),
            (r"\bonderkast\b", "losse-onderkasten", "Onderkast"),
            (r"\bspiegelkast\b", "spiegelkasten", "Spiegelkast"),
            (r"\bspiegel\b", "badkamerspiegels", "Badkamerspiegel"),
            (r"\bwandcloset\b", "hangtoiletten", "Wandcloset"),
            (r"\bfontein\b", "losse-fonteinen", "Fontein"),
            (r"\bligbad\b", "baden", "Bad"),
            (r"\btoiletzitting\b", "toiletzittingen", "Toiletzitting"),
            (r"\bbedieningspaneel\b", "bedieningspanelen", "Bedieningspaneel"),
            (r"\bdouchegoot\b", "douchegoten", "Douchegoot"),
            (r"\bdoucheput\b", "doucheputten", "Doucheput"),
            (r"\bhanddouchehouder\b", "handdouchehouders", "Handdouchehouder"),
            (r"\bhoofddouchehouder\b", "hoofddouchehouders", "Hoofddouchehouder"),
            (r"\bhanddouche\b", "handdouches", "Handdouche"),
            (r"\bhoofddouche\b", "hoofddouches", "Hoofddouche"),
            (r"\bdoucheslang\b", "doucheslangen", "Doucheslang"),
            (r"\bglijstang\b", "glijstangen", "Glijstang"),
            (r"\bdouchearm\b", "hoofddouchehouders", "Douchearm"),
            (r"\bkeukenkraan\b", "keukenkranen", "Keukenkraan"),
            (r"\bhoekstopkraan\b", "hoekstopkranen", "Hoekstopkraan"),
            (r"\bfonteinkraan\b", "fonteinkranen", "Fonteinkraan"),
            (r"\bwastafelkraan\b", "wastafelkranen", "Wastafelkraan"),
            (r"\bafvoerplug\b|\bclickwaste\b", "afvoerpluggen", "Afvoerplug"),
            (r"\bsifon\b", "sifons", "Sifon"),
            (r"\bhanglamp\b", "hanglampen", "Hanglamp"),
            (r"\binbouwspot\b", "inbouwspots", "Inbouwspot"),
            (r"\belektrische radiator\b", "elektrische-radiatoren", "Elektrische radiator"),
            (r"\b(?:sier|design)radiator\b", "designradiatoren", "Designradiator"),
            (r"\bvloerverwarming\b", "elektrische-vloerverwarming", "Elektrische vloerverwarming"),
            (r"\binbouwnis\b", "inbouw-opbouw-nissen", "Inbouwnis"),
        ]
        for word, target in accessory_names:
            title_rules.append((r"\b"+re.escape(word)+r"\b", target, word.capitalize()))
        # The first product noun identifies the main article. A later mention
        # after 'voor' or an accessory noun cannot turn a part into its parent.
        guard = re.search(r"\b(?:voor|houder|onderdeel|profiel|beugel|steun|paneel|frame|rozet)\b", name)
        candidates = [(match.start(), target, kind) for pattern, target, kind in title_rules
                      if (match := re.search(pattern, name)) and (not guard or match.start() < guard.start())]
        if candidates:
            _, target, kind = min(candidates)
            return target, kind, "EXPLICIT_SOURCE_NAME_REVIEW"
        return None, None, "NO_RULE_REVIEW"
    best = max(matches)
    equally_specific = {x[1] for x in matches if x[0] == best[0]}
    if len(equally_specific) > 1:
        return None, None, "CONFLICTING_SOURCE_CATEGORIES_REVIEW"
    return best[1], best[2], "SOURCE_CATEGORY_RULE"


def menu_paths(menus):
    paths = defaultdict(list)
    def walk(items, trail):
        for item in items:
            current = trail + [{k: item.get(k) for k in ["title", "url", "resourceId"]}]
            if item.get("resourceId"):
                paths[item["resourceId"]].append(current)
            walk(item.get("items", []), current)
    for menu in sorted(menus, key=lambda x: x["handle"] != "main-menu"):
        walk(menu["items"], [])
    return paths


def cast(value, definition):
    kind = definition["type"]["name"]
    if value == "":
        return None, "EMPTY_SOURCE_NO_WRITE"
    if kind == "single_line_text_field":
        if value.casefold() in ("overig", "overige", "onbekend", "n.v.t.", "nvt"):
            return None, "GENERIC_SOURCE_VALUE_REVIEW"
        return value, "TYPED_VALUE_CANDIDATE"
    if kind == "boolean":
        if value.casefold() in ["ja", "nee"]:
            return value.casefold() == "ja", "TYPED_VALUE_CANDIDATE"
        return None, "BOOLEAN_NOT_EXPLICIT_REVIEW"
    if kind in ["number_decimal", "number_integer"]:
        if definition["key"] == "aantal_kraangaten":
            holes = re.fullmatch(r"([0-9]+)-gats", value, re.I)
            if holes:
                return holes[1], "TYPED_VALUE_CANDIDATE"
        match = re.fullmatch(r"\s*([0-9]+(?:[.,][0-9]+)?)\s*(mm|cm|m)?\s*", value, re.I)
        if not match:
            return None, "NUMERIC_VALUE_REVIEW"
        n = Decimal(match[1].replace(",", "."))
        if definition["key"].endswith("_mm"):
            if not match[2]:
                return None, "SOURCE_UNIT_MISSING_REVIEW"
            n *= {"mm": Decimal(1), "cm": Decimal(10), "m": Decimal(1000)}[match[2].lower()]
        elif match[2]:
            return None, "TARGET_UNIT_UNDEFINED_REVIEW"
        if kind == "number_integer" and n != int(n):
            return None, "INTEGER_VALUE_REVIEW"
        return str(n), "TYPED_VALUE_CANDIDATE"
    return None, "TARGET_TYPE_REVIEW"


def filter_candidates(record, definitions):
    # Only explicit equivalent facts. Do not infer colour groups or dimensions
    # from unlabelled title numbers. Keep conflicting aliases for review.
    aliases = {"oppervlaktebehandeling": "afwerking", "materiaal_kraan": "materiaal",
        "met_omstelinrichting": "met_omstel", "met_overloopgat": "met_overloop",
        "overloop": "met_overloop", "uitloop_draaibaar": "draaibare_uitloop",
        "soft_close_systeem": "softclose"}
    by_key = {d["key"]: d for d in definitions}
    by_label = {source.slug(d["name"]): d for d in definitions}
    candidates = []
    for item in record["specifications"]:
        label = source.slug(item["label"])
        target = by_key.get(aliases.get(label, label)) or by_label.get(label)
        if not target:
            continue
        value, status = cast(item["value"], target)
        candidates.append({"source_label": item["label"], "source_value": item["value"],
            "proposed_field": "bc_filters."+target["key"], "proposed_type": target["type"]["name"],
            "proposed_value": value, "mapping_status": status})
    grouped = defaultdict(list)
    for item in candidates:
        if item["mapping_status"] == "TYPED_VALUE_CANDIDATE":
            grouped[item["proposed_field"]].append(item)
    for items in grouped.values():
        if len({json.dumps(x["proposed_value"], ensure_ascii=False) for x in items}) > 1:
            for item in items:
                item["mapping_status"] = "CONFLICTING_SOURCE_FACTS_REVIEW"
    return candidates


def grouped_specs(record):
    groups = defaultdict(list)
    for item in record["specifications"]:
        label, value = item["label"], item["value"]
        if not value:
            continue
        k = source.slug(label)
        if k in ["sku", "merk", "serie", "model", "uitvoering"]:
            group = "Product"
        elif any(x in k for x in ["breedte", "hoogte", "lengte", "diepte", "diameter", "dikte"]):
            group = "Afmetingen en verstelbaarheid"
        elif any(x in k for x in ["montage", "aansluit", "bevestig", "rozet"]):
            group = "Montage en aansluiting"
        elif any(x in k for x in ["kleur", "materiaal", "glans", "oppervlakte", "vorm", "profiel"]):
            group = "Materiaal en uitvoering"
        else:
            group = "Eigenschappen"
        # Preserve display strings including explicit 'Nee' and '0'. Do not
        # invent units or replace missing data with a negative statement.
        groups[group].append({"key": "fabrikantnummer" if k == "sku" else k,
                              "label": "Artikelnummer" if k == "sku" else label,
                              "value": value})
    return [{"group": name, "items": items} for name, items in groups.items()]


def current_change(product_id, field, value, snapshots):
    if not product_id:
        return {"current_value": None, "change_status": "NEW_PRODUCT_CANDIDATE"}
    snapshot = snapshots[product_id]
    existing = next((m for m in snapshot["metafields"]["nodes"]
                     if m["namespace"]+"."+m["key"] == field), None)
    if existing is None:
        status, old = "NEW_FIELD_CANDIDATE", None
    else:
        old = existing["value"]
        comparable = old
        if existing["type"] in ("json", "boolean", "number_decimal", "number_integer"):
            try:
                comparable = json.loads(old)
            except (ValueError, TypeError):
                pass
        if existing["type"].startswith("number_") and value is not None:
            same = str(comparable) == str(value)
            try:
                same = Decimal(str(comparable)) == Decimal(str(value))
            except InvalidOperation:
                pass
        else:
            same = comparable == value
        status = "SAME_VALUE" if same else "CHANGE_REQUIRES_REVIEW"
    return {"current_value": old, "change_status": status,
            "snapshot_updated_at": snapshot["updatedAt"]}


def main(root):
    root = Path(root)
    structure = source.load_json(root/"shopify/current-structure.json")
    products = source.load_json(root/"manufacturer-catalogue.json")["products"]
    collections = {c["handle"]: c for c in structure["collections"]["nodes"]}
    by_path = menu_paths(structure["menus"]["nodes"])
    # Verified current Wiesbaden data and its 16-Oct renderer use custom.*.
    # specs.* belongs to the JEE-O mapping: don't populate an unused namespace.
    spec_defs = [d for d in structure["metafieldDefinitions"]["nodes"] if d["namespace"] == "custom"]
    by_label = defaultdict(list)
    for d in spec_defs:
        by_label[source.slug(d["name"])].append(d)
    aliases = {"materiaal_kraan": "materiaal", "oppervlaktebehandeling": "afwerking",
               "montagewijze": "montage", "sku": "artikelnummer"}
    comparison = {r["sku"]: r for r in source.load_json(root/"output/comparison.json")}
    snapshots = {p["id"]: p for p in source.load_json(root/"shopify/current-product-metafields.json")}
    filter_defs = [d for d in structure["metafieldDefinitions"]["nodes"] if d["namespace"] == "bc_filters"]
    targets, fields, complete, filters = [], [], [], []
    for p in products:
        primary, product_type, reason = classify(p)
        current = comparison[p["sku"]]
        issues = list(current["issues"])
        if "REVIEW" in reason:
            issues.append("CLASSIFICATION_REQUIRES_REVIEW")
        if reason == "EXPLICIT_SOURCE_NAME_REVIEW":
            issues.append("SOURCE_CATEGORY_ABSENT_NAME_RULE_REQUIRES_REVIEW")
        breadcrumb, memberships = [], []
        if primary not in collections:
            issues.append("NO_EXISTING_TARGET_COLLECTION_REVIEW")
        else:
            c = collections[primary]
            candidates = by_path.get(c["id"], [])
            if candidates:
                breadcrumb = candidates[0]
                memberships = [item["url"].split("/collections/")[-1].split("?")[0]
                               for item in breadcrumb if item.get("resourceId")
                               and item.get("url") and "/collections/" in item["url"]]
            else:
                issues.append("NO_CURRENT_MENU_BREADCRUMB_REVIEW")
                memberships = [primary]
        targets.append({"sku": p["sku"], "name": p["name"], "comparison_status": current["comparison_status"],
            "proposed_product_type": product_type, "primary_collection": primary,
            "proposed_collection_memberships": memberships, "target_breadcrumb": breadcrumb,
            "classification_evidence": reason, "collections_to_add": sorted(set(memberships)-set(current["current_collections"])),
            "existing_collections_to_review": sorted(set(current["current_collections"])-set(memberships)),
            "issues": issues, "status": "PROPOSED_NOT_APPLIED"})
        path = source.product_path(root, p)
        if not path.exists():
            continue
        record = source.load_json(path)
        complete.append({"sku": p["sku"], "product_id": current["product_id"],
            "namespace": "custom", "key": "complete_specificaties", "type": "json",
            "value": grouped_specs(record), "source_url": record["source"]["url"],
            "source_sha256": record["source"]["sha256"], "source_issues": current["issues"],
            **current_change(current["product_id"], "custom.complete_specificaties", grouped_specs(record), snapshots),
            "status": "PROPOSED_NOT_APPLIED_RENDERER_ROUTE_REQUIRES_REVIEW"})
        for item in filter_candidates(record, filter_defs):
            filters.append({"sku": p["sku"], "product_id": current["product_id"], **item,
                **current_change(current["product_id"], item["proposed_field"], item["proposed_value"], snapshots),
                "write_gate": "VERIFY_MANIFEST_AND_EXTERNAL_INDEX_CONTRACT_BEFORE_APPLY"})
        for s in record["specifications"]:
            if s["label"] == "Merk":
                continue  # Native product vendor; brand conflicts are reviewed separately.
            label = source.slug(s["label"])
            candidates = by_label[label]
            if not candidates and label in aliases:
                candidates = [d for d in spec_defs if d["key"] == aliases[label]]
            candidate = candidates[0] if len(candidates) == 1 else None
            value, state = cast(s["value"], candidate) if candidate else (None, "NO_UNIQUE_TARGET_DEFINITION_REVIEW")
            fields.append({"sku": p["sku"], "product_id": current["product_id"],
                "source_label": s["label"], "source_value": s["value"],
                "proposed_field": candidate["namespace"]+"."+candidate["key"] if candidate else None,
                "proposed_type": candidate["type"]["name"] if candidate else None,
                "proposed_value": value, "mapping_status": state,
                **(current_change(current["product_id"], candidate["namespace"]+"."+candidate["key"], value, snapshots) if candidate else {}),
                "write_gate": "VERIFY_CURRENT_PDP_AND_FILTER_CONTRACT_BEFORE_APPLY"})
    out = root/"output"
    source.write_json(out/"category-import-proposal.json", targets)
    source.write_csv(out/"category-import-proposal.csv", targets, list(targets[0]))
    source.write_json(out/"specification-field-proposal.json", fields)
    source.write_json(out/"complete-specifications-proposal.json", complete)
    source.write_json(out/"filter-field-proposal.json", filters)
    source.write_csv(out/"filter-field-proposal.csv", filters, list(filters[0]) if filters else [])
    source.write_csv(out/"specification-field-proposal.csv", fields, list(fields[0]) if fields else [])
    report = {"built_at": source.now(), "products": len(targets),
        "classification_reasons": dict(Counter(r["classification_evidence"] for r in targets)),
        "category_review_issues": dict(Counter(i for r in targets for i in r["issues"])),
        "specification_values_available": len(fields),
        "field_mapping_status": dict(Counter(r["mapping_status"] for r in fields)),
        "filter_value_proposals": len(filters),
        "filter_mapping_status": dict(Counter(r["mapping_status"] for r in filters)),
        "existing_field_changes": dict(Counter(r.get("change_status", "UNMAPPED") for r in fields)),
        "live_writes": 0, "renderer_filter_contract_verified": False}
    source.write_json(out/"mapping-summary.json", report)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", required=True)
    args = parser.parse_args()
    main(args.run_dir)
