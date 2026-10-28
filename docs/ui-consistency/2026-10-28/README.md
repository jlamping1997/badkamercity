# BadkamerCity — productfoto’s en consistente bediening

**28 oktober 2026 · UI-01.** De eigenaar kiest nu expliciet onderzoek naar inconsistenties en wil dezelfde productfotopijlen als bij Sunshower. De optionele vraag is beantwoord met **‘Bij de productfoto’s’**. De eerder geplande DOC-03E-headerverdieping is geparkeerd; checkout blijft buiten scope.

**PREVIEW_READY · DESKTOP_GETEST · MOBIEL_OPEN · NIET_GEPUBLICEERD.** Concept **195850764554 — BadkamerCity - gelijke fotopijlen** is gebouwd. Vooraf alle1.262 bestanden gelijk; finaal drie bedoelde verschillen/1.259 gelijk. MAIN blijft1.262/1.262 ongewijzigd. [Voorcontrole](initial-parity.json), [eindcontrole en exact QA-herstel](final-parity.json), [browserbewijs](browser-observations.json), [beoordelingsbeeld](preview.jpg).

## Onderzoek dat werkelijk is uitgevoerd

De broncontrole gebruikt MAIN **195818389770 — Smooth winkelwagen pop-up**. Git-start: actieve doelbranch `fix/product-cards-2026-10-14` op `521c487b9c58b49f5de36fb16de210170f24d4d8`, main op `178d55292a25f93a2c2639e97cfe18680dba72e0`. De Linux-werkmappen waren schoon; Windows is niet gecontroleerd. De bronmap/Git-root is niet automatisch gelijk aan het huidige thema.

[source-provenance.json](source-provenance.json) verifieert 29 bestaande capturebestanden opnieuw tegen actuele Shopify-MD5/grootte. Het verse volledige bronmanifest bevat 1.262 paden. Er is geen nieuwe volledige body-export of productdatabase-export gedaan. Settingspariteit uit DOC-01 blijft apart open; voor conceptvergelijking worden de door Shopify gerapporteerde originele bestandschecksums gebruikt, zonder settingsbytes te normaliseren.

Browser: desktop **1363 × 936**. Bekeken: homepage → Sunshowerlanding → Round ONE Medium White; Wiesbaden 24.3710; Hotbath SDS1GN14; Wastafelkranen. De collectie wisselde van de eerste native markup naar 24 externe kaarten; conclusies moeten daarom de renderer en laadstaat noemen. Geen real-cart-, wishlist-, checkout-, formulier- of accountactie uitgevoerd.

## Bevestigde verschillen en advies

| ID | Dezelfde functie | Werkelijke afwijking | Status / kleine vervolgstap |
| --- | --- | --- | --- |
| UI-F01 | Vorige/volgende productfoto | Sunshower: cirkelpijlen op de hoofdfoto. Native PDP: pijlen bij de thumbnailrail, bij hoge foto’s pas lager in beeld | Eigenaar vraagt gelijkmaken; gedeelde native kandidaat hieronder |
| UI-C01 | Omschrijving uitklappen | Sunshower ‘Toon meer’; algemene PDP ‘Lees meer/Lees minder’ | Woordkeuze gelijkmaken; bestaande animatie-/focuscontrollers behouden |
| UI-C02 | Primaire winkelwagenknop | Hotbath 56px hoog/radius40px; Sunshower49px/radius8px in de waargenomen desktopstaat | Ontwerpvariatie; één knopvorm/minimum kiezen, verschillende pending-/koopregels behouden |
| UI-C03 | Ja/Nee-specificatie | Algemene tabel tekst; Sunshower vink/kruis met toegankelijke Ja/Nee-naam | Presentatiekeuze harmoniseren; geen fout in de productspecificatie vastgesteld |
| UI-P01 | Uitvergrote foto bekijken | Hotbath heeft al vorige/volgende, teller en Escape | Werkende controle: 1/3 → 2/3 en sluiten bevestigd; geen nieuwe viewer nodig |
| UI-S01 | Native kaart zonder afbeelding | Eerste native AX toont dezelfde producttitel in twee headinglocaties | Kandidaat; settled pagina is extern. Geen bewezen actuele externe-kaartbug |

[findings.json](findings.json) bewaart status, voorgestelde standaard en wat wel/niet is geïmplementeerd. Alleen UI-F01 hoort bij de huidige concrete wijziging. De drie overige bevestigde verschillen zijn geen drie automatisch bewezen verkoopbugs. De reeds afzonderlijk aangetoonde filter-/cart-/wishlistproblemen blijven in het [bevindingenregister](../../architecture/FINDINGS.md) staan.

## De kleinste gedeelde fotowijziging

