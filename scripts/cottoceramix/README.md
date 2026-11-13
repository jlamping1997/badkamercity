# Cottoceramix importplan

Deze scripts maken uitsluitend een privé-uitvoerplan. Ze hebben geen token, netwerkclient, Shopify-write of publicatieactie.

`build_import_plan.py` leest de gecorrigeerde, genormaliseerde bronregels en maakt DRAFT `ProductSetInput`-variabelen. Alle m²- en prijswaarden komen uit de gecorrigeerde verpakking; een zeshoek of ander vormproduct wordt nooit als omhullende rechthoek doorgerekend. Productidentiteit is het exacte SKU. Reeds bestaande SKU's worden overgeslagen, niet opnieuw aangemaakt of via `productSet` bijgewerkt.

```sh
python3 scripts/cottoceramix/build_import_plan.py \
  --source-json /private/normalized-products.json \
  --output-dir /private/import-plan \
  --existing-json /private/current-sku-registry.json \
  --menu-evidence /private/verified-menu-groups.json \
  --collections-json /private/verified-collection-ids.json \
  --source-snapshot 2026-11-05T12:01:36

python3 -m unittest discover -s scripts/cottoceramix -p 'test_*.py' -v
node scripts/cottoceramix/audit_choice_matrix.mjs /private/import-plan

python3 scripts/cottoceramix/verify_readback.py \
  --planned /private/import-plan/products.json \
  --readback /private/full-admin-readback.json \
  --active-skus /private/already-active-skus.json \
  --require-group-refs \
  --output /private/readback-verification.json
```

Het uitvoerpad moet buiten deze publieke repository liggen. De JSONL bevat complete privébronregels en mag niet worden gecommit. `product-set-variables.jsonl` bevat per regel `{ "input": ProductSetInput }`; de daadwerkelijke bulkmutatie en Shopify-readback blijven verantwoordelijkheid van de uitvoerder.

De gekozen maattekst Z/AA en gekozen dikte AF voeden de gepubliceerde maatvoering. De oudere Excel-numerieke kolommen AB/AC/AE mogen die keuzes niet terug overschrijven. Niet enkelvoudige diktes, zoals een bereik, vragen een aparte representatie en worden in deze basisversie geblokkeerd.

## Blokkades en publicatie

Een hele voorgestelde groep blijft op HOLD als een lid onbekende of conflicterende kerngegevens heeft, als dezelfde echte keuzewaarden meerdere SKU's aanwijzen, als verkoopeenheden door elkaar lopen of als de groep meer dan vijftig artikelen bevat. Niet-m²-artikelen vragen een eigen kooproute. Ontbrekende/ongeldige EAN wordt weggelaten en blokkeert niet zelfstandig. Bronafbeeldingen moeten echte publieke Cottoceramix-afbeeldingen zijn; de externe `no-img.svg`-placeholder wordt afgekeurd.

Groepen zonder nagekeken bronmenu zijn kandidaten, geen exacte kopie van Cottoceramix. `--menu-evidence` accepteert een array van objecten met `verified: true`, `group_key`, een exacte unieke `skus`-lijst en publieke Cottoceramix-`source_urls`. Ook met dit bewijs blijven daadwerkelijke readback, groepsreferenties, media-READY en publicatie afzonderlijke stappen. Het script schrijft geen `tiles.group_products` voordat echte product-ID's bestaan.

De matrixaudit gebruikt de bestaande echte selectiekern met de geplande Shopify-metafieldwaarden. Hij bewijst unieke runtimekeuzes en behoud van een werkelijk beschikbare combinatie. Hij rapporteert apart wanneer een niet-bestaande combinatie naar een andere uitvoering terugvalt, bijvoorbeeld een gekoppelde andere dikte na een formaatkeuze. Dat rapport bewijst geen bronmenu-equivalentie of visuele browserkwaliteit.

`subdivide_groups.py` kan een afzonderlijke afgeleide kopie maken op basis van het private publicatiereview. Hij gebruikt bestaande officiële modelwaarden, gekozen afwerking en waar nodig expliciete formaten/diktes om technisch samenhangende kleurgroepen te vormen. Alleen `tiles.group_id`, `tiles.group_label` en `custom.switch_group` veranderen in de productinputs. Ontbrekende combinaties worden niet uitgevonden. Bronconflicten krijgen een eigen ongepubliceerde HOLD-groep; de bedoelde publicatie-SKU's staan apart. Gebruik deze `final-products.json` vervolgens als de verwachte input van de readback-verifier. De oorspronkelijke bron- en v2-planbestanden blijven ongewijzigd. Een uniforme selector over de afgescheiden modellen/formaatfamilies is afzonderlijk toekomstig UX-werk.

`verify_readback.py` werkt met volledige Admin-objecten of MCP-wrappers. Ontbrekende geselecteerde velden, afwijkende voorraadinstellingen/prijzen/eenheden/gewichten/metafields, dubbele SKU's en niet-gereed media blokkeren steeds de hele groep. De verwachte status is DRAFT, behalve de expliciete SKU-lijst in `--active-skus`. Met `--require-group-refs` moet elk groepslid exact alle bedoelde product-ID's verwijzen. Verkoopkanaalpublicatie en daadwerkelijke browser-/koopcontrole blijven afzonderlijke gates.

## Feedgrens

Het oorspronkelijke leveranciersmerk blijft intern bewaard; winkelmerk is Cottoceramix. Titel, omschrijving, URL, SEO, keuzerelaties en handmatige correcties zijn beschermd tegen een latere generieke feedoverschrijving. Levertijd-/voorraadvelden kunnen later gecontroleerd automatisch worden vernieuwd. Prijsverversing vraagt eerst expliciet prijsbeleid en behoud van handmatige prijs-/verpakkingscorrecties. Een bronsnapshot wordt als snapshot opgeslagen en nooit als een nieuw uitgevoerde voorraadcontrole gepresenteerd.
