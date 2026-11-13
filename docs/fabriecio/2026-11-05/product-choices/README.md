# Fabriecio — gekoppelde productkeuzes

Datum: 5 november 2026. Status: **VERIFIED_ADMIN / PREVIEW_VERIFIED / OWNER_REVIEW_PENDING / NOT_PUBLISHED**. De productvelden zijn toegepast en teruggelezen; de echte Malmö-pagina werkt in het ongepubliceerde concept.

De eigenaar vraagt dezelfde productkeuzes als Fabriecio, weergegeven met de bestaande Hotbath-bediening. Ieder Fabriecio-artikel behoudt zijn eigen product-ID, SKU en Shopify-URL. De producten worden niet samengevoegd tot één variantproduct. Automatische feedsynchronisatie is expliciet uitgesteld.

## Bron en gecontroleerde omvang

De openbare Fabriecio-productsitemap leverde 861 productpagina's. De collector heeft van alle 861 artikelen de bronidentiteit vastgesteld; bij één ontbrekende paginacode is de exacte B2B Store API-permalink/SKU gebruikt. De echte `iconic-wlv-variations`-links zijn de bron voor productrelaties. De CSV-feed en gelijkende titels zijn geen bewijs dat twee artikelen bij elkaar horen.

De bron bevat 727 artikelen met keuzemenu's in 82 gekoppelde families en 134 artikelen zonder menu. De volledige broncapture is privé. De gekoppelde bestaande Shopify-inventaris bevat 861 artikelen: 851 `ACTIVE`, tien `ARCHIVED`; geen actieve Shopify-SKU ontbreekt in de bron.

| Actieve artikelen in het plan | Aantal |
| --- | ---: |
| Gecontroleerd keuzemenu | 665 |
| Keuzemenu op HOLD wegens bronfouten | 53 |
| Geen keuzemenu bij Fabriecio | 132 |
| Alleen een gearchiveerde tegenhanger | 1 |
| Totaal actief | 851 |

Voor alle 851 actieve artikelen is de brongebaseerde leveringspayload opgeslagen en exact teruggelezen. In totaal zijn 1.516 nieuwe JSON-velden toegepast: 665 keuzes en 851 leverinformatie. De nulmeting, alle 61 vervolgbatches en de vier-artikelenproef zijn privé vastgelegd; nul userErrors. De tien gearchiveerde artikelen blijven buiten de schrijf- en navigatiescope. Het plan verandert geen prijs, voorraadhoeveelheid, voorraadbeleid, artikelstatus, producthandle, media of gegevens van andere merken.

De eerste proef omvat Malmö `VSB_2001` t/m `VSB_2004`: Wit/Mat Wit en 170×80/180×85 cm. De bron meldt de witte baden beschikbaar en voor de matwitte baden letterlijk `Verwacht: Week 50`; er is geen kalenderdatum of levergarantie toegevoegd.

## Bewuste uitzonderingen

Er zijn 26 bronlinks gevonden die naast de gekozen eigenschap ook een andere eigenschap veranderen. Twee volledige families, samen 53 actieve artikelen, blijven daarom zonder nieuw geactiveerd keuzemenu:

- Zeven Berlin-glijstanguitvoeringen: een kleurkeuze kan naar een andere lengte wijzen.
- 46 TOP-bladen: sommige kleurkeuzes verwijzen naar een andere bladlengte.

De concrete bronkeuzes en werkelijke bestemmingen staan in het privéplan onder `holds`; zij worden niet automatisch gecorrigeerd op grond van namen of aannemelijke combinaties.

Drie bestaande actieve glijstangen melden op de actuele bron `Nooit meer leverbaar`: `BR-7008-100`, `BR-7008-80` en `BR-7008-90`. De leveringspayload geeft dit expliciet aan, maar de productstatus wordt niet automatisch gearchiveerd. `FAB_1006` heeft alleen gearchiveerde tegenhangers en krijgt geen nieuwe actieve productlink. Twee verschillen tussen bronbeschikbaarheid en Shopify-aantal/voorraadbeleid blijven afzonderlijke voorraadwaarschuwingen; deze menu-opdracht wijzigt die voorraad niet.

