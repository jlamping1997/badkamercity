"""Guarded, catalog-free Cottoceramix visual color corrections.

The release builder freezes reviewed rules and the resulting worker hash.
Manufacturer fields, existing owner rules, API source and size codes are kept.
"""
import ast
import hashlib

BASE_WORKER_SHA256 = '3c6dd21f50081f4ad8d770194dc35a97c101a09910dd8892403e51b93f1495eb'
PATCHED_WORKER_SHA256 = 'cc13abd05c87a490bf06d0a7358ef36bc700edc0a736a48714d704df62f8dcc2'
SCOPED_RULES = [{'series': '3D Bars', 'exact_color': 'Onix Gloss', 'colors': ['Zwart'], 'confidence': 0.98}, {'series': '3D Bars', 'exact_color': 'Onix Matt', 'colors': ['Zwart'], 'confidence': 0.94}, {'series': '3D Bars', 'exact_color': 'Quartz Gloss', 'colors': ['Wit'], 'confidence': 0.96}, {'series': '3D Bars', 'exact_color': 'Quartz Matt', 'colors': ['Wit'], 'confidence': 0.96}, {'series': '3D Bars', 'exact_color': 'Topaz Matt', 'colors': ['Beige'], 'confidence': 0.93}, {'series': 'Alma Scale', 'exact_color': 'Pearl', 'colors': ['Grijs'], 'confidence': 0.98}, {'series': 'Alter Ego', 'exact_color': 'Bruciato', 'colors': ['Bruin'], 'confidence': 0.94}, {'series': 'Alter Ego', 'exact_color': 'Sbiancato', 'colors': ['Beige'], 'confidence': 0.95}, {'series': 'Alure Scale', 'exact_color': 'Pearl', 'colors': ['Grijs'], 'confidence': 0.98}, {'series': 'Arabesco', 'exact_color': 'Silver Mist', 'colors': ['Grijs'], 'confidence': 0.9}, {'series': 'Arabesco', 'exact_color': 'Silver Sands', 'colors': ['Grijs', 'Beige'], 'confidence': 0.85}, {'series': 'Arabesco', 'exact_color': 'Snow Cap', 'colors': ['Wit'], 'confidence': 0.92}, {'series': 'Arabesco', 'exact_color': 'Timberline', 'colors': ['Grijs'], 'confidence': 0.76}, {'series': 'Arabesco', 'exact_color': 'Volcánico', 'colors': ['Zwart'], 'confidence': 0.97}, {'series': 'Argillae', 'exact_color': 'Gobi', 'colors': ['Oranje'], 'confidence': 0.88}, {'series': 'Argillae', 'exact_color': 'Nocta', 'colors': ['Zwart'], 'confidence': 0.94}, {'series': 'Argillae', 'exact_color': 'Terra', 'colors': ['Oranje'], 'confidence': 0.88}, {'series': 'Arka', 'exact_color': 'Bone', 'colors': ['Beige'], 'confidence': 0.96}, {'series': 'Arka', 'exact_color': 'Steel', 'colors': ['Grijs'], 'confidence': 0.9}, {'series': 'Attico', 'exact_color': 'Natural', 'colors': ['Beige'], 'confidence': 0.97}, {'series': 'Bejmat', 'exact_color': 'Tan Matt', 'colors': ['Oranje'], 'confidence': 0.86}, {'series': 'Belgium Stone', 'exact_color': 'Dark', 'colors': ['Grijs'], 'confidence': 0.96}, {'series': 'Benasal', 'exact_color': 'Caldera', 'colors': ['Bruin'], 'confidence': 0.88}, {'series': 'Bloom-R', 'exact_color': 'Bold', 'colors': ['Bruin'], 'confidence': 0.91}, {'series': 'Bloom-R', 'exact_color': 'Chipper', 'colors': ['Bruin'], 'confidence': 0.91}, {'series': 'Bloom-R', 'exact_color': 'Mellow', 'colors': ['Beige'], 'confidence': 0.91}, {'series': 'Boston', 'exact_color': 'Day', 'colors': ['Beige'], 'confidence': 0.93}, {'series': 'Boston', 'exact_color': 'Downtown', 'colors': ['Wit', 'Beige'], 'confidence': 0.88}, {'series': 'Boston', 'exact_color': 'East', 'colors': ['Beige'], 'confidence': 0.93}, {'series': 'Boston', 'exact_color': 'North', 'colors': ['Bruin', 'Oranje'], 'confidence': 0.88}, {'series': 'Boston', 'exact_color': 'South', 'colors': ['Bruin'], 'confidence': 0.93}, {'series': 'Boston', 'exact_color': 'West', 'colors': ['Grijs', 'Bruin'], 'confidence': 0.88}, {'series': 'Boubles', 'exact_color': 'Dark', 'colors': ['Grijs'], 'confidence': 0.93}, {'series': 'Boubles', 'exact_color': 'Terra', 'colors': ['Bruin'], 'confidence': 0.95}, {'series': 'Casablanca', 'exact_color': 'Adobe', 'colors': ['Oranje'], 'confidence': 0.86}, {'series': 'Casablanca', 'exact_color': 'Ash', 'colors': ['Beige'], 'confidence': 0.86}, {'series': 'Casablanca', 'exact_color': 'Water', 'colors': ['Groen', 'Blauw'], 'confidence': 0.9}, {'series': 'Casetone', 'exact_color': 'Oak', 'colors': ['Beige'], 'confidence': 0.91}, {'series': 'Ceppo di Gre', 'exact_color': 'Natural', 'colors': ['Beige', 'Grijs'], 'confidence': 0.86}, {'series': 'Cool', 'exact_color': 'Ash', 'colors': ['Grijs'], 'confidence': 0.94}, {'series': 'Corso', 'exact_color': 'Hueso', 'colors': ['Beige'], 'confidence': 0.91}, {'series': 'Craquelé', 'exact_color': 'Perla Claro', 'colors': ['Grijs'], 'confidence': 0.94}, {'series': 'Craquelé', 'exact_color': 'Perla Medio', 'colors': ['Grijs'], 'confidence': 0.84}, {'series': 'Craquelé', 'exact_color': 'Perla Palido', 'colors': ['Grijs'], 'confidence': 0.83}, {'series': 'Crayon', 'exact_color': 'Muscari', 'colors': ['Blauw'], 'confidence': 0.94}, {'series': 'Croccante', 'exact_color': 'Araandano', 'colors': ['Grijs', 'Groen'], 'confidence': 0.8}, {'series': 'Croccante', 'exact_color': 'Avelle', 'colors': ['Beige'], 'confidence': 0.95}, {'series': 'Delight', 'exact_color': 'Pearl', 'colors': ['Beige'], 'confidence': 0.81}, {'series': 'Diamond', 'exact_color': 'Gold', 'colors': ['Wit', 'Beige'], 'confidence': 0.95}, {'series': 'Durst', 'exact_color': 'Maple', 'colors': ['Beige'], 'confidence': 0.94}, {'series': 'Durst', 'exact_color': 'Oak', 'colors': ['Bruin'], 'confidence': 0.93}, {'series': 'Elements', 'exact_color': 'Abyss', 'colors': ['Blauw'], 'confidence': 0.99}, {'series': 'Elements', 'exact_color': 'Ember', 'colors': ['Geel', 'Oranje'], 'confidence': 0.9}, {'series': 'Elements', 'exact_color': 'Horizon', 'colors': ['Blauw'], 'confidence': 0.99}, {'series': 'Elements', 'exact_color': 'Magma', 'colors': ['Rood'], 'confidence': 0.99}, {'series': 'Elements', 'exact_color': 'Pure', 'colors': ['Wit', 'Beige'], 'confidence': 0.85}, {'series': 'Elements', 'exact_color': 'Terra', 'colors': ['Rood'], 'confidence': 0.88}, {'series': 'Epoca', 'exact_color': 'Bone', 'colors': ['Beige'], 'confidence': 0.91}, {'series': 'Escama', 'exact_color': 'Silver Sands', 'colors': ['Beige', 'Grijs'], 'confidence': 0.85}, {'series': 'Escama', 'exact_color': 'Snow Cap', 'colors': ['Wit'], 'confidence': 0.99}, {'series': 'Escama', 'exact_color': 'Timberline', 'colors': ['Grijs'], 'confidence': 0.82}, {'series': 'Escama', 'exact_color': 'Volcánico', 'colors': ['Zwart'], 'confidence': 0.95}, {'series': 'Evoke', 'exact_color': 'Clay', 'colors': ['Oranje'], 'confidence': 0.94}, {'series': 'Evoke', 'exact_color': 'Clear', 'colors': ['Beige'], 'confidence': 0.98}, {'series': 'Evoke', 'exact_color': 'Dark', 'colors': ['Grijs'], 'confidence': 0.96}, {'series': 'Fan', 'exact_color': 'Ash', 'colors': ['Beige'], 'confidence': 0.94}, {'series': 'Fan', 'exact_color': 'Clay', 'colors': ['Oranje'], 'confidence': 0.94}, {'series': 'Fan', 'exact_color': 'Clear', 'colors': ['Beige'], 'confidence': 0.94}, {'series': 'Fan', 'exact_color': 'Dark', 'colors': ['Grijs'], 'confidence': 0.96}, {'series': 'Fika', 'exact_color': 'Fossil', 'colors': ['Beige', 'Grijs'], 'confidence': 0.8}, {'series': 'Fluid', 'exact_color': 'Achillea', 'colors': ['Grijs'], 'confidence': 0.94}, {'series': 'Fluid', 'exact_color': 'Giunco', 'colors': ['Groen'], 'confidence': 0.94}, {'series': 'Fluid', 'exact_color': 'Muscari', 'colors': ['Blauw'], 'confidence': 0.94}, {'series': 'Fluid', 'exact_color': 'Tulipano', 'colors': ['Blauw'], 'confidence': 0.96}, {'series': 'Fuego', 'exact_color': 'Natural', 'colors': ['Oranje', 'Bruin'], 'confidence': 0.97}, {'series': 'Funky', 'exact_color': 'Bondi', 'colors': ['Groen', 'Blauw'], 'confidence': 0.9}, {'series': 'Funky', 'exact_color': 'Garden', 'colors': ['Groen'], 'confidence': 0.99}, {'series': 'Funky', 'exact_color': 'Lollipop', 'colors': ['Rood'], 'confidence': 0.99}, {'series': 'Funky', 'exact_color': 'Mintwood', 'colors': ['Groen'], 'confidence': 0.99}, {'series': 'Funky', 'exact_color': 'Seaport', 'colors': ['Blauw'], 'confidence': 0.99}, {'series': 'Färgblock', 'exact_color': 'Canella', 'colors': ['Rood'], 'confidence': 0.96}, {'series': 'Garden', 'exact_color': 'Dark', 'colors': ['Groen', 'Grijs'], 'confidence': 0.91}, {'series': 'Garden', 'exact_color': 'Light', 'colors': ['Groen', 'Beige'], 'confidence': 0.92}, {'series': 'Genesi26', 'exact_color': 'Perla', 'colors': ['Wit'], 'confidence': 0.88}, {'series': 'Goldfinger', 'exact_color': 'Metal', 'colors': ['Zilver'], 'confidence': 0.99}, {'series': 'Groovy', 'exact_color': 'Bluejay', 'colors': ['Blauw'], 'confidence': 0.94}, {'series': 'Groovy', 'exact_color': 'Formal Garden', 'colors': ['Groen'], 'confidence': 0.94}, {'series': 'Groovy', 'exact_color': 'Sunset', 'colors': ['Oranje'], 'confidence': 0.94}, {'series': 'Groovy', 'exact_color': 'Tiffanys', 'colors': ['Groen'], 'confidence': 0.94}, {'series': 'Harlem', 'exact_color': 'Terra', 'colors': ['Beige'], 'confidence': 0.93}, {'series': 'Hashi', 'exact_color': 'Camelia', 'colors': ['Wit'], 'confidence': 0.94}, {'series': 'Hashi', 'exact_color': 'Fotinia', 'colors': ['Oranje'], 'confidence': 0.94}, {'series': 'Hashi', 'exact_color': 'Giunco', 'colors': ['Groen'], 'confidence': 0.94}, {'series': 'Hashi', 'exact_color': 'Iris', 'colors': ['Blauw'], 'confidence': 0.94}, {'series': 'Hashi', 'exact_color': 'Loto', 'colors': ['Beige'], 'confidence': 0.94}, {'series': 'Hashi', 'exact_color': 'Muscari', 'colors': ['Blauw'], 'confidence': 0.94}, {'series': 'Hashi', 'exact_color': 'Primula', 'colors': ['Geel'], 'confidence': 0.94}, {'series': 'Hashi', 'exact_color': 'Senecio', 'colors': ['Grijs'], 'confidence': 0.94}, {'series': 'Hashi', 'exact_color': 'Tulipano', 'colors': ['Groen', 'Blauw'], 'confidence': 0.9}, {'series': 'Jarel', 'exact_color': 'Oak', 'colors': ['Bruin'], 'confidence': 0.86}, {'series': 'Jazz', 'exact_color': 'Luz', 'colors': ['Wit', 'Beige'], 'confidence': 0.85}, {'series': 'Joyful', 'exact_color': 'Ash', 'colors': ['Grijs'], 'confidence': 0.97}, {'series': 'Joyful', 'exact_color': 'Bone', 'colors': ['Beige'], 'confidence': 0.98}, {'series': 'Joyful', 'exact_color': 'Lava', 'colors': ['Zwart'], 'confidence': 0.99}, {'series': 'Joyful', 'exact_color': 'Steel', 'colors': ['Grijs'], 'confidence': 0.99}, {'series': 'Kyoto', 'exact_color': 'Garden', 'colors': ['Groen'], 'confidence': 0.85}, {'series': 'Kyoto', 'exact_color': 'Palace', 'colors': ['Blauw', 'Groen'], 'confidence': 0.85}, {'series': 'Kyoto', 'exact_color': 'River', 'colors': ['Wit', 'Blauw'], 'confidence': 0.85}, {'series': 'Laverton', 'exact_color': 'Natural', 'colors': ['Oranje', 'Bruin'], 'confidence': 0.97}, {'series': 'Lexa', 'exact_color': 'Pearl Brillo', 'colors': ['Grijs'], 'confidence': 0.97}, {'series': 'Lingotti', 'exact_color': 'Ghiaccio', 'colors': ['Grijs'], 'confidence': 0.97}, {'series': 'Lingotti', 'exact_color': 'Terra', 'colors': ['Oranje'], 'confidence': 0.86}, {'series': 'Luca', 'exact_color': 'Lava', 'colors': ['Bruin', 'Oranje'], 'confidence': 0.9}, {'series': 'Luca', 'exact_color': 'Nacar', 'colors': ['Grijs'], 'confidence': 0.9}, {'series': 'Lula', 'exact_color': 'Pearl', 'colors': ['Grijs'], 'confidence': 0.8}, {'series': 'Madrid', 'exact_color': 'Avema Mate', 'colors': ['Beige'], 'confidence': 0.95}, {'series': 'Madrid', 'exact_color': 'Luna Mate', 'colors': ['Grijs'], 'confidence': 0.99}, {'series': 'Madrid Metro', 'exact_color': 'Oroval', 'colors': ['Geel'], 'confidence': 0.99}, {'series': 'Malaga', 'exact_color': 'Azafata T-1', 'colors': ['Groen', 'Blauw'], 'confidence': 0.9}, {'series': 'Malaga', 'exact_color': 'Azafata T-2', 'colors': ['Groen', 'Blauw'], 'confidence': 0.9}, {'series': 'Malaga', 'exact_color': 'Bauxita', 'colors': ['Bruin'], 'confidence': 0.99}, {'series': 'Malaga', 'exact_color': 'Craquele', 'colors': ['Wit'], 'confidence': 0.95}, {'series': 'Malaga', 'exact_color': 'Glen', 'colors': ['Groen'], 'confidence': 0.99}, {'series': 'Malaga', 'exact_color': 'Ravine', 'colors': ['Groen'], 'confidence': 0.99}, {'series': 'Marble Line', 'exact_color': 'Gold Brillo', 'colors': ['Wit', 'Beige'], 'confidence': 0.95}, {'series': 'Marble Line', 'exact_color': 'Gold Mate', 'colors': ['Wit', 'Beige'], 'confidence': 0.95}, {'series': 'Marea', 'exact_color': 'Terra Matt', 'colors': ['Oranje'], 'confidence': 0.96}, {'series': 'Maris', 'exact_color': 'Earth Haze', 'colors': ['Beige'], 'confidence': 0.95}, {'series': 'Maris', 'exact_color': 'Mystic Night', 'colors': ['Zwart'], 'confidence': 0.99}, {'series': 'Maris', 'exact_color': 'Soft Cloud', 'colors': ['Grijs'], 'confidence': 0.99}, {'series': 'Marmorea', 'exact_color': 'Biancone', 'colors': ['Beige'], 'confidence': 0.95}, {'series': 'Modulo', 'exact_color': 'Mattone', 'colors': ['Oranje'], 'confidence': 0.94}, {'series': 'Modulo', 'exact_color': 'Polvere', 'colors': ['Beige'], 'confidence': 0.88}, {'series': 'Muris', 'exact_color': 'Nix', 'colors': ['Beige'], 'confidence': 0.99}, {'series': 'Muris', 'exact_color': 'Nocta', 'colors': ['Grijs'], 'confidence': 0.94}, {'series': 'Muris', 'exact_color': 'Terra', 'colors': ['Oranje'], 'confidence': 0.93}, {'series': 'Muris', 'exact_color': 'Vidri', 'colors': ['Groen'], 'confidence': 0.99}, {'series': 'Nala', 'exact_color': 'Pearl', 'colors': ['Grijs'], 'confidence': 0.98}, {'series': 'Neri', 'exact_color': 'Silver Mist', 'colors': ['Grijs'], 'confidence': 0.99}, {'series': 'New Cotto', 'exact_color': 'Pearl Brillo', 'colors': ['Grijs'], 'confidence': 0.89}, {'series': 'Node', 'exact_color': 'Bone', 'colors': ['Beige'], 'confidence': 0.84}, {'series': 'Nomade', 'exact_color': 'Bone', 'colors': ['Beige'], 'confidence': 0.93}, {'series': 'Nomade', 'exact_color': 'Pearl', 'colors': ['Wit'], 'confidence': 0.98}, {'series': 'Pigmento', 'exact_color': 'Terra Matt', 'colors': ['Oranje'], 'confidence': 0.9}, {'series': 'Pool Porc.', 'exact_color': 'Luz', 'colors': ['Wit', 'Beige'], 'confidence': 0.9}, {'series': 'Pop Tile', 'exact_color': 'Nacar', 'colors': ['Wit'], 'confidence': 0.96}, {'series': 'Pop Tile', 'exact_color': 'Nácar', 'colors': ['Wit'], 'confidence': 0.96}, {'series': 'Potters', 'exact_color': 'Fossil', 'colors': ['Beige'], 'confidence': 0.88}, {'series': 'Pottery', 'exact_color': 'Natural', 'colors': ['Beige'], 'confidence': 0.96}, {'series': 'Pradolongo', 'exact_color': 'Pearl', 'colors': ['Grijs'], 'confidence': 0.92}, {'series': 'Puck', 'exact_color': 'Pearl', 'colors': ['Grijs'], 'confidence': 0.98}, {'series': 'Re-Bel', 'exact_color': 'Cuivre', 'colors': ['Beige', 'Bruin'], 'confidence': 0.94}, {'series': 'Re-Bel', 'exact_color': 'Or', 'colors': ['Wit', 'Grijs'], 'confidence': 0.92}, {'series': 'Re-Bel', 'exact_color': 'Perle', 'colors': ['Wit'], 'confidence': 0.96}, {'series': 'Retiro', 'exact_color': 'Colonial Brillo', 'colors': ['Beige'], 'confidence': 0.8}, {'series': 'Retiro', 'exact_color': 'Marina Brillo', 'colors': ['Blauw'], 'confidence': 0.99}, {'series': 'Retiro', 'exact_color': 'Titanio Brillo', 'colors': ['Grijs'], 'confidence': 0.99}, {'series': 'Ribe-R', 'exact_color': 'Natural', 'colors': ['Beige', 'Bruin'], 'confidence': 0.95}, {'series': 'Ritmo', 'exact_color': 'Bronce Oxidado', 'colors': ['Groen', 'Beige'], 'confidence': 0.95}, {'series': 'Ritmo', 'exact_color': 'Mostaza Oro Viejo', 'colors': ['Geel', 'Beige'], 'confidence': 0.93}, {'series': 'Ritmo', 'exact_color': 'Rojizo Cobre', 'colors': ['Roze', 'Beige'], 'confidence': 0.88}, {'series': 'Rock Star', 'exact_color': 'Gold', 'colors': ['Wit', 'Grijs'], 'confidence': 0.95}, {'series': 'Root', 'exact_color': 'Bold', 'colors': ['Bruin'], 'confidence': 0.91}, {'series': 'Root', 'exact_color': 'Chipper', 'colors': ['Bruin'], 'confidence': 0.91}, {'series': 'Root', 'exact_color': 'Mellow', 'colors': ['Beige'], 'confidence': 0.91}, {'series': 'Root', 'exact_color': 'Pearl', 'colors': ['Beige'], 'confidence': 0.97}, {'series': 'SAFARI', 'exact_color': 'Bruciato', 'colors': ['Bruin'], 'confidence': 0.88}, {'series': 'Salerno-R', 'exact_color': 'Bold', 'colors': ['Bruin'], 'confidence': 0.91}, {'series': 'Salerno-R', 'exact_color': 'Chipper', 'colors': ['Bruin'], 'confidence': 0.91}, {'series': 'Salerno-R', 'exact_color': 'Mellow', 'colors': ['Beige'], 'confidence': 0.91}, {'series': 'Seine', 'exact_color': 'Natural', 'colors': ['Bruin'], 'confidence': 0.98}, {'series': 'Sentier', 'exact_color': 'Bone', 'colors': ['Beige'], 'confidence': 0.95}, {'series': 'Sentier', 'exact_color': 'Light', 'colors': ['Beige'], 'confidence': 0.95}, {'series': 'Sentier', 'exact_color': 'Natural', 'colors': ['Beige'], 'confidence': 0.94}, {'series': 'Souk', 'exact_color': 'Bone', 'colors': ['Beige'], 'confidence': 0.98}, {'series': 'Stracciatella', 'exact_color': 'Nacar', 'colors': ['Wit'], 'confidence': 0.94}, {'series': 'Stripes', 'exact_color': 'Dove Matt', 'colors': ['Grijs'], 'confidence': 0.9}, {'series': 'Studio', 'exact_color': 'Silver Sands', 'colors': ['Grijs', 'Beige'], 'confidence': 0.85}, {'series': 'Studio', 'exact_color': 'SilverSands', 'colors': ['Grijs', 'Beige'], 'confidence': 0.85}, {'series': 'Studio', 'exact_color': 'Snow Cap', 'colors': ['Wit'], 'confidence': 0.99}, {'series': 'Studio', 'exact_color': 'Timberline', 'colors': ['Grijs'], 'confidence': 0.78}, {'series': 'Studio', 'exact_color': 'Volcanico', 'colors': ['Zwart'], 'confidence': 0.96}, {'series': 'Studio', 'exact_color': 'Volcánico', 'colors': ['Zwart'], 'confidence': 0.95}, {'series': 'Svenka', 'exact_color': 'Bone', 'colors': ['Beige'], 'confidence': 0.94}, {'series': 'Sweet Bars', 'exact_color': 'Berry Matt', 'colors': ['Rood', 'Roze'], 'confidence': 0.85}, {'series': 'Sweet Bars', 'exact_color': 'Tan Matt', 'colors': ['Oranje'], 'confidence': 0.82}, {'series': 'Tanger Mate', 'exact_color': 'Tiffany', 'colors': ['Groen', 'Blauw'], 'confidence': 0.85}, {'series': 'Tivoli-R', 'exact_color': 'Canella', 'colors': ['Bruin'], 'confidence': 0.88}, {'series': 'Travento', 'exact_color': 'Pearl', 'colors': ['Wit'], 'confidence': 0.89}, {'series': 'Vodevil', 'exact_color': 'Nacár', 'colors': ['Wit'], 'confidence': 0.92}, {'series': 'Volume', 'exact_color': 'Nacar Brillo', 'colors': ['Grijs'], 'confidence': 0.88}, {'series': 'Wabisabi', 'exact_color': 'Ghiaccio', 'colors': ['Grijs'], 'confidence': 0.96}, {'series': 'Wabisabi', 'exact_color': 'Terra', 'colors': ['Oranje'], 'confidence': 0.83}, {'series': 'Waves', 'exact_color': 'Micro Chip', 'colors': ['Grijs'], 'confidence': 0.94}, {'series': 'Waves', 'exact_color': 'Periscope', 'colors': ['Grijs'], 'confidence': 0.94}, {'series': 'Yuri', 'exact_color': 'Caldera', 'colors': ['Bruin'], 'confidence': 0.95}, {'series': 'Zelij', 'exact_color': 'Hueso 1010', 'colors': ['Beige'], 'confidence': 0.93}, {'series': 'Zelij', 'exact_color': 'Pergamon', 'colors': ['Beige'], 'confidence': 0.95}, {'series': 'Zelij', 'exact_color': 'Via Lactea', 'colors': ['Wit', 'Blauw'], 'confidence': 0.85}, {'series': 'Zero', 'exact_color': 'Bold', 'colors': ['Bruin'], 'confidence': 0.91}, {'series': 'Zero', 'exact_color': 'Chipper', 'colors': ['Bruin'], 'confidence': 0.91}, {'series': 'Zero', 'exact_color': 'Mellow', 'colors': ['Beige'], 'confidence': 0.91}, {'series': 'Zero', 'exact_color': 'Pearl', 'colors': ['Beige'], 'confidence': 0.97}, {'series': 'Zero Origo', 'exact_color': 'Pearl', 'colors': ['Beige'], 'confidence': 0.97}, {'series': 'Zero-R', 'exact_color': 'Bold', 'colors': ['Bruin'], 'confidence': 0.91}, {'series': 'Zero-R', 'exact_color': 'Chipper', 'colors': ['Bruin'], 'confidence': 0.91}, {'series': 'Zero-R', 'exact_color': 'Mellow', 'colors': ['Beige'], 'confidence': 0.91}]
MARKER = '# BC_COTTO_VISUAL_COLORS_V1'

