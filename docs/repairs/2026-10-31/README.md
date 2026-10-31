# FIX-01 — betrouwbaar bestellen, filters en presentatie

**31 oktober 2026 · PREVIEW_VERIFIED / OWNER_REVIEW_PENDING.** Eigenaar geeft opdracht de gedocumenteerde fouten gericht te herstellen. Actieve branch: `fix/product-cards-2026-10-14`. Dit dossier vervangt het tussencheckpoint; oude before/replay-JSON blijft historisch bewijs. Geen schrijver of achtergrondtaak blijft actief na overdracht.

## Wat staat waar?

| Onderdeel | Stand en bewijs |
| --- | --- |
| Live thema | **195947036938 — BadkamerCity - Categorieen zonder schuiven**. Eigenaar heeft NAV-02 gepubliceerd vóór deze uitvoering. Alle 1.354 paden in eindmanifest gelijk aan opening; MAIN-bestanden niet geschreven. |
| Reviewconcept | **195948839178 — BadkamerCity - Betrouwbaar bestellen en filters**, UNPUBLISHED. 1.355 bestanden: 20 gewijzigde bestaande paden + één nieuwe gedeelde tegelprijssnippet. Exact 21 bedoelde verschillen. Niet gepubliceerd. |
| Conceptbasis | Beide volledige manifests hadden aanvankelijk alleen een headerachterstand. Verse MAIN-header exact naar concept overgenomen; vóór featurewrites opnieuw volledige nul-diff. Header blijft daarna gelijk aan MAIN. |
| Hygrometer | Twee live URL-redirects naar bestaande gepubliceerde `/pages/hygro-meter`. GraphQL readback én drie openbare GETs eindigen HTTP 200 met correcte H1/canonical. Geen nieuwe dubbele pagina. |
| Retouren | Bestaande gepubliceerde pagina blijft native contactaanvraag. **MAIL_DELIVERY_PENDING**: geen mailboxontvangst/spam/antwoord of retourlabel bewezen. |
| Offerte | **CUSTOMER_ACTIVATION_DISABLED** behouden. Privéaccount-/mailverificatie door eigenaar; geen hernieuwde toegangspoging en geen activatie. |

De volledige Git-root is geen actuele MAIN-snapshot. Alleen de 21 expliciete featurepaden zijn als implementatie overgenomen. Settings_data.json niet geüpload of openbaar opgeslagen; de bestaande body/hash-uitzondering blijft zichtbaar. De retourtemplate heeft een bestaande commentaar-/byte-uitzondering; geen nieuwe wijziging eraan. [Einddiff](final-theme-delta.json) · [manifestcontrole](manifest-verification.json) · [hashes](final-source-provenance.json).

## Herstelde contracten

