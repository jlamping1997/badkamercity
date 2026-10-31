# DOC-03D — verlanglijst en browseropslag

**28 oktober 2026.** Drie methodedossiers: [opslag/events](../../components/micro/WISHLIST_STORAGE.md), [identity/adapters](../../components/micro/WISHLIST_IDENTITY.md), [renderen/cache/toevoegen](../../components/micro/WISHLIST_RENDER_AND_ADD.md). Dit bewijs certificeert benoemde lokale codepaden, geen volledige browser-, verkoop- of operationele werking.

## Bron en herkomst

- Git-start actief: `8227eaed86c2386391b8b27a210d1490942ce2b3`; main: `cb685367c3ab75738a3ba2644eb5dd28d8e09ab7`. Beide lokale werkmappen waren schoon; Windows is niet gecontroleerd. Actieve doelbranch blijft fix/product-cards-2026-10-14; main ontvangt uitsluitend documentatie.
- Shopify MAIN bij aanvang/einde: **195818389770 — BadkamerCity - Smooth winkelwagen pop-up**, updatedAt=2026-10-28T01:37:04Z. [Eindcontrole](theme-end-check.json) bevat ook de opnieuw gelezen metadata voor de vijftien bronnen.
- [source-provenance.json](source-provenance.json): vijftien **verse metadatareads**, met MD5/grootte gelijk aan reeds aanwezige ruwe bronbytes uit de eerdere gecontroleerde capture. Die bytes zijn opnieuw gelezen/gekopieerd naar een aparte private scratchbronmap en SHA-256-gehasht. Geen nieuwe volledige thema-export of verse bodydownload geclaimd. De ontbrekende eerst geprobeerd benoemde bc-sunshower-experience-sectie is niet als bron geteld; de echte adapter is assets/bc-sunshower-shop.js.
- Elf van de vijftien bestanden staan ook in de eerdere geselecteerde DOC-02A-bronindex en hebben dezelfde SHA-256; CSS, wishlistsectie, buttonsnippet en paginatemplate stonden niet in die selectie van 85 bestanden. Alle vijftien passen bij de huidige metadata aan begin/einde; geen drift vastgesteld tussen die reads. config/settings_data.json is niet betrokken en blijft een afzonderlijke open pariteitsgrens.
- Read-only Admin GraphQL-schema ontdekt vóór queries. De compatibiliteitsvalidator meldde overgeslagen validatie; graphql_query valideert vóór uitvoering. Geen afzonderlijke validator-PASS claim. De parallel beschikbare mcp__shopify-dataverbinding meldde authenticatie vereist; de bestaande gekoppelde Shopify-app werkte wel. Er zijn geen rechten omzeild of nieuwe accounts gebruikt.

## Reproduceerbare replay

