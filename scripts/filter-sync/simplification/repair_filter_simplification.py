#!/usr/bin/env python3
"""Guarded release of simplified BadkamerCity filters in the existing search worker.

The release builder embeds the two reviewed pure patch modules. This program
uses the deployed worker's existing complete staging, readback and activation
checks. It never edits Shopify product data or runs historical cleanup.
"""
from __future__ import annotations

import ast
import datetime as dt
import fcntl
import hashlib
import json
import os
from pathlib import Path
import signal
import stat
import subprocess
import sys
import tempfile
import threading
import time
import types

PATCH_SOURCES = {'worker': '"""Pure guarded worker patch for derived colors and paired tile formats."""\nimport ast\nimport hashlib\n\nBASE_WORKER_SHA256 = \'e5f3c4103266c3df1f03b855395d0d6c1711b7452a7626c91889cfc9b3ab280c\'\nPATCHED_WORKER_SHA256 = \'d12e717a88729bb98d2282425a2e5dbea93d08ae0d128010c31113ab90f5527f\'\nMARKER = \'# BC_FILTER_SIMPLIFICATION_WORKER_V1\'\nCOLOR_SOURCE = \'"""Derived color groups for filter documents. Never rewrites source specifications.\\n\\nUses only Python\\\'s standard library; compact catalog-free rules are embedded.\\nThe score labels describe the rule source; they are not numerical probabilities.\\n"""\\nfrom __future__ import annotations\\n\\nimport json\\nfrom pathlib import Path\\nimport re\\nimport unicodedata\\n\\nRULES = {\\\'taxonomy\\\': [\\\'Wit\\\',\\n              \\\'Zwart\\\',\\n              \\\'Grijs\\\',\\n              \\\'Beige\\\',\\n              \\\'Bruin\\\',\\n              \\\'Groen\\\',\\n              \\\'Blauw\\\',\\n              \\\'Geel\\\',\\n              \\\'Oranje\\\',\\n              \\\'Rood\\\',\\n              \\\'Roze\\\',\\n              \\\'Paars\\\',\\n              \\\'Goud\\\',\\n              \\\'Koper\\\',\\n              \\\'Brons\\\',\\n              \\\'Zilver\\\',\\n              \\\'Transparant\\\',\\n              \\\'Multicolor\\\'],\\n \\\'other\\\': \\\'Overige kleuren\\\',\\n \\\'patterns\\\': {\\\'Wit\\\': \\\'(?:^|[^a-z])(?:wit|white|blanc|blanco|bianco|weiss)(?=$|[^a-z])\\\',\\n              \\\'Zwart\\\': \\\'(?:^|[^a-z])(?:zwart|black|negro|nero|noir)(?=$|[^a-z])\\\',\\n              \\\'Grijs\\\': \\\'(?:^|[^a-z])(?:grijs|grey|gray|grigio|gris|griseo|grafietgrijs|anthracite|antraciet|antracita|antracite|grafito|graphite|graystone|cemento|cement|beton|cenere|ceniza|humo|fumo|smoke|smoked|fog|mist|marengo|pewter|plomb|gery|gunmetal|gun \\\'\\n                       \\\'metal)(?=$|[^a-z])\\\',\\n              \\\'Beige\\\': \\\'(?:^|[^a-z])(?:beige|creme|cream|crema|ivory|avorio|marfil|ecru|sand|sabbia|zand|arena|almond|amande|biscuit|bisquit|biscotti|cashmere|greige|grege|taupe|tortora|nude|linen|lino|panna|nata|crudo|sesamo|vainilla|vanilla)(?=$|[^a-z])\\\',\\n              \\\'Bruin\\\': \\\'(?:^|[^a-z])(?:bruin|brown|brun|marron|maronne|chocolate|chocolat|cocoa|cacao|moka|umber|umbra|cognac|caramel|caramelo|nocciola|noce|nogal|nuez|nut|walnut|wallnut|walnoot|avellana|tostado|tabacco|pardo|wengue|vison|camel|cafe|latte)(?=$|[^a-z])\\\',\\n              \\\'Groen\\\': \\\'(?:^|[^a-z])(?:groen|green|verde|vert|olive|olivo|sage|salvia|emerald|emeral|esmeralda|smeraldo|mint|menta|agave|avocado|avocat|basil|bottiglia|eucalyptus|fern|forest|foresta|ficus|evergreen|jade|kale|kiwi|leaf|matcha|moss|muschio|musgo|pistacho|verdino|khaki|kaqui)(?=$|[^a-z])\\\',\\n              \\\'Blauw\\\': \\\'(?:^|[^a-z])(?:blauw|blue|bleu|blu|azul|azzurro|azure|azur|cobalt|cobalto|indigo|navy|marine|marino|oltremare|ceruleo|celeste|cielo|denim|jeans|sapphire|saphir|sky|prusian|carta \\\'\\n                       \\\'da zucchero)(?=$|[^a-z])\\\',\\n              \\\'Geel\\\': \\\'(?:^|[^a-z])(?:geel|yellow|amarillo|giallo|mustard|mostaza|moutarde|senape|ocher|ochre|ocra|ocre|honey|miel|miele|lemonade|limon|buttercream|paja|amber|ambar)(?=$|[^a-z])\\\',\\n              \\\'Oranje\\\': \\\'(?:^|[^a-z])(?:oranje|orange|arancio|naranja|apricot|mango|papaya|tangerine|terracota|terracotta|terra \\\'\\n                        \\\'cotta|cotto|teja|rust|corten|sienna|siena)(?=$|[^a-z])\\\',\\n              \\\'Rood\\\': \\\'(?:^|[^a-z])(?:rood|red|rojo|rosso|rouge|bordeaux|bordeau|burdeos|burgundy|wine|borgogna|borgona|marsala|carmin|garnet|granate|ruby|cereza|cherry|frambuesa|mosto|rojizo)(?=$|[^a-z])\\\',\\n              \\\'Roze\\\': \\\'(?:^|[^a-z])(?:roze|pink|rosa|rose|blush|cipria|fucsia|fuxia|malvarrosa|peach|pesca|pitaya|salmon|salmon \\\'\\n                      \\\'pink|rosantico|rosette)(?=$|[^a-z])\\\',\\n              \\\'Paars\\\': \\\'(?:^|[^a-z])(?:paars|purple|violeta|morado|lila|lavanda|malva|ametyst|glicine|parme|porpora|prugna)(?=$|[^a-z])\\\',\\n              \\\'Goud\\\': \\\'(?:^|[^a-z])(?:goud|gold|golden|oro|or|aurum|brass|messing)(?=$|[^a-z])\\\',\\n              \\\'Koper\\\': \\\'(?:^|[^a-z])(?:koper|copper|cuivre|cobre)(?=$|[^a-z])\\\',\\n              \\\'Brons\\\': \\\'(?:^|[^a-z])(?:brons|bronze|bronzo|bronce)(?=$|[^a-z])\\\',\\n              \\\'Zilver\\\': \\\'(?:^|[^a-z])(?:zilver|silver|chroom|chrome|rvs|nikkel|nickel|staal|steel|acero|acciaio|platinum|titanio)(?=$|[^a-z])\\\',\\n              \\\'Transparant\\\': \\\'(?:^|[^a-z])(?:transparant|transparent|clear|helder glas|cristal)(?=$|[^a-z])\\\'},\\n \\\'direct_patterns\\\': {\\\'Wit\\\': \\\'(?:^|[^a-z])(?:wit|white|blanc|blanco|bianco|weiss)(?=$|[^a-z])\\\',\\n                     \\\'Zwart\\\': \\\'(?:^|[^a-z])(?:zwart|black|negro|nero|noir)(?=$|[^a-z])\\\',\\n                     \\\'Grijs\\\': \\\'(?:^|[^a-z])(?:grijs|grey|gray|grigio|gris|griseo)(?=$|[^a-z])\\\',\\n                     \\\'Beige\\\': \\\'(?:^|[^a-z])(?:beige|creme|cream|crema)(?=$|[^a-z])\\\',\\n                     \\\'Bruin\\\': \\\'(?:^|[^a-z])(?:bruin|brown|brun|marron|maronne)(?=$|[^a-z])\\\',\\n                     \\\'Groen\\\': \\\'(?:^|[^a-z])(?:groen|green|verde|vert)(?=$|[^a-z])\\\',\\n                     \\\'Blauw\\\': \\\'(?:^|[^a-z])(?:blauw|blue|bleu|blu|azul|azzurro|azure|azur)(?=$|[^a-z])\\\',\\n                     \\\'Geel\\\': \\\'(?:^|[^a-z])(?:geel|yellow|amarillo|giallo)(?=$|[^a-z])\\\',\\n                     \\\'Oranje\\\': \\\'(?:^|[^a-z])(?:oranje|orange|arancio|naranja)(?=$|[^a-z])\\\',\\n                     \\\'Rood\\\': \\\'(?:^|[^a-z])(?:rood|red|rojo|rosso|rouge)(?=$|[^a-z])\\\',\\n                     \\\'Roze\\\': \\\'(?:^|[^a-z])(?:roze|pink|rosa|rose)(?=$|[^a-z])\\\',\\n                     \\\'Paars\\\': \\\'(?:^|[^a-z])(?:paars|purple|violeta|morado|lila)(?=$|[^a-z])\\\',\\n                     \\\'Goud\\\': \\\'(?:^|[^a-z])(?:goud|gold|golden|oro|or|aurum)(?=$|[^a-z])\\\',\\n                     \\\'Koper\\\': \\\'(?:^|[^a-z])(?:koper|copper|cuivre|cobre)(?=$|[^a-z])\\\',\\n                     \\\'Brons\\\': \\\'(?:^|[^a-z])(?:brons|bronze|bronzo|bronce)(?=$|[^a-z])\\\',\\n                     \\\'Zilver\\\': \\\'(?:^|[^a-z])(?:zilver|silver|chroom|chrome|rvs|nikkel|nickel|staal|steel|acero|acciaio)(?=$|[^a-z])\\\',\\n                     \\\'Transparant\\\': \\\'(?:^|[^a-z])(?:transparant|transparent|clear)(?=$|[^a-z])\\\'},\\n \\\'no_color\\\': [\\\'\\\',\\n              \\\'none\\\',\\n              \\\'null\\\',\\n              \\\'r\\\',\\n              \\\'brillo\\\',\\n              \\\'mate\\\',\\n              \\\'mat\\\',\\n              \\\'matt\\\',\\n              \\\'craquele\\\',\\n              \\\'metal\\\',\\n              \\\'metalizado\\\',\\n              \\\'hout\\\',\\n              \\\'eik\\\',\\n              \\\'eiken\\\',\\n              \\\'oak\\\',\\n              \\\'natuursteen\\\',\\n              \\\'steen\\\',\\n              \\\'stone\\\',\\n              \\\'natural\\\',\\n              \\\'natural oak\\\',\\n              \\\'natual oak\\\',\\n              \\\'naturel eik\\\',\\n              \\\'licht eiken\\\',\\n              \\\'donker eiken\\\',\\n              \\\'warm eiken\\\',\\n              \\\'\u2013 (tegelrooster)\\\'],\\n \\\'finish_pattern\\\': \\\'(?:\\\\\\\\b(?:mat|matt|matte|mate|glans|glanzend|gloss|glossy|brillo|lucido|geborsteld|brushed|gepolijst|polished|pvd|satin|satijn|anticato|craquele)\\\\\\\\b)\\\',\\n \\\'conventional\\\': {\\\'snow\\\': [\\\'Wit\\\'],\\n                  \\\'neve\\\': [\\\'Wit\\\'],\\n                  \\\'nieve\\\': [\\\'Wit\\\'],\\n                  \\\'milk\\\': [\\\'Wit\\\'],\\n                  \\\'milkwhite\\\': [\\\'Wit\\\'],\\n                  \\\'cotton\\\': [\\\'Wit\\\'],\\n                  \\\'gesso\\\': [\\\'Wit\\\'],\\n                  \\\'alabaster\\\': [\\\'Wit\\\'],\\n                  \\\'albatre\\\': [\\\'Wit\\\'],\\n                  \\\'nube\\\': [\\\'Wit\\\'],\\n                  \\\'cloud\\\': [\\\'Wit\\\'],\\n                  \\\'rice\\\': [\\\'Wit\\\'],\\n                  \\\'sugar\\\': [\\\'Wit\\\'],\\n                  \\\'swan\\\': [\\\'Wit\\\'],\\n                  \\\'carbon\\\': [\\\'Zwart\\\'],\\n                  \\\'carbone\\\': [\\\'Zwart\\\'],\\n                  \\\'charbon\\\': [\\\'Zwart\\\'],\\n                  \\\'ebony\\\': [\\\'Zwart\\\'],\\n                  \\\'kohl\\\': [\\\'Zwart\\\'],\\n                  \\\'lavagna\\\': [\\\'Zwart\\\'],\\n                  \\\'midnight\\\': [\\\'Zwart\\\'],\\n                  \\\'night\\\': [\\\'Zwart\\\'],\\n                  \\\'basalt\\\': [\\\'Grijs\\\'],\\n                  \\\'basalto\\\': [\\\'Grijs\\\'],\\n                  \\\'iron\\\': [\\\'Grijs\\\'],\\n                  \\\'ferro\\\': [\\\'Grijs\\\'],\\n                  \\\'bardiglio\\\': [\\\'Grijs\\\'],\\n                  \\\'crudo\\\': [\\\'Beige\\\'],\\n                  \\\'coquille\\\': [\\\'Beige\\\'],\\n                  \\\'fango\\\': [\\\'Beige\\\'],\\n                  \\\'bamboo\\\': [\\\'Beige\\\'],\\n                  \\\'cafe latte\\\': [\\\'Beige\\\'],\\n                  \\\'macchiato\\\': [\\\'Bruin\\\'],\\n                  \\\'frappe\\\': [\\\'Beige\\\'],\\n                  \\\'aqua\\\': [\\\'Blauw\\\', \\\'Groen\\\'],\\n                  \\\'acqua\\\': [\\\'Blauw\\\', \\\'Groen\\\'],\\n                  \\\'agua\\\': [\\\'Blauw\\\', \\\'Groen\\\'],\\n                  \\\'aquamarina\\\': [\\\'Blauw\\\', \\\'Groen\\\'],\\n                  \\\'acquamarina\\\': [\\\'Blauw\\\', \\\'Groen\\\'],\\n                  \\\'agua marina\\\': [\\\'Blauw\\\', \\\'Groen\\\'],\\n                  \\\'cyan\\\': [\\\'Blauw\\\', \\\'Groen\\\'],\\n                  \\\'cyaan\\\': [\\\'Blauw\\\', \\\'Groen\\\'],\\n                  \\\'turquoise\\\': [\\\'Blauw\\\', \\\'Groen\\\'],\\n                  \\\'turqoise\\\': [\\\'Blauw\\\', \\\'Groen\\\'],\\n                  \\\'turques\\\': [\\\'Blauw\\\', \\\'Groen\\\'],\\n                  \\\'turquesa\\\': [\\\'Blauw\\\', \\\'Groen\\\'],\\n                  \\\'turchese\\\': [\\\'Blauw\\\', \\\'Groen\\\'],\\n                  \\\'teal\\\': [\\\'Blauw\\\', \\\'Groen\\\'],\\n                  \\\'petrol\\\': [\\\'Blauw\\\', \\\'Groen\\\'],\\n                  \\\'petrolio\\\': [\\\'Blauw\\\', \\\'Groen\\\'],\\n                  \\\'ottanio\\\': [\\\'Blauw\\\', \\\'Groen\\\'],\\n                  \\\'verdeacqua\\\': [\\\'Groen\\\', \\\'Blauw\\\'],\\n                  \\\'ocean\\\': [\\\'Blauw\\\'],\\n                  \\\'oceano\\\': [\\\'Blauw\\\'],\\n                  \\\'oceanum\\\': [\\\'Blauw\\\'],\\n                  \\\'deep ocean\\\': [\\\'Blauw\\\'],\\n                  \\\'deep sea\\\': [\\\'Blauw\\\'],\\n                  \\\'mar\\\': [\\\'Blauw\\\'],\\n                  \\\'lagoon\\\': [\\\'Blauw\\\', \\\'Groen\\\'],\\n                  \\\'laguna\\\': [\\\'Blauw\\\', \\\'Groen\\\'],\\n                  \\\'lake\\\': [\\\'Blauw\\\'],\\n                  \\\'seafoam\\\': [\\\'Groen\\\'],\\n                  \\\'coral\\\': [\\\'Roze\\\', \\\'Oranje\\\']},\\n \\\'owner_rules\\\': [[\\\'Porcelanosa\\\', \\\'Saddle\\\', \\\'Caliza\\\', [\\\'Beige\\\'], \\\'Beige\\\'],\\n                 [\\\'Cottoceramix\\\', \\\'Malaga\\\', \\\'Bone\\\', [\\\'Wit\\\'], \\\'Wit\\\'],\\n                 [\\\'Cottoceramix\\\', \\\'Etnia\\\', \\\'Marfil\\\', [\\\'Beige\\\'], \\\'Beige\\\'],\\n                 [\\\'Cottoceramix\\\', \\\'Portofino\\\', \\\'Grafito\\\', [\\\'Grijs\\\'], \\\'Grijs\\\'],\\n                 [\\\'Cottoceramix\\\', \\\'Malaga\\\', \\\'Acero\\\', [\\\'Grijs\\\'], \\\'Grijs\\\'],\\n                 [\\\'Porcelanosa\\\', \\\'Saddle\\\', \\\'Topo\\\', [\\\'Beige\\\'], \\\'Beige\\\'],\\n                 [\\\'Cottoceramix\\\', \\\'Souk\\\', \\\'Pearl\\\', [\\\'Wit\\\'], \\\'Wit\\\'],\\n                 [\\\'Cottoceramix\\\', \\\'Sweet Bars\\\', \\\'Greige\\\', [\\\'Beige\\\'], \\\'Beige\\\'],\\n                 [\\\'Cottoceramix\\\', \\\'Souk\\\', \\\'Aqua\\\', [\\\'Groen\\\'], \\\'Groen\\\'],\\n                 [\\\'Cottoceramix\\\', \\\'Waves\\\', \\\'Copper Green\\\', [\\\'Groen\\\'], \\\'Groen\\\'],\\n                 [\\\'Cottoceramix\\\', \\\'Himalayas\\\', \\\'Everest\\\', [\\\'Wit\\\', \\\'Beige\\\'], \\\'Wit\\\'],\\n                 [\\\'Cottoceramix\\\', \\\'Strand\\\', \\\'Natural\\\', [\\\'Beige\\\', \\\'Bruin\\\'], \\\'Beige\\\'],\\n                 [\\\'Cottoceramix\\\', \\\'Marmorea\\\', \\\'Carrara\\\', [\\\'Wit\\\', \\\'Grijs\\\'], \\\'Wit\\\'],\\n                 [\\\'Cottoceramix\\\', \\\'Marmorea\\\', \\\'Nero Marquina\\\', [\\\'Zwart\\\'], \\\'Zwart\\\'],\\n                 [\\\'Cottoceramix\\\', \\\'Marmorea\\\', \\\'Botticino\\\', [\\\'Beige\\\'], \\\'Beige\\\']]}\\nTAXONOMY = tuple(RULES[\\\'taxonomy\\\'])\\nOTHER = RULES[\\\'other\\\']\\nOWNER_RULES = RULES[\\\'owner_rules\\\']\\nPATTERNS = {k: re.compile(v, re.I) for k, v in RULES[\\\'patterns\\\'].items()}\\nDIRECT = {k: re.compile(v, re.I) for k, v in RULES[\\\'direct_patterns\\\'].items()}\\nFINISH = re.compile(RULES[\\\'finish_pattern\\\'])\\nNO_COLOR = set(RULES[\\\'no_color\\\'])\\nCONVENTIONAL = RULES[\\\'conventional\\\']\\n\\n\\ndef normalize(value):\\n    value = \\\'\\\' if value is None else str(value)\\n    value = unicodedata.normalize(\\\'NFKD\\\', value)\\n    value = \\\'\\\'.join(c for c in value if not \\\'\\\\u0300\\\' <= c <= \\\'\\\\u036f\\\')\\n    return re.sub(r\\\'\\\\s+\\\', \\\' \\\', value.lower().replace(\\\'\u2019\\\', "\\\'").replace(\\\'\u2018\\\', "\\\'")).strip()\\n\\n\\ndef normalize_series(value):\\n    return re.sub(r\\\'\\\\s+\\\', \\\' \\\', re.sub(r\\\'-r\\\\b\\\', \\\'\\\', normalize(value))).strip()\\n\\n\\ndef _result(raw, colors, confidence, reason, primary=None):\\n    selected = list(dict.fromkeys(colors))\\n    return {\\\'raw\\\': \\\'\\\' if raw is None else str(raw), \\\'colors\\\': selected,\\n            \\\'primary\\\': primary or (selected[0] if selected else None),\\n            \\\'confidence\\\': confidence, \\\'reason\\\': reason}\\n\\n\\ndef classify_color(raw, context=None):\\n    ctx = context or {}\\n    s = normalize(raw)\\n    vendor = normalize(ctx.get(\\\'vendor\\\') or ctx.get(\\\'store_vendor\\\'))\\n    series = normalize_series(ctx.get(\\\'series\\\'))\\n    for v, sr, exact, colors, primary in OWNER_RULES:\\n        if vendor == normalize(v) and series == normalize_series(sr) and s == normalize(exact):\\n            return _result(raw, colors, \\\'OWNER_CONFIRMED\\\', \\\'Owner-approved exact vendor/series/color rule.\\\', primary)\\n    if vendor == \\\'porcelanosa\\\' and s == \\\'caliza\\\':\\n        return _result(raw, [\\\'Beige\\\'], \\\'OWNER_CONFIRMED\\\', \\\'Owner-approved Porcelanosa exact Caliza rule.\\\')\\n    if s in NO_COLOR:\\n        return _result(raw, [], \\\'UNRESOLVED\\\', \\\'No specific color or context-dependent material/trade name.\\\')\\n\\n    if \\\'/\\\' in s and not re.match(r\\\'^c/c\\\\b\\\', s):\\n        components = [classify_color(part, ctx) for part in s.split(\\\'/\\\')]\\n        colors = list(dict.fromkeys(c for part in components for c in part[\\\'colors\\\']))\\n        if colors:\\n            return _result(raw, colors, \\\'INFERRED\\\', \\\'Separate named finish/color components; match each visible color using OR.\\\')\\n\\n    if re.search(r\\\'(?:\\\\b)(?:rose gold|roze goud|pink gold)(?:\\\\b|$)\\\', s):\\n        return _result(raw, [\\\'Goud\\\'], \\\'INFERRED\\\', \\\'Rose gold grouped with gold; exact finish retained.\\\')\\n    if re.search(r\\\'zwart chroom|black chrome|gun\\\\s?metal black\\\', s):\\n        return _result(raw, [\\\'Zwart\\\'], \\\'INFERRED\\\', \\\'Explicit dark metallic finish grouped as black.\\\')\\n    if re.search(r\\\'verouderd messing|antique brass|aged brass\\\', s) and \\\'/\\\' not in s:\\n        return _result(raw, [\\\'Brons\\\'], \\\'INFERRED\\\', \\\'Aged brass grouped with bronze; exact finish retained.\\\')\\n    if re.search(r\\\'gun\\\\s?metal|verouderd ijzer|dark steel\\\', s) and \\\'/\\\' not in s:\\n        return _result(raw, [\\\'Grijs\\\'], \\\'INFERRED\\\', \\\'Dark metallic finish grouped with gray.\\\')\\n    if s in (\\\'copper green\\\', \\\'verde cobre\\\'):\\n        return _result(raw, [\\\'Groen\\\'], \\\'INFERRED\\\', \\\'Green is the named visible patina family, not bare copper.\\\')\\n    if re.match(r\\\'^(?:off white|off-white|blanc de lin)(?:\\\\b|$)\\\', s):\\n        return _result(raw, [\\\'Beige\\\'], \\\'INFERRED\\\', \\\'Warm off-white grouped with beige.\\\')\\n\\n    explicit_colors = [group for group, pattern in DIRECT.items() if pattern.search(s)]\\n    colors = [group for group, pattern in PATTERNS.items() if pattern.search(s)]\\n    if explicit_colors and len(colors) > len(explicit_colors) and not re.search(r\\\'[/+]|\\\\band\\\\b|\\\\bwith\\\\b|speckle\\\', s):\\n        genuine_shade_combo = re.search(r\\\'(?:blue[- ]grey|grey[- ]blue|green grey|gris taupe|bianco petrolio|nero petrolio)\\\', s)\\n        if not genuine_shade_combo:\\n            return _result(raw, explicit_colors, \\\'DIRECT\\\', \\\'Explicit base color/translation; descriptive finish or shade retained on product.\\\')\\n    if colors:\\n        return _result(raw, colors, \\\'DIRECT\\\' if len(explicit_colors) == len(colors) else \\\'INFERRED\\\',\\n                       \\\'Multiple named color families; eligible for each family using OR matching.\\\' if len(colors) > 1 else\\n                       \\\'Recognizable color or conventional shade; exact manufacturer name retained.\\\')\\n    plain = re.sub(r\\\'\\\\s+\\\', \\\' \\\', FINISH.sub(\\\' \\\', s)).strip()\\n    if plain in CONVENTIONAL:\\n        return _result(raw, CONVENTIONAL[plain], \\\'INFERRED\\\', \\\'Conventional shade; boundary shades may appear in both relevant base colors.\\\')\\n    if re.search(r\\\'multicolor|multi color|contrast mix|tutti frutti\\\', s) or s == \\\'mix\\\':\\n        return _result(raw, [\\\'Multicolor\\\'], \\\'DIRECT\\\', \\\'Explicit mixed-color designation without reliable separate named colors.\\\')\\n    return _result(raw, [], \\\'UNRESOLVED\\\', \\\'Opaque trade/color name: keep under Other colors until product context is available.\\\')\\n\\n\\ndef _strings(value):\\n    if isinstance(value, str):\\n        return [value] if value.strip() else []\\n    if isinstance(value, (list, tuple)):\\n        return [v for v in value if isinstance(v, str) and v.strip()]\\n    return []\\n\\n\\ndef _document_context(doc):\\n    """Resolve only a known reviewed series from title when f_serie is absent.\\n\\n    This is deliberately not a generic color extraction from arbitrary title text.\\n    Vendor equality and exact f_kleur equality are still required by owner rules.\\n    """\\n    vendor = next(iter(_strings(doc.get(\\\'vendor\\\'))), \\\'\\\')\\n    series_values = _strings(doc.get(\\\'f_serie\\\')) or _strings(doc.get(\\\'series\\\'))\\n    if not series_values:\\n        title = normalize(doc.get(\\\'title\\\'))\\n        for rule_vendor, rule_series, _raw, _colors, _primary in OWNER_RULES:\\n            if normalize(vendor) != normalize(rule_vendor):\\n                continue\\n            term = normalize_series(rule_series)\\n            if re.search(r\\\'(?<![a-z0-9])\\\' + re.escape(term) + r\\\'(?:-r)?(?![a-z0-9])\\\', title):\\n                series_values.append(rule_series)\\n    # Do not turn an ambiguous title containing multiple known series into a scoped rule.\\n    series_values = list(dict.fromkeys(series_values))\\n    return [{\\\'vendor\\\': vendor, \\\'series\\\': s} for s in series_values] if len(series_values) == 1 else [{\\\'vendor\\\': vendor}]\\n\\n\\ndef normalize_document_colors(doc, *, include_other=True):\\n    """Return derived string[] from f_kleur, without modifying doc or any source field.\\n\\n    No color data returns []. A nonempty unresolved manufacturer name becomes the\\n    single optional fallback group, so unknown names do not create hundreds of UI\\n    choices. Set include_other=False to omit unresolved source names from facets.\\n    """\\n    raw_values = _strings(doc.get(\\\'f_kleur\\\'))\\n    contexts = _document_context(doc)\\n    colors = []\\n    for raw in raw_values:\\n        matches = [classify_color(raw, ctx) for ctx in contexts]\\n        found = list(dict.fromkeys(color for match in matches for color in match[\\\'colors\\\']))\\n        if found:\\n            colors.extend(found)\\n        elif include_other:\\n            colors.append(OTHER)\\n    selected = set(colors)\\n    return [color for color in (*TAXONOMY, OTHER) if color in selected]\\n\\n\'\nRUNTIME_SOURCE = \'"""Embedded derived filter behavior; source product fields remain intact."""\\nimport decimal as _bc_simple_decimal\\nimport re as _bc_simple_re\\n\\n_BC_SIMPLE_VERSION = \\\'bc-filter-simple-v2-exact-format-codes\\\'\\n_BC_SIMPLE_TARGETS = ((50,50),(50,200),(50,250),(50,300),(65,200),(75,150),(75,300),\\n (100,100),(100,200),(100,300),(112.5,450),(125,250),(130,130),(150,150),(150,300),\\n (160,160),(200,200),(200,400),(200,600),(200,1200),(250,250),(250,400),(250,500),\\n (300,300),(300,600),(300,900),(300,1200),(330,330),(333,333),(335,335),(400,400),\\n (400,800),(450,450),(500,500),(600,600),(600,1200),(750,750),(800,800),(800,1600),\\n (900,900),(1000,1000),(1200,1200),(1200,1800),(1200,2000))\\n_BC_SIMPLE_SPECIAL = _bc_simple_re.compile(r\\\'\\\\b(?:hexagon\\\\w*|hexa|octogon\\\\w*|octagon\\\\w*|escama|scale|zeshoek\\\\w*|round|rond|ronde|circular|circle|arabesque|fishscale|fish scale|rhomb\\\\w*|diamond|picket)\\\\b|moza[i\xef]e?k|mosaic|sheet|tegelmat|visgraatmat\\\', _bc_simple_re.I)\\n\\ndef _bc_simple_strings(value):\\n    if isinstance(value, str):\\n        return [value] if value.strip() else []\\n    return [v for v in value if isinstance(v, str) and v.strip()] if isinstance(value, (list, tuple)) else []\\n\\ndef _bc_simple_flat(value):\\n    return list(value) if isinstance(value, (list, tuple)) else [value]\\n\\ndef _bc_simple_tile_label(doc):\\n    """Use an actual typed pair, never independent facet cross-products."""\\n    D = _bc_simple_decimal.Decimal\\n    raw = []\\n    for key in (\\\'f_tegel_breedte_mm\\\', \\\'f_tegel_lengte_mm\\\'):\\n        value = doc.get(key)\\n        if isinstance(value, bool) or value is None:\\n            return None\\n        try:\\n            number = D(str(value))\\n        except _bc_simple_decimal.InvalidOperation:\\n            return None\\n        if not number.is_finite() or number <= 0:\\n            return None\\n        raw.append(number)\\n    raw.sort()\\n    result = tuple(raw)\\n    text = \\\' \\\'.join(str(doc.get(key) or \\\'\\\') for key in (\\\'title\\\', \\\'product_type\\\', \\\'f_productsoort\\\'))\\n    if not _BC_SIMPLE_SPECIAL.search(text):\\n        targets = [tuple(D(str(n)) for n in pair) for pair in _BC_SIMPLE_TARGETS]\\n        if result not in targets:\\n            fits = [p for p in targets if all(abs(a-b) <= D(\\\'8\\\') and abs(a-b) <= b*D(\\\'.03\\\') for a,b in zip(result,p))]\\n            scored = sorted((sum(abs(a-b) for a,b in zip(result,p)), p) for p in fits)\\n            if scored and (len(scored) == 1 or scored[0][0] < scored[1][0]):\\n                result = scored[0][1]\\n            elif D(\\\'596\\\') in result:\\n                result = tuple(D(\\\'600\\\') if n == D(\\\'596\\\') else n for n in result)\\n    show = lambda n: format((n/D(\\\'10\\\')).normalize(), \\\'f\\\').replace(\\\'.\\\', \\\',\\\')\\n    return \\\' \xd7 \\\'.join(show(n) for n in result) + \\\' cm\\\'\\n\\ndef _bc_simple_schema(schema):\\n    result = copy.deepcopy(schema)\\n    fields = {f[\\\'name\\\']: f for f in result[\\\'fields\\\']}\\n    if \\\'f_kleur\\\' not in fields:\\n        raise RuntimeError(\\\'Bestaand kleurindexveld ontbreekt\\\')\\n    fields[\\\'f_kleur\\\'][\\\'type\\\'] = \\\'string[]\\\'\\n    fields[\\\'f_kleur\\\'][\\\'facet\\\'] = True\\n    for name, kind, facet in [(\\\'f_kleur_exact\\\', \\\'string\\\', False), (\\\'f_tegel_formaat\\\', \\\'string\\\', True),\\n                              (\\\'f_tegel_formaat_code\\\', \\\'int32\\\', False)]:\\n        if name in fields and (fields[name].get(\\\'type\\\') != kind or bool(fields[name].get(\\\'facet\\\')) != facet):\\n            raise RuntimeError(\\\'Nieuw filterveld bestaat met afwijkend type: \\\' + name)\\n        if name not in fields:\\n            result[\\\'fields\\\'].append({\\\'name\\\': name, \\\'type\\\': kind, \\\'facet\\\': facet, \\\'optional\\\': True})\\n    return result\\n\\ndef _bc_simple_tile_code_map(docs):\\n    """Generation-local codes keep formatted text out of exact selection clauses."""\\n    labels = {d[\\\'f_tegel_formaat\\\'] for d in docs if d.get(\\\'f_tegel_formaat\\\')}\\n    if len(labels) >= 2**31 or any(not isinstance(label, str) for label in labels):\\n        raise RuntimeError(\\\'Onverwacht groot of ongeldig formaatregister\\\')\\n    labels = sorted(labels)\\n    return {label: position for position, label in enumerate(labels, 1)}\\n\\ndef _bc_simple_check_tile_codes(docs, codes):\\n    if (codes != _bc_simple_tile_code_map(docs) or\\n            len(codes) != len(set(codes.values())) or\\n            any(type(value) is not int or value <= 0 for value in codes.values())):\\n        return False\\n    return all((type(d.get(\\\'f_tegel_formaat_code\\\')) is int and\\n                d.get(\\\'f_tegel_formaat_code\\\') == codes[d[\\\'f_tegel_formaat\\\']]\\n                if d.get(\\\'f_tegel_formaat\\\') else \\\'f_tegel_formaat_code\\\' not in d)\\n               for d in docs)\\n\\ndef _bc_simple_definitions(definitions):\\n    result = copy.deepcopy(definitions)\\n    if any(d[\\\'field\\\'] == \\\'f_tegel_formaat\\\' for d in result):\\n        raise RuntimeError(\\\'Afgeleid formaatveld staat onverwacht in brondefinities\\\')\\n    result.append({\\\'key\\\': \\\'tegel_formaat_nominaal\\\', \\\'field\\\': \\\'f_tegel_formaat\\\',\\n                   \\\'label\\\': \\\'Tegelformaat\\\', \\\'type\\\': \\\'choice\\\', \\\'data_type\\\': \\\'string\\\'})\\n    return result\\n\\n_bc_simple_original_enrich = enrich_b2c_documents\\ndef enrich_b2c_documents(docs, definitions, schema):\\n    original = {d[\\\'id\\\']: copy.deepcopy(d.get(\\\'f_kleur\\\')) for d in docs}\\n    stats = _bc_simple_original_enrich(docs, definitions, schema)\\n    counts = collections.Counter()\\n    for doc in docs:\\n        raw = original[doc[\\\'id\\\']]\\n        values = _bc_simple_strings(raw)\\n        if values:\\n            if len(values) != 1:\\n                raise RuntimeError(\\\'Onverwacht meervoudige exacte bronkleur\\\')\\n            doc[\\\'f_kleur_exact\\\'] = values[0]\\n            color_doc = {**doc, \\\'f_kleur\\\': raw}\\n            doc[\\\'f_kleur\\\'] = _BC_SIMPLE_COLORS[\\\'normalize_document_colors\\\'](color_doc)\\n            counts[\\\'simple_color_products\\\'] += 1\\n            counts[\\\'simple_multiple_color_products\\\'] += int(len(doc[\\\'f_kleur\\\']) > 1)\\n            counts[\\\'simple_unresolved_color_products\\\'] += int(\\\'Overige kleuren\\\' in doc[\\\'f_kleur\\\'])\\n        else:\\n            doc.pop(\\\'f_kleur\\\', None)\\n        label = _bc_simple_tile_label(doc)\\n        if label is not None:\\n            doc[\\\'f_tegel_formaat\\\'] = label\\n            counts[\\\'simple_tile_format_products\\\'] += 1\\n        else:\\n            doc.pop(\\\'f_tegel_formaat\\\', None)\\n    codes = _bc_simple_tile_code_map(docs)\\n    for doc in docs:\\n        label = doc.get(\\\'f_tegel_formaat\\\')\\n        if label:\\n            doc[\\\'f_tegel_formaat_code\\\'] = codes[label]\\n        else:\\n            doc.pop(\\\'f_tegel_formaat_code\\\', None)\\n    if not _bc_simple_check_tile_codes(docs, codes):\\n        raise RuntimeError(\\\'Formaatregister en productcodes komen niet overeen\\\')\\n    counts[\\\'simple_tile_format_codes\\\'] = len(codes)\\n    stats.update(dict(counts))\\n    return stats\\n\\n_bc_simple_original_finite = finite_value\\ndef finite_value(value):\\n    return bool(value) and all(_bc_simple_original_finite(v) for v in value) if isinstance(value, (list, tuple)) else _bc_simple_original_finite(value)\\n\\ndef distinct_values(values):\\n    flat = (v for value in values for v in _bc_simple_flat(value))\\n    return list({(type(v).__name__, str(v)): v for v in flat}.values())\\n\\ndef color_groups_for(docs):\\n    colors = sorted({color for d in docs for color in _bc_simple_strings(d.get(\\\'f_kleur\\\'))}, key=str.casefold)\\n    return {\\\'groups\\\': [{\\\'label\\\': color, \\\'exact_values\\\': [color]} for color in colors],\\n            \\\'ungrouped_exact_values\\\': [], \\\'selection\\\': \\\'or_exact_values\\\'}\\n\\n_bc_simple_original_ui = filter_ui\\ndef filter_ui(field, definition, group, values, section, opened):\\n    ui = _bc_simple_original_ui(field, definition, group, values, section, opened)\\n    aliases = _BC_SIMPLE_ENUM_ALIASES.get(field)\\n    if aliases and definition.get(\\\'data_type\\\') == \\\'string\\\':\\n        grouped = collections.defaultdict(list)\\n        for value in values:\\n            if not isinstance(value, str):\\n                raise RuntimeError(\\\'Gegroepeerd keuzefilter heeft onverwacht niet-tekstueel bronveld\\\')\\n            key = \\\' \\\'.join(value.split()).casefold()\\n            label = aliases.get(key, TYPE_LABELS.get(value, value) if field == \\\'f_productsoort\\\' else value)\\n            grouped[label].append(value)\\n        ui[\\\'option_groups\\\'] = [{\\\'label\\\':label,\\\'exact_values\\\':sorted(set(raw),key=str.casefold)} for label,raw in sorted(grouped.items(),key=lambda kv:kv[0].casefold())]\\n        ui[\\\'request_mode\\\'] = \\\'or_exact_values\\\'\\n    return ui\\n\\ndef _bc_simple_aliases(docs):\\n    candidates = collections.defaultdict(set)\\n    for d in docs:\\n        raw = d.get(\\\'f_kleur_exact\\\')\\n        colors = _bc_simple_strings(d.get(\\\'f_kleur\\\'))\\n        if raw and colors:\\n            candidates[raw].add(colors[0])\\n            # Older requests pass through the existing RVS middleware first.\\n            candidates[canonical_color(raw)].add(colors[0])\\n    output = {}\\n    for raw, values in candidates.items():\\n        result = _BC_SIMPLE_COLORS[\\\'classify_color\\\'](raw, {})\\n        output[raw] = next(iter(values)) if len(values) == 1 else (result.get(\\\'primary\\\') or \\\'Overige kleuren\\\')\\n    for value in (*_BC_SIMPLE_COLORS[\\\'TAXONOMY\\\'], _BC_SIMPLE_COLORS[\\\'OTHER\\\']):\\n        output[value] = value\\n    for value in (\\\'RVS\\\', \\\'RVS geborsteld\\\', \\\'Geborsteld RVS\\\', \\\'Geborsteld RVS PVD\\\'):\\n        output[value] = \\\'Zilver\\\'\\n    return output\\n\\n_bc_simple_original_profiles = make_profiles\\ndef make_profiles(docs, categories, old_profiles, definitions):\\n    profiles = _bc_simple_original_profiles(docs, categories, old_profiles, definitions)\\n    aliases = _bc_simple_aliases(docs)\\n    identities = set((*_BC_SIMPLE_COLORS[\\\'TAXONOMY\\\'], _BC_SIMPLE_COLORS[\\\'OTHER\\\'], \\\'RVS\\\', \\\'RVS geborsteld\\\', \\\'Geborsteld RVS\\\', \\\'Geborsteld RVS PVD\\\'))\\n    for handle, profile in profiles.items():\\n        relevant = identities | {raw for d in docs if handle == \\\'__all__\\\' or handle in d[\\\'collection_handles\\\'] for raw in (d.get(\\\'f_kleur_exact\\\'), canonical_color(d.get(\\\'f_kleur_exact\\\'))) if raw}\\n        profile[\\\'b2c_policy\\\'][\\\'color_value_aliases\\\'] = {k:v for k,v in aliases.items() if k in relevant}\\n        profile[\\\'b2c_policy\\\'][\\\'filter_simplification_v1\\\'] = True\\n    return profiles\\n\\ndef _bc_simple_snapshot(snapshot, docs):\\n    snapshot[\\\'filter_simplification_v1\\\'] = True\\n    snapshot[\\\'tile_format_codes_v1\\\'] = True\\n    snapshot[\\\'tile_format_codes\\\'] = _bc_simple_tile_code_map(docs)\\n    if not _bc_simple_check_tile_codes(docs, snapshot[\\\'tile_format_codes\\\']):\\n        raise RuntimeError(\\\'Generatie mist correcte exacte formaatcodes\\\')\\n    snapshot[\\\'filter_color_aliases\\\'] = _bc_simple_aliases(docs)\\n    counts = collections.Counter(color for d in docs if d[\\\'general_shopping\\\'] for color in set(_bc_simple_strings(d.get(\\\'f_kleur\\\'))))\\n    snapshot[\\\'simple_color_counts\\\'] = dict(counts)\\n    snapshot[\\\'simple_tile_counts\\\'] = dict(collections.Counter(d[\\\'f_tegel_formaat\\\'] for d in docs if d[\\\'general_shopping\\\'] and d.get(\\\'f_tegel_formaat\\\')))\\n\\ndef _bc_simple_body(snapshot, body):\\n    if not isinstance(body, dict) or not isinstance(body.get(\\\'filters\\\'), dict):\\n        return body\\n    values = body[\\\'filters\\\'].get(\\\'f_kleur\\\')\\n    if not isinstance(values, list) or not all(isinstance(v, str) for v in values):\\n        return body\\n    aliases = snapshot.get(\\\'filter_color_aliases\\\', {})\\n    mapped = list(dict.fromkeys(aliases.get(canonical_color(v), aliases.get(v, v)) for v in values))\\n    return {**body, \\\'filters\\\': {**body[\\\'filters\\\'], \\\'f_kleur\\\': mapped}}\\n\\ndef selected(docs, snapshot, body, exclude=None):\\n    body = _bc_simple_body(snapshot, body)\\n    handle = body.get(\\\'collection\\\', \\\'__all__\\\')\\n    profile = snapshot[\\\'profiles\\\'].get(handle)\\n    if profile is None:\\n        return []\\n    q = body.get(\\\'q\\\', \\\'*\\\').strip().casefold()\\n    exact = q in set(snapshot[\\\'exact\\\'])\\n    out = []\\n    for doc in docs:\\n        if handle != \\\'__all__\\\' and handle not in doc[\\\'collection_handles\\\']:\\n            continue\\n        if exact:\\n            if q not in (doc.get(\\\'sku_aliases\\\', []) if snapshot.get(\\\'variant_aliases_v1\\\') else [doc[\\\'sku_exact\\\']]):\\n                continue\\n        elif not profile[\\\'service_category\\\'] and not doc[\\\'general_shopping\\\']:\\n            continue\\n        if any(not any(value in choices for value in _bc_simple_flat(doc.get(field, UNKNOWN))) for field, choices in body.get(\\\'filters\\\', {}).items() if field != exclude):\\n            continue\\n        if any(field not in doc or (r.get(\\\'min\\\') is not None and doc[field] < r[\\\'min\\\']) or\\n               (r.get(\\\'max\\\') is not None and doc[field] > r[\\\'max\\\']) for field,r in body.get(\\\'ranges\\\', {}).items() if field != exclude):\\n            continue\\n        out.append(doc)\\n    return out\\n\\n_bc_simple_original_cases = make_cases\\ndef make_cases(docs, snapshot):\\n    cases, facets = _bc_simple_original_cases(docs, snapshot)\\n    for case in cases:\\n        case[\\\'name\\\'] = case[\\\'name\\\'].replace(\\\'Geborsteld RVS PVD blijft afzonderlijk\\\', \\\'Oude RVS PVD-link verwijst naar Zilver\\\')\\n    for case in facets:\\n        group = selected(docs, snapshot, case[\\\'body\\\'], exclude=case[\\\'field\\\'])\\n        case[\\\'expected_counts\\\'] = dict(collections.Counter(str(value) for d in group if case[\\\'field\\\'] in d for value in set(_bc_simple_flat(d[case[\\\'field\\\']]))))\\n    handles = [\\\'__all__\\\', \\\'tegels\\\'] + [h for h,p in snapshot[\\\'profiles\\\'].items() if h != \\\'tegels\\\' and p.get(\\\'b2c_policy\\\', {}).get(\\\'group\\\') == \\\'tile\\\'][:1]\\n    for handle in handles:\\n        profile = snapshot[\\\'profiles\\\'].get(handle)\\n        if not profile:\\n            continue\\n        visible = {f[\\\'field\\\'] for f in profile[\\\'filters\\\']}\\n        for field in (\\\'f_kleur\\\', \\\'f_tegel_formaat\\\'):\\n            if field not in visible:\\n                continue\\n            body = {\\\'collection\\\': handle, \\\'per_page\\\': 1}\\n            group = selected(docs, snapshot, body, exclude=field)\\n            expected = dict(collections.Counter(str(v) for d in group if field in d for v in set(_bc_simple_flat(d[field]))))\\n            facets.append({\\\'name\\\': \\\'Unieke afgeleide facet-aantallen: \\\' + handle + \\\'/\\\' + field, \\\'body\\\': body, \\\'field\\\': field, \\\'expected_counts\\\': expected})\\n            # Every distinct format is checked against its complete expected ID\\n            # set. The old first-three sample missed token-filter collisions.\\n            values_to_check = sorted(expected) if field == \\\'f_tegel_formaat\\\' else list(expected)[:3]\\n            for value in values_to_check:\\n                body = {\\\'collection\\\': handle, \\\'include_facets\\\': False, \\\'filters\\\': {field: [value]}}\\n                cases.append({\\\'name\\\': \\\'Afgeleide keuze: \\\' + handle + \\\'/\\\' + value, \\\'body\\\': body, \\\'status\\\': 200,\\n                              \\\'expected_ids\\\': [d[\\\'id\\\'] for d in selected(docs, snapshot, body)]})\\n        if \\\'f_tegel_formaat\\\' in visible:\\n            formats = [value for value in (\\\'60 \xd7 60 cm\\\', \\\'60 \xd7 120 cm\\\', \\\'60 \xd7 150 cm\\\')\\n                       if value in snapshot[\\\'tile_format_codes\\\']]\\n            if len(formats) > 1:\\n                body = {\\\'collection\\\': handle, \\\'include_facets\\\': False,\\n                        \\\'filters\\\': {\\\'f_tegel_formaat\\\': formats}}\\n                cases.append({\\\'name\\\': \\\'Exacte formaatcodes met OF-selectie: \\\' + handle,\\n                              \\\'body\\\': body, \\\'status\\\': 200,\\n                              \\\'expected_ids\\\': [d[\\\'id\\\'] for d in selected(docs, snapshot, body)]})\\n            if formats and \\\'f_kleur\\\' in visible:\\n                color = next((color for d in selected(docs, snapshot, {\\\'collection\\\':handle,\\n                                  \\\'filters\\\': {\\\'f_tegel_formaat\\\': [formats[0]]}})\\n                              for color in _bc_simple_strings(d.get(\\\'f_kleur\\\'))), None)\\n                if color:\\n                    body = {\\\'collection\\\': handle, \\\'include_facets\\\': False,\\n                            \\\'filters\\\': {\\\'f_tegel_formaat\\\': [formats[0]], \\\'f_kleur\\\': [color]}}\\n                    cases.append({\\\'name\\\': \\\'Exact formaat en basiskleur met EN-selectie: \\\' + handle,\\n                                  \\\'body\\\': body, \\\'status\\\': 200,\\n                                  \\\'expected_ids\\\': [d[\\\'id\\\'] for d in selected(docs, snapshot, body)]})\\n            body = {\\\'collection\\\': handle, \\\'include_facets\\\': False,\\n                    \\\'filters\\\': {\\\'f_tegel_formaat\\\': [\\\'__bc_unknown_format__\\\']}}\\n            cases.append({\\\'name\\\': \\\'Onbekend formaat geeft nul producten: \\\' + handle,\\n                          \\\'body\\\': body, \\\'status\\\': 200, \\\'expected_ids\\\': []})\\n    return cases, facets\\n\\ndef hot_checks(snapshot):\\n    checks = hot_checks_base(snapshot)\\n    for base, label in [(\\\'http://127.0.0.1:8082\\\', \\\'Lokale\\\'), (\\\'https://vps-7ffd625d.vps.ovh.net/verified\\\', \\\'Publieke\\\')]:\\n        handle = \\\'wastafelkranen\\\' if \\\'wastafelkranen\\\' in snapshot[\\\'profiles\\\'] else \\\'__all__\\\'\\n        expected = snapshot[\\\'profiles\\\'][handle]\\n        profile, _ = probe(base + \\\'/api/v1/profile/\\\' + handle)\\n        search, _ = probe(base + \\\'/api/v1/search\\\', {\\\'collection\\\': handle, \\\'per_page\\\': 1})\\n        good = (profile.get(\\\'filter_policy\\\') == expected[\\\'b2c_policy\\\'] and search.get(\\\'filter_policy\\\') == expected[\\\'b2c_policy\\\'] and [f[\\\'field\\\'] for f in profile.get(\\\'filters\\\', [])] == [f[\\\'field\\\'] for f in expected[\\\'filters\\\']])\\n        checks.append({\\\'name\\\': label + \\\' API gebruikt vereenvoudigd B2C-profiel\\\', \\\'passed\\\': good})\\n        for value in (\\\'Goud\\\', \\\'Groen\\\', \\\'Zilver\\\', \\\'RVS\\\', \\\'Geborsteld RVS PVD\\\'):\\n            data, _ = probe(base + \\\'/api/v1/search\\\', {\\\'collection\\\': \\\'__all__\\\', \\\'per_page\\\': 1, \\\'include_facets\\\': False, \\\'filters\\\': {\\\'f_kleur\\\': [value]}})\\n            expected_count = snapshot[\\\'simple_color_counts\\\'].get(snapshot[\\\'filter_color_aliases\\\'].get(value, value), 0)\\n            checks.append({\\\'name\\\': label + \\\' unieke basiskleurcontrole: \\\' + value, \\\'passed\\\': data.get(\\\'found\\\') == expected_count, \\\'expected_count\\\': expected_count, \\\'actual_count\\\': data.get(\\\'found\\\')})\\n        tile = next((h for h,p in snapshot[\\\'profiles\\\'].items() if p.get(\\\'b2c_policy\\\', {}).get(\\\'group\\\') == \\\'tile\\\' and h == \\\'tegels\\\'), None)\\n        if tile and snapshot[\\\'simple_tile_counts\\\']:\\n            values = [value for value in (\\\'60 \xd7 60 cm\\\', \\\'60 \xd7 120 cm\\\', \\\'60 \xd7 150 cm\\\')\\n                      if value in snapshot[\\\'simple_tile_counts\\\']]\\n            if not values:\\n                values = [next(iter(snapshot[\\\'simple_tile_counts\\\']))]\\n            for value in values:\\n                data, _ = probe(base + \\\'/api/v1/search\\\', {\\\'collection\\\': \\\'__all__\\\', \\\'per_page\\\': 1, \\\'include_facets\\\': False, \\\'filters\\\': {\\\'f_tegel_formaat\\\': [value]}})\\n                count = snapshot[\\\'simple_tile_counts\\\'][value]\\n                checks.append({\\\'name\\\': label + \\\' exacte formaatcode: \\\' + value, \\\'passed\\\': data.get(\\\'found\\\') == count, \\\'expected_count\\\': count, \\\'actual_count\\\': data.get(\\\'found\\\')})\\n        checks += _bc_variant_hot_check(snapshot, base, label)\\n    return checks\\n\\n_bc_simple_original_check_profiles = check_b2c_profiles\\ndef check_b2c_profiles(docs, snapshot):\\n    checks = _bc_simple_original_check_profiles(docs, snapshot)\\n    valid = all(isinstance(d.get(\\\'f_kleur\\\', []), list) and len(d.get(\\\'f_kleur\\\', [])) == len(set(d.get(\\\'f_kleur\\\', []))) and all(c in (*_BC_SIMPLE_COLORS[\\\'TAXONOMY\\\'], _BC_SIMPLE_COLORS[\\\'OTHER\\\']) for c in d.get(\\\'f_kleur\\\', [])) for d in docs)\\n    checks.append({\\\'name\\\': \\\'Basiskleuren zijn unieke geldige lijsten; exacte bronkleur apart bewaard\\\', \\\'passed\\\': valid and all(\\\'f_kleur_exact\\\' in d for d in docs if d.get(\\\'f_kleur\\\'))})\\n    valid = all(f.get(\\\'coverage_pct\\\', 0) <= 100 for p in snapshot[\\\'profiles\\\'].values() for f in p[\\\'filters\\\'])\\n    checks.append({\\\'name\\\': \\\'Afgeleide profieldekking telt ieder product hoogstens \xe9\xe9n keer\\\', \\\'passed\\\': valid})\\n    checks.append({\\\'name\\\': \\\'Exacte formaatcodes zijn een-op-een en horen bij het zichtbare maatpaar\\\',\\n                   \\\'passed\\\': snapshot.get(\\\'tile_format_codes_v1\\\') is True and\\n                   _bc_simple_check_tile_codes(docs, snapshot.get(\\\'tile_format_codes\\\', {}))})\\n    return checks\\n\\n# The same known alias table is shared with the frontend label normalizer.\\nclass _BcSimpleTypeLabels(dict):\\n    def get(self, key, default=None):\\n        return _BC_SIMPLE_TYPE_LABELS.get(\\\' \\\'.join(str(key).split()).casefold(), super().get(key, default))\\nTYPE_LABELS = _BcSimpleTypeLabels(TYPE_LABELS)\\nPLANS[\\\'tile\\\'] = (words(\\\'f_tegel_formaat\\\') + COMMON, words(\\\'f_serie f_tegel_breedte_mm f_tegel_lengte_mm f_materiaal f_slipvastheid\\\'))\\nLABELS[\\\'f_tegel_formaat\\\'] = \\\'Tegelformaat\\\'\\n\'\nTYPE_ALIASES = {\'f_productsoort\': {\'afvoerplug\': \'Afvoerplug\', \'afvoerpluggen\': \'Afvoerplug\', \'badkraan\': \'Badkraan\', \'badkranen\': \'Badkraan\', \'bidetkraan\': \'Bidetkraan\', \'bidetkranen\': \'Bidetkraan\', \'buitendouche\': \'Buitendouche\', \'buitendouches\': \'Buitendouche\', \'douchearm\': \'Douchearm\', \'douchearmen\': \'Douchearm\', \'douchebak\': \'Douchebak\', \'douchebakken\': \'Douchebak\', \'doucheslang\': \'Doucheslang\', \'doucheslangen\': \'Doucheslang\', \'fontein\': \'Fontein\', \'fonteinen\': \'Fontein\', \'fonteinkast\': \'Fonteinkast\', \'fonteinkasten\': \'Fonteinkast\', \'fonteinkraan\': \'Fonteinkraan\', \'fonteinkranen\': \'Fonteinkraan\', \'handdouche\': \'Handdouche\', \'handdouches\': \'Handdouche\', \'handdouchehouder\': \'Handdouchehouder\', \'handdouchehouders\': \'Handdouchehouder\', \'hangtoilet\': \'Hangtoilet\', \'hangtoiletten\': \'Hangtoilet\', \'wandclosetten\': \'Hangtoilet\', \'hoofddouche\': \'Hoofddouche\', \'hoofddouches\': \'Hoofddouche\', \'inloopdouche\': \'Inloopdouche\', \'inloopdouches\': \'Inloopdouche\', \'kolomkast\': \'Kolomkast\', \'kolomkasten\': \'Kolomkast\', \'onderkast\': \'Onderkast\', \'onderkasten\': \'Onderkast\', \'wastafelonderkast\': \'Onderkast\', \'sifon\': \'Sifon\', \'sifons\': \'Sifon\', \'toiletzitting\': \'Toiletzitting\', \'toiletzittingen\': \'Toiletzitting\', \'toiletaccessoire\': \'Toiletaccessoire\', \'toiletaccessoires\': \'Toiletaccessoire\', \'toilet toebehoren\': \'Toiletaccessoire\', \'bekerhouder\': \'Bekerhouder\', \'bekerhouders\': \'Bekerhouder\', \'keukenkraan\': \'Keukenkraan\', \'keukenkranen\': \'Keukenkraan\', \'los onderdeel\': \'Los onderdeel\', \'losse onderdelen\': \'Los onderdeel\', \'elektrische radiator\': \'Elektrische radiator\', \'elektrische radiatoren\': \'Elektrische radiator\', \'spiegelkast\': \'Spiegelkast\', \'spiegelkasten\': \'Spiegelkast\', \'reservoir\': \'Reservoir\', \'reservoirs\': \'Reservoir\', \'wastafel\': \'Wastafel\', \'wastafels\': \'Wastafel\', \'waskom\': \'Waskom\', \'waskommen\': \'Waskom\', \'wastafelblad\': \'Wastafelblad\', \'topbladen\': \'Wastafelblad\', \'vrijstaand bad\': \'Vrijstaand bad\', \'vrijstaande baden\': \'Vrijstaand bad\', \'halfvrijstaand bad\': \'Halfvrijstaand bad\', \'half vrijstaande baden\': \'Halfvrijstaand bad\', \'halfvrijstaande baden\': \'Halfvrijstaand bad\', \'inbouw badkraan\': \'Inbouw badkraan\', \'inbouwbadkraan\': \'Inbouw badkraan\', \'inbouw douchekraan\': \'Inbouw douchekraan\', \'inbouwdouchekraan\': \'Inbouw douchekraan\', \'inbouw doucheset\': \'Inbouw doucheset\', \'inbouwdoucheset\': \'Inbouw doucheset\', \'inbouw wastafelkraan\': \'Inbouw wastafelkraan\', \'inbouwwastafelkraan\': \'Inbouw wastafelkraan\', \'opbouw wastafelkraan\': \'Opbouw wastafelkraan\', \'opbouwwastafelkraan\': \'Opbouw wastafelkraan\', \'schuifdeur\': \'Schuifdeur\', \'douche schuifdeur\': \'Schuifdeur\', \'bedieningspaneel\': \'Bedieningspaneel\', \'bedieningspaneel toilet\': \'Bedieningspaneel\', \'bedieningspaneel voor toilet\': \'Bedieningspaneel\', \'bedieningsplaten\': \'Bedieningspaneel\', \'spiegels met verlichting\': \'Spiegels met verlichting\', \'moza\xefek\': \'Moza\xefek\', \'mozaiektegel\': \'Moza\xefek\'}, \'f_materiaal\': {\'rvs\': \'RVS\', \'roestvast staal\': \'RVS\', \'roestvrij staal\': \'RVS\', \'stainless steel\': \'RVS\', \'solid surface\': \'Solid surface\', \'solid-surface\': \'Solid surface\', \'keramiek\': \'Keramiek\', \'ceramic\': \'Keramiek\', \'ceramics\': \'Keramiek\', \'acryl\': \'Acryl\', \'acrylic\': \'Acryl\'}, \'f_kraanmontage\': {\'inbouw\': \'Inbouw\', \'opbouw\': \'Opbouw\', \'vrijstaand\': \'Vrijstaand\'}}\n\ndef patch_simple_worker(source):\n    if not isinstance(source, str):\n        raise RuntimeError(\'Workerbron moet tekst zijn\')\n    if MARKER in source:\n        if source.count(MARKER) != 1 or hashlib.sha256(source.encode()).hexdigest() != PATCHED_WORKER_SHA256:\n            raise RuntimeError(\'Bestaande vereenvoudigingspatch wijkt af; geen wijziging\')\n        compile(source, \'<simple-worker-existing>\', \'exec\')\n        return source\n    if hashlib.sha256(source.encode()).hexdigest() != BASE_WORKER_SHA256:\n        raise RuntimeError(\'Worker wijkt af van de beoordeelde bestaande versie\')\n    tree = ast.parse(source)\n    functions = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}\n    if not {\'prepare\',\'patch_api\'}.issubset(functions):\n        raise RuntimeError(\'Verwachte voorbereidings- of APIhook ontbreekt\')\n    prepare = functions[\'prepare\']\n    changes = {\'schema\': 0, \'definitions\': 0, \'snapshot\': 0, \'log\': 0}\n    output = []\n    for statement in prepare.body:\n        output.append(statement)\n        if isinstance(statement, ast.Assign) and len(statement.targets) == 1 and isinstance(statement.targets[0], ast.Name):\n            target = statement.targets[0].id\n            if target == \'schema\' and isinstance(statement.value, ast.Call) and isinstance(statement.value.func, ast.Name) and statement.value.func.id == \'_bc_add_variant_schema\':\n                output.extend(ast.parse(\'schema = _bc_simple_schema(schema)\').body); changes[\'schema\'] += 1\n            if target == \'definitions\':\n                output.extend(ast.parse(\'definitions = _bc_simple_definitions(definitions)\').body); changes[\'definitions\'] += 1\n            if target == \'snapshot\':\n                output.extend(ast.parse(\'_bc_simple_snapshot(snapshot, docs)\').body); changes[\'snapshot\'] += 1\n        if isinstance(statement, ast.Expr) and isinstance(statement.value, ast.Call) and isinstance(statement.value.func, ast.Name) and statement.value.func.id == \'log\':\n            text = ast.unparse(statement)\n            if \'PVD blijft apart\' in text:\n                output[-1] = ast.parse("log(\'Basiskleuren en gepaarde tegelformaten afgeleid; exacte bronwaarden behouden.\')").body[0]\n                changes[\'log\'] += 1\n    prepare.body = output\n    if changes != {\'schema\': 1, \'definitions\': 1, \'snapshot\': 1, \'log\': 1}:\n        raise RuntimeError(\'Niet alle vereenvoudigingshooks gevonden\')\n    api = functions[\'patch_api\']\n    api.body = ast.parse("if \'# BC_FILTER_SIMPLIFICATION_V1\' in source:\\n    return patch_simple_api(source)\\nreturn patch_simple_api(patch_variant_api(patch_rvs_api(patch_b2c_api(patch_generation_api(source)))))").body\n    ast.fix_missing_locations(tree)\n    # Replace only two reviewed functions so unrelated source stays byte-identical.\n    lines = source.splitlines(keepends=True)\n    replacements = []\n    for node in (prepare, api):\n        start = sum(len(s) for s in lines[:node.lineno-1])\n        end = sum(len(s) for s in lines[:node.end_lineno])\n        replacements.append((start,end,ast.unparse(node)+\'\\n\'))\n    result = source\n    for start,end,text in sorted(replacements, reverse=True):\n        result = result[:start] + text + result[end:]\n    result_tree = ast.parse(result)\n    guards = [n for n in result_tree.body if isinstance(n, ast.If) and \'__name__\' in ast.unparse(n.test)]\n    if len(guards) != 1:\n        raise RuntimeError(\'Geen unieke workerstartguard\')\n    lines = result.splitlines(keepends=True)\n    position = sum(len(s) for s in lines[:guards[0].lineno-1])\n    prelude = MARKER + \'\\n_BC_SIMPLE_COLORS = {"__name__": "bc_simple_colors_embedded"}\\nexec(compile(\' + repr(COLOR_SOURCE) + \', "<derived-color-rules>", "exec"), _BC_SIMPLE_COLORS)\\n\'\n    prelude += \'_BC_SIMPLE_ENUM_ALIASES = \' + repr(TYPE_ALIASES) + \'\\n_BC_SIMPLE_TYPE_LABELS = _BC_SIMPLE_ENUM_ALIASES["f_productsoort"]\\n\'\n    prelude += RUNTIME_SOURCE.rstrip() + \'\\n\\n\'\n    result = result[:position] + prelude + result[position:]\n    compile(result, \'<simple-worker>\', \'exec\')\n    return result\n', 'api': '"""Guarded request normalization for the existing search API; no deployment."""\n\n_BC_SIMPLE_API_BASE_AST = \'76a5ab7e741528d0aa5327b64988fd57d5f3b5fb7f54e952f76ce2bd50e0a938\'\n_BC_SIMPLE_API_MARKER = \'# BC_FILTER_SIMPLIFICATION_V1\'\n_BC_SIMPLE_API_REQUEST_HELPER = \'\'\'def _bc_simple_request(body):\n    snapshot = _bc_snapshot()\n    if snapshot.get(\'filter_simplification_v1\') is not True:\n        return body\n    aliases = snapshot.get(\'filter_color_aliases\') or {}\n    values = body.filters.get(\'f_kleur\')\n    if not isinstance(values, list) or len(values) > 100:\n        return body\n    normalized = []\n    seen = set()\n    for value in values:\n        if not isinstance(value, str):\n            normalized.append(value)\n            continue\n        canonical = aliases.get(value, value)\n        if not isinstance(canonical, str):\n            raise RuntimeError(\'Ongeldige kleurregels in actieve filtergeneratie\')\n        if canonical not in seen:\n            normalized.append(canonical)\n            seen.add(canonical)\n    if normalized == values:\n        return body\n    filters = {**body.filters, \'f_kleur\': normalized}\n    return body.copy(update={\'filters\': filters})\n\ndef _bc_simple_facet_limit(facet):\n    if _bc_snapshot().get(\'filter_simplification_v1\') is not True:\n        return 100\n    if facet.get(\'field\') == \'f_tegel_formaat\':\n        return 500\n    if facet.get(\'type\') == \'range\':\n        return 100\n    count = facet.get(\'distinct_values\', 100)\n    if isinstance(count, int) and not isinstance(count, bool):\n        return min(1000, max(100, count))\n    return 100\n\ndef _bc_simple_choice_clause(field, values, quoted_values):\n    snapshot = _bc_snapshot()\n    if field != \'f_tegel_formaat\' or snapshot.get(\'filter_simplification_v1\') is not True:\n        return field + (\':=\' + quoted_values[0] if len(quoted_values) == 1 else \':=[\' + \',\'.join(quoted_values) + \']\')\n    if snapshot.get(\'tile_format_codes_v1\') is not True:\n        raise RuntimeError(\'Exacte formaatcodes ontbreken in actieve filtergeneratie\')\n    mapping = snapshot.get(\'tile_format_codes\')\n    if not isinstance(mapping, dict) or any(not isinstance(label, str) or type(code) is not int or not 1 <= code <= 2147483647 for label, code in mapping.items()):\n        raise RuntimeError(\'Ongeldige formaatcodekaart in actieve filtergeneratie\')\n    if len(set(mapping.values())) != len(mapping):\n        raise RuntimeError(\'Dubbele formaatcodes in actieve filtergeneratie\')\n    codes = list(dict.fromkeys(mapping.get(value, 0) for value in values if isinstance(value, str) and value.strip()))\n    # Code zero is reserved and never assigned to a document.\n    if len(codes) == 1:\n        return \'f_tegel_formaat_code:=\' + str(codes[0])\n    return \'f_tegel_formaat_code:[\' + \',\'.join(str(code) for code in codes) + \']\'\n\'\'\'\n\n\ndef patch_simple_api(source):\n    import ast\n    import copy\n    import hashlib\n\n    def canonical(value):\n        if isinstance(value, ast.AST):\n            return (type(value).__name__, tuple((key, canonical(child))\n                for key, child in ast.iter_fields(value)\n                if not (key == \'type_params\' and not child)))\n        if isinstance(value, list):\n            return tuple(canonical(child) for child in value)\n        return value\n\n    def digest(tree):\n        return hashlib.sha256(repr(canonical(tree)).encode()).hexdigest()\n\n    tree = ast.parse(source)\n    plans = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == \'plan\']\n    if len(plans) != 1:\n        raise RuntimeError(\'Geen unieke gecontroleerde filterplanner\')\n    plan = plans[0]\n    assignment = ast.parse(\'body = _bc_simple_request(body)\').body[0]\n    expected_helpers = ast.parse(_BC_SIMPLE_API_REQUEST_HELPER).body\n    helper_names = {n.name for n in expected_helpers}\n    helpers = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in helper_names]\n\n    class FormatClause(ast.NodeTransformer):\n        def __init__(self, restore=False):\n            self.restore = restore\n            self.count = 0\n\n        def visit_Assign(self, node):\n            self.generic_visit(node)\n            old = ast.parse("clauses[field] = field + (\':=\' + vals[0] if len(vals) == 1 else \':=[\' + \',\'.join(vals) + \']\')").body[0]\n            new = ast.parse(\'clauses[field] = _bc_simple_choice_clause(field, values, vals)\').body[0]\n            expected, replacement = (new, old) if self.restore else (old, new)\n            if canonical(node) == canonical(expected):\n                self.count += 1\n                return ast.copy_location(replacement, node)\n            return node\n\n    class FacetLimit(ast.NodeTransformer):\n        def __init__(self, restore=False):\n            self.restore = restore\n            self.count = 0\n\n        def visit_Dict(self, node):\n            self.generic_visit(node)\n            for i, key in enumerate(node.keys):\n                if isinstance(key, ast.Constant) and key.value == \'max_facet_values\':\n                    value = node.values[i]\n                    expected = ast.parse(\'_bc_simple_facet_limit(f)\', mode=\'eval\').body\n                    if self.restore:\n                        if canonical(value) != canonical(expected):\n                            raise RuntimeError(\'Onverwachte wijziging in facetlimiet\')\n                        node.values[i] = ast.Constant(value=100)\n                    else:\n                        if not isinstance(value, ast.Constant) or value.value != 100:\n                            raise RuntimeError(\'Onverwachte bestaande facetlimiet\')\n                        node.values[i] = expected\n                    self.count += 1\n            return node\n    if _BC_SIMPLE_API_MARKER in source:\n        if source.count(_BC_SIMPLE_API_MARKER) != 1 or len(helpers) != len(expected_helpers):\n            raise RuntimeError(\'Onverwachte bestaande vereenvoudigingspatch\')\n        if canonical(helpers) != canonical(expected_helpers) or canonical(plan.body[0]) != canonical(assignment):\n            raise RuntimeError(\'Bestaande filtervereenvoudiging is gewijzigd\')\n        restored = copy.deepcopy(tree)\n        restored.body = [n for n in restored.body if not (isinstance(n, ast.FunctionDef) and n.name in helper_names)]\n        restored_plan = next(n for n in restored.body if isinstance(n, ast.FunctionDef) and n.name == \'plan\')\n        restored_plan.body.pop(0)\n        clauses = FormatClause(restore=True)\n        clauses.visit(restored_plan)\n        if clauses.count != 1:\n            raise RuntimeError(\'Exacte formaatplanner is gewijzigd\')\n        limits = FacetLimit(restore=True)\n        limits.visit(restored_plan)\n        if limits.count != 1:\n            raise RuntimeError(\'Facetplanner mist de gecontroleerde limiet\')\n        if digest(restored) != _BC_SIMPLE_API_BASE_AST:\n            raise RuntimeError(\'Overige API-code is tussentijds gewijzigd\')\n        return source\n    if helpers or digest(tree) != _BC_SIMPLE_API_BASE_AST:\n        raise RuntimeError(\'API-bron wijkt af van de beoordeelde actieve versie\')\n    plan.body.insert(0, assignment)\n    clauses = FormatClause()\n    clauses.visit(plan)\n    if clauses.count != 1:\n        raise RuntimeError(\'Geen unieke keuzeclausule in bestaande planner\')\n    limits = FacetLimit()\n    limits.visit(plan)\n    if limits.count != 1:\n        raise RuntimeError(\'Geen unieke facetplannerlimiet\')\n    ast.fix_missing_locations(plan)\n    lines = source.splitlines(keepends=True)\n    start = sum(len(line) for line in lines[:plan.lineno - 1])\n    end = sum(len(line) for line in lines[:plan.end_lineno])\n    result = source[:start] + ast.unparse(plan) + \'\\n\' + source[end:]\n    result = result.rstrip() + \'\\n\\n\' + _BC_SIMPLE_API_MARKER + \'\\n\' + _BC_SIMPLE_API_REQUEST_HELPER\n    compile(result, \'<simplified-filter-api>\', \'exec\')\n    # Prove that the added helper and the exact original program can be recovered.\n    return patch_simple_api(result)\n'}
TARGET_WORKER_SHA256 = '25e8c3b1763171875bebd5b85e7099b26f87e36f3ece0b9f1f21e1d37b56dbe3'
TARGET_API_SHA256 = '3a7701134be7ac55b0a83436ceb16ebb19ac0a88aba17c283490f90047f02094'
TARGET_API_AST_SHA256 = '4b4dcf726b3f66f06d5f62bc322c8a9a236459ddf32cf56a2440e4c10147570b'
BASE_WORKER_SHA256 = 'e5f3c4103266c3df1f03b855395d0d6c1711b7452a7626c91889cfc9b3ab280c'
BASE_API_SHA256 = '7fe0b7faa2f5bf83af40edfa8d409dc382ba25453c15f6ebea4115c76e29f3b3'
BASE_API_AST_SHA256 = '76a5ab7e741528d0aa5327b64988fd57d5f3b5fb7f54e952f76ce2bd50e0a938'
ROOT = Path('/opt/badkamercity/filter-sync')
LIVE = Path('/home/ubuntu/bc_apiproef_20261013')
TIMER = 'bc-filter-sync.timer'
SERVICE = 'bc-filter-sync.service'
DEADLINE_SECONDS = 900
RECOVERY_SECONDS = 240


