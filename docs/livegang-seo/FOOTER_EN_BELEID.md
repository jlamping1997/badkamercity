# Eén footer en één beleidsbron

**Stand: 8 november 2026 — CONTACT-RETURNS-01. Footer: OWNER_PUBLISHED / PUBLIC_HTML_VERIFIED.** **MAIN 196354474250 — BadkamerCity - Eenduidige footer 8 nov** is door de eigenaar gepubliceerd en vers bevestigd (`updatedAt=2026-11-08T16:37:38Z`). Twee footer-MD5's komen exact overeen; veertien publieke routes zonder preview tonen dezelfde footer, inclusief tijdelijke telefoon, e-mail en duidelijk contact-/retouradres. De eerdere footerpublicatieactie is afgerond. Geen nieuwe desktop-/mobiele runtimeproef uit deze HTTP-nacontrole afleiden. [Actuele reparatieronde](../repairs/2026-11-08/contact-and-returns/README.md).

De Contactpagina zelf bevat nu ook de bevestigde gegevens en retour-/beleidslinks; het native contactformulier is behouden en twee eigen SEO-waarden zijn toegevoegd. Dit is live publiek teruggelezen. De native Contact policy is hiermee niet automatisch gewijzigd; policybewerking blijft afzonderlijk geblokkeerd door de ontbrekende `write_legal_policies`-scope. Het contact-/retouradres bewijst geen geregistreerde juridische vestiging en er is geen btw-cijfer geraden.

## Retourinformatie — voorbereid in volgend concept

**PREVIEW_IMPLEMENTED_NOT_PUBLISHED:** UNPUBLISHED **196368531722 — BadkamerCity - Retourinformatie 8 nov** is eerst volledig gelijkgetrokken met de nieuwe MAIN (1.387/1.387), daarna op precies vier bestanden aangepast: `sections/bc-returns.liquid`, `locales/nl.json`, `locales/en.default.json` en `templates/index.json`. Vier Liquid-controles (revisie 2) en exacte bronreadback zijn geslaagd. Publiek previewbewijs en review/publicatie staan in het nieuwe reparatiedossier; deze inhoud is nog niet live verklaard.

De tekst brengt de aanmeldroute in lijn met de bestaande native retourpolicy: 30 dagen aanmelden plus 14 dagen terugsturen; rechtstreekse beleidslink; andere uitvoering via retour en nieuwe bestelling; vast contact-/retouradres met afgeven op afspraak; klantbetaalde spijtretour, €75 incl. btw als raming per standaard NL-retourpallet en kosteloze noodzakelijke afhandeling bij een terechte fout/garantie. De homepage noemt het bestelnummer alleen indien bekend. Er worden geen nieuwe commerciële voorwaarden toegevoegd.

De retour-Page-body is bewust niet gewijzigd: deze route rendert de eigen `bc-returns`-sectie en locales. Formactie, veldnamen en formuliercontract zijn behouden; geen nieuwe JavaScript toegevoegd en geen bericht verstuurd. Deze copycorrectie sluit de open verificatie van de herroepingsfunctie of onmiddellijke bewaarbare klantbevestiging niet af.

## Historische voorbereiding en conceptreparatie — vóór eigenaarspublicatie

**Historisch conceptcheckpoint: 8 november 2026 — FOOTER-FIX-01, toen PREVIEW_IMPLEMENTED_NOT_PUBLISHED.** De gedeelde footer staat in **UNPUBLISHED 196354474250 — BadkamerCity - Eenduidige footer 8 nov**. MAIN **196328685834** is ongewijzigd. [Reparatie en actuele bewijsgrenzen](../repairs/2026-11-08/footer-and-content/README.md); [oorspronkelijke audit en routeoverzicht](../audits/2026-11-08/README.md).

Eerst zijn zes actuele SEO-/headerbestanden uit MAIN overgenomen en is **1.387/1.387 pariteit** bevestigd. Daarna zijn precies `sections/footer.liquid` en `sections/footer-group.json` aangepast; **1.385 overige bestanden blijven gelijk**. `compact_homepage=false` kiest de standaardfooter winkelbreed. De inhoud telt **17 blocks: 4 service, 10 categorie, 3 informatie**; de afzonderlijke schemawaarde **category.limit is van 6 naar 10** verhoogd. Schema eerst uploaden, section group daarna.