| Gebrek | Gedrag na herstel | Eigenaarcode en bewijs |
| --- | --- | --- |
| CART-F01: oud artikel bij ontbrekende sections | Productinhoud wordt gewist, CTA wordt generieke cartlink, onbekende oude teller wordt verborgen. Geldige nieuwe sections kunnen later weer verversen. Geen tweede add-verzoek. | `cart-notification.js`; CN-02/03/08, native dialogfixture |
| SS-F01: set wijzigen/dubbel proberen tijdens koopactie | Configuratie, aantallen, extras en andere lokale koopformulieren zijn geblokkeerd tijdens pending. Ook een niet bevestigde fout blijft vergrendeld met route om de cart te controleren; bfcache ontgrendelt niet blind. | `bc-sunshower-page.js`; SS-01…04 |
| FILTER-F01: oude externe controller na native terugval | Na eerste fallback bezit native Shopify de huidige pagina. Externe requests/popstate en verouderde DOM-writes stoppen; nieuwe volledige paginanavigatie mag opnieuw starten. Debounce wordt gewist. | `bc-external-filters.js`; FX-37 incl. echte native gridmethode |
| FILTER-F02: verkeerd aantal na Toon minder | Eerste weergave en opnieuw inklappen delen dezelfde ingestelde facetlimiet; geselecteerde opties blijven zichtbaar. | FX-22 |
| Zoekstatus/titel spreekt actieve lijst tegen | Native statusteksten verdwijnen bij externe activatie; titel gebruikt actieve telling. Bij fallback komt oorspronkelijke native titel terug. Correcte enkele HTML-escaping. | FX-42; browser native606 → extern337 en titel337 |
| Tegenstrijdige verzendcopy | Zoekstrip sluit aan op bestaande €100-copy. Onbewezen 22:00/vandaagverzondenclaim vervangen door “Levertijd per artikel”. | locale NL/EN + USP-strip; renderfixture en browser |
| Tegeldoosprijs oogt als m²prijs | Gedeelde helper labelt doosprijs/inhoud en m²prijs op native, custom search en gehydrateerde externe cards. Geen dubbele m²regel bij bestaande unit measurement. Alleen geverifieerde positieve doosoppervlakte; geen verzonnen eenheid voor gewone producten. | `bc-card-tile-price.liquid`, cards/data/CSS; FX-43/44, Liquidfixtures, HTTP/browser |
| Vooraf ingevuld tegeloppervlak / verouderd totaal bij fout | Actieve `bc-porcelanosa-buybox` begint leeg en neutraal, bestellen uit tot geldige invoer. Bestaande 10% snijverlies behouden. Handmatige dozen blijven werken met 0% extra afval; fouten wissen oud totaal en blokkeren koopknoppen. Expliciet opgeslagen keuze blijft geldig. | Actieve buybox-JS/snippet; 6 calculatorchecks + echte productpagina |
| WISH-F01: gelijktijdige keuzes overschrijven elkaar | Elke identity-intent wordt tegen actuele opslag gecommit; native Web Locks serialiseren wanneer beschikbaar. Twee add-intents maken geen toggle-off. Zonder Locks vermindert opnieuw lezen het risico, maar biedt geen atomiciteitsgarantie. | `bc-wishlist.js`; WL-23/44/45 + native same-origin framecontrole |
| WISH-F02: Sunshower-hartje verouderd na kaartrender | Nieuwe kaart synchroniseert direct via publieke scoped refresh. Intent volgt bekende identiteit/geheugen bij klik, niet een achtergebleven aria-status. | `bc-sunshower-shop.js` + wishlist; WL-43 |
| Beschadigde/onleesbare wishlist kan worden overschreven | Commit leest strikt en weigert bij onzekere bestaande opslag; geen succesmelding of stil vervangen door leeg. Initiële lege presentatie blijft als benoemde grens. | WL-46 en bestaande foutpaden |
| Footerlabels zonder bestemming | Buiten Theme Editor alleen bruikbare bestemmingen zichtbaar; editor behoudt placeholders. “Onze merken” wijst naar bestaande merkengids. Retourgate en verwijderd adres blijven behouden. | footer.liquid/footer-group.json; renderfixture/browser |
| Lege collectieomschrijving voor SEO | Alleen lege page_description krijgt compacte gelokaliseerde titelgebonden fallback van max160 tekens; bestaande redactie behouden. Geen collectie-HTML/styleblokken lekken in meta/OG/Twitter. | layout/theme.liquid/meta-tags; renderfixtures en twee HTTP-reads |

**Waarom Sunshower ook bij 422 eerst cart controleren vraagt:** een Shopify add kan deels slagen en toch een voorraadfout teruggeven. Netwerkfout of null section bewijst evenmin dat niets is toegevoegd. Geen automatische retry is hier het veilige koopcontract; een label “mislukt” is geen rollback.

## Gecorrigeerde bronaanname tijdens de controle

