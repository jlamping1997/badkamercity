# Systemen, bronnen en de daadwerkelijke opbouw

**Bronmoment: 28 oktober 2026.** Dit register maakt onderscheid tussen vers gelezen code, bestandsmetadata en historische operationele beschrijvingen. Het bevat geen tokens, klantdata of privéserverconfiguratie.

**Vervolg DOC-01/02A:** volledige broninventaris + private productexport zijn vastgelegd. [Componentdossiers](components/README.md), [fundament/tooling](components/FOUNDATIONS_AND_TOOLING.md) en [routematrix](ROUTE_RENDERER_MATRIX.md) geven de actuele verdieping. De vroegere nulmeting is daarmee aangevuld, niet een nieuwe volledige runtimevrijgave.

## 1. Gebruikte techniek

| Onderdeel | Aangetroffen opbouw | Bewijs en grens |
| --- | --- | --- |
| Winkel | Shopify Online Store 2.0, winkel `fpa9hu-i3.myshopify.com`, publiek `badkamercity.nl` | Verse theme-query; winkelinstellingen/abonnement niet volledig opnieuw gelezen |
| Themafundament | Dawn; metadata `theme_version: 15.4.1` | `config/settings_schema.json` uit Git is checksumgelijk aan het verse live manifest. Dit is de vermelde basisversie, geen claim dat alle maatwerkcode standaard Dawn is |
| Rendering | Liquid layout, JSON-templates, secties en snippets | Git-root volledig geïnventariseerd; actuele live layout, algemene PDP en Sunshower-template/sectie ook inhoudelijk gelezen |
| Interactie | Gewone JavaScript-bestanden en custom elements; bestaande Dawn cart- en productcontracten plus maatwerk | Actuele switcher-, Sunshower-, filter- en cartbestanden gelezen. Geen React/Hydrogen-migratie voorgesteld |
| Vormgeving | Globale CSS, componentassets, inline Liquid-styles, afzonderlijke merk-/functiestijlen | Huidige opbouw vraagt cascade-/laadvolgordeonderzoek. Losse stylesheets zijn niet per definitie een duplicatie |
| Productdata | Shopify-producten/varianten, SKU's, prijzen, media, metafields; aanvullende JSON-keuzedata en exacte relaties | Private DOC-01-export: 11.343 producten/varianten; schema en scope in PRODUCT_DATA.md; externe/app-private bronnen uitgesloten |
| Sunshower afbeeldingen | Eigen galerij/carrousel; viewer-module verwijst naar `bc-photoswipe.esm.js` | Actuele moduleheader vermeldt PhotoSwipe 5.4.4; bronheader gelezen, geen volledige licentie-/kwetsbaarheidsaudit |
| Zoeken en filters | Shopify-routes plus externe filter-/zoekfrontend met API-basis `/verified` op een OVH-host | Actuele snippet en frontend gelezen. Welke collecties/staten werkelijk extern renderen, API-health en indexactualiteit niet nu end-to-end bewezen |
| Externe index | Typesense/VPS volgens bestaande dossiers en `scripts/filter-sync/README.md` | Historische/offline documentatie, geen nieuwe server-, synchronisatie- of schedulerclaim |
| Ontwikkelhulpmiddelen | Python-, Node- en PowerShell-tools; tests per dossier | Geen centraal runtimepakket veronderstellen. Bestaande wrapper noemt Shopify CLI **4.6.1 als projectbaseline**; geïnstalleerde CLI niet opnieuw vastgesteld |
| Nieuwe inventarisatiescanner | Python standaardbibliotheek; deze ronde op Python 3.12.14 uitgevoerd | Geen extra pakket of netwerktoegang nodig; handleiding in [SCANNING.md](SCANNING.md) |

## 2. Code- en datastromen

### Algemene productpagina

`product.json` kiest een sectie; de algemene productpagina gebruikt `main-product.liquid`. Die assembleert onder andere koopbediening, specificaties en productkeuzes via snippets en assets. Prijs, voorraad/publicatie en relaties komen uit Shopify en aanvullende expliciete datasets. De winkelwagen wordt via de bestaande cartcontracten bijgewerkt.

Voor elke wijziging moet de daadwerkelijke producttemplate-toewijzing in Shopify worden gecontroleerd. De aanwezigheid van `product.sunshower.json` bewijst niet welke producten die template gebruiken.

### Sunshower

De verse template `templates/product.sunshower.json` verwijst naar `sections/main-sunshower.liquid`. Die laadt Sunshower CSS/JavaScript, leest onder andere `bc_sunshower.source`, gebruikt een productcatalogusasset en bevat de eigen galerij en configuratiebediening. De sectie bevat expliciete vorige-/volgende-fotoknoppen en een teller. Die knoppen zijn een **fotoactie**, geen bewijs dat de gemelde inconsistentie uitsluitend daar zit.

