#!/usr/bin/env python3
"""Offline Wiesbaden bulk-verrijking: reviewvoorstellen, NOOIT live writes.

Input: BadkamerCity_Wiesbaden_datarun_20261019.zip of de uitgepakte outputmap.
Output: 50 per-SKU JSON voorstellen, manifest en CSV reviewrapport.
Alleen Python standaardbibliotheek; behoud bestaande prijs, voorraad, handle,
afbeeldingen, variant, publicatie, collectieleden en externe filterindex.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import html
import io
import json
import re
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

VERSION = "wiesbaden-bulk-review-v1.1"
APPROVED = {"24.3710", "20.3755", "20.3756", "32.3411", "32.3594", "32.2510", "32.3670", "38.4125"}
HOLDS = {"29.8007": "KNOWN_IDENTITY_AND_COLOUR_CONFLICT", "41.3540": "KNOWN_RADIATOR_TECH_CONFLICT"}
PROFILES = {
    "Opbouwwastafelkraan": (12, "opbouw wastafelkraan", {"opbouw-wastafelkranen"}, "wastafel", "TAP"),
    "Fonteinkraan": (10, "fonteinkraan", {"opbouw-fonteinkranen", "inbouw-fonteinkranen"}, "fontein", "TAP"),
    "Inbouwwastafelkraan": (6, "inbouw wastafelkraan", {"inbouw-wastafelkranen"}, "wastafel", "INBOUW"),
    "Thermostatische douchekraan": (5, "thermostatische douchekraan", {"douchekranen", "inbouw-douchekranen"}, "douche", "THERMO"),
    "Afbouwdeel voor douchekraan": (5, "afbouwdeel voor douchekraan", {"afbouwdelen-voor-kranen"}, "douchekraan", "PART"),
    "Thermostatische badkraan": (4, "thermostatische badkraan", {"badkranen", "inbouw-badkranen"}, "bad", "THERMO"),
    "Inbouwdeel voor douchekraan": (3, "inbouwdeel voor douchekraan", {"losse-inbouwdelen"}, "douchekraan", "PART"),
    "Vrijstaande badkraan": (3, "vrijstaande badkraan", {"vrijstaande-badkranen"}, "bad", "INBOUW"),
    "Fonteinkraanset": (2, "fonteinkraanset", {"fonteinsets"}, "fontein", "SET"),
}
assert sum(p[0] for p in PROFILES.values()) == 50
SENSITIVE = re.compile(r"\b(?:ean|gtin|barcode|inkoopprijs|voorraad|levertijd|garantieduur)\b", re.I)
MEASURE = re.compile(r"\b(hoogte|breedte|diepte|lengte|voorsprong|uitloophoogte|dikte|hartafstand|diameter)\b", re.I)
BAD_CLAIM = re.compile(r"\b(?:gratis|duurzaam|levenslang|altijd op voorraad|binnen \d+ dagen)\b", re.I)


def canonical(obj):
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def dump(obj):
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, indent=2) + "\n"


def digest(obj):
    return hashlib.sha256(canonical(obj).encode("utf-8")).hexdigest()


class Datarun:
    def __init__(self, source: Path):
        self.source = source
        self.archive = zipfile.ZipFile(source) if source.is_file() and zipfile.is_zipfile(source) else None
        if self.archive:
            choices = [x for x in self.archive.namelist() if x.endswith("/output/product-master.jsonl")]
            if len(choices) != 1:
                raise ValueError("Precies één output/product-master.jsonl nodig")
            self.prefix = choices[0].removesuffix("product-master.jsonl")
        else:
            paths = [source / "output", source, source / "Wiesbaden_20261019" / "output"]
            self.prefix = next((x for x in paths if (x / "product-master.jsonl").is_file()), None)
            if self.prefix is None:
                raise FileNotFoundError("product-master.jsonl niet gevonden")

    def read(self, name):
        if self.archive:
            return self.archive.read(self.prefix + name).decode("utf-8-sig")
        return (self.prefix / name).read_text(encoding="utf-8-sig")

    def json(self, name):
        return json.loads(self.read(name))

    def jsonl(self, name):
        return [json.loads(x) for x in self.read(name).splitlines() if x.strip()]


def keyed(rows, label):
    index, duplicates = {}, set()
    for row in rows:
        sku = str(row.get("sku") or "").strip()
        if sku in index:
            duplicates.add(sku)
        index[sku] = row
    if not index:
        raise ValueError("Lege input voor " + label)
    return index, duplicates


def selection(products, limit):
    by_type = defaultdict(list)
    for item in products:
        if item.get("comparison_status") == "EXISTING_WIESBADEN" and item.get("source_brand") == "Wiesbaden" and item.get("current_vendor") == "Wiesbaden":
            if item.get("current_product_type") in PROFILES:
                by_type[item["current_product_type"]].append(item)
    selected = []
    for name, (count, *_rest) in PROFILES.items():
        pool = sorted(by_type[name], key=lambda x: x["sku"])
        pinned = [p for p in pool if p["sku"] in ("24.3710", "29.8007")]
        rest = [p for p in pool if p["sku"] not in ("24.3710", "29.8007")]
        step = max(1, len(rest) // max(1, count - len(pinned)))
        take = pinned + rest[::step][:count - len(pinned)]
        if len(take) < count:
            take += [p for p in rest if p not in take][:count-len(take)]
        if len(take) != count:
            raise ValueError("Te weinig bestaande artikelen voor " + name)
        selected.extend(take)
    if len(selected) != 50 or len({x["sku"] for x in selected}) != 50:
        raise ValueError("Dubbele SKU of onvolledige 50-stuks steekproef")
    return selected[:limit]


def facts_for(product):
    evidence = product.get("source_evidence") or {}
    facts = []
    for field in product.get("specifications", []):
        label = str(field.get("label") or "").strip()
        raw = str(field.get("value") or "").strip()
        if not label or not raw or SENSITIVE.search(label):
            continue
        value, unit = raw, None
        if raw.casefold() in ("ja", "nee"):
            value = raw.casefold() == "ja"
        elif MEASURE.search(label):
            match = re.fullmatch(r"\s*(\d+(?:[.,]\d+)?)\s*(mm|cm)\s*", raw, re.I)
            if match:
                value = round(float(match.group(1).replace(",", ".")) * (10 if match.group(2).lower() == "cm" else 1), 3)
                unit = "mm"
        facts.append({"label": label, "raw": raw, "value": value, "unit": unit,
                      "source_url": product.get("source_url"), "source_sha256": evidence.get("sha256"),
                      "fetched_at": evidence.get("fetched_at")})
    return facts


def shorten(text, length):
    if len(text) <= length:
        return text
    return text[:length+1].rsplit(" ", 1)[0].rstrip(" –-,;:")


def propose_copy(p, profile, facts, cat):
    _, noun, _, use, kind = profile
    lookup = {f["label"].casefold(): f["value"] for f in facts}
    series = lookup.get("serie")
    colour = lookup.get("basiskleur") or lookup.get("kleur")
    if isinstance(colour, str) and colour.casefold() in ("overig", "onbekend", "nvt"):
        colour = None
    name = re.sub(r"\b(?:KIWA|FSC)[ -]?(?:gekeurd)?\b", "", str(p.get("name") or ""), flags=re.I)
    name = re.sub(r"\s+", " ", name).strip(" -–")
    title = shorten("Wiesbaden " + (name or " ".join(str(x) for x in (series, noun) if x)), 112)
    if kind == "PART":
        intro = f"Dit {html.escape(noun)} van Wiesbaden is een afzonderlijk onderdeel voor een {html.escape(use)}. Het is niet automatisch een complete kraan. Controleer welke andere onderdelen erbij passen."
    elif kind == "SET":
        intro = f"Deze Wiesbaden {html.escape(noun)} is bedoeld voor de {html.escape(use)}. De exacte meegeleverde onderdelen moeten nog worden geverifieerd."
    else:
        place = {"wastafel":"de wastafel", "fontein":"de fontein", "douche":"de douche", "bad":"het bad"}.get(use, "de badkamer")
        intro = f"De {html.escape(title)} is een {html.escape(noun)} voor {place}."
    paragraphs = ["<p>" + intro + "</p>"]
    sentences, claims = [], []
    for key, sentence in (
        ("materiaal kraan", lambda v: f"Het kraanlichaam is volgens de fabrikant van {v}."),
        ("basiskleur", lambda v: f"De opgegeven basiskleur is {v}."),
        ("oppervlaktebehandeling", lambda v: f"De fabrikant noemt de afwerking {v.lower()}."),
        ("montage", lambda v: f"De aangegeven montagewijze is {v}."),
        ("montagewijze", lambda v: f"De aangegeven montagewijze is {v}."),
        ("maat aansluiting aanvoer", lambda v: f"De aanvoeraansluiting is opgegeven als {v}."),
    ):
        val = lookup.get(key)
        if isinstance(val, str) and val.casefold() not in ("overig", "onbekend", "nvt") and len(val) < 65:
            text = sentence(val)
            sentences.append(text)
            claims.append({"text": text, "facts": [key]})
    holes = lookup.get("aantal kraangaten")
    if kind not in ("PART", "SET") and isinstance(holes, str):
        match = re.fullmatch(r"([1-4])-gats", holes.strip())
        if match:
            s = f"Voor de montage worden {int(match.group(1))} kraangaten aangegeven."
            sentences.append(s)
            claims.append({"text": s, "facts": ["aantal kraangaten"]})
    if lookup.get("coldstart") is True and kind == "TAP":
        s = "Deze uitvoering heeft een coldstart-functie."
        sentences.append(s)
        claims.append({"text": s, "facts": ["coldstart"]})
    if sentences:
        paragraphs.append("<h2>Uitvoering en eigenschappen</h2><p>" + " ".join(html.escape(s) for s in sentences[:7]) + "</p>")
    paragraphs.append("<h2>Voor bestelling controleren</h2><p>Vergelijk de afmetingen en aansluitingen met de gekozen montageplek. Bekijk ook of aanvullende onderdelen nodig zijn.</p>")
    bc = [x.get("url", "") for x in (cat or {}).get("target_breadcrumb", [])]
    if bc and re.fullmatch(r"/collections/[a-z0-9-]+", bc[-1]):
        paragraphs.append('<p>Bekijk ook onze <a href="' + html.escape(bc[-1], quote=True) + '">bijpassende producten</a>.</p>')
    seo_base = " ".join(str(x) for x in ("Wiesbaden", series, noun) if x)
    if colour and len(seo_base + " – " + str(colour) + " | BadkamerCity") <= 60:
        seo_base += " – " + str(colour)
    seo_title = shorten(seo_base, 60-len(" | BadkamerCity")) + " | BadkamerCity"
    meta_base = "Wiesbaden " + (str(series) + " " if series else "") + noun
    if colour:
        meta_base += " in " + str(colour)
    if lookup.get("coldstart") is True and kind == "TAP":
        meta_base += " met coldstart"
    meta = ""
    for tail in (". Bekijk de uitvoering, specificaties en montage-info bij BadkamerCity.",
                 ". Bekijk de technische gegevens en uitvoering bij BadkamerCity.",
                 ". Bekijk de specificaties bij BadkamerCity.", ". Bekijk de specificaties."):
        if len(meta_base+tail) <= 155:
            meta = meta_base + tail
            break
    if not meta:
        meta = shorten(meta_base, 150).rstrip("., ") + "."
    n = int(p.get("image_count") or 0)
    alt = ("Wiesbaden " + str(series or "") + " " + noun + " " + str(colour or "")).strip() if n > 0 else None
    return {"title": title, "card_title": shorten(title, 72), "description_html": "".join(paragraphs),
            "seo": {"title": seo_title, "description": meta}, "image_alt_candidate": alt,
            "claim_evidence": claims,
            "copy_notes": (["PART_COMPATIBILITY_REQUIRES_MANUAL_VERIFICATION"] if kind=="PART" else
                           ["SET_CONTENTS_REQUIRES_MANUAL_VERIFICATION"] if kind=="SET" else [])}


def evaluate(p, category, filter_items, specproposal, duplicates):
    sku = p["sku"]
    profile = PROFILES[p["current_product_type"]]
    blockers, warnings = [], []
    if sku in duplicates: blockers.append("DUPLICATE_SOURCE_SKU")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9.\-_/]*", sku): blockers.append("INVALID_SKU")
    if p.get("source_brand") != "Wiesbaden" or p.get("current_vendor") != "Wiesbaden": blockers.append("BRAND_MISMATCH")
    if p.get("comparison_status") != "EXISTING_WIESBADEN" or not p.get("product_id") or not p.get("variant_id"):
        blockers.append("NOT_AN_EXACT_EXISTING_SKU_MATCH")
    proof = p.get("source_evidence") or {}
    if proof.get("url") != p.get("source_url") or not re.fullmatch(r"[a-f0-9]{64}", str(proof.get("sha256") or "")) or proof.get("http_status") != 200:
        blockers.append("SOURCE_PROVENANCE_MISSING_OR_INVALID")
    for issue in p.get("issues", []):
        (blockers if any(x in issue for x in ("CONFLICT","SET_COMPONENTS","SOURCE_BRAND","ZERO_OR_NEGATIVE","SPARSE_SPECIFICATIONS")) else warnings).append(issue)
    if sku in HOLDS: blockers.append(HOLDS[sku])
    if sku in APPROVED: warnings.append("ALREADY_REVIEWED_PREVIOUSLY_PRESERVE_LIVE_CONTENT")
    facts = facts_for(p)
    values = {x["label"].casefold():x["value"] for x in facts}
    by_key = defaultdict(set)
    for x in facts: by_key[x["label"].casefold()].add(canonical(x["value"]))
    for key, vals in by_key.items():
        if len(vals)>1:blockers.append("CONFLICTING_DUPLICATE_SPEC_"+key.replace(" ","_"))
    holes = values.get("aantal kraangaten")
    if isinstance(holes,str):
        match=re.search(r"\d+",holes)
        if match and int(match.group())>4:blockers.append("UNPLAUSIBLE_KRAANGAT_COUNT_REVIEW")
    if "afbouwdeel" in p["name"].casefold() and str(values.get("model","")).casefold()=="inbouwdeel":
        blockers.append("PART_TYPE_CONFLICT_MODEL_INBOUWDEEL_VS_AFBOUWDEEL")
    if "mat zwart" in p["name"].casefold() and str(values.get("basiskleur","")).casefold() in ("chroom","wit","rvs"):
        blockers.append("COLOUR_CONFLICT_TITLE_VS_BASISKLEUR")
    _, _, expected, _, kind = profile
    if len(facts)<6:blockers.append("ESSENTIAL_SPECS_TOO_SPARSE")
    if kind in ("TAP","THERMO","INBOUW") and not any(k in values for k in ("montage","montagewijze","aansluiting aanvoer","maat aansluiting aanvoer","aantal kraangaten","type aansluiting")):
        warnings.append("MOUNTING_OR_CONNECTION_NEEDS_VERIFICATION")
    if kind=="PART":blockers.append("PART_COMPATIBILITY_NOT_VERIFIED")
    if kind=="SET":blockers.append("SET_COMPONENTS_NOT_VERIFIED")
    cat = category or {}
    primary=cat.get("primary_collection")
    if primary not in expected:blockers.append("CATEGORY_INCOMPATIBLE_WITH_PRODUCT_TYPE")
    bc=cat.get("target_breadcrumb") or []
    if not bc or not all(re.fullmatch(r"/collections/[a-z0-9-]+",x.get("url","")) and str(x.get("resourceId","")).startswith("gid://shopify/Collection/") for x in bc):
        blockers.append("BREADCRUMB_IDENTITY_UNVERIFIED")
    elif bc[-1]["url"] != "/collections/"+str(primary):
        blockers.append("BREADCRUMB_PRIMARY_COLLECTION_CONFLICT")
    if cat.get("classification_evidence")!="SOURCE_CATEGORY_RULE":
        warnings.append("CATEGORY_ONLY_INFERRED_FROM_NAME_OR_PART_RULE")
    if cat.get("collections_to_add"):warnings.append("COLLECTION_MEMBERSHIP_NOT_YET_PRESENT")
    warnings.extend(cat.get("issues") or [])
    if specproposal.get("product_id")!=p.get("product_id") or specproposal.get("sku")!=sku:
        blockers.append("SPECIFICATION_PROPOSAL_IDENTITY_CONFLICT")
    groups=[]
    for group in specproposal.get("value") or []:
        clean=[x for x in group.get("items",[]) if not SENSITIVE.search(str(x.get("key",""))+" "+str(x.get("label","")))]
        if clean:groups.append({"group":group.get("group"),"items":clean})
    if not groups:blockers.append("NO_GROUPED_SPECIFICATIONS")
    filters, held=[],[]
    original={x["label"].casefold():x for x in facts}
    types={"single_line_text_field":str,"number_integer":int,"boolean":bool}
    for item in filter_items:
        field=str(item.get("proposed_field") or "")
        key=str(item.get("source_label") or "").casefold()
        val=item.get("proposed_value")
        expected_type=types.get(item.get("proposed_type"))
        if expected_type is int and type(val) is str and re.fullmatch(r"[0-9]{1,4}",val):
            val=int(val)
        if (item.get("product_id")!=p.get("product_id") or key not in original or
            not re.fullmatch(r"bc_filters\.[a-z][a-z0-9_]*",field) or SENSITIVE.search(field) or
            item.get("mapping_status")!="TYPED_VALUE_CANDIDATE" or expected_type is None or
            type(val) is not expected_type):
            held.append({"field":field,"reason":"UNVERIFIED_FILTER_IDENTITY_OR_TYPE"});continue
        raw=original[key]["raw"]
        if str(item.get("source_value","")).strip()!=raw:
            held.append({"field":field,"reason":"FILTER_SOURCE_VALUE_CHANGED"});continue
        if expected_type is int and (not 0<=val<=1000 or not (raw==str(val) or (key=="aantal kraangaten" and raw.casefold()==f"{val}-gats"))):
            held.append({"field":field,"reason":"NUMERIC_FILTER_OUT_OF_RANGE_OR_SOURCE_CONFLICT"});continue
        filters.append({"field":field,"type":item["proposed_type"],"value":val,"source_label":item["source_label"],"source_value":item["source_value"],
                        "apply_gate":"INDEX_MANIFEST_AND_SHOPIFY_DEFINITION_UNVERIFIED"})
    duplicate_keys={x for x,c in Counter(z["field"] for z in filters).items() if c>1}
    if duplicate_keys:
        blockers.append("DUPLICATE_FILTER_KEY")
        filters=[x for x in filters if x["field"] not in duplicate_keys]
    if held:warnings.append("SOME_FILTERS_REQUIRE_REVIEW")
    content=propose_copy(p, profile, facts, cat)
    for value in (content["title"],content["description_html"],*content["seo"].values()):
        if BAD_CLAIM.search(value):blockers.append("UNSUPPORTED_MARKETING_CLAIM")
        if re.search(r"\b(?:EAN|GTIN)\b",value,re.I):blockers.append("IDENTIFIER_LEAK_IN_COPY")
    if len(content["seo"]["title"])>60 or len(content["seo"]["description"])>155:
        blockers.append("SEO_LENGTH_OVER_LIMIT")
    for claim in content["claim_evidence"]:
        if not all(k in values for k in claim["facts"]):blockers.append("UNSOURCED_TEXT_CLAIM")
    blockers=sorted(set(blockers));warnings=sorted(set(warnings))
    status="BLOCKED_FACTS_OR_IDENTITY" if blockers else "EDITORIAL_REVIEW_REQUIRED"
    if sku in APPROVED:status="EXISTING_REVIEWED_DO_NOT_REPLACE"
    return {"sku":sku,"status":status,"run_rule_version":VERSION,
            "input_sha256":digest({"version":VERSION,"product":p,"category":category,"filters":filter_items,"specproposal":specproposal}),
            "product_type":p["current_product_type"],"source_title":p["name"],
            "current_store_title_at_snapshot":p.get("current_title"),
            "product_id":p.get("product_id"),"variant_id":p.get("variant_id"),
            "source":{"url":p.get("source_url"),"sha256":proof.get("sha256"),"fetched_at":proof.get("fetched_at")},
            "facts":facts,"issues_blocking":blockers,"issues_review":warnings,
            "category":{"primary":primary,"classification_evidence":cat.get("classification_evidence"),
                        "category_handles":[x["url"].removeprefix("/collections/") for x in bc],
                        "breadcrumb_targets":bc,"membership_to_add_review_only":cat.get("collections_to_add",[])},
            "specifications_proposal":groups,"filters_proposal":filters,"filters_needing_review":held,
            "content_proposal":content,
            "write_permissions":{"shopify":False,"theme":False,"search_index":False},
            "verification_before_write":["FRESH_SHOPIFY_IDENTITY_AND_DIGEST","MERCHANT_CONTENT_REVIEW",
                                         "LIVE_COLLECTION_MEMBERSHIP","SHARED_RENDERER","EXTERNAL_FILTER_INDEX_ROUTE"]}


def write_if_changed(path, value):
    content=value.encode("utf-8")
    if path.exists() and path.read_bytes()==content:
        return False
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_bytes(content)
    return True


def run(input_path:Path, output:Path, limit:int=50):
    if not 1<=limit<=50:raise ValueError("limit 1..50 vereist")
    source=Datarun(input_path)
    master=source.jsonl("product-master.jsonl")
    products,dup_products=keyed(master,"product")
    chosen=selection(master,limit)
    category,dup_category=keyed(source.json("category-import-proposal.json"),"category")
    specs,dup_specs=keyed(source.json("complete-specifications-proposal.json"),"spec")
    filters=defaultdict(list)
    for item in source.json("filter-field-proposal.json"):
        filters[str(item["sku"])].append(item)
    duplicates=dup_products|dup_category|dup_specs
    counts,profiles,skus,rows=Counter(),Counter(),[],[]
    generated=reused=0
    for item in chosen:
        sku=item["sku"]
        proposal=evaluate(item,category.get(sku),filters[sku],specs.get(sku,{}),duplicates)
        changed=write_if_changed(output/"products"/(sku+".json"),dump(proposal))
        generated+=int(changed);reused+=int(not changed)
        counts[proposal["status"]]+=1;profiles[proposal["product_type"]]+=1;skus.append(sku)
        rows.append({"sku":sku,"product_type":proposal["product_type"],"status":proposal["status"],
                     "blocking_issues":" | ".join(proposal["issues_blocking"]),
                     "review_issues":" | ".join(proposal["issues_review"]),
                     "source_facts":len(proposal["facts"]),"filter_candidates":len(proposal["filters_proposal"]),
                     "category":proposal["category"]["primary"],"source_url":proposal["source"]["url"]})
    buffer=io.StringIO(newline="")
    writer=csv.DictWriter(buffer,fieldnames=list(rows[0]))
    writer.writeheader();writer.writerows(rows)
    write_if_changed(output/"review-50.csv",buffer.getvalue())
    manifest={"rules":VERSION,"input":input_path.name,
              "source_archive_sha256":hashlib.sha256(input_path.read_bytes()).hexdigest() if input_path.is_file() else None,
              "selected_skus":skus,"count":len(chosen),"statuses":dict(sorted(counts.items())),
              "profile_counts":dict(sorted(profiles.items())),"read_only":True,
              "fresh_shopify_product_check_required_before_application":True,
              "external_filter_index_sync_not_verified":True}
    write_if_changed(output/"manifest.json",dump(manifest))
    report=["# Wiesbaden: eerste 50-kraans proef","",
            "Bron: datarun 19 oktober 2026. Runregels: "+VERSION+".","",
            f"Artikelen: {len(chosen)}. Nieuwe JSON: {generated}; identiek hergebruikt: {reused}.",
            "Geen Shopify-, theme- of VPS-writes.", "", "## Status"]
    report.extend("- "+k+": "+str(n) for k,n in sorted(counts.items()))
    report+=["","## Grenzen","Alle voorstellen zijn reviewdata. De 31 niet-geblokkeerde concepten zijn niet automatisch goedgekeurd.",
             "Bestaande 24.3710-proef en zes andere goedgekeurde artikelen blijven beschermd.",
             "Broncollecties, filters en bijlagen zijn niet onafhankelijk live gevalideerd.",
             "Vereist voor live mutatie: verse identiteit/readback, menselijke controle, rollback en bewezen externe indexroute."]
    write_if_changed(output/"PROEFRAPPORT.md","\n".join(report)+"\n")
    return {"products":len(chosen),"statuses":dict(counts),"generated":generated,"reused":reused,"output":str(output)}


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",required=True,type=Path)
    p.add_argument("--output",required=True,type=Path)
    p.add_argument("--limit",type=int,default=50)
    args=p.parse_args()
    print(dump(run(args.input,args.output,args.limit)))