De oude `bc-tile-fix-preview`-variant had 0% als markupdefault. De echte huidige PDP gebruikt `main-product → bc-porcelanosa-buybox`, met reeds 10% én handmatige doosbediening. De browsercontrole toonde dat een wijziging van alleen de oude preview de klantpagina niet wijzigde. Daarom zijn die twee inactieve previewbestanden exact hersteld en uitsluitend de actieve renderer aangepast. Het einddiff bevat geen previewvariant. De 10% was dus al correct in de actieve calculator; die waarde wordt niet als nieuw ingevoerde zakelijke instelling geclaimd.

## Testresultaat en grenzen

**126 lokale gevallen/checks**, uitgevoerd met exacte SHA-256-broncontrole, uitsluitend synthetische requests/opslag: 18 cart/Sunshower, 44 filters, 46 wishlist en 18 presentatie/calculator. Binnen de eerste drie: **81 controles +15 regressies +12 expliciete grenzen**, nul resterende DEFECT_REPRODUCED in deze nieuwe harnesses. De 18 presentatiechecks slagen. Dit zijn geen 126 aangetoonde productie-incidenten en ook geen certificering van elke winkelroute.

[Cart/Sunshower](final-cart-sunshower.json) · [filters](final-filters.json) · [wishlist](final-wishlist.json) · [presentatie](final-presentation.json). Historische harnesses en before-logs niet aangepast om oude fouten te verbergen.

Theme Check R4/R5/R6/R7: gewijzigde bestanden geldig; vijf bestaande niet-blokkerende waarschuwingen in layout/search/card blijven benoemd. De eerste poging kon niet draaien zonder pakketdependencies; na installatie ontbrak validatorcontext en daarna is de verse schema-locale toegevoegd. Pas resultaten vanaf R3 gelden als codevalidatie. [R4](theme-check-r4.txt) · [R5](theme-check-r5.txt) · [R6](theme-check-r6.txt) · [actieve calculator R7](theme-check-r7.txt). Git diff-whitespacecontrole meldt alleen de al in de verse MAIN aanwezige lege regel met twee spaties in card-product.liquid:27; geen nieuwe whitespacefout in de featurepatch. Geen runtimebibliotheek toegevoegd; LiquidJS is alleen een gepinde testdependency.

**Echte Cloud Chrome, 1348×926:** native cartdialog met fictieve sections; oude inhoud/teller weg bij onvolledige B; Escape en Sluiten herstellen focus. Echte Locks in twee same-origin frames bewaren beide fictieve keuzes onder een afzonderlijke tijdelijke sleutel, daarna opgeruimd. Dit bewijst niet alle top-level tab-/browserprocessen of browsers zonder Locks. Echte huidige tegel-PDP: leeg/10%/neutraal/geblokkeerd; 10m² →11m² nodig →8dozen →11,44m² →€1.143,44; handmatig3dozen →4,29m²/€428,79; 0m² toont fout/geen oud totaal. Geen echte cartwrite/order/checkout. [Browserbewijs](browser-verification.json).

Zoeken liet native606 en extern337 zien. De actieve externe lijst en titel tonen beide337; enkele apostroffen correct. Sorteer-URL en terugknop herstellen de controlestand; geen afzonderlijke uiteindelijke prijsvolgordeclaim. Indexinhoud en Shopifytelling zijn niet gelijkgemaakt. Footer toont echte links en geen adres/lege labels. Tijdelijke QA-template direct daarna exact hersteld naar MD5 `24ae4cff55afe7f2453e4e9b6a0c2479`; geen extra QA-afwijking in eindmanifest.

[HTTP-presentatie](presentation-http-after.json): Wandtegels heeft nieuwe bruikbare meta/OG-fallback en24dooslabels; bestaande Badkamermeubels-SEO behouden, geen stylelekkage. [Redirect-HTTP](hygrometer-http-after.json): twee oude routes en canoniek eindpunt HTTP200.

