# RET-01 — retouraanmelding en footeradres

> **Latere status:** de eigenaar heeft dit thema inmiddels gepubliceerd. De verse bron en nieuwe desktopheaderknop staan in [RET-02](HEADER.md). De onderstaande opleverstand blijft historisch.

30 oktober 2026. Expliciete eigenaaropdracht: Zichtenburglaan150 uit de footer verwijderen; een klant kan een retour aanmelden met producten/reden, zodat de winkel de aanvraag beoordeelt en eventueel een label toestuurt. Uitvoerder Codex via connector/werkboom; bestaande branch `fix/product-cards-2026-10-14`, geen Windows-controle.

## Verse bron en grenzen

De eigenaar heeft HDR-01 bekeken en goedgekeurd. Verse Shopify-read bevestigt **MAIN195932061962 — BadkamerCity - Vaste mobiele header**,1351bestanden; vorigeMAIN195915448586 is UNPUBLISHED. Headerwerk is dus inmiddels daadwerkelijk door de eigenaar gepubliceerd. Geen themePublish door deze uitvoering.

Nieuw concept **195947036938 — BadkamerCity - Retour aanmelden en footer**, gedupliceerd van de huidige MAIN. Voor de eerste runtimewrite volledige1351/1351kopiepariteit bewezen. Offerteconcept195916628234 blijft afzonderlijk en wordt niet overschreven. Acht runtimefiles; geen product-, prijs-, order-, refund-, voorraad-, vervoerder-, DNS- of notificatie-instellingenmutaties.

Page **166668894474**, handle`retour-aanmelden`, template`retour-aanmelden`, **isPublished=false**. Geen bestaande retourpagina aangetroffen in de volledig ontvangen120Page-records vóór creatie. Preview via bestaande gepubliceerde `/pages/contact?view=retour-aanmelden`; de Page blijft verborgen tot eigenaarreview. Publicatie van de Page is geen themefilewrite en moet bij vrijgave bewust met het concept worden afgestemd.

## Besluit over verwerking

De bestaande Jotform-integratie voor offertes is onderzocht als hergebruikmogelijkheid. Pluginzoeker gaf geen Jotform-plugin. De browser-auto-review **weigerde** het openen van `www.jotform.com/myforms`: deze opdracht autoriseerde geen toegang tot privé-Jotform-accountinhoud. Geen andere URL, login, API, account, key of omweg naar dat account gebruikt. Er is geen nieuw Jotform-formulier gemaakt en geen privé-inzending gelezen.

Materieel veiliger alternatief: de expliciet gevraagde retourpagina gebruikt de bestaande **Shopify Liquid contact-mailer**, zonder ander account. De aanvraag wordt als contactmail behandeld, met een vaste onderwerpregel in de berichtvelden: `Retouraanvraag Badkamercity`. Shopify’s formele mailsubject zelf wordt niet via een verzonnen recipient/subject-API overschreven. Admin-shop.email en contactEmail zijn vers gelijk aan info@badkamercity.nl. Volgens Shopify worden contactinzendingen bij het afzender-e-mailadres bezorgd; echte mailboxontvangst blijft een eigen test, niet afleiden uit alleen deze waarden.

Dit is een aanmelding en handmatige afhandeling per e-mail. Er wordt geen Shopify Return/RMA aangemaakt, geen order opgezocht namens een anonieme bezoeker, geen label gekocht/aangemaakt en geen terugbetaling verwerkt. Het formulier voegt geen nieuwe automatische klantbevestigingsmail toe. De medewerker bevestigt ontvangst en de vervolgstap zelf per e-mail. De medewerker kan informatie vragen, een oplossing/omruiling bespreken, verzendinstructies en een bestaand label per e-mail sturen. Carrierkeuze/kosten worden niet verzonnen of automatisch toegepast.

## Formuliercontract

| Veld | Contract |
| --- | --- |
| Naam | Verplicht, contact[name], max100tekens, autocomplete name |
| E-mail | Verplicht, contact[email], native emailvalidatie, max254 |
| Bestelnummer | Optioneel, contact[Bestelnummer], max80; ontbrekend nummer verhindert geen melding |
| Verzoek | Verplicht: retourneren/herroepen, omruilen of probleem |
| Producten/aantallen | Verplicht, contact[body], max2500; gewone tekst per product |
| Retourreden | Optioneel; standaard Geen reden opgeven, verder verkeerd besteld/past niet/schade/verkeerd of onvolledig/defect/anders |
| Toelichting | Optioneel, max3000 |
| Onderwerp | Vaste hidden contact[Onderwerp] voor herkenning in merchantmail |

