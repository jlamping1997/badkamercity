# Homepage SEO — 8 november 2026

Taak SEO-HOME-01. Eigenaar vraagt na de Search Console-inrichting verder te gaan met de homepage. Bron: Shopify MAIN 196341825802; concept 196328685834 — BadkamerCity - Homepage SEO 8 nov. Codebranch fix/product-cards-2026-10-14, themabron shopify/current/. Main krijgt uitsluitend documentatie. Geen publicatie door de uitvoerder.

## Gewenste werking

| Onderdeel | Eerder | Voorstel in concept |
| --- | --- | --- |
| Effectieve SEO-titel | Badkamercity | Badkamerproducten, tegels en kranen – Badkamercity |
| Meta description | Ontbreekt | Alles voor je badkamer: tegels, kranen, douches, badkamermeubels, spiegels en toiletten. Bekijk het assortiment van BadkamerCity en kies wat bij je past. |
| Eerste campagnekop | Kleine update. Groot verschil. | Alles voor jouw badkamer. |
| Homepage H1 | Logo plus campagnekop | Alleen campagnekop; logowrapper wordt div met dezelfde klasse |
| Gedeelde afbeelding | Ontbreekt | Bestaand bch-primary.webp, 1440 × 480; geen nieuwe media-upload |

De homepage-titel krijgt alleen een themavangnet wanneer page_title leeg is of gelijk aan shop.name. De beschrijving krijgt dit alleen wanneer page_description leeg is. Een later ingevulde eigen SEO-titel/beschrijving blijft voorgaan. Deze taak wijzigt geen globale Shopify-voorkeuren. Beide teksten en afbeelding-alt staan in nl/en-localevelden. De bestaande merchantinstelling van de campagnekop blijft bewerkbaar via het homepageblok.

De afbeelding is het bestaande kraan-/waskombeeld van de homepage. De voorkeur blijft een expliciete page_image wanneer die beschikbaar is; anders geldt de nieuwe fallback uitsluitend voor de homepage. Product-, categorie-, advies-, zoek- en verlanglijstroutes krijgen geen nieuwe homepagegegevens. De bestaande canonical, wishlist-noindex, product-schema’s en foto-uitzonderingen blijven gelden.

## Bestanden

- shopify/current/layout/theme.liquid
- shopify/current/sections/header.liquid
- shopify/current/templates/index.json
- shopify/current/snippets/meta-tags.liquid
- shopify/current/locales/nl.json
- shopify/current/locales/en.default.json

config/settings_data.json blijft beschermd en wordt niet geüpload. Het bestaande, niet-actieve concept 196328685834 is eerst op acht bestanden gelijkgetrokken met MAIN. Daarna 1.387/1.387 metadata-checksums gelijk, nul ontbrekend/extra. Pas daarna zijn de zes featurewijzigingen geplaatst. Een succesvolle kopie is geen vrijgave van de historische settings_data-API-bodyuitzondering.

## Search Console — eigenaarsscreenshots

- Domeinproperty badkamercity.nl via DNS geverifieerd. Verificatiecode niet in publieke Git opgenomen.
- Hoofdsitemap https://badkamercity.nl/sitemap.xml: Sitemap index processed successfully. Dit is geen bewijs van alle kind-sitemaps of productindexatie.
- Homepage: Google Index Page is indexed; aparte live-test beschikbaar/indexeerbaar.
- Wastafelkranen: Google-indexstatus URL is unknown to Google; live-test geslaagd en Indexing requested bevestigd. Opname in de Google-index blijft onbewezen.
- Overige indexdekking, zoekprestaties, Merchant Center, GA4 en Core Web Vitals blijven open.

## Validatie en actuele status

Voorbereiding: zes Shopify Theme Check-uitkomsten zonder fouten, met één waarschuwing over het reeds bestaande scheme_classes in de layout. Locale-/template-JSON parsebaar; diff-whitespacecontrole geslaagd. De validator gebruikte de meegeleverde schema’s nadat het ophalen van de nieuwste documentatiecache niet lukte. Geen claim dat die documentatiecache is bijgewerkt.

Conceptstatus **PREVIEW_VERIFIED / OWNER_REVIEW_PENDING**. Eindmeting: MAIN 1.387 bestanden en nul afwijkingen; concept 1.387 bestanden met precies zes bedoelde verschillen en nul overige verschillen. Alle zes writes exact teruggelezen. Tijdelijk breedtecontroletemplate daarna checksum-exact hersteld naar 9046f6312adff5be09cfca657cf351a9; geen template-toewijzing.

Veertien HTTP-responses, zeven MAIN-/conceptparen: alle 200, werkelijk juiste theme-ID per response gecontroleerd. Homepage heeft bedoelde titel, één meta description van 153 tekens, één H1 en één HTTPS og:image. Canonical gelijk. Wastafelkranen en pagina 2, Hotbath-, tegel- en Sunshower-product en verlanglijst: titel/beschrijving/H1/canonical gelijk; wishlist-noindex behouden. Cookies zijn per previewrequest behouden; de eerste cookieloze poging viel terug naar MAIN en is niet als conceptbewijs gebruikt.

Werkelijke Chrome-preview op 1363×936 bekeken: nieuwe kop en afbeelding zichtbaar, geen documentoverloop. De extra offerteknop is de reeds bestaande preview-only-regel quote_cta_preview en theme.role != main; geen offerteactivatie gewijzigd. De instellingenbody is tussen MAIN en concept gelijk teruggelezen; de historische API-body/checksumgrens blijft open.

**Mobiel NOT_TESTED:** echte storefrontframes werden geweigerd. Navigatie naar een lokale statische momentopname is door de browser-URL-policy geblokkeerd; niet via een andere route omzeild. De tijdelijke remote testtemplate is hersteld. Geen mobiele visuele vrijgave of telefoonclaim. Eigenaar controleert zijn telefoon vóór publicatie. Cart/checkout/formulier, performance en Google-effect zijn niet getest.

De trage native reservekopie 196354474250 is hernoemd naar BadkamerCity - Reservekopie voor homepage SEO en heeft geen feature-writes gekregen. Laatst waargenomen nog in Shopify-verwerking; dit is niet het te beoordelen of publiceren concept. Geen AI-achtergrondschrijver actief na overdracht.

## Beoordeling en herstel

Jackson beoordeelt straks het voorbeeld van precies dit genoemde concept en publiceert zelf na akkoord. Vlak vóór publicatie de actuele MAIN en eventuele tussentijdse verschillen opnieuw controleren. De huidige livewinkel blijft de bron voor herstel; de zes oorspronkelijke bronbestanden zijn gecontroleerd vastgelegd. Alleen de bedoelde featurepaden terugzetten bij terugdraaien; geen blind volledig thema-upload en geen product-, prijs- of voorraadmutatie.

## Volgende handeling

**Jackson opent Webshop → Thema’s → BadkamerCity - Homepage SEO 8 nov → Voorbeeld, controleert laptop en telefoon en publiceert zelf bij akkoord.** Vlak vóór publicatie opnieuw MAIN en eventuele tussentijdse wijzigingen controleren. Na publicatie de nieuwe MAIN en openbare homepage teruglezen; daarna pas de SEO-taak als live aftekenen. De gewone meta- en kopverbeteringen beloven geen Google-positie.
