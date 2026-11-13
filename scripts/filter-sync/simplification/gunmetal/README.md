# Gecombineerde filterupdate — 10 november 2026

Eigen Gunmetal-kleur, stabiele aanbevolen mix en controle op de twee gecorrigeerde Cinto-spiegelbreedtes. Geen API-bronwijziging, productimport of populariteitsclaims.

Zie [scope, tests, grenzen en installatie](../../../../docs/filters/gunmetal-2026-11-10/README.md).

```bash
python -m unittest discover -s scripts/filter-sync/simplification/gunmetal -p test_gunmetal.py -q
python -m unittest discover -s scripts/filter-sync/simplification/tile-looks/release -p test_apply_tile_look_filter.py -q
python scripts/filter-sync/simplification/gunmetal/build_gunmetal_filter.py
```

De tests gebruiken openbare bron-/modelfixtures en geïsoleerde lifecycle-mocks. De complete private runtime blijft op de VPS. Zonder echte staging-/API-/activeringscontrole is dit geen productiecertificaat.