def sha256(value):
    return hashlib.sha256(value).hexdigest()


def ast_digest(source):
    def canonical(value):
        if isinstance(value, ast.AST):
            return (type(value).__name__, tuple((key, canonical(child))
                for key, child in ast.iter_fields(value)
                if not (key == 'type_params' and not child)))
        if isinstance(value, list):
            return tuple(canonical(child) for child in value)
        return value
    return sha256(repr(canonical(ast.parse(source))).encode('utf-8'))


def base_api_matches(source):
    if sha256(source) == BASE_API_SHA256:
        return True
    try:
        return bool(BASE_API_AST_SHA256 and ast_digest(source) == BASE_API_AST_SHA256)
    except (SyntaxError, UnicodeError, ValueError):
        return False


def say(value):
    try:
        print(value, flush=True)
    except OSError:
        # A closed SSH/PowerShell output stream must not interrupt recovery.
        pass


def read_regular(path, optional=False):
    if any(part.is_symlink() for part in (path, *path.parents)):
        raise RuntimeError('Onverwachte bestandsverwijzing; gestopt')
    try:
        info = path.stat()
    except FileNotFoundError:
        if optional:
            return None
        raise RuntimeError('Een vereist serverbestand ontbreekt') from None
    if not stat.S_ISREG(info.st_mode) or info.st_size > 5_000_000:
        raise RuntimeError('Onverwacht bestandstype of bestandsgrootte')
    return path.read_bytes()