De data-, gallery-, configuratie- en cartlogica moeten afzonderlijk worden beschreven. Gelijke afwerking kan gedeeld worden zonder productrelaties of configuratieregels samen te voegen.

### Productlijsten en zoekresultaten

Er zijn meerdere mogelijke renderpaden: native Liquid-productkaarten, zoekkaarten, externe JavaScript-lijsten, mobiele listingcode en Sunshower shopkaarten. Een aanpassing aan `card-product.liquid` raakt dus niet aantoonbaar alle kaarten. DOC-02A koppelt de renderers in de routematrix; DOC-02B moet de werkelijk zichtbare browserstaten bevestigen.

### Keuzedata

Live bevat veel `bc-choice-data-*.json`-assets. Het dossier [gedeelde keuzecode](https://github.com/jlamping1997/badkamercity/blob/fix/product-cards-2026-10-14/docs/code-cleanup/2026-10-25/README.md) beschrijft een generator, bronrevisies, router en fallback. Het aantal gegenereerde databestanden is geen aantal afzonderlijke UI-implementaties. Handmatig corrigeren van een afgeleid bestand is geen duurzame broncorrectie.

### Externe filters en index

De actuele `bc-external-filters.liquid` levert de API-basis en labels aan `bc-external-filters.js`; de frontend doet onder andere zoekverzoeken en kan kaartdata ophalen. Reconstructie moet verder gaan dan die frontend: collectieprofielen, indexschema, publicatie, uitsluitingen, indexverversing, prijsconversie, foutafhandeling en native terugval horen bij hetzelfde contract.

`scripts/filter-sync/` beschrijft voorbereiding en geïsoleerde staging. Dat is geen bewijs dat een permanente synchronisatie of productieomschakeling bestaat. Verifieer op de bevoegde server voordat een opvolger onderhoud uitvoert.

## 3. Waar ligt de waarheid?

| Vraag | Primaire bron | Wat Git niet bewijst |
| --- | --- | --- |
| Welke code draait nu? | Verse Shopify MAIN + volledig manifest + inhoudelijke snapshot | Een branchnaam, publicatienotitie of oude themakopie |
| Waar is een wijziging bewaard? | Git-commit en exact pad; ook releasedossiers meenemen | Dat de root automatisch de release bevat |
| Welke template/collectie/menu gebruikt de winkel? | Actuele Shopify-toewijzing/Theme Editor/menu | Alleen het bestaan van een JSON-template |
| Klopt een prijs, artikelrelatie of levertijd? | Shopify-waarde plus officiële bron en mapping | Titel, illustratie of testfixture |
| Welke CSS wint? | Werkelijk geladen assets en computed styles op die route/staat | Een losse CSS-regel of kleurentelling |
| Werkt zoeken met recente producten? | Shopify publicatie + indexdocument + API + storefront | Alleen ACTIVE-status of bereikbare API |
| Werkt de bestelafhandeling? | Checkout/configuratie en afgesproken operationele test | Een goed werkende cart-popup |
| Werkt de hele site mobiel? | Werkelijke viewport/bediening en fysieke telefoon waar nodig | Alleen een desktopbrowser of statisch iframe |

## 4. Buiten de themacode te inventariseren

Product-/variant-/collectie-/metafield- en metaobjectdefinities; werkelijk gevulde waarden; menu's; productpublicatie; collectie- en paginabody's met inline HTML/CSS/JS; app embeds/blocks; Search & Discovery; markets/talen/valuta; redirects/domeinen; consent/pixels; checkout/shipping/tax/payment; leverancierbestanden en importcode; VPS/backend/index/jobs/back-ups; analytics en Search Console.

Dit zijn onderzoeksingangen, geen verklaring dat al die systemen zijn aangesloten of actief. Per bron vastleggen: zakelijke rol, beheerlocatie, toegang nodig, versie/tijdstip, datacontract, controle, herstelpad. Geheime waarden en klant-/orderexports blijven buiten deze publieke repo.

## 5. Wat volgt uit de nulmeting?

De oude 441-bestandenkaart blijft bruikbaar voor historische verbanden. DOC-01 heeft alle 1.262 live bestanden naast Git opgehaald; 1.261 bytegelijk, één settings-uitzondering. DOC-02A verdiept de gecontroleerde bronnen en documenteert de nog ontbrekende runtime-/backenddekking. De root wordt nu niet overschreven en er wordt geen Shopify-Git-koppeling verondersteld. De betekenis van mogelijke automatische deployments moet eerst worden vastgesteld.
