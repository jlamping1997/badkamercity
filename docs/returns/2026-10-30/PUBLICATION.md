# RET-03 — retourknop zichtbaar op de live winkel

30 oktober 2026, 17:44 CET. De eigenaar heeft RET-02 zelf gepubliceerd en meldt met screenshots dat de retourknop op de live desktop ontbreekt. Dit is een herstel binnen de eerder gevraagde publieke retourpagina en headeringang.

## Oorzaak en kleinste herstel

Verse Admin-read bevestigt MAIN **195948839178 — BadkamerCity - Retourknop in header**, gepubliceerd door de eigenaar op 16:41:30Z. De eerdere previewcode is aanwezig: header MD5 `78a34a0d90ff1df449f3f6ac05db476d`, URL-helper `000ab5cee978aaf63059307902dc4cc3`, retoursection `1746659cd84502875b24f4fe311f80c9`, paginatemplate `2e5141a5c097bfb87ccc21e92fa51d66`.

Page **166668894474**, `/pages/retour-aanmelden`, was nog `isPublished=false`. De gedeelde URL-helper geeft voor een verborgen Page in MAIN bewust geen link terug; daardoor verdween de knop na themapublicatie. De eerdere previewcontrole sloot deze samengestelde publicatiestand niet. De eigenaar had het juiste thema gekozen; opnieuw een thema maken of uploaden zou dit niet oplossen.

Alleen de zichtbaarheid van de bestaande Page naar `isPublished=true` gezet via pageUpdate. Onafhankelijke read-after-write bevestigt de juiste handle, ongewijzigde templatesuffix en publicatietijd **2026-10-30T16:44:26Z / 17:44:26 CET**. Geen themabestand geschreven, geen thema omgewisseld of gepubliceerd, geen inhoud/voorwaarden aangepast. [Admin-bewijs](page-publication-admin.json), [schemavalidatie](page-publish-validation.json).

## Publieke controle

- Browser expliciet uit Shopify-voorbeeldmodus gehaald via Exit preview. Live homepage toont Retour aanmelden direct links van Verlanglijst, met echte href `/pages/retour-aanmelden`; de offertepreview wordt niet op de live header getoond.
- De live knop echt aangeklikt: URL `https://badkamercity.nl/pages/retour-aanmelden`, titel Retour aanmelden – Badkamercity, juiste H1 en native retourformulier POST `/contact`. Viewport1348px, scrollWidth1348px.
- Twee aanvullende HTTP-GETs zonder cookies/previewparameters: homepage en echte retour-URL beide200, Shopify.theme.id195948839178/rolemain, headerlink naar dezelfde echte Page. Canonical van de retourpagina exact de echte URL; geen robots-noindex aangetroffen. [Publieke HTTP-check](live-publication-check.json), [live beeld](return-live.jpg).
- Eerder desktop/mobielbronwerk niet opnieuw gewijzigd. Geen nieuwe resize-, fysieke telefoon-, checkout-, order-, refund- of labeltest. Geen formulierinzending gedaan; mailboxbezorging blijft NOT_TESTED. De zichtbaarheid en het formulier bereiken zijn bewezen, e-mailontvangst niet.

## Beheer en herstel

De retouringang is nu live. De volgende functionele controle is één herkenbare testaanvraag door de eigenaar en ontvangstcontrole op info@badkamercity.nl inclusief spam; de winkel behandelt aanvragen per e-mail en stuurt instructies/een eventueel label handmatig.

Bij een expliciet terugzetverzoek kan alleen deze Page weer worden verborgen. Dat verwijdert volgens de bestaande guard ook de nieuwe live headerlink; daarom Page- en thema-publicatie altijd samen controleren. Oude concepten niet over deze samengestelde live stand publiceren zonder vergelijking. Geen Windows-controle; GitHub/Shopify-connectors en cloudbrowser gebruikt.