def write_atomic(path, data, mode=0o600):
    if path.is_symlink():
        raise RuntimeError('Onverwachte verwijzing bij schrijven')
    fd, name = tempfile.mkstemp(prefix='.bc-filter-', dir=str(path.parent))
    try:
        with os.fdopen(fd, 'wb') as stream:
            os.fchmod(stream.fileno(), mode)
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def compose_worker(source, patch_sources):
    if sha256(source) != BASE_WORKER_SHA256:
        raise RuntimeError('Worker verschilt van de aangeleverde en beoordeelde versie')
    namespace = {'__name__': 'bc_filter_worker_patch'}
    exec(compile(patch_sources['worker'], '<reviewed-worker-patch>', 'exec'), namespace)
    result = namespace['patch_simple_worker'](source.decode('utf-8'))
    api_module = patch_sources['api']
    api_tree = ast.parse(api_module)
    if not any(isinstance(node, ast.FunctionDef) and node.name == 'patch_simple_api'
               for node in api_tree.body):
        raise RuntimeError('API-module mist de beoordeelde filterpatch')
    if any(isinstance(node, ast.ImportFrom) and node.module == '__future__'
           for node in api_tree.body):
        raise RuntimeError('API-module mag hier geen future-import bevatten')
    tree = ast.parse(result)
    hooks = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == 'patch_api']
    if len(hooks) != 1:
        raise RuntimeError('Geen unieke API-patchfunctie in worker')
    lines = result.splitlines(keepends=True)
    position = sum(len(line) for line in lines[:hooks[0].lineno - 1])
    result = result[:position] + api_module.rstrip() + '\n\n' + result[position:]
    compile(result, '<repaired-search-worker>', 'exec')
    return result.encode('utf-8')


