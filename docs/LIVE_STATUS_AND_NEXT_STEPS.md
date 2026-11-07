# BadkamerCity — actuele werkstatus

## BRAUER-24 — brononderzoek loopt; gecontroleerd tussenresultaat · 7 november 2026

Actieve offline taak: resterende 4.968 openbare bronkandidaten exact op merk/SKU/EAN toetsen. Gecontroleerde tussenstand na 2.110 nieuwe pagina’s: **11.809 extra velden**, totaal155.887feiten. Nog9.100artikelen met ontbrekende gekozen kerngegevens,989minder dan BRAUER-23. Dataset en nativeXLSX gecontroleerd op dezelfde stand:13.161artikelregels,20.528cumulatieve aanvullingen,178vragen exact gelijk;12EAN-voorbeelden strings, nul native foutcellen, vijf bladen gerenderd/gecontroleerd.32tests PASS.

Nog28open retailveldverschillen en108verdachte slanglengtes apart. Oorspronkelijke42dataholds/163toekomstige artikelen en alle prijzen/titels/families/opties/notities/media behouden. Primaire bronraadpleging loopt verder; extra gelezen technische tabellen staan privé klaar voor verwerking. Dit is een lopend checkpoint, geen claim dat de volledige werklijst klaar is. Bronraadpleging houdt de gepubliceerde leeslimiet aan; geen tariefwijziging, betaalde uitbreiding of omzeiling.

Geen Shopify-writes, DRAFT-import, media-upload of publicatie; officiële complete afbeeldingen/PDF’s nog afwachten. Retail-extractie bewaart nu ook de aangevraagde URL, zodat doorverwijzingen niet als onbehandelde kandidaten blijven staan. Geen Windows/Excel-app- of live winkeltest geclaimd.

**Eén volgende handeling:** de resterende primaire bronkandidaten en tijdelijke leesfouten afwerken, daarna definitieve dataset/vragen/XLSX/privépakket controleren en dit lopende checkpoint afsluiten. Andere Brauer-schrijvers wachten tot afronding/overdracht.

---

## VERLAVIO-MENU-02 — gegevens toegepast, concept gecontroleerd · 7 november 2026

Eigenaar heeft uitvoering van de geauditeerde keuzeverbeteringen goedgekeurd. **481 bestaande custom.fabriecio_choices-velden live aangepast en exact teruggelezen**: 494 fotoreferenties, 406 eigen-kleurprioriteiten voor compatibiliteit met de huidige renderer, 30 bewezen vervallen keuzes en 15 numerieke lijsten. Alle 4.761 records en 4.096 geldige overgangen behouden; geen prijzen, voorraad, verkoopbeleid of productstatus geschreven. De eerder goedgekeurde productfoto’s blijven gekoppeld; het losse overloopartikel ACS_6001 blijft overgeslagen.

**Nieuw concept: 196341825802 — BadkamerCity - Verlavio keuzemenus 7 nov (UNPUBLISHED).** Exacte kleur-plus-configuratiefoto’s, zes kleuren direct zichtbaar, duidelijke Nederlandse labels en oplopende maten. 19/19 echte JS-tests, 5/5 Shopify-validatorchecks en drie werkelijke browserroutes geslaagd. Eigen server-rendered component op 320/390 CSS-pixels: alle zes foto’s zichtbaar/geladen, geen horizontale overloop. Geen fysieke-telefoon- of checkoutclaim.

De native kopie was vóór bewerking 1.385/1.385 bestanden gelijk aan MAIN **196246372618 — BadkamerCity - Groene voorraadmelding**. Eindcontrole: MAIN nog steeds dezelfde rol en alle oorspronkelijke checksums ongewijzigd; concept 1.387 files, exact vijf productieverschillen plus één geneutraliseerd controletemplate. De connector blokkeerde verwijderen van alleen die QA-file met de algemene theme-deletionregel; daarom veilig overschreven met alleen standaard productsectie, zonder QA-interface, iframes of aparte layout. Geen template-toewijzing uitgevoerd. Config/settings_data.json ongewijzigd.

**Volgende Verlavio-stap:** eigenaar bekijkt en publiceert uitsluitend dit genoemde menuconcept in Shopify. De koppeling staat theme-publicatie/MAIN-filewrites niet toe. Vlak vóór publicatie opnieuw MAIN/einddiff controleren bij eventuele tussentijdse andere theme-wijzigingen; daarna rol/hashes en drie productroutes teruglezen. Geen publicatie uitgevoerd. De bestaande tijdelijke instelling die overal Op voorraad toont verklaart de tegenstelling met een uitverkochte koopknop bij BC_2008/BC_2009; leveranciersstatus N bevestigd. Eerdere eigenaarafspraak over die tekst niet stil gewijzigd; adviseer de voorraadtekst weer de werkelijke beschikbaarheid te laten volgen, zonder voorraad te verzinnen of nabestellen aan te zetten.

[Dossier en herstelgrenzen](fabriecio/2026-11-07/menu-improvements/README.md), [eindcontrole](fabriecio/2026-11-07/menu-improvements/final-verification.json). Code/tests op bestaande branch fix/product-cards-2026-10-14; main krijgt alleen documentatie. Volledig herstelpakket privé opgeslagen; geen ruwe catalogus/feed, herstelwaarden of Admin-receipts in publieke Git. Bestaande lokale header/main-product/Lagoo-werkbestanden blijven behouden. Dit checkpoint wijzigt de aparte BRAUER/Cottoceramix-holds en vervolgafspraken hieronder niet.

## BRAUER-23 - leveranciersbestanden en bestaande tabellen verder benut · 7 november 2026

Eigenaar vraagt toe te voegen wat nog kan; drie oorspronkelijke kranen-, glas- en meubelbestanden zijn al aanwezig en blijven de basis. Alle 13.161 artikelen gescand op nog onbenutte letterlijke gegevens. **4.734 extra specificaties bij 4.380 artikelen:** 4.300 uit de leveranciersgegevens, 434 uit al eerder gecontroleerde technische tabellen. Geen nieuwe websitecrawl of achtergrondtaak voor deze batch.

Leveranciersaanvullingen omvatten letterlijke uitvoeringsnamen, expliciete straalstanden handdouche, uitgesloten grepen, draaibare/platte uitlopen, dim-/lichtkleurfuncties, afstandsbediening, klokken, wasbak-aantallen en expliciete plaatsings-/opbergkenmerken. Geen mm-dikte of fysieke maten uit namen als Slim/Medium of uit unitloze maatcodes afgeleid. Retail onder andere bediening, plaats bediening, hartafstand, vorm/aantal rozetten, plugdiameter en sifonaansluiting; uitsluitend passende veldcontext en exact merk/SKU/EAN. Geen uitlezen van ontbrekende iconen als Nee.

**Alle bestaande specificatiewaarden, prijzen inclusief btw, SKU/EAN, titels, families, opties, eigen aanvullingen, originele bronnen en media behouden.** Businessrecords exact gelijk aan BRAUER-22 buiten specificaties en controlenotities; geen bestaande specificatie gewijzigd/verwijderd. Oorspronkelijke 42 dataholds, 163 toekomstige artikelen, 28 open retailveldverschillen bij 24 artikelen, 14 verdachte slangwaarden en dezelfde 84 vragen bij 80 artikelen behouden. Historische tegenstrijdige maatwaarden blijven meetellen na verwijdering uit klantvelden; opnieuw verwerken maakt die velden niet alsnog vrij. Twee 004-B4-maatvelden blijven leeg. Herhaalde verwerking behoudt catalogus, veldherkomst en cumulatieve aanvullingen exact.

Totaal **144.078 feiten**. Cumulatieve aanvullende herkomst: 4.419 retailvelden plus 4.300 leveranciersvelden. Nog 10.089 artikelen met minimaal één ontbrekend gekozen kernveld; geen aantal ontbrekende producten of foutpercentage. 4.968 verdere openbare bronkandidaten blijven onbeoordeeld. Nog steeds 905 bronpagina’s / 892 bron-SKU’s / 902 exacte merk-SKU-EAN-pagina’s; drie overige pagina’s zonder EAN alleen aanvullend bewijs.

**Controle:** 23 specificatie-/retail-/leverancierstests + negen voorbereidingstests PASS. NativeXLSX alle 13.161 artikelregels, 8.719 cumulatieve aanvullingen en 84 vragen exact vergeleken; 12 EAN-voorbeelden strings, nul native foutcellen. Vijf bladen gerenderd/gecontroleerd plus afzonderlijk de leveranciersregels; recalc 13.161/10.089 correct. Privébundel 79 entries, 78 manifesthashes; alle oorspronkelijke bestanden en eigen invoer behouden. Codecheckpoint **3e873f0056ee8605610dac7865d933fc5f343cca** op fix/product-cards-2026-10-14. [Gegevens en vervolg](brauer/2026-11-07/RETAILSPECIFICATIES.md), [dekking](brauer/2026-11-07/RETAILDEKKING.json).

**Geen Shopify-writes, DRAFT-import, media-upload, themawrite of publicatie.** MAIN voor/na 196246372618. Alle vrijgavevlaggen false; preflight terecht exit2. Officiële volledige afbeeldingen/PDF-aanlevering nog afwachten. Daarna inventarisatie/exacte koppeling en complete representatieve pagina-/keuzeproef vóór enige import. Connector/remote-werk, scratch geen Git-checkout; geen Windows/Excel-app- of live winkeltest geclaimd. Volledige catalogus, leveranciersbestanden en gebruikersinhoud blijven privé.

**Eén volgende handeling:** verdere openbare bronkandidaten exact op artikelidentiteit onderzoeken voor ontbrekende kerngegevens; uitzonderingsvragen apart laten bevestigen. Media afwachten en import geblokkeerd houden tot ontvangst, inventarisatie, volledige proef en akkoord.

---

## BRAUER-22 - verdere specificaties en concrete open vragen · 7 november 2026

500 verdere openbare productpagina’s uit34typen gelezen; alle500 exact op fabrikant-SKU, EAN en merk. Cumulatief905pagina’s /892bron-SKU’s /902exacte merk-SKU-EAN-pagina’s. Drie pagina’s zonderEAN alleen vergelijkingsbewijs. **Deze batch2.264extra klantvelden; cumulatief3.985nieuwe velden bij871artikelen**, zeven oudere externe waarden ingehouden. Totaal139.344feiten;10.089artikelen missen één of meer gekozen kernvelden. De volledige catalogus is nog niet uit alle bronnen onderzocht;4.968verdere URL-kandidaten staan klaar zonder achtergrondtaak.

Collision GS-CLI1H100200CE helder glas bevestigd door leverancier plus tweede winkel bij exact hetzelfde SKU/EAN. Afwijkende Brons rook-waarde blijft in de historie, maar wordt voor dit artikel verworpen. Geen PDF-maatbesluit of mediaontvangst daarvoor geclaimd. Door extra kleuronderzoek nu28openveldverschillen bij24artikelen, vooral dezelfde RVS/messing-tegenspraak. Veertien verdachte15cm-slanglengtes blijven ingehouden; geen gok naar150cm. Oorspronkelijke42dataholds behouden:27leveranciersverschillen,12uitvoeringsambiguïteiten en3maatbronconflicten.

**84concrete vragen bij80artikelen** met SKU, EAN, veld, waarden en bronlinks in het privévoorbereidingspakket en Excelblad Bronverschillen. Tellingen overlappen; niet optellen bij aantallen ontbrekende kernvelden. Geen bericht naar leverancier verstuurd. Huidige fabrikant-handleiding inbouwwastafelkranen noemt328–335, dus geen onbewezen toepassing op004. Niet visueel raadpleegbare winkelbijlagen/alleen metadata lossen geen fysieke maat op.

**Controle:** elf retailtests + zes specificatietests + negen voorbereidingstests PASS. Alle13.161artikelrecords buiten specificaties/review exact gelijk aan BRAUER-21; prijs/BTW, titels, SKU/EAN, families, opties, notities en163toekomstige artikelen behouden. Definitieve nativeXLSX:13.161artikelregels,3.985aanvullingen en84vragen exact vergeleken;12EAN-voorbeelden strings, nul native foutcellen. Vijf bladen gerenderd/gecontroleerd; recalc13.161/10.089correct. Privépakket70entries,69manifesthashes en alle oorspronkelijke bestanden behouden. Bestaande Excel en ZIP vervangen met behoud van hun identiteit; één Excel-versieconflict via verse ongewijzigde bron herladen en opnieuw toegepast.

**Geen Shopify-writes, DRAFT-import, media-upload of thema/publicatiewrite.** MAIN voor/na196246372618. Alle vrijgavevlaggenfalse, preflight terecht exit2. Volledige officiële afbeeldingen/PDF-aanlevering nog niet ontvangen. Daarna inventarisatie/exacte koppeling en volledige representatieve pagina-/keuzeproef vóór enige import. Codecheckpoint **0b4d067233fc76de0abeaa4cda56f1d124233837** op fix/product-cards-2026-10-14. Connector/remote-werk; lokale scratch is geen Git-checkout, geen Windows/Excel-app- of livewinkeltest geclaimd. [Onderzoek en open werk](brauer/2026-11-07/RETAILSPECIFICATIES.md), [dekking](brauer/2026-11-07/RETAILDEKKING.json).

**Eén volgende handeling:** resterende openbare bronkandidaten exact op merk/SKU/EAN onderzoeken en bewezen ontbrekende kernvelden aanvullen; de84concrete uitzonderingsvragen apart laten bevestigen aan actuele artikelgegevens. Media afwachten; import blijft geblokkeerd.

---

## BRAUER-21 - retaileronderzoek en eerste brede technische verrijking · 7 november 2026

Eigenaar staat gegevensonderzoek bij BadkamerXXL en Sanitairwinkel expliciet toe. Alle170Brauer-overzichtspagina’s gelezen;10.148uniekeURL-kandidaten en5.827letterlijke codesuffix-kandidaten geregistreerd. Dit zijn zoekkandidaten, geen artikelidentiteitsbewijs. Eerste brede selectie351artikelen uit39typen plus54vergelijkingspagina’s, allemaal vers opnieuw gelezen:405openbare productpagina’s /392bron-SKU’s;402pagina’s exact op merk + fabrikant-SKU + EAN. Drie pagina’s zonderEAN alleen als vergelijking, niet zelfstandig voor een nieuwe waarde. Geen overerving naar kleuren, maten of andere serieleden.

**1.721velden toegevoegd bij379artikelen; zeven eerdere externe waarden bij tegenspraak ingehouden.** Netto1.714extra klantvelden, totaal137.080inclusiefidentiteiten.17openveldverschillen bij13artikelen en14afwijkende15cm-doucheslangwaarden apart; geen stille correctie naar150cm. Ook een bron zonderEAN kan tegenbewijs leveren: de Garnet-breedte blijft daarom open. De oudere59/60cm-spiegelkastafwijking is met verse inhoud van beide bronnen opgelost op59cm. Galactic6/8mm-getuigenis is op de exact gekoppelde artikeltekening gecontroleerd;8mm en breedte118,1–119,6cm ondersteund. Onderdeelmaten krijgen hun eigen context, geen2,4cm als diameter van een hele doucheset. Leveranciersgegevens, prijzen incl.btw, titels, opties,1.568groepen, eigen aanvullingen en media ongewijzigd; oorspronkelijke42dataholds en163toekomstige artikelen behouden. Nu10.357artikelen met ontbrekende gekozen kernvelden; geen volledige technische vrijgave.

**Controle:** tien retailtests + zes specificatietests + negen voorbereidingstests PASS. DefinitieveXLSX:13.161artikelregels en1.721aanvullingsregels native exact tegen catalogus/report vergeleken,12EAN-voorbeelden strings, nul native foutcellen. Vijf bladen gerenderd/gecontroleerd; recalc13.161/10.357correct. Bestaande review-XLSX uitgebreid met Aanvullingen en Bronverschillen; privévoorbereidingspakket bevat alle veldherkomst, bronobservaties, tekeningsbesluiten en5.468verdere URL-kandidaten. Geen achtergrondtaak of volledig gescrapete eigen catalogus geclaimd. [Onderzoek en vervolg](brauer/2026-11-07/RETAILSPECIFICATIES.md), [dekking](brauer/2026-11-07/RETAILDEKKING.json).

**Geen Shopify-writes, DRAFT-import, media-upload of thema/publicatiewrite.** MAIN voor/na196246372618 (BadkamerCity - Groene voorraadmelding). Nieuwe vrijgavevoorwaarde retail_specifications_reviewed=false; echte onopgeloste artikelvelden blokkeren ook wanneer alleen vlaggen worden omgezet. Volledige officiële mediapakket nog niet ontvangen; een gevonden derden-PDF telt niet als ontvangst. Codecheckpoint **9c3486c3440b9aaadc8dd13e228bbb5dffa538aa** op fix/product-cards-2026-10-14; connector/remote-werk, geen Windows-Git-, fysiekeExcel- of livewinkeltest. Code en overdracht vóór afronden exact op beide vaste ingangen teruglezen.

**Eén volgende handeling:** de17openvelden en14afwijkende slangwaarden op actuele technische tekeningen/leveranciersgegevens controleren, vóór de volgende batch uit de resterende werklijst. Alle bestaande media-/proef-/importvoorwaarden blijven gelden.

## BRAUER-20 - duidelijke productspecificaties offline · 7 november 2026

Alle 13.161 artikelen / 76 producttypen hebben nu een klantgerichte specificatietabel: Algemeen, Afmetingen, Uitvoering en Meegeleverd. Alle 135.366 veldwaarden hebben bronbewijs; dit totaal bevat ook merk/artikelnummer/EAN. Elke unieke fabrikant-SKU behoudt zijn eigen tabel; 64 eerdere exacte SKU/EAN-controles behouden zonder uitbreiding naar andere kleuren. Geen onbekende Nee-waarden, geen fysieke cm-maten uit unitloze modelnummers. De 27 materiaal-/afwerkingsconflicten en drie maatconflicten leveren geen betwiste klantwaarden meer op.12niet-unieke keuzeartikelen en163toekomstige artikelen blijven apart;42dataholds behouden. Prijzen incl.btw, artikelidentiteit, opties, families, eigen aanvullingen en media onveranderd.

Voor10.552artikelen ontbreken nog gekozen technische kernvelden. Dit is geen foutpercentage; ook2.609artikelen met gekozen kernvelden zijn nog niet technisch of commercieel vrijgegeven. Nieuwe review-XLSX met Overzicht, Voorbeelden en Artikelen; volledige tabellen/provenance en reproduceerbare scripts in bestaande privé-ZIP bijgewerkt. Zes nieuwe specificatietests en negen voorbereidingstests PASS; elke zichtbare waarde heeft bewijs, bestaande bedrijfsdata fingerprintgelijk. Bestands-/recalc-/visuele controles vastgelegd bij [specificaties](brauer/2026-11-07/SPECIFICATIES.md). Huidige Brauer-theme-router nog niet op het nieuwe tabelformaat aangesloten; latere UNPUBLISHED-integratie en winkelproef verplicht.

**Geen Shopify-writes/import, ook geen DRAFT/media-upload/publicatie.** Volledige officiële afbeeldingen/PDF’s ontbreken. MAIN voor en na read-only196246372618 (BadkamerCity - Groene voorraadmelding). Geen lokale Windows/Git- of Excel-appcontrole geclaimd. Actieve codebranchfix/product-cards-2026-10-14; codecheckpoint is de commit die dit blok en scripts invoert, remote teruglezen vereist. **Eén volgende handeling:** ontbrekende fysieke maten en aansluitgegevens per exact artikel verrijken met officiële technische productdata. Mediaontvangst/inventarisatie en latere beoordeelde proef blijven importvoorwaarden.

## BRAUER-19 - volledige catalogus offline voorbereid na UX-goedkeuring · 7 november 2026

Eigenaar keurt de aangepaste voorbeelden goed en geeft opdracht de goedgekeurde regels op het hele bestand voor te bereiden voor latere import. **Geen opdracht om nu te importeren.** Volledige officiële media-/PDF-ontvangst en de daaropvolgende proef blijven voorwaarden.

**Volledige verwerking:** drie originele lijsten en productbasisversie1 na workspace-onderhoud teruggehaald uit de bestaande bestandsopslag.13.757bronregels →13.161unieke SKU/EAN’s,76producttypen en1.568keuzegroepen.1.559groepen voorbereid; negen groepen bevatten nog vastgelegde dataholds. Eén artikelidentiteit per fabrikant-SKU behouden; alle voorgestelde handles onderling uniek. Consumentenprijzen allemaal21%btw inclusief, Decimal half-up én onafhankelijke gehele-centcontrole;469halvecentgevallen correct. Alle SKU’s/EAN’s/voorgestelde handles uniek en EAN-checksums geldig. Nog geen winkelbrede botsingscontrole.

**Goedgekeurde UI-regels toegepast op de hele gegevensvoorbereiding:** kleur eerst / zes zichtbaar / Bekijk meer kleuren; knoppen bij twee of drie maten, grotere maatgroepen dropdown; ontbrekende combinaties zichtbaar-uitgeschakeld; eerste foto exact gekoppeld product voor kleur/configuratie/bakpositie; spiegelkastdecorstalen; greepafwerking Standaard/glad, Carving/gekarteld, Stripe/gestreept; geverifieerde losse hendelbeelden blijven binnen bewezen scope. Standaard/ondiep en120cm-halfhoog/160cm-hoog apart. Deurrichting alleen bij echte alternatieven voor gekozen maat/decor; afvoerkeuze opnieuw beoordelen na maat/lades. Alle150opbouwwastafelkranen zijn als bronbevestigde hoogte-/greep-/uitloopmatrix voorbereid, met conditionele uitloopvorm; Laag/Verhoogd/Hoog blijven fabrikantbenamingen, geen verzonnen middelmaat of universele fysieke hoogte. Kritieke resttekst/setcomponenten, materiaal en onderdeelrollen blijven groepsgrenzen; geen compatibiliteit of setinhoud bijverzonnen. Twintig niet-verbonden oorspronkelijke keuzegrafen gesplitst zodat bereikbaarheid geen stille tweede keuzeverandering vraagt.