Drie bestanden op de actieve branch, onder [implementation op de werkbranch](https://github.com/jlamping1997/badkamercity/tree/fix/product-cards-2026-10-14/docs/ui-consistency/2026-10-28/implementation):

| Bestand | Wijziging |
| --- | --- |
| snippets/product-media-gallery.liquid | Twee gewone buttons, vertaalde bestaande sliderlabels, aria-controls en beleefde teller; verborgen tot JS klaar is |
| assets/media-gallery.js | Bestaande controller kiest media; één tellermodel voor overlay/miniaturen/swipe/variantupdate, begrensde randen en annulering van de vorige fade |
| assets/section-main-product.css | 44px cirkelknoppen, 12px van de zijkanten, teller en focusring; verbergt de dubbele oude rail-/mobiele knoppen wanneer de nieuwe bediening klaar is |

Het native basisproducttemplate en de twee Hotbath-templates gebruiken dezelfde thumbnail_slider-galerij. Sunshower heeft de gewenste bediening al en krijgt geen tweede controller of extra knoppen. Producten met nul/één weergegeven medium houden de nieuwe bediening verborgen. Een desktopfoto krijgt maximaal180ms opacity-overgang; reduced motion schakelt die uit. De bestaande fotozoom, mediapauze, geselecteerde thumbnail en productvariant blijven via de oorspronkelijke methoden lopen. Geen extra runtimebibliotheek, productgegevens of kooprequest toegevoegd.

De CSS-/controllerwijziging is geen algemene vrijgave van alle toekomstige Theme Editor-layouts, 3D/video-interacties of fysieke touchapparaten. De huidige toegewezen templates zijn het doel; afwijkende toekomstige galerijlayouts opnieuw beoordelen.

## Tests en hun grenzen

[gallery-tests.json](gallery-tests.json): **15 lokale controles**, met de volledige bestaande global.js/SliderComponent en volledige kandidaat-MediaGallery. De ongewijzigde global.js is eerst op SHA-256 gecontroleerd. De controls komen uit de werkelijke kandidaat-Liquidmarkup; geometrie, mediaqueries, scroll, timers en animaties zijn gecontroleerde modellen. Geen netwerk toegestaan.

Bevestigd: nul/één medium, eerste/middelste/laatste foto, geen wrap bij de nieuwe pijlen, thumbnailselectie, variant-prepend, verborgen media, mobile-model zonder thumbnails, echt SliderComponent-scroll-event in dat model, snelle klikken, annulering, reduced motion en disconnect. Dit zijn geen vijftien echte browser-/touchtests. De desktopviewercontrole hierboven is apart daadwerkelijk in de browser uitgevoerd.

Reproduceren vanaf de actieve branch met de bestaande gepinde happy-dom21.0.4:

```bash
node scripts/component-audit/gallery.mjs \
  --source /pad/naar/gecontroleerde-themefiles \
  --candidate docs/ui-consistency/2026-10-28/implementation \
  --manifest docs/ui-consistency/2026-10-28/source-provenance.json \
  --output /tmp/badkamercity-gallery.json
```

Optioneel `--dom-module` wijst de expliciete ESM-module van de bestaande installatie aan. Het thema gebruikt die testdependency niet. De Shopify-skillvalidator is in stateless modus uitgevoerd op snippet, JS en CSS; de drie rapporten staan naast dit dossier. De graphQL-compatibiliteitsvalidator slaat over; de uitvoerende connector valideert het schema vóór uitvoering. Een statische validator is geen bewijs voor effectieve CSS of native bediening.

## Veilige uitvoering en herstel

Voor schrijven: volledige conceptkopie uitlezen, processing=false en alle1.262 naam/MD5/groottevelden vergelijken. Daarna alleen de drie beoordeelde bestanden schrijven en teruglezen. De bestaande product.bc-responsive-qa-template mag tijdelijk uitsluitend in het concept een iframecontrole bevatten; daarna exacte oorspronkelijke bytes herstellen en opnieuw vergelijken. Geen Admin-Page toewijzen of bestaand live template wijzigen.

Na schrijven: concept hoort alleen de drie benoemde verschillen met de startbron te hebben; MAIN-manifest/rol moeten onveranderd blijven. Bewaar originele Shopifybron/checksums voor herstel. Merchant beoordeelt en publiceert via Shopify; deze opdracht publiceert niet. Voor een terugzetactie vóór publicatie volstaat het concept niet te publiceren; bij een latere uitrol gelden de normale release-/rollbackafspraken.

Bronuitleg: [Shopify productmedia](https://shopify.dev/docs/storefronts/themes/product-merchandising/media/support-media), [themeFilesUpsert](https://shopify.dev/docs/api/admin-graphql/2026-10/mutations/themeFilesUpsert). De winkelbron en het gedateerde bewijs blijven leidend voor wat hier werkelijk bestaat.

## Werkelijke conceptcontrole en oplevering

- Wiesbaden24.3710: twee zichtbare44×44px overlayknoppen, teller1/2, oorspronkelijke railknoppen verborgen. Klik volgende geeft2/2 en disabled-next; Space op vorige geeft1/2 en disabled-previous. Echte desktopbrowser, geen nagebootste keyactivation.
- HotbathSDS1GN14: dezelfde gedeelde bediening; twee volgende-klikken geven3/3 en disabled-next. De product-/cartactie is niet uitgevoerd.
- De oorspronkelijke Sunshowerpijl gaf voor de wijziging1/5 →2/5 met de tweede thumbnail geselecteerd. De Sunshowerbestanden zijn niet gewijzigd.
- Het tijdelijke QA-template leverde frames van320/390/1024px, maar de site toonde in alle frames ‘refused to connect’. Geen geslaagde iframe-/mobielcontrole; geen framingbeveiliging aangepast of omzeild. Het bestaande QA-template is meteen teruggezet naar zijn originele448 bytes/MD5 en inhoudelijk teruggelezen.
- De drie eindbestanden zijn exact op body én metadata teruggelezen. Een nieuw volledig main-/conceptmanifest bewijst alleen die drie verschillen en nul MAIN-wijzigingen. Geen Shopify-copyjob of eigen schrijver blijft lopen.

Het concept kan door de eigenaar worden beoordeeld in Shopify → Webshop → Thema’s → **BadkamerCity - gelijke fotopijlen**. Controleer ook de echte mobiele weergave vóór publicatie. De actieve browser is op het concept behouden; een gewone storefront-URL zonder previewcontext toont niet vanzelf dit concept. De kopieerlinkknop meldde succes, maar de browserconnector leverde geen bruikbare clipboard-URL terug; er is geen deelbare link verzonnen.

De overige drie vorm-/tekstverschillen blijven voorgesteld, niet stil meegecorrigeerd. De volgende uitvoering begint bij de actuele status en behoudt alle eerder geregistreerde functionele bevindingen.