def load_worker(source):
    module = types.ModuleType('bc_filter_release_candidate')
    module.__file__ = str(ROOT / 'sync.py')
    exec(compile(source, '<repaired-search-worker>', 'exec'), module.__dict__)
    return module


def systemctl(*args):
    try:
        result = subprocess.run(['systemctl', *args], capture_output=True, text=True,
                                timeout=30, check=False)
    except (OSError, subprocess.TimeoutExpired):
        raise RuntimeError('Systeemtaak reageert niet op tijd') from None
    return result.returncode, result.stdout.strip()


def change_timer(action):
    code, _ = systemctl(action, TIMER)
    if code:
        raise RuntimeError('Automatische ververstimer kon niet worden ' +
                           ('gepauzeerd' if action == 'stop' else 'hervat'))
    _, state = systemctl('is-active', TIMER)
    if state != ('active' if action == 'start' else 'inactive'):
        raise RuntimeError('Status van ververstimer is niet bevestigd na ' + action)


def restore_bytes(path, data, mode=0o600):
    current = read_regular(path, optional=True)
    if current == data:
        return
    if data is None:
        if current is not None:
            path.unlink()
    else:
        write_atomic(path, data, mode)


def restore_owned_metadata(path, previous, generation):
    """Restore our generation's bookkeeping while preserving an unrelated edit."""
    current = read_regular(path, optional=True)
    if current == previous:
        return True
    if generation is None or current is None:
        return False
    try:
        if path.name == 'prepared.txt':
            owned = current.decode('utf-8').strip() == generation
        else:
            value = json.loads(current)
            owned = isinstance(value, dict) and value.get('generation') == generation
    except (ValueError, UnicodeError):
        return False
    if not owned:
        return False
    restore_bytes(path, previous)
    return True