**Holds behouden:**27artikelen met29materiaal-/afwerkingsconflicten;12artikelen met identieke keuzewaarden maar andere codes (onder meer013/153); drie eerdere maatconflicten op5-CE-001,5-GG-001 enGS-OBI2B9030200CE. Samen42verschillende artikelen op datahold; daarnaast163toekomstige artikelen met bronbeschikbaarheid1februari2027, geen voorraadclaim.64eerder exact-SKU/EAN-gecontroleerde verrijkingen hersteld; betwiste maten expliciet Te bevestigen. Geen dealerbeeld als ontvangen officieel pakket opgevoerd. Oorspronkelijke productbasis en bronbestanden ongewijzigd; gebruikersaanvullingen behouden.

**Controles:** negen passende tests PASS; alle13.161artikelen verwerkt, alle familieleden precies eenmaal geregistreerd, alle gegenereerde grafen verbonden.155.162geldige transities en9.822ontbrekende transities gecontroleerd;454meervoudige uitkomsten blijven onbeslist, geen willekeurig artikel gekozen. De twaalf niet-unieke artikelkeuzes blijven expliciet HOLD. Exacte bestandskoppeling voorkomt001/001-HD1- en L/R-verwisseling; onduidelijke eerste fotovolgorde vraagt controle. Importcontrole geeft terechtfalse/exit2, ook wanneer alleen ontvangstvlaggen worden omgezet: ontbrekende beelden en artikelproblemen blijven blokkeren. Geen API-importer of winkelwrites in de scripts.

**Bestanden:** nieuw Brauer-importvoorbereiding-2026-11-07.xlsx met vier bladen: Overzicht, Producten, Keuzegroepen, Uitzonderingen. Vier gele kolommen voor eigen tekst/techniek/afbeeldingen/PDF’s; aparte lezer koppelt deze strikt op SKU én EAN. Alle13.161nativeXLSX-SKU/EAN/titel/statuswaarden exact met export vergeleken; EAN’s blijven strings. Recalc telt13.161/1.568/27/12/163/0correct, drie maatbronconflicten apart; nul formulefouten. Alle vier bladen en aanvulgebied visueel gecontroleerd. Volledig privéherstel-/voorbereidingspakket Brauer-importpakket-2026-11-07.zip bevat originele bronnen, catalogus, groepen, mediakoppelaar, veld-/collectievoorstellen, release-gate, controles, scripts en PowerShell-uitleg. Publieke Git bevat alleen code en samengevat bewijs, geen volledige bron-/prijslijsten of beeldbytes.

**Aansluiting winkel:**227bestaande collecties opnieuw volledig read-only gepagineerd; alle76typevoorstellen hebben bestaande doelidentiteiten. Toewijzingen blijven voorstellen: actuele collectievoorwaarden/velddefinities en winkelbrede SKU/EAN/handle-botsingen vóór import toetsen. Huidige prototypes nog niet in Shopify-theme geïntegreerd; specs/leverinformatie/V2-selector, officiële media en concept-PDP/cartproef blijven releasevoorwaarden. Oudere Liquid ThemeCheck-dependency blijft open. Alle stappen staan onder [volledige voorbereiding en bewijs](brauer/2026-11-07/VOLLEDIGE_VOORBEREIDING.json); code op bestaande actieve branch fix/product-cards-2026-10-14 onder scripts/brauer/preparation/.

MAIN read-only bevestigd als196246372618 — BadkamerCity - Groene voorraadmelding. Geen Shopify-writes, DRAFT-import, voorraad-/prijsinstellingwijziging, media-upload of publicatie. Scratch geen Git-werkboom; geen Windows-lokale controleclaim. Geen actieve schrijver na overdracht.

**Exact één volgende handeling:** volledig officieel Brauer-afbeeldingen-/PDF-pakket ontvangen en op exact artikelnummer inventariseren; daarna de42dataholds met de juiste leveranciersbronnen sluiten en de bestaande concept-/proefroute uitvoeren.

## BRAUER-18 - greepdetails, kleur eerst en voorwaardelijke deurkeuzes · 7 november 2026

Expliciete gebruikerscorrecties op de offline proef verwerkt. Eerdere BRAUER-16-kleurenregel krijgt een gerichte uitzondering voor spiegelkastdecorstalen; BRAUER-17 gecombineerde120/160cm-kast en breedte/deurmenu zijn vervangen.

**Uitgevoerd:**
- Kleur/decor staat als eerste beschikbare keuze in alle23voorbeeldfamilies (14eerdere +9bijgewerkte). Eén vaste kleur wordt geen nutteloze keuzeknop. Consumentenlabel Edition vervangen door Standaard; originele leveranciersidentiteit/SKU’s/EANs blijven brondata.
- Greepafwerking toont drie daadwerkelijke detailfoto’s: Standaard/glad, Carving/gekarteld en Stripe/gestreept. Foto’s uit de bestaande BadkamerXXL-uitleg Afwerking greep opgehaald, hashes gecontroleerd en visueel bekeken. Expliciet structuurvoorbeeld in RVS-kleur, geen exacte gekozen SKU-/kleurfoto. Zeven bestaande standaard-lage001artikelen toegevoegd naast de12Carving/Stripe-artikelen, waaronder toekomstigeCoffee alleen waar een echte SKU bestaat.
- Hoofd-/kleurfoto’s en overige fotokeuzes blijven eerste beeld exact gekoppeld product; de vijf bestaande losse A-E-hendelvormfoto’s blijven behouden.
- Aurora heet wastafel voor onderkast; montage/omschrijving verduidelijkt. Bakpositie gebruikt de eerste foto van de bij breedte/kraangaten passende SKU. Geen onbewezen wastafel/onderkastcombinatie aangemaakt.
- Adore MFC120cm is nu afzonderlijk halfhoge kast30artikelen;160cm afzonderlijk hoge kast15artikelen. Geen hoogtemenu tussen beide.
- Impress Deluxe heeft kleurstalen, breedtedropdown en een dynamische deurrichting. De Links/Rechts-keuze verschijnt alleen wanneer meer dan één echte richting bij gekozen breedte én decor bestaat; in deze90artikelen alleen bij60cm. Algoritme leest werkelijke kandidaten, geen hardcoded60cm. Eerste bezoek aan een onbesliste60cm-uitvoering vraagt richting en kiest niet stil een SKU. Reeds expliciet gekozen richting blijft bij terugschakelen bewaard.80cm en breder verbergen de keuze.
- Spiegelkastkleuren zijn benoemde decorstalen, steeds zes zichtbaar plus Bekijk meer kleuren. Hoofdfoto blijft het exacte product.

**Validatie:** nieuwe9families/469unieke artikelen: werkelijke preview-JS met DOM-stub,8.294geldige /573geweigerde transities PASS;120overgangen bewust onbeslist (60afvoer,60deurrichting). Alle artikelen bereikbaar; SKU/EAN/prijs, behoud overige keuzes, eerste-image add/append/reorder/remove, identiteitbescherming, afvoerbehoud, deurzichtbaarheid/onthouden en decorstalen PASS.469prijzen onafhankelijk met Decimal×1,21 half-up tegen originele bron vergeleken. Positie-spoelbakfoto reageert op wijziging van het eerste beeld van exact het kandidaatartikel terwijl de huidige SKU gelijk blijft.
Eerdere14families/876records opnieuw getest:13.488geldige /1.489geweigerde transities; kleur-eerst en de vijf A-E-vormbeelden PASS. Totaal23families,1.345voorbeeldrecords /1.326uniekeSKU’s (bewuste overlap). Geen browserlayout/native touch/live PDP/cart-test geclaimd. Nieuwe proef984.763bytes,104exacte tijdelijke productbeelden plus3structuurclose-ups. Oorspronkelijke98voorbeeldbeelden aangevuld met6bestaande standaard-kraanfoto’s; Coffee nog zonder beeld.

[Correctiecontract, beeldbronnen en controles](brauer/2026-11-06/UX_CORRECTIES_CONTRACT.json). Geteste offline generator-/template-/conditionele provider-/testcode op bestaande actieve branch fix/product-cards-2026-10-14 onder scripts/brauer/prototypes/ux-refinement/. Publieke Git bevat geen private volledige bron-/prijslijsten of derdenbeeldbytes. Geen Shopify-thema-integratie. Productbasis-XLSX versie1 en oorspronkelijke leveranciersdata ongewijzigd.

MAIN read-only vóór/na bevestigd als196246372618 — BadkamerCity - Groene voorraadmelding. Geen Shopify-writes, import (ook geen DRAFT), media-upload, voorraadwijziging of publicatie. Volledig aangekondigd officieel beelden-/PDF-pakket blijft vereist vóór import; tijdelijke dealerbeelden tellen niet als pakketontvangst. Drie eerdere maatconflicten en Liquid ThemeCheck-blokkade blijven open. Scratch geen Git-werkboom; geen Windows-lokale controleclaim. Geen actieve schrijver na overdracht.

**Exact één volgende handeling:** eigenaar beoordeelt de aangepaste proef, vooral greepdetails, spiegelkast60→80cm en de losse120/160cm-kasten.

## BRAUER-17 - acht andere productgroepen als offline proef · 7 november 2026

Eigenaar wil de overige voorgestelde producten daadwerkelijk kunnen proberen. Alleen offline gesprekproef, geen import- of publicatievrijgave.

**Nieuwe scope:** 462 unieke bronartikelen: Galactic cabine12, Void tweedelige nisdeur132, Aurora13, Trust MFC standaard120, Adore MFC standaard hoge kast45, Impress Deluxe MFC90, Carving/Stripe laag12 en opbouwfonteinkranen38. Voorgaande veertien-familieproef blijft apart en ongewijzigd.

Galactic heeft twee afmetingknoppen en omkeerbaarheid als specificatie. Void toont eerste artikelfoto’s voor scharnieren aan muur of glas; de deurbreedte volgt de echte bronconfiguratie. Aurora combineert breedte, bak midden/links/rechts en kraangaten; alle13exacte dealer-SKU/EANs bevestigen bakpositie en buitenbreedte61/81/101/121cm. Trust heeft aparte standaarddieptescope, grepen uitgesloten en de bestaande voorwaardelijke afvoerindeling. Adore gebruikt drie heldere hoogte/deuruitvoeringen; Wavy uitgesloten. Impress combineert breedte/deuren en voegt geen onbewezen bediening/dimmer toe. Carving/Stripe gebruiken eigen artikelfoto’s. Fonteinkranen houden design, uitloop en werkelijke kleurbeperkingen.

**Foto’s en data:** 98 tijdelijke eerste-galerijbeelden, ieder exact SKU/EAN gecontroleerd; 200px-rendities van hetzelfde eerste bestandsnaambeeld, byte/hashes gecontroleerd. Een ontbrekende foto blijft Productfoto volgt en blokkeert geen geldige SKU. Maatverrijking blijft uitsluitend per gecontroleerde SKU; overige buitenmaten Te bevestigen. Geen Joy-maten op Trust. Alle462btw-prijzen onafhankelijk Decimal×1,21 half-up vergeleken met het bestaande prijsvoorstel. Productbasis-XLSX versie1 ongewijzigd.

**Verificatie:** werkelijke ingebedde JavaScript met DOM-stub, alle462toestanden en8.319geldige /559geweigerde transities PASS;60meubeltransities bewust onbeslist tot afvoerkeuze. Alle bronartikelen bereikbaar, SKU/EAN/prijs/statebehoud/zes-kleurenlimiet/disabled-opties en eerste-beeld add/append/reorder/remove plus identity guards PASS. Gekozen afvoerindeling blijft nu ook bij kleurpreview behouden; een onbesliste afvoerindeling toont geen willekeurige exact-artikelfoto. Acht representatieve productbeelden visueel ingezien, waaronder beide Void-scharnieropstellingen en Carving/Stripe. Fragment876.510bytes. Browserlayout/native bediening/live PDP/cart NOT_TESTED.

[Proefcontract en representatieve bronnen](brauer/2026-11-06/NIEUWE_PRODUCTPROEF_CONTRACT.json). Alleen sanitiseerde generator-/renderer-/testcode op de actieve codebranch onder scripts/brauer/prototypes/other-products/; geen volledige private product-/prijslijsten of derdenbeeldbytes in publieke Git. Lokale fixtures blijven aanvullende reviewdata. De voorbeeldtemplate is een offline generatorbasis, geen Shopify-theme-integratie.

MAIN read-only bevestigd als196246372618 — BadkamerCity - Groene voorraadmelding. Geen Shopify-writes, media-upload, import (ookgeenDRAFT) of themapublicatie. Alle import wacht op volledige aangekondigde leveranciersbeeld-/PDF-ontvangst en inventarisatie; tijdelijke dealerfoto’s vervangen dat pakket niet. Drie eerdere maatbronconflicten en Liquid ThemeCheck-blokkade blijven open. Scratch geen Git-werkboom; geen Windows-lokale statusclaim. Geen actieve schrijver na overdracht.

**Exact één volgende handeling:** eigenaar beoordeelt deze acht nieuwe offline menu’s; daarna concrete feedback verwerken voordat de catalogus verder wordt vrijgegeven.

## BRAUER-16 - kleurbeelden overal gekoppeld en UX-goedkeuring vastgelegd · 7 november 2026

Eigenaar vult aan dat dezelfde eerste-productfoto-regel ook overal voor kleurkeuzes geldt en keurt met die aanvulling de huidige opzet goed. Vraagt welke afwijkende keuzemenu's nog controle verdienen.

**Uitgevoerd:** alle bestaande kleur-/decorstalen in de gesprekproef gebruiken nu het eerste beeld van het exacte kandidaatkleurartikel, met de andere keuzes behouden. Dezelfde product-ID/SKU-resolver als voor overige fotokeuzes; geen aparte kleurfoto-URL's of representatief ander model. Zes zichtbaar / Bekijk meer kleuren / actieve kleur zichtbaar bij inklappen behouden. Zonder beeld blijft een benoemde voorbeeldstaal met Productfoto volgt; ontbrekende combinaties blijven uitgeschakeld en heten Niet combineerbaar. De losse greepbeelden zijn ongewijzigd. De preview opent op de basishoogtegroep zodat de zes daadwerkelijk gekoppelde kleurartikelfoto's direct zichtbaar zijn.

De huidige opzet is hiermee **UX_GOEDGEKEURD**. Dit is geen verklaring dat alle brondata, alle 13.161 artikelen, alle menu's of de nog niet gekoppelde Shopify-media compleet/gepubliceerd zijn. Bestaande importstop tot volledige leveranciersmedia-/PDF-ontvangst blijft.

**Controle:** werkelijke preview-JS opnieuw doorlopen voor alle 876 voorbeeldrecords / 864 unieke SKU's; 13.488 geldige / 1.489 geweigerde transities en 60 bewust onbesliste meubeltransities. Iedere kleurtegel op kandidaat-SKU/beeldbron gecontroleerd; eerste-beeld-update op een voordien fotoloos glasartikel werkt tegelijk in de hoofdfoto én kleurtegel. Zes-stalenlimiet en grepen intact. Browserlayout/echte bediening NOT_TESTED. Fragment 741.784 bytes; nog 58 tijdelijke referentiebeelden, geen extra leveranciersbeelden geclaimd.

[Goedkeuring en resterende controles](brauer/2026-11-06/UX_GOEDKEURING_EN_RESTERENDE_CONTROLES.md) onderbouwd met de oorspronkelijke drie leverancierslijsten. Grootste nog niet beoordeelde gedragingen:
1. Douchecabines en andere nisdeuren: draai/schuif/draai-schuif, breedte × diepte, deur aan wand/glas en correcte omgang met omkeerbaarheid.
2. Andere onderkastseries, wastafels en topbladen: grepen, kraangaten, bakpositie, afvoeren en bewezen onderlinge compatibiliteit; Joy is geen volledige meubeldekking.
3. Carving/Stripe, overige douchevarianten en fonteinkranen: structuur, bediening, sets en inkortbaarheid.
4. Hoge kasten, spiegels/spiegelkasten: deurrichting en modelgebonden verlichting/bediening.
Losse accessoires en gewone kleur-/maatgroepen daarna met dezelfde geautomatiseerde combinatietests; geen handmatige product-voor-productcontrole als nieuwe standaard.

Geen nieuwe productfamilies gebouwd of Shopify-writes uitgevoerd in deze inventarisatiestap. De eerdere drie maatbronconflicten en Liquid ThemeCheck-dependency blijven open. MAIN read-only bevestigd als196246372618 — BadkamerCity - Groene voorraadmelding; geen themawrite, productimport, media-upload of publicatie. Productbasis-XLSX versie1 ongewijzigd, scratch geen Git-werkboom; geen Windows-lokale statusclaim. Geen actieve schrijver na overdracht.

**Exact één volgende handeling:** één representatieve douchecabine met afwijkende deur-/opstellingskeuzes als volgende offline proef uitwerken. Daarna een wastafel-/meubelcombinatie; bronconflicten sluiten zodra het officiële pakket binnen is.

## BRAUER-15 - grepen hersteld, eerste productafbeelding als bron en zelfstandige steekproef · 7 november 2026

Eigenaar wil de eerdere losse greepafbeeldingen terug, keuzefoto's voortaan uit de eerste afbeelding van het gekoppelde product laden, en een onafhankelijke BadkamerXXL-steekproef op ontbrekende data.

**Uitgevoerd in de offline preview:**
- De vijf goedgekeurde losse hendelvormbeelden zijn terug op de inbouw-hendelkeuze; uitloop, wandafwerking, bedieningskant en opbouwuitvoering blijven fotokeuzes.
- De renderer leest nu de eerste afbeelding uit het gekoppelde productrecord via product-ID én exact SKU. Geen aparte productPhotos/keuzefoto-URL-tabel in de renderer. Bij append blijft de bestaande eerste foto; herschikken verandert de eerste; verwijderen toont Afbeelding volgt en maakt een geldige SKU niet onbestelbaar. Geen fallback naar een ander artikel of een tweede/onjuiste foto.
- Canonieke offline productrecords worden nog gevuld met de eerder gecontroleerde 58 tijdelijke referentiebeelden; synthetische offline-ID's zijn geen Shopify-ID's. Nieuwe productbeelden kunnen via bijgewerkte productdata direct door dezelfde renderer worden gelezen, ook op een eerder fotoloos product. Geen claim op live push vanuit Shopify Admin: nieuwe data/paginaherlaadbeurt blijft nodig.
- Herbruikbare resolver en contracttests staan alleen op de actieve codebranch onder scripts/brauer/prototypes/. Voorbereide Liquid-adapter leest linked_product.images.first uit een al door de bestaande familieprovider opgelost productobject; vereist het huidige één-SKU-per-productcontract en geeft geen beeld bij mismatch/meerdere varianten. **Niet in een Shopify-thema geïntegreerd of uitgerold.**
- Shopify Liquid-docs geraadpleegd. Liquid ThemeCheck geprobeerd, maar BLOCKED: toolkit mist @shopify/theme-check-common. Geen geslaagde Liquid-/live integratievalidatie geclaimd; vóór latere conceptthema-integratie opnieuw valideren. De losse JS-resolver en de werkelijke preview zijn wel uitgevoerd/getest.

**Zelfstandige bronsteekproef:** elf exacte SKU/EAN-controles, verspreid over lage wastafelkranen, inbouwkranen, inbouwbadset, drie glasopstellingen en twee onderkasten. Identiteiten en gekozen configuraties in deze steekproef passen bij de bron; geen complete catalogusdekking geclaimd.
- 32 exact-artikelgebonden specificatieaanvullingen: inbouwdeel/plug/sifon inbegrepen, kraansetuitvoering en stopfuncties, glasdikte/stelbereik, meubel zonder wastafel/blad en zonder sifon. Niet blind naar hele series/kleuren overgenomen; dealerprijzen/voorraad/levertijden niet gekopieerd.
- Vijf maatvelden zichtbaar op Te bevestigen gezet wegens drie bronconflicten: 5-CE-001 (hoogte, uitloophoogte, uitloopdiepte), 5-GG-001 (hoogte) en GS-OBI2B9030200CE (plaatsingsmaten).
- De aan 5-CE-001 en 5-GG-001 gekoppelde merk-PDF's zijn byte-identiek en tonen 148/68/115 mm; dealer meldt bij CE 165/85/104 mm, bij GG hoogte 158 mm. De tekening drukt geen artikel/revisie af: actuele leveranciersversie opvragen/controleren, geen bron stil als definitieve waarheid gekozen. Eerdere maatverschillen zijn dus niet simpel als werkelijke kleurverschillen bevestigd.
- De bronzen Oblivion-plaatsingsmaten bij de dealer wijken af van de eerder gelezen generieke GS-OBI2-handleiding. Catalogusmaat 90/30 blijft, nauwkeurige inbouwmaten blijven open tot de productgeneratie/tekening vaststaat.
- Exacte 5-CE-083-S2-65-tekening ondersteunt de 18,1–20,1cm-uitloopdiepte: totaal255 mm minus inbouw54–74 mm. Dit is montageafhankelijk en geen extra kort/lang-SKU-keuze; niet als inkortbaar gepresenteerd.