De conceptfooter bevat de bevestigde tijdelijke telefoon **06 85887536**, e-mail en het gelabelde contact-/retouradres **Zichtenburglaan 150, 2544 EB Den Haag, bij Harry Suiker**. Bezorgen, advies en inspiratie linken winkelbreed naar `/#HomeDelivery`, `/#HomeAdvice` en `/#HomeInspiration`. Bestaande retour-/offerteguards, CSS, JavaScript en policy-/betaalbronnen zijn behouden. Dit is nog geen live footerpublicatie.

Twee afzonderlijke contentproblemen zijn **wel live hersteld en publiek teruggelezen**: Antikalk heeft één H1 na omzetting van de body-H1 naar H2; RapoWash heeft eigen SEO-titel en beschrijving na compare-and-set-correctie van `global.title_tag` en `global.description_tag`. Reukslot, identiteiten, statussen en overige bodyinhoud zijn behouden.

De native voorwaarden/kennisgeving zijn **niet gewijzigd**: de connector mist voor `shopPolicyUpdate` de scope `write_legal_policies`. Die opmaakcorrectie en het ontbrekende verzendbeleid blijven afzonderlijke open taken.

## Historische voorbereiding DOC-LIVE-01 — vóór implementatie in concept

## Bewezen oorzaak

`layout/theme.liquid` laadt één `footer-group`. In `sections/footer-group.json` staat `compact_homepage=true`. `sections/footer.liquid` kiest daardoor op de homepage `snippets/bc-home-footer.liquid`; overige routes gebruiken de bestaande standaardfooter `bcf-v2 bcf-v3`. Deze vier bestanden zijn vers byte-exact gelijk tussen MAIN 196328685834 en de onderzochte Git-bron. Dit is een gevonden renderer-/configuratieverschil.

De 364-routecontrole vindt één `bch-footer` (homepage) en 363 standaardfooters, ook op de gecontroleerde 404-responses. Een aparte gerichte matrix bevat 14 representatieve routes. Dit zijn HTML-/broncontroles; er is geen nieuwe mobiele layoutproef uit af te leiden.

| Onderdeel | Homepage | Standaardfooter |
| --- | --- | --- |
| Totaal links | 25 | 19 |
| Service / assortiment / info | 4 / 11 / 3 | 3 / 7 / 1 |
| Categorie-ingangen | Tien hoofdgroepen + `/collections` | Zes hoofdgroepen + `/collections/all` |
| Extra inhoud | Bezorgen/afhalen, 3D, inspiratie, meer categorieën | Trustitems, merkintro, contact-CTA, uitgebreidere contactkolom |
| Stijl in bron | Achtergrond #102b43, tekst 14 px, logo 185 px | Achtergrond #1a253f, tekst 16 px, logo 240 px |
| Uitklappen | Native details aanvankelijk gesloten | Eigen controller sluit tot en met 749 px en opent vanaf 750 px |
| Contact | E-mail/contactlink; geen telefoon of volledig adres | E-mail/contactlink; geen telefoon of volledig adres |
| Policies | Vijf automatische policies via `shop.policies` | Dezelfde primaire policybron |

De drie themakolommen worden door **section blocks** beheerd, niet door het Shopify-menu “Voettekstmenu” met handle `footer`. Checkout en klantaccount zijn afzonderlijke platformschillen; ze krijgen niet automatisch deze themefooter.

## Eén inhoudsset voorbereiden

Gebruik de **bestaande standaardfooter** winkelbreed. Een nieuwe derde footer is niet nodig. Alleen `compact_homepage` uitschakelen verliest nu categorie-/informatiedekking; inhoud eerst gelijk trekken.

Er bestaan 18 blocks bij een maximum van 18. Acht URL-loze placeholders zijn door de huidige guards verborgen; ze zijn geen acht zichtbare kapotte klantlinks. Hergebruik of vervang ze. Voorstel: **4 service + 10 categorie + 3 informatie = 17 blocks**. Vier extra blocks toevoegen boven de bestaande 18 overschrijdt de schemalimiet.