## Aansluiting op het bestaande thema

Actieve codebranch: `fix/product-cards-2026-10-14`. Themabron: `shopify/current/`. De relevante bronbestanden zijn vóór wijziging vergeleken met de verse MAIN-bestandschecksums. Gedeelde Hotbath-JavaScript en CSS blijven inhoudelijk gelijk; Fabriecio krijgt een afgeschermde merkadapter voor dezelfde engine.

| Onderdeel | Werking |
| --- | --- |
| `snippets/bc-fabriecio-choices.liquid` | Leest expliciete Fabriecio-bestemmingen en gebruikt dezelfde compacte kleur- en keuzeweergave |
| `snippets/bc-fabriecio-delivery.liquid` | Toont eigen leveranciersstatus, expliciete verwachte weektekst of levering op aanvraag; vervangt alleen voor Fabriecio de vaste 8–9-wekenfallback |
| `sections/main-product.liquid` | Routeert uitsluitend Fabriecio naar de nieuwe adapters |
| `custom.fabriecio_choices` | Merchant-owned JSON met per pagina de werkelijk aangeboden keuzes en hun bestaande product-URL's |
| `custom.fabriecio_delivery` | Merchant-owned JSON met bronstatus, verwachting, vervallenmelding, URL en bronmoment |

De grootste bronfamilie telt 72 artikelen. De schrijfbare payloads bevatten maximaal elf actieve rechtstreeks aangeboden bestemmingen per pagina. Een keuze opent de echte bestemmings-URL en laadt daar het eigen menu. Zo worden geen niet-aangeboden combinaties bijgemaakt. De Liquid-adapter ondersteunt daarnaast validatie in blokken van vijftig zodat een grotere payload niet stil wordt afgekapt.

De poging om nieuwe product-metafielddefinities toe te voegen werd door Shopify afgewezen omdat de limiet van 256 definities is bereikt. Er is geen bestaande definitie verwijderd of gewijzigd. De twee nieuwe velden worden ongestructureerde JSON-velden, zoals de bestaande Lagoo-route; de aangepaste Liquid-weergave is daarmee getest. Voor aantoonbaar lege velden worden writes beschermd met `compareDigest: null`, gevolgd door read-after-write.

## Themastatus en publicatiegrens

- MAIN **196116087050 — BadkamerCity - Lagoo foto's en productkeuzes** bleef live; alle 1.378 bestanden zijn na uitvoering gelijk aan de nulmeting.
- Concept **196227170570 — BadkamerCity - Fabriecio productkeuzes**, rol `UNPUBLISHED`, volledig verwerkt vóór upload. Eerst 1.378/1.378 checksums identiek aan MAIN.
- Eindstand concept: 1.381 bestanden. Exact drie gewijzigde bestaande paden (main-product en twee locales) en drie nieuwe paden (twee Fabriecio-snippets en één inactieve QA-template).
- Alle zes uiteindelijke featurebestanden exact op MD5 teruggelezen. Gedeelde Hotbath-JavaScript/CSS ongewijzigd. Beschermde settings_data.json niet geüpload.
- De tijdelijke iframe-testtemplate kon niet via `themeFilesDelete` worden verwijderd: de koppeling blokkeert deze operatie als destructief. Veilig alternatief toegepast en teruggelezen: `page.bc-fabriecio-qa.liquid` bevat uitsluitend `{% section 'main-page' %}`; geen frames, testdata of actieve QA-route. Dit ongebruikte bestand wordt niet aan een Page toegewezen.
- Geen themapublicatie uitgevoerd. De bestaande standaard preview-offerteactie is niet nieuw geactiveerd.

Volledige finale Admin-readback: 861 producten gelezen; 665 keuzes en 851 leverinformatie exact; nul wijzigingen in vergeleken handle, titel, vendor, status, variant-ID/SKU/prijs/voorraadbeleid/-aantal en featuredMedia. Gearchiveerde artikelen behouden.

