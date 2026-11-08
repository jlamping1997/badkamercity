# Eenheidskaart: dezelfde functie, herkenbare bediening

## Actuele afwijking — 8 november 2026

**FOOTER-F02 · VERIFIED_THEME / VERIFIED_HTML · OPEN.** Op MAIN **196328685834** kiest `compact_homepage=true` op home `bc-home-footer` en elders de standaard `bcf-v3`. De verschillen in kolommen, bestemmingen, trust-/contactopbouw en bronstijl zijn daadwerkelijk uit code en 14 publieke responses gelezen; de brede 364-set bevestigt de classverdeling. Dit is meer dan een vermoedelijke CSS-afwijking. [Exacte bron, linkmatrix en voorstel](components/FOOTER.md) · [centrale audit](../audits/2026-11-08/README.md).

| Te harmoniseren | Huidige concrete varianten | Voorgesteld contract | Status |
| --- | --- | --- | --- |
| Storefrontfooter | Home `.bch-footer`; overige `.bcf-v2.bcf-v3` | Bestaande standaardrenderer op alle gewone storefront-routes | PROPOSED; geen code-/instellingswijziging |
| Linkdekking | Home tien hoofdcategorieën + advies/inspiratie; elders zes categorieblocks en merkengids | 17 blocks: 4 service, 10 categorie, 3 info; acht lege slots herbestemmen/verwijderen, het maximum van 18 respecteren | PROPOSED; verzendlink pas na bestaande juiste openbare bestemming |
| Contact / policies | Geen telefoon/adres in beide footers; vijf policies, twee met zichtbare HTML | Correcte eigenaargegevens en leesbare bestaande policies; beleidslinks uit `shop.policies` | OPEN; geen juridische/bedrijfsgegevens afleiden |
| Detailsbediening | Home native gesloten markup; standaard desktop-open/mobielcontroller | Eén gedocumenteerde lifecycle met keyboard/touch/focus en 749↔750px-regressie | Nieuwe runtimecontrole open |

Checkout en extern gehoste accounts blijven afzonderlijke Shopify-shells. De footerharmonisatie is geen globale CSS-refactor of redesign van die systemen. De oudere vergelijkingen hieronder behouden **28 oktober** als bronmoment.

Bronmoment **28 oktober 2026**. Dit is de koppeling tussen [componentafspraken](COMPONENT_CONTRACTS.md), bestaande implementaties en nog uit te voeren vergelijkingen. Bronverschillen zijn vastgesteld; een visuele afwijking is pas bevestigd bij dezelfde functie/staat/viewport. Het register autoriseert geen blinde globale CSS-refactor.

| Functie | Huidige varianten | Te behouden / gelijk te trekken | Status |
| --- | --- | --- | --- |
| Product openen | Native card-product, zoekkaart, externe JS-kaart, eigen home-/Sunshowerkaart | Zelfde actie duidelijk; hele-kaartlink zonder geneste links; pijl alleen betekenisvol | Bronkaart bekend; mobiele vergelijking OPEN |
| Productkleur kiezen | V2/Hotbath, Wiesbaden-adapter, externe kaart, Sunshower | Label, geselecteerd, beschikbaar, focus, naam en identiteit samen; datamapping apart | Gedeelde keuzelogica deels getest; visueel OPEN |
| Favoriet bewaren | Eén wishlistcontroller met PDP/native/externe/home/Sunshower-adapters | Identity en aria-pressed/is-saved na dezelfde keuzecommit bijwerken | WISH-F02: Sunshower-kaarthart blijft lokaal achter; [identitydossier](components/micro/WISHLIST_IDENTITY.md) |
| Dropdown | Native variantpicker, V2-select, Sunshower-select, sortering | Controlhoogte, chevron, fout/disabled/loading en focus bij dezelfde functie | Geen gekozen globale referentiestijl vrijgegeven |
| Paneel uitklappen | Footer details, filters, productdisclosure, mobile contents | Label, expanded, keyboard, verborgen tabstops | Mechanismen verschillen bewust; vergelijk resultaat |
| Fotobladeren | Algemene media, Sunshower native scroll, PhotoSwipe | Vorige/volgende, begrensde rand, geselecteerd beeld, zoom/sluiten | Pijlen hebben andere taak dan product-CTA |
| Toevoegen bevestigen | Popup/drawer, inline Sunshower, cartnavigatie bij set/inbouw/wishlist | Exact artikel/aantal, fout/uncertain, heldere vervolgactie | UI-F03 open; geen tweede kooprequest toevoegen |
| Overlay sluiten | Cartdialog, maathulp, menu/filterdrawer, viewer | Vindbaar kruis, Escape waar passend, buitenklik, focus/scrollherstel | Controller-eigenaar behouden; mobiele checks OPEN |
| Prijs/levering | Kaart, Shopify-verrijking, PDP, settotalen, cart | Zelfde actuele identiteit/valuta/btw; geen valse vaste levertijd | Bronverschillen gedocumenteerd; data-/bedrijfscontrole apart |
| Knoppen/links | Globale Dawn, bc-*, ss-*, bcf-* | Betekenis van primair/secundair, hover/focus/disabled/loading | Tokens/cascade niet sitebreed geharmoniseerd |

