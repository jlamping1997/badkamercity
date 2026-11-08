# FOOTER-FIX-01 — footerconcept en twee live contentcorrecties

**8 november 2026. Content: APPLIED_VERIFIED. Footer: PREVIEW_VERIFIED_DESKTOP / NOT_PUBLISHED.** Op de opdracht “Los iets op” zijn twee concrete contentfouten live hersteld en is de gedeelde footer in een gecontroleerd Shopify-concept toegepast.

## Live opgelost

| Pagina | Wijziging | Onafhankelijke nacontrole |
| --- | --- | --- |
| Antikalk | Alleen de ene H1 in de Page-body naar H2 gewijzigd; bestaande template-H1 blijft leidend | Publieke pagina heeft precies één H1; titel, metadata, canonical, handle, publicatie en template behouden |
| RapoWash | Twee bestaande global SEO-metafields met compareDigest bijgewerkt; eigen douche-wc-titel en beschrijving | Nieuwe publieke title/description gelezen; Reukslot behoudt zijn eigen oude metadata; beide bodies en identiteiten behouden |

Nieuwe RapoWash-titel: **Wat is RapoWash? Uitleg over de douche-wc**. Beschrijving: Lees wat RapoWash betekent bij een douche-wc, hoe reinigen met water werkt en waar je op kunt letten bij het kiezen van een toilet.

[Publieke readback](pages-public-readback.json) en [gerichte herstelwaarden](page-rollback.json). BC-AUD-008/009 en CONTENT-F03/F04 zijn hiermee opgelost; dit is geen Google-indexatie-/rankingclaim.

## Gedeelde footer klaar voor review

**Reviewthema: UNPUBLISHED 196354474250 — BadkamerCity - Eenduidige footer 8 nov.** [Open het concept](https://badkamercity.nl/?preview_theme_id=196354474250). Live MAIN blijft196328685834; er is niet gepubliceerd en geen MAIN-file geschreven.

De bestaande complete reservekopie is hergebruikt. Eerst zijn zes bestaande SEO-/headerpaden byte-exact gelijkgetrokken met verse MAIN; daarna 1.387/1.387 bronpariteit vastgesteld. Pas daarna zijn twee footerfiles aangepast. Finale volledige herlezing van beide manifesten:1.387 bestanden, 1.385 gelijk, precies 2 bedoelde verschillen, 0 ontbrekend/extra en MAIN 0 verschillen met de nulmeting.

| Bestand | Aanpassing |
| --- | --- |
| sections/footer-group.json | compact_homepage=false;17 blocks met 4 service, 10 categorie en 3 informatie; alle hoofdcategorieën, root-home delivery/advies/inspiratie en bevestigde contactgegevens |
| sections/footer.liquid | Alleen bestaande category.limit van6 naar 10; dezelfde renderer, CSS, JS, lifecycle en retour-/offerte-/policy-/betaalguards |

Het maximale aantal blijft 18. Schemawijziging moet vóór de afhankelijke sectiongroup worden opgeslagen: een gezamenlijke upload werd gedeeltelijk toegepast omdat de group nog tegen de oude limiet 6 werd gecontroleerd. Na schema-readback 10 is uitsluitend de group opnieuw opgeslagen; beide inhouden exact gecontroleerd.

Telefoon 06 85887536, e-mail info@badkamercity.nl en **Contact- en retouradres (op afspraak): Badkamercity – bij Harry Suiker, Zichtenburglaan 150, 2544 EB Den Haag** staan in het concept. Geen juridische vestiging, openingstijden of betaalmethode verzonnen. Bezorgen/afhalen verwijst naar bestaande /#HomeDelivery, geen ontbrekende shippingpolicy. Native contactpolicy en Contact-body blijven afzonderlijk open; deze release vult de footer.

[Volledig checksumregister](theme-parity.json), [patchoverzicht](patch-summary.json), [14 paginatypen met identieke footerlinkset](preview-routes.json), [echte desktopbrowsercontrole](browser-verification.json), [verificatie en grenzen](verification.json).

De preview-only offertelink wordt door de bestaande guard getoond; deze functie is niet live geactiveerd. De gewone automatische beleidslinks blijven uit shop.policies komen. De conditionele homefooter blijft in de bron beschikbaar maar staat in de gedeelde group uit. Er is geen derde renderer gebouwd.

## Testgrenzen en laatste stap

Echte browser: homepage, Wastafelkranen en Contact tonen dezelfde standaardfooter, tien categorieën en contact-/retourinformatie; geen horizontale footer-overloop waargenomen. Alleen de Zoeken-link is als navigatie gevolgd; geen echte categorieklik als bewezen test registreren. Gemelde desktopbreedte circa 1024–1300 px; geen exact meetframe. Fysieke telefoon, 390 px en 749/750 px-bediening blijven NOT_TESTED. De Liquid-toolkit keurt beide gewijzigde files goed.

**Volgende handeling:** eigenaar bekijkt dit bestaande concept op laptop en telefoon en publiceert het via Webshop→Thema’s bij akkoord. De connector blokkeert themapublicatie; er is geen omweg gebruikt. Daarna verse MAIN, footerlinks en responsive bediening opnieuw controleren. De niet-gebruikte nieuwe duplicatie196368531722 is hernoemd naar Reservekopie live 8 nov; die bevat geen footerfeatures en is niet het reviewdoel.

## Beleidsopmaak bleef geblokkeerd

De correcte HTML-opbouw voor voorwaarden/kennisgeving is lokaal voorbereid met tekstbehoudcontrole. De eerste shopPolicyUpdate voor LEGAL_NOTICE werd echter geweigerd: ontbrekende write_legal_policies-scope. Geen native policy gewijzigd; TERMS daarna niet alsnog geprobeerd en geen andere route gebruikt om deze rechten te omzeilen. BC-AUD-001/002 blijven OPEN/BLOCKED_SCOPE.

## Bronbeheer en herstel

Code blijft op fix/product-cards-2026-10-14 onder shopify/current; main krijgt alleen documentatie. De vijftien eerder gemeten algemene Git/live-verschillen zijn hiermee niet winkelbreed gereconcilieerd. Alleen de twee bedoelde featurefiles deployen naar de bewezen paritaire kopie; geen blind volledig theme-push.

Voor featureherstel vóór publicatie de twee footerfiles van verse ongewijzigde MAIN terugnemen, eerst sectiongroup terug naar zes categorieën en daarna de schemalimiet 6. Voor contentherstel eerst huidige body/digests vergelijken met page-rollback.json en alleen de bedoelde Page-body/twee waarden herstellen. Geen globale rollback over nieuwe externe wijzigingen.