| Onderdeel | Afspraak |
| --- | --- |
| Service | Contact, echte verzend-/afhaalinformatie, retour aanmelden/herroepen, zoeken; alleen bestaande openbare bestemmingen |
| Assortiment | Tien bedoelde hoofdgroepen winkelbreed behouden; huidige homepagecategorieën niet verliezen |
| Informatie | Merken, 3D-advies, inspiratie; gebruik voor homeankers `/#HomeAdvice` en `/#HomeInspiration` |
| Contact | Badkamercity, info@badkamercity.nl, tijdelijk 06 85887536 en duidelijk gelabeld contact-/retouradres Zichtenburglaan 150, 2544 EB Den Haag |
| Juridische identiteit | KvK-opgave en btw-id eerst verifiëren; geen juridische vestiging afleiden uit de retourlocatie |
| Policies | `shop.policies` als primaire bron; geen tweede handmatig gekopieerde retour-/voorwaardentekst onderhouden |
| Retourfunctie | Bestaande `bc-returns-url`-guard behouden; geen verborgen of kapotte Page linken |
| Offerte | Bestaande `bc-footer-quote`-guard behouden; uploadfunctie niet activeren |
| Ontbrekende bestemming | Eerst echte inhoud publiceren; geen `#`, nepbestemming of “binnenkort” |

## Uitvoering en acceptatie

1. Lees actuele MAIN en de beoogde ongepubliceerde kopie opnieuw. De diepe audit registreert 15 algemene Git/live-verschillen; alleen deze vier footerfiles zijn exact-paritair bewezen. Geen blind deploy vanaf een verouderde bronkopie.
2. Gebruik de bestaande releasewerkwijze met een bewezen MAIN-paritair **UNPUBLISHED** concept. Geen directe live filewrite en geen oude preview alsnog publiceren.
3. Maak de gekozen linkset compleet, vul contactgegevens in en zet `compact_homepage=false`. Native policies inhoudelijk/opmaakmatig apart corrigeren.
4. Controleer homepage, collectie, gewone PDP, tegel, Sunshower, cart, zoekresultaat, Contact, Retour, policy en 404: precies één footer, dezelfde tien hoofdgroepen en geldige bestemmingen.
5. Controleer desktop en 390 px mobiel; grens 749↔750 px, touch, toetsenbord/focus, reduced motion en section load/unload. Geen verloren categorieën, dubbele policies, URL-loze placeholders of ongeldige lokale ankers.
6. Eigenaarreview/publicatie via de afgesproken releaseprocedure; daarna verse publieke route-/HTML-/bedieningscontrole. De voorbereiding hierboven is later in het concept geïmplementeerd; de live footer is nog niet gepubliceerd.

## Huidige policybron en open correcties

De [retourpolicy](https://badkamercity.nl/policies/refund-policy) is live: 30 dagen aanmelden + 14 dagen terugsturen, klant betaalt gewone spijtretour, €75 incl. btw raming per standaard NL-retourpallet, afgeven op afspraak en modelformulier in dezelfde HTML. Verkeerd/ondeugdelijk geleverd heeft een afzonderlijke kosteloze passende afhandeling.

Contact-, privacy-, voorwaarden- en kennisgevingspolicy bestaan eveneens. **Voorwaarden en kennisgeving tonen letterlijke HTML-tags** en hebben geen werkende links in die body. **Verzendpolicy ontbreekt** en geeft 404. De automatische footer kan alleen tonen wat als policy bestaat; een menu toevoegen lost de opmaak of ontbrekende verzendinformatie niet op.

Het retourconcept van 5 november is historische voorbereiding. Werk alleen de huidige native policy als gezaghebbende klantbron bij. Merchant Center moet dezelfde daadwerkelijke termijnen, methoden en kosten teruglezen; die accountinstellingen zijn nog niet onafhankelijk gecontroleerd.

[Bedrijfsgegevens](BEDRIJFSGEGEVENS.md) · [Controles](CONTROLES.md) · [Taken](TAKEN.md) · [Historisch retourconcept](retouren/RETOURBELEID_CONCEPT.md)