**Bewijs:** alle 876 voorbeeldrecords / 864 unieke artikelen door de werkelijke preview-JS met DOM-stub getest; 13.488 geldige en 1.489 geweigerde transities, 60 meubeltransities bewust onbeslist. Alle artikelen bereikbaar. Byte-exacte tijdelijke beelden, losse hendelbeelden, product-ID/SKU-bescherming en eerste-beeldgedrag bij toevoegen/append/herschikken/verwijderen PASS. Ook een afbeelding toegevoegd aan een voorheen fotoloos glasartikel: renderer volgt de nieuwe productdata zonder keuzefoto-codering. Afbeelding ontbreken beïnvloedt de SKU-combinatiegeldigheid niet. Bron-/specificatiecorrecties exact hersteld uit gedeelde paren. Fragment 740.487 bytes. Browserlayout/echte bediening en live Shopify-integratie NOT_TESTED.

[Bronsteekproef, bevindingen en mediacontract](brauer/2026-11-06/MEDIAKOPPELING_EN_STEEKPROEF.json). Geen bronbeeldbytes, volledige prijslijsten of privégegevens in publieke Git. Productbasis-XLSX versie 1 niet vervangen; deze data is een aanvullende exacte-SKU-overlay voor latere voorbereiding. MAIN read-only bevestigd als 196246372618 — BadkamerCity - Groene voorraadmelding. Geen Shopify-write, import (ook geen DRAFT), media-upload of themapublicatie. Alles wacht op het volledige aangekondigde leveranciersbeeld-/PDF-pakket en inventarisatie. Scratch is geen Git-werkboom; geen Windows-lokale statusclaim. Geen actieve schrijver na overdracht.

**Exact één volgende handeling:** de drie gevonden maatconflicten sluiten met de actuele artikelgebonden leveranciersdocumenten zodra het pakket binnen is. Daarna verrijking en eerste-afbeeldingadapter in de bestaande import-/UNPUBLISHED-reviewroute verwerken, inclusief nog geblokkeerde Liquid-validatie; geen vroege import.

## BRAUER-14 - visuele inbouwconfiguratie, hoogtemodellen en kleine maatkeuzes · 7 november 2026

Eigenaar merkt terecht op dat twee Galactic-breedtes geen dropdown nodig hebben; vraagt passende laag/verhoogd/hoog-groeperingen en echte eerste artikelfoto's voor inbouw-uitloop, rozetten/afdekplaat en bediening links/rechts. Onderzoek expliciet op BadkamerXXL gevraagd.

**Uitgevoerd, uitsluitend offline review:**
- Maatgroepen met twee of drie waarden tonen knoppen; grotere groepen blijven native dropdowns, één waarde wordt niet als keuze herhaald. Galactic heeft twee breedteknoppen. Zes kleuren plus Bekijk meer kleuren blijft.
- Opbouwgroep toegevoegd met 18 exact gecontroleerde Edition-basishendelartikelen: zes kleuren × laag / verhoogd / hoog met gebogen uitloop. Dit zijn passende bronuitvoeringen, geen universele samenvoeging van alle 001/002/003-hendelmodellen. Modelnamen en werkelijke artikelhoogte staan op de fotokeuzes en in de specificaties.
- Belangrijk: Verhoogd is hier 32,8 cm; de fabrikanttekening 5-CE-002_T.pdf is gedownload, gerenderd en visueel gelezen (328 mm). Hoog met gebogen uitloop staat bij deze zes dealerartikelen op 29,2 cm. Daarom niet hernoemd naar Middel of blind op benaming gesorteerd. Laag heeft per dealer-SKU 15,8 of 16,5 cm; waarden blijven artikelgebonden en moeten vóór import met het complete officiële documentpakket worden vergeleken. Geen maat van één kleur naar andere kleuren gekopieerd.
- Inbouwproef verdiept naar 40 Chrome Edition gladde uitvoeringen: vijf hendelvormen × twee uitlopen × twee wandafwerkingen × twee bedieningskanten. Alle 40 exacte fabrikant-SKU/EAN's en dealerkenmerken gecontroleerd. Binnen deze afgebakende proef: model A1–E1 / 004 = bediening rechts; A2–E2 / 083 = links. E1/E2 is Type 2, B1/B2 Type 5 etc. Tien codeboekregels opgeslagen; geen onbewezen universele decoder voor andere series/merken/kleuren.
- Eerste productgalerij-afbeelding van alle 58 artikelen afzonderlijk uit de artikelpagina vastgesteld. De keuzes tonen het eerste beeld van het **prospectieve exacte artikel bij behoud van de overige opties**, en de grote foto toont het gekozen artikel. Originele 480px-beelden bewaard voor analyse; het gesprek bevat ongewijzigde 200px-CDN-rendities van hetzelfde eerste bronbestand. Geen AI-beelden, omkleuring, spiegeling of generieke rozetten-/links-rechtsillustratie als artikelbeeld.
- Alle afbeeldingsbestanden byte/hash-gecontroleerd; vier representatieve artikelbeelden visueel ingezien (004 rechts, 083 links, rechte uitloop/afdekplaat, verhoogde opbouw). Bronpagina 5-s-001 gebruikt lowercase fabrikantnummer; alleen lettercase genormaliseerd naar het oorspronkelijke bron-SKU 5-S-001, EAN exact bevestigd.
- De foto-inbouwproef is expliciet chroom; Carving/Stripe en overige kleuren zijn niet als al gefotografeerd vrijgegeven. Het eerdere A1-kleurvoorbeeld staat nog in de vorige gesprekpreview, maar is in de nieuwe preview vervangen door de gerichte fotovergelijking.

**Bewijs/omvang:** 14 voorbeeldfamilies, 876 voorbeeldrecords / 864 unieke bron-SKU's (12 bewuste overlaprecords door de nieuwe basishoogtevergelijking naast bestaande losse kraanproeven). Werkelijke ingebedde JavaScript in VM/DOM-stub: alle 876 toestanden, 13.488 geldige transities, 1.489 ontbrekende transities geweigerd, 60 meubeltransities correct onbeslist. Alle artikelen bereikbaar. Foto per kandidaat-SKU en gekozen SKU, 58 fotobytes, 40 links/rechts-koppelingen, per-artikelhoogtes, prijs/EAN, kleine maatknoppen en zes-kleurenlimiet PASS. Specificatieparen gedeeld opgeslagen en voor weergave exact hersteld; reconstructie getest. Fragment 729.943 bytes. Browserlayout/echte native bediening/live PDP/cart NOT_TESTED (geen browserexecutable).

[Visuele configuratie: bron- en fotokoppelingen](brauer/2026-11-06/VISUELE_KRAANCONFIGURATIE.json) bevat de 58 publieke artikel-/fotobronverwijzingen, controles, codeboek en maatverschillen. Geen productprijzen, volledige private bronlijsten of derdenbeeldbytes naar publieke Git. Productbasis-XLSX versie 1 niet vervangen; verrijking blijft aanvullende reviewdata. Overige eerdere douche-/glas-/meubelvoorbeelden behouden.

MAIN read-only bevestigd als 196246372618 — BadkamerCity - Groene voorraadmelding. Geen Shopify-write, import (ook geen DRAFT), media-import, voorraadwijziging of themapublicatie. Alle import wacht op het volledige aangekondigde leveranciersbeeld-/PDF-pakket en inventarisatie; deze dealerfoto's tellen niet als volledige ontvangst of productiebeeldvrijgave. Scratch geen Git-werkboom; geen Windows-lokale statusclaim. Geen actieve schrijver na overdracht.

**Exact één volgende handeling:** eigenaar beoordeelt de 40 foto-opstellingen en de drie opbouwuitvoeringen met hun echte hoogtes. Daarna alleen bronbevestigde regels/foto's per volgende familie/kleur uitbreiden en de gemelde lage-kraanmaatverschillen met de officiële documenten sluiten.

## BRAUER-13 - dropdownmaten, zes kleurstalen en uitgebreide offline steekproef · 7 november 2026

Eigenaar wijzigt de eerdere kleurdropdownwens: toon zes kleuren op de productpagina en alleen bij meer dan zes een knop Bekijk meer kleuren. Afmetingen moeten een gewone nette dropdown krijgen. Nieuwe beoordeling gevraagd van andere glaswanden en verschillende wastafel-/badkranen.

