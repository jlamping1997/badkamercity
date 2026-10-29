# FLASH-01 — stabiel eerste laadmoment

29 oktober 2026. Eigenaar meldt kort een grote blauwe pijl tijdens navigeren en een hoog blauw vlak bij de zoekbalk bij opstarten. Op expliciete opdracht wordt de laadvolgorde hersteld. De precieze oorspronkelijke flits is nog niet op zijn iPhone opgenomen; houd reproduceerbare risico's en het incidentele eigenaarsbeeld gescheiden.

## Actuele bronnen en scope

Verse Shopify-read: menuconcept195913482506 is inmiddels MAIN, gepubliceerd door eigenaar. Nieuw concept195915448586 **BadkamerCity - Stabiele header en iconen** wordt van deze MAIN gekopieerd. Actieve branch `fix/product-cards-2026-10-14`; startcheckpoint0b43825409828d583f5e709eed8e1ce892937fd6. Main alleen documentatie. Lokale checkout vóór werk schoon; geen Windowsmeting.

Status bij checkpoint: **COPY_PROCESSING / LOCAL_IMPLEMENTED / BROWSER_QA_PENDING / NOT_PUBLISHED**. Eerst volledige checksumpariteit vóór writes. Geen wijzigingen aan MAIN.

## Gevonden oorzaken en oplossing

1. `component-search.css` stond in de body/header als media=print/onload; predictive-search CSS stond ook asynchroon. De gesloten suggestiecontainer en de aangepaste loader krijgen pas in dat laatste bestand display:none/afmetingen. `loading-spinner` vervangt bij een opgegeven class de standaard hidden-klasse. Zonder de component-CSS kan die lege laadcontainer dus de header vergroten.
2. `icon-arrow.svg` had alleen viewBox, geen intrinsieke width/height. De normale maat hing volledig van CSS af. Het is een aantoonbaar risico op een groot standaard SVG-vlak als die stijl ontbreekt, niet het bewijs dat exact dit icoon de gemelde iPhone-flits veroorzaakte.

`layout/theme.liquid` laadt beide zoekstyles nu synchroon in de head, in dezelfde cascadevolgorde na base.css. De dubbele component-search-aanvraag uit header.liquid vervalt. Een klein inline `bc-first-paint` snippet staat vóór content_for_header: minimale SVG-wrapper-/pijl-/spinnermaten en een guard die gesloten suggesties verbergt. Open/loading-staten blijven door de bestaande zoekcontroller bestuurd. De pijl krijgt daarnaast width14/height10 in het SVG zelf; CSS height:auto bewaart zijn verhouding bij schalen.

Geen sitebrede verberglaag, kunstmatige wachttimer of wijziging van de zoekcontroller. Menugedrag/homepage/checkout blijven zoals gepubliceerd. Geen algemene snelheid-/Lighthouseclaim.

## Git en deployment

Vier bestanden uploaden, zie deployment-manifest.json. De huidige layout uit Shopify bevatte eerdere live-wijzigingen die nog niet in de Git-root stonden (o.a. typografie/wishlist): die zijn behouden. Drie ongewijzigde live-afhankelijkheden zijn ook in Git en de lokale validatieboom opgenomen, maar horen niet bij de Shopify-upload. De runtimekopie is geen volledige product-/Admin-export.

De bestaande bronbestanden staan met LF-genormaliseerde regeleinden als baseline-*.txt in dit dossier. Originele Shopify-checksums staan in het manifest. Terugzetten: herstel de drie oorspronkelijke bestanden; het nieuwe snippet kan ongebruikt blijven. Nooit de volledige Git-root uploaden.

## Controle bij checkpoint

ThemeCheck R2: vier bestanden zonder errors; bestaande waarschuwing over scheme_classes in de overgenomen layout blijft zichtbaar. R1 vond drie bestaande live-afhankelijkheden die in de onvolledige lokale runtimekopie ontbraken; ze zijn uit MAIN gelezen voor R2. Browsercontrole, gecontroleerde ontbrekende-CSS-vergelijking, werkend zoeken en directe navigatie moeten nog volgen. De oorspronkelijke flits op de fysieke iPhone is nog niet geverifieerd.

## Exact volgende handeling

Voltooi kopiepariteit, upload de vier bestanden naar het concept en voer de gecontroleerde opstartvergelijking plus zoek-/navigatieregressie uit. Geen publicatie door deze sessie.