De eerste echte previewcontrole vond een extra renderpoort voor single-SKU-producten. Die poort is gericht aangevuld; de regressietest rendert nu de werkelijke sectievoorwaarde met een defaultproduct zonder legacy-groep. Daarna verschenen de menu's aantoonbaar op de Shopify-pagina.

## Uitgevoerde lokale controles

| Controle | Resultaat en grens |
| --- | --- |
| Builder | 14 tests PASS: onder meer foutieve kruislinks, onveilige/ontbrekende URL's, dubbele SKU's, gearchiveerde bestemmingen, expliciete weekverwachting en 72-artikelfamilie |
| Extractor | Drie tests PASS, inclusief uitsluiting van verborgen bundelonderdeelvoorraad en SKU-bewijs |
| Werkelijk bronplan met gedeelde switcher | 5.425 keuzecontroles en 4.096 navigaties PASS volgens onafhankelijke runtimecontrole |
| Leveringsweergave | Negen gerichte rendergevallen PASS volgens de adaptercontrole |
| Concept/echte browser | PASS op 1363 CSS-pixels: Malmö 170 wit → 170 mat wit → 180 mat wit → 180 wit; echte URL, juiste kleur/maatselectie, eigen prijs en beide swatches geladen; geen horizontale overloop |
| Mobiele keuzecomponent | PASS in echte Chrome-frames op 320 en 390 CSS-pixels: vier zichtbare keuzeknoppen, twee geladen swatchbeelden en geen horizontale overloop. Geïsoleerde servergerenderde component, geen volledige mobiele paginavrijgave |
| Fysieke telefoon / winkelwagen / checkout | NOT_TESTED; bestaande publieke Uitverkocht-blokkade blijft zichtbaar |
| Officiële Theme Check | Alle zes featurefiles geldig; main-product heeft drie niet-blokkerende bevindingen (complexiteit, bestaande ongebruikte seo_media en continue). Bundled fallback-documentatie gebruikt waar update-downloads time-out gaven |

De volledige runtime-uitvoer, bronpagina's, Admin-inventaris en mutation/readback-antwoorden blijven privé. Lokale DOM-/Liquid-controles bewijzen geen fysieke telefoon-, volledige checkout- of bestelbaarheidsvrijgave.

## Herstel

De publiek gebruikte MAIN-bestanden worden niet geschreven. Een conceptwijziging wordt hersteld door alleen de benoemde featurepaden terug te zetten naar de vooraf vastgelegde MAIN-versie; beschermde `config/settings_data.json` blijft buiten uploads. Ongebruikte nieuwe snippets mogen in een ongepubliceerd concept blijven staan.

Voor productvelden: bewaar de nulmeting, het exacte schrijfplan en de readbacks privé. Herstel is een afzonderlijk expliciet geautoriseerde operatie die uitsluitend de twee nieuw aangemaakte Fabriecio-velden verwijdert, nadat is bevestigd dat hun huidige waarden nog bij deze uitvoering horen. Er wordt geen generieke metafieldverwijdering of automatische rollback uitgevoerd. Bestaande velden, prijzen, voorraad en andere merken blijven behouden.

## Open en volgende stap

De eerder gevonden afwijking tussen leveranciersvoorraad en openbare Shopify-bestelbaarheid blijft een afzonderlijk commerceprobleem. Deze keuzemenu-opdracht is geen claim dat winkelwagen/checkout daarmee zijn hersteld. De periodieke feedkoppeling is op eigenaarsverzoek uitgesteld.

**Exact één volgende handeling:** Jackson bekijkt het concept **BadkamerCity - Fabriecio productkeuzes**, te beginnen bij Malmö. De 53 bronafwijkingen en de bestaande Uitverkocht-blokkade blijven afzonderlijke open taken; automatische synchronisatie blijft uitgesteld. Geen actieve schrijver na overdracht.

Herhaalbare hulpmiddelen: [scripts en opdrachten](../../../../scripts/fabriecio/README.md). De centrale status en vaste main-ingang worden uitsluitend door de hoofdtaak bijgewerkt.