Geen marketing, verplichte accountaanmaak, bewijsfoto of akkoordcheckbox als voorwaarde voor herroeping. Bij schade kunnen foto’s naderhand per e-mail worden gevraagd; geen niet-werkend file-input. Naam/e-mail/productinformatie dienen identificatie, geen automatische orderverificatie. Geen klantgegevens in URL, analytics, browseropslag of openbare database. De form-tag behoudt Shopify’s eigen endpoint, UTF-8/form_type, spam- en CAPTCHA-koppeling; geen eigen fetch/send-endpoint. `return_to: 'back'` houdt de klant bij de gebruikte pagina/preview.

Bij server-succes vervangen een ontvangstmelding en contactroute de invoervelden; geen ongeteste automatische klantmailclaim. Bij serverfout blijven de velden en Shopify’s fouten zichtbaar. De pagina maakt helder dat instructies/een eventueel label apart volgen. De retourreden is optioneel conform ACM; een retouraanmelding is geen vrijbrief om geldige herroeping van toestemming afhankelijk te maken. Bestaande wettelijke rechten en contact per e-mail blijven vermeld. De pagina is geen volledige herziening van de winkelvoorwaarden of automatische garantie-/herroepingsbeslisser.

## Vormgeving en gedeelde footer

Rustige lichtgrijze achtergrond, donkerblauwe kop/knop, witte formulierkaart en drie beknopte stappen. Desktop formulier links en de drie stappen rechts; mobiel één kolom. De DOM-volgorde heeft het formulier op beide formaten eerst, zonder CSS-order die de toetsenbordvolgorde laat afwijken. Velden16px/46pxhoog, knop50px, native select/details en zichtbare focus. Geen nieuwe JS-library, JS-controller, iframe, animatielibrary of externe afbeelding. Alle nieuwe klantteksten in `bc_returns` in NL en EN; bestaande localegegevens inhoudelijk behouden.

`sections/footer-group.json` verwijdert uitsluitend het adres en wijzigt het bestaande Retourneren-block in Retour aanmelden met de nieuwe bestemming. De compacte footer rendert zijn adresblok inclusief kop alleen bij een gevuld adres. De grote footer had die guard al.

`snippets/bc-returns-url.liquid` is de gezamenlijke URL-regel: gepubliceerde Page→echteURL; ontbrekende Page in unpublished→contact-viewpreview; ontbrekende Page inMAIN→geen nieuwe dode link. De grote footer behoudt dan een tekstlabel, de compacte footer zijn oorspronkelijke HomeReturns-anker. Zodra de eigenaar de Page publiceert verwijzen beide footers naar dezelfde nieuwe pagina. Header/stickygedrag blijven behouden.

## Verificatie