def safe_message(error, secrets):
    message = str(error) if isinstance(error, RuntimeError) else type(error).__name__
    for secret in sorted({str(x) for x in secrets if x and len(str(x)) >= 4}, key=len, reverse=True):
        message = message.replace(secret, '[afgeschermd]')
    return message[:900]


def repair(root=ROOT, live=LIVE, patch_sources=None, worker_factory=load_worker):
    if os.geteuid() != 0:
        raise RuntimeError('Voer deze reparatie met sudo python3 uit')
    if root != ROOT or live != LIVE:
        raise RuntimeError('Dit pakket is uitsluitend voor de bestaande zoekservice')
    patch_sources = patch_sources or PATCH_SOURCES
    if not isinstance(patch_sources, dict) or set(patch_sources) != {'api', 'worker'}:
        raise RuntimeError('Gebruik het complete gepubliceerde reparatiepakket')
    worker_path = root / 'sync.py'
    app_path = live / 'app.py'
    snapshot_path = live / 'bc_sync/active.json'
    original_worker = read_regular(worker_path)
    original_app = read_regular(app_path)
    if (TARGET_WORKER_SHA256 and sha256(original_worker) == TARGET_WORKER_SHA256 and
            TARGET_API_AST_SHA256 and ast_digest(original_app) == TARGET_API_AST_SHA256):
        snapshot = json.loads(read_regular(snapshot_path))
        if (snapshot.get('variant_aliases_v1') is not True or
                snapshot.get('filter_simplification_v1') is not True or
                snapshot.get('tile_format_codes_v1') is not True):
            raise RuntimeError('Gepatchte code gevonden zonder bevestigde filterindex')
        current = worker_factory(original_worker)
        health, _ = current.probe('http://127.0.0.1:8082/health')
        if health.get('ok') is not True or health.get('typesense_collection') != snapshot['collection']:
            raise RuntimeError('Gepatchte code gevonden; actieve zoekservice is nog niet bevestigd')
        _, timer_state = systemctl('is-active', TIMER)
        say('FILTERAANPASSING WAS AL TOEGEPAST | collectie: ' + snapshot['collection'])
        return {'status': 'already_applied' if timer_state == 'active' else 'already_applied_scheduler_pending',
                'collection': snapshot['collection'], 'timer_state': timer_state}
    if sha256(original_worker) != BASE_WORKER_SHA256 or not base_api_matches(original_app):
        raise RuntimeError('Servercode is inmiddels gewijzigd; geen bestanden overschreven')
    patched_worker = compose_worker(original_worker, patch_sources)
    if TARGET_WORKER_SHA256 and sha256(patched_worker) != TARGET_WORKER_SHA256:
        raise RuntimeError('Filterpakket heeft een afwijkende workerhash')
    worker = worker_factory(patched_worker)
    worker.log = say
    expected_api = worker.patch_api(original_app.decode()).encode()
    if TARGET_API_AST_SHA256 and ast_digest(expected_api) != TARGET_API_AST_SHA256:
        raise RuntimeError('Filterpakket heeft afwijkende API-logica')
    lock_path = root / 'sync.lock'
    if lock_path.is_symlink():
        raise RuntimeError('Onverwachte verwijzing in synchronisatieslot')
    with lock_path.open('a+') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise RuntimeError('Een verversing loopt al. Wacht tot die klaar is en voer opnieuw uit.') from None
        # Recheck after locking; a completed hourly run or manual deployment is preserved.
        if read_regular(worker_path) != original_worker or read_regular(app_path) != original_app:
            raise RuntimeError('Servercode veranderde tijdens controle; gestopt')
        original_snapshot = read_regular(snapshot_path, optional=True)
        metadata_paths = ['STATUS.json', 'prepared.txt', 'last_transaction.json', 'original_transaction.json']
        metadata = {name: read_regular(root / name, optional=True) for name in metadata_paths}
        old_error = read_regular(root / 'LAST_ERROR.json', optional=True)
        _, timer_state = systemctl('is-active', TIMER)
        if timer_state not in ('active', 'inactive', 'failed'):
            raise RuntimeError('Status van ververstimer is niet eenduidig')
        timer_was_active = timer_state == 'active'
        timer_stopped = False
        completed = False
        installed = False
        backup = None
        staged = None
        candidate_generation = None
        secrets = []
        stop_heartbeat = threading.Event()
        started = time.monotonic()
        phase = ['voorbereiden']

        def heartbeat():
            while not stop_heartbeat.wait(20):
                say('Nog bezig: ' + phase[0] + ' | ' + str(int(time.monotonic() - started)) + ' seconden')

        def expired(signum, frame):
            raise RuntimeError('Tijdslimiet van 15 minuten bereikt; veilige afronding/herstel gestart')

        def terminated(signum, frame):
            raise RuntimeError('Uitvoering onderbroken; veilige afronding/herstel gestart')

        old_handler = signal.signal(signal.SIGALRM, expired)
        termination_handlers = {number: signal.signal(number, terminated)
                                for number in (signal.SIGTERM, signal.SIGHUP)}
        thread = threading.Thread(target=heartbeat, daemon=True)
        try:
            if timer_was_active:
                timer_stopped = True
                change_timer('stop')
            stamp = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S') + '-' + os.urandom(3).hex()
            backups = root / 'filter-simplification-backups'
            if backups.is_symlink():
                raise RuntimeError('Onverwachte verwijzing in herstelmap')
            backups.mkdir(mode=0o700, exist_ok=True)
            backup = backups / stamp
            backup.mkdir(mode=0o700)
            for name, data in {'sync.py': original_worker, 'app.py': original_app,
                               'active.json': original_snapshot, 'LAST_ERROR.json': old_error,
                               **metadata}.items():
                if data is not None:
                    write_atomic(backup / name, data)
            write_atomic(backup / 'candidate.py', patched_worker)
            say('Back-up gereed: ' + str(backup))
            signal.alarm(DEADLINE_SECONDS)
            thread.start()
            shop = worker.Shopify()
            secrets.extend([getattr(shop, 'token', ''), *getattr(shop, 'config', {}).values()])
            ts = worker.Typesense()
            secrets.append(getattr(ts, 'key', ''))
            phase[0] = 'volledige Shopify-export en controles'
            staged = worker.prepare(shop, ts)
            candidate_snapshot = json.loads((staged / 'snapshot.json').read_text())
            candidate_generation = candidate_snapshot.get('generation')
            if candidate_snapshot.get('variant_aliases_v1') is not True:
                raise RuntimeError('Voorbereide index mist de volledige variantondersteuning')
            if candidate_snapshot.get('filter_simplification_v1') is not True:
                raise RuntimeError('Voorbereide index mist de vereenvoudigde filterlaag')
            if candidate_snapshot.get('tile_format_codes_v1') is not True:
                raise RuntimeError('Voorbereide index mist de exacte tegelformaatcodes')
            phase[0] = 'gecontroleerde index activeren'
            snapshot = worker.activate(shop, ts, staged)
            if (snapshot.get('variant_aliases_v1') is not True or
                    snapshot.get('filter_simplification_v1') is not True or
                    snapshot.get('tile_format_codes_v1') is not True):
                raise RuntimeError('Actieve generatie mist vereiste variant-/filter-/formaatvlaggen')
            report = json.loads((staged / 'RESULTAAT.json').read_text())
            if report.get('passed') is not True or report.get('active_changes') is not True:
                raise RuntimeError('Activatierapport bevestigt geen volledige reparatie')
            if read_regular(worker_path) != original_worker:
                raise RuntimeError('Worker is tussentijds gewijzigd; handmatige wijziging behouden')
            if read_regular(app_path) != expected_api:
                raise RuntimeError('Actieve API wijkt af van de voorbereide reparatie')
            write_atomic(root / 'sync.previous.py', original_worker, 0o755)
            write_atomic(worker_path, patched_worker, 0o755)
            installed = True
            if read_regular(worker_path) != patched_worker:
                raise RuntimeError('Ge\xefnstalleerde worker is niet exact teruggelezen')
            systemctl('reset-failed', SERVICE)
            error_path = root / 'LAST_ERROR.json'
            if error_path.exists():
                read_regular(error_path)
                error_path.unlink()
            completed = True
            signal.alarm(0)
            summary = {'status': 'applied_verified', 'collection': snapshot['collection'],
                       'products': report['products'], 'profiles': report['profiles'],
                       'backup': str(backup), 'worker_sha256': sha256(patched_worker),
                       'api_sha256': sha256(expected_api), 'variant_aliases_v1': True,
                       'filter_simplification_v1': True, 'tile_format_codes_v1': True}
            write_atomic(backup / 'REPAIR_RESULT.json', json.dumps(summary, indent=2).encode())
            say('FILTERS VEREENVOUDIGD | ' + str(report['products']) + ' producten | ' + str(report['profiles']) + ' profielen')
            return summary
        except BaseException as error:
            completed = False
            signal.alarm(0)
            for number in termination_handlers:
                signal.signal(number, signal.SIG_IGN)
            phase[0] = 'herstel controleren'
            restored = False
            try:
                signal.alarm(RECOVERY_SECONDS)
                now_snapshot = read_regular(snapshot_path, optional=True)
                now_app = read_regular(app_path)
                if now_snapshot == original_snapshot and now_app == original_app:
                    restored = True
                elif staged is not None:
                    candidate_bytes = read_regular(staged / 'snapshot.json')
                    # Restore only our own activation, never a different human deployment.
                    if now_snapshot == candidate_bytes and now_app in (original_app, expected_api):
                        transaction = json.loads(read_regular(root / 'last_transaction.json'))
                        previous_collection = (json.loads(original_snapshot)['collection']
                                               if original_snapshot is not None else None)
                        if (transaction.get('generation') != json.loads(candidate_bytes)['generation'] or
                                transaction.get('had_snapshot') is not (original_snapshot is not None) or
                                (previous_collection is not None and
                                 transaction.get('previous_collection') != previous_collection)):
                            raise RuntimeError('Hersteltransactie hoort niet bij deze uitvoering')
                        worker.restore_transaction(transaction)
                        restored = (read_regular(snapshot_path, optional=True) == original_snapshot and
                                    read_regular(app_path) == original_app)
                if restored:
                    if installed and read_regular(worker_path) == patched_worker:
                        write_atomic(worker_path, original_worker, 0o755)
                        installed = False
                    for name, data in metadata.items():
                        restore_owned_metadata(root / name, data, candidate_generation)
                if backup is not None:
                    failure = {'status': 'failed', 'previous_live_restored': restored,
                               'message': safe_message(error, secrets)}
                    write_atomic(backup / 'REPAIR_RESULT.json', json.dumps(failure, indent=2).encode())
                say('REPARATIE GESTOPT | ' + safe_message(error, secrets))
                say('Vorige liveversie gecontroleerd: ' + ('hersteld/behouden' if restored else 'handmatige controle nodig'))
            except BaseException as recovery_error:
                say('HERSTELCONTROLE NIET VOLTOOID | ' + safe_message(recovery_error, secrets))
            finally:
                signal.alarm(0)
            raise RuntimeError('Reparatie niet als voltooid gemarkeerd. Plak de uitvoer terug in de chat.') from None
        finally:
            signal.alarm(0)
            for number in termination_handlers:
                signal.signal(number, signal.SIG_IGN)
            stop_heartbeat.set()
            if thread.ident is not None:
                thread.join(timeout=1)
            try:
                if timer_stopped:
                    try:
                        change_timer('start')
                        say('Automatische ververstimer hervat.')
                    except RuntimeError:
                        if completed:
                            say('INDEX EN WORKER HERSTELD; VERFRESTIMER NIET HERVAT. Plak deze uitvoer terug.')
                            if backup is not None:
                                summary['status'] = 'applied_scheduler_pending'
                                summary['timer_active'] = False
                                write_atomic(backup / 'REPAIR_RESULT.json', json.dumps(summary, indent=2).encode())
                        else:
                            say('Ververstimer niet hervat; controle nodig.')
                        raise
            finally:
                signal.signal(signal.SIGALRM, old_handler)
                for number, handler in termination_handlers.items():
                    signal.signal(number, handler)


if __name__ == '__main__':
    try:
        result = repair()
        say(json.dumps(result, ensure_ascii=False))
    except (Exception, KeyboardInterrupt) as error:
        say('STOP: ' + safe_message(error, []))
        raise SystemExit(2)
