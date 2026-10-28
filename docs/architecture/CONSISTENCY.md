# Eenheidskaart: dezelfde functie, herkenbare bediening

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