Tool op de [actieve branch](https://github.com/jlamping1997/badkamercity/blob/fix/product-cards-2026-10-14/scripts/component-audit/wishlist.mjs):

```bash
npm ci --prefix scripts/component-audit --ignore-scripts
node scripts/component-audit/wishlist.mjs \
  --source /pad/naar/gecontroleerde-themefiles \
  --manifest docs/architecture/evidence/2026-10-28-wishlist/source-provenance.json \
  --output /tmp/badkamercity-wishlist.json
```

Werkelijke omgeving: **Node 24.22.1 / happy-dom 21.0.4**, bestaande gepinde installatie via --dom-module gebruikt; geen nieuwe dependency/installatie. De volledige ongewijzigde wishlistclosure wordt uitgevoerd. WL-43 voert ook de volledige Sunshower-shopclosure uit; beide JS-bestanden worden **vóór uitvoering** tegen SHA-256 geweigerd bij afwijking. De overige dertien bestanden dienen als inhoudelijke Liquid/CSS/callercontext, geen Liquid-runtime of CSS-engine.

Alle getItem/setItem en storage-events zijn synthetisch. WL-23 gebruikt twee onafhankelijke closures en een gedeelde Map met bewust vertraagde eventbezorging; dit is geen native browser-multitabproef. Een JSON-roundtrip vertaalt alleen resultaten uit het DOMrealm voor hostassertions; de list-copycontrole muteert de echte API-returnwaarde. De programmacode wordt niet herschreven of met privéhelpers ontsloten.

Transport staat alleen synthetische product-GET en cart-POST toe; andere fetches worden geweigerd. Navigatie, timers en Sunshower-imagepreload zijn expliciete stubs. MutationObserver is uitgeschakeld behalve WL-40 en WL-43, die de DOMlibrary-observer gebruiken. Native browserfocus, layout/CSS, touch, screenreader, echte afbeeldingrequests en eventlooptiming zijn niet bewezen. Geen nieuwe browserinteractie of echte cart-/index-/checkoutactie.

## Uitkomst en interpretatie

[results.json](results.json): **43 cases, 34 CONTROL_PASSED, twee DEFECT_REPRODUCED en zeven BOUNDARY_CONFIRMED**. Een succesvolle toolrun kan dus bewust een fout aantonen; ‘alle tests geslaagd’ betekent hier niet ‘webshop foutloos’.

| Cases | Onderzoek / uitkomst |
| --- | --- |
| WL-01…11 | Leeg, normalisatie, malformed/ander schema, read/write-denied, limiet, duplicaten, timestamps, kopieën en normale event/toggle |
| WL-12…20 | Form-/Sunshoweridentity, ontbrekende variant, beschikbaarheidsfallback, ambiguïteit, eigen busyguard en cache-retry |
| WL-21/22 | Storage-key/clear-event en opeenvolgende tabedits met tijdige eventbezorging |
| **WL-23** | **WISH-F01:** tweede tab schrijft verouderde array en verliest eerste toevoeging |
| WL-24…32 | Productprijs, exacte/missende variant, source/complexiteit/selling-plan/quantity/unavailable en HTTP-fout |
| WL-33/34 | Verwijderde kaart blijft weg bij laat antwoord; vier workers per render |
| WL-35/36 | Alleen synthetische add, exacte payload, dubbelklikguard, behouden favoriet, cartnavigatie en foutunlock |
| WL-37/38 | Succes-cache zonder TTL; geen requesttimeout; geen realtime-/netwerkgezondheidsclaim |
| WL-39…42 | textContent en javascript-imageguard, dynamische kaartdecoratie, bootguard, framecoalescing en expliciet variant-change-event |
| **WL-43** | **WISH-F02:** echte Sunshower-keuzecommit met nieuwe handle/variant, hartjesstatus nog die van oude uitvoering; volgende hartklik bewaart wel correct |

De zeven grenzen zijn WL-03/04/05/07/16/37/38: herstel/duplicaten, unavailable opslaan en cache/timeout. Deze zijn geen zeven extra aangetoonde actuele bezoekersbugs. Geen opgeslagen echte product- of klantrecords onderzocht.

## Controle en resterend werk

Uitgevoerd: JS-syntaxcheck; 43-case replay; afzonderlijke negatieve SHA-manifestcontrole die vóór uitvoering/output stopt; pariteit van alle vijftien bronnen aan het einde; JSON/doclinks/diff/privacycontrole. [Documentcontrole](documentation-validation.json) vermeldt de werkelijk getelde resultaten.

Geen themecodecorrectie, deployment, productdatawrite, cart-restore, formulier-/mailverzending of checkoutread. WISH-F01/F02 blijven open tot gerichte conceptfix en passende echte browserregressie. De overige eerdere bevindingen blijven behouden. Volgende onderzoekstaak staat uitsluitend actueel in [de centrale status](../../../LIVE_STATUS_AND_NEXT_STEPS.md).

Externe uitleg gecontroleerd: [Shopify themefile-body](https://shopify.dev/docs/api/admin-graphql/2026-10/objects/OnlineStoreThemeFileBodyText), [MDN storage-event](https://developer.mozilla.org/en-US/docs/Web/API/Window/storage_event), [HTML Web Storage](https://html.spec.whatwg.org/multipage/webstorage.html). Geen externe bron vervangt de echte winkelcode of de benoemde replay.
