# Wastafelkranen — eerste inhoudelijke steekproef

12 november 2026 · SEO-S06 / READ_ONLY_SAMPLE_COMPLETED.
Eigenaar kiest in een nieuwe chatvertakking ander werk terwijl Lagoo elders wordt aangevuld. Dit is een afgebakende inhoudscontrole, geen bewijs dat wastafelkranen commercieel de beste SEO-cluster zijn. SEO-S05-clusterkeuze blijft open.

## Scope en bewijs

Negen bestaande kranen: drie Hotbath, drie BRAUER, twee JEE-O en één Wiesbaden. Gerichte convenience-steekproef, geen willekeurige of complete categorie-audit. Eén extra gevonden JEE-O-wastafel is op producttype uitgesloten.
Alle negen via actuele Shopify Admin-API gelezen, daarna publieke pagina HTTP200 en server-HTML bekeken. Geen browser-, fysieke telefoon-, cart-, checkout-, fabrikantwaarheid-, ranking- of Rich Results Test-vrijgave.

MAIN vers gelezen: 196542005514, BadkamerCity - Brauer keuzemenus 11 nov. Bestaand UNPUBLISHED-specificatieconcept 196557144330 is zichtbaar; geen van beide beschreven of gepubliceerd.
Geen lokale repository/Windows-werkmap aanwezig in deze sessie; alleen connector-reads en GitHub-documentatie. Themabron blijft shopify/current op fix/product-cards-2026-10-14.

## Gecontroleerde artikelen

| SKU | Productpagina | Bevinding |
| --- | --- | --- |
| 29.4114 | [Wiesbaden Caral](https://badkamercity.nl/products/wiesbaden-caral-wastafelkraan-met-draaibare-uitloop-chroom-29-4114) | Concrete omschrijving, montage-/aansluitgegevens en lijntekening in publieke HTML. Geen complete technische juistheidsvrijgave. |
| B078WCR | [Hotbath Buddy](https://badkamercity.nl/products/hotbath-buddy-b078w-wastafelmengkraan-vloermontage-chroom) | Omschrijving noemt vooral artikelnummer, chroom en messing. Publieke tabel bevat veel meer gegevens. custom.complete_specificaties is gevuld als gegroepeerde JSON. |
| CB078WCR | [Hotbath Cobber](https://badkamercity.nl/products/hotbath-cobber-cb078w-wastafelmengkraan-vloermontage-chroom) | Generieke omschrijving en installatieadvies over inbouwdeel/aantal uitgangen. Publieke specificatietabel toont alleen artikelnummer en merk. custom.complete_specificaties ontbreekt. |
| CX078WCR | [Hotbath Cobber X](https://badkamercity.nl/products/hotbath-cobber-x-cx078w-wastafelkraan-vloermontage-chroom) | Omschrijving noemt concrete maten en coldstart; publieke tabel alleen artikelnummer en merk. custom.complete_specificaties ontbreekt. |
| 5-S-329 | [BRAUER Stripe](https://badkamercity.nl/products/brauer-standaard-stripe-inbouw-wastafelkraan-met-gebogen-uitloop-en-afdekplaat-model-a1-mat-zwart-5-s-329) | Omschrijving herhaalt vrijwel de titel. Publieke tabel toont identiteit, glansgraad en materiaal; maat-/montage-informatie in deze HTML-steekproef beperkt. |
| 5-CE-001 | [BRAUER lage kraan](https://badkamercity.nl/products/brauer-standaard-lage-opbouw-wastafelkraan-model-a-chroom-5-ce-001) | Korte titelachtige omschrijving; publieke tabel identiteit/glansgraad/materiaal. Coldstart-pluspunt aanwezig. |
| 5-CE-004 | [BRAUER inbouwkraan](https://badkamercity.nl/products/brauer-standaard-inbouw-wastafelkraan-met-gebogen-uitloop-en-rozetten-model-a1-chroom-5-ce-004) | Korte titelachtige omschrijving. Inclusief inbouwdeel staat wel als pluspunt en tabelwaarde. Niet als ontbrekend onderdeel opvoeren. |
| 500-1750 | [JEE-O Flow hoog](https://badkamercity.nl/products/jee-o-flow-opbouw-wastafelkraan-met-eengreepsmengkraan-geborsteld-rvs-hoog-41cm-500-1750-76e99d10) | Uitgebreide tabel; omschrijving bespreekt ook andere montages/modellen. Harde krasbestendigheidsclaim vraagt fabrikantbewijs. |
| 700-1502 | [JEE-O Soho](https://badkamercity.nl/products/jee-o-soho-wand-wastafelmengkraan-met-progressieve-cartrigde-en-inbouwdeel-hammercoated-zwart-rvs-700-1502-087d6ff4) | Uitgebreide tabel en inclusief inbouwdeel vermeld. Publiek aandachtspunt adviseert autowas; fabrikantonderhoudsvoorschrift eerst controleren. Progressieve cartridge/regeling evenmin vrijgeven vanuit eigen copy alleen. |

Lege Admin-SEO-velden bij BRAUER betekenen geen ontbrekende publieke meta description: bij alle drie rendert het thema een beschrijving. Twee publieke BRAUER-paginatitels worden afgekapt midden in de formulering; dit is een presentatiebevinding, geen bewezen rankingoorzaak.

Alle drie Hotbath-producten hebben leeg Admin-productType. Dit bewijst niet dat collectieplaatsen of filters ontbreken; die zijn hier niet geïnventariseerd.
custom.complete_specificaties=null bewijst alleen dat dit specifieke veld ontbreekt, niet dat alle andere namespaces of oorspronkelijke leveranciersbestanden leeg zijn. Bij B078WCR klopt het bestaan van de JSON met de uitgebreide publieke tabel; dat geeft geen toestemming om diens waarden naar CB/CX te kopiëren.

## Eerste herstelprioriteit en hervatpunt

Eerst CB078WCR en CX078WCR: bestaande bronbestanden, individuele metafields en renderroute vergelijken met de zichtbare tabel. Pas daarna bepalen of data ontbreken of de mapping onvolledig is. Geen nieuwe volledige scraper/import, geen B078W-waarden op verwante modellen projecteren. Technische eigenschappen en setinhoud per exact fabrikantnummer bevestigen.
Daarna B078WCR-customertekst en JEE-O-claims/onderhoud controleren. BRAUER-specificaties behouden hun afzonderlijke bestaande werkstroom; geen tweede schrijver of concurrerend concept.

Geen product-, prijs-, voorraad-, publicatie-, Google-kanaal- of themamutaties. Geen categoriebrede SEO-claims. Geen uitgevoerde correctie claimen.

## Voortgang

SEO-S06: kleine verkennende steekproef afgerond; volledige bronvergelijking en proefgroepkeuze open. SEO-S05 niet afgerond. SEO-S03-restpunten en Merchant-sync blijven open; volgens laatste eigenaarbeeld zijn geen accountbrede installatie-/beleidsproblemen zichtbaar, geen onafhankelijke Merchant-controle in deze sessie.
Lagoo blijft bij de andere chat. Totale SEO-voortgang blijft 1/20 DONE.

**Exact één volgende handeling:** bij CB078WCR/CX078WCR de bestaande bron- en metafielddekking onderzoeken voordat correctie wordt voorbereid. Geen actieve Shopify-schrijver na overdracht.
