#!/usr/bin/env python3
"""Apply reviewed exact Cottoceramix series/color corrections.

The builder embeds one catalog-free worker patch. The existing full staging,
readback, activation and rollback lifecycle stays in force. API source and
Shopify product data must remain unchanged.
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

PATCH_SOURCES = {'worker': '"""Guarded, catalog-free Cottoceramix visual color corrections.\n\nThe release builder freezes reviewed rules and the resulting worker hash.\nManufacturer fields, existing owner rules, API source and size codes are kept.\n"""\nimport ast\nimport hashlib\n\nBASE_WORKER_SHA256 = \'3c6dd21f50081f4ad8d770194dc35a97c101a09910dd8892403e51b93f1495eb\'\nPATCHED_WORKER_SHA256 = \'cc13abd05c87a490bf06d0a7358ef36bc700edc0a736a48714d704df62f8dcc2\'\nSCOPED_RULES = [{\'series\': \'3D Bars\', \'exact_color\': \'Onix Gloss\', \'colors\': [\'Zwart\'], \'confidence\': 0.98}, {\'series\': \'3D Bars\', \'exact_color\': \'Onix Matt\', \'colors\': [\'Zwart\'], \'confidence\': 0.94}, {\'series\': \'3D Bars\', \'exact_color\': \'Quartz Gloss\', \'colors\': [\'Wit\'], \'confidence\': 0.96}, {\'series\': \'3D Bars\', \'exact_color\': \'Quartz Matt\', \'colors\': [\'Wit\'], \'confidence\': 0.96}, {\'series\': \'3D Bars\', \'exact_color\': \'Topaz Matt\', \'colors\': [\'Beige\'], \'confidence\': 0.93}, {\'series\': \'Alma Scale\', \'exact_color\': \'Pearl\', \'colors\': [\'Grijs\'], \'confidence\': 0.98}, {\'series\': \'Alter Ego\', \'exact_color\': \'Bruciato\', \'colors\': [\'Bruin\'], \'confidence\': 0.94}, {\'series\': \'Alter Ego\', \'exact_color\': \'Sbiancato\', \'colors\': [\'Beige\'], \'confidence\': 0.95}, {\'series\': \'Alure Scale\', \'exact_color\': \'Pearl\', \'colors\': [\'Grijs\'], \'confidence\': 0.98}, {\'series\': \'Arabesco\', \'exact_color\': \'Silver Mist\', \'colors\': [\'Grijs\'], \'confidence\': 0.9}, {\'series\': \'Arabesco\', \'exact_color\': \'Silver Sands\', \'colors\': [\'Grijs\', \'Beige\'], \'confidence\': 0.85}, {\'series\': \'Arabesco\', \'exact_color\': \'Snow Cap\', \'colors\': [\'Wit\'], \'confidence\': 0.92}, {\'series\': \'Arabesco\', \'exact_color\': \'Timberline\', \'colors\': [\'Grijs\'], \'confidence\': 0.76}, {\'series\': \'Arabesco\', \'exact_color\': \'Volc\xe1nico\', \'colors\': [\'Zwart\'], \'confidence\': 0.97}, {\'series\': \'Argillae\', \'exact_color\': \'Gobi\', \'colors\': [\'Oranje\'], \'confidence\': 0.88}, {\'series\': \'Argillae\', \'exact_color\': \'Nocta\', \'colors\': [\'Zwart\'], \'confidence\': 0.94}, {\'series\': \'Argillae\', \'exact_color\': \'Terra\', \'colors\': [\'Oranje\'], \'confidence\': 0.88}, {\'series\': \'Arka\', \'exact_color\': \'Bone\', \'colors\': [\'Beige\'], \'confidence\': 0.96}, {\'series\': \'Arka\', \'exact_color\': \'Steel\', \'colors\': [\'Grijs\'], \'confidence\': 0.9}, {\'series\': \'Attico\', \'exact_color\': \'Natural\', \'colors\': [\'Beige\'], \'confidence\': 0.97}, {\'series\': \'Bejmat\', \'exact_color\': \'Tan Matt\', \'colors\': [\'Oranje\'], \'confidence\': 0.86}, {\'series\': \'Belgium Stone\', \'exact_color\': \'Dark\', \'colors\': [\'Grijs\'], \'confidence\': 0.96}, {\'series\': \'Benasal\', \'exact_color\': \'Caldera\', \'colors\': [\'Bruin\'], \'confidence\': 0.88}, {\'series\': \'Bloom-R\', \'exact_color\': \'Bold\', \'colors\': [\'Bruin\'], \'confidence\': 0.91}, {\'series\': \'Bloom-R\', \'exact_color\': \'Chipper\', \'colors\': [\'Bruin\'], \'confidence\': 0.91}, {\'series\': \'Bloom-R\', \'exact_color\': \'Mellow\', \'colors\': [\'Beige\'], \'confidence\': 0.91}, {\'series\': \'Boston\', \'exact_color\': \'Day\', \'colors\': [\'Beige\'], \'confidence\': 0.93}, {\'series\': \'Boston\', \'exact_color\': \'Downtown\', \'colors\': [\'Wit\', \'Beige\'], \'confidence\': 0.88}, {\'series\': \'Boston\', \'exact_color\': \'East\', \'colors\': [\'Beige\'], \'confidence\': 0.93}, {\'series\': \'Boston\', \'exact_color\': \'North\', \'colors\': [\'Bruin\', \'Oranje\'], \'confidence\': 0.88}, {\'series\': \'Boston\', \'exact_color\': \'South\', \'colors\': [\'Bruin\'], \'confidence\': 0.93}, {\'series\': \'Boston\', \'exact_color\': \'West\', \'colors\': [\'Grijs\', \'Bruin\'], \'confidence\': 0.88}, {\'series\': \'Boubles\', \'exact_color\': \'Dark\', \'colors\': [\'Grijs\'], \'confidence\': 0.93}, {\'series\': \'Boubles\', \'exact_color\': \'Terra\', \'colors\': [\'Bruin\'], \'confidence\': 0.95}, {\'series\': \'Casablanca\', \'exact_color\': \'Adobe\', \'colors\': [\'Oranje\'], \'confidence\': 0.86}, {\'series\': \'Casablanca\', \'exact_color\': \'Ash\', \'colors\': [\'Beige\'], \'confidence\': 0.86}, {\'series\': \'Casablanca\', \'exact_color\': \'Water\', \'colors\': [\'Groen\', \'Blauw\'], \'confidence\': 0.9}, {\'series\': \'Casetone\', \'exact_color\': \'Oak\', \'colors\': [\'Beige\'], \'confidence\': 0.91}, {\'series\': \'Ceppo di Gre\', \'exact_color\': \'Natural\', \'colors\': [\'Beige\', \'Grijs\'], \'confidence\': 0.86}, {\'series\': \'Cool\', \'exact_color\': \'Ash\', \'colors\': [\'Grijs\'], \'confidence\': 0.94}, {\'series\': \'Corso\', \'exact_color\': \'Hueso\', \'colors\': [\'Beige\'], \'confidence\': 0.91}, {\'series\': \'Craquel\xe9\', \'exact_color\': \'Perla Claro\', \'colors\': [\'Grijs\'], \'confidence\': 0.94}, {\'series\': \'Craquel\xe9\', \'exact_color\': \'Perla Medio\', \'colors\': [\'Grijs\'], \'confidence\': 0.84}, {\'series\': \'Craquel\xe9\', \'exact_color\': \'Perla Palido\', \'colors\': [\'Grijs\'], \'confidence\': 0.83}, {\'series\': \'Crayon\', \'exact_color\': \'Muscari\', \'colors\': [\'Blauw\'], \'confidence\': 0.94}, {\'series\': \'Croccante\', \'exact_color\': \'Araandano\', \'colors\': [\'Grijs\', \'Groen\'], \'confidence\': 0.8}, {\'series\': \'Croccante\', \'exact_color\': \'Avelle\', \'colors\': [\'Beige\'], \'confidence\': 0.95}, {\'series\': \'Delight\', \'exact_color\': \'Pearl\', \'colors\': [\'Beige\'], \'confidence\': 0.81}, {\'series\': \'Diamond\', \'exact_color\': \'Gold\', \'colors\': [\'Wit\', \'Beige\'], \'confidence\': 0.95}, {\'series\': \'Durst\', \'exact_color\': \'Maple\', \'colors\': [\'Beige\'], \'confidence\': 0.94}, {\'series\': \'Durst\', \'exact_color\': \'Oak\', \'colors\': [\'Bruin\'], \'confidence\': 0.93}, {\'series\': \'Elements\', \'exact_color\': \'Abyss\', \'colors\': [\'Blauw\'], \'confidence\': 0.99}, {\'series\': \'Elements\', \'exact_color\': \'Ember\', \'colors\': [\'Geel\', \'Oranje\'], \'confidence\': 0.9}, {\'series\': \'Elements\', \'exact_color\': \'Horizon\', \'colors\': [\'Blauw\'], \'confidence\': 0.99}, {\'series\': \'Elements\', \'exact_color\': \'Magma\', \'colors\': [\'Rood\'], \'confidence\': 0.99}, {\'series\': \'Elements\', \'exact_color\': \'Pure\', \'colors\': [\'Wit\', \'Beige\'], \'confidence\': 0.85}, {\'series\': \'Elements\', \'exact_color\': \'Terra\', \'colors\': [\'Rood\'], \'confidence\': 0.88}, {\'series\': \'Epoca\', \'exact_color\': \'Bone\', \'colors\': [\'Beige\'], \'confidence\': 0.91}, {\'series\': \'Escama\', \'exact_color\': \'Silver Sands\', \'colors\': [\'Beige\', \'Grijs\'], \'confidence\': 0.85}, {\'series\': \'Escama\', \'exact_color\': \'Snow Cap\', \'colors\': [\'Wit\'], \'confidence\': 0.99}, {\'series\': \'Escama\', \'exact_color\': \'Timberline\', \'colors\': [\'Grijs\'], \'confidence\': 0.82}, {\'series\': \'Escama\', \'exact_color\': \'Volc\xe1nico\', \'colors\': [\'Zwart\'], \'confidence\': 0.95}, {\'series\': \'Evoke\', \'exact_color\': \'Clay\', \'colors\': [\'Oranje\'], \'confidence\': 0.94}, {\'series\': \'Evoke\', \'exact_color\': \'Clear\', \'colors\': [\'Beige\'], \'confidence\': 0.98}, {\'series\': \'Evoke\', \'exact_color\': \'Dark\', \'colors\': [\'Grijs\'], \'confidence\': 0.96}, {\'series\': \'Fan\', \'exact_color\': \'Ash\', \'colors\': [\'Beige\'], \'confidence\': 0.94}, {\'series\': \'Fan\', \'exact_color\': \'Clay\', \'colors\': [\'Oranje\'], \'confidence\': 0.94}, {\'series\': \'Fan\', \'exact_color\': \'Clear\', \'colors\': [\'Beige\'], \'confidence\': 0.94}, {\'series\': \'Fan\', \'exact_color\': \'Dark\', \'colors\': [\'Grijs\'], \'confidence\': 0.96}, {\'series\': \'Fika\', \'exact_color\': \'Fossil\', \'colors\': [\'Beige\', \'Grijs\'], \'confidence\': 0.8}, {\'series\': \'Fluid\', \'exact_color\': \'Achillea\', \'colors\': [\'Grijs\'], \'confidence\': 0.94}, {\'series\': \'Fluid\', \'exact_color\': \'Giunco\', \'colors\': [\'Groen\'], \'confidence\': 0.94}, {\'series\': \'Fluid\', \'exact_color\': \'Muscari\', \'colors\': [\'Blauw\'], \'confidence\': 0.94}, {\'series\': \'Fluid\', \'exact_color\': \'Tulipano\', \'colors\': [\'Blauw\'], \'confidence\': 0.96}, {\'series\': \'Fuego\', \'exact_color\': \'Natural\', \'colors\': [\'Oranje\', \'Bruin\'], \'confidence\': 0.97}, {\'series\': \'Funky\', \'exact_color\': \'Bondi\', \'colors\': [\'Groen\', \'Blauw\'], \'confidence\': 0.9}, {\'series\': \'Funky\', \'exact_color\': \'Garden\', \'colors\': [\'Groen\'], \'confidence\': 0.99}, {\'series\': \'Funky\', \'exact_color\': \'Lollipop\', \'colors\': [\'Rood\'], \'confidence\': 0.99}, {\'series\': \'Funky\', \'exact_color\': \'Mintwood\', \'colors\': [\'Groen\'], \'confidence\': 0.99}, {\'series\': \'Funky\', \'exact_color\': \'Seaport\', \'colors\': [\'Blauw\'], \'confidence\': 0.99}, {\'series\': \'F\xe4rgblock\', \'exact_color\': \'Canella\', \'colors\': [\'Rood\'], \'confidence\': 0.96}, {\'series\': \'Garden\', \'exact_color\': \'Dark\', \'colors\': [\'Groen\', \'Grijs\'], \'confidence\': 0.91}, {\'series\': \'Garden\', \'exact_color\': \'Light\', \'colors\': [\'Groen\', \'Beige\'], \'confidence\': 0.92}, {\'series\': \'Genesi26\', \'exact_color\': \'Perla\', \'colors\': [\'Wit\'], \'confidence\': 0.88}, {\'series\': \'Goldfinger\', \'exact_color\': \'Metal\', \'colors\': [\'Zilver\'], \'confidence\': 0.99}, {\'series\': \'Groovy\', \'exact_color\': \'Bluejay\', \'colors\': [\'Blauw\'], \'confidence\': 0.94}, {\'series\': \'Groovy\', \'exact_color\': \'Formal Garden\', \'colors\': [\'Groen\'], \'confidence\': 0.94}, {\'series\': \'Groovy\', \'exact_color\': \'Sunset\', \'colors\': [\'Oranje\'], \'confidence\': 0.94}, {\'series\': \'Groovy\', \'exact_color\': \'Tiffanys\', \'colors\': [\'Groen\'], \'confidence\': 0.94}, {\'series\': \'Harlem\', \'exact_color\': \'Terra\', \'colors\': [\'Beige\'], \'confidence\': 0.93}, {\'series\': \'Hashi\', \'exact_color\': \'Camelia\', \'colors\': [\'Wit\'], \'confidence\': 0.94}, {\'series\': \'Hashi\', \'exact_color\': \'Fotinia\', \'colors\': [\'Oranje\'], \'confidence\': 0.94}, {\'series\': \'Hashi\', \'exact_color\': \'Giunco\', \'colors\': [\'Groen\'], \'confidence\': 0.94}, {\'series\': \'Hashi\', \'exact_color\': \'Iris\', \'colors\': [\'Blauw\'], \'confidence\': 0.94}, {\'series\': \'Hashi\', \'exact_color\': \'Loto\', \'colors\': [\'Beige\'], \'confidence\': 0.94}, {\'series\': \'Hashi\', \'exact_color\': \'Muscari\', \'colors\': [\'Blauw\'], \'confidence\': 0.94}, {\'series\': \'Hashi\', \'exact_color\': \'Primula\', \'colors\': [\'Geel\'], \'confidence\': 0.94}, {\'series\': \'Hashi\', \'exact_color\': \'Senecio\', \'colors\': [\'Grijs\'], \'confidence\': 0.94}, {\'series\': \'Hashi\', \'exact_color\': \'Tulipano\', \'colors\': [\'Groen\', \'Blauw\'], \'confidence\': 0.9}, {\'series\': \'Jarel\', \'exact_color\': \'Oak\', \'colors\': [\'Bruin\'], \'confidence\': 0.86}, {\'series\': \'Jazz\', \'exact_color\': \'Luz\', \'colors\': [\'Wit\', \'Beige\'], \'confidence\': 0.85}, {\'series\': \'Joyful\', \'exact_color\': \'Ash\', \'colors\': [\'Grijs\'], \'confidence\': 0.97}, {\'series\': \'Joyful\', \'exact_color\': \'Bone\', \'colors\': [\'Beige\'], \'confidence\': 0.98}, {\'series\': \'Joyful\', \'exact_color\': \'Lava\', \'colors\': [\'Zwart\'], \'confidence\': 0.99}, {\'series\': \'Joyful\', \'exact_color\': \'Steel\', \'colors\': [\'Grijs\'], \'confidence\': 0.99}, {\'series\': \'Kyoto\', \'exact_color\': \'Garden\', \'colors\': [\'Groen\'], \'confidence\': 0.85}, {\'series\': \'Kyoto\', \'exact_color\': \'Palace\', \'colors\': [\'Blauw\', \'Groen\'], \'confidence\': 0.85}, {\'series\': \'Kyoto\', \'exact_color\': \'River\', \'colors\': [\'Wit\', \'Blauw\'], \'confidence\': 0.85}, {\'series\': \'Laverton\', \'exact_color\': \'Natural\', \'colors\': [\'Oranje\', \'Bruin\'], \'confidence\': 0.97}, {\'series\': \'Lexa\', \'exact_color\': \'Pearl Brillo\', \'colors\': [\'Grijs\'], \'confidence\': 0.97}, {\'series\': \'Lingotti\', \'exact_color\': \'Ghiaccio\', \'colors\': [\'Grijs\'], \'confidence\': 0.97}, {\'series\': \'Lingotti\', \'exact_color\': \'Terra\', \'colors\': [\'Oranje\'], \'confidence\': 0.86}, {\'series\': \'Luca\', \'exact_color\': \'Lava\', \'colors\': [\'Bruin\', \'Oranje\'], \'confidence\': 0.9}, {\'series\': \'Luca\', \'exact_color\': \'Nacar\', \'colors\': [\'Grijs\'], \'confidence\': 0.9}, {\'series\': \'Lula\', \'exact_color\': \'Pearl\', \'colors\': [\'Grijs\'], \'confidence\': 0.8}, {\'series\': \'Madrid\', \'exact_color\': \'Avema Mate\', \'colors\': [\'Beige\'], \'confidence\': 0.95}, {\'series\': \'Madrid\', \'exact_color\': \'Luna Mate\', \'colors\': [\'Grijs\'], \'confidence\': 0.99}, {\'series\': \'Madrid Metro\', \'exact_color\': \'Oroval\', \'colors\': [\'Geel\'], \'confidence\': 0.99}, {\'series\': \'Malaga\', \'exact_color\': \'Azafata T-1\', \'colors\': [\'Groen\', \'Blauw\'], \'confidence\': 0.9}, {\'series\': \'Malaga\', \'exact_color\': \'Azafata T-2\', \'colors\': [\'Groen\', \'Blauw\'], \'confidence\': 0.9}, {\'series\': \'Malaga\', \'exact_color\': \'Bauxita\', \'colors\': [\'Bruin\'], \'confidence\': 0.99}, {\'series\': \'Malaga\', \'exact_color\': \'Craquele\', \'colors\': [\'Wit\'], \'confidence\': 0.95}, {\'series\': \'Malaga\', \'exact_color\': \'Glen\', \'colors\': [\'Groen\'], \'confidence\': 0.99}, {\'series\': \'Malaga\', \'exact_color\': \'Ravine\', \'colors\': [\'Groen\'], \'confidence\': 0.99}, {\'series\': \'Marble Line\', \'exact_color\': \'Gold Brillo\', \'colors\': [\'Wit\', \'Beige\'], \'confidence\': 0.95}, {\'series\': \'Marble Line\', \'exact_color\': \'Gold Mate\', \'colors\': [\'Wit\', \'Beige\'], \'confidence\': 0.95}, {\'series\': \'Marea\', \'exact_color\': \'Terra Matt\', \'colors\': [\'Oranje\'], \'confidence\': 0.96}, {\'series\': \'Maris\', \'exact_color\': \'Earth Haze\', \'colors\': [\'Beige\'], \'confidence\': 0.95}, {\'series\': \'Maris\', \'exact_color\': \'Mystic Night\', \'colors\': [\'Zwart\'], \'confidence\': 0.99}, {\'series\': \'Maris\', \'exact_color\': \'Soft Cloud\', \'colors\': [\'Grijs\'], \'confidence\': 0.99}, {\'series\': \'Marmorea\', \'exact_color\': \'Biancone\', \'colors\': [\'Beige\'], \'confidence\': 0.95}, {\'series\': \'Modulo\', \'exact_color\': \'Mattone\', \'colors\': [\'Oranje\'], \'confidence\': 0.94}, {\'series\': \'Modulo\', \'exact_color\': \'Polvere\', \'colors\': [\'Beige\'], \'confidence\': 0.88}, {\'series\': \'Muris\', \'exact_color\': \'Nix\', \'colors\': [\'Beige\'], \'confidence\': 0.99}, {\'series\': \'Muris\', \'exact_color\': \'Nocta\', \'colors\': [\'Grijs\'], \'confidence\': 0.94}, {\'series\': \'Muris\', \'exact_color\': \'Terra\', \'colors\': [\'Oranje\'], \'confidence\': 0.93}, {\'series\': \'Muris\', \'exact_color\': \'Vidri\', \'colors\': [\'Groen\'], \'confidence\': 0.99}, {\'series\': \'Nala\', \'exact_color\': \'Pearl\', \'colors\': [\'Grijs\'], \'confidence\': 0.98}, {\'series\': \'Neri\', \'exact_color\': \'Silver Mist\', \'colors\': [\'Grijs\'], \'confidence\': 0.99}, {\'series\': \'New Cotto\', \'exact_color\': \'Pearl Brillo\', \'colors\': [\'Grijs\'], \'confidence\': 0.89}, {\'series\': \'Node\', \'exact_color\': \'Bone\', \'colors\': [\'Beige\'], \'confidence\': 0.84}, {\'series\': \'Nomade\', \'exact_color\': \'Bone\', \'colors\': [\'Beige\'], \'confidence\': 0.93}, {\'series\': \'Nomade\', \'exact_color\': \'Pearl\', \'colors\': [\'Wit\'], \'confidence\': 0.98}, {\'series\': \'Pigmento\', \'exact_color\': \'Terra Matt\', \'colors\': [\'Oranje\'], \'confidence\': 0.9}, {\'series\': \'Pool Porc.\', \'exact_color\': \'Luz\', \'colors\': [\'Wit\', \'Beige\'], \'confidence\': 0.9}, {\'series\': \'Pop Tile\', \'exact_color\': \'Nacar\', \'colors\': [\'Wit\'], \'confidence\': 0.96}, {\'series\': \'Pop Tile\', \'exact_color\': \'N\xe1car\', \'colors\': [\'Wit\'], \'confidence\': 0.96}, {\'series\': \'Potters\', \'exact_color\': \'Fossil\', \'colors\': [\'Beige\'], \'confidence\': 0.88}, {\'series\': \'Pottery\', \'exact_color\': \'Natural\', \'colors\': [\'Beige\'], \'confidence\': 0.96}, {\'series\': \'Pradolongo\', \'exact_color\': \'Pearl\', \'colors\': [\'Grijs\'], \'confidence\': 0.92}, {\'series\': \'Puck\', \'exact_color\': \'Pearl\', \'colors\': [\'Grijs\'], \'confidence\': 0.98}, {\'series\': \'Re-Bel\', \'exact_color\': \'Cuivre\', \'colors\': [\'Beige\', \'Bruin\'], \'confidence\': 0.94}, {\'series\': \'Re-Bel\', \'exact_color\': \'Or\', \'colors\': [\'Wit\', \'Grijs\'], \'confidence\': 0.92}, {\'series\': \'Re-Bel\', \'exact_color\': \'Perle\', \'colors\': [\'Wit\'], \'confidence\': 0.96}, {\'series\': \'Retiro\', \'exact_color\': \'Colonial Brillo\', \'colors\': [\'Beige\'], \'confidence\': 0.8}, {\'series\': \'Retiro\', \'exact_color\': \'Marina Brillo\', \'colors\': [\'Blauw\'], \'confidence\': 0.99}, {\'series\': \'Retiro\', \'exact_color\': \'Titanio Brillo\', \'colors\': [\'Grijs\'], \'confidence\': 0.99}, {\'series\': \'Ribe-R\', \'exact_color\': \'Natural\', \'colors\': [\'Beige\', \'Bruin\'], \'confidence\': 0.95}, {\'series\': \'Ritmo\', \'exact_color\': \'Bronce Oxidado\', \'colors\': [\'Groen\', \'Beige\'], \'confidence\': 0.95}, {\'series\': \'Ritmo\', \'exact_color\': \'Mostaza Oro Viejo\', \'colors\': [\'Geel\', \'Beige\'], \'confidence\': 0.93}, {\'series\': \'Ritmo\', \'exact_color\': \'Rojizo Cobre\', \'colors\': [\'Roze\', \'Beige\'], \'confidence\': 0.88}, {\'series\': \'Rock Star\', \'exact_color\': \'Gold\', \'colors\': [\'Wit\', \'Grijs\'], \'confidence\': 0.95}, {\'series\': \'Root\', \'exact_color\': \'Bold\', \'colors\': [\'Bruin\'], \'confidence\': 0.91}, {\'series\': \'Root\', \'exact_color\': \'Chipper\', \'colors\': [\'Bruin\'], \'confidence\': 0.91}, {\'series\': \'Root\', \'exact_color\': \'Mellow\', \'colors\': [\'Beige\'], \'confidence\': 0.91}, {\'series\': \'Root\', \'exact_color\': \'Pearl\', \'colors\': [\'Beige\'], \'confidence\': 0.97}, {\'series\': \'SAFARI\', \'exact_color\': \'Bruciato\', \'colors\': [\'Bruin\'], \'confidence\': 0.88}, {\'series\': \'Salerno-R\', \'exact_color\': \'Bold\', \'colors\': [\'Bruin\'], \'confidence\': 0.91}, {\'series\': \'Salerno-R\', \'exact_color\': \'Chipper\', \'colors\': [\'Bruin\'], \'confidence\': 0.91}, {\'series\': \'Salerno-R\', \'exact_color\': \'Mellow\', \'colors\': [\'Beige\'], \'confidence\': 0.91}, {\'series\': \'Seine\', \'exact_color\': \'Natural\', \'colors\': [\'Bruin\'], \'confidence\': 0.98}, {\'series\': \'Sentier\', \'exact_color\': \'Bone\', \'colors\': [\'Beige\'], \'confidence\': 0.95}, {\'series\': \'Sentier\', \'exact_color\': \'Light\', \'colors\': [\'Beige\'], \'confidence\': 0.95}, {\'series\': \'Sentier\', \'exact_color\': \'Natural\', \'colors\': [\'Beige\'], \'confidence\': 0.94}, {\'series\': \'Souk\', \'exact_color\': \'Bone\', \'colors\': [\'Beige\'], \'confidence\': 0.98}, {\'series\': \'Stracciatella\', \'exact_color\': \'Nacar\', \'colors\': [\'Wit\'], \'confidence\': 0.94}, {\'series\': \'Stripes\', \'exact_color\': \'Dove Matt\', \'colors\': [\'Grijs\'], \'confidence\': 0.9}, {\'series\': \'Studio\', \'exact_color\': \'Silver Sands\', \'colors\': [\'Grijs\', \'Beige\'], \'confidence\': 0.85}, {\'series\': \'Studio\', \'exact_color\': \'SilverSands\', \'colors\': [\'Grijs\', \'Beige\'], \'confidence\': 0.85}, {\'series\': \'Studio\', \'exact_color\': \'Snow Cap\', \'colors\': [\'Wit\'], \'confidence\': 0.99}, {\'series\': \'Studio\', \'exact_color\': \'Timberline\', \'colors\': [\'Grijs\'], \'confidence\': 0.78}, {\'series\': \'Studio\', \'exact_color\': \'Volcanico\', \'colors\': [\'Zwart\'], \'confidence\': 0.96}, {\'series\': \'Studio\', \'exact_color\': \'Volc\xe1nico\', \'colors\': [\'Zwart\'], \'confidence\': 0.95}, {\'series\': \'Svenka\', \'exact_color\': \'Bone\', \'colors\': [\'Beige\'], \'confidence\': 0.94}, {\'series\': \'Sweet Bars\', \'exact_color\': \'Berry Matt\', \'colors\': [\'Rood\', \'Roze\'], \'confidence\': 0.85}, {\'series\': \'Sweet Bars\', \'exact_color\': \'Tan Matt\', \'colors\': [\'Oranje\'], \'confidence\': 0.82}, {\'series\': \'Tanger Mate\', \'exact_color\': \'Tiffany\', \'colors\': [\'Groen\', \'Blauw\'], \'confidence\': 0.85}, {\'series\': \'Tivoli-R\', \'exact_color\': \'Canella\', \'colors\': [\'Bruin\'], \'confidence\': 0.88}, {\'series\': \'Travento\', \'exact_color\': \'Pearl\', \'colors\': [\'Wit\'], \'confidence\': 0.89}, {\'series\': \'Vodevil\', \'exact_color\': \'Nac\xe1r\', \'colors\': [\'Wit\'], \'confidence\': 0.92}, {\'series\': \'Volume\', \'exact_color\': \'Nacar Brillo\', \'colors\': [\'Grijs\'], \'confidence\': 0.88}, {\'series\': \'Wabisabi\', \'exact_color\': \'Ghiaccio\', \'colors\': [\'Grijs\'], \'confidence\': 0.96}, {\'series\': \'Wabisabi\', \'exact_color\': \'Terra\', \'colors\': [\'Oranje\'], \'confidence\': 0.83}, {\'series\': \'Waves\', \'exact_color\': \'Micro Chip\', \'colors\': [\'Grijs\'], \'confidence\': 0.94}, {\'series\': \'Waves\', \'exact_color\': \'Periscope\', \'colors\': [\'Grijs\'], \'confidence\': 0.94}, {\'series\': \'Yuri\', \'exact_color\': \'Caldera\', \'colors\': [\'Bruin\'], \'confidence\': 0.95}, {\'series\': \'Zelij\', \'exact_color\': \'Hueso 1010\', \'colors\': [\'Beige\'], \'confidence\': 0.93}, {\'series\': \'Zelij\', \'exact_color\': \'Pergamon\', \'colors\': [\'Beige\'], \'confidence\': 0.95}, {\'series\': \'Zelij\', \'exact_color\': \'Via Lactea\', \'colors\': [\'Wit\', \'Blauw\'], \'confidence\': 0.85}, {\'series\': \'Zero\', \'exact_color\': \'Bold\', \'colors\': [\'Bruin\'], \'confidence\': 0.91}, {\'series\': \'Zero\', \'exact_color\': \'Chipper\', \'colors\': [\'Bruin\'], \'confidence\': 0.91}, {\'series\': \'Zero\', \'exact_color\': \'Mellow\', \'colors\': [\'Beige\'], \'confidence\': 0.91}, {\'series\': \'Zero\', \'exact_color\': \'Pearl\', \'colors\': [\'Beige\'], \'confidence\': 0.97}, {\'series\': \'Zero Origo\', \'exact_color\': \'Pearl\', \'colors\': [\'Beige\'], \'confidence\': 0.97}, {\'series\': \'Zero-R\', \'exact_color\': \'Bold\', \'colors\': [\'Bruin\'], \'confidence\': 0.91}, {\'series\': \'Zero-R\', \'exact_color\': \'Chipper\', \'colors\': [\'Bruin\'], \'confidence\': 0.91}, {\'series\': \'Zero-R\', \'exact_color\': \'Mellow\', \'colors\': [\'Beige\'], \'confidence\': 0.91}]\nMARKER = \'# BC_COTTO_VISUAL_COLORS_V1\'\n\nHELPERS = \'\'\'\n# BC_COTTO_VISUAL_COLORS_V1\ndef _bc_cotto_expected_color(doc):\n    rules = _BC_SIMPLE_COLORS[\'COTTO_VISUAL_SCOPED_RULES\']\n    normalize_color = _BC_SIMPLE_COLORS[\'normalize\']\n    normalize_series_color = _BC_SIMPLE_COLORS[\'normalize_series\']\n    if normalize_color(doc.get(\'vendor\')) != \'cottoceramix\' or not _bc_acero_is_tile(doc):\n        return None\n    raw = doc.get(\'f_kleur_exact\')\n    series = _bc_simple_strings(doc.get(\'f_serie\')) or _bc_simple_strings(doc.get(\'series\'))\n    if not isinstance(raw, str) or len(series) != 1:\n        return None\n    return rules.get((normalize_series_color(series[0]), normalize_color(raw)))\n\ndef _bc_cotto_targets(docs):\n    return [doc for doc in docs if _bc_cotto_expected_color(doc) is not None]\n\ndef _bc_cotto_check(docs):\n    return all(doc.get(\'f_kleur\') == _bc_cotto_expected_color(doc)\n               for doc in _bc_cotto_targets(docs))\n\'\'\'\n\n\ndef _sha(source):\n    return hashlib.sha256(source.encode(\'utf-8\')).hexdigest()\n\n\ndef _replace_once(source, old, new):\n    if source.count(old) != 1:\n        raise RuntimeError(\'Cotto-kleurhook ontbreekt of is niet uniek\')\n    return source.replace(old, new, 1)\n\n\ndef _offsets(source, node):\n    lines = source.splitlines(keepends=True)\n    start = len(\'\'.join(lines[:node.lineno - 1])) + len(lines[node.lineno - 1].encode()[:node.col_offset].decode())\n    end = len(\'\'.join(lines[:node.end_lineno - 1])) + len(lines[node.end_lineno - 1].encode()[:node.end_col_offset].decode())\n    return start, end\n\n\ndef reviewed_rule_map(rules, namespace):\n    if not isinstance(rules, list) or not rules:\n        raise RuntimeError(\'Een niet-lege lijst beoordeelde Cotto-kleurregels is vereist\')\n    normalize_color = namespace[\'normalize\']\n    normalize_series_color = namespace[\'normalize_series\']\n    taxonomy = namespace[\'TAXONOMY\']\n    owners = {(normalize_color(v), normalize_series_color(s), normalize_color(raw)): colors\n              for v, s, raw, colors, _primary in namespace[\'OWNER_RULES\']}\n    result = {}\n    for rule in rules:\n        if (not isinstance(rule, dict) or not isinstance(rule.get(\'series\'), str)\n                or not isinstance(rule.get(\'exact_color\'), str)\n                or not rule[\'series\'].strip() or not rule[\'exact_color\'].strip()):\n            raise RuntimeError(\'Kleurregels vereisen een exacte serie en bronkleur\')\n        confidence = rule.get(\'confidence\')\n        if (isinstance(confidence, bool) or not isinstance(confidence, (int, float))\n                or not .70 <= confidence <= 1):\n            raise RuntimeError(\'Visuele kleurregel mist voldoende vastgelegde zekerheid\')\n        colors = rule.get(\'colors\')\n        if (not isinstance(colors, list) or not colors\n                or any(not isinstance(color, str) or color not in taxonomy for color in colors)\n                or len(colors) != len(set(colors))):\n            raise RuntimeError(\'Visuele kleurregel bevat ongeldige basiskleuren\')\n        ordered = [color for color in taxonomy if color in colors]\n        key = (normalize_series_color(rule[\'series\']), normalize_color(rule[\'exact_color\']))\n        if key in result and result[key] != ordered:\n            raise RuntimeError(\'Tegenstrijdige Cotto-regels na normalisatie van serie/kleur: \' + \' / \'.join(key))\n        owner = owners.get((\'cottoceramix\', *key))\n        if owner is not None and set(owner) != set(ordered):\n            raise RuntimeError(\'Visuele kleurregel strijdt met een expliciete eigenaarregel\')\n        if key[1] == \'acero\' and ordered != [\'Grijs\']:\n            raise RuntimeError(\'De bevestigde Acero-regel moet behouden blijven\')\n        result[key] = ordered\n    return dict(sorted(result.items()))\n\n\ndef patch_cotto_worker(source):\n    if not isinstance(source, str):\n        raise RuntimeError(\'Workerbron moet tekst zijn\')\n    if MARKER in source:\n        if source.count(MARKER) != 1 or not PATCHED_WORKER_SHA256 or _sha(source) != PATCHED_WORKER_SHA256:\n            raise RuntimeError(\'Bestaande Cotto-kleurcorrectie wijkt af; niets gewijzigd\')\n        compile(source, \'<existing-cotto-worker>\', \'exec\')\n        return source\n    if _sha(source) != BASE_WORKER_SHA256:\n        raise RuntimeError(\'Worker wijkt af van de beoordeelde liveversie\')\n    tree = ast.parse(source)\n    literals = [node.args[0] for node in ast.walk(tree)\n                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)\n                and node.func.id == \'compile\' and len(node.args) >= 3\n                and isinstance(node.args[1], ast.Constant) and node.args[1].value == \'<derived-color-rules>\'\n                and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str)]\n    if len(literals) != 1:\n        raise RuntimeError(\'Geen unieke afgeleide kleurmodule\')\n    literal = literals[0]\n    namespace = {\'__name__\': \'reviewed_cotto_color_source\'}\n    exec(compile(literal.value, \'<reviewed-cotto-color-source>\', \'exec\'), namespace)\n    rules = reviewed_rule_map(SCOPED_RULES, namespace)\n    colors = _replace_once(literal.value,\n        \'\\ndef classify_color(raw, context=None):\\n\',\n        \'\\nCOTTO_VISUAL_SCOPED_RULES = \' + repr(rules) + \'\\n\\ndef classify_color(raw, context=None):\\n\')\n    colors = _replace_once(colors,\n        "    if vendor == \'porcelanosa\' and s == \'caliza\':\\n",\n        "    if vendor == \'cottoceramix\' and ctx.get(\'is_tile\') is True and ctx.get(\'cotto_explicit_series\') is True:\\n"\n        "        visual = COTTO_VISUAL_SCOPED_RULES.get((series, s))\\n"\n        "        if visual is not None:\\n"\n        "            return _result(raw, visual, \'INFERRED_VISUAL\', \'Reviewed exact series/color product swatch; manufacturer name retained.\')\\n"\n        "    if vendor == \'porcelanosa\' and s == \'caliza\':\\n")\n    colors = _replace_once(colors,\n        "    series_values = _strings(doc.get(\'f_serie\')) or _strings(doc.get(\'series\'))\\n",\n        "    series_values = _strings(doc.get(\'f_serie\')) or _strings(doc.get(\'series\'))\\n"\n        "    cotto_explicit_series = len(series_values) == 1\\n")\n    old_context = "return [{\'vendor\': vendor, \'series\': s, \'is_tile\': doc.get(\'_bc_tile_color_context\') is True} for s in series_values] if len(series_values) == 1 else [{\'vendor\': vendor, \'is_tile\': doc.get(\'_bc_tile_color_context\') is True}]"\n    new_context = "return [{\'vendor\': vendor, \'series\': s, \'is_tile\': doc.get(\'_bc_tile_color_context\') is True, \'cotto_explicit_series\': cotto_explicit_series} for s in series_values] if len(series_values) == 1 else [{\'vendor\': vendor, \'is_tile\': doc.get(\'_bc_tile_color_context\') is True, \'cotto_explicit_series\': False}]"\n    colors = _replace_once(colors, old_context, new_context)\n    compile(colors, \'<cotto-visual-color-rules>\', \'exec\')\n    start, end = _offsets(source, literal)\n    result = source[:start] + repr(colors) + source[end:]\n    tree = ast.parse(result)\n    snapshots = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == \'_bc_simple_snapshot\']\n    checks = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == \'check_b2c_profiles\']\n    guards = [node for node in tree.body if isinstance(node, ast.If) and ast.unparse(node.test) == "__name__ == \'__main__\'"]\n    if len(snapshots) != 1 or len(checks) != 2 or len(guards) != 1:\n        raise RuntimeError(\'Verwachte bestaande workerhooks verschillen\')\n    check = checks[-1]\n    returns = [node for node in check.body if isinstance(node, ast.Return)]\n    if len(returns) != 1 or check.body[-1] is not returns[0]:\n        raise RuntimeError(\'Geen unieke eindcontrole voor filters\')\n    lines = result.splitlines(keepends=True)\n    positions = [\n        (sum(len(line) for line in lines[:snapshots[0].end_lineno]),\n         "    if not _bc_cotto_check(docs):\\n"\n         "        raise RuntimeError(\'Cotto-tegelkleuren voldoen niet aan beoordeelde serieregels\')\\n"\n         "    snapshot[\'cotto_visual_colors_v1\'] = True\\n"\n         "    snapshot[\'cotto_visual_color_products\'] = len(_bc_cotto_targets(docs))\\n"),\n        (sum(len(line) for line in lines[:returns[0].lineno - 1]),\n         "    checks.append({\'name\': \'Cotto-seriekleuren volgen beoordeelde productstalen; bronkleur behouden\',\\n"\n         "                   \'passed\': snapshot.get(\'cotto_visual_colors_v1\') is True and _bc_cotto_check(docs),\\n"\n         "                   \'products\': len(_bc_cotto_targets(docs))})\\n"),\n        (sum(len(line) for line in lines[:guards[0].lineno - 1]), HELPERS.rstrip() + \'\\n\\n\'),\n    ]\n    for position, text in sorted(positions, reverse=True):\n        result = result[:position] + text + result[position:]\n    if result.count(MARKER) != 1:\n        raise RuntimeError(\'Cotto-kleurcorrectie niet eenduidig toegevoegd\')\n    compile(result, \'<cotto-color-corrected-worker>\', \'exec\')\n    return result\n'}
TARGET_WORKER_SHA256 = 'cc13abd05c87a490bf06d0a7358ef36bc700edc0a736a48714d704df62f8dcc2'
TARGET_API_SHA256 = '3a7701134be7ac55b0a83436ceb16ebb19ac0a88aba17c283490f90047f02094'
TARGET_API_AST_SHA256 = '4b4dcf726b3f66f06d5f62bc322c8a9a236459ddf32cf56a2440e4c10147570b'
BASE_WORKER_SHA256 = '3c6dd21f50081f4ad8d770194dc35a97c101a09910dd8892403e51b93f1495eb'
BASE_API_SHA256 = '3a7701134be7ac55b0a83436ceb16ebb19ac0a88aba17c283490f90047f02094'
BASE_API_AST_SHA256 = '4b4dcf726b3f66f06d5f62bc322c8a9a236459ddf32cf56a2440e4c10147570b'
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
    # A color-only update must not rewrite even whitespace in the API source.
    return sha256(source) == BASE_API_SHA256


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
        raise RuntimeError('Worker verschilt van de beoordeelde huidige versie')
    if set(patch_sources) != {'worker'}:
        raise RuntimeError('Cotto-kleurcorrectie bevat uitsluitend een workerpatch')
    namespace = {'__name__': 'bc_cotto_worker_patch'}
    exec(compile(patch_sources['worker'], '<reviewed-cotto-worker-patch>', 'exec'), namespace)
    result = namespace['patch_cotto_worker'](source.decode('utf-8'))
    compile(result, '<cotto-corrected-search-worker>', 'exec')
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
    if not isinstance(patch_sources, dict) or set(patch_sources) != {'worker'}:
        raise RuntimeError('Gebruik het complete gepubliceerde reparatiepakket')
    worker_path = root / 'sync.py'
    app_path = live / 'app.py'
    snapshot_path = live / 'bc_sync/active.json'
    original_worker = read_regular(worker_path)
    original_app = read_regular(app_path)
    if (TARGET_WORKER_SHA256 and sha256(original_worker) == TARGET_WORKER_SHA256 and
            TARGET_API_SHA256 and sha256(original_app) == TARGET_API_SHA256):
        snapshot = json.loads(read_regular(snapshot_path))
        if (snapshot.get('variant_aliases_v1') is not True or
                snapshot.get('filter_simplification_v1') is not True or
                snapshot.get('tile_format_codes_v1') is not True or
                snapshot.get('acero_gray_v1') is not True or
                snapshot.get('cotto_visual_colors_v1') is not True):
            raise RuntimeError('Gepatchte code gevonden zonder bevestigde filterindex')
        current = worker_factory(original_worker)
        health, _ = current.probe('http://127.0.0.1:8082/health')
        if health.get('ok') is not True or health.get('typesense_collection') != snapshot['collection']:
            raise RuntimeError('Gepatchte code gevonden; actieve zoekservice is nog niet bevestigd')
        _, timer_state = systemctl('is-active', TIMER)
        say('COTTO-KLEURCORRECTIE WAS AL TOEGEPAST | collectie: ' + snapshot['collection'])
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
    if expected_api != original_app:
        raise RuntimeError('Cotto-kleurcorrectie mag de bestaande API-bron niet wijzigen')
    if TARGET_API_SHA256 and sha256(expected_api) != TARGET_API_SHA256:
        raise RuntimeError('Cotto-kleurcorrectie heeft een afwijkende API-hash')
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
            if candidate_snapshot.get('acero_gray_v1') is not True:
                raise RuntimeError('Voorbereide index mist de Acero-naar-Grijs-correctie')
            if candidate_snapshot.get('cotto_visual_colors_v1') is not True:
                raise RuntimeError('Voorbereide index mist de beoordeelde Cotto-kleurregels')
            phase[0] = 'gecontroleerde index activeren'
            snapshot = worker.activate(shop, ts, staged)
            if (snapshot.get('variant_aliases_v1') is not True or
                    snapshot.get('filter_simplification_v1') is not True or
                    snapshot.get('tile_format_codes_v1') is not True or
                    snapshot.get('acero_gray_v1') is not True or
                    snapshot.get('cotto_visual_colors_v1') is not True):
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
                       'filter_simplification_v1': True, 'tile_format_codes_v1': True,
                       'acero_gray_v1': True, 'acero_gray_products': snapshot.get('acero_gray_products'),
                       'cotto_visual_colors_v1': True,
                       'cotto_visual_color_products': snapshot.get('cotto_visual_color_products')}
            write_atomic(backup / 'REPAIR_RESULT.json', json.dumps(summary, indent=2).encode())
            say('COTTO-KLEUREN GECORRIGEERD | ' + str(report['products']) + ' producten | ' + str(report['profiles']) + ' profielen')
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
