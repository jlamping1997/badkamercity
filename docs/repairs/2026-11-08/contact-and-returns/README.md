# CONTACT-RETURNS-01 — contact aangevuld en retourinformatie gelijkgetrokken

> **Opgevolgd door DELIVERY-INFO-01:** dit dossier bewaart het oorspronkelijke vier-file retourcheckpoint. Hetzelfde concept 196368531722 heet nu **Klantenservice 8 nov** en heeft twee bezorglinkfiles erbij; de vier hieronder beschreven retourfiles zijn checksumgelijk behouden. Nieuwe bezorg-Page en Contact-link zijn live. [Laatste status, zes-file eindmanifest en herstel](../delivery-information/README.md). Nog geen themapublicatie.

**8 november 2026. Footer: OWNER_PUBLISHED / LIVE_HTML_VERIFIED. Contact en RapoWash: APPLIED_VERIFIED. Retourinformatie: PREVIEW_VERIFIED / NOT_PUBLISHED.** De eigenaar heeft het vorige footerconcept gepubliceerd. Daarna zijn de volgende concrete punten onderzocht en hersteld.

## Wat nu live staat

| Onderdeel | Resultaat | Bewijs |
| --- | --- | --- |
| Gedeelde footer | MAIN 196354474250 — Eenduidige footer 8 nov; beide featurefiles exact; dezelfde footer met telefoon/e-mail/gelabeld adres op 14 publieke routes zonder preview | [Live footercontrole](live-footer.json) |
| Contact | Bestaande lege Page-body aangevuld met bevestigde contactgegevens, contact-/retouradres, afspraaktekst en retour-/beleidslinks; native formulier behouden | [Publieke readback](live-pages.json) |
| Contact SEO | Eigen titel Contact en klantenservice en beschrijving toegevoegd via twee global-metafields met compareDigest=null | [Publieke readback](live-pages.json) |
| RapoWash | Vier kapotte tekstplaatsen gecorrigeerd: hygiëne tweemaal, geïntegreerde en één | [Publieke readback](live-pages.json) |

Contact heeft één H1 en dezelfde handle, publicatiestatus en template. Telefoonlink is tel:+31685887536; zichtbaar 06 85887536. E-mail info@badkamercity.nl. Alleen het bevestigde contact-/retouradres is toegevoegd: Badkamercity – bij Harry Suiker, Zichtenburglaan 150, 2544 EB Den Haag, Nederland. Afgeven uitsluitend op afspraak. Geen openingstijden, juridische vestiging, bankrekening of onvolledig btw-id toegevoegd. RapoWash behoudt zijn eerder herstelde SEO en alle inhoud buiten de vier gerichte tekenreparaties.

## Volgend concept: retourpagina en homepage

**UNPUBLISHED 196368531722 — BadkamerCity - Retourinformatie 8 nov.** [Bekijk het concept](https://badkamercity.nl/pages/retour-aanmelden?preview_theme_id=196368531722).

De retourpagina gebruikt bc-returns.liquid en vertaalteksten; de bestaande Page-body wordt daar niet gerenderd. Een wijziging aan alleen die body zou de zichtbare fout dus niet oplossen. De Page-body is behouden.

De bestaande reservekopie is eerst met twee footerfiles bijgewerkt naar de actuele MAIN. Volledige manifests plus exacte readback bewijzen daarna 1.387/1.387 pariteit. Vervolgens zijn alleen vier bestanden gewijzigd:

| Bestand | Gerichte wijziging |
| --- | --- |
| sections/bc-returns.liquid | Bestaande intro krijgt een link naar de echte shop.refund_policy; formulieractie, velden, required-attributen en CSS blijven behouden |
| locales/nl.json | Acht bestaande retourteksten gelijk aan het gepubliceerde beleid: 30 dagen melden, daarna 14 dagen terugsturen; vaste retourlocatie; zelfbetaalde gewone retour en kosteloze passende oplossing bij fout/ondeugdelijk; €75 incl. btw als standaard NL-palletraming |
| locales/en.default.json | Dezelfde acht bestaande sleutels in het Engels; geen nieuwe sleutels of commerciële afspraken |
| templates/index.json | Alleen bc_homepage.settings.returns_text: dezelfde termijnen en bestelnummer expliciet indien bekend |

De keuze Ik wil omruilen is zichtbaar vervangen door **Andere uitvoering (retour + nieuwe bestelling)**, passend bij de bestaande policy die geen directe omruilservice belooft. Het formulier blijft een melding; geen automatische terugbetaling, label of bestelactie toegevoegd. De €75 is een raming voor een standaard retourpallet binnen Nederland, geen heenzendtarief of universele transportprijs.

## Controle en grenzen

- Alle vier daadwerkelijke featurefiles slagen voor de Liquid-toolkit op revisie 2 en zijn exact teruggelezen uit Shopify.
- Volledige finale manifestcontrole: 1.387 bestanden per thema, 1.383 gelijk, precies vier bedoelde verschillen, nul ontbrekend/extra; MAIN-bestanden ongewijzigd.
- [Drie previewroutes](returns-preview.json): homepage, retourpagina en Contact tonen de juiste concept-ID en behouden de gedeelde footer. De beleidslink, termijnen, adres, raming en aangepaste keuze zijn zichtbaar. Bestelnummer en retourreden blijven optioneel; native POST-contactformulier blijft aanwezig.
- [Patchregister](patch-summary.json), [volledig checksumregister](theme-parity.json), [Liquid-validatie](liquid-validation.json), [verificatiegrenzen](verification.json) en [gerichte herstelwaarden](rollback-pages.json).

Geen formulier verstuurd, nieuwe desktop-/mobiele browserbediening, betaling, ordermail of aankoopmeting getest. De oudere footerdesktopproef behoudt zijn eigen meetmoment. De online herroepingsfunctie met onmiddellijke bewaarbare bevestiging blijft afzonderlijk open; copyverbetering bewijst die functie niet.

## Wat open blijft

Native voorwaarden/kennisgeving tonen nog letterlijke HTML; de eerder vastgestelde write_legal_policies-scope ontbreekt. Die actie is in deze ronde niet opnieuw geprobeerd. Het native contactbeleid blijft apart te actualiseren; de gewone Contactpagina en footer zijn wel bijgewerkt. Verzendbeleid, geverifieerd btw-id/juridische identiteit en de echte betaal-/mail-/meetketen blijven open.

**Volgende handeling:** eigenaar beoordeelt het bestaande concept Retourinformatie 8 nov op laptop en telefoon en publiceert via Shopify bij akkoord. De uitvoerder heeft niet gepubliceerd. Daarna actuele MAIN, de zichtbare retourteksten en native formulierbediening opnieuw controleren. De aparte Cotto-/filter- en importwerkstromen behouden hun eigen status.

## Herstel en onderhoud

Code staat op de bestaande branch fix/product-cards-2026-10-14 onder shopify/current. Main bevat alleen documentatie. Voor het concept kunnen de vier files worden teruggenomen uit verse MAIN, nadat tussentijdse wijzigingen zijn gecontroleerd. Page-herstel blijft beperkt tot de bedoelde bodies/twee nieuwe SEO-waarden. Geen volledige themapush vanuit de Git-bronkopie: de overige eerder geregistreerde Git/live-verschillen zijn niet in deze ronde opgelost.
