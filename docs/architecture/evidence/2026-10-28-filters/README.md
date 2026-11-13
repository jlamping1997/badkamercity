# Bewijs DOC-03C: externe filters, native terugval en kaartverrijking

Bronmoment **28 oktober 2026**. De eigenaar vraagt verder onderzoek/documentatie. Checkout blijft buiten scope. Geen theme-, product-, cart-, index- of servermutatie en geen publicatie uitgevoerd. De werkelijke openbare API is alleen twee keer voor zoek-/facetmetadata gelezen.

## Bron en methode

[source-provenance.json](source-provenance.json): negen gericht opnieuw gelezen MAIN-bestanden, alle MD5/grootte passend en voorzien van SHA-256. MAIN bij aanvang 195818389770, Smooth winkelwagen pop-up. Geen volledige nieuwe themesnapshot of backendscan. Git-baselines: actieve branch 5f0dd414f9243e46757930b7924329f4abc4fe1f; main dd780e9a19d18d36da33780885489cf47dc86893.

De harness voert de complete externe filterclosure en de mobiele listinghelper uit. FX-37 voert ook actuele native facets-code uit: de popstate-handler en gridvervangingsmethode blijven echt; de native requestorkestratie wordt vervangen door een gecontroleerde directe aanroep van die gridmethode. Een audit-only export maakt de class toegankelijk in de sandbox. Geen productiebron gewijzigd.

**Omgeving:** Node 24.22.1, bestaande gepinde happy-dom 21.0.4. Geen nieuwe dependency geïnstalleerd. Zoek-/sectionantwoorden, navigatie, timers, mediaqueries, observers, geometrie en scroll zijn stubs. History-URL/state wordt in de DOMomgeving gezet; dit is geen echte browser back/forward-meting.

### Expliciete beperking van numerieke validatie

De eerste run liet zien dat happy-dom exacte step-0.1-veelvouden via floating-point-remainder onterecht afwees. De fixture gebruikt daarom een afzonderlijk numeriek validitymodel met min/max/step en tolerantie; non-numeric validatie blijft bij de DOMlibrary. Dit bewijst de sourceguard en staatsovergang onder de gegeven validitystimulus, niet native browservalidatie. Productiecode en hashes zijn hiervoor niet aangepast. De definitieve historyfixture geeft ook event.state expliciet mee, zoals een echte navigatie dat doet.

## Resultaten

[results.json](results.json): **41 cases — 35 CONTROL_PASSED, twee DEFECT_REPRODUCED, vier BOUNDARY_CONFIRMED**. Een succesvolle harnessrun bevat bewust reproducties van bestaande codeafwijkingen; geen algemene “winkel geslaagd”-status.

| Cases | Onderzocht |
| --- | --- |
| FX-01…04 | Automatische activatie, URL-staat, productzoekcontext en overslaan andere zoektypes |
| FX-05…11/33 | Prijs/range/debounce/draft, integerguard, boolean/group/exact values, wissen, sort en pagina |
| FX-12…21/36 | Nulresultaat, netwerk/HTTP/schema/count/global-context, stale success/error, timeout en popstate-eigenaarschap |
| FX-22 | Afwijkend visible_values wordt na Meer/Minder niet hersteld |
| FX-23…25/32 | Grenzen: collectiehandle bij gelijk count, twee URL-dialecten, omgekeerde range, niet uitgevoerde beleidsflags |
| FX-26…29/34…35 | Product-ID, section-cache, retry/timeout, nieuwe grid- en kleurintentie |
| FX-30…31 | Synthetische drawer/Escape/inert/querywissel |
| FX-37 | Native gridvervanging na fallback + latere externe response met oude DOM-referenties |
| FL-01…04 | Zwevende shortcut, bodyplaatsing, overlay-/mediaqueryvoorwaarden en openerkeuze |

## Twee verschillende defecten, afgebakend

**FILTER-F01 / FX-37, P1-kandidaat, VERIFIED_ISOLATED:** na fallback krijgen beide historycontrollers het event. De echte native methode vervangt de containerkinderen; de latere externe response werkt op bewaarde, inmiddels losse nodes en kan active=true zetten met native live grid en ontbrekende toolbar. Dit is onder gecontroleerde timing gereproduceerd, niet als werkelijk huidig bezoekersincident of frequentie vastgesteld.

**FILTER-F02 / FX-22, P2-kandidaat, VERIFIED_ISOLATED:** bij synthetisch visible_values=2 levert de eerste render twee, na uit-/inklappen zes opties. De reset gebruikt een hardcoded zes. [Twee verse facetprofielen](facet-settings.json) leveren momenteel overal zes; een actuele fout op die twee routes is dus niet aangetoond. Andere profielen zijn niet gelezen.

De vier boundaries zijn: een collection-handle wordt bij gelijk profielcount niet extra gecontroleerd; native URL-parameters worden niet vertaald; een omgekeerde geldige range wordt doorgestuurd; metadataflags searchable/section hebben frontenduitzonderingen. Backend- of browsergevolgen daarvan zijn niet als nieuwe live defects bewezen.

## Openbare facetmetadata

[facet-settings.json](facet-settings.json): twee read-only zoek-POST's, beide HTTP 200. Wastafelkranen heeft tien facetten, Inloopdouches zeven. Alleen veld/type/UI-metadata opgeslagen; geen productrecords, prijzen per product, serverkeys of gebruikersfilters. Deze meting is geen compleet serverprofielregister, preflighttest of index-/voorraad-/prijsvergelijking.

## Overdracht

[Filterstate/fallback](../../components/micro/FILTER_STATE_AND_FALLBACK.md), [typed controls](../../components/micro/FILTER_VALUES_AND_CONTROLS.md), [kaartverrijking](../../components/micro/CARD_HYDRATION_AND_COLORS.md) en [drawer/shortcut](../../components/micro/MOBILE_LISTING_AND_DRAWER.md) bevatten de eigenaars, herstelrichtingen en open acceptatie.

Tool: [scripts/component-audit](https://github.com/jlamping1997/badkamercity/tree/fix/product-cards-2026-10-14/scripts/component-audit), `filters.mjs`. Alleen uitvoeren met de benoemde aparte bronmap en dit manifest. Native volledige request-/rendercyclus, echte CSS/constraints, viewport/touch, browserhistory, screenreader, serverfrequentie en checkout zijn niet gecertificeerd. Ruwe bron- en winkel-HTML blijven buiten de publieke repository.
