# Taken — livegang, Google en SEO

**Stand: 8 november 2026 — CONTACT-RETURNS-01; eerdere DOC-LIVE-01/FOOTER-FIX-01 blijven gedateerde checkpoints.** Deze matrix vervangt de actuele statusclaims van LAUNCH-01/02/03; het [logboek](LOGBOEK.md) en oude bewijsbestanden behouden hun meetmoment. [Diepe audit en bevindingen](../audits/2026-11-08/README.md). Jackson beslist over bedrijfsgegevens, accounts en echte bedrijfsafhandeling; uitvoering levert controleerbare technische wijzigingen/bewijzen.

Status: DONE = binnen benoemde scope bewezen; OPEN = nog uitvoeren; PARTIAL = deel bewezen; IN_PROGRESS_USER = eigenaar werkt eraan; TO_VERIFY = actuele werking of vereiste nog gericht toetsen; LATER = na de basis. P0 = voor betrouwbare verkoop/promotie; P1 = voor het betreffende Google-/SEO-spoor; P2 = verdere groei. Een blokkade voor één product houdt de rest niet automatisch tegen.

## Winkelbasis

| ID | Prio | Taak | Status | Acceptatie / wat resteert | Eigenaarrol |
| --- | --- | --- | --- | --- | --- |
| BC-LIVE-000 | P0 | Openbaarheid, HTTPS, robots en sitemap lezen | DONE | Gedateerde nulmeting + 8-novemberaudit; geen verklaring dat alle interactieve routes werken | Uitvoering |
| BC-LIVE-001 | P0 | Bedrijfsidentiteit en contact afronden | PARTIAL | Contactpagina en gedeelde footer bevatten nu bevestigde telefoon/mail/contact-/retourlocatie, publiek teruggelezen. Btw-id, juridische naam/vestiging en native Contact policy blijven apart te controleren | Jackson + uitvoering |
| BC-LIVE-001A | P0 | Contact-/retouradres en juridische vestiging onderscheiden | PARTIAL | Openbare contact-/retourlocatie Zichtenburglaan 150 bevestigd; geregistreerde KvK-vestiging NOT_VERIFIED, niet afleiden of privé-adres herpubliceren | Jackson |
| BC-LIVE-002 | P0 | Contact, verzending, retourbeleid en voorwaarden publiceren | PARTIAL | Contactpagina en footer zijn live aangevuld. Vijf native policies bestaan; voorwaarden/kennisgeving blijven BLOCKED_SCOPE en verzending ontbreekt. Een Page-correctie wijzigt geen native policy | Jackson + uitvoering |
| BC-LIVE-003 | P0 | Bestelproces doorlopen | PARTIAL | Zoek/filter/cart en gastcheckout desktop bewezen in beperkte proef; [verzending, betaalmiddelen, betaling, ordermail en mobiel](CONTROLES.md) nog toetsen | Jackson + uitvoering |
| BC-LIVE-004 | P0 | Leverbaarheid en levertijden afmaken | IN_PROGRESS_USER | Onderbouwde bron per merk/product; FAB-04 en gerichte latere bewijzen hergebruiken, geen algemene voorraad-/levertijdclaim | Jackson + uitvoering |
| BC-LIVE-005 | P0 | Contact- en retourberichten ontvangen en beantwoorden | PARTIAL | Formulieren aanwezig; [mailproef](CONTROLES.md) nog uitvoeren: succes, ontvangst/spam, juiste velden, reply-to en antwoord | Jackson + uitvoering |
| BC-LIVE-006 | P1 | Producten klaarzetten voor Google | OPEN | [Batchcontrole](GOOGLE_PRODUCTCONTROLE.md), circa tien uiteenlopende items en Merchant-readback; ACTIVE is geen feedvrijgave | Uitvoering |
| BC-LIVE-007 | P1 | Verlavio-beelden en Google-geschiktheid controleren | PARTIAL | Rebrand/gericht koopbaarheidsherstel FAB-03/04 behouden; juiste beelden, identifiers en huidige Google-bestemming per batch | Jackson + uitvoering |
| BC-LIVE-008 | P1 | Productfoto's en foute beeldweergave nalopen | IN_PROGRESS_USER | Echte requests/zichtbaarheid per relevante renderer; Lagoo-fotoverbod behouden | Jackson + uitvoering |
| BC-LIVE-009 | P1 | Eén standaardfooter winkelbreed gebruiken | DONE | FOOTER-FIX-01 door eigenaar gepubliceerd: MAIN 196354474250, twee MD5’s exact en 14 publieke routes zonder preview met dezelfde footer/contactgegevens. DONE betreft bron-/HTML-publicatie; geen nieuwe mobiele of koopflowclaim | Uitvoering + Jackson |
| BC-LIVE-010 | P0 | Dertig-dagenretourpolicy op website | DONE | Live policy volledig gelezen: 30 dagen aanmelden + 14 terugsturen, €75 incl. btw standaard NL-palletraming, afgeven op afspraak, fout/defect apart; Google gelijkzetten blijft BC-GOOGLE-004 | Jackson + uitvoering |
| BC-LIVE-011 | P0 | Online herroepingsfunctie en directe klantbevestiging | OPEN | Native POST-formulier alleen is onvoldoende bewijs; toegankelijke functie, definitieve stap en onmiddellijke bewaarbare bevestiging met aankoop/datum/tijd testen | Uitvoering + Jackson |
| BC-LIVE-012 | P0 | Modelformulier herroeping beschikbaar | DONE | Volledig formulier met lege velden staat leesbaar in live retourpolicy; gebruik niet verplicht. Geen afzonderlijke PDF als extra eis; dit sluit BC-LIVE-011 niet | Uitvoering |
| BC-LIVE-013 | P0 | HTML-opmaak voorwaarden en kennisgeving herstellen | OPEN | BC-AUD-001/002 blijven open: geen policywrite, `shopPolicyUpdate` mist `write_legal_policies`. Via bevoegde policybewerking correcte HTML opslaan en publiek teruglezen | Uitvoering + Jackson |
| BC-LIVE-014 | P0 | Verzendbeleid en echte tarieven vastleggen | OPEN | BC-AUD-003/010: werkelijke pakket-/pallet-/regioregels, levering en eventuele afhaalafspraak; één locatie zonder rates onderzoeken; €75 retour is geen heenprijs | Jackson + uitvoering |
| BC-LIVE-015 | P0 | Actuele garantie-informatieplicht toetsen | TO_VERIFY | [ACM/EU-bronnen, opnieuw geraadpleegd 8 november](BRONNEN.md): toepasselijk EU-garantiebericht zichtbaar aanbieden, order-/winkelinformatie toetsen; geen uniforme Nederlandse wettelijke termijn van twee jaar claimen | Jackson + uitvoering |
| BC-LIVE-016 | P0 | Productveiligheidsinformatie bij online aanbod toetsen | TO_VERIFY | [NVWA/GPSR](BRONNEN.md): gerichte producttype-/batchcontrole op fabrikantcontact, eventuele EU-verantwoordelijke, identificatie en toepasselijke veiligheidsinformatie; ontbrekende productdata opvragen, geen catalogusbrede overtredingsclaim | Jackson + uitvoering |
| BC-LIVE-017 | P2 | Gerichte content-/navigatieafwijkingen herstellen | PARTIAL | Antikalk-H1 en RapoWash-metadata waren live opgelost; nu ook vier RapoWash-tekencoderingen gericht hersteld. Retour-FAQ/homepagecopy is geïmplementeerd in volgend UNPUBLISHED concept, nog niet gepubliceerd; zie BC-LIVE-020 | Uitvoering |
| BC-LIVE-018 | P1 | Contactpagina met bereikbare gegevens en eigen SEO | DONE | Page 160794411274 live aangevuld; telefoon/mail/adres op afspraak en retour-/policy-links publiek gelezen. Native formulier behouden; native Contact policy en mailontvangst apart | Uitvoering |
| BC-LIVE-019 | P2 | RapoWash-tekencodering herstellen | DONE | Vier concrete mojibakeplaatsen in Page-body gericht hersteld; correcte SEO, identiteit en status behouden; publieke readback PASS | Uitvoering |
| BC-LIVE-020 | P1 | Retourinformatie op aanmeldpagina en homepage gelijkzetten | PARTIAL | PREVIEW_IMPLEMENTED_NOT_PUBLISHED in 196368531722 — Retourinformatie 8 nov, na 1.387/1.387 pariteit precies vier bestanden. 30+14, beleidslink, adres/kosten en retour + nieuwe bestelling; 4/4 Liquid-checks revisie 2/readback. Publieke previewcontrole, review en publicatie nog afronden | Uitvoering + Jackson |