- Theme Check revision3: alle8files SUCCESS in geïsoleerde actuele runtimeboom. De bestaande lokale Shopify-doccache wordt gebruikt als online refresh timeout geeft.
- 22 render-/contractcases PASS: required/optioneel, lege/ongeldige/volledige invoer, geen reden/bestelnummer nodig, unieke veldnamen/labels/IDs, requestsoorten, escaping, server-succes/-fout, NL/EN, native FAQ, geen bijlage/account/marketing, vier URL-publicatierollen, lege-adresguard, exacte configpatch en additive locales.
- De LiquidJS-formtag in de test is een renderfixture; geen echte Shopify-email of servervalidatieclaim. De eerste URL-test gebruikte per ongeluk render-isolatie zonder Shopify-globalen; gecorrigeerd door de echte snippet met zijn expliciete globale context te renderen. Geen productiecode veranderd voor die testfixture.
- Echte Shopify-preview op1348px: formulier, optionele reden/ordernummer, endpointPOST/contact, requiredvelden, h1 en footer bekeken. Lege-submit stopt client-side bij Naam; er is geen succesvolle aanvraag ingestuurd. Shopify’s eigen CAPTCHA-assets worden geladen; geen CAPTCHA opgelost of omzeild.
+- Homepagefooter Klantenservice geopend en Retour aanmelden aangeklikt → echte retourpreview. De huidige homepage-, categorie- en retourresponses bevatten geen adres meer in de footer. Beide renderers verwijzen naar dezelfde previewroute; na publicatie van de Page naar de echte Page. URL-captures expliciet gestript nadat servermarkup een onnodige voorloopnewline bevatte; finaleGET bevestigt schonehrefs.
+- Componentbrowserframes320/390/880/1024: scrollWidth=clientWidth,16pxvelden,49–50pxhogeinputs/selects en51pxknop. Formulier staat in DOM én mobiel visueel vóór de stappen. Geen fysieke telefoonclaim. De fixture gebruikt echte Shopify-markup/styles van de retourpagina; header en globale koopinteracties vallen buiten deze componentproef.
+- Finale bron: MAIN195932061962 nogMAIN en1351/1351ongewijzigd. Concept195947036938UNPUBLISHED,1354files: exact vijf bestaandefiles gewijzigd en drie nieuwe, geen ontbrekende. Zeven featurebodies exact teruggelezen; de nieuweJSON-template is semantisch exact en heeft de checksum van de ingezonden122bytes, maar Shopify voegt in zijn body-read een automatisch commentaarblok toe. Die body-normalisatie is geen runtimeverschil of niet-onderzochte featurewijziging.
+- Tijdelijke bestaande `templates/page.bc-mobile-qa.liquid` exact hersteld naar MD5 `24ae4cff55afe7f2453e4e9b6a0c2479`. Page166668894474 onafhankelijk teruggelezen als verborgen met juistehandle/template. Geen liveTheme-/Page-publicatie.
+- [Browsermetingen](browser-measurements.json), [eindverificatie](final-verification.json), [HTTP-footercontrole](final-footer-http.json) en [beeld](returns-mobile-desktop-proof.jpg).
- Echte aanvraag/mailboxontvangst, eventuele spammap, klantantwoord en echte labellevering: niet stil als PASS registreren. Fysieke iPhone, refund en retourlabelaankoop niet getest/uitgevoerd.

## Concrete volgende handeling
+
+Eigenaar doet één duidelijk herkenbare testaanvraag in het concept, controleert ontvangst op info@badkamercity.nl en de spammap en antwoordt daarop. Daarna de echte telefoonweergave beoordelen en de nieuwe Page plus dit concept bewust publiceren. Zolang die ontvangsttest niet is uitgevoerd blijft status MAIL_DELIVERY_PENDING. Een bevestigingspagina bewijst geen mailboxbezorging. Geen nieuwe klantactieve route beloven voor deze vrijgave.
+
+## Behandelen en terugzetten

Controleer nieuwe contactmail op `Retouraanvraag Badkamercity`. Zoek zelf de bestelling erbij en verifieer identiteit/producten. Behandel in de inbox als Nieuw → In behandeling → Instructies verstuurd → Afgehandeld. Dit zijn aanbevolen handmatige werkstaten; geen automatisch aangemaakte mailboxlabels of dashboard. Reageer vanuit de bestaande winkelmail en voeg alleen het label/transport toe dat bij die concrete aanvraag past. Beoordeel ontvangen producten en eventuele terugbetaling apart in de bestaande orderworkflow.

Tot publicatie blijft MAIN195932061962 terugval. Baselines voor alle gewijzigde bestaandefiles staan in `baseline/`. Bij terugzetten alleen die vijf bestaande paden herstellen; nieuwe section/template/snippet mogen daarna ongebruikt blijven. De nieuwe Page is verborgen en kan zo blijven; geen verwijdering nodig. Publiceer geen oudere offertepreview zonder het gepubliceerde headerwerk en deze retourwijzigingen opnieuw samen te brengen.

## Bronnen

- https://shopify.dev/docs/storefronts/themes/customer-engagement/add-contact-form
- https://shopify.dev/docs/api/liquid/tags/form
- https://help.shopify.com/nl/manual/intro-to-shopify/initial-setup/setup-your-email
- https://consument.acm.nl/aankoop-dienst-annuleren/bedenktijd
- Native selfservice-retouren zijn als alternatief onderzocht, niet geactiveerd: https://help.shopify.com/nl/manual/fulfillment/managing-orders/returns/self-serve-returns
