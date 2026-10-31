> **Actueel: Jotform-account en formulier bestaan.** Formulier263018521531044 is aangemaakt, met fictieve PDF getest en alleen in het ongepubliceerde websiteconcept gekoppeld. Meldingen naar info@badkamercity.nl; verificatie/bezorgbevestiging nog nodig. Klantmail en publieke klantactivatie uit. Zie [actuele integratie en testgrenzen](INTEGRATION.md). Eerdere account-/rolmeldingen hieronder zijn geschiedenis.

> **Actueel besluit:** footerlink onder Klantenservice in beide footers voorbereid en getest; klantactivatie uit. MAIN195915448586 door eigenaar gepubliceerd; reviewconcept195916628234. [Footer, bewijs en aansluitstatus](FOOTER.md). Uploadkoppeling blijft accountafhankelijk.

> **Actueel:** eigenaar wil geen offerteactie in de mobiele header. Zie [desktopknop en voorstellen voor betere plaatsen](HEADER.md). Reviewconcept195915448586; MAIN195916628234 door eigenaar gepubliceerd. Upload blijft uit.

> Headeruitbreiding: [Offerte uploaden op desktop en mobiel](HEADER.md), 30 oktober 2026. Alleen conceptpreview, klantknop uit.

# BC-QUOTE-001 — offerte vergelijken

30 oktober 2026, Europe/Amsterdam. Eigenaar kiest uitvoering van offertevergelijking. **DESIGN_IMPLEMENTED / INTEGRATION_PENDING_ACCOUNT / NOT_PUBLISHED.** Dit is een concreet reviewbaar ontwerp met een voorbereide providerkoppeling, geen werkende ontvangst-/uploaddienst.

## Goedgekeurde commerciële aanvulling

Eigenaar bevestigt30oktober expliciet: **Laagsteprijsgarantie — stuur je offerte op en ontvang een betere prijs.** Dit vervangt de eerdere terughoudende formulering. NL/EN-kop, intro, stappen, formulierkop, FAQ en homepageverwijzing aangepast. Gelijkwaardige vergelijking betekent dezelfde artikelen, aantallen en afwerkingen, inclusief btw en verzending. Geen extra kortingspercentages, termijnen of uitzonderingen toegevoegd. Geen review als voorwaarde voor de prijs gesteld.

Eigenaar heeft nog geen Jotform-account. Accountkeuze/inrichting blijft de volgende praktische stap; upload en homepageverwijzing blijven uit. Conceptpagina is opnieuw als ongepubliceerd teruggelezen met titel Laagsteprijsgarantie — offerte vergelijken. [Nieuwe tekst in preview](guarantee-desktop.jpg) · [readback](guarantee-readback.json) · [localevalidatie](guarantee-themecheck.json). Veertien bestaande render-/gatecases opnieuw PASS. Geen nieuwe upload-/ontvangsttest of mobiele hercontrole geclaimd bij deze tekstwijziging. Oudere screenshots/FAQ-beschrijvingen hieronder horen bij de eerste ontwerpversie.

## Omgeving en scope

MAIN **195915448586 — BadkamerCity - Mobiel assortiment**, ASSORT-02 inmiddels door eigenaar gepubliceerd. Alle1.344MAIN-bestanden ongewijzigd. Concept **195916628234 — BadkamerCity - Offerte vergelijken**, UNPUBLISHED,1.348bestanden. De bestaande ongepubliceerde vorige versie is bijgewerkt met de zes verschillende MAIN-bronpaden, alle broninhoud exact of volledig JSON-semantisch gelijk, en hernoemd. Geen nieuwe volledige themakopie nodig.

Actieve codebranch `fix/product-cards-2026-10-14`; vervolg op105b8b6. Definitief remote codecheckpoint: `99dd1bb4714148423ab2484da6f53b4b113fe7ff`. Main ontvangt uitsluitend documentatie. De reservekopie uit ASSORT-02 is niet gebruikt.

Aangemaakt: ongepubliceerde Shopify-pagina **166573539594**, handle `offerte-vergelijken`, templateSuffix `offerte-vergelijken`, isPublished=false teruggelezen. Geen bestaande pagina gewijzigd. Geen klantbestanden, klanten-/orderrecords, prijzen, catalogus of e-mailberichten gebruikt.

## Gebouwd