Niet gedaan: fysieke iPhone/Windows/laptopcontrole, nieuwe volledige mobiele responsive matrix, echte koopactie, mailbox-/klantmail-/retourlabelbewijs, privé-Jotform/VPS/indexmutatie, rankings of performanceclaims. NAV-02 heeft eigen gedateerd breedtebewijs; publicatie ervan is in deze beurt wel opnieuw vastgesteld.

## Reproduceren

In de actieve branch: `npm ci --prefix scripts/component-audit`, daarna `node scripts/component-audit/replay-fix01.mjs /absoluut/pad/naar/resultaten`.

Het script maakt een tijdelijke geselecteerde bronmap, controleert alle26hashes en draait de vier harnesses. De21kandidaatbestanden en ongewijzigde facetsbron komen uit de checkout. Vier expliciete MAIN-dependencies die niet gelijk zijn aan de historische Git-root zitten als onveranderlijke fixtures onder `scripts/component-audit/fixtures/fix01-baseline/`. Die fixtures zijn geen nieuwe productiecode of volledige themesnapshot. Een gewijzigde kandidaat faalt de hashcontrole en vereist bewuste nieuwe bronregistratie. Geen echte netwerkrequest is toegestaan in de replays.

## Open punten en eigenaarstest

1. **Retourmail:** één herkenbare fictieve aanvraag met ordernummer `TEST-GEEN-ECHTE-ORDER`, retourreden en gewenste oplossing versturen; ontvangst in info@badkamercity.nl, spam, leesbaarheid en antwoordroute controleren. Pas na daadwerkelijk mailboxbewijs sluiten. Dit formulier maakt geen RMA-/label-/refundautomatisering; behandeling en labelbesluit zijn handmatig.
2. **Offerte:** eigenaar voltooit bestaande mailverificatie en ontvangst/opslag/privacy-/verwijdercontrole. Klantactivatie blijft uit; geen privétoegang opnieuw proberen.
3. **Resterende contractgrenzen:** omgekeerd prijsbereik bereikt nog API; native/externe parameterdialecten worden niet gemigreerd; response-collectionidentity is geen nieuwe harde validator; searchable-facetflag levert nog geen extra waardezoeker. Niet stil als gerepareerd markeren. Backend-/UXbesluit en gerichte test nodig.
4. **Wishlist:** zonder Web Locks/oudere tabversie geen atomaire garantie; bestaande dubbele/corrupte opgeslagen arrays worden niet gemigreerd. Productread heeft geen nieuwe timeout/TTL. Bewaren is geen voorraadreservering.
5. **Review en publicatie:** Jackson beoordeelt dit exacte concept en de echte telefoon. Theme-publicatie door eigenaar volgens AGENTS. Na publicatie opnieuw rolread en gerichte controles van de koop-/zoekroutes.

## Terugzetten

[Per pad](rollback-manifest.json): herstel de twintig originele bestaande bodies uit de gecontroleerde MAIN/baseline, met vooraf nieuwe rol-/hashcontrole zodat later eigenaarwerk niet overschreven wordt. Verwijder de nieuwe helper pas nadat callers hersteld zijn. Oude live MAIN195947036938 blijft beschikbaar; geen automatische publicatieswap. Tijdelijke QA is al hersteld en geen onderdeel van deze rollback.

Adminrollback afzonderlijk: redirect617898017034 (`/begrippenlijst/hygrometer`) had oorspronkelijk target `/pages/hygrometer`; nieuwe alias687302050058 is `/pages/hygrometer → /pages/hygro-meter`. Alleen indien inhoudelijk nodig de oorspronkelijke redirect herstellen en de nieuw gemaakte alias verwijderen, na verse readback. Dit brengt de oorspronkelijke404 terug en is geen aanbevolen herstelactie. Bestaande pagina’s blijven behouden.

**Exact volgende handeling:** Jackson beoordeelt het UNPUBLISHED concept195948839178 en voert de gemarkeerde retourmailboxproef uit. Geen codewriter blijft actief; publicatie en offerteactivatie niet uitgevoerd.
