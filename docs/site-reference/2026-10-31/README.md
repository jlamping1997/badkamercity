# DOC-04 — naslagwerk, praktische verdieping en verse bronkaart

31 oktober 2026. Deze ronde wijzigt alleen documentatie. Geen Shopify-, formulier-, cart-, catalogus-, prijs-, voorraad- of publicatiemutaties.

De [vaste leesbron](../../MASTER_SITE_REFERENCE.md) bevat nu 80 hoofdstukken: de bestaande 47 hoofd-/registerhoofdstukken, 32 nieuwe praktische hoofdstukken en het gedateerde productrouteregister als hoofdstuk 80. Toegevoegd: 50 beheertaken, 40 diagnosepaden en 50 acceptatiescenario’s. De bronhoofdstukken en JSON-registers staan onder [handbook/2026-10-31](../../handbook/2026-10-31/README.md).

## Verse bewijsmiddelen

| Bestand | Inhoud | Grens |
| --- | --- | --- |
| live-manifest.json | Alle 1.354 MAIN-paden, metadatahash en grootte | Geen volledige bytepariteit van alle thema-assets |
| manifest-delta.json | Vier toegevoegd, zes gewijzigd ten opzichte van 30 oktober | Delta van metadata; geen nieuwe runtimevrijgave |
| admin-inventory.json | Verse rollen, 121 Pages, 226 collecties, negen menu’s en exacte producttellingen | Geen orders/klanten, productwaarden of privégegevens |
| source-verification.json | 409 geselecteerde tekstbronnen, 407 bytegelijk, twee afwijkingen | Alleen hashes/metadata; geen raw settings_data of private configuratie |
| http-refresh.json | 18 openbare GETs, titels/head/formulierschema/thema/retourlink/railcontrols/footer | Geen JavaScriptuitvoering, formulierinzending, mail of cartwrite |
| closing-state.json | Herhaalde thema-/Page-rollen bij afronding, gelijk aan beginread | Geen tweede volledig manifest |
| document-validation.json | Offline checks van het nieuwe HTML-naslagwerk | Geen visuele browser-, iPhone-, Windows- of checkoutclaim |

MAIN 195948839178 blijft live. NAV-02-concept 195947036938 blijft UNPUBLISHED. Retour-Page 166668894474 is gepubliceerd; mailboxbezorging blijft open. Offerteconcept 195916628234 en klantactivatie behouden hun begrenzing.

De verse tellingen zijn 11.680 producten totaal, 11.679 ACTIVE, één DRAFT en 11.679 gepubliceerd, alle EXACT. De 11.679 ingebouwde productidentiteiten zijn **de export van 30 oktober**; gelijke tellingen zijn geen opnieuw bewezen setgelijkheid. Blog-/metafielddefinities en de brede SEO-/sitemapinventaris zijn niet opnieuw integraal geëxporteerd.

## Bronuitzonderingen

- `config/settings_data.json`: metadata en ontvangen bytes verschillen. De bestaande uitzondering blijft open; geen normalisatie gebruiken om pariteit te claimen.
- `templates/page.retour-aanmelden.json`: ontvangen tekst bevat een Shopify-commentaar en heeft daardoor een andere bytehash. De bestaande retourvrijgave bevat een afzonderlijke semantische vergelijking. Niet vermengen met een bewezen runtimefout of een nieuw volledige-bytepariteitsbewijs.

## Actualiseren

Bewaar de oude [nulmeting](../2026-10-30/baseline-and-checks.json) en de 36 opgenomen brondossiers met hun datum. Werk eerst hoofdstukken 1 en 49 en de centrale status bij. Bij een echte release horen nieuwe rollen, relevante hashvergelijking en passende live taakproeven. Deze documentatieronde publiceert NAV-02 niet en voert geen mailboxproef uit.