## Google en meten

| ID | Prio | Taak | Status | Acceptatie / wat resteert | Eigenaarrol |
| --- | --- | --- | --- | --- | --- |
| BC-GOOGLE-001 | P1 | Google-toegang en eigendom vastleggen | TO_VERIFY | Bestaand Merchant-ID 5898992928 is historische eigenaarsopgave; huidige toegang/rol via info@ teruglezen, geen dubbel account | Jackson |
| BC-GOOGLE-002 | P1 | Google & YouTube verbinden | PARTIAL | Integratie en meetconfig aanwezig; huidige accountselectie, Merchant-koppeling, domeinclaim en productbronnen nog onafhankelijk teruglezen | Jackson + uitvoering |
| BC-GOOGLE-003 | P1 | Search Console-eigendom en sitemap | DONE | Eigenaarsbeelden 8 november: DNS-property, sitemap verwerkt, homepage geïndexeerd/live; Wastafelkranen indexering aangevraagd. Geen algemene opname-/rankingclaim | Jackson + uitvoering |
| BC-GOOGLE-004 | P1 | Google-verzending en retouren gelijkzetten | OPEN | NL/EUR, 30 dagen, methoden/kosten en verwerking naast live policy/checkout teruglezen; niet €75 als universeel heen- of retourtarief invullen | Jackson + uitvoering |
| BC-GOOGLE-005 | P1 | Kleine productfeedproef | OPEN | Circa tien uiteenlopende varianten in Merchant teruglezen op koopbare prijs, foto, identifiers, voorraad en bestemmingen; tegeldoos en eenheidsprijs scheiden | Uitvoering |
| BC-GOOGLE-006 | P1 | Gratis vermeldingen uitbreiden | OPEN | Geschikt/beperkt/afgekeurd per batch registreren; beeldloos Lagoo apart voor Google-productbestemming behandelen | Uitvoering |
| BC-GOOGLE-007 | P1 | GA4 en toestemming aansluiten | PARTIAL | G-H9YFB5TC6N in live appconfig, Realtime USER_REPORTED; browserkeuzes bedienbaar, technisch consent-/taggedrag en één meetroute nog bewijzen | Jackson + uitvoering |
| BC-GOOGLE-008 | P1 | Koopgebeurtenissen en omzet valideren | OPEN | view_item/add_to_cart/begin_checkout/purchase met juiste variant, value/currency en één transaction_id; geen persoonsgegevens | Uitvoering |
| BC-GOOGLE-009 | P1 | Indexatie en feedkwaliteit bewaken | OPEN | Eerste gedateerd rapport uit echte accounts: indexatie, geschikte/afgekeurde items en oorzaken | Uitvoering |
| BC-GOOGLE-010 | P2 | Google Bedrijfsprofiel beoordelen | LATER | Alleen als Badkamercity zelf aan voorwaarden voor persoonlijk klantcontact voldoet; geen Harry Suiker-profiel hergebruiken | Jackson |
| BC-GOOGLE-011 | P1 | Ads-account en campagne-inrichting controleren | IN_PROGRESS_USER | Eigenaar heeft account-/campagneonboarding gestart; werkelijk account, budget, bestemmingen, marges en conversiemeting controleren. Geen campagne automatisch starten | Jackson |

