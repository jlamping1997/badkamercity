# Filtervereenvoudiging — 8 november 2026

**FILTER-SIMPLE-01 · READ_ONLY_AUDIT / PROPOSAL_READY / NOT_APPLIED.** Eigenaar vraagt een diepe analyse en veel eenvoudiger kleuren: goud is goud, groen is groen. Geen Shopify-, VPS-, index- of theme-write/publicatie.

## Volledige configuratie-inventaris

Alle226 actuele collectie-URL's uit de Shopify-sitemap plus globaal profiel gelezen: **227/227**, nul fouten, dezelfde generatie20261107T080100_ca321b. **34 verschillende velden**,149 profielen met algemeen f_kleur.62 profielen zonder filters,56 daarvan zonder producten; de andere zes hebben1–18producten. Categorieën overlappen en zijn niet optelbaar. Dit is een volledige configuratie-inventaris, geen SKU-voor-SKU datavrijgave.

Globaal profiel15.897producten/shopping15.155; **1.002 exacte kleurnamen**. Tegels807, Cottoceramix792, Wastafelkranen29, Kranen50. De volledige vocabulaire is uit profile.filter_policy.color_groups gelezen, niet uit de tot100 waarden begrensde searchfacets.

## Bewezen oorzaak van lange kleurenlijsten

Bestaand beleid:13 groepen,36 ingedeelde namen,966 oningedeeld. LiveJS leest noch filter_policy.color_groups noch ui.group_source=f_kleurgroep. Alleen ui.option_groups wordt echt gegroepeerd. Dus de bestaande gedeeltelijke beleidsgroepen worden niet als basiskleuren in de sidebar toegepast.

Een snelle option_groups-patch is onvoldoende: aantallen/chips blijven rawwaarden, oude exacte URL's kunnen gedeeltelijk geselecteerde groepen tonen, onbekende kleuren worden toegevoegd en sommen van maximaal100 teruggestuurde facetbuckets kunnen onvolledig zijn. Eerst bestaande f_kleurgroep op de echte index/schema/coverage beoordelen en hergebruiken als het contract klopt. Anders één versieerbare basiskleurindeling met backend-unietellingen; geen tweede los clientregexsysteem.

## Voorgestelde eenvoudige kleurkeuze

18 winkelbrede basisfamilies: Wit, Zwart, Grijs, Beige, Bruin, Groen, Blauw, Geel, Oranje, Rood, Roze, Paars, Goud, Koper, Brons, Zilver, Transparant, Multicolor. Alleen relevante kleuren per categorie tonen. Zilver is een uiterlijkgroep voor onder andere Chroom/RVS/Nikkel/Staal, geen materiaalgelijkstelling; Gunmetal→Grijs is een expliciete vereenvoudigingskeuze. Exacte fabrikantkleuren/PVD/afwerking en koopbare keuzen behouden bij product. Glaskleur/profielkleur en kaderkleur/lichtkleur niet verwarren.

Complete privévoorstelkaart: **1.002/1.002 unieke namen behouden**;335 duidelijke naam-/vertaalvoorstellen,160 tint-/ontwerpvoorstellen,486 broncontroles en21 zonder specifieke kleur.495 toegewezen voorstellen/507open. Dit zijn namen, geen productgewogen dekking; geen productvrijgave uit een tekstregel. Onder andere Everest/C-83, turquoise/aqua/petrol, messing, brons-koper en hout-/steenhandelsnamen eerst controleren.

Wastafelkranen:25 van29 namen hebben voorstellen voor zeven basisfamilies; vier twijfelgevallen blijven open: Geborsteld messing PVD, Geborsteld messing, Verouderd messing en Geborsteld brons koper PVD. Geen automatische Goud-toekenning aan messing.

## Beperkte technische proef

Vijf voorgestelde goud-/messingrawwaarden in één OR-zoekactie: **93 found/93 returned/93 unieke IDs**. Dit bewijst het gezamenlijke zoekgedrag, niet de inhoudelijke goudclassificatie van de twee messingnamen. Geen nieuwe groepsknop of productwrite.

## Andere concrete vereenvoudigingen

- Brede Douches65 soortnamen, Badkamermeubels19, Toiletten24 en Baden27. Eerst bestaande subcategorieën; aantoonbare synoniemen bundelen. Set en onderdeel niet gelijkstellen.
- Per echte productgroep circa4–5 hoofdkeuzes; Serie onder Meerfilters. LiveJS forceert Serie nu primair en negeert searchable/value_sort. Nieuwe basiskleur-swatches vereisen ook passende presentatie.
- Bij inloopdouches breedte/glaskleur/profielkleur; meubels type/breedte/kastkleur; spiegels vorm/maat/verwarming; vrijstaande baden lengte/breedte/vorm. Geen generieke materiaal-/maatfilters op alle gemengde afdelingen.
- Baden-lengtedekking20,19% versus Vrijstaande baden85,29%: toepassing en ontbrekende data onderscheiden. Wastafelkranen-kleur91,87%, hoogte uitloop49,27%, kraangaten55,61%.
- Tegelformaat alleen uit echte productparen, geen automatische59,6→60afronding. Prijsfilter price_cents versus m²-kaartprijs eerst op eenheid controleren; geen alleen-labelcorrectie.
- Spiegeldiameter3mm en meubelmaten30/3mm zijn broncontrolepunten; niets geraden of gewijzigd.
- Telefoon: korte basiskeuze, geselecteerde opties zichtbaar, voorstel vaste ToonNproducten-knop; geen nieuwe mobiele test of conversiestijging bewezen.

## Bronidentiteit en releasegrens

VerseMAIN196328685834 en alle drie filterfiles rechtstreeks via Shopify gelezen; parent bevestigt checksums:
- JS5bc50f08e750aff663b8de6309e909ec
- CSS6e3cba08884edac08fdcf229a9fd170d
- snippetfdbb71e4463e700b721c21ee95a38331

Alle drie wijken af van actieve Git-bron. Onder meer live pageshow-handling/opacity/tijdelijke voorraadcontext behouden. **Geen implementatie starten vanuit een veronderstelde Git/MAIN-pariteit.** Eerst verse identieke UNPUBLISHED-kopie en scoped bewijs; eigenaar publiceert. Geen bronfiles overschreven door dit onderzoek. Shopify-native groeperingsdocumentatie bevestigt ontwerpprincipe, maar alleen Search & Discovery aanpassen verandert deze externe route niet.

## Privérapport en overdracht

Gebruikersrapport **Badkamercity-filteranalyse-2026-11-08.html** bevat volledige doorzoekbare1.002-namenvoorstelkaart, alle227profielen,34velden, bronnen, categorieadvies en testgrenzen. Geen ruwe productrecords of volledige mapping in publiekeGit. Inhoudelijke onafhankelijke review: geen noodzakelijke correcties.

**Exact één volgende handeling:** eigenaar beoordeelt het18-basiskleurenvoorstel; daarna de vier Wastafelkranen-twijfelgevallen gericht classificeren voor één begrensde pilot. Restartbeleid/timerbewijs uit FILTER-RESTORE-01 blijft afzonderlijk open. Eerdere homepage/bestelbaarheid/BRAUER-holds behouden. Actieve branch fix/product-cards-2026-10-14; main alleen docs. Geen actieve schrijver na checkpoint.
