# Vereenvoudigde filters — voorbereide serverrelease

8 november 2026. FILTER-SIMPLE-02 v2 / EXACT_FORMAT_CODES / RELEASE_READY / NOT_DEPLOYED.

De eigenaar geeft expliciet opdracht alle filters zelfstandig te vereenvoudigen op basis van redelijke naam-/productaanwijzingen (ongeveer 70% zekerheid); geen nieuwe kleurbevestiging vragen. Dit vervangt de eerdere reviewwacht voor het algemene kleurenvoorstel. Het is geen opdracht productmaten, prijzen of fabrikantafwerkingen in Shopify te wijzigen.

Deze release gebruikt de bestaande Verified Candidate, synchronisatieworker en staging-/activatiecontrole. Geen themawijziging of publicatie nodig: publieke velden blijven f_kleur en de nieuwe keuze f_tegel_formaat past in de bestaande checkboxrenderer. De originele private runtime is niet ingebed of publiek opgeslagen.

## Correctie v2 na echte stagingcontrole

De eerste release is door de volledige controle tegengehouden en niet geactiveerd. De read-only diagnose bevestigt: 60 × 60 cm verwacht159, query vond309 =159van60×60 +58van60×120 +92van60×150; geen ontbrekende of dubbele IDs, geen searchcutoff. Het probleem zit in de tekstselectie, niet in het formaatlabel of de bronafmetingen.

V2 behoudt de menselijke f_tegel_formaat-facet en URL, maar selecteert via een intern int32-veld f_tegel_formaat_code. Per generatie krijgt ieder gesorteerd uniek label één code vanaf1; snapshot.tile_format_codes bevat de kaart. De API vertaalt selectie naar numerieke gelijkheid of numerieke OF-lijst en behoudt de publieke clausulesleutel voor disjunctieve facetten. Code0 is gereserveerd voor onbekend: nul resultaten. Ongeldige/ontbrekende kaarten stoppen; het private codeveld staat niet in de publieke allowlist. De generatiecontext koppelt de kaart aan dezelfde index binnen ieder verzoek.

Alle132formaatselecties worden vóór activatie op volledige product-ID-set gecontroleerd, plus formaat-OF, kleur-EN-formaat en onbekende labels. Livechecks controleren60×60,60×120,60×150afzonderlijk. Schema/codekaart/productcode-bijectie wordt afzonderlijk gecontroleerd. Installer vereist variant_aliases_v1,filter_simplification_v1 én tile_format_codes_v1 vóór en na activatie en bij herhaling. De oude bronhashes blijven geldig omdat v1 niet is geactiveerd.

**51 release-/API-/worker-/installertests PASS** (23lifecycle,19API,9worker). Bestaande3.496tegelrecords behouden159/58/92gescheiden formaten. Echte nieuwe Typesense-/ASGI-/activeringstests van v2 volgen in het serverinstallatieblok; dit is nog geen livevrijgave. Andere kleur-/maat-/enumregels blijven gelijk.

## Gedrag

- 18 basiskleuren plus Overige kleuren. Mat/geborsteld/PVD verandert de kleurfamilie niet; RVS en chroom vallen onder Zilver. Meerdere zichtbare kleuren zijn per product mogelijk en Typesense telt elk product per kleur eenmaal. De 15 eigenaarregels blijven beperkt tot leverancier/serie/exacte bronkleur.
- De exacte bronkleur staat in het nieuwe indexveld f_kleur_exact. Shopify-specificaties, koopbare uitvoering en bronmetingen blijven onaangetast. Niet-herkenbare namen krijgen Overige kleuren; ontbrekende bronkleur blijft ontbrekend. Geen vrije titel-/afbeeldingsgok voor ontbrekende gegevens.
- Tegelformaat gebruikt het werkelijke maatpaar, onafhankelijk van oriëntatie. 59,6 × 59,6 wordt 60 × 60 cm. Overige herkenbare nominale paren maximaal 8 mm en 3% verschil per zijde. Mozaïek-/bijzondere vormnamen blijven exact; ontbrekende maten worden niet verzonnen. De twee exacte tegelranges blijven onder Meer filters.
- Niet-tegelmaten blijven exact met bestaande cm/mm-weergave. Soort-, materiaal- en plaatsingssynoniemen worden gegroepeerd via exact-OR; RVS 316, componenten en technische materiaaltypen blijven gescheiden.
- Legacykleurverzoeken worden via bron->primaire kleur vertaald; bestaande enkelvoudige color_value_aliases blijven frontendcompatibel. De oude nauwe kleurnaam wordt daarmee bewust een bredere basiskleurkeuze. Basislabels zijn identiteiten. Bestaande varianten/SKU-aliases, sortering en productkaarten blijven behouden.
- Nieuwe index: f_kleur string[]; f_kleur_exact optional string; f_tegel_formaat optional facetstring; f_tegel_formaat_code optional int32, intern selectiefilter. Afgeleide velden worden bij iedere reguliere synchronisatie opnieuw gemaakt. Formatfacet tot 500 waarden; andere keuzefacetten op bron-distinctcount begrensd tot 1.000. Numerieke rangefacetten behouden de bestaande limiet.

