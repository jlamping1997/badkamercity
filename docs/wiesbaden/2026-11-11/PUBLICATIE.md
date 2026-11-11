# Wiesbaden — publicatie gereed, laatste klik door eigenaar

11 november 2026. De eigenaar heeft expliciet opdracht gegeven alle goedgekeurde keuzemenu’s te publiceren en de65 twijfelgevallen ongemoeid te laten. Die65 zijn bewust uitgesteld en mogen zonder nieuwe opdracht niet verder worden aangepast of onderzocht.

**Status: VERIFIED_READY_MANUAL_PUBLICATION_REQUIRED. Er is nog geen publicatie bevestigd.** De Shopify-koppeling heeft de ontdekte themePublish-mutatie geweigerd wegens de beveiligingsregel “Publishing a theme is blocked here”. De genoemde aparte theme_publish-functie is niet beschikbaar in deze omgeving. Geen andere API-, live-file- of browserroute gebruikt om deze blokkade te omzeilen.

Doelthema: **196441932042 — BadkamerCity - Wiesbaden vervolg concept (UNPUBLISHED)**. Huidig live/terugvalthema: **196416504074 — BadkamerCity - SEO + Wiesbaden concept (MAIN)**. De reserve196395073802 en het oude189117628682 blijven behouden.

## Gecontroleerde inhoud

- 268 actieve Wiesbaden-groepen met1845 unieke uitgebreide producten. Cumulatief2386/2451 menubeoordelingen afgerond;65 bewust uitgesteld, niet als afgerond tellen.
- Volledige bestandsvergelijking: MAIN1436 bestanden, concept1684.1434 bestaande bestanden zijn exact gelijk. Alleen sections/main-product.liquid en snippets/bc-choice-data-source.liquid verschillen;248 begrensde JSON-assets zijn toegevoegd, geen bestanden verwijderd. Bestaande JS, andere merken, instellingen, templates en overige vormgeving hebben dezelfde checksums.
- Onafhankelijke controle van alle268 routes, product-/variant-/URL-identiteiten, assen en unieke keuzetupels PASS.254 compacte groepen plus14 bestaande niet-compacte groepen zijn bewust behouden.35 oude routes worden268 actuele routes;233 toegevoegd en één bestaande Ribbd-route naar de geverifieerde uitbreiding verplaatst. Ongebruikte eerdere JSON-versies blijven beschikbaar.
- Alle65 uitgestelde product-ID’s/SKU’s ontbreken in de actieve groepen. Vier keuzeroutevelden per product zijn vers gelezen en leeg: custom.switch_group, custom.color_variants, custom.group, custom.switch_key. Geen productmutaties in deze publicatieronde.
- Eerdere bron- en batchcontroles blijven gelden; dit is een releasecontrole en geen nieuwe volledige1845-productbron- of Admin-hercontrole.

## Browser en winkelwagen

Desktop: Ribbd29.5301, Chroom/Standaard(coldstart)/€145 →29.5310, Chroom/XL(zonder coldstart)/€219. Geselecteerde uitvoering, eigen titel/SKU/prijs, ontbrekende combinaties en native winkelwagenknop correct.

De echte native productknop heeft variant53859822338314 van29.5310 éénmaal voor€219 aan een vooraf lege testwinkelwagen toegevoegd. Productnaam, variant en prijs exact bevestigd. Alleen dit testartikel daarna verwijderd; winkelwagen weer leeg. Geen checkout of bestelling.

Responsive: dezelfde browser op449CSS-pixels breed via de normale browserzoom. Geen horizontale overflow, uitvoeringsknoppen passen en breken over regels. Wissel29.5310→29.5301 geeft de juiste geselecteerde uitvoering, titel/SKU en€145. Browserzoom teruggezet naar100%. Geen fysieke telefoontest of volledige responsive regressie van alle268 groepen.

## Laatste eigenaarhandeling

Open https://admin.shopify.com/store/fpa9hu-i3/themes. Kies **Publiceren** bij **BadkamerCity - Wiesbaden vervolg concept** en bevestig de publicatie. Het andere thema met “SEO + Wiesbaden concept” is de bestaande liveversie en wordt niet gekozen.

Daarna eerst via Admin opnieuw controleren dat196441932042 MAIN is en196416504074 UNPUBLISHED, gevolgd door enkele verse productpagina’s zonder previewparameter. Markeer publicatie pas dan als voltooid. Geen verdere actie aan de65 uitgestelde producten.

## Terugval

Bij een werkelijk publicatieprobleem kan de eigenaar het behouden thema196416504074 opnieuw publiceren. Er zijn in deze ronde geen themafiles of productvelden geschreven; herstel daarom geen productmetafields uit oude batch-rollbackbestanden. De bestaande batchherstelgegevens blijven uitsluitend voor hun eigen eerdere wijzigingen gelden.

Bewijs: PUBLICATIE_CHECKS.json, PUBLICATIE_BESTANDSVERGELIJKING.json en PUBLICATIE_ONAFHANKELIJK.json. Codebasis voor de goedgekeurde menu’s: d1c746b573382d7616ecd2f179bfb8629e285bad op fix/product-cards-2026-10-14, shopify/current.