HELPERS = '''
# BC_COTTO_VISUAL_COLORS_V1
def _bc_cotto_expected_color(doc):
    rules = _BC_SIMPLE_COLORS['COTTO_VISUAL_SCOPED_RULES']
    normalize_color = _BC_SIMPLE_COLORS['normalize']
    normalize_series_color = _BC_SIMPLE_COLORS['normalize_series']
    if normalize_color(doc.get('vendor')) != 'cottoceramix' or not _bc_acero_is_tile(doc):
        return None
    raw = doc.get('f_kleur_exact')
    series = _bc_simple_strings(doc.get('f_serie')) or _bc_simple_strings(doc.get('series'))
    if not isinstance(raw, str) or len(series) != 1:
        return None
    return rules.get((normalize_series_color(series[0]), normalize_color(raw)))

def _bc_cotto_targets(docs):
    return [doc for doc in docs if _bc_cotto_expected_color(doc) is not None]

def _bc_cotto_check(docs):
    return all(doc.get('f_kleur') == _bc_cotto_expected_color(doc)
               for doc in _bc_cotto_targets(docs))
'''


def _sha(source):
    return hashlib.sha256(source.encode('utf-8')).hexdigest()


def _replace_once(source, old, new):
    if source.count(old) != 1:
        raise RuntimeError('Cotto-kleurhook ontbreekt of is niet uniek')
    return source.replace(old, new, 1)


