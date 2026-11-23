# Drie thema’s vergeleken en vereenvoudigd — 10 november 2026

THEME-CONSOLIDATION-01 / VERIFIED_SOURCE_AND_PREVIEW / WIESBADEN_QA_STILL_PENDING.

## Opdracht

Eigenaar toont de actieve SEO-versie en twee concepten die kort na elkaar zijn bijgewerkt. Nieuwe expliciete voorkeur: “Alles mag gewoon op index staan”. Dit trekt het extra noindex-voorstel voor lege categorieën in. Het is geen nieuwe opdracht om categorieën te vullen, collectiepublicaties te wijzigen of een thema te publiceren.

## Uitkomst

| Rol | Huidige naam | ID | Bestanden | Werkelijke inhoud |
| --- | --- | --- | ---: | --- |
| MAIN | BadkamerCity - SEO afronding 10 nov | 196441932042 | 1.401 | Bestaande gepubliceerde basis met 181 SEO-metaparen |
| Enig uitvoerend concept | BadkamerCity - SEO + Wiesbaden concept | 196416504074 | 1.418 | Dezelfde vier SEO-files plus 17 groepen voor 110 Wiesbaden-producten |
| Reserve | Reserve - gelijk aan live 10 nov | 196395073802 | 1.401 | Op alle 1.401 actuele checksums identiek aan MAIN |

Het thema met de oude naam Merkenbalk zonder pijlen had de vier actuele SEO-bestanden al overgenomen in de Wiesbaden-uitvoering. Geen nieuwe code-integratie tussen MAIN en dat concept nodig. De 21 verschillen zijn vier bestaande keuzebestanden en zeventien nieuwe groepsassets; niets ontbreekt ten opzichte van MAIN. Onder andere homepage, menu’s, prijsopmaak en bestaande productkaarten delen dezelfde basis, buiten de vier benoemde switcherbestanden.

Het voormalige Lege categorieen tijdelijk uit had exact één verschil: de extra robotsvoorwaarde in layout/theme.liquid. Die is ingetrokken. De reserve-layout is vervangen door de exacte huidige MAIN-body; de andere 1.400 bestanden zijn niet geschreven. De hele reserve is daarna opnieuw gelijk bevonden. Het active thema en alle Wiesbaden-featurebestanden zijn volledig ongewijzigd gebleven. Twee namen aangepast; geen extra thema aangemaakt of gepubliceerd.

## Controle

- Alle drie manifesten volledig gepagineerd vóór én na de ene filewrite: MAIN1.401 / Wiesbaden1.418 / reserve1.401.
- Finale MAIN volledig ongewijzigd. Alle 1.418 Wiesbaden-bestandschecksums gelijk aan vóór deze taak; alleen de naam veranderd.
- Vier SEO-bestanden in alle drie thema’s exact gelijk: layout/theme.liquid, snippets/meta-tags.liquid, locales/nl.json, locales/en.default.json.
- Reserve-layout exact teruggelezen; checksum abc5ba016b9eaa6db486741c9701aeec. Geen bc_empty_category_handles-blokkade meer. Bestaande robotskeuzes voor technische pagina’s, waaronder de verlanglijst, behouden.
- Officiële lokale Shopify-validator op de herstelde layout: geldig, nul fouten, alleen de bestaande scheme_classes-waarschuwing.
- Alle zeventien actuele JSON-groepsassets gelezen: 17 groepen,110 unieke product-ID’s, geen dubbele volledige optiecombinaties; URLs, variant-/productidentiteiten, menuwaarden en routerverwijzingen consistent. JS-syntaxis PASS.
- Werkelijke HTTP-controle:18 PASS. Homepage, merkenoverzicht, Wiesbaden-vendorlijst, Wastafelkranen en lege Toiletspiegels op alle drie thema’s; juiste theme-ID,200,status van title/description/H1/canonical/og/robots identiek en geen categorie-noindex. Drie PDP-monsters (UniMatch,Loft,Ribbd) verwijzen in het concept naar hun bedoelde groepsasset.
- Lokale HTML-rapportlogica gecontroleerd:181 live metaparen,0 actieve noindexvoorstellen,58 assortimentsholds behouden. Geen lokale browser-render geclaimd.

Deze vergelijking en 18 HTTP-checks zijn geen nieuwe volledige 110-artikelenvrijgave. De eerdere Wiesbaden-run heeft85transportfouten bij de publieke servertest en nog open nieuwe cart-/native mobiele proeven. Die blijven zichtbaar in CHOICE_PILOT.md. Geen checkout, bestelling, betaling, ranking, CTR of fysieke-telefooncheck geclaimd.

## Wat nu gebruiken

Laat MAIN actief totdat de Wiesbaden-taak de resterende publieke, mobiele en cartnacontrole afrondt. Werk uitsluitend verder op **196416504074 — SEO + Wiesbaden concept**. Dat is al de combinatie van SEO en Wiesbaden; geen noindexdelta uit de reserve meer meenemen. Eerst verse rollen en bronnen lezen bij een nieuwe sessie.

De reserve is alleen terugval en bevat geen extra verbetering om te publiceren. De oude V1.0 is niet beschreven of verwijderd.

De 57 lege collecties blijven assortimentsholds: geen producten gekoppeld en geen meta’s uit de oude vijf invulvoorstellen toegepast. Alleen het noindex-voorstel is ingetrokken. Online Store-publicatie en de bestaande ongepubliceerde Tegeltoebehoren-route zijn niet gewijzigd.

## Herstel en opslag

Vooraf de volledige drie inventarissen en de vier SEO-bodies privé bewaard in Badkamercity-themas-vergelijking-backup-2026-11-10.json. Herstel bij behoefte uitsluitend de ene reserve-layout en/of de twee namen, na controle van huidige checksums en de laatste eigenaarvoorkeur. Niet een complete oude themakopie over nieuw werk zetten.

Codebranch fix/product-cards-2026-10-14: alleen shopify/current/layout/theme.liquid terug naar actuele MAIN-body. Alle andere Wiesbaden-code behouden. Main ontvangt uitsluitend documentatie. Geen lokale Git-checkout of Windows-controle. Geen MAIN-filewrite, product-/collectie-/menu-/prijs-/voorraadmutatie of publicatie.

Eén volgende handeling: de bestaande Wiesbaden-QA hervatten op 196416504074, zonder nieuwe families toe te voegen totdat de vastgelegde controlegrenzen gesloten zijn.
