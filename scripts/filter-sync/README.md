# BadkamerCity — veilige Wiesbaden → Typesense indexvoorbereiding

**Status 22 oktober 2026: IMPLEMENTED_OFFLINE / NOT_DEPLOYED.** Deze tool is bedoeld voor de bestaande Shopify-catalogus en de bestaande Typesense-architectuur op de VPS. Er is géén live-indexsynchonisatie, automatische planning, API-omschakeling of VPS-uitvoering door deze Git-commit uitgevoerd.

## Waarom deze route?

De bestaande `run_index.py` uit de proef van 13 oktober leest slechts de bevroren 11.050-productenexport. Het kan nieuwe Wiesbaden-producten en recente prijs-/metafieldaanpassingen niet ophalen. De werkende `/verified/` API en de 149 collectieprofielen moeten intact blijven totdat een nieuwe index gecontroleerd is.

Waarnemingen (21–22 oktober, uit Shopify Admin en handmatige SSH-console):

- Shopify: **2.451** ACTIVE en Online Store-gepubliceerde Wiesbaden-producten.
- Index van 13 oktober: **2.265** Wiesbaden-producten, waarvan **2.219** in de algemene winkelresultaten. De overige **46** zijn voornamelijk onderdelen (rozetten, binnenwerken, verlengsets, reparatieonderdelen); hun bestaande `general_shopping`-regel wordt behouden.
- **186** verschil in aantallen tussen oude index en Shopify; dit is nog geen volledige ID-voor-ID-diff.
- Collectie `inloopdouches`: API had 294 producten, Shopify Admin 305. In `profiles.json` zijn op 22 oktober de filters `f_breedte_mm`, `f_glasdikte_mm`, `f_glaskleur` voor die collectie handmatig toegevoegd, met back-up en API-test (8 → 11 filters); een volledige storefront-check is nog niet bewezen.
- Actieve Shopify MAIN: `195491168522`; externe `bc-external-filters.liquid` wijst naar de `/verified/`-API.
- De eigenaar kon op 22 oktober via Windows PowerShell met wachtwoord op de VPS inloggen. Deze GitHub-uitvoersessie heeft geen SSH-toegang en kent geen Shopify- of Typesense-token op de VPS; het doorgegeven laatste commando bevatte **geen terminaluitvoer**.

## Wat het script wél doet

`index_sync.py` (alleen Python-standaardbibliotheek):

1. `capture`: leest via de **Shopify Admin GraphQL API** de actieve, Online Store-gepubliceerde Wiesbaden-producten inclusief SKU, prijs (zoals Shopify die al als consumentenprijs incl. btw heeft), collecties, featured image en getypeerde metafields. Schrijft uitsluitend een privé-JSONL, geen Shopify-mutaties.
2. `prepare`: voegt het actuele merkoverzicht samen met de **bestaande, gecontroleerde** Typesense-documenten van 13 oktober. Niet-Wiesbaden blijft byte-semantisch gelijk; bestaande service-uitsluitingen blijven behouden. Nieuwe producttypen krijgen alleen automatisch een classificatie als álle oude Wiesbaden-producten met exact dat type dezelfde classificatie hebben. Onbekende types stoppen de run voor handmatige beoordeling. `bc_data.filter_manifest.values` en latere expliciete `bc_filters.*` zijn de technische velden, nooit geraden titelspecificaties. Bekende schema-velden worden strikt getypeerd, onbekende filterkeys in het rapport geregistreerd. Collectieprofieltellingen worden opnieuw berekend; `allowed_filters` en `filters` worden **niet automatisch geactiveerd of verwijderd**.
3. `stage`: mag uitsluitend een **nieuwe**, geïsoleerde collectie met naam `bc_wiesbaden_stage_<hash>` op Typesense localhost:8108 maken. Het overschrijft/verwijdert nooit een bestaande collectie of alias; de live API en Caddy blijven ongewijzigd. Elke importregel en een volledige document-export worden tegen de verwachte documenten gecontroleerd. Bij een fout wordt **niet** omgeschakeld.

Prijzen worden als exacte decimalen naar centen geconverteerd; **geen extra 21% btw** en geen nieuwe prijsafleiding. Afwijkende of ontbrekende SKU, onbekende serviceclassificatie, meervoudige varianten, afgekapt Shopify-metafield-/collectie-overzicht, ongeldige getypeerde waarde of verdwenen bestaand product = STOP vóór staging.

**Beperking:** de nieuwe `bc_filters`-waarden kunnen keys bevatten waarvoor nog geen bevestigd `f_*`-veld in het oude schema bestaat. Deze worden afzonderlijk gerapporteerd en niet stil omgezet. `bc_data.filter_manifest.values_sha256` is niet onafhankelijk opnieuw berekend. De inhoudelijke juistheid van fabrikantgegevens wordt niet opnieuw gecertificeerd. Het script is **geen productiegeschikte permanente autosync** en er is geen cron of webhook ingericht.