def _offsets(source, node):
    lines = source.splitlines(keepends=True)
    start = len(''.join(lines[:node.lineno - 1])) + len(lines[node.lineno - 1].encode()[:node.col_offset].decode())
    end = len(''.join(lines[:node.end_lineno - 1])) + len(lines[node.end_lineno - 1].encode()[:node.end_col_offset].decode())
    return start, end


def reviewed_rule_map(rules, namespace):
    if not isinstance(rules, list) or not rules:
        raise RuntimeError('Een niet-lege lijst beoordeelde Cotto-kleurregels is vereist')
    normalize_color = namespace['normalize']
    normalize_series_color = namespace['normalize_series']
    taxonomy = namespace['TAXONOMY']
    owners = {(normalize_color(v), normalize_series_color(s), normalize_color(raw)): colors
              for v, s, raw, colors, _primary in namespace['OWNER_RULES']}
    result = {}
    for rule in rules:
        if (not isinstance(rule, dict) or not isinstance(rule.get('series'), str)
                or not isinstance(rule.get('exact_color'), str)
                or not rule['series'].strip() or not rule['exact_color'].strip()):
            raise RuntimeError('Kleurregels vereisen een exacte serie en bronkleur')
        confidence = rule.get('confidence')
        if (isinstance(confidence, bool) or not isinstance(confidence, (int, float))
                or not .70 <= confidence <= 1):
            raise RuntimeError('Visuele kleurregel mist voldoende vastgelegde zekerheid')
        colors = rule.get('colors')
        if (not isinstance(colors, list) or not colors
                or any(not isinstance(color, str) or color not in taxonomy for color in colors)
                or len(colors) != len(set(colors))):
            raise RuntimeError('Visuele kleurregel bevat ongeldige basiskleuren')
        ordered = [color for color in taxonomy if color in colors]
        key = (normalize_series_color(rule['series']), normalize_color(rule['exact_color']))
        if key in result and result[key] != ordered:
            raise RuntimeError('Tegenstrijdige Cotto-regels na normalisatie van serie/kleur: ' + ' / '.join(key))
        owner = owners.get(('cottoceramix', *key))
        if owner is not None and set(owner) != set(ordered):
            raise RuntimeError('Visuele kleurregel strijdt met een expliciete eigenaarregel')
        if key[1] == 'acero' and ordered != ['Grijs']:
            raise RuntimeError('De bevestigde Acero-regel moet behouden blijven')
        result[key] = ordered
    return dict(sorted(result.items()))


