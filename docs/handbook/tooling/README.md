# Historische handboekgenerator — 31 oktober 2026

Deze tooling reproduceert het gedateerde 80-hoofdstukkenboek en de offline leesfunctie. Actuele winkelgegevens staan in [de huidige masterindex](../../MASTER_SITE_REFERENCE.md) en [de audit van 8 november](../../audits/2026-11-08/README.md). Een geslaagde historische DOM-test bewijst geen actuele Shopify-werking.

`render-handbook.cjs` leest expliciet `docs/MASTER_SITE_REFERENCE_2026-10-31.md`. De bestaande `check-handbook.cjs` controleert die historische HTML met zijn oorspronkelijke aantallen en datering. De bronarchiefbytes zijn bij de actualisatie behouden.

```sh
node docs/handbook/tooling/render-handbook.cjs /absolute/repo /absolute/scratch/handbook-2026-10-31.html
node docs/handbook/tooling/check-handbook.cjs /absolute/scratch/handbook-2026-10-31.html /absolute/scratch/handbook-check.json
python3 docs/handbook/tooling/compile-practical.py /absolute/repo --output /absolute/scratch/rebuilt-handbook.md
```

De compiler vereist een apart uitvoerpad en weigert zowel de actuele masterindex als het oorspronkelijke archief te overschrijven. Gebruik voor historische reconstructie de oorspronkelijke JSON/Markdown-input in `docs/handbook/2026-10-31/`. Een eventuele inhoudelijke heruitgave krijgt een nieuwe peildatum en eigen bewijs.