## SEO en structurele groei

| ID | Prio | Taak | Status | Acceptatie / wat resteert | Eigenaarrol |
| --- | --- | --- | --- | --- | --- |
| BC-SEO-001 | P1 | Homepagezoekvermelding verbeteren | DONE | De eerder gepubliceerde homepage-SEO blijft behouden op huidige MAIN 196354474250; geen ranking-/mobiele vrijgave | Uitvoering + Jackson |
| BC-SEO-002 | P1 | Technische SEO-steekproef uitbreiden | PARTIAL | 364 serverresponses, H1/metadata/canonical/schema gecontroleerd; gerichte afwijkingen geregistreerd; rich results, JavaScript/paginering en echte indexatie apart | Uitvoering |
| BC-SEO-003 | P1 | Mobiele kernroutes en snelheid meten | TO_VERIFY | Echte telefoonbediening en benoemde PageSpeed-/veldmetingen; desktop-HTML is geen mobiele test | Jackson + uitvoering |
| BC-SEO-004 | P1 | Eerste categoriecluster kiezen | OPEN | Assortiment, koopintentie en overlap gecontroleerd; keuze en meetpunt in paginaregister | Jackson + uitvoering |
| BC-SEO-005 | P2 | Bestaande categorieën verbeteren | OPEN | Nuttige keuzehulp, unieke metadata, interne links en passende producten; eerst gekozen cluster | Uitvoering |
| BC-SEO-006 | P2 | Merk-/seriepagina's onderzoeken | OPEN | Bestaande vendor-/Sunshower-routes onderzoeken, één scope per klantvraag; geen automatische kruistabelpagina's | Uitvoering |
| BC-SEO-007 | P2 | Advies en begrippen onderhouden | PARTIAL | Alle 119 gepubliceerde Pages in HTTP-/metadata-audit; inhoudelijke beoordeling per onderwerp blijft open, RapoWash/Antikalk gericht herstellen | Uitvoering |
| BC-SEO-008 | P2 | Imports standaard controleren | OPEN | Categorie, identifiers, media, eenheidsprijs, levering, veiligheidsinformatie en Google-status in bestaande importcontrole | Uitvoering |
| BC-DOC-001 | P1 | Vast livegang-/Google-/SEO-dossier | DONE | LAUNCH-01-structuur en gedateerde nulmeting behouden | Uitvoering |
| BC-DOC-002 | P1 | Eigenaarsaanvulling en vervolgstappen | DONE | LAUNCH-02/03 blijven historische documentatie, geen huidige publicatieclaim | Uitvoering |
| BC-DOC-003 | P1 | Actuele docs reconciliëren met live | DONE | CONTACT-RETURNS-01: eigenaarspublicatie footer, Contact/tekencodering live en volgend retourconcept onderscheiden; remote opslag wordt afzonderlijk door root gecontroleerd | Uitvoering |

