# Taken — livegang, Google en SEO

**Stand: 8 november 2026 — DOC-LIVE-01, aangevuld met FOOTER-FIX-01.** Deze matrix vervangt de actuele statusclaims van LAUNCH-01/02/03; het [logboek](LOGBOEK.md) en oude bewijsbestanden behouden hun meetmoment. [Diepe audit en bevindingen](../audits/2026-11-08/README.md). Jackson beslist over bedrijfsgegevens, accounts en echte bedrijfsafhandeling; uitvoering levert controleerbare technische wijzigingen/bewijzen.

Status: DONE = binnen benoemde scope bewezen; OPEN = nog uitvoeren; PARTIAL = deel bewezen; IN_PROGRESS_USER = eigenaar werkt eraan; TO_VERIFY = actuele werking of vereiste nog gericht toetsen; LATER = na de basis. P0 = voor betrouwbare verkoop/promotie; P1 = voor het betreffende Google-/SEO-spoor; P2 = verdere groei. Een blokkade voor één product houdt de rest niet automatisch tegen.

## Winkelbasis

| ID | Prio | Taak | Status | Acceptatie / wat resteert | Eigenaarrol |
| --- | --- | --- | --- | --- | --- |
| BC-LIVE-000 | P0 | Openbaarheid, HTTPS, robots en sitemap lezen | DONE | Gedateerde nulmeting + 8-novemberaudit; geen verklaring dat alle interactieve routes werken | Uitvoering |
| BC-LIVE-001 | P0 | Bedrijfsidentiteit en contact afronden | PARTIAL | [Register](BEDRIJFSGEGEVENS.md): tijdelijke telefoon en Zichtenburglaan bekend; volledig btw-id, juridische naam/vestiging controleren en consistente publicatie | Jackson + uitvoering |
| BC-LIVE-001A | P0 | Contact-/retouradres en juridische vestiging onderscheiden | PARTIAL | Openbare contact-/retourlocatie Zichtenburglaan 150 bevestigd; geregistreerde KvK-vestiging NOT_VERIFIED, niet afleiden of privé-adres herpubliceren | Jackson |
| BC-LIVE-002 | P0 | Contact, verzending, retourbeleid en voorwaarden publiceren | PARTIAL | Vijf native policies bestaan; voorwaarden/kennisgeving correct als HTML opslaan; verzending ontbreekt; contact en footer gelijk trekken | Jackson + uitvoering |
| BC-LIVE-003 | P0 | Bestelproces doorlopen | PARTIAL | Zoek/filter/cart en gastcheckout desktop bewezen in beperkte proef; [verzending, betaalmiddelen, betaling, ordermail en mobiel](CONTROLES.md) nog toetsen | Jackson + uitvoering |
| BC-LIVE-004 | P0 | Leverbaarheid en levertijden afmaken | IN_PROGRESS_USER | Onderbouwde bron per merk/product; FAB-04 en gerichte latere bewijzen hergebruiken, geen algemene voorraad-/levertijdclaim | Jackson + uitvoering |
| BC-LIVE-005 | P0 | Contact- en retourberichten ontvangen en beantwoorden | PARTIAL | Formulieren aanwezig; [mailproef](CONTROLES.md) nog uitvoeren: succes, ontvangst/spam, juiste velden, reply-to en antwoord | Jackson + uitvoering |
| BC-LIVE-006 | P1 | Producten klaarzetten voor Google | OPEN | [Batchcontrole](GOOGLE_PRODUCTCONTROLE.md), circa tien uiteenlopende items en Merchant-readback; ACTIVE is geen feedvrijgave | Uitvoering |
| BC-LIVE-007 | P1 | Verlavio-beelden en Google-geschiktheid controleren | PARTIAL | Rebrand/gericht koopbaarheidsherstel FAB-03/04 behouden; juiste beelden, identifiers en huidige Google-bestemming per batch | Jackson + uitvoering |
| BC-LIVE-008 | P1 | Productfoto's en foute beeldweergave nalopen | IN_PROGRESS_USER | Echte requests/zichtbaarheid per relevante renderer; Lagoo-fotoverbod behouden | Jackson + uitvoering |
| BC-LIVE-009 | P1 | Eén standaardfooter winkelbreed gebruiken | PARTIAL | FOOTER-FIX-01: [concept geïmplementeerd](FOOTER_EN_BELEID.md) in UNPUBLISHED 196354474250 na 1.387/1.387 pariteit; precies twee footerfiles gewijzigd. 17 blocks (4/10/3), category.limit 6→10, contactgegevens en winkelbrede homeankers; eigenaarreview/publicatie en publieke nacontrole open | Uitvoering + Jackson |
| BC-LIVE-010 | P0 | Dertig-dagenretourpolicy op website | DONE | Live policy volledig gelezen: 30 dagen aanmelden + 14 terugsturen, €75 incl. btw standaard NL-palletraming, afgeven op afspraak, fout/defect apart; Google gelijkzetten blijft BC-GOOGLE-004 | Jackson + uitvoering |
| BC-LIVE-011 | P0 | Online herroepingsfunctie en directe klantbevestiging | OPEN | Native POST-formulier alleen is onvoldoende bewijs; toegankelijke functie, definitieve stap en onmiddellijke bewaarbare bevestiging met aankoop/datum/tijd testen | Uitvoering + Jackson |
| BC-LIVE-012 | P0 | Modelformulier herroeping beschikbaar | DONE | Volledig formulier met lege velden staat leesbaar in live retourpolicy; gebruik niet verplicht. Geen afzonderlijke PDF als extra eis; dit sluit BC-LIVE-011 niet | Uitvoering |
| BC-LIVE-013 | P0 | HTML-opmaak voorwaarden en kennisgeving herstellen | OPEN | BC-AUD-001/002 blijven open: geen policywrite, `shopPolicyUpdate` mist `write_legal_policies`. Via bevoegde policybewerking correcte HTML opslaan en publiek teruglezen | Uitvoering + Jackson |
| BC-LIVE-014 | P0 | Verzendbeleid en echte tarieven vastleggen | OPEN | BC-AUD-003/010: werkelijke pakket-/pallet-/regioregels, levering en eventuele afhaalafspraak; één locatie zonder rates onderzoeken; €75 retour is geen heenprijs | Jackson + uitvoering |
| BC-LIVE-015 | P0 | Actuele garantie-informatieplicht toetsen | TO_VERIFY | [ACM/EU-bronnen, opnieuw geraadpleegd 8 november](BRONNEN.md): toepasselijk EU-garantiebericht zichtbaar aanbieden, order-/winkelinformatie toetsen; geen uniforme Nederlandse wettelijke termijn van twee jaar claimen | Jackson + uitvoering |
| BC-LIVE-016 | P0 | Productveiligheidsinformatie bij online aanbod toetsen | TO_VERIFY | [NVWA/GPSR](BRONNEN.md): gerichte producttype-/batchcontrole op fabrikantcontact, eventuele EU-verantwoordelijke, identificatie en toepasselijke veiligheidsinformatie; ontbrekende productdata opvragen, geen catalogusbrede overtredingsclaim | Jackson + uitvoering |
| BC-LIVE-017 | P2 | Gerichte content-/navigatieafwijkingen herstellen | PARTIAL | BC-AUD-008/009 en CONTENT-F03/F04 DONE: eigen RapoWash-metadata met compare-and-set en body-H1→H2 op Antikalk live toegepast; publieke HTML-readback PASS. Reukslot, identiteiten, statussen en overige bodies behouden. Retour-FAQ/policy-afstemming blijft apart te controleren | Uitvoering |

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
| BC-SEO-001 | P1 | Homepagezoekvermelding verbeteren | DONE | Homepage-SEO staat live op MAIN 196328685834 en publieke head is teruggelezen; geen ranking-/mobiele vrijgave | Uitvoering + Jackson |
| BC-SEO-002 | P1 | Technische SEO-steekproef uitbreiden | PARTIAL | 364 serverresponses, H1/metadata/canonical/schema gecontroleerd; gerichte afwijkingen geregistreerd; rich results, JavaScript/paginering en echte indexatie apart | Uitvoering |
| BC-SEO-003 | P1 | Mobiele kernroutes en snelheid meten | TO_VERIFY | Echte telefoonbediening en benoemde PageSpeed-/veldmetingen; desktop-HTML is geen mobiele test | Jackson + uitvoering |
| BC-SEO-004 | P1 | Eerste categoriecluster kiezen | OPEN | Assortiment, koopintentie en overlap gecontroleerd; keuze en meetpunt in paginaregister | Jackson + uitvoering |
| BC-SEO-005 | P2 | Bestaande categorieën verbeteren | OPEN | Nuttige keuzehulp, unieke metadata, interne links en passende producten; eerst gekozen cluster | Uitvoering |
| BC-SEO-006 | P2 | Merk-/seriepagina's onderzoeken | OPEN | Bestaande vendor-/Sunshower-routes onderzoeken, één scope per klantvraag; geen automatische kruistabelpagina's | Uitvoering |
| BC-SEO-007 | P2 | Advies en begrippen onderhouden | PARTIAL | Alle 119 gepubliceerde Pages in HTTP-/metadata-audit; inhoudelijke beoordeling per onderwerp blijft open, RapoWash/Antikalk gericht herstellen | Uitvoering |
| BC-SEO-008 | P2 | Imports standaard controleren | OPEN | Categorie, identifiers, media, eenheidsprijs, levering, veiligheidsinformatie en Google-status in bestaande importcontrole | Uitvoering |
| BC-DOC-001 | P1 | Vast livegang-/Google-/SEO-dossier | DONE | LAUNCH-01-structuur en gedateerde nulmeting behouden | Uitvoering |
| BC-DOC-002 | P1 | Eigenaarsaanvulling en vervolgstappen | DONE | LAUNCH-02/03 blijven historische documentatie, geen huidige publicatieclaim | Uitvoering |
| BC-DOC-003 | P1 | Actuele docs reconciliëren met live | DONE | DOC-LIVE-01: huidige status, route-/footer-/bronverschillen en expliciete testgaten gekoppeld; opslag op remote branches afzonderlijk door root te verifiëren | Uitvoering |

## Volgende handeling en andere werkstromen

Binnen dit consistentiedossier: eigenaar bekijkt het bestaande concept **BadkamerCity - Eenduidige footer 8 nov (196354474250)** en publiceert na review via de afgesproken releaseprocedure; daarna publieke footer-/routecontrole. De actuele testgrenzen staan in [het reparatiedossier](../repairs/2026-11-08/footer-and-content/README.md). Antikalk/RapoWash zijn al live gecorrigeerd. Btw-identiteit, policyopmaak en overige koop-/meetchecks blijven afzonderlijke taken.

Het eigen filterdossier is leidend: **FILTER-SIMPLE-02v2 APPLIED_VERIFIED / PUBLIC_API_VERIFIED / DESKTOP_UI_VERIFIED** volgens de parallelle overdracht van 8 november; installer niet herhalen. **FILTER-ACERO-01 APPLIED_VERIFIED / PUBLIC_API_VERIFIED** is volgens de latere parallelle overdracht live gecontroleerd; niet opnieuw installeren. Praktijkreview en het Cottoceramix-merkprofiel blijven apart vervolgwerk. Deze audit heeft geen nieuwe filtertest uitgevoerd en wijzigt die volgorde niet.