- `sections/bc-quote.liquid`, `assets/bc-quote.css`, `templates/page.offerte-vergelijken.json`: uitleg, drie stappen, vergelijking op artikel/uitvoering/aantallen/totaalkosten, drie native FAQ's en contactfallback.
- Eén aanvraag voor volledige offerte of één product; geen automatische prijsaanpassing en geen onbevestigde reactietijd. Laagsteprijsgarantie is inmiddels expliciet door eigenaar goedgekeurd, zie aanvulling hierboven.
- Voorbeeld met naam/e-mail, optionele telefoon/toelichting en PDF/foto. Alle voorbeeldvelden zijn echt uitgeschakeld in een disabled fieldset; er is geen verzendform/action, geen POST, geen upload of verzonnen bevestiging. Alleen preview, geen ontvangstclaim.
- Voorbereide Jotform-iframekoppeling met uitsluitend numeriek formulier-ID, vaste HTTPS-host en afzonderlijke activatieschakelaar. Geen API-key in het thema. Zonder activering geen providerframe of externe formulierrequest. Ongeldig ID valt terug op contact. Een iframe houdt de provider verantwoordelijk voor bestandsoverdracht en servervalidatie; het eigen previewformulier wordt niet stil als providerformulier verzonden.
- Werkelijke toekomstige Jotform-layout moet na accountkoppeling worden afgestemd op het ontwerp. De preview bewijst geen veldmapping, providerlayout, bijlagenverwerking, servervalidatie of afleveren.
- `sections/bc-quote-teaser.liquid` en gedeelde CSS: rustige homepageverwijzing. In `templates/index.json` voorbereid maar **disabled:true**, zodat geen bezoekers naar de ongepubliceerde pagina worden gestuurd. Pas activeren na integratietest en paginapublicatie.
- Additieve NL/EN-localegroep `bc_quote`, alle bestaande vertalingen behouden.

## Review en bewijs

Open het genoemde concept via Shopify en gebruik de bestaande contactpagina met `?view=offerte-vergelijken`. Bezochte previewingang: `https://badkamercity.nl/pages/contact?view=offerte-vergelijken&preview_theme_id=195916628234`. Shopify verwijdert de themeparameter tijdens de sessie. Dit is een alternatieve conceptview: de documenttitel/canonical blijven daar Contact; geen SEO-/indexeerbaarheidsvrijgave voor de definitieve nieuwe pagina.

- [ThemeCheck R2](themecheck.json): zeven productiebestanden PASS. Een docs-manifestverversing gaf eerst een netwerk-timeout; de validator gebruikte de aanwezige Shopify-doccache en valideerde succesvol. Instrumentatie uitgeschakeld via ondersteunde optie.
- [14 LiquidJS/DOM-cases](tests.json), [test](test-quote.cjs): disabled preview, geen netwerkformulier, labels/ID's, ongeldig/ontbrekend/te lang provider-ID, expliciete activatie, veilige vaste host, uitgeschakelde homepageverwijzing en behoud van bestaande locales. Geen remote provideractie.
- [Desktop](desktop.jpg): juiste H1, twee kolommen, geen horizontale overloop, drie FAQ's, nul providerframes, disabled preview. FAQ over goedkoopste prijs geopend en correcte genuanceerde tekst gelezen.
- [Mobiele componentframes](mobile.jpg), [metingen](browser-checks.json):320/390/1024px met effectieve305/375/1009px; geen documentoverloop, één H1, compacte driestappenrij op mobiel, nul providerframes en uitgeschakelde velden. Dit zijn uit Shopify gerenderde componenten; geen native telefoon of volledige mobiele header/footer.
- [Eindverificatie](deployment-verification.json): concept1.348files, exact zeven gewijzigde/nieuwe paden, overige1.341checksums gelijk aan MAIN. Alle zeven productie-inhouden exact tekstueel of JSON-semantisch teruggelezen. MAIN1.344/1.344ongewijzigd. QA-template exact hersteld, MD5 `c76529d094fb4d534f9cd3352c63f4b4`.
- Page-create en readback tonen isPublished=false. Geen live bezoeker kan via de nieuwe normale paginaroute een aanvraag doen.

Geen echte upload, ontvangstmail, klantbevestiging, viruscontrole, bestandstoegang, verwijdering, spam-/rate-limit-, fout-/herstel-, native telefoon-, performance- of publicatietest geclaimd. Die zijn onderdeel van de volgende integratiefase, niet geslaagd op basis van het ontwerp.

