# Verlavio — inbegrepen onderdelen van douchesets

5 november 2026 · VERLAVIO-SET-01 · uitvoering op expliciet verzoek van de eigenaar.

## Resultaat

78 bestaande Verlavio-douchesets hebben het bestaande blok **Deze set bestaat uit** gekregen: 36 Milaan, 36 Palermo en 6 Porlezza. Samen 462 inbegrepen onderdelenregels en 108 unieke losse artikelen. Iedere regel noemt aantal, beschrijving en artikelcode en verwijst naar het exacte losse artikel; afbeelding waar beschikbaar, losse verkoopprijs en bestaande componentleverinformatie komen uit dat artikel. De introductie maakt duidelijk dat de onderdelen inbegrepen zijn en dat de getoonde prijzen losse prijzen per stuk zijn.

Alle onderdelen zijn rechtstreeks bevestigd door verplichte leveranciersbundelregels met expliciete aantallen. Alle 78 leverancierspagina's zijn opnieuw gelezen en kwamen exact overeen. Related products, foto's of optionele suggesties zijn geen bron voor deze lijsten. De zichtbare merknaam blijft Verlavio.

Twaalf Venetie-regendouchesets zijn niet aangevuld: productpagina's, feed en onderzochte leveranciersdocumentatie geven geen expliciete onderdelenlijst. Bron-HOLDs: BC_2001, BC_2002, BG_2001, BG_2002, BKK_2021, BKK_2022, CKK_2027, CKK_2028, GM_2001, GM_2002, RVS_2001, RVS_2002. Volgende inhoudelijke stap: bevestigde samenstelling voor deze twaalf artikelen verkrijgen; geen onderdelen raden.

## Techniek en grenzen

Data-only uitvoering op bestaande producten: uitsluitend `bc_data.set_components` (json) en `bc_data.component_products` (list.product_reference), bestaande definities hergebruikt. De 156 velden waren aantoonbaar afwezig en zijn met `compareDigest: null` geschreven en exact teruggelezen. Status `VERIFIED_DESCRIPTION`; iedere regel heeft exact product-ID, variant-ID, SKU, positief aantal en beschrijvende `short_title`.

De bestaande route is `main-product → bc-product-set-components → bc-product-set-verified → bc-product-set-item`. Alle zeven onderzochte live bronbestanden inclusief CSS/locale zijn bytegelijk aan `shopify/current/`. MAIN bleef **196238639370 — BadkamerCity - Re-Bel tegelkeuze**. Geen theme-write, nieuw conceptthema of publicatie nodig. Hotbath IBS70CR347 behield exact zijn acht oorspronkelijke onderdelen.

De renderer verbergt de hele lijst als één component niet exact overeenkomt met de gekoppelde producten, variant-ID, SKU, vendor of toegestane verificatiestatus. Setvoorraad en setprijs blijven onafhankelijk van losse onderdelen. Het blok voegt geen losse artikelen aan de winkelwagen toe. Bronvoorraad is niet uit de onderdelen opgeteld.

## Controle en herstel

Volledige read-after-write van de 861 Verlavio-producten bevestigt alle 78 lijsten exact. Alle overige vastgelegde velden en producten bleven gelijk, inclusief prijs, SKU, variant-ID, handle, vendor, status en leverancierleverinformatie. Herhaalde builder tegen de nieuwe inventaris levert nul writes, 78 identieke sets en 12 bron-HOLDs.

Alle 78 live productpagina's geven HTTP 200 en exact één juist onderdelenblok. Alle 462 aantallen, omschrijvingen, artikelcodes en exacte product-/variantlinks komen overeen met het plan. Hoofd- en losse componentprijzen sluiten aan op de Admin-inventaris; geen nulprijzen of winkelwagencontrols in het onderdelenblok. Componentlevermeldingen sluiten aan op de vastgelegde velden. De twintig niet-voorraadsets kregen geen belofte van 1–2 werkdagen.

Echte desktopbrowser op `https://badkamercity.nl/products/fabriecio-ckk-2015` bij 1363 px: zes juiste regels, zes exacte variantlinks, duidelijke inbegrepen-/losse-prijstekst, geen winkelwagenknoppen binnen de lijst. Screenshot vastgelegd. Mobiele browserbediening en echte aankoop zijn in deze taak niet uitgevoerd; bestaande mobiele CSS is ongewijzigd hergebruikt.

De openbare `verification.json` bewaart uitsluitend scope, productidentiteiten en veldhashes voor gecontroleerd herstel. Ruwe leveranciers-HTML, Admin-export, schrijfplan en API-antwoorden blijven privé. Terugzetten: lees eerst de huidige waarden van uitsluitend deze 78 product-ID's; verwijder de twee toegevoegde velden alleen als hun inhoudshashes nog overeenkomen met de vastgelegde uitvoering. Bij afwijking eerst handmatig beoordelen. Oorspronkelijke waarden waren afwezig. Geen productverwijdering of themawissel nodig.

## Opnieuw voorbereiden

De twee hulpscripts zijn read-only ten opzichte van Shopify. Gebruik een privéwerkmap buiten de publieke repository en een verse Admin-inventaris met `publishedAt`, exacte varianten en bestaande veldwaarden. Schrijven blijft een afzonderlijke gecontroleerde stap. Bestaande conflicterende velden geven HOLD; identieke waarden worden overgeslagen.

```sh
python scripts/fabriecio/collect_set_components.py --catalog ../fabriecio-private/normalized-catalog.json --html-dir ../fabriecio-private/html --output ../fabriecio-private/set-source.json --verify-live
python scripts/fabriecio/build_set_components.py --source ../fabriecio-private/set-source.json --shopify ../fabriecio-private/shopify.json --output ../fabriecio-private/set-plan.json
```

De collector vereist verplichte bundelregels, expliciet positieve aantallen en exacte bron-URL-koppelingen. De builder vereist één gepubliceerde actieve Verlavio-variant per artikel, unieke SKU's, bronbewijs en beschrijvende titels. Beide schrijven UTF-8. Dit voegt geen periodieke onderdelen- of voorraadsynchronisatie toe; latere imports moeten deze velden bewaren en gewijzigde leverancierssamenstellingen opnieuw laten controleren.