def patch_cotto_worker(source):
    if not isinstance(source, str):
        raise RuntimeError('Workerbron moet tekst zijn')
    if MARKER in source:
        if source.count(MARKER) != 1 or not PATCHED_WORKER_SHA256 or _sha(source) != PATCHED_WORKER_SHA256:
            raise RuntimeError('Bestaande Cotto-kleurcorrectie wijkt af; niets gewijzigd')
        compile(source, '<existing-cotto-worker>', 'exec')
        return source
    if _sha(source) != BASE_WORKER_SHA256:
        raise RuntimeError('Worker wijkt af van de beoordeelde liveversie')
    tree = ast.parse(source)
    literals = [node.args[0] for node in ast.walk(tree)
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id == 'compile' and len(node.args) >= 3
                and isinstance(node.args[1], ast.Constant) and node.args[1].value == '<derived-color-rules>'
                and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str)]
    if len(literals) != 1:
        raise RuntimeError('Geen unieke afgeleide kleurmodule')
    literal = literals[0]
    namespace = {'__name__': 'reviewed_cotto_color_source'}
    exec(compile(literal.value, '<reviewed-cotto-color-source>', 'exec'), namespace)
    rules = reviewed_rule_map(SCOPED_RULES, namespace)
    colors = _replace_once(literal.value,
        '\ndef classify_color(raw, context=None):\n',
        '\nCOTTO_VISUAL_SCOPED_RULES = ' + repr(rules) + '\n\ndef classify_color(raw, context=None):\n')
    colors = _replace_once(colors,
        "    if vendor == 'porcelanosa' and s == 'caliza':\n",
        "    if vendor == 'cottoceramix' and ctx.get('is_tile') is True and ctx.get('cotto_explicit_series') is True:\n"
        "        visual = COTTO_VISUAL_SCOPED_RULES.get((series, s))\n"
        "        if visual is not None:\n"
        "            return _result(raw, visual, 'INFERRED_VISUAL', 'Reviewed exact series/color product swatch; manufacturer name retained.')\n"
        "    if vendor == 'porcelanosa' and s == 'caliza':\n")
    colors = _replace_once(colors,
        "    series_values = _strings(doc.get('f_serie')) or _strings(doc.get('series'))\n",
        "    series_values = _strings(doc.get('f_serie')) or _strings(doc.get('series'))\n"
        "    cotto_explicit_series = len(series_values) == 1\n")
    old_context = "return [{'vendor': vendor, 'series': s, 'is_tile': doc.get('_bc_tile_color_context') is True} for s in series_values] if len(series_values) == 1 else [{'vendor': vendor, 'is_tile': doc.get('_bc_tile_color_context') is True}]"
    new_context = "return [{'vendor': vendor, 'series': s, 'is_tile': doc.get('_bc_tile_color_context') is True, 'cotto_explicit_series': cotto_explicit_series} for s in series_values] if len(series_values) == 1 else [{'vendor': vendor, 'is_tile': doc.get('_bc_tile_color_context') is True, 'cotto_explicit_series': False}]"
    colors = _replace_once(colors, old_context, new_context)
    compile(colors, '<cotto-visual-color-rules>', 'exec')
    start, end = _offsets(source, literal)
    result = source[:start] + repr(colors) + source[end:]
    tree = ast.parse(result)
    snapshots = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == '_bc_simple_snapshot']
    checks = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == 'check_b2c_profiles']
    guards = [node for node in tree.body if isinstance(node, ast.If) and ast.unparse(node.test) == "__name__ == '__main__'"]
    if len(snapshots) != 1 or len(checks) != 2 or len(guards) != 1:
        raise RuntimeError('Verwachte bestaande workerhooks verschillen')
    check = checks[-1]
    returns = [node for node in check.body if isinstance(node, ast.Return)]
    if len(returns) != 1 or check.body[-1] is not returns[0]:
        raise RuntimeError('Geen unieke eindcontrole voor filters')
    lines = result.splitlines(keepends=True)
    positions = [
        (sum(len(line) for line in lines[:snapshots[0].end_lineno]),
         "    if not _bc_cotto_check(docs):\n"
         "        raise RuntimeError('Cotto-tegelkleuren voldoen niet aan beoordeelde serieregels')\n"
         "    snapshot['cotto_visual_colors_v1'] = True\n"
         "    snapshot['cotto_visual_color_products'] = len(_bc_cotto_targets(docs))\n"),
        (sum(len(line) for line in lines[:returns[0].lineno - 1]),
         "    checks.append({'name': 'Cotto-seriekleuren volgen beoordeelde productstalen; bronkleur behouden',\n"
         "                   'passed': snapshot.get('cotto_visual_colors_v1') is True and _bc_cotto_check(docs),\n"
         "                   'products': len(_bc_cotto_targets(docs))})\n"),
        (sum(len(line) for line in lines[:guards[0].lineno - 1]), HELPERS.rstrip() + '\n\n'),
    ]
    for position, text in sorted(positions, reverse=True):
        result = result[:position] + text + result[position:]
    if result.count(MARKER) != 1:
        raise RuntimeError('Cotto-kleurcorrectie niet eenduidig toegevoegd')
    compile(result, '<cotto-color-corrected-worker>', 'exec')
    return result