## Volgende handeling en andere werkstromen

Binnen dit consistentiedossier: de gedeelde footer **196354474250** is door de eigenaar gepubliceerd en publiek nagecontroleerd; die publicatieactie niet herhalen. Contactpagina en vier RapoWash-tekencoderingen zijn ook live hersteld. Het volgende concept is **UNPUBLISHED 196368531722 — BadkamerCity - Retourinformatie 8 nov**. Eerst aanvullend publiek previewbewijs vastleggen, daarna eigenaarreview op laptop/telefoon en bij akkoord publiceren; het [nieuwe reparatiedossier](../repairs/2026-11-08/contact-and-returns/README.md) bewaart de actuele grens. Btw-identiteit, native policyopmaak/verzending, mail, aankoopmeting en volledige mobiele werking blijven afzonderlijke taken.

Het eigen filterdossier is leidend: **FILTER-SIMPLE-02v2 APPLIED_VERIFIED / PUBLIC_API_VERIFIED / DESKTOP_UI_VERIFIED** volgens de parallelle overdracht van 8 november; installer niet herhalen. **FILTER-ACERO-01 APPLIED_VERIFIED / PUBLIC_API_VERIFIED** is volgens de latere parallelle overdracht live gecontroleerd; niet opnieuw installeren. Praktijkreview en het Cottoceramix-merkprofiel blijven apart vervolgwerk. Deze audit heeft geen nieuwe filtertest uitgevoerd en wijzigt die volgorde niet.
