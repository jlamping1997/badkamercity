# Producttekst en specificaties: meten, bewegen en focus behouden

**28 oktober 2026 · DOC-03B.** Bron `assets/bc-product-disclosure.js`, opnieuw bytegeverifieerd. Hoofddossiers: [productpagina's](../PRODUCT_PAGES.md) en [stijl/beweging](../MOTION_AND_STYLES.md). DS-01 t/m DS-05 zijn replays met expliciet nagebootste geometrie, mediaqueries, ResizeObserver, requestAnimationFrame en Web Animations.

## Initialisatie en meten

`connectedCallback` vereist viewport, content en toggle. Een bestaande AbortController voorkomt een tweede initialisatie. De controller registreert klik, telefoonmediaquery, persisted pageshow en image-load; een ResizeObserver en `document.fonts.ready` kunnen een meting plannen. `scheduleMeasure` annuleert de vorige frame-aanvraag voordat hij een nieuwe maakt.

| Modus | Ingeklapte hoogte | Actief |
| --- | --- | --- |
| Beschrijving | Vier berekende regels; fallback line-height 28px | Ook op desktop |
| Specificaties | Onderkant van rij 10 bij meer dan tien rijen; anders volledige hoogte | Alleen bij maximaal 749px |

`hasMore` vereist meer dan vier pixels verschil tussen volledige en ingeklapte hoogte. Meting annuleert een lopende animatie, zet de gewenste eindhoogte, knopzichtbaarheid en focusstaat. Font-/beeld-/viewportwijzigingen zijn dus onderdeel van het componentcontract, niet alleen styling. De gemeten fixture met 20px regelhoogte geeft een clamp van 80px; dat is geen vast sitebreed CSS-getal.

## Wisselen en snelle herhaling

`toggle` bewaart de actuele beginhoogte, annuleert een vorige animatie, wisselt `expanded`, synchroniseert aria/class/focus en zet de doelhoogte. Animatie gebruikt **320ms** met `cubic-bezier(0.22, 1, 0.36, 1)`. Na afloop mag alleen de nog actuele animatie de eindhoogte zetten: open wordt `auto`, dicht de berekende clamp.

DS-02 laat bewust een oude finished-promise laat aflopen na een tegengestelde klik. Die mag de nieuwe gesloten toestand niet opnieuw openzetten. Dit beschermt tegen terugveren bij snel klikken. De replay bevestigt de afhandeling; waargenomen smoothness, framerate en continue hoogteverandering op een apparaat zijn hiermee niet gemeten.

Bij reduced motion of ontbrekende `.animate` gaat de controller direct naar de eindstaat. Wanneer dichtklappen scrollherstel nodig maakt (componenttop kleiner dan 96px), gebruikt hij `instant` bij reduced motion en anders `smooth`. Een ingeklapte component op een andere scrollpositie hoeft niet te scrollen. De 96px is een componentregel, geen bewezen actuele headerhoogte voor elke route.

## Verborgen links uit de tabvolgorde

Vóór iedere focusberekening herstelt `restoreFocus` de eerder bewaarde tabindexwaarden. Wanneer de inhoud gesloten is, krijgen focusbare nodes die onder de gemeten clamp eindigen `tabindex=-1`. De oorspronkelijke waarde — ook een bestaand expliciet tabindex — wordt bewaard en bij uitklappen/herberekenen/cleanup hersteld.

DS-01 bevestigt het traject originele `tabindex=2` → `-1` bij verbergen → `2` bij openen → `-1` bij sluiten. Dit is een synthetische input om herstel aan te tonen, geen aanbeveling om positieve tabindexen in de winkel toe te voegen. De code kijkt naar de onderkant van een element; gedeeltelijk geclipte links worden ook buiten de tabvolgorde gehouden.

## Breakpoint en cleanup

Bij telefoonquerychange en persisted pageshow wordt `expanded=false` en opnieuw gemeten. Specificaties staan buiten telefoonmodus volledig open; DS-04 bevestigt dat de testdesktop geen toggle nodig heeft en dat terugschakelen de originele focuswaarden herstelt. De mobiele flag/geometrie zijn stubs, geen echte mobiele browsermeting.

`disconnectedCallback` abort listeners, stopt ResizeObserver, annuleert frame/animatie en herstelt tabindex. DS-05 bevestigt die cleanup in de DOM-simulatie. Een latere font-promise controleert `isConnected` voordat hij opnieuw plant.

## Veilige wijzigingsgrens

Behoud meten, eindstaat, reversalguard, focusherstel en cleanup als één contract. Alleen een CSS-transitionduur veranderen kan de JS-eigenaar niet vervangen. Bij een nieuwe vormgeving: lange/korte tekst, 10/11 specificatierijen, laden van font/beeld, snelle open/dicht, ontbrekende animate, reduced motion, gefocuste verborgen link en section reload controleren.

Open: werkelijke CSS/layout, touch, screenreader, focus na sluiten met actieve link, browserbfcache en visuele soepelheid op apparaten. De vijf nieuwe controles zijn geen algemene motion-/toegankelijkheidsvrijgave. [Bronnen en methode](../../evidence/2026-10-28-transitions/README.md).
