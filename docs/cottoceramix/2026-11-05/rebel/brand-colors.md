# COTTO-02 — Cottoceramix en uitklapbare tegelkleuren

5 november 2026. **ADMIN_APPLIED_VERIFIED / PREVIEW_VERIFIED / AWAITING_MERCHANT_PUBLICATION.**

De eigenaar wil Cottoceramix als winkelmerk voor de 22 Re-Bel-pilotartikelen en een kleurmenu zoals de bestaande Hotbath-keuze, met echte vierkante tegelafbeeldingen.

## Resultaat en gegevens

Alle 22 bestaande producttitels beginnen nu met Cottoceramix. Vendor en de zichtbare specificatie Merk zijn Cottoceramix; beschrijving, SEO en alle 70 afbeeldings-altwaarden sluiten daarop aan. De bestaande naam Revoir Paris blijft na het voorvoegsel in de titel staan, volgens “voeg overal voor toe”; Re-Bel blijft het bestaande serie-/keuzegroepslabel. Het oorspronkelijke leveranciersmerk blijft intern herleidbaar via `tiles.source.original_brand`; `store_brand` is Cottoceramix.

Volledige Admin-voor-/navergelijking: 22 artikelen en 70 beelden, nul afwijkingen van het uitvoerplan. Product-/variant-ID's, SKU's, handles, status, Webshop-publicaties, prijs/einheidsprijs, verpakking, gewicht, voorraadbeleid, collecties en afbeelding-ID's/URL's zijn behouden. Geen nieuwe metafielddefinitie of categorie gemaakt. Volledige herstelkopie en readbacks zijn privé bewaard.

## Herbruikbaar kleurmenu

- Opt-in via `custom.bron_toelichtingen_json.tiles.color_picker_layout = "expandable_grid"`.
- Vier keuzes in vier kolommen. Als de geselecteerde kleur verderop staat, vervangt die de vierde keuze.
- “Bekijk alle 11 kleuren” met +7 opent alle elf in bronvolgorde; “Minder kleuren” sluit ze.
- Echte productafbeeldingen van de tegels, vierkant met een subtiele hoekafronding. Geselecteerde tegel krijgt een rand/vinkje en vet label.
- Open/gesloten toestand blijft per serie in sessionStorage bij kleur-/formaatnavigatie behouden. Bij geblokkeerde opslag blijft de bediening werken.
- Bestaande tegelgroepen zonder opt-in behouden hun rail. Tot vier kleuren is geen uitklapknop nodig. De bestaande NL-/EN-vertalingen worden hergebruikt.
- De gedeelde bestaande Liquid-/JavaScript-/CSS-component is uitgebreid; geen kopie van de Hotbath-configurator.

Bron: `shopify/current/snippets/bc-porcelanosa-buybox.liquid`, `assets/bc-porcelanosa-buybox.js` en `assets/bc-porcelanosa-buybox.css`.

## Bewijs en grenzen

Zes semantische controles in `scripts/component-audit/cotto-color-grid.mjs` PASS; de zeven bestaande pilotcontroles inclusief 286 productwissels en doosberekening blijven PASS. De drie gewijzigde productbestanden en de tijdelijke controletemplate zijn door de Shopify Liquid-validator goedgekeurd; de validator gebruikte meegeleverde documentatie waar online documentatie niet bereikbaar was.

Echte Chrome-preview: Perle blijft zichtbaar bij inklappen, alle elf foto's laden bij openklappen, Blanc → Perle en 60 → 100 cm navigeren naar het juiste artikel met behoud van de andere keuze en open toestand. RR1008 toont €79,95/m² en €159,90 per doos van 2 m². Dezelfde echte component is ook binnen kaders van 320 en 390 CSS-pixels getest: vierkant beeld, vier kolommen, elf open keuzes, geen horizontale overloop. Dit is componentbreedtecontrole, geen volledige mobiele PDP- of fysieke telefoontest. Cart/checkout/betaling zijn niet opnieuw uitgevoerd voor deze merk-/menupatch; de eerdere COTTO-01-cartproef blijft het gedateerde bewijs.

De preview-only controletemplate `templates/page.cotto02-grid-check.liquid` is na controle teruggebracht tot gewone page-rendering zonder testproducten, testformulieren of controlescherm. De connector weigert elke themeFilesDelete generiek; daarom is geen verwijderingsomweg gebruikt. De inactieve template is mee opgeslagen voor exacte bronpariteit en is aan geen pagina toegewezen.

## Thema, integratie en herstel

MAIN blijft **196227170570 — BadkamerCity - Verlavio voorraad en levertijd**: volledige 1381/1381-checksumvergelijking gelijk aan de eerdere nulmeting. Alleen het bestaande **UNPUBLISHED196238639370 — BadkamerCity - Re-Bel tegelkeuze** bevat de nieuwe kleurweergave. Geen publicatie door uitvoerder.

De finale inventaris heeft 1383 conceptbestanden en elf afwijkingen tegenover MAIN: vier bestaande cartbestanden, drie COTTO-02-productbestanden, de inactieve controletemplate en drie actuele SEARCH-01-bestanden. De gelijktijdige zoekcorrectie in codecheckpoint `05a54c8d8b7df8c41644eec7abd5bd812a3cb6d5` is behouden; COTTO-02 heeft die drie zoekbestanden niet geschreven. De oude enkele zoekhash uit COTTO-01 is dus geschiedenis, niet de huidige zoekbaseline.

Herstel van uitsluitend COTTO-02: de drie productcomponentbestanden uit de parent van deze patch terugzetten in een ongepubliceerd concept; de 22 merk-/JSON-/altvelden kunnen gericht uit de privévoorafkopie worden hersteld. Prijs-/voorraadvelden niet mee overschrijven. De ongebruikte neutrale page-template mag blijven. De eerdere winkelwagen- en nieuwste zoekwijzigingen afzonderlijk behouden.

**Exact één volgende handeling:** eigenaar beoordeelt en publiceert **BadkamerCity - Re-Bel tegelkeuze**. Daarna de verse MAIN-rol en de publieke merk-/kleurenweergave controleren. Geen actieve COTTO-02-schrijver na overdracht; verdere import en het backendindexherstel blijven afzonderlijke taken.