## Uitvoering op een geautoriseerde VPS-sessie (nog niet uitgevoerd)

De code hoort op de **actieve branch** `fix/product-cards-2026-10-14`, in `scripts/filter-sync/`. Gebruik de bestaande productie-back-ups. Bewaar privé-snapshots **buiten** de publieke repo, bijv. onder `/home/ubuntu/bc_sync_private_20261022/`. Controleer eerst of de actuele 13-oktober-indexbestanden, de live `profiles.json` met de drie nieuwe douchefilters en de Shopify-authenticatie beschikbaar zijn.

```bash
# Eerst alleen de offline tests; voert geen netwerkmutaties uit.
python3 -m unittest discover -s scripts/filter-sync -p 'test_*.py' -v

# Het volgende pas wanneer geautoriseerde env-var beschikbaar is.
# Deel SHOPIFY_ADMIN_ACCESS_TOKEN / TYPESENSE_API_KEY NOOIT in chat of Git.
python3 scripts/filter-sync/index_sync.py capture \
  --out /home/ubuntu/bc_sync_private_20261022/shopify_wiesbaden.jsonl

# Leest 13-okt-gegevens en actuele serverprofielen; geen netwerkmutaties.
python3 scripts/filter-sync/index_sync.py prepare \
  --base /home/ubuntu/bc_filterindex_20261013_874e415c15/index_products.jsonl \
  --snapshot /home/ubuntu/bc_sync_private_20261022/shopify_wiesbaden.jsonl \
  --schema /home/ubuntu/bc_filterindex_20261013_874e415c15/index_schema.json \
  --profiles /home/ubuntu/bc_apiproef_20261013/profiles.json \
  --out /home/ubuntu/bc_sync_private_20261022/candidate

# Optionele VOLGENDE fase; vereist bestaande Typesense-auth en expliciete operatorcontrole.
# Creëert alleen een nieuwe testcollectie op localhost, nooit de actieve.
python3 scripts/filter-sync/index_sync.py stage \
  --folder /home/ubuntu/bc_sync_private_20261022/candidate
```

De capture vereist `SHOPIFY_ADMIN_ACCESS_TOKEN` in de procesomgeving; alleen de vaste toegestane Shopify-host wordt benaderd. De stage vereist `TYPESENSE_API_KEY`, gebruikt alleen de lokale `127.0.0.1:8108`-poort, en vraagt geen Shopify-write-scopes. Configureer sleutels op de VPS volgens bestaand geheimenbeheer met root-only rechten; voer geen sleutels als CLI-argument in en plaats ze niet in commandologs. **Het laatste doorgegeven commando toonde geen werkelijke uitvoer**, dus het is nog onbekend of zulke variabelen al bestaan.

## Handmatige preflight, acceptatie en omschakeling

1. Vergelijk alle Shopify-ID's/SKU's en de ontbrekende 186 met de oude index; controleer eventuele nieuwe service-producttypes en alle gerapporteerde onbekende filterkeys. Neem de 28 prijsuitzonderingen en 3 eerder geblokkeerde SKU-creaties niet opnieuw in behandeling.
2. Verifieer schema, unieke ID's, nieuwe aantallen en prijzen, actieve merkfilters, collectie-lidmaatschappen en productkaarten. De `profiles.json`-tellingen moeten exact met Shopify publicatie en het gewenste uitgesloten servicebereik overeenkomen; dezelfde controle op minimaal `inloopdouches`, `kranen`, `wastafels`, `baden`.
3. Test filtercombinaties/ranges (breedte, glasdikte, glaskleur), sortering op actuele incl.-btw-prijs en CORS/fallback. Test echte desktop-/mobiele storefrontweergave en de bestaande JavaScript-guard op `profile_products`. **Nog niet getest.**
4. Maak vóór enige release een verifieerbare back-up van de werkende Typesense-collectie én de API- en profielenbestanden. Schakel alleen met expliciet goedgekeurde release-/rollbackprocedure de Verified Candidate om; deze tool bevat bewust geen deploy-, delete-, alias- of restart-actie.
5. Na succesvolle readbacks kan later een incrementele/webhook-synchronisatie worden ontworpen. Plan niet vooraf automatisch updates zolang ID-/service-/metafieldmapping en idempotente delete-afhandeling niet zijn bewezen.

**Huidige controlegrens:** tests op synthetische fixtures bewijzen codegedrag, geen echte VPS-indexering, Shopify token beschikbaarheid, volledige bedrijfsdata of live storefront-succes.
