# BadkamerCity — productmetafield schema- en code-audit
> **Snapshot 7 oktober 2026, alleen lezen.** Definities via Shopify Admin GraphQL, vaste metafieldverwijzingen uit live-thema #194864677130. **Geen productwaarden of dekking gecontroleerd.** Ontbrekende definities zijn niet automatisch bewijs van een defect: legacy-/unstructured metafields kunnen bestaan, veel code is niet actief, en dynamische Liquid-verwijzingen vallen buiten deze tekstscan.

## Samenvatting

| Onderdeel | Feitelijke meting |
| --- | --- |
| Shopify product-metafielddefinities | **174** |
| Shopify variant-metafielddefinities | **0** |
| Shopify collectie-metafielddefinities | **0** |
| Statisch gedetecteerde unieke namespace/key-combinaties in thema | **68** |
| Ook in Shopify PRODUCT-definities aanwezig | **14** |
| Niet teruggevonden in PRODUCT-definities | **54** |
| Definities die deze statische scan niet letterlijk terugziet | **160** |

**Belangrijkste aandachtspunt:** een deel van de productspecificatie-UI leest `product.metafields.custom.*`, terwijl het Admin-schema veel velden onder `specs.*` definieert. Als een nieuw importproces alleen `specs.*` vult, verschijnen die waarden niet automatisch in bestaande Liquid-code die `custom.*` verwacht. Controleer per relevante SKU in Admin **welke namespace + key daadwerkelijk waarden heeft**, voordat je data migreert of Liquid verandert.

## Hoogste prioriteit: werkelijk ingeladen PDP-code
De volgende *vaste* key-verwijzingen staan in `main-product.liquid` of de door dit bestand aangeroepen custom PDP-snippets. Dit is **geen** uitspraak dat elk veld actief renderend is; templates en branches zijn conditioneel.

| Namespace.key | Definitie in Admin? | Directe codeplaatsen |
| --- | --- | --- |
| `custom.aandachtspunten` | Ja | `snippets/product-pros-cons.liquid` |
| `custom.aantal_straalsoorten_handdouche` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.aantal_straalsoorten_hoofddouche` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.aantal_uitgangen_tegelijk_bedienbaar` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.afmeting` | **Niet gevonden** | `sections/main-product.liquid` |
| `custom.afwerking` | Ja | `sections/main-product.liquid` |
| `custom.afwerking_greep` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.artikelnummer` | Ja | `snippets/bc-product-detail-specs.liquid` |
| `custom.basiskleur` | Ja | `sections/main-product.liquid`, `snippets/bc-product-detail-specs.liquid` |
| `custom.bediening_voor_aan_uit` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.belgaqua_keurmerk` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.breedte_diameter_douchekop` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.breedte_diameter_hoofddouche` | **Niet gevonden** | `sections/main-product.liquid`, `snippets/bc-product-detail-specs.liquid` |
| `custom.dikte_hoofddouche` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.ean` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.fabrikantnummer` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.frame` | **Niet gevonden** | `sections/main-product.liquid` |
| `custom.glansgraad` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.group` | **Niet gevonden** | `sections/main-product.liquid` |
| `custom.handdouche` | **Niet gevonden** | `sections/main-product.liquid` |
| `custom.hoofddouche` | **Niet gevonden** | `sections/main-product.liquid` |
| `custom.hoogte` | **Niet gevonden** | `sections/main-product.liquid` |
| `custom.hotbath_ecoair_system` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.hotbath_fluhs` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.hotbath_plumber_friendly` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.hotbath_shower_power_system` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.kleurgroep` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.led` | **Niet gevonden** | `sections/main-product.liquid` |
| `custom.lengte` | **Niet gevonden** | `sections/main-product.liquid` |
| `custom.lengte_douchearm` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.lengte_doucheslang` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.leverancier_verwachte_datum` | Ja | `sections/main-product.liquid` |
| `custom.leverancier_voorraad` | Ja | `sections/main-product.liquid` |
| `custom.materiaal_kraan` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.menu_1` | **Niet gevonden** | `sections/main-product.liquid` |
| `custom.menu_2` | **Niet gevonden** | `sections/main-product.liquid` |
| `custom.menu_3` | **Niet gevonden** | `sections/main-product.liquid` |
| `custom.menu_4` | **Niet gevonden** | `sections/main-product.liquid` |
| `custom.menu_5` | **Niet gevonden** | `sections/main-product.liquid` |
| `custom.met_doucheslang` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.met_glijstang` | **Niet gevonden** | `sections/main-product.liquid`, `snippets/bc-product-detail-specs.liquid` |
| `custom.met_handdouche` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.met_hoofddouche` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.met_inbouwdeel` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.montage` | Ja | `sections/main-product.liquid` |
| `custom.montagewijze` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.plaatsing` | **Niet gevonden** | `sections/main-product.liquid` |
| `custom.pluspunten` | Ja | `snippets/product-pros-cons.liquid` |
| `custom.serie` | Ja | `snippets/bc-product-detail-specs.liquid` |
| `custom.switch_group` | Ja | `sections/main-product.liquid`, `snippets/bc-product-switcher.liquid` |
| `custom.switch_key` | **Niet gevonden** | `sections/main-product.liquid` |
| `custom.thermostatisch` | Ja | `snippets/bc-product-detail-specs.liquid` |
| `custom.type` | **Niet gevonden** | `sections/main-product.liquid` |
| `custom.type_bevestiging_hoofddouche` | **Niet gevonden** | `sections/main-product.liquid`, `snippets/bc-product-detail-specs.liquid` |
| `custom.type_handdouche` | **Niet gevonden** | `sections/main-product.liquid`, `snippets/bc-product-detail-specs.liquid` |
| `custom.vorm` | Ja | `sections/main-product.liquid` |
| `custom.vorm_thermostaat` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `custom.vormgeving_stijlgroep` | **Niet gevonden** | `snippets/bc-product-detail-specs.liquid` |
| `reviews.rating` | **Niet gevonden** | `sections/main-product.liquid` |
| `reviews.rating_count` | **Niet gevonden** | `sections/main-product.liquid` |