## Tokens en beweging

Er bestaat geen aangetoonde ene universele design-tokenbron voor alle maatwerkonderdelen. Dawn-settings genereren globale variabelen; footer heeft `--bcf-*`; Sunshower en overige BC-componenten hebben eigen families. Gelijkende kleuren vervangen voordat scope en contrast bekend zijn kan regressies geven. De technische bronindex is een zoekkaart, geen computed-stylemeting.

De eigenaar vindt soepele bediening belangrijk. Documenteer daarvoor meer dan duration: begin-/eindstaat, annuleren, snelle herhaling, al geladen versus trage content, focus en scroll, reduced motion en cleanup. Een 300ms transition is geen bewijs dat een UI smooth is. De bestaande cart-close/heropen-replays en beperkte Sunshower-maathulp/galerijwaarneming zijn specifieke bewijzen, geen sitebrede animatievrijgave.

## Werkwijze voor één verbetering

Kies één functie en bestaande referentievariant → toon de gebruiksplaatsen uit de dossiers → vergelijk dezelfde viewport/staat → classificeer BUG/INCONSISTENCY/INTENTIONAL_VARIANT/UNKNOWN → kleinste gedeelde stijl/adapter aanpassen in concept → relevante uitzonderingen controleren → bevinding en docs bijwerken. Alleen wanneer dezelfde functionele code werkelijk herhaald is en dezelfde foutgrenzen heeft, is samenvoegen aangewezen.

Footerlabels zonder URL en de lege populaire collectie zijn configuratievragen. Ze vragen geen nieuwe dropdownlibrary of sitebrede componentherbouw. De twee geïsoleerde koopfeedbackproblemen hebben klantimpact en krijgen voorrang zodra gerichte correcties aan de beurt zijn.

## Reële verschillen in actieregels, nu verder gevolgd

De [inbouwketen](components/micro/INBOUW_RECOVERY.md) bewaakt product-form via een consume/delegate-returnwaarde, busy/uncertain en aria-disabled. De eerder onderzochte Sunshower-sethandler heeft een andere lockgrens. Gedeelde knopstyling mag deze afzonderlijke requesteigenaars niet dubbel activeren. [Disclosure](components/micro/DISCLOSURE_MOTION.md) bevestigt reversal-/focus-/cleanupgedrag dat bij soepele gedeelde uitklappers behouden moet blijven. Uniformiteit betekent ook dezelfde betrouwbare toestanden; niet alleen dezelfde chevron.

## Eerste concrete vergelijking UI-01

De eigenaar heeft de pijlbedoeling nu bevestigd: productfoto’s. [Vergelijking en conceptwerk](../ui-consistency/2026-10-28/README.md) registreert de gedeelde galerijkandidaat en drie echte desktopverschillen in labels, knopvorm en Ja/Nee-presentatie. Het dossier benoemt de actuele test-/conceptstand; overige ontwerpvarianten zijn nog niet automatisch gecorrigeerd.