**Uitgevoerd, alleen offline gesprekvoorbeeld:**
- Native dropdowns voor beschikbare breedte-/hoofddouchematen; ontbrekende combinaties blijven als uitgeschakelde opties zichtbaar. Een wijziging behoudt alle andere keuzes; ook een programmatig ongeldige selectiewijziging wordt teruggezet.
- Alle kleur-/decorgroepen tonen maximaal zes stalen. Bij meer dan zes: Bekijk meer kleuren / Minder kleuren; gekozen kleur blijft bij inklappen zichtbaar. Meubels tonen nu eveneens zes echte decorstalen, geen kleurdropdown. Standaard en ondiep blijven aparte meubelfamilies met de eerder 165 gecontroleerde maatrecords.
- Eén productkiezer met groepen Kranen, Glas en Meubels voorkomt dertien lange navigatieknoppen. Iedere voorbeeldfamilie bewaart de eigen selectie.
- Zes kraanproefgroepen: lage Edition 001 (32, met de bestaande vijf vormfoto's), hoge Edition draaibare uitloop model A (13, rond/plat), inbouwwastafelkraan model A1 (25, rechte/gebogen uitloop en rozetten/afdekplaat), opbouwbadkraanset (26, houder/handdouche), vrijstaande badkraan (14, handdouche), inbouwbadkraanset (52, badvulling/bediening/handdouche). De hoge/inbouw-wastafelproeven zijn expliciet afgebakend tot A/A1; geen universele modelcodevertaling of overdracht van 001-hendelfoto's naar andere modellen. Carving/Stripe en A2 zijn hier niet als bewezen gekoppelde opties toegevoegd.
- Drie andere glasfamilies: Oblivion standaard helder/brons (168; Flow apart gehouden), Orion helder/brons (36), Galactic tweedelige schuifnisdeur (12). Oblivion gebruikt de bestaande drie bovenaanzichten; de haakse GS-OBI2-opstelling is visueel tegen de officiële technische tekening gecontroleerd. Bronbreedtes van deze nieuwe glasproeven zijn catalogusmaten, geen gegokte plaatsingsmaten. Galactic-deurtype/omkeerbaarheid volgen de exacte prijslijst; de grote online PDF kon de webviewer niet openen en is niet als volledig gecontroleerde montagebron geclaimd.
- Eerdere Edition-doucheset (168), Void (132) en twee Joy-menu's (120/45) blijven beschikbaar. Totaal dertien families en 843 unieke bronartikelen. Geen volledige cartesische varianten aangemaakt. Het verschil tussen heldere/bronzen Oblivion-combinaties blijft werkelijk zichtbaar als grijze ontbrekende keuzes.

**Bewijs:** werkelijke ingebedde JavaScript met DOM-stub uitgevoerd: alle 843 artikeltoestanden, 13.141 geldige transities, 1.509 ontbrekende transities geweigerd en 60 meubeltransities correct onbeslist gelaten. Alle artikelen bereikbaar via geldige keuzes; artikel/EAN/btw-prijzen, native selectwaarden/disabled-opties, zes-stalenlimiet/uitklappen/actieve staal, statebehoud en exact-SKU-only verrijking gecontroleerd. Geen 16,5cm-kraanhoogte of andere eerdere HD1-verrijking gelekt naar andere kranen. Browserlayout/echte native dropdown-/touch-/toetsenbordbediening NOT_TESTED (geen browserexecutable); geen live Shopify/PDP/cart-test. Fragment 617.730 bytes, ingebedde bestaande beelden; geen netwerkafhankelijkheid in de preview.

[Steekproefcontract en tellingen](brauer/2026-11-06/UITGEBREIDE_STEEKPROEF_CONTRACT.json) bevat scope/controles zonder volledige private productlijsten of derdenbeelden. Data/bronafbakening blijven privaat voorbereid; productbasis-XLSX versie 1 niet vervangen. De voormalige BRAUER-11-kleurdropdown is hiermee als UI-voorstel vervangen; de maat-/SKU-koppelingen van BRAUER-12 blijven gelden.

MAIN read-only bevestigd als 196246372618, nu genaamd BadkamerCity - Groene voorraadmelding. Naamwijziging van andere sessie waargenomen; geen themafilewrite, publicatie of product-/voorraadwijziging door deze taak. Alle Shopify-import, ook DRAFT, blijft wachten op volledige aangekondigde media-/PDF-ontvangst en inventarisatie. Scratch geen lokale Git-werkboom; geen Windows-lokale status geclaimd. Geen actieve schrijver na overdracht.

**Exact één volgende handeling:** eigenaar probeert de uitgebreide steekproef, met aandacht voor afmetingdropdowns, kleurinklappen, hoge/inbouw-wastafeluitlopen, de drie badkraanroutes en de beperkte bronzen Oblivion-combinaties. Alleen daarna de beoordeelde groeperingsregels naar volgende bronfamilies uitbreiden.

## BRAUER-12 - aparte meubeldieptes, Breedte-labels en gecontroleerde afmetingen · 7 november 2026

Eigenaar vraagt de dieptekeuze te verwijderen en standaard/ondiep niet in hetzelfde menu te groeperen; Meubelmaat en Meubelmaat uit prijslijst worden Breedte. Breedte/diepte/hoogte en verdere specificaties aanvullen. De visuele glasopstellingen zijn door eigenaar positief beoordeeld. Eerst dit aangepaste voorbeeld beoordelen; pas daarna een nieuwe steekproef met verschillende productfamilies uit kranen, glas en meubels.

**Uitgevoerd in het offline voorbeeld:**
- Joy MFC opgesplitst in twee afgebakende families: 120 standaard artikelen en 45 ondiepe artikelen, ieder met eigen selectie. Geen diepte-as of dieptewissel binnen een menu. Bij ondiep vervalt ook de eenkeuzeknop voor twee lades; het aantal blijft als specificatie aanwezig.
- Het keuzelabel en de specificatie heten Breedte. Weergave gebruikt gecontroleerde buitenbreedte; bronmaatklasse blijft interne joinwaarde. Bijvoorbeeld bronklasse 120 → 119 cm; 140 → 138,8 cm. Artikelnummer/EAN/btw-prijs behouden.
- Per exacte SKU/EAN Breedte, Diepte, Hoogte en Montage toegevoegd; materiaal, ladeaantal, uitsparingen, greeploos, softclose en decor behouden. Alle 165 actuele dealerartikelregels gelezen en met de bronidentiteit vergeleken: nul mismatches. Standaarddiepte 455 mm, ondiep 386 mm, hoogte 500 mm; breedtes niet uit nominale artikelcodes gegokt.
- Drie getoonde fabrikanttekeningen visueel vergeleken: OK-JY80CH, OK-JY120-4CH en OK-JYO80CH. Dit is steekproefbewijs voor tekeningen, geen claim dat alle 165 officiële tekeningen zijn ontvangen/gecontroleerd. Overige verrijking is expliciet exacte dealer-SKU/EAN-data.
- De vijftien decorstalen, de afzonderlijke afvoerafstemming bij de ambigue standaard 119 cm / twee lades en de bestaande bescherming tegen stille andere keuzes blijven. Geen automatische wastafelcompatibiliteit afgeleid.
- Doucheset en glas: bronartikelen/inhoud ongewijzigd; dezelfde goedgekeurde glasdiagrammen en keuzelogica.

**Duurzame gegevens:** [Joy-maten en menucontract](brauer/2026-11-06/JOY_MATEN_MENUCONTRACT.json) bevat uitsluitend publieke maatfeiten, exacte bron-URL/hash en de menuregels; 165 records in elf geometriegroepen, in beide branches exact teruggelezen. Geen volledige prijslijsten, advies-/inkoopprijzen of derdenbeelden in deze Git-toevoeging. Productbasis-XLSX actueel gelezen als versie 1 en niet vervangen; deze gegevens zijn een aanvullende overlay voor de latere importvoorbereiding.

**Controle:** werkelijke ingebedde JavaScript in VM/DOM-stub: 465 toestanden, 8.070 geldige hoofdkeuzetransities, 696 ontbrekende combinaties geweigerd, 60 meubeltransities correct onbeslist tot afvoerkeuze. Alle 165 meubelafmetingen in de specificaties tegen exact-SKU-bronrecord gecontroleerd. Aparte selectiestaat voor beide meubelfamilies, geen diepteknop, zichtbare buitenbreedtes, artikel/EAN/prijzen, kleurdropdown/Escape/buitenklikhandlers en glasdiagrammen PASS. Browserlayout en echte touch/toetsenbordbediening NOT_TESTED; geen browserexecutable. Gesprekfragment 391.469 bytes; alleen review, geen Shopify-integratie.

MAIN opnieuw read-only bevestigd als 196246372618; geen Shopify-writes, import (ook geen DRAFT), media-import of publicatie. De beloofde complete leveranciersmedia/PDF-ontvangst blijft voorwaarde vóór alle import. Scratch is geen Git-werkboom; geen uitspraak over Windows-lokale status. Eerder gesprekvoorbeeld blijft beschikbaar als referentie/herstel. Geen actieve schrijver na overdracht.

**Exact één volgende handeling:** eigenaar beoordeelt dit aangepaste voorbeeld, inclusief de twee aparte Joy-menu's en de specificaties. Daarna volgt de gevraagde volgende steekproef met twee andere productfamilies per categorie (kranen, glas, meubels); deze nog niet als vervanging voor de eigenaarreview uitvoeren.

## BRAUER-11 - eenvoudiger meubelkeuze en visuele glasopstellingen · 7 november 2026

Eigenaar beoordeelt de doucheset positief, vindt het meubelmenu te technisch en vraagt om kleurdropdowns bij veel kleuren en plaatjes voor zijwanden. Alleen het offline gesprekvoorbeeld aangepast; geen Shopify-productimport (ook geen DRAFT), media-import, themawrite of publicatie.

**Voorstel ter beoordeling, niet al catalogusbreed goedgekeurd:**
- Joy MFC: 15 originele decorstalen met naam in een native uitklapmenu; selectie sluit het menu en brengt focus terug. Afzonderlijke assen voor meubelmaat, diepte en aantal lades. De oude gecombineerde lade-/sifonkeuze vervalt als primaire as.
- De afvoeruitsparing wordt automatisch afgeleid als exact één bronartikel bij de hoofdkeuzes hoort. Alleen standaard 120 cm / twee lades heeft twee bronuitvoeringen (één/twee uitsparingen); daar verschijnt een aparte uitklapbare afstemming op de wastafel. Bij zo'n nieuwe onbesliste combinatie GEEN definitief artikelnummer/EAN en alleen een vanafprijs uit de echte kandidaten. Geen stille artikelkeuze. Kleurwissels behouden een al gekozen afvoerindeling; andere gewijzigde hoofdkeuzes laten eventuele ambiguïteit opnieuw kiezen.
- Eindrichting is de juiste onderkast uit een gekozen wastafel afleiden. Daarvoor ontbreekt een bewezen compatibiliteitsmatrix. Aantal waskommen/afvoeren is niet geïmplementeerd als voldoende compatibiliteitsbewijs. Ook bij een unieke bronuitvoering blijft wastafelpassing te controleren.
- Void: drie klikbare bovenaanzichten (recht, zijwand maat 30, zijwand maat 40), schematisch en niet op schaal. Vaste haakse zijwand aan vrij einde geverifieerd met officiële BRAUER-handleiding (GS-VOI2, technische tekening/overzichtsbeeld). Links/rechts omkeerbaarheid niet als extra SKU-as toegevoegd. Breedte heet nu Breedtemaat: catalogusmaat niet gelijkstellen aan plaatsingsmaat.
- Edition-doucheset: dezelfde bronartikelen, prijzen en keuzemogelijkheden behouden.

**Bewijs:** uitgevoerd met de werkelijke ingebedde JavaScript in een VM met DOM-stub: alle 465 artikeltoestanden; 8.370 geldige hoofdkeuzetransities; 951 ontbrekende combinaties geweigerd; 60 meubeltransities correct onbeslist gelaten. Afvoerresolutie, artikel/EAN/btw-prijs, statebehoud, dropdownselectie/focus/Escape/buitenklikhandlers en grijze glasopties gecontroleerd. Ingebedde bronfamilies byte-inhoudelijk gelijk aan het voorgaande voorbeeld; 15 bestaande originele decorstalen behouden. Gesprekfragment 382.145 bytes. Browserlayout en echte toetsenbord-/touchbediening: **NOT_TESTED** (geen browserexecutable); dit is geen live webshoptest.

**Opslag/afbakening:** inline gesprekvoorbeeld, geen los websiteproject; volledige private artikeldata en derdenbeelden niet naar publieke Git gekopieerd. Bestaande productbasis-XLSX niet gewijzigd. Scratch is geen Git-werkboom; geen uitspraak over Windows-lokale status. MAIN vers read-only bevestigd als 196246372618 (BadkamerCity - Cottoceramix volledig assortiment). Centrale checkpoint in beide branches exact teruglezen. Eerdere previews blijven als herstel/referentie beschikbaar.

**Volgende handeling:** eigenaar beoordeelt dit vereenvoudigde gesprekvoorbeeld; daarna de wastafel-onderkastcompatibiliteit met officiële tekeningen vastleggen, binnen de bestaande importstop tot alle aangekondigde leveranciersbestanden zijn ontvangen/geïnventariseerd.

## BRAUER-10 - drie extra offline productfamilies met meerdere keuzes · 7 november 2026

Eigenaar bevestigt: niet-opgenomen combinaties blijven in de opties staan, grijs en niet aanklikbaar; geen stille wijziging van andere keuzes. Verzoek daarna: enkele extra producten proberen. Drie gesprekvoorbeelden voorbereid uit de actuele drie bronlijsten, met uitsluitend exact aanwezige SKU's:
- Edition thermostatische inbouwregendouche met stopkranen: 168 artikelen, vijf assen (kleur, hoofddouche 20/30 cm, rechte/gebogen wandarm of plafondarm, staaf/3-standen handdouche, met/zonder glijstang). Alle combinaties binnen deze afgebakende familie aanwezig. 24 Coffee-SKU's met bronbeschikbaarheid vanaf 1 februari 2027; geen actuele voorraadclaim.
- Void inloopdouche helder glas 200 cm hoog: 132 artikelen, beslagkleur × breedte 50–140 cm × zonder zijwand/30 cm/40 cm. Zijwanden komen alleen bij 90–140 cm voor in deze lijst. Losse wand en SKU-opstelling met zijwand blijven als bestaande verkoopartikelen gekoppeld; geen zelf samengestelde set.
- Joy onderkast uitsluitend MFC: 165 artikelen, vijftien decors × meubelmaat 60/80/100/120/140/160 × standaard/ondiep × drie bestaande lade-/sifonindelingen. Laden en uitsparingen vormen één leesbare indelingskeuze. Geen MDF-/eikenmodellen bijgemengd. Bronmaat als catalogusmaat behandeld; geen buitenmaten van andere SKU's overgenomen.

Generic keuzelogica bewaart andere opties en de eigen selectie per voorbeeld. Alle 465 toestanden, 8.370 geldige keuzeovergangen en 1.116 pogingen naar niet-opgenomen combinaties gecontroleerd. Alle artikelen bereikbaar via geldige één-optieovergangen; nul fouten. Prijsbasis onafhankelijk met Decimal 21%/centafronding tegen bestaande voorbereiding gecontroleerd. SKU/EAN/prijs, geen achterblijvende specs, kleuruitklappen en gekozen kleur zichtbaar bij inklappen gecontroleerd. Geen productimport of Shopify-integratie geclaimd. Browserlayout/live URL/cart niet getest.

Vijftien originele MFC-decorstalen van het [dealerkeuzemenu](https://www.badkamerxxl.nl/brauer-joy-onderkast-80-met-2-softclose-lades-greeploos-en-1-sifon-uitsparing-chateau-ok-jy80ch) in het gesprekvoorbeeld opgenomen, byte-exact gecontroleerd; drie representatieve stalen visueel ingezien. Metaalkleuren zijn duidelijk als indicatief gemarkeerd. [Doucheset-referentie](https://www.badkamerxxl.nl/brauer-chrome-edition-chrom-edition-unterputz-set-1-chroom-5-ce-024) alleen ter vergelijking; dealerprijzen/leverbeloften/onderdeelnummers niet toegevoegd aan deze bronvoorbeelden. Hoofdproductbeelden/PDF's niet toegevoegd of als ontvangen pakket geteld. Volledige data en analyse blijven privé, gesprekvoorbeelden zijn geen themacode-release. Productbasis-XLSX versie 1 ongewijzigd. MAIN read-only bevestigd als 196246372618; geen Shopify-writes/import/publicatie.

**Exact één volgende handeling:** eigenaar probeert de drie voorbeelden, met nadruk op Void breedte 80 cm tegenover 90 cm met zijwand en Joy standaard tegenover ondiep. Daarna pas deze bronafbakening per volgende familie uitbreiden. Alle import blijft wachten op volledige aangekondigde media-/PDF-ontvangst. Geen actieve schrijver na dit checkpoint.


## BRAUER-09 - echte hendelafbeeldingen in het offline keuzemenu · 7 november 2026

Eigenaar vraagt afbeeldingen op de hendelkeuzes. Vijf bestaande 147×147 JPEG-vormvoorbeelden uit het [BadkamerXXL-hendelmenu](https://www.badkamerxxl.nl/brauer-chrome-edition-wastafelmengkraan-opbouw-round-energy-saving-chroom-550001cs-hd1) gelezen en visueel beoordeeld. Mapping binnen uitsluitend deze 001-proeffamilie: A → type-1.jpg (lang/smal), B → type-5-1.jpg (kort/smal), C → type-3.jpg (breed/plat), D → type-4.jpg (smal/plat), E → type-2.jpg (dikkere greep). C/D ook in hun exacte dealerartikelvelden als Type 3/4 gecontroleerd; de eerdere fabrikant-SKU/EAN- en vormbeschrijvingen blijven de bronkoppeling. De beelden zijn ongewijzigd in het gesprekvoorbeeld opgenomen; geen AI-beelden, geen omkleuring en geen fabriekspakketvrijgave. E heet nu 'Dikkere greep' in plaats van 'Dik en rond', passend bij de concrete foto.

Keuzes tonen afbeelding plus begrijpelijke naam en actieve rand. Duidelijk gelabeld als vormvoorbeelden in chroom: zij wisselen niet naar de gekozen verkoopkleur. De aparte kleurkeuze, exacte artikelidentiteit, prijsbasis incl btw en bestaande combinatiebeperkingen blijven behouden. Originele leverancierbeelden/PDF's voor producten blijven af te wachten; niets aan productmedia in Shopify of productbasis-XLSX versie 1 toegevoegd.

Vijf ingebedde JPEGs byte-exact tegen gedownloade bron geverifieerd, lokale beelden visueel bekeken; alle 32 keuzestaten op label/artikel/EAN/prijs/selectie en ontbrekende combinaties gecontroleerd, nul fouten. HTML/IDs gecontroleerd. Browserlayout/live URL/cart niet getest. MAIN opnieuw read-only bevestigd als 196246372618. Geen Shopify-writes/import/publicatie.

**Exact één volgende handeling:** deze afbeelding-met-naam-opzet als offline voorbeeld beoordelen en vervolgens per volgende productfamilie alleen exact gecontroleerde keuzeafbeeldingen koppelen. De aangekondigde volledige mediaontvangst blijft voorwaarde vóór alle Shopify-import. Geen actieve schrijver na dit checkpoint.


## BRAUER-08 - begrijpelijke hendelnamen in het offline voorbeeld · 7 november 2026

Eigenaar wil herkenbare klantkeuzes in plaats van Model A/B of Type 1/2. Voor uitsluitend de lage Edition-wastafelkraan 001 zijn vijf productbeschrijvingen op exacte fabrikant-SKU en EAN vergeleken. Gekozen korte klantlabels: A Lang en smal (5-CE-001), B Kort en smal (5-CE-001-HD5), C Breed en plat (5-CE-001-HD3), D Smal en plat (5-CE-001-HD4), E Dik en rond (5-CE-001-HD1). A–D volgen de lange/korte/smalle/brede/platte dealerbeschrijvingen; E is verkort uit 'Middel dikke gladde hendel', met de ronde cilindrische vorm ook zichtbaar in de geraadpleegde technische tekening. Dit zijn eigen klantlabels, geen nieuw bevestigde fabrikantnamen of universele modelcodebetekenis.

Bronnen: [A](https://www.sanitairwinkel.nl/p/76190081/brauer-chrome-edition-lage-opbouw-wastafelmengkraan-model-a-chroom), [B](https://www.sawiday.be/nl-be/p/77155561/brauer-chrome-edition-lage-opbouw-wastafelmengkraan-model-b-chroom), [C](https://www.sanitairwinkel.nl/p/77155559/brauer-chrome-edition-lage-opbouw-wastafelmengkraan-model-c-chroom), [D](https://www.sanitairwinkel.nl/p/77155560/brauer-chrome-edition-lage-opbouw-wastafelmengkraan-model-d-chroom), [E](https://www.sawiday.be/nl-be/p/77155558/brauer-chrome-edition-lage-opbouw-wastafelmengkraan-model-e-chroom). E-tekening via eerder gevonden CDN-document noemt 5-GG-001-HD1; kleurafwijking zichtbaar behouden, niet vrijgegeven als document voor chroom. Alleen de vormherkenning gebruikt. Geen nieuwe dealerafmetingen overgenomen: die verschillen van eerdere dealerdata. De installatiehandleiding met drie verwijdertypes A/B/C is geen bewijs voor deze vijf verkoopmodellen.

Het gesprekvoorbeeld toont deze vormnamen in knoppen, titel en omschrijving. Fabrikantletter alleen als referentie in specificaties; interne SKU/handle/brondata blijven intact. Geen verzonnen hendelfoto's toegevoegd; eigen officiële mediapakket blijft af te wachten. Alle vijf labels en 32 keuzestaten gecontroleerd op artikel/EAN/prijs, broncodebehoud en geen overdracht van de twaalf eerdere technische velden naar andere SKU's: nul fouten. De bestaande keuzelogica is behouden. Browserlayout/live URL/cart niet opnieuw getest. Productbasis-XLSX versie 1 ongewijzigd. MAIN read-only bevestigd als 196246372618; geen Shopify-writes/import/publicatie.

**Exact één volgende handeling:** per volgende productfamilie de technische keuzecodes naar brononderbouwde klanttermen vertalen; vormfoto's pas koppelen zodra exact gecontroleerde officiële beelden beschikbaar zijn. Geen universele A/B-vertaling toepassen. Geen actieve schrijver na dit checkpoint.


## BRAUER-07 - offline voorbeeld met meerdere keuzeassen · 7 november 2026

Eigenaar verduidelijkt dat naast kleur ook andere opties nodig zijn. Het gesprekvoorbeeld is uitgebreid naar **Kleur + Hendelmodel** voor de lage Edition-opbouwkraan. Exact 32 bestaande bronartikelen met vijf modellen A–E en zeven kleuren; geen combinaties uit een volledig cartesisch product aangemaakt. Coffee komt in deze bron uitsluitend voor bij A en B (twee SKU's met bronbeschikbaarheid 1 februari 2027). Coffee/C–E zijn niet in de lijst opgenomen en blijven onselecteerbaar. Modelnaam uit de fabrikantlijst behouden; geen gegokte vertaling van A–E naar dealerhendeltypen. Carving en Stripe vallen buiten deze proef.

Kleurwissel behoudt het gekozen model, modelwissel behoudt de kleur. Ontbrekende combinaties zijn grijs; de andere keuze wordt nooit stil gewijzigd. Titel, artikelnummer, EAN, beschrijving en adviesbasis incl btw volgen de exacte SKU. De dealerverrijking uit BRAUER-06 blijft alleen op 5-CE-001-HD1; andere modellen/kleuren erven die maten niet. De geselecteerde kleur blijft zichtbaar bij inklappen. Dit is een offline menuvoorstel, geen technische compatibiliteitsvrijgave of winkelintegratie.

Alle 32 toestanden en 360 geldige keuzeovergangen gecontroleerd; 24 pogingen richting niet-opgenomen combinaties veilig afgewezen. Prijs/identiteit, behoud van de andere keuze, toekomstige bronbeschikbaarheid en verwijderen van achterblijvende specs gecontroleerd; nul fouten. Browserlayout/live URL/cart niet getest. Productbasis-XLSX versie 1 ongewijzigd. MAIN opnieuw read-only bevestigd als 196246372618. Geen Shopify-writes/import/publicatie. Alle aangekondigde officiële beelden/PDF's blijven af te wachten.

**Exact één volgende handeling:** dit model per productfamilie uitwerken naar bronbevestigde relevante opties voor kranen, glas en meubels, beginnend met één representatieve douchefamilie. Geen universeel menu of onbewezen setkoppelingen toepassen. Geen actieve schrijver na dit checkpoint.


## BRAUER-06 - offline Hotbath-menuvoorbeeld en gerichte verrijking · 7 november 2026

Eigenaar vraagt zichtbaar artikelnummer, Hotbath-opzet en één BadkamerXXL-proef. Voor het verrijkte voorbeeld is exact 5-CE-001-HD1 / EAN 4260483798535 gekoppeld aan [de dealerpagina](https://www.badkamerxxl.nl/brauer-chrome-edition-wastafelmengkraan-opbouw-round-energy-saving-chroom-550001cs-hd1). Fabrikantlijst noemt model E, dealer noemt hendel Type 2. Dealer-ID 899558 blijft uitsluitend bronidentificatie. Twaalf technische velden als dealerinformatie vastgelegd, alleen voor deze SKU: hoogte 16,5 cm, uitloophoogte 8,5 cm, diepte 10,4 cm, vaste I-uitloop, hendel Type 2/glad, 1-gats/eengreeps, aanvoer 1/2 inch, warm/koud, Brauer ColdStart. Niet als fabrikantbevestiging aangemerkt. De eerdere model-A-proef 5-CE-001 is hiermee niet technisch verrijkt.

Klikbaar gesprekvoorbeeld gebruikt de bestaande compacte Hotbath-opzet: ronde indicatieve kleurstalen, vier zichtbaar, alle zes uitklappen, actieve kleur zichtbaar bij inklappen. Zes echte model-E-kleurartikelen uit eigen bron; artikelnummer/titel/EAN/adviesbasis incl btw wisselen mee. Dealerprijs/voorraad/leverbeloften/reviews/garantie niet overgenomen; bronprijzen behouden. Niet-gecontroleerde kleuren krijgen de twaalf technische velden niet automatisch. Gevonden PDF-bronlink nog niet gekoppeld: documentdekking niet gecontroleerd (metadata noemt andere kleur).

Zes keuzestaten, prijs/identiteit en terugwisselen zonder achterblijvende specs getest; nul fouten. Geen browserlayout-/live product-/URL-/carttest en geen werkende Shopify-integratie geclaimd. Voorbeeld blijft gesprekspreview; productbasis-XLSX versie 1 ongewijzigd. MAIN read-only bevestigd als 196246372618. Geen Shopify-writes, import of publicatie. Volledig aangekondigd media-/PDF-pakket blijft af te wachten.

**Exact één volgende handeling:** eigenaar beoordeelt het offline Hotbath-menuvoorbeeld; daarna alleen exact gematchte dealerinformatie verder verrijken. Officiële bestanden en technische bevestiging blijven apart van deze bronproef. Geen actieve schrijver na dit checkpoint.


## BRAUER-05 - offline kleurrelaties voorbereid · 7 november 2026

13.161 exacte artikelidentiteiten in het koppelregister.1.355 kandidaatkleurfamilies met9.697SKU's;3.464SKU's afzonderlijk gehouden. Alleen gelijke bronmodeltekst na expliciet kleur-/afwerkingsverschil, met gelijk producttype/serie/uitvoering/materiaal, unieke kleur per kandidaatcombinatie. Alle27SKU's met materiaal-/afwerkingsconflict buiten groepen. Pilots bevestigen kleurrelatieCE001/GG001;20/30cm,Carving/Stripe,links/rechts en0/1kraangat blijven gescheiden. Relaties zijn wederzijds; geen technische compatibiliteit of leveranciersstuklijst afgeleid.

Productbasis uitgebreid met Koppelingen-tab. Exacte privérelaties blijven buiten publieke Git. Ontvangen media/PDF's:0; werkelijke mediakoppelingen:0; bevestigde onderdeelcompatibiliteit:0. Geen Shopify-writes/import, ook geenDRAFT. Volledige aangekondigde bestandenontvangst blijft harde voorwaarde vóór import.

Volgende handeling: kleurfamilievoorstellen gericht controleren en ontvangen afbeeldingen/PDF's later op exactSKU inventariseren/koppelen; ontbrekende technische onderdeelrelaties door leverancier laten bevestigen. Geen productpublicatievrijgave.


## BRAUER-04 - volledig offline productwerkbestand · 7 november 2026

Alle 13.161 SKU's in een aparte productbasis voorbereid: brongetrouwe opgeschoonde titels/omschrijving, unieke handlevoorstellen met SKU-suffix, producttypevoorstel, bronbevestigde specs, btw-prijsbasis, toekomstige datum, bronconflicten en vier lege aanvulkolommen. De 31 eerder inhoudelijk uitgewerkte voorbeelden blijven herkenbaar; de overige 13.130 omschrijvingen zijn bronbasis en geen volledig verrijkte tekst. Techniek/media nog aanvullen; 27 materiaalconflicten en twee afwerkingsvelden blijven open. Volledige gegevens blijven privé.

Geen enkele import, ook geen DRAFT, totdat alle aangekondigde beelden/PDF's/bestanden ontvangen en geïnventariseerd zijn. Geen Shopify-writes of kooptest. Volgende handeling: ontbrekende productdata in het werkbestand aanvullen en na ontvangst de media exact koppelen. Andere merken en eerdere werkzaamheden behouden.


## BRAUER-03 - productinhoud offline; alle import wacht op bestanden · 6 november 2026

**OFFLINE_CONTENT_PREPARED / ALL_IMPORT_PAUSED_BY_OWNER.** Jackson stelt expliciet: pas importeren wanneer alle afbeeldingen/PDF's en overige aangekondigde bestanden binnen zijn. Dit geldt ook voor DRAFT-pilots. Tot ontvangst en inventarisatie alleen offline inhoud/structuur/relaties/controles voorbereiden; geen Shopify-productwrite.

31proefartikelen nu inhoudelijk uitgewerkt: leesbare titels, handlevoorstellen, korte tekst, bronbevestigde specs, productrol en expliciete inhoud/uitsluitingen. Alle31 onafhankelijk inhoudelijk beoordeeld;646bronverwijzingen gecontroleerd, nul feitelijke verschillen na normale numerieke-/witruimtenotatievergelijking.31handlevoorstellen onderling uniek; volledige catalogus/URL-conflictcontrole nog open. Gewicht alleen nodig waar vervoerberekening het vereist; gedeelde officiële modelhandleiding toegestaan bij bewezen dekking; component-ID's nodig voor gekoppeld setblok, geen universele productpublicatievoorwaarde.27materiaalconflicten blijven open;2afwerkingsvelden vallen binnen diezelfdeSKU-groep.

[Productinhoud en gerichte aanlevering](brauer/2026-11-06/PRODUCTINHOUD.md) · [werkafspraken in plan](brauer/2026-11-06/PLAN_VAN_AANPAK.md) · [taken](brauer/2026-11-06/TAKEN.md). Volledige privéproductteksten/bronbewijs blijven buiten publieke Git. Excel uitgebreid met afzonderlijke Productteksten-tab; de bestaande13.161artikelen/prijzen en bronverschillen behouden. Geen nieuwe theme-/Admin-/collectie-/prijs-/voorraad-/publicatiewrites of browsercartproef.

**Exact één volgende handeling:** de31offlineinhoudsvoorstellen beoordelen en gerichte ontbrekende productinformatie aanvullen; compleet toegezegd mediapakket afwachten. Daarna pas inventariseren/koppelen en eerste conceptimport voorbereiden. Actieve codebranch blijft `fix/product-cards-2026-10-14`, themabron `shopify/current/`; andere merken/Cottoceramix behouden. Eerdere passages over vroege conceptimport zijn door deze eigenaarinstructie vervangen.


## BRAUER-02 - btw-prijsbasis, producttypen en proef uitgewerkt · 6 november 2026

**DATA_PREPARED / NO_SHOPIFY_WRITES.** Jackson bevestigt btw in de prijs en verdere uitwerking. Alle13.161adviesprijzen incl21% en consumentenbasis zonder aangenomen korting voorbereid. Decimal+onafhankelijke centcontrole; Excel26.322prijswaarden en469exactehalve-centgevallen gecontroleerd, nul afwijkingen. Bron ex btw behouden; `shop.taxesIncluded=true` vers bevestigd, geen belastinginstellingen gewijzigd.

Alle13.161SKU's hebben een producttypevoorstel; dit zijn geen nieuwe categoriepagina's of technische vrijgaven.36lichtlijsten/vijf ontbrekende groepvelden/vijf fout als handdoekbeugel getypeerde topbladbeugels/één haak-beugel-afwijking als brononderbouwde classificatievoorstellen;27materiaal- en2afwerkingsconflicten blijven open.227collecties en258PRODUCT-definities volledig gelezen; exacte bestaande doelen en echte hiaten vastgelegd.31proefartikelen technisch uitgewerkt, winkelbredeSKU- énEAN-zoekingangen nul matches voor die31; overige13.130nog niet gecontroleerd.

[Concrete uitwerking](brauer/2026-11-06/UITWERKING.md) · [velden/collecties](brauer/2026-11-06/VELDEN_EN_COLLECTIES.md) · [bijgewerkt plan](brauer/2026-11-06/PLAN_VAN_AANPAK.md) · [taken](brauer/2026-11-06/TAKEN.md). Actuele MAIN196246372618 read-only: Brauer valt op legacy-specs; generieke leverroute voor kaart/cart ontbreekt. Gerichte previewadapter en V2-dataset nodig; niets aan theme/Admin geschreven.31pilots krijgen eigen Excel-tab;163toekomstigeSKU's blijven gemarkeerd, geen actuele voorraadclaim. Ruwe bronnen/exports blijven privé.

**Exact één volgende handeling:** officiële productdata/media voor de31pilots koppelen en daarna de Brauer-preview met correcte specificaties/leverinformatie voorbereiden. Btw-keuze blokkeert dit niet meer. Geen productimport/publicatie/browsercartproef/feed uitgevoerd. Actieve branch `fix/product-cards-2026-10-14`, bron `shopify/current/`; Cottoceramix blijft apart. De BRAUER-01-prijsblokkade hieronder is het eerdere checkpoint.


## BRAUER-01 - brononderzoek en plan gereed · 6 november 2026

**SOURCE_AUDIT_COMPLETE / PLAN_REVIEW_PENDING / NO_SHOPIFY_WRITES.** Nieuwe eigenaarprioriteit: BRAUER voorbereiden voor volledige, gecontroleerde webshopuitrol. Drie bronnen: meubels8.687, kranen3.374, glas1.696; totaal13.757 bronregels, **13.161 exacte unieke SKU's**. 372 SKU's staan in meerdere bestanden (596 extra vermeldingen). 578 veldverschillen over371SKU's, waaronder27materiaal- en2afwerkingsconflicten; geen overlappende prijs-/EAN-conflicten. Alle EAN13-checkdigits geldig. **163 unieke artikelen** hebben beschikbaarheid vanaf1februari2027; geen actuele voorraadclaim.

[Plan van aanpak](brauer/2026-11-06/PLAN_VAN_AANPAK.md), [taken](brauer/2026-11-06/TAKEN.md), bronmanifest en veilige samenvatting gereed. Voorstel: één SKU per product, bestaande V2-selector/setblokken hergebruiken,31gevarieerde proefartikelen, daarna DRAFT-batches en vrijgave per geschikte deelgroep. Verkoopprijzen nog niet vastgesteld; alle bronnen geven adviesprijs ex btw. Brongegevens en complete exports blijven privé; deze Git is openbaar. Geen volledige XLSX-/mediaupload naar publieke Git.

Read-only Shopify: nul Brauer via vendorfilter en vrije zoekterm; volledige exacte SKU-botsingscontrole nog open. Verse rolmeting bevestigt **MAIN196246372618 - BadkamerCity - Cottoceramix volledig assortiment**. Dit bewijst geen nieuwe Cottoceramix-unitcarttest; oude publicatieblokkade hieronder is een historisch checkpoint. Geen BRAUER-import, theme-write, productpublicatie of browser-/cartproef. Bestaande Cottoceramix-openpunten blijven apart behouden.

**Exact één volgende handeling:** prijs-/publicatieafspraken voor de BRAUER-proef vastleggen, daarna categorie-/veldmapping. Foto's/PDF's volgen; bronvoorbereiding kan al door. Actuele codebranch blijft `fix/product-cards-2026-10-14`, themabron `shopify/current/`. Geen actieve schrijver na overdracht.


## COTTO-05 — m²-assortiment gepubliceerd; native units wachten op eigenaar · 5 november 2026

**PARTIALLY_PUBLISHED / BLOCKED_MERCHANT_THEME_AND_INDEX_LAG.** Verse eindcontrole bevestigt **3.159 ACTIVE en Webshop-gepubliceerde Cottoceramix-artikelen**. Er zijn 3.764 unieke Shopify-producten/varianten: 3.159 ACTIVE en 605 DRAFT, waarvan 597 native stuks-/pak-/setartikelen en acht bestaande bron-HOLDs. De broncheckpointset bevat 3.771 exacte SKU's; zes nieuwe afwerkingsconflicten en AD5917 zonder bruikbare foto zijn niet aangemaakt. Totaal 15 bron-HOLDs, geen extra unit-HOLD.

De 1.127 nieuwe strict-m²-artikelen slagen met 87.323 veld-/groep-/mediacontroles; alle 1.127 publicaties en publieke URL's teruggelezen. De 1.186 overige m²-artikelen slagen met 91.398 controles en daarna 9.489 nacontroles op exacte SKU-/product-/variantidentiteit, ACTIVE, Webshop en URL. Vier gerichte Malaga-handlecorrecties behouden de afzonderlijke punt-SKU's; nul uitsluitingen. De 854 bestaande producten zijn apart teruggelezen: 846 blijven ACTIVE/gepubliceerd met behouden handles/URL's; acht HOLDs blijven ongepubliceerd DRAFT.

Alle **597 native unitartikelen blijven DRAFT**. De actuele gecombineerde readback na de ene MC0031-onderhoudscorrectie slaagt: 41.740 hoofdcontroles en 21.297 onafhankelijke semantische controles, nul fouten; 1.182 beelden READY en 497 groepen exact. 134 gewichten bevestigd, 463 onbekende gewichten bewust weggelaten; geen m²-claims op de unitroute. MC0031 gebruikt de bestaande onderhoudscollectie; SKU, variant, prijs €39,95, bron-JSON, foto's en referenties behouden. De overige 596 unitrecords zijn exact ongewijzigd.

**Themapublicatie door eigenaar vereist:** MAIN **196238639370** heeft verse ongewijzigde metadata; de eerdere volledige vergelijking van alle 1.383 MAIN-baselinebestanden blijft behouden. Deze laatste ronde heeft de volledige preview opnieuw gelezen: **UNPUBLISHED196246372618 — BadkamerCity - Cottoceramix volledig assortiment**, 1.385 bestanden, exact 16 gewijzigde bestanden en twee nieuwe helpers. Alle **18** bedoelde bestanden komen exact overeen met de gevalideerde bronbytes; geen onverwachte afwijkingen. Geen themapublicatie door uitvoerder. Import-/unitcodebasis **916a431e180e28672b70feebc574ca345c6fbe80**; aanvullende beschikbaarheidslabelcorrectie **4976dd7ee56e9dd664e4e19198b6e2d852a46b2b**. Bron `shopify/current/`, vaste branch `fix/product-cards-2026-10-14`.

Echte conceptbrowser toont 3.159 producten, 24 kaarten, paginalink132 en geen overloop. Sweet Bars heeft acht geladen kleurkeuzen; Deep White→Royal Green bewaart 2,5m²+10% en rekent zeven dozen/€398,44. De native Cottoceramix-beschikbaarheidsfilter gebruikt nu **Bestelbaar / Niet bestelbaar**, passend bij Shopify-bestelbaarheid; leveranciersvoorraad en productdata zijn ongewijzigd. Vijf aanvullende themabestanden officieel gevalideerd, acht gerichte renderchecks en onafhankelijke review PASS. Echte desktopproef: Bestelbaar(3159)/Niet bestelbaar(0), aanvinken toont de correcte actieve chips, wissen herstelt nul chips/3.159 producten/24 kaarten. Mobiel en schermlezertekst zijn via fixtures gecontroleerd; geen nieuwe echte mobiele viewport- of cartproef.

De echte **unit-UI/cartproef blijft BLOCKED** doordat de gebruikte DRAFT-productpreview aan het oude MAIN-thema bleef gebonden; geen unit-koopbewijs of rendererfout geclaimd.

De openbare zoekdienst blijft bij de verse controle van 21:39:41 UTC gezond (HTTP200), consistente generatie **20261105T210044_bd0667**, met 1.973 Cottoceramix-resultaten. Het telverschil met het gepubliceerde totaal is 1.186; geen individuele ontbrekende-SKU-audit uitgevoerd. Geen timerstoring of verplichte reparatie bewezen; volledige zoekopname van 3.159 nog niet bevestigd. SSH/VPS-route vanuit deze uitvoering niet bereikbaar.

[Definitieve beperkte overdracht en publicatiegrens](cottoceramix/2026-11-05/full-catalog/README.md) · [Openbare verificatiesamenvatting](cottoceramix/2026-11-05/full-catalog/verification-summary.json). Geen automatische Cottoceramix-feed ingericht. Fysieke telefoon, adresafhankelijke verzending, checkout en betaling niet uit de Admin-/offlinetests afgeleid.

**Exact één volgende handeling:** eigenaar publiceert **BadkamerCity - Cottoceramix volledig assortiment (196246372618)**. Daarna verse MAIN-rol/hashcontrole, zes unitproefartikelen activeren en echte unit-/cartproef uitvoeren; alleen na PASS de overige 591 unitartikelen publiceren. Vervolgens indexopname opnieuw controleren en uitsluitend indien nodig de bestaande reguliere synchronisatie uitvoeren.

## COTTO-04 — tweede controle productkeuzes · 5 november 2026

**REVIEW_COMPLETE / VERIFIED_BROWSER / NO_STORE_WRITES.** Zeven live series getest: Funky, Re-Bel, Croccante, Zelij, Magnetism, Lula en Marea Alta Mat. In 26 vastgelegde browsertoestanden kloppen doosafronding en totaalbedrag; geen horizontale overloop bij desktopviewport1363×936. Kleur-, formaat-, foto-, titel-, verpakkings- en prijswissels werken in de geteste routes. In m²-modus blijven gewenste m² en snijverlies behouden; na handmatig dozen invoeren blijven juist de dozen behouden. Uit-/inklappen bewaart de gekozen kleur, ook bij Zelij met24kleuren.

Onafhankelijke selectiecontrole op824 gepubliceerde nieuwe producten/126families: **11.314 kernwissels**, geen ongewenste technische verandering door alleen een kleurwissel. Dit is een bron-/runtimecontrole, geen live browserklik op elk artikel. Veertig formaat→dikte-koppelingen zijn verwacht; Croccante60→80cm met9→10mm ook live bevestigd. De vier relevante componentbestanden zijn checksumgelijk aan MAIN **196238639370**;846 actieve Cottoceramix-artikelen bij begin en einde.

Geen functionele blokkade gevonden in deze steekproef. Verbeteringen geparkeerd: expliciete vormnamen bij onder meer Magnetism/Cottage, aparte uitvoeringnavigatie tussen model-/afwerkingsfamilies, bronkleurnamen bij Croccante normaliseren. Afrondingsverschillen van maximaal één cent in de afgeleide m²-prijs vragen geen prijsbatch. Eén laag geprioriteerde lifecycle-kwestie alleen in een verwijdertest gereproduceerd; geen fout in de normale productwissel bewezen. Geen product-/prijs-/voorraad-/theme-mutatie of publicatie.

[Uitgevoerde scenario's, beoordeling en grenzen](cottoceramix/2026-11-05/menu-review/README.md) · [Beperkte openbare verificatie](cottoceramix/2026-11-05/menu-review/verification.json). Fysieke telefoon, nieuwe cartactie, verzending, checkout/betaling en livefeed deze ronde **NOT_TESTED**. Geen actieve COTTO-04-schrijver na overdracht.

**Exact één volgende handeling binnen het cataloguswerk:** de al openstaande aparte stuks-/m¹-route voor onder meer Casablanca-randstukken en Enso als kleine volgende batch voorbereiden; bovenstaande UX-ideeën blijven apart van die import.

## LAUNCH-03 — eenmanszaakadres en retourlocatie apart bevestigd · 5 november 2026

**OWNER_CONFIRMED / DOCS_UPDATED / NOT_PUBLISHED.** Bedrijfsadres van de eenmanszaak blijft **Hengelolaan70,2545JR 's-Gravenhage**. Werk-/retourontvangstlocatie is **bij Harry Suiker, Zichtenburglaan150,2544EB 's-Gravenhage**. Eigenaar bevestigt de retourafspraak; postcode via officiële contactpagina gecontroleerd. Harry Suiker wordt niet de verkoper.

[Bedrijfsgegevens](livegang-seo/BEDRIJFSGEGEVENS.md), [retourconcept](livegang-seo/retouren/RETOURBELEID_CONCEPT.md), modelformulier, footerplan en taken bijgewerkt. **BC-LIVE-001A DONE**; eigen zakelijk telefoonnummer volgt later, geen Harry Suiker-nummer overnemen. Geen algemene vrije-inloop-/afhaalbelofte. Oudere LAUNCH-02-opmerkingen dat retouradres nog onbekend is, zijn hiermee historisch.

**Volgende handeling voor livegang:** volledig btw-id/juridische identiteit en retourkosten/raming voor grote goederen aanvullen; telefoon later zodra beschikbaar. Retourfunctie/mail-/publicatiecontroles blijven open. Geen Shopify- of Google-mutatie; andere actuele taken behouden.

## VERLAVIO-SET-01 — inbegrepen onderdelen douchesets · 5 november 2026

**APPLIED_VERIFIED / 78 SETS LIVE / 12 SOURCE_HOLDS.** De eigenaar vroeg dezelfde onderdelenweergave als Hotbath IBS70. 36 Milaan-,36 Palermo- en6 Porlezza-sets hebben nu462 bevestigde inbegrepen onderdelenregels uit108 losse Verlavio-artikelen. Uitsluitend156 waarden in de bestaande `bc_data.set_components` en `bc_data.component_products` toegevoegd; geen theme-writes of publicatie. MAIN blijft196238639370.

Alle78 bronpagina's exact opnieuw gecontroleerd; alle156 waarden teruggelezen in de volledige861-productinventaris, overige vastgelegde velden gelijk. Alle78 live productpagina's/462 regels PASS op aantallen, namen, SKU's, exacte variantlinks en prijzen. Desktopbrowser1363px bevestigt pilotCKK_2015. IBS70CR347 bleef exact gelijk met8 onderdelen; herhaling geeft0 writes. Mobiele browser en aankoop niet uitgevoerd.

[Uitvoering, grenzen en herstel](fabriecio/2026-11-05/set-components/README.md) · [Beperkte openbare verificatie](fabriecio/2026-11-05/set-components/verification.json). Twaalf Venetie-sets blijven zonder lijst wegens ontbrekend leveranciersbewijs. Volgende inhoudelijke handeling binnen deze scope: expliciete samenstelling voor deze twaalf opvragen/verkrijgen; niet raden. COTTO-03,LAUNCH-02 en overige lopende werkzaamheden hieronder blijven van kracht.

## LAUNCH-02 — bedrijfsgegevens,30dagenretourconcept en praktische controles · 5 november 2026

**OWNER_INPUT_RECORDED / DRAFT_READY / NOT_PUBLISHED.** Jackson levert bedrijfsadres/KvK/IBAN en kiest jaarrond30dagen retour. Opgenomen in [bedrijfsgegevens](livegang-seo/BEDRIJFSGEGEVENS.md); btw-id **NL00548932B64** mist in het opgegeven formaat één cijfer vóór B, telefoon/juridische handelsnaam en fysiek retouradres nog niet compleet. Geen cijfer of oude showroomgegevens gegokt. IBAN-checksum geldig, geen rekeninghouderschap of officiële KvK/VIES-koppeling geclaimd.

Eigen [retourconcept](livegang-seo/retouren/RETOURBELEID_CONCEPT.md) en leeg modelformulier voorbereid:30dagen melden, daarna14dagen terugsturen, geen novemberverlenging. Algemene uitsluiting “speciaal besteld” niet overgenomen; echt individueel maatwerk apart toetsen. Referentie is geen juridische bron; geen automatische50%-aftrek of algemene tegel-/douchewanduitsluiting. Retouradres en vooraf kenbare grote-retourkosten/raming nog aanvullen.

[Bestel-/contact-/retourchecks](livegang-seo/CONTROLES.md) maken het werk voor Jackson en uitvoering afzonderlijk afvinkbaar. Het native retourformulier toont paginasucces, maar een eigen directe bewaarbare klantmail is niet in de bron aangetroffen; werkelijke mailbox-/platformafhandeling nog testen. Herroepingsfunctie/ontvangstbevestiging en publicatie van het modelformulier staan expliciet open. Geen formulierinzending, order of betaling in deze taak uitgevoerd.

[Google-productcontrole in gewone taal](livegang-seo/GOOGLE_PRODUCTCONTROLE.md): bestaande data automatisch controleren, alleen uitzonderingen aan eigenaar voorleggen, geschikt assortiment niet laten wachten op ontbrekende beelden. Verlavio is publieke merknaam, Fabriecio blijft interne bron. Latere FAB-03/04-bewijzen vervangen het oude algemene koopbaarheidsprobleem; foto-/Google-vrijgave niet uit die proeven afleiden. Jackson werkt verder aan levertijden en foto’s; die taken niet als volledig getest afgevinkt. Lagoo-fotoverbod behouden.

[Universele-footerplan](livegang-seo/FOOTER_EN_BELEID.md): bestaande standaardfooter hergebruiken via footer-group/compact_homepage, volledige navigatiedekking bewaren; beide renderers tonen al shop.policies. Tijdens de read-only controle veranderde MAIN van196227170570 naar **196238639370 — BadkamerCity - Re-Bel tegelkeuze** door publicatie buiten deze uitvoering. Dit is geen schrijfbaar concept meer. Geen themefilewrite, policy-/product-/Google-instelling gewijzigd of thema gepubliceerd; COTTO/SEARCH-werk behouden.

**Exact één volgende handeling voor LAUNCH-02:** ontbrekend [gegevenspakket](livegang-seo/BEDRIJFSGEGEVENS.md) aanvullen: volledig btw-id/telefoon/juridische naam, bevestigd Nederlands retouradres en grote-retourkosten/raming. Daarna het al voorbereide beleid en de bestaande footerroute gericht afronden. [Bijgewerkte taken](livegang-seo/TAKEN.md) · [logboek](livegang-seo/LOGBOEK.md). Geen actieve LAUNCH-02-schrijver na overdracht.

## COTTO-03 — eerste grote catalogusbatch gepubliceerd · 5 november 2026

**PUBLISHED_VERIFIED / NEXT_BATCHES_OPEN.** Op expliciete opdracht 832 nieuwe Cottoceramix-artikelen aangemaakt; exact **824 ACTIVE én op Webshop gepubliceerd**, acht bronconflicten DRAFT/niet gepubliceerd. Alle 832 status-/kanaalwaarden onafhankelijk teruggelezen: nul afwijkingen. De 22 Re-Bel-artikelen zijn op ID/titel/vendor/handle/status/variant/prijs/mediareferenties onveranderd. Shopify telt nu **846 actieve Cottoceramix-artikelen**. Uit de gecorrigeerde werkset van 3.770 resteren **2.916 nog niet aangemaakte** artikelen; samples/vervallen artikelen en drie extra nieuwe feedrecords blijven apart.

126 nieuwe coherente kleurfamilies gebruiken de bestaande vierkante keuze. Bronmodellen/afwerkingen/formaten zijn waar nodig gesplitst; geen claim dat elk leveranciersmenu exact is gekopieerd of alle families één gezamenlijke selector hebben. Groepsreferenties volledig gelezen en correct. De gekozen Z/AA-maat en AF-dikte gaan vóór oude AB/AC/AE-waarden; een gevonden mapperfout is vóór verdere publicatie hersteld. Vijftien originele bronfoto's met octet-stream-header ongewijzigd als JPEG aangeleverd en gekoppeld; **2.705 beelden READY** over de 832 nieuwe artikelen.

**Bewijs:** gefaseerde volledige veld-/groeps-/fotoreadback, **64.900 controles PASS**; 29 script-/regressietests PASS. Live Chrome Funky: twaalf kleuren, Amber→Seaport, juiste prijs en 10m²+10%=14dozen/€1.234,24. Twee dozen daadwerkelijk toegevoegd: 1,68m²/€176,32, juiste per-dooslabels; eigen regel verwijderd, cart leeg. Monaco-R: vijf kleuren, Beige→Verde, €79,95/m² en €102,34/doos/1,28m². Fysieke telefoon, adresafhankelijke verzending, checkout/betaling en Google-/zoekindexopname deze ronde NOT_TESTED.

De eigenaar heeft het vorige concept gepubliceerd: **MAIN196238639370 — BadkamerCity - Re-Bel tegelkeuze**. De drie kleurcomponenthashes ongewijzigd bevestigd. Geen themabestand geschreven of thema gepubliceerd in COTTO-03; andere merken behouden. Algemene bulkmutaties geblokkeerd door de connector; begrensde toegestane API-batches gebruikt. Geen automatische Cottoceramix-feed of importworker ingericht.

Codecheckpoint **fdac6c95fbfbb751c9f18bffe5b35531acb8aca0**, bron `shopify/current/`, vaste branch `fix/product-cards-2026-10-14`. [Batch, gegevenscontract, bewijs en herstel](cottoceramix/2026-11-05/rollout/README.md). Geen actieve COTTO-03-schrijver na overdracht.

**Exact één volgende handeling voor COTTO-03:** aparte stuks-/m¹-route voor onder meer Casablanca-randstukken en Enso als volgende kleine batch voorbereiden; daarna bronconflicten/ontbrekende waarden gericht oplossen. Geen huidige batch opnieuw aanmaken of bestaande SKU's blind upserten. Oudere COTTO-02-publicatiestatus hieronder is geschiedenis.
## COTTO-02 — Cottoceramix en uitklapbare tegelkleuren gereed · 5 november 2026

**ADMIN_APPLIED_VERIFIED / PREVIEW_VERIFIED / AWAITING_MERCHANT_PUBLICATION.** Alle 22 bestaande Re-Bel-artikelen hebben Cottoceramix als vendor, titelvoorvoegsel en zichtbaar Merk; beschrijving, SEO en 70 afbeeldings-altwaarden aangepast. Volledige voor-/navergelijking: nul afwijkingen van plan; identiteiten, URL's, publicaties, doos-/m²-prijzen, verpakking, gewicht, voorraadbeleid en fotoreferenties behouden.

Het bestaande concept toont vier vierkante tegelfoto's inclusief de gekozen kleur; “Bekijk alle 11 kleuren” / +7 opent de volledige vierkolomskeuze. Open toestand blijft bij productwissels bewaard. Opt-in via `tiles.color_picker_layout="expandable_grid"`; overige tegelgroepen behouden de rail. Zes nieuwe semantische kleurchecks en zeven bestaande pilotchecks PASS; drie productbestanden en de neutrale QA-template door Liquid-validator goedgekeurd. Echte Chrome: uit-/inklappen, alle elf foto's, Blanc→Perle en 60→100 cm met behoud van de andere keuze; componentkaders 320/390 CSS-pixels zonder overloop. Fysieke telefoon, volledige mobiele PDP en checkout/betaling deze ronde NOT_TESTED.

**Thema's:** MAIN **196227170570** is volledig 1381/1381 checksumgelijk gebleven. Alleen **UNPUBLISHED196238639370 — BadkamerCity - Re-Bel tegelkeuze** bevat het nieuwe menu. Finale inventaris: 1383 bestanden, elf verschillen tegenover MAIN — vier eerdere cartfiles, drie nieuwe productcomponentfiles, één inactieve neutrale QA-template en drie laatste SEARCH-01-files. De parallelle zoekpatch `05a54c8d8b7df8c41644eec7abd5bd812a3cb6d5` behouden; oude COTTO-01-zoekhash is niet langer de huidige zoekbaseline. COTTO-02 heeft geen backendindex gewijzigd en publiceert geen thema.

Codecheckpoint **cb55eb45f1e32f9044a3b91279e0c41aa1b7c410**, vaste branch `fix/product-cards-2026-10-14`, bron `shopify/current/`. [Gegevens, menucontract, bewijs en herstel](cottoceramix/2026-11-05/rebel/brand-colors.md). Geen actieve COTTO-02-schrijver na overdracht.

**Exact één volgende handeling voor COTTO-02:** eigenaar beoordeelt en publiceert **BadkamerCity - Re-Bel tegelkeuze**; daarna verse MAIN-rol en publieke merk-/kleurenweergave controleren. SEARCH-01 en verdere import blijven afzonderlijk. De COTTO-01-merk-/menubeschrijving hieronder is het vorige checkpoint.
## COTTO-01 — Re-Bel live; winkelwagencorrectie gereed voor eigenaarspublicatie · 5 november 2026

**PRODUCTS_LIVE_VERIFIED / CART_PREVIEW_VERIFIED / AWAITING_MERCHANT_PUBLICATION.** Exact 22 nieuwe Revoir Paris Re-Bel-artikelen ACTIVE en gepubliceerd op de Webshop: 11 kleuren × 60×60/100×100 cm. Gedeeld kleur-/formaatmenu, native m²-eenheidsprijzen, juiste doosprijzen, dozen als bestelaantal, 70 afbeeldingen READY, volledige specificaties en gewichten gecontroleerd. Actuele XML gebruikt; vijf voorraadverschillen tegenover Excel verwerkt. EAN RR6011 heeft een onjuist controlecijfer en is niet als barcode gepubliceerd. [Uitvoering, productregister, hergebruik en herstel](cottoceramix/2026-11-05/rebel/README.md).

**VERIFIED_ADMIN / VERIFIED_BROWSER.** Alle 22 productveldsets, 22 groepslijsten met elk 22 referenties en Webshoppublicaties teruggelezen. Live kleur/maat wisselt met behoud van de andere keuze; 10 m² + 10% geeft 8 dozen/11,52 m²/€794,32 bij 60 cm of 6 dozen/12 m²/€959,40 bij 100 cm. Ongeldige invoer blokkeert bestellen. Live en preview elk drie dozen werkelijk toegevoegd voor €297,87; alleen eigen testregel verwijderd, cart leeg. Previewbevestiging én cart tonen nu “per doos”, de juiste leveranciersleverinformatie en €68,95/m². Toolkit 5/5 (gecombineerde revisie 2) en zeven lokale render-/matrixchecks PASS. Fysieke mobiel, adresafhankelijke verzending, checkout en betaling NOT_TESTED. Automatische Cottoceramix-feedverversing is niet ingericht. Echte zoekproef op RR6001 en Re-Bel geeft nog nul; zoekvindbaarheid van deze nieuwe serie blijft OPEN bij het aparte indexherstel, zonder veronderstelde oorzaak.

**Rollen en scope:** MAIN **196227170570 — BadkamerCity - Verlavio voorraad en levertijd** is 1381/1381 behouden. Nieuw UNPUBLISHED **196238639370 — BadkamerCity - Re-Bel tegelkeuze** was vooraf 1381/1381 identiek en heeft finaal 1382 bestanden met exact vijf bedoelde afwijkingen: de vier winkelwagenbestanden en de al gecontroleerde zoekbescherming uit SEARCH-01. Geen themapublicatie door uitvoerder; producten zijn al live, winkelwagencorrectie alleen in dit concept. Branch `fix/product-cards-2026-10-14`, bron `shopify/current/`. Andere merken, instellingen en de Lagoo-foto-instructie behouden. De oudere FAB-04-overdracht hieronder dateert van vóór de inmiddels waargenomen eigenaarspublicatie van het Verlavio-voorraadthema.

**Integratie SEARCH-01:** het byte-identieke zoekbestand (MD5 `e0783b4ed15e1acc70ff1518cf2b5f20`) uit concept196116087050 is in dit COTTO-concept overgenomen. De bestaande 23 runtimechecks slagen ook hier. Publiceer alleen het gecombineerde COTTO-concept; het losse zoekconcept mist de vier winkelwagenbestanden en mag daarna niet als latere release gebruikt worden. Backendindex/SSH zijn niet gewijzigd.

**Geen actieve COTTO-01-schrijver of feedworker. Exact één volgende handeling:** eigenaar beoordeelt Re-Bel en publiceert **BadkamerCity - Re-Bel tegelkeuze** in Shopify. Daarna verse MAIN-rol en de gepubliceerde winkelwagenlabels controleren, vóór verdere import.

## SEARCH-01 — index en prijsweergave live; afgerond · 5 november 2026

**OWNER_PUBLISHED / INDEX_LIVE_VERIFIED / UI_LIVE_VERIFIED.** Eigenaar heeft het gecombineerde thema gepubliceerd: **MAIN 196238639370 — BadkamerCity - Re-Bel tegelkeuze**; voorraadthema 196227170570 is UNPUBLISHED. Alle drie live prijsbestanden zijn checksum-exact teruggelezen. De eerdere COTTO-publicatieverzoeken zijn gedateerde checkpoints; geen resterende publicatiestap.

Momentopname van de gecontroleerde indexgeneratie op 5 november rond 18:07 UTC; latere COTTO-03-imports vallen buiten deze meting en vereisen een volgende geslaagde reguliere synchronisatieronde.

De volledige index `bc_sync_20261105t180750_9caf43` is live: 226 profielen, 12.760 globaal / 12.018 shopping, Verlavio 851, Re-Bel 22, RR6001 exact Cottoceramix, beide Nesso-SKU's exact op hetzelfde product met minimum 7800 / price_varies=true/geen Lagoo-afbeelding, Hotbath 7.540 en echte nul voor onzin. Generatieheader gelijk in alle gecontroleerde antwoorden; installercontroles en onafhankelijke publieke nacontrole PASS.

Echte Chrome zonder preview: Verlavio 851 producten / 24 externe kaarten / 0 native / geen foutbanner. Ná themapublicatie via echte header N8271TC + Enter: **één product/één externe Nesso-kaart, “Vanaf € 78,00”, geen foutbanner**. De SKU-alias en nieuwe kaartprijsweergave werken op MAIN.

**SEARCH-01 afgerond; geen server- of publicatiehandeling nodig. Installer niet opnieuw uitvoeren.** De bestaande uurlijkse timer is hervat; een volgende toekomstige uitvoering is nog niet waargenomen. Geen nieuwe automatisering, leveranciersfeedclaim of Shopify-datawijziging. [Eindbewijs en grenzen](search-index/2026-11-05/README.md). COTTO-historie behouden; geen actieve SEARCH-01-schrijver.

**Publicatie-afstemming COTTO-01:** de oorspronkelijke zoekbescherming (historisch controlepunt MD5 `e0783b4ed15e1acc70ff1518cf2b5f20`, vóór de prijsuitbreiding met concept-JS `11de150d3e2797a6f35742a813281fcb`) is meegenomen in **UNPUBLISHED 196238639370 — BadkamerCity - Re-Bel tegelkeuze**, samen met de vier COTTO-winkelwagenbestanden. Eigen 23 runtimechecks en gecombineerde 5/5 validatie PASS. Publiceer alleen dit gecombineerde concept. Het losse zoekconcept 196116087050 mist de winkelwagenwijzigingen en mag daarna niet als latere release worden gebruikt. De nieuwe publieke index vindt Re-Bel 22 en RR6001 als exact Cottoceramix-artikel.

## FAB-04 — historisch checkpoint vóór eigenaarspublicatie: koopbaarheid hersteld · 5 november 2026

**BACKEND_APPLIED_VERIFIED / PREVIEW_VERIFIED / COPY_AWAITING_MERCHANT_PUBLICATION.** De winkel gebruikt Market-driven verzending. De werkelijke Nederlandse verzendoptie bevatte alleen de winkellocatie. Uitsluitend de Verlavio-leverancierslocatie is als oorsprong toegevoegd. Volledige voor-/navergelijking: alleen die toevoeging; bestaande tarief-ID's, €6,95, gratis-verzendingdrempel €100,01 en andere Markets gelijk.

**Volledige readback PASS, 16:37:57 UTC:** alle 861 producten, nul afwijkingen. Exact 29 gewijzigde echte aantallen met CAS uit de feed bijgewerkt; 118 lege aantallen niet verzonnen. De 84 actieve Y-artikelen met leeg aantal behouden CONTINUE/nul; overige voorraadregels DENY. ID's, titels, handles, SKU's, prijzen, tracking, beleid, status en overige locatievoorraad/-velden behouden; 851 ACTIVE / 10 ARCHIVED. Zes bronconflicten op aanvraag; bestaande portalweek 50 behouden waar de feed week 28 meldt.

Publieke eindcontrole 16:31:19 UTC: drie voorraadproducten beschikbaar/InStock met actieve koopknop; nulvoorraadvoorbeeld niet beschikbaar/OutOfStock met week 50; conflict zonder bevestigde voorraadbelofte. Echte Chrome-preview: VSB_2001 met “Op voorraad / Levertijd: 1–2 werkdagen” succesvol toegevoegd via de winkelwagenknop; alleen eigen testregel verwijderd, eindcart nul. Mat Wit navigeert naar VSB_2003 met week 50 en uitgeschakelde knop; GM_3001 toont “Voorraad en levertijd op aanvraag”. Geen checkout-/betalingstest of fysieke telefoon.

MAIN **196116087050** blijft ongeschreven. **UNPUBLISHED196227170570 — BadkamerCity - Verlavio voorraad en levertijd**: vóór wijziging 1.381/1.381 identiek aan MAIN, finaal exact drie bestanden gewijzigd (leveringssnippet en NL/EN-vertaling), alle hashes teruggelezen. 23 leveringsgevallen, 16 menu-/URL-overgangen en drie Liquidvalidaties geldig. De 1–2 werkdagen is winkelbeleid voor de 774 bevestigde actieve Y-artikelen zonder conflict; dit staat niet als apart levertijdveld in de feed. De 71 N-artikelen en zes conflicten volgen hun eigen status.

**Exact één volgende handeling:** eigenaar publiceert **BadkamerCity - Verlavio voorraad en levertijd (196227170570)**; daarna MAIN-rol en drie publieke leverstatussen teruglezen. Geen actieve FAB-04-schrijver of feedworker na overdracht; de aparte COTTO-01-prioriteit hierboven blijft behouden. [Voorraad, oorzaak, herstel en bewijsgrenzen](fabriecio/2026-11-05/stock/README.md). Zes leveranciersconflicten, 53 bronmenu-uitzonderingen en merkenoverzicht blijven open; geen automatische feed of vijfminutenverversing ingericht. FAB-03 hieronder is het gedateerde rebrandcheckpoint; het toenmalige koopbaarheidsonderzoek is door FAB-04 afgerond.

## FAB-03 — historisch rebrandcheckpoint: Verlavio live en volledig gecontroleerd · 5 november 2026

**APPLIED_VERIFIED / MERCHANT_PUBLISHED.** De eigenaar heeft **BadkamerCity - Verlavio merknaam** gepubliceerd. Verse Shopify-controle bevestigt **MAIN 196116087050**; voormalig MAIN 196227170570 is UNPUBLISHED. Alle drie gepubliceerde compatibiliteitsbestanden zijn checksum-exact gecontroleerd. Geen MAIN-filewrite of publicatie door de uitvoerder.

Alle **861 bestaande producten** hebben nu merk Verlavio, de bijbehorende producttitel en exacte merk-tag. **665 keuzemenutitels** en **1.665 afbeeldings-altwaarden** zijn omgezet. Volledige read-after-writecontrole op 15:51:12 UTC: exact gelijk aan het uitvoerplan, nul afwijkingen; eindtelling **861 Verlavio / 0 Fabriecio**. Status blijft 851 ACTIVE / 10 ARCHIVED. Product-/variant-ID's, handles/URL's, SKU's, prijzen, voorraad/-beleid, mediareferenties/-URL's, omschrijvingen, SEO en levering zijn gelijk aan de nulmeting. Menuopbouw, opties en bestemmingen blijven behouden; interne leveranciersvelden en bron-/importtags blijven Fabriecio.

**PASS:** eerst vier Malmö-producten als proef; daarna de volledige catalogusvergelijking. Publieke eindcontrole op 15:49:20 UTC: VSB_2001, VSB_2004 en BKK_1001 geven HTTP 200 met Verlavio in H1, JSON-LD Brand, alle menutitels en productafbeelding-alt; menu's aanwezig. Vooraf alle 665 menu's onder Verlavio getest: 5.425 keuzecontroles / 4.096 URL-wissels / nul fouten. Geen nieuwe fysieke telefoon-, cart-, checkout- of betalingstest.

Het bestaande Uitverkocht-probleem en 53 bronuitzonderingen blijven open; automatische feedkoppeling blijft uitgesteld. De merknaamwijziging bewijst geen koopbaarheid. Verlavio ontbreekt nog in het merkenoverzicht, net zoals Fabriecio daar voordien ontbrak; een eventuele toevoeging is afzonderlijk themawerk.

**Exact één volgende handeling:** de bestaande Uitverkocht-/koopbaarheidsafwijking gericht onderzoeken met een product dat volgens Admin voorraad heeft. Geen merkdatabatches of publicatie meer nodig. Geen actieve schrijver of feedworker na overdracht. [Uitvoering, herstel en testgrenzen](fabriecio/2026-11-05/verlavio/README.md). De FAB-01/FAB-02-blokken hieronder zijn historische checkpoints; hun publicatie-/nulproductclaims zijn niet de huidige status.

## FAB-02 — historisch checkpoint: Verlavio private label voorbereid · 5 november 2026

**AWAITING_MERCHANT_PUBLICATION / PRODUCT_REBRAND_NOT_APPLIED.** Eigenaar wil merk **Verlavio**. Fabriecio blijft intern de leverancier. Verse rollen: **196227170570 is nu MAIN**; eigenaar heeft het vorige concept gepubliceerd. Alleen vendor wijzigen zou de665menu's verbergen. Daarom compatibel concept **UNPUBLISHED196116087050 — BadkamerCity - Verlavio merknaam** gereedgemaakt: eerst zes verschillen exact vanuit MAIN overgenomen, daarna drie files ondersteunen beide merknamen. Alle drie hashes teruggelezen; MAIN niet geschreven.

**PASS:**18Python-tests,16brand/productwissels,12leveringsgevallen,5425keuzecontroles/4096URL-wissels met Verlavio,3Liquidfiles geldig. Privéplan:861merk/titelwijzigingen,665menutitels,1665imagealtwaarden. Actueel nog **861Fabriecio / 0Verlavio**; niets als gewijzigd claimen. Leverancierssleutels en bestaandeURL's/SKU's blijven behouden. De53bronuitzonderingenenhetbestaandeUitverkocht-probleemblijvenopen.

**Exact één volgende handeling:** eigenaar publiceert **BadkamerCity - Verlavio merknaam**. Daarna actueleMAIN/hashcontrole en de voorbereide merkdatamutaties met teruglezing uitvoeren. De Shopify-koppeling staat codewrites alleen in concept toe. Geen actieve schrijver na overdracht. [Uitvoering en hervatten](fabriecio/2026-11-05/verlavio/README.md).

## FAB-01 — historisch checkpoint: Fabriecio productkeuzes en levering in concept · 5 november 2026

**VERIFIED_ADMIN / PREVIEW_VERIFIED / OWNER_REVIEW_PENDING / NOT_PUBLISHED.** Alle 861 Fabriecio-bronartikelen exact aan bestaande Shopify-SKU's gekoppeld. Op 851 actieve artikelen zijn 1.516 nieuwe velden opgeslagen en exact teruggelezen: 665 keuzemenu's en 851 leverinformatie. Prijs, voorraad, status, SKU/variant-ID, handle en featuredMedia onveranderd. Tien gearchiveerde artikelen overgeslagen; 132 actieve artikelen hebben geen bronmenu, één heeft alleen een gearchiveerde tegenhanger. Twee families/53 artikelen blijven op HOLD wegens 26 bronlinks die ongemerkt ook een andere maat/kleur wijzigen.

UNPUBLISHED **196227170570 — BadkamerCity - Fabriecio productkeuzes** is eerst 1.378/1.378 identiek aan MAIN **196116087050** gemaakt. Daarna exact zes featurepaden: twee snippets, main-product, twee locales en een geneutraliseerde ongebruikte QA-template. MAIN 1.378/1.378 ongewijzigd. Geen publicatie. Actuele bron: **shopify/current/** op **fix/product-cards-2026-10-14**, codecheckpoint **ab312b8f3685de23fb34166c307d680d284869e4**.

**PASS:** 17 Python-tests, 5.425 werkelijke Liquid/JS-keuzecontroles/4.096 URL-wissels; native Chrome Malmö-wissels met behoud van kleur/maat, juiste prijs/Week50 en geladen swatches; 320/390 CSS-pixelcomponenten zonder overloop; zes ThemeCheck-files geldig. Fysieke telefoon/cart/checkout niet vrijgegeven. De bestaande publieke Uitverkocht-blokkade blijft open; automatische feedkoppeling is uitgesteld. Limiet256metafielddefinities behouden; twee nieuwe ongestructureerde JSON-velden zonder bestaande definities te verwijderen.

[Uitvoering, herstel en grenzen](fabriecio/2026-11-05/product-choices/README.md) · [getelde verificatie](fabriecio/2026-11-05/product-choices/verification.json).

**Exact één volgende handeling:** Jackson bekijkt het concept **BadkamerCity - Fabriecio productkeuzes**, te beginnen bij Malmö. Geen actieve schrijver na overdracht. Andere dossiers en het Lagoo-fotoverbod blijven behouden.

## LAUNCH-01 — vast dossier voor livegang, Google en SEO · 5 november 2026

**DOCUMENTATION_READY / READ_ONLY_BASELINE / SETUP_NOT_EXECUTED.** Eigenaar wil bestaande verkoopklare producten nu vindbaar maken en het assortiment daarna uitbreiden. Vast dossier [Livegang & SEO](livegang-seo/README.md) aangemaakt: [taken/acceptatie](livegang-seo/TAKEN.md), webshopbasis, account-/gegevensstromen, Search Console, Merchant Center, GA4/privacy, SEO-roadmap, paginaregister, volledig niet-product-URL-register en logboek.

Verse Shopify-read: MAIN **196116087050**, hoofdadres HTTPS badkamercity.nl, NL, taxesIncluded=true; zeven app-installaties volledig gelezen, Google & YouTube niet aangetroffen. Alleen standaard privacybeleid ingevuld; standaard refund/terms/shipping-URL's geven404. Retourformulier en Contact zijn publiek200; ontvangst en volledige bedrijfsinformatie niet bewezen. Homepage mist meta description. Alle17kind-sitemaps gelezen: **11.887unieke product-URL's**,225collecties,119Pages,éénblog,éénartikel; dit is geen indexatie-/koopbaarheidsmeting. Zes productvoorbeelden met head/schema onderzocht. FabriecioGM_1002 meldt schemaOutOfStock en ontbreekt in deze product-sitemapcapture; oorzaak open.

Route: bestaand Merchant Center **5898992928** hergebruiken (account/status alleen eerder door eigenaar gemeld), standaard Google & YouTube-koppeling, gratis vermeldingen eerst; Ads later afzonderlijk. Google-login, domeinverificatie, Search Console-indexatie en GA4 niet gecontroleerd. **Lagoo-fotoverbod behouden**: geen foto's terugzetten; beeldloze artikelen afzonderlijk uit de Google-productbestemming houden zolang ze niet aan de beeldvereiste voldoen. Bestaande catalogus-/kleur-/LVS-/offerteafspraken blijven gelden.

Uitsluitend documentatie op main en de bestaande codebranch **fix/product-cards-2026-10-14**; themabron blijft **shopify/current/**. Geen Shopify-write, appinstallatie, feedactivering, advertentiebudget, formulierinzending of publicatie. Geen browser-/mobiel-/checkout-/betalingstest of Windows-controle. [Nulmeting en grenzen](livegang-seo/bewijs/2026-11-05-nulmeting.json) · [logboek/herstel](livegang-seo/LOGBOEK.md).

**Exact één volgende handeling:** **BC-LIVE-001** — de werkelijke verkopersgegevens en bezorg-/retourafspraken vaststellen om ontbrekende winkelinformatie gericht af te ronden. Andere dossiers blijven behouden; geen actieve schrijver na overdracht.

## LAGOO-19 — alle productafbeeldingen verwijderd · 4 november 2026

**VERIFIED_ADMIN / LIVE_PRODUCT_CHECK.** Op expliciete eigenaaropdracht alle Lagoo-productafbeeldingen onmiddellijk verwijderd. Verse inventaris: **232 Lagoo-producten**, waarvan 175 met samen **1.788 afbeeldingskoppelingen** naar 1.763 unieke bestanden. Eén proefverwijdering met readback, daarna acht opeenvolgende batches via `fileUpdate.referencesToRemove`; alle antwoorden zonder userErrors. Alleen relaties met gecontroleerde vendor Lagoo verwijderd. Bestanden blijven beschikbaar voor herstel; variantafbeeldingen worden door dezelfde Shopify-operatie leeggemaakt.

Volledige eindcontrole: **232/232 producten, nul media** en geen volgende pagina. Titels, handles, vendor, status en descriptionHtml gelijk aan de nulmeting. MAIN **196116087050** ongewijzigd; geen themefilewrite/publicatie. Openbare Garda-productpagina zonder preview: nul product-`img` in main en visueel geen productfoto. Native zoekmarkup bevat Lagoo-kaarten zonder foto's; de latere externe zoeklaag toont vier Wiesbaden Lagos-producten met hun eigen foto's. Deze afzonderlijke zoekafwijking is niet aangepast. Geen Windows-, fysieke telefoon-, cart- of checkouttest.

**Nieuwe foto-instructie gaat vóór eerdere foto-uitrol:** Lagoo blijft zonder productfoto's. Niet automatisch opnieuw importeren/herkoppelen of de oude foto-uitrol hervatten. LVS1/2/3 en overige eerdere grenzen behouden. [Bewijs en herstel](lagoo/2026-11-04/no-product-images/README.md).

**Exact één volgende handeling voor Lagoo:** wacht op een nieuwe expliciete eigenaaropdracht voordat foto's opnieuw worden gekoppeld. Geen actieve schrijver na overdracht.

## LAGOO-18 — goedgekeurde Lagoo-stijl live bevestigd; offerteactie nog uit · 3 november 2026

Eigenaar keurt LAGOO-17 goed met “Ja dit is goed voeg toe”. Verse Shopify-controle toont dat thema **196116087050 — BadkamerCity - Lagoo foto's en productkeuzes** inmiddels al **MAIN** is; voormalig MAIN196110090506 is UNPUBLISHED. Deze uitvoering heeft niets gepubliceerd en geen Shopify-code/data/instellingen gemuteerd.

Volledige live-inventaris: 1378 bestanden. Alle zeven LAGOO-featurebestanden komen exact overeen met de eerder gecontroleerde code (checkpoint e8939e96d9aebd4f7338f29cba0ff17fd3a3d649). Publieke G1104BN-pagina zonder previewcookie/-parameter HTTP200 met compacte kleurenadapter en 24 echte productbestemmingen. De Hotbath-keuzestijl is dus live; eerdere NOT_PUBLISHED voor het thema is historisch.

**Concrete resterende afwijking offerteknop:** live header-group heeft quote_cta_enabled=false / quote_cta_preview=true. De offerte-Page166573539594 (offerte-vergelijken) is nog isPublished=false en de klant-URL geeft404. Op de live productpagina is de offerteactie daarom afwezig. De alternatieve contact?view-route geeft200 maar bevat live geen Jotform-iframe. Het goedgekeurde rustige ontwerp staat in de code; geen kapotte klantlink geactiveerd en geen claim dat offerte-upload al live werkt.

Bestaande productstatussen, foto's, 400 reviews en LVS-uitstel niet gewijzigd. Volledige Lagoo-catalogusomzetting blijft open volgens LAGOO-16. CONTENT-01 en andere taken hieronder behouden.

**Exact één volgende handeling voor offerteactivatie:** bestaande uploadpagina/koppeling en ontvangst aantoonbaar afronden, daarna de Page en klantactie gericht activeren via de bestaande preview-/publicatiewerkwijze. Geen actieve schrijver na overdracht.

## CONTENT-01 — plus- en aandachtspunten beoordeeld; niets toegepast · 3 november 2026

**READ_ONLY_AUDIT / PROPOSALS_READY / NOT_APPLIED.** Op verzoek van de eigenaar de bestaande punten inhoudelijk beoordeeld. Volledige inventaris11.887ACTIVE producten/48pagina's;148verschillende veldteksten, waarvan67bij273JEE-O-producten.6.318producten hebben minstens één gevuld veld. Twee gecontroleerde JEE-O-lijsten overlappen woordelijk met BadkamerXXL; geen algemene herkomstclaim voor alle producten. Bij48JEE-O-waskommen staat geen overloop zowel bij plus als aandacht.

Privéreview bevat alle148teksten met voorstel, reden en verificatievoorwaarde; standaardJEE-O-filter. Geen verplicht aantal punten; specificaties/setinhoud apart, geen stijl- of veiligheidsclaims verzinnen. Temperatuur, onderhoud, universele passing en ontbrekende eenheden eerst controleren. Sunshower heeft daarnaast een aparte configuratieroute buiten deze veldinventaris.

**PASS:** inventaris/148van148beoordelingen en filterlogica67/148/81/18 plus lege zoekstatus; geen visuele browser-, telefoon- of checkouttest. Geen Shopify-product-/thema-/publicatiemutatie. Verse eindcontrole MAIN196110090506; Lagoo-concept196116087050 UNPUBLISHED. Bestaande Lagoo-code/status behouden. [Scope, broncontrole en overdracht](product-content/PROS_CONS_REVIEW_2026-11-03.md).

**Exact één volgende handeling voor CONTENT-01:** Jackson beoordeelt de JEE-O-termvoorstellen. Daarna pas een kleine fabrikantbevestigde productgroep voorbereiden; geen automatische catalogusbrede vervanging. Geen actieve schrijver na overdracht.

## LAGOO-17 — Hotbath-keuzestijl en subtiele offerteactie in concept · 3 november 2026

Eigenaar accepteert de productnavigatie en vraagt exact de Hotbath-stijl met eigen Lagoo-opties. Bestaand UNPUBLISHED **196116087050** aangepast: dezelfde Hotbath-CSS/JavaScript voor vier ronde kleurbolletjes, geselecteerde kleur altijd zichtbaar, selectierand/vinkje en Bekijk alle 8 kleuren / +4. Eigen Lagoo-kleurnamen en Regular/Medium/High behouden. Bestaande illustratieve afwerkingsassets hergebruikt, aparte illustratieve Tuscany/champagne-SVG's; echte productfoto's blijven ongewijzigd. De grote blauwe offertebalk is nu een rustig icoon met label bij Retour/Verlanglijst/Winkelwagen. Bestemming, instellingen en mobiele verberging blijven behouden; geen nieuwe formulierontvangsttest geclaimd.

Zes conceptfiles bijgewerkt/toegevoegd en exact teruggelezen. Gedeelde Hotbath-CSS/JavaScript en MAIN-header/snippet ongewijzigd. Finale volledige vergelijking: MAIN 1374 bestanden, concept 1378, exact zeven bedoelde verschillen inclusief vorige Lagoo-adapter/main-product-wijziging; geen ontbrekende bestanden. Geen product-/prijs-/foto-/publicatiedatamutaties en geen themapublicatie; LVS blijft later.

**Bewezen:** ThemeCheck 6/6 PASS; bijgewerkte bestaande DOM-test 216/216 wissels, juiste vier zichtbare kleuren met selectie, uitklappen en bestaande kleurassets, Liquid-grensgevallen PASS. Echte Chrome op 1363 CSS-pixels: transparante compacte offerteactie, geen horizontale overloop, 8/8 swatchafbeeldingen geladen. Uitklappen en kleurwissel naar G1104BK (€570), daarna Medium naar G1102BK (€440): echte nieuwe URL, koper behouden, juiste foto/selectie/titel/prijs. **NOT_TESTED:** fysieke telefoon/aparte mobiele viewport, cart/checkout en offerteontvangst. Browserbeelden buiten publieke Git/Library gehouden.

Codecheckpoint **e8939e96d9aebd4f7338f29cba0ff17fd3a3d649** op **fix/product-cards-2026-10-14**, bron **shopify/current/**. [Details en herstel](lagoo/2026-11-03/product-links/README.md). Alleen het bestaande concept aangepast; volledige Lagoo-catalogusomzetting blijft open volgens LAGOO-16.

**Exact één volgende handeling:** eigenaar bekijkt de bijgewerkte stijl in hetzelfde concept, daarna gecontroleerde Lagoo-uitrol voortzetten. Publicatie door eigenaar volgens bestaande werkwijze. Herstel via vorige codecommit voor de zes gewijzigde conceptpaden; nieuwe ongebruikte assets/helper mogen blijven. Geen actieve schrijver na overdracht.

## LAGOO-16 — proef met juiste foto's en echte productlinks klaar; uitrol nog open · 3 november 2026

**LVS1/LVS2/LVS3 nu ongemoeid laten. To-do voor na de fotocorrectie:** zelf samen te stellen sets zoals Hotbath IBS70, met type handdouche en met/zonder glijstang. Andere setkeuzes, technische compatibiliteit, prijzen en productrelaties eerst controleren. De 20 beschikbare LVS-beelden en 4 fotogaten blijven in de privéwerkset. Geen nieuwe LVS-producten/configurator nu.

De huidige Lagoo-import heeft 208 groepen / 1772 SKU-varianten en te brede gezamenlijke galerijen. Eigenaar wil aparte echte product-URL's zoals Hotbath. **Eerste concrete proef:** 24 nieuwe producten voor G1100/G1102/G1104, elk één SKU, één aantoonbaar bijbehorende eigen Lagoo-foto, actuele bestaande prijs/BTW/verzend-/trackingwaarden, artikelgerichte fabrikanttekst en bevestigde eigen PDF's. Status UNLISTED; alleen Webshop gepubliceerd en via directe link bereikbaar/koopbaar, buiten zoeken/collecties/aanbevelingen. Dezelfde SKU's bestaan tijdelijk ook nog in de oude groep. Geen catalogusbrede omzetting claimen: bestaande proefouder exact intact (ACTIVE / 24 varianten / 37 foto's); overige 207 groepen niet gemuteerd.

UNPUBLISHED **196116087050 — BadkamerCity - Lagoo foto's en productkeuzes**, eerst volledig 1374/1374 checksums identiek aan verse MAIN **196110090506**. Nu 1375 conceptbestanden met exact twee bedoelde afwijkingen: main-product.liquid en nieuwe bc-lagoo-choices.liquid onder shopify/current/. De adapter gebruikt de bestaande Hotbath V2-navigatie met expliciete productbestemmingen; kleur/hoogte blijven bij wisselen behouden. Andere merken en gedeelde JavaScript/CSS niet gewijzigd. MAIN na afloop 1374/1374 checksums ongewijzigd, niet gepubliceerd.

**Bewezen:** 24/24 Admin-readbacks op foto, SKU, prijs, opties, publicatie, tekst/PDF's en voorraad-/verzendinstellingen; 216/216 kleur-/hoogtewissels in bestaande echte JavaScript via Happy DOM; Liquid-rendering en grensgevallen PASS; 24/24 conceptpagina's HTTP200 met juiste inline navigatie en exact één juiste fabrikantfoto-ID. ThemeCheck PASS met twee bestaande main-product-waarschuwingen; git diff --check en Python compile PASS. **NOT_TESTED:** echte browser/mobiel/visuele eigenaarreview, cart/checkout, volledige migratie en SEO-/historische URL-afhandeling.

Codecheckpoint **433ee10324a29fa755f9b4aff484ba57eb9a8f9a** op bestaande branch **fix/product-cards-2026-10-14**. [Proefpagina High/nikkel](https://badkamercity.nl/products/lagoo-g1104bn?preview_theme_id=196116087050) · [uitvoering en herstel](lagoo/2026-11-03/product-links/README.md). Volledige catalogus, oorspronkelijke 400 reviews en API-receipts niet publiek opgeslagen; privéfabrikantwerkset bijgewerkt naar versie 7 met fotobewijs en readbacks.

**Exact één volgende handeling:** eigenaar beoordeelt deze 24 uitvoeringen in het concept; daarna de resterende groepen met bewezen foto-/kleurkoppelingen en behoudende ID-/URL-omzetting voorbereiden. Publiceren door eigenaar na controle, volgens de bestaande Git-werkwijze. Herstel: nieuwe proefproducten terug naar DRAFT / uitsluitend hun Webshop-publicatie ontkoppelen; oorspronkelijke groep intact. Geen actieve schrijver na overdracht.

## QC-15 — fotogalerijprobleem vastgesteld; LVS-foto’s voorbereid · 3 november 2026

Eigenaar constateert dat kraangalerijen te veel modellen/kleuren bevatten. Bevestigd: de QC-11-fabrikantgalerijen zijn te breed samengevoegd; bronherkomst/READY en eerdere API-verificaties bewijzen geen juiste klantgalerij per gekozenkleur/model. De208publicaties uitQC-14 blijven uitgevoerd, maar de galerijpresentatie is nog niet hersteld. Geen nieuwe brede fotovervanging uitvoeren. Eerst één model/kleur aantoonbaar correct maken en bestaande gegevens behouden.

G1104 gebruikt publiek een VulpStudio3D/AR-viewer met één3D-model en materiaalpalet ch/bn/mb/tc/bb/bk/gm/pg; kleurbolletjes daar leveren niet automatisch acht losse2D-foto’s. Geen AR in Badkamercity ingebouwd. Advies: eerst correcte2D-variantfoto’s; externe viewerintegratie later afzonderlijk toetsen.

Nieuwe eigenaarsopdracht omvat LVS1/2/3-foto’s.20fabrikantkleurbeelden voorbereid:7LVS1/5LVS2/8LVS3, éénbeeldperkleur;4exacte fabrikantcodekoppelingen en16sterke beeldidentiteiten met eerder door eigenaar geaccepteerde LVS-foto’s metkleurcode (genormaliseerdeRMSEmax0,602/255, duidelijkeafstandtotanderekleuren). Legacybestanden uitsluitend referentie, alle nieuwe beeldURL’s eigen fabrikantkopieën. Extra/niet-gematchte beelden niet alskleurfoto opgenomen. Ontbreekt:LVS1PG,LVS2CH,LVS2TC,LVS2PG; geenanderekleurfallback.

LiveShopify-zoekopdracht vendorLagoo+LVS1*/LVS2*/LVS3* gaf0producten. Alleenfoto’s/CSV/bronbewijzenaangevuld in privéfabrikantwerkset, inclusief20echteJPG’s. Productimportbescherming blijft; geen drie nieuwe producten/prijzen/publicatie, geen themamutatie of QC-reviewwijziging. VolgendeLagoo-stap: G1104-fotokoppeling en zichtbare galerij per uitvoering corrigeren op bewezen bronnen; LVS-productimport eventueel gericht uitvoeren met de vier open fotogaten zichtbaar.

## GIT-SYNC-01 — actuele themabron en JEE-O-publicatie bevestigd · 3 november 2026

Shopify MAIN is inmiddels **196110090506 — BadkamerCity - JEE-O kleurkeuzes**; vorig MAIN196052189450 is UNPUBLISHED. De24JEE-O-codefiles stonden al exact in Git en zijn ongewijzigd live aangetroffen. Eerdere PUBLICATION_BLOCKED-status hieronder is hiermee historisch; deze Git-taak heeft zelf niet gepubliceerd.

Volledige vergelijking: live1374bestanden; oude Git-root507, waarvan451bytegelijk en56afwijkend;867livepaden ontbraken in de root. Daarom een aparte actuele bronkopie **shopify/current/** op bestaande branch **fix/product-cards-2026-10-14**. Geen onzekere root-/deploykoppeling omgezet. Main ontvangt uitsluitend documentatie/manifest.

Alle1374livepaden gelezen:1373inhoudelijk bytegelijk vastgesteld. Acht historische QA/debugbackups niet als actieve code opgenomen: de actuele bronmap bevat1366themafiles, waarvan1365bytegelijk. Enige API-bodyuitzondering config/settings_data.json expliciet vastgelegd en tegen upload beschermd. Retourtemplate hersteld naar exact de Shopify-checksum door uitsluitend de gegenereerde API-header weg te nemen.804JSON/JSONC-bestanden parsebaar; geen credentialpatroon gevonden. Bronmanifest opnieuw gelezen:1374paden/geen wijzigingen tijdens de capture. Geen nieuwe browser-/mobiel-/checkoutvrijgave.

Broncodecheckpoint **d4cc4bcf360d1f91d5a6ab8270a0ad7a188f0434**; Git-readback1366/1366exact aan de gecontroleerde capture.

[Actuele bron, gebruik en herstel](git-sync/2026-11-03/README.md) · [volledige bestandscontrole](git-sync/2026-11-03/live-theme-manifest.json). Catalogus, metafields, menu-inhoud, orders en externe backend blijven afzonderlijke systemen. QC-/Lagoo-status hieronder behouden. Geen actieve Git-schrijver na overdracht.

**Volgende Git-handeling:** bij nieuw themawerk de codebranch met **shopify/current/** als bron openen en de actuele MAIN opnieuw controleren; settings_data pas meenemen nadat de checksumuitzondering onafhankelijk is gesloten.

## QC-14 — Lagoo online op Webshop · 3 november 2026

Op expliciete opdracht de208geïmporteerdeLagoo-productgroepen gepubliceerd op de bewezen OnlineStore/Webshop-publicatie283427864842, geïdentificeerd via apphandle online_store. Eerst éénpilot gepubliceerd en teruggelezen, daarna207groepen in begrensde aliasbatches.208geslaagd/0fouten. Finale onafhankelijke paginering: alle208ACTIVE, publishedOnPublication=true op exactditkanaal en publishedAtingevuld. LVS1/LVS2/LVS3 uitgesloten. Andereverkoopkanalen/marktpublicaties, productdata, thema en reviews niet gewijzigd.

OpenbareNesso-productpagina op badkamercity.nl HTTP200 met juisteproductnaam. Verdere publiekeproductsteekproeven volgen in privéverslag. Geen echtecart/checkout of fysieke telefoon getest. Privépublicatieverslag bevat exactebefore/afterID’s en herstel: uitsluitend ditkanaal ontkoppelen na expliciete opdracht. Bestaande57beeldlozegroepen en eerder gedocumenteerde datagaten blijven kwaliteitswerk; publicatie is geen nieuwe inhoudelijke datavrijgave.

**Volgende Lagoo-stap:** eigenaar bekijkt de gepubliceerdeproducten en vult ontbrekende fabrikantbeelden/technischeinformatie gericht aan. Publicatie afgerond; geen actieve schrijver.

## QC-13 — Lagoo-status ACTIVE · 3 november 2026

Op expliciete opdracht “Zet ze op actief” exact de208eerder geïmporteerdeLagoo-productgroepen vanDRAFTnaarACTIVEgezet. Vijf native statusbatches50/50/50/50/8:208geslaagd/0mislukt. Alle208daarna opnieuw uitShopify gelezen: juisteID/handle/vendor enACTIVE. LVS1/LVS2/LVS3 en andereproducten buiten scope. Alleenproductstatus gewijzigd; geen prijs-,optie-,media-,voorraad-,review- ofthemawijziging. PublishedAtblijftvooralle208null; geenverkoopkanaalpublicatiegeclaimd. [Importscope en herstel](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_IMPORT_EXECUTED_2026-11-03.md). Privéactivatieverslag bevat before/after enexacteID’s. VolgendeLagoo-stap: verkoopkanaalpublicatie en ontbrekendegegevens gericht beoordelen; geen actieve schrijver.

## QC-12 — Lagoo geïmporteerd als concept · 3 november 2026

Op expliciete opdracht208groepen/1772varianten geïmporteerd:202nieuweDRAFT-groepen,6bestaandeproefgroepenopbestaandeIDbijgewerkt. Alle208groepen direct vergeleken en finale vendorinventaris208uniekehandles/alleDRAFT/publishedAtnull.105bestaandevariant-ID’s behouden; prijzen, opties, SKU’s en fotorelaties gecontroleerd.151groepenmetfabrikantfoto’s,57zonder;1764galerijreferenties/1763uniekefabrikantbestandenREADY,612exactevariantfoto’s.156seriewaarden geverifieerd,390PDF-linksnaar eigenopslag. LVS1/2/3 uitgesloten.

Geen publicatie/thema-/voorraadhoeveelheid-/review-/D1-mutatie; MAINvóór/na196052189450. Browser/telefoon/checkout niet getest. Volledige input/before/readbacks/importverslag uitsluitend privé in bijgewerkte fabrikantwerkset; nieuwe producten blijven concept tot gegevens en verkoopprijzen zijn gecontroleerd. [Scope, bewijs en herstel](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_IMPORT_EXECUTED_2026-11-03.md).

**Volgende Lagoo-stap:** eigenaar bekijkt de concepten en vult alleen de ontbrekende fabrikantbeelden/technische gegevens aan vóór gerichte publicatie. Import afgerond; geen actieve Lagoo-schrijver.

## JEEO-03 — 228 kleurkoppelingen en kleurbolletjes LIVE bevestigd · 3 november 2026

**VERIFIED_ADMIN / LIVE_THEME_CONFIRMED / DESKTOP_PREVIEW_TESTED.** Bij deze nieuwe controle is196110090506 MAIN; alle24eerder geleverde JEE-O-codefiles zijn exact gelijk gebleven. Alle65groepen/228producten,456metafields en273behouden titels horen bij de eerder gecontroleerde uitvoering; deze Git-taak heeft geen productdata opnieuw geschreven.

De eerdere29PDP-/29kaartdata-, prijs-/foto-/SKU-/link- en desktopcontroles behouden hun bronmoment. Mobiele interactie/fysieke telefoon en checkout niet als nieuw getest opgevoerd. SWMBAS71/2producten en43producten zonder kleurtegenhanger behouden hun eerdere uitzondering.

Publiceren was tijdens implementatie door de Shopify-koppeling geblokkeerd; het thema is daarna buiten deze uitvoering gepubliceerd. Geen nieuwe publicatie nodig. [Kleurcontract, tests en herstel](product-content/JEEO_COLOURS_2026-11-03.md) · [24featurepaden](product-content/JEEO_COLOURS_THEME_FILES_2026-11-03.json). Voor actuele Git-bron: GIT-SYNC-01 hierboven.

## QC-11 — uitsluitend officiële Lagoo-foto’s in import en proefproducten · 3 november 2026

Op expliciete eigenaarsopdracht fabrikantgalerijen toegestaan in importv5, zonder terugval op Badkamervoorjou. 1.562 van1.772niet-beschermde varianten hebben fabrikantbeelden;210zonder gevonden fabrikantfoto. Productgalerij en vaste variantfoto gescheiden:612exacte artikel-/kleurkoppelingen. Het eerdere getal1.558 telde alleen kandidaatgalerijen; vier exacte varianten zonder kandidaatgalerij komen erbij. LVS1/2/3 ongewijzigd.

Zes bestaande Shopify-DRAFT-proefgroepen aangepast en volledig teruggelezen:168eigen fabrikantfoto’s in vijf galerijen,102oude referenties uit zes galerijen ontkoppeld. RE9012zonder fabrikantfoto nu beeldloos. Alle105variantrelaties gecontroleerd:48exactgekoppeld/57zondervastefoto. Bestanden behouden voor herstel. Geen productcreatie/publicatie of prijs-,titel-,optie-,voorraad- of themamutatie. Verse MAIN196052189450; andere taken hieronder behouden hun status.

Sites-versie14 succeeded, bron dff37cd29558b345be7d1bd9b7411bfbbe3db61e, deployment appgdep_6ae9c6a0f6c481918766f09ec4f3de90. TypeScript/15Lagoo- en10fabrikantcontractgroepen PASS. HostedimportHTTP200:1772/1562metfoto/210leeg/612exact, allebeeldURLs eigen fabrikantbestanden. Authclient/toegangsbeleid identiek. Eerste deployment faalde op oude buildchunks; schone tweede build33.697.516bytes geslaagd. Alleen onbereikbare gegenereerde chunks opgeschoond, brondata behouden. Browser/telefoon niet opnieuw getest.

Privéwerkset bijgewerkt met Shopify-concept-CSV208groepen/1772varianten. OpenbareGit uitsluitend code/dossier; brondata/reviews/herstel privé. [Scope en herstel](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_PHOTO_POLICY_2026-11-03.md). **Volgende Lagoo-stap:** bijgewerkte fabrikantconceptimport gebruiken en alleen ontbrekende beelden/technische gegevens behandelen. Geen automatische volledige publicatie.

## JEEO-02 — titels bevestigd en kleurkoppelingen uitgewerkt · 3 november 2026

Alle273JEE-O-titels/handles opnieuw uit Shopify gelezen: exact gelijk aan JEEO-01. Geen herhaalde productwrite.66mogelijke kleurgroepen/230producten en43zonder kleurtegenhanger voorbereid;8groepen/28producten ook op fabrikantartikelcode bevestigd,57catalogusgevalideerd en1SWMBAS71-HOLDgroep/2producten. Volledige koppellijst privé; geen kleurrelatie geactiveerd.

Huidige MAIN196052189450 read-only onderzocht. Bestaande kleuradapter en bc-card-data begrenzen color_variants tot Wiesbaden; alleen productrefs invullen toont JEE-O nog niet. V2 kan worden hergebruikt. Manifestprecedentie voor kaartkleur bij implementatie expliciet oplossen. [Details en testgrenzen](product-content/JEEO_TITLES_2026-11-03.md).

**Volgende JEE-O-actie:** in een identiek UNPUBLISHED-concept de JEE-O-product- en kaartkoppeling voorbereiden; eerst3groepen van5Slimline-plafondarmen per lengte15/25/35cm testen. Geen theme-write/publicatie of metafieldmutatie in deze controle; geen actieve JEE-O-schrijver. Andere trajecten hieronder behouden hun status.

## JEEO-01 — 273 klantvriendelijke producttitels afgerond · 3 november 2026

Op expliciete eigenaarsopdracht alle273JEE-O-producttitels aangepast naar natuurlijke namen, bijvoorbeeld **JEE-O flow hoge wastafelkraan Geborsteld RVS**. Merk/serie/product/afwerking; geen lange technische omschrijvingen. Maat behouden waar uitvoeringen anders niet herkenbaar zijn. Korte/lange Soho-uitlopen apart; nul dubbele nieuwe titels.

Drie proefproducten + vijf groepen van50 + één van20 vooraf gecontroleerd en exact teruggelezen. Volledige eindinventaris273/273titels exact; nul onverwachte wijzigingen in vergeleken overige velden, waaronder URL/handle, omschrijving, status, opties en varianten met SKU/prijs. Drie oorspronkelijke openbare URL's HTTP200 met juiste nieuweH1. Geen theme-write/publicatie, keuzemenu-, SEO-, metafield- of mediabatch. Voor/na-overzicht en herstelgegevens privé bewaard; geen actieve JEE-O-schrijver. [Scope, bewijs en herstel](product-content/JEEO_TITLES_2026-11-03.md).

**Volgende JEE-O-stap:** keuzemenu's per exacte modelfamilie uitwerken; eerst15Slimline-plafondarmen met lengte15/25/35cm en vijf afwerkingen. Huidige storefrontbron vóór implementatie controleren. Lagoo-QC en de bestaande themareview hieronder behouden hun eigen status.

## QC-10 — officiële Lagoo-bron en klantdocumenten · 3 november2026

Alle199productpagina's en27mediapagina's gelezen;2.629mediarecords tegenover2.679headercount,50verschil expliciet open. Nieuwe werkset met1.823eigen fabrikantfoto's en372PDF-kopieën READY. Geen3D/CAD-bestandsdownload.254PDF-records in actuele paginalinks; overige alleen kandidaat.48pagina's/314bestaande varianten noemen inbouwdelen met originele voorwaarden/alternatieven.616varianten met expliciete artikel-/kleurcode,612niet beschermd voor importfoto's. Andere kleurkoppelingen blijven onzeker; ook fabrikant hergebruikt seriebeelden.

Dezelfde privé-QC gebruikt nieuwe fabrikantfoto-ID's, duidelijke bronlabels en huidige/kandidaat-PDF's;24LVS1/2/3varianten en alle andere merken exact behouden. Oude400beoordelingen blijven historie, geen automatische goedkeuring van nieuwe bestanden. Checkpoints blijven per SKU. Importv4:1772niet-beschermde varianten,612photoImportReady; alle andere importfoto's leeg/hold. Prijzen/opties/EAN's niet uit groepsclaims overschreven. Geen Shopify-productmutatie/publicatie; uitsluitend eigen bestandskopieën. [Scope en herstel](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_OFFICIAL_SOURCE_2026-11-03.md).

Sites-versie12 succeeded; bron627aafcae4508977066e13e68ef7ab8e1341b2c2, deployment appgdep_6ae9b9ea19488191a5816154ba3b1387. Schone build33MiB, originele brondata privé behouden. TypeScript/build/45bestaande API-SQLite-Lagoo-groepen+8nieuwe fabrikantcontractgroepen PASS. Hosted reviewcatalogus1796/1772official/24protected HTTP200; G1100BN juiste eigen fabrikant-URL HTTP200; import1772/612photoReady HTTP200; review zonder visitor401. Authclient/toegangsbeleid gelijk. Browsergoedkeuring faalde door capaciteit, geen browseromweg; fysieke telefoon/visitor-write niet getest. Twee bronbeelden onverwerkbaar;24PDF-kopieën lokaal signature/EOF/SHA gecontroleerd, overige READY maar lokale verificatie door proxy403onvolledig. Volledige data/reviews uitsluitend privé; downloadbare werkset geleverd. Eigenaar herlaadt en behandelt alleen resterende onzekere fabrikantkoppelingen.

## QC-09 — eerste400Lagoo-fotoselecties verwerkt, LVS1/2/3 overgeslagen · 3 november 2026

Checkpoint400 bevestigd: vervolg N8100CH.24LVS1/2/3varianten uitgesloten van galerie, brondata/Shopify daarvoor ongemoeid.400bekeken varianten verwerkt in private importwerkkopie:366met selectie/367beelden,34zonder keuze blijven open. Alle oorspronkelijke kandidaten, specificaties, prijzen, opties en eigen PDF's behouden. Export bevat approvedLagooImport. Geen automatische goedkeuring/afkeur of D1-reset.

Actuele Shopifyinventaris6DRAFT-proefgroepen; binnen eerste400bestaan3groepen/25varianten. Vijf Nesso-variantkoppelingen gecorrigeerd en drie niet-geselecteerde productgalerijreferenties verwijderd; eigen bestanden behouden. Alle25koppelingen en drie galerijen exact teruggelezen; geen nieuwe producten/publicatie. De overige30groepen zijn alleen voorbereid in importdata, niet geïmporteerd. [Scope/rollback/testgrenzen](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_400_APPLIED_2026-11-03.md).

Sites-versie10 succeeded, bron1b7fabbd6840ec8d2c91511fd1b8fc38776eea66, deployment appgdep_6ae9a3a5712c81918b0638ebdd0bb148. TypeScript/build/45API-SQLite-Lagoo-groepen+6selectie-integriteitstests PASS. Authclient/toegangsbeleid gelijk. Browser/telefoon/hosted visitor-write niet getest. Reviews/checkpoints/volledige catalogus/receipt uitsluitend privé. Eigenaar herlaadt de bestaande privétool en vervolgt met N8100CH.

## QC-08 — alleen goede foto's, vaste kleur, checkpoints per20 · 3 november 2026

Galerie toont één selecteerknop per foto, geen fout-/twijfelactie. Deselecteren=unchecked; niet geselecteerd is geen afkeur. Kleur/SKU blijven sticky bovenaan. Foto-oordelen direct opgeslagen; bij20/40/60etc en laatste groep eerst online checkpoint, dan volgende product. Herladen hervat op nextSku van laatste galeriecheckpoint; tussentijdse bevestigde selecties blijven behouden. Zelfde eigenaargebonden API/schema, geen Shopify-write. TypeScript/build/45API-SQLite-Lagoo-groepen PASS. Browser/telefoon/hosted visitor-write niet getest. Versie9 succeeded, bron c5a4ee8dea2043da36db698505cb19bfc06893a2, deployment appgdep_6ae98d0bef948191831ff2ad92f3b432. Authclient/toegangsbeleid identiek. [Dossier](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_SELECTION_2026-11-03.md). Eigenaar herlaadt en controleert selectie/hervatten na20producten.

## QC-07 — Lagoo-galerie per SKU · 3 november 2026

Dezelfde privétool toont producttitel, kleur en alle kandidaatfoto’s; per foto Goed/Niet goed/Twijfel. Meerdere goede foto’s per variant, productwissel handmatig. Individuele foto-oordelen via bestaande D1-review-API, geen automatische hoofdfotokeuze/Shopify-write. TypeScript/build en44API/SQLite/Lagoo-contractgroepen PASS, inclusief twee onafhankelijke oordelen binnen één SKU. Browser/telefoon niet getest. Sites-bron71e835d774cdca06467f685e9286ed0fc0c8feb8, deployment appgdep_6ae98b7954fc8191b5ce72dfe703f0a0 succeeded. [Werkwijze](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_GALLERY_2026-11-03.md). Eigenaar herlaadt privétool en beoordeelt foto’s per kleurvariant. Bij herladen start galerie op eerste product; bevestigde oordelen blijven zichtbaar.

## QC-06 — Lagoo: directe kleurcontrole · 2 november 2026

Dezelfde privétool opent nu standaard alleen Lagoo: kleur uit titel groot boven één foto, Ja/Nee/Twijfel en automatisch volgende SKU na bevestigde opslag. Andere foto wisselt kandidaat direct. Geen ronde-start of algemene merk-/PDF-menu's in de eenvoudige weergave; Uitgebreid behoudt de bestaande QC en voortgang. [Actuele werkwijze op quality-control](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_FAST_REVIEW_2026-11-02.md).

Sites-versie7 succeeded; broncommit e21a5308e2d4867fc702a0bd73d13b8ec7de6177, deployment appgdep_6ae897e9677c81918bd7fe9efee75b7f. TypeScript/build,43bestaande API/SQLite/Lagoo-groepen en6gerenderde kleurcontrolecontracten PASS. Hosted Lagoo1796kaarten en SKU-gallery HTTP200; review zonder visitor401. Native begrensde24reviews+1checkpoint identiek vóór/na, authclient/toegangsbeleid gelijk. Geen Shopify-write, catalogus- of databaseschemamutatie. Browser/telefoon/hosted visitor-write niet opnieuw getest; eerdere previewinfrastructuur niet aantoonbaar hersteld. Volgende QC-actie: eigenaar herlaadt privélink en controleert kleur/foto met directe knoppen. Andere storefronttaken hieronder blijven afzonderlijk.

**31 oktober 2026 · NAV-03 / TILE-02 PREVIEW_VERIFIED / OWNER_REVIEW_PENDING.** Compact menu, startwaarde1m² en tegelinformatie staan in het gecontroleerde concept. Geen actieve schrijver na overdracht.

## QC-05 — Lagoo in dezelfde privécontrole · 2 november 2026

Afzonderlijk van het NAV-03-themaconcept: branch `quality-control` bevat nu 211 Lagoo-brongroepen als 1.796 SKU/kleurkaarten in [dezelfde privétool](https://badkamercity-quality.jason015.chatgpt.site), versie6. Per SKU hoofdfoto kiezen/expliciet goedkeuren; Aanleverlijst met ontbrekende PDF, technische documentatie, foto, kenmerken en EAN. 1.229 afbeeldingen en251PDF-bestanden in eigen Shopify Files; PDF-kopieën volledig op SHA256/grootte gecontroleerd. 92groepen zonder directe PDF; koppelsuggesties blijven ongeverifieerd. Geen automatische goedkeuring of fotocorrectie.

Sites-broncommit `5634119673735eb88cce104c51e2b4f8fe7a8d2a`, deployment `appgdep_6ae894b87f3c8191b8f1ce1d6894e20c` succeeded. TypeScript/build/43contractgroepen PASS. Hosted Lagoo1796kaarten en lazySKU-gallery HTTP200; review zonder visitor401. Bounded native24reviewrijen+1checkpoint identiek vóór/na, authclient/toegangsbeleid ongewijzigd. Browser/telefoon/hosted-visitorwrite niet getest in deze taak. Volledige catalogus en reviews blijven privé; publieke Git alleen code en scope.

Vijf bestaande DRAFT-proefomschrijvingen gebruiken nu eigen PDF-links. Geen volledige import/publicatie van overige205groepen. Volgende QC-actie: eigenaar kiest Lagoo en controleert foto's en ontbrekende gegevens per SKU. [QC-dossier op quality-control](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_QC_2026-11-02.md). NAV-03-status en vervolghandeling hieronder blijven van kracht voor het storefrontthema.

## Begin hier: actuele rollen en code

- **MAIN195974824202 — BadkamerCity - Betrouwbaar bestellen en filters.** De eigenaar heeft de herstelde FIX-01 gepubliceerd. Verse eindmeting:1.355bestanden, nul gewijzigde paden tegenover opening van deze taak. Geen MAIN-filewrite of publicatie door deze uitvoering.
- **UNPUBLISHED195947036938 — BadkamerCity - Compact menu en tegelinformatie.** Eerst alle21FIX-01-paden vanuit MAIN overgenomen; vóór nieuwe features1355/1355checksumpariteit. Finaal1.356bestanden, exactzesgewijzigdebestaandepaden +éénnieuweoverflow-snippet. Alle zeven checksums correct teruggelezen. QA-template exact hersteld.
- Repository **jlamping1997/badkamercity**, bestaande branch **fix/product-cards-2026-10-14**. Runtimecheckpoint **b7a5308038965bf874e06ed5115aa9431eb381d3**. Alleen de zeven expliciete featurepaden uploaden; Git-root is geen volledige actuele MAIN-snapshot. Main ontvangt dezelfde overdracht/testdocumentatie, geen themacode.

[Actuele wijziging, bewijs en rollback](navigation-and-tiles/2026-10-31/README.md) · [einddiff](navigation-and-tiles/2026-10-31/final-verification.json).

## Nieuwe werking

| Onderdeel | Gedrag in het concept |
| --- | --- |
| Desktop/laptopcategorieën | Eén rij; werkelijk passende categorieën direct zichtbaar. Rest met volledige sublinks onder Meer categorieën. Geen horizontaal schuiven of tweede rij. |
| Tablet/telefoon | Onder990CSS-px bestaand menu. Brede tablet/laptop kan de passende enkele rij gebruiken; apparaatnaam is geen vaste layoutkeuze. |
| Zonder scripts | Native Alle categorieën-details met bestaande bestemmingen. |
| Tegelcalculator | Verse start1m², 10% snijverlies behouden; opgeslagen expliciete keuzes en handmatige dozen blijven werken. Ongeldige invoer blijft blokkeren. |
| Informatieknop | Native popup naast Bereken je bestelling met vloer-/wanduitleg, Sluiten/Escape/focusterugkeer; NL/EN. |

## Verificatie en grenzen

**Dertien CSS-breedtes 320–1920px:** geen document- of categorierail-overloop; vanaf990px één48pxrij. In de gebruikte fixtures990/1024:7direct+4Meer;1180/1280:9+2;1366enbreder11direct. Deze aantallen zijn meetresultaten, geen vaste limieten. Meer opent binnen viewport, ArrowDown/Escape/focus getest. Tablet820:Menu→Douche→Terug→Escape. Open mobiel menu sluit bij resize naar1366zonderbodylock.

**Tien lokale regressies PASS**, Theme Checkrevisie3 allezevenfiles geldig. Echte tegel-PDP begint1m²/10%;10m²→8dozen/11,44m²;0m² geeft fout/geblokkeerd/geen oud totaal. Native informatiepopup en Escape/focus/body-scroll gecontroleerd. Echte concept-homepage visueel bekeken. Tijdelijke QA-template exact teruggezet.

Dit is Cloud Chrome en componentframes met echte conceptcode, geen fysieke telefoon/tablet/Windows-, touch-hardware-, volledige checkout-, mailbox-, ranking- of performancevrijgave. Geen echte cart-, order- of formulieractie. Settings_data/retourtemplate-bodyuitzonderingen behouden; beide niet geüpload.

## Exact één volgende handeling

**Eigenaar opent bij Webshop→Thema’s het Voorbeeld van BadkamerCity - Compact menu en tegelinformatie, controleert eigen laptop/tablet/telefoon en publiceert daarna zelf.** Geen publicatie door uitvoerder.

## Bestaande reparaties en open taken behouden

FIX-01 is nu LIVE door eigenaarspublicatie: cartbevestiging, Sunshower pending/onzekere add, definitieve native filterterugval, Toon minder, zoektelling, tegelprijseenheden, wishlist-intents en echte footerlinks/SEO. De eerdere lege calculatorstart is door de nieuwe expliciete opdracht vervangen door1m². [Oorspronkelijke FIX-01](repairs/2026-10-31/README.md) · [herstel verwijderd concept](repairs/2026-10-31/recovery/README.md).

- **Retouraanmelding:** bestaande live Page166668894474, handmatige native contactaanvraag. Mailontvangst/spam/antwoord en labellevering nog onbewezen; geen automatisch RMA/label/refund gebouwd. [Publicatie](returns/2026-10-30/PUBLICATION.md).
- **Offerte:** deze taak wijzigt geen activatie of account/verificatie. Het bestaande verificatie-/ontvangst-/opslag-/verwijderbewijs blijft open; geen privéaccountpoging. [Integratie](quote/2026-10-30/INTEGRATION.md).
- **Hygrometer:** eerdere twee redirects naar bestaande /pages/hygro-meter behouden; in deze taak niet opnieuw alle redirects getest.
- **Filters/wishlist:** eerdere grenzen voor omgekeerd bereik/APIbeleid, URLdialecten, responseidentity, facetzoeker, oudere/no-Locks-tabversies, opgeslagen corrupte/dubbele arrays en productread-timeout/TTL blijven open. Niet als nieuwe productie-incidenten opgevoerd.
- **QC-04:** afzonderlijke privétool op quality-control; geen privébeoordelingen gelezen of Shopify-productmutatie uitgevoerd.

[Het naslagwerk](MASTER_SITE_REFERENCE.md) blijft het gedateerde DOC-04-boek met80hoofdstukken. Oude NAV-02-rijen/publicatierollen zijn historisch en vervangen door deze actuele status en NAV-03. De registers behouden hun eigen peildatum. Geen Windows-controle geclaimd.