## Onderzochte route en bronkeuze

Verse Shopify-read: zeven apps, geen geschikte formulierendienst. De bestaande Glossary Upload-app is een eigen beheerapp; een geïnstalleerde uploadapp is geen bewezen publieke privé-offerteopslag. Geen klantdocument via Shopify Files, product/cart-upload of openbaar Git aangeboden.

Officiële bronnen gelezen30oktober:
- https://help.shopify.com/en/manual/promoting-marketing/create-marketing/forms-app/settings/all-forms — Shopify Forms heeft inmiddels een bestandveld. Een generieke uitspraak dat Forms nooit bestanden ondersteunt is daarom onjuist.
- https://help.shopify.com/en/manual/shopify-admin/productivity-tools/file-uploads — Content > Files is voor openbare bestanden; geen vertrouwelijke offertes daar opslaan.
- https://www.jotform.com/help/673-how-to-unrequire-log-in-to-view-uploaded-files/ — instelling Require Log-in to View Uploaded Files kan downloads afschermen; daadwerkelijk controleren na accountkoppeling, niet uitschakelen.
- https://www.jotform.com/security/ — bestandstoegang kan op ingelogde gebruikers worden beperkt. Een moeilijk te raden URL alleen is geen toegangstest.
- https://www.jotform.com/help/how-to-create-file-upload-forms-without-login/ — bezoekers kunnen zonder eigen account uploaden; ontvangende beheerder behoudt afzonderlijke toegang.

Jotform is de voorbereide praktische route, geen al afgesloten dienst of gekozen abonnement. Geen account aangemaakt, voorwaarden geaccepteerd, app geïnstalleerd, nieuwe externe datatoegang verleend of betaalverplichting aangegaan.

## Concrete aansluitinstructie

1. Bestaand Jotform-account van eigenaar koppelen of eigenaar maakt een account. Geen credentials/API-key in chat/Git. Planlimieten, prijs en opslagregio pas bij de keuze controleren.
2. Formulier aanmaken: vergelijkingstype, naam en e-mail verplicht; telefoon/toelichting optioneel; upload PDF/JPG/PNG. Voorstel maximaal10MB per bestand en geen extra persoonsgegevens vragen. Limieten op provider/server vastleggen; HTML accept is geen beveiliging.
3. Require Log-in to View Uploaded Files aan laten; alleen bevoegde medewerkers toegang. Geen upload in klantbevestigingsmail terugsturen; geen openbare gedeelde tabel of openbare PDF-link.
4. Ontvangstadres en handmatige opvolging met eigenaar vastleggen; de huidige publieke contactlink is info@badkamercity.nl, maar dat is geen geteste notificatieconfiguratie. Klantbevestiging zonder bijlage, geen marketinginschrijving als voorwaarde.
5. Bewaartermijn en verwijderprocedure vastleggen vóór activering; voorstel90dagen na afhandeling van niet-gewonnen aanvragen, nog niet als vastgesteld beleid publiceren. Opdrachten/facturen zijn een afzonderlijk bedrijfsproces.
6. Fictieve kleine PDF/foto testen op mobiel en desktop: opslag, notificatie, klantbevestiging, bevoegde download en anonieme weigering. Ook fout type/grootte, verzendfout, dubbele klik en verwijderen controleren. Geen echte klantofferte gebruiken als test.
7. Numeriek formulier-ID in sectie invullen, provideropmaak afstemmen, preview uit, integratie activeren. Pas na resultaat: pagina en concept door eigenaar publiceren, homepageverwijzing inschakelen en definitieve SEO/canonical/mobile controleren.

**Exact volgende handeling:** eigenaar maakt een formulieraccount beschikbaar; er is nog geen Jotform-account. Daarna werkelijke koppeling en ontvangstproef uitvoeren. Deze sessie kan zonder die accounttoegang geen echte privé-upload of aflevering configureren/verifiëren.

## Rollback

Nieuwe homepageverwijzing disabled houden, uploadkoppeling uit, pagina ongepubliceerd laten. Bestaande locale- en indexbronnen staan in baseline. Nieuwe ongebruikte bestanden hoeven niet verwijderd te worden. Publiceer deze hele conceptversie pas na integratievrijgave; geen volledige Git-root uploaden. Het onafgemaakte ontvangstdeel blijft expliciet open.