## Bewijs en beperking

51 release-/worker-/API-tests PASS, daarnaast zes kleurclassificatietests, 46 JS-asserties en acht maat-/enumtests PASS. Volledige JS/Python-pariteit over 1.022 kleurgevallen. Integratie gebruikt de aangeleverde private runtime, exact gereconstrueerd naar het geverifieerde worker-/API-checkpoint van 5 november.

De bestaande 3.496 gepubliceerde tegelrecords: 3.490 geldige formaatparen -> 132 labels; zes zonder maatpaar. 2.412 producten met herkenbare basiskleur, 523 Overige kleuren, 561 zonder gestructureerde kleur; 117 met meerdere kleuren. De 786/1.002 ingedeelde namen zijn naamdekking, geen zekerheidsscore of winkelbrede productdekking. Technische bronwaarden en identiteiten in de fixture behouden.

Geen SSH-verbinding vanuit deze uitvoeromgeving (Network is unreachable), geen serverwrite en geen wijziging in Shopify. Openbare API voor de release: ok=true, 227 profielen, collectie bc_sync_20261108t130100_bc1233, versie0.4.0. Echte nieuwe Typesense/FastAPI/ASGI-, livebrowser-, reboot- en toekomstige timerproeven zijn hier NOT_TESTED. De installer voert de bestaande volledige indexreadback, API-vergelijking en lokale/publieke activeringstests op de VPS uit voordat hij succes meldt. Eigenaartest volgt na uitvoering.

## Installeren en herstellen

Gebruik uitsluitend repair_filter_simplification.py met de SHA256 uit filter-simplification-release.json. De actuele centrale handoff geeft een downloadlink vastgezet op het codecommit. Geen oude variantinstaller of historische cleanup herhalen.

De installer controleert huidige bronhashes vóór wijzigingen, neemt het bestaande sync.lock, bewaart een private back-up, pauzeert alleen een actieve timer en bouwt een nieuwe geïsoleerde index. Hij behoudt variant_aliases_v1 en vereist filter_simplification_v1 en tile_format_codes_v1. Bestaande staging, volledige readback, eigen-generatieherstel en timerstand blijven behouden. Pas na geslaagde activatie schrijft hij de nieuwe worker voor volgende timeruitvoeringen. Een onverwachte handmatige wijziging wordt niet overschreven. Binnen dezelfde release herhalen controleert eerst of hij al is toegepast.

Back-ups: /opt/badkamercity/filter-sync/filter-simplification-backups/. Op een stage-/activatiefout behoudt/herstelt de bestaande transactie de vorige live-index en API; installer herstelt uitsluitend zijn eigen generatie. De bronindex wordt niet verwijderd. Geen automatische rollback claimen als de uitvoer handmatige controle vraagt. Deadline 900 seconden, aparte herstelgrens 240 seconden; voortgang iedere 20 seconden.

## Tests en herbouw

De installer-lifecycletests zijn zelfstandig uitvoerbaar met Python unittest. API-/workerintegratie gebruikt private bronbestanden en data buiten Git: BC_FILTER_RUNTIME_DIR (sync.py/app.py), BC_FILTER_PROFILE_DIR (gecontroleerde profiel-JSON) en BC_FILTER_TILE_CATALOG (catalog-colors.json). Zonder die bronnen worden de integratietests expliciet overgeslagen; niet als PASS claimen.

build_filter_simplification.py gebruikt --worker-source, --api-source, --worker-patch simple_worker_patch.py, --api-patch simple_api_patch.py, --output repair_filter_simplification.py en --manifest filter-simplification-release.json. De pure workerpatch bewaart de zelfstandige kleurregels en runtimehelpers als bronconstanten; pas daar de afgeleide regels aan, bouw opnieuw en test vóór een volgende release. De oorspronkelijke complete serverbron blijft privé.

**Eén volgende handeling:** eigenaar voert het vastgezette PowerShell-installatieblok uit; daarna publieke API/readbacks en de echte filters controleren. Geen nieuwe inhoudelijke goedkeuring nodig.
