# BadkamerCity — actuele werkstatus

**29 oktober 2026 · HOME-01 — gekozen homepage met negen rondjes en actiebanners geïmplementeerd in concept.** De eigenaar geeft in de huidige conversatie expliciet opdracht om het goedgekeurde ontwerp functioneel uit te voeren. Eerdere UI-01-review blijft bewaard en geparkeerd in [de vorige werkstatus](homepage/2026-10-29/previous-work-status.md).

## Actuele uitvoering

[Implementatie, bronnen, bediening, tests en terugzetten](homepage/2026-10-29/README.md).

- MAIN: **195876815114 — BadkamerCity - Compact mobiel zoeken**, ongewijzigd door deze uitvoering.
- Concept: **195910795530 — BadkamerCity - Homepage rondjes en acties**, **UNPUBLISHED**.
- Status: **PREVIEW_READY / DESKTOP_GETEST / MOBIELE_COMPONENTLAYOUT_GETEST / NATIVE_TELEFOON_OPEN / NIET_GEPUBLICEERD**.
- Actieve branch: `fix/product-cards-2026-10-14`; start `83b6ab9ab9a5adf22150232920cb88cf42af0974`. Main uitsluitend documentatie.
- Startkopie1.318/1.318 bestanden checksumgelijk vóór writes. Alleen gerichte homepage-/footer-/locale-/beeldbestanden gewijzigd; geen volledige root-sync.

## Opgeleverd

Twee configureerbare banners met bestaande collectiedoelen; negen klikbare categorieën in3×3 op mobiel; vier werkende merkbestemmingen; USP gratis verzending boven€100; showroompartner Harry Suiker alleen voor advies/3D op afspraak; afhalen/retourinformatie en compacte homepagefooter. Header/zoeken/cart behouden. Bestaande homepage-secties disabled bewaard.

Geen boekingslink gevonden: **Vraag een 3D-afspraak aan** opent een native Shopify-aanvraagformulier; beschikbaarheidsagenda niet verzonnen. Via een homepage-instelling kan later een echte boekingslink worden gekoppeld. Geen testmail verstuurd.

## Bewijs en grenzen

Alle negen categorieroutes, vier vendorlinks, zoeken en lege cart in echte desktopbrowser geopend. Alle13 beelden laden; ankers en aanvraag-/servicedetails werken. Liquid/JSON/theme-check op de10 gewijzigde tekstbestanden geslaagd. Componentbreedtes320/390/1024 zonder horizontale overloop; dit is een geïsoleerde gerenderde componentfixture, geen volledige native mobiele header-/touchvrijgave. Echte afspraakontvangst, native telefoon en verzendtariefgrens blijven open. Geen koopactie of checkout-/verzendinstelling veranderd.

Tijdelijke QA-template veilig geneutraliseerd tot een inerte noindex-pagina nadat de connector bestandsverwijdering blokkeerde; er blijft geen testschrijver of actief testscript achter.

## Exact één volgende handeling

**Eigenaar beoordeelt concept ‘BadkamerCity - Homepage rondjes en acties’ op zijn telefoon en test één echte afspraakaanvraag inclusief ontvangst vóór publicatie.** De eigenaar publiceert volgens AGENTS.md; deze uitvoering heeft geen publicatie gedaan.

## Overdracht

Lees deze status → AGENTS.md → HOME-01-dossier. Eerdere UI-/filter-/cart-/wishlistbevindingen en settings-bytepariteitsvragen blijven afzonderlijk bestaan; deze homepage-opdracht lost die niet automatisch op. Geen Windowscontrole claimen. De Git-root is geen volledige actuele productiebron: gebruik alleen het expliciete deploymentmanifest bovenop een verse geverifieerde MAIN-kopie.