## Alle overige statische verwijzingen zonder Admin-definitie
Deze lijst kan ook oudere of niet-actieve secties en pilotbestanden omvatten. Gebruik de codekaart om statische aanroepen te volgen; *niet* automatisch alle velden aanmaken.

| Namespace.key | Bestanden met letterlijke verwijzing |
| --- | --- |
| `bc_data.component_products` | `snippets/bc-hotbath-data-set.liquid` |
| `bc_data.set_components` | `snippets/bc-hotbath-data-set.liquid` |
| `bc_pilot.is_pilot` | `snippets/bc-hotbath-pilot-controls.liquid` |
| `bc_pilot.presentation` | `snippets/bc-hotbath-pilot-controls.liquid`, `snippets/bc-hotbath-pilot-specs.liquid` |
| `custom.search_card_spec_1` | `snippets/bc-card-product-search.liquid` |
| `custom.search_card_spec_2` | `snippets/bc-card-product-search.liquid` |

## Verwijzingen mét Admin-definitie

| Namespace.key | Type volgens Admin |
| --- | --- |
| `custom.aandachtspunten` | `list.single_line_text_field` |
| `custom.afwerking` | `single_line_text_field` |
| `custom.artikelnummer` | `single_line_text_field` |
| `custom.basiskleur` | `single_line_text_field` |
| `custom.complete_specificaties` | `json` |
| `custom.korte_omschrijving` | `multi_line_text_field` |
| `custom.leverancier_verwachte_datum` | `date` |
| `custom.leverancier_voorraad` | `boolean` |
| `custom.montage` | `single_line_text_field` |
| `custom.pluspunten` | `list.single_line_text_field` |
| `custom.serie` | `single_line_text_field` |
| `custom.switch_group` | `single_line_text_field` |
| `custom.thermostatisch` | `boolean` |
| `custom.vorm` | `single_line_text_field` |

## Gecontroleerd vervolgonderzoek (niet uitgevoerd in deze documentatieronde)

1. Selecteer per merk/productklasse een actieve en een concept-/draft-SKU; controleer Online Store-publicatie en variant/prijs.
2. Lees per geselecteerd product zowel `product.metafields.custom.*` als `product.metafields.specs.*` (alleen uitlezen). Noteer key, type, daadwerkelijke waarde, herkomst en beschikbaarheid.
3. Bepaal uit code- en runtime-rendering welke velden op de huidige productpagina zichtbaar zijn; onderscheid `main-product.liquid`/actieve snippets van de legacy secties `product-specs.liquid` en `short-specs.liquid`.
4. Controleer of EAN, fabrikantnummer, afwerking, installatie-/douchespecificaties onder een andere namespace of in native velden zijn opgeslagen.
5. Maak een mappingtabel per leverancier: `bronkolom → Shopify namespace.key → datatype/eenheid → PDP/filter/search → validatie`; gebruik `docs/PRODUCT_DATA_CONTRACT.md` alleen als conceptueel kader.
6. Pas **pas na goedkeuring** databron of Liquid aan. Geen automatische bulkcopy tussen namespaces, geen kunstmatige defaults, geen spec uit een titel afleiden.
7. Test productspecificatietabel, plus/minpunten, filterindex, SEO en variantselectie na elke mappingwijziging.

