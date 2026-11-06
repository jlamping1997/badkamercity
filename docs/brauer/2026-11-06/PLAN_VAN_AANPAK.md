# BRAUER op Badkamercity

Plan van aanpak en brononderzoek · 6 november 2026 · uitwerking 2

**Status: aanpak door Jackson positief beoordeeld; btw in prijs bevestigd. Brononderzoek, btw-berekening en eerste categorisatie-/proefuitwerking gereed. Geen BRAUER-producten geïmporteerd of gepubliceerd.**

## Update: btw en concrete voorbereiding

Jackson heeft bevestigd dat de btw in de prijs moet zitten. Voor alle 13.161 artikelen is daarom de adviesprijs inclusief 21% btw berekend: adviesprijs ex btw × 1,21, commercieel afgerond op twee decimalen. De voorbereide consumentenprijs gebruikt diezelfde basis, zonder aangenomen korting. De originele ex-btw-prijs blijft behouden. Dit stelt geen marge of kortingsbeleid vast.

Voorbeeld: `5-CE-001` heeft adviesprijs €155,10 ex btw en €187,67 incl btw. De winkel staat bij de verse read-only controle al op `taxesIncluded=true`. Het importontwerp moet daarom de consumentenprijs inclusief btw gebruiken en geen tweede btw-opslag toepassen. Er zijn geen winkelbrede belastinginstellingen gewijzigd. Afwijkende Markets/checkoutbelasting blijft onderdeel van de proef.

Voor elk exact artikelnummer ligt ook een producttypevoorstel klaar. Dat is een inhoudelijke classificatie, geen opdracht om voor elk type een nieuwe collectie te maken. Technische conflicten blijven apart. De 31 proefartikelen zijn op hun expliciete bronkenmerken uitgewerkt; voor deze 31 zijn in de hele Shopify-catalogus via SKU- en barcodezoekingangen geen bestaande matches gevonden. Een volledige SKU/EAN-botsingscontrole voor de andere artikelen is nog niet uitgevoerd.

De bestaande specificatieroute moet voor Brauer eerst gericht in preview worden aangepast: Brauer valt nu op de legacy-weergave. Alleen `custom.complete_specificaties` vullen garandeert dus geen zichtbare volledige meubel-/glasinformatie. Ook leverteksten op kaart en winkelwagen moeten voor Brauer expliciet worden aangesloten en getest.

Zie de concrete vervolgspecificatie in `UITWERKING.md`. De beschrijvingen verderop zijn het basisplan; bovenstaande vastgelegde besluiten vervangen de eerdere lege prijsbasis en prijskeuze als eerste blokkade.

## 1. Aanbevolen route

Maak één centraal artikelregister voor de drie programma's. Bereid daarin prijzen, categorieën, eigenschappen, echte keuzefamilies en media voor. Bewijs daarna met een kleine, gevarieerde proef dat het artikel klopt van productkaart tot winkelwagen. Pas dan volgt de volledige conceptimport en een gefaseerde publicatie.

De prijslijsten zijn een goede start, maar geen volledige webshopcatalogus. Eerst alles publiceren en daarna de samenstelling en techniek herstellen levert onnodig herstelwerk op. We kunnen het meeste voorbereidende werk nu doen, terwijl de afbeeldingen en PDF's onderweg zijn.

Gebruik de bestaande Badkamercity-componenten. Bouw nu geen aparte BRAUER-selector, universele meubelconfigurator of nieuwe complete categorieboom. Dat vergroot onderhoud voordat de benodigde bronrelaties bewezen zijn.

## 2. Wat de drie bestanden werkelijk bevatten

Alle bestanden hebben één werkblad, `Blad1`, en dezelfde veertien kolommen. Alleen echte artikelregels tellen mee; lege opgemaakte rijen niet.

| Bron | Artikelregels | Bestandsversie |
| --- | ---: | --- |
| Meubelprogramma | 8.687 | 13 oktober 2026 |
| Kranenprogramma | 3.374 | 13 oktober 2026 |
| Glasprogramma | 1.696 | 28 oktober 2026 |
| Totaal bronregels | 13.757 | Drie originele bestanden |
| Unieke exacte artikelnummers samen | **13.161** | Voorlopige catalogusscope |

**372 artikelnummers staan in meerdere bestanden:** 224 in alle drie, 148 in twee. Dat zijn 596 extra bronregels, geen 596 verschillende producten. Eén artikel mag meerdere relevante collectieplaatsen krijgen, maar wordt niet driemaal aangemaakt.

Binnen elk bestand zijn de SKU's uniek. Alle 13.757 EAN-vermeldingen hebben een geldig EAN-13-controlecijfer; er zijn geen EAN's die verschillende SKU's verbinden. Alle adviesprijzen zijn positief. Bij overlappende SKU's zijn geen prijs-, EAN-, titel- of levertijdconflicten gevonden. Een geldige EAN-checksum bewijst niet onafhankelijk de fabrikantregistratie.

De bronkolommen zijn: artikelcode, EAN, merk, productomschrijving, adviesverkoopprijs exclusief btw, levertijd, hoofdcategorie, productcategorie, productgroep, serie, uitvoering, materiaal, kleur en afwerking.

Er zijn geen aparte kolommen voor lange omschrijving, gestructureerde maatvoering, stelmaten, gewicht, afbeeldingen, technische PDF's of componentlijsten. Een deel van de technische gegevens staat wel in de omschrijving en kan gecontroleerd worden overgenomen met bronverwijzing.

### Concreet gevonden aandachtspunten

| Bevinding | Gevolg en voorgestelde verwerking |
| --- | --- |
| Alle bronprijzen zijn adviesprijzen EX btw | Bron behouden; voor alle artikelen advies incl 21% en voorbereide consumentenprijs zonder korting berekend. Korting/marge afzonderlijk; geen Shopify-prijzen geschreven. |
| 163 unieke artikelen hebben beschikbaarheid vanaf 1 februari 2027 | Apart behandelen. Geen voorraadclaim vandaag; pas als verwachte beschikbaarheid tonen na actuele bevestiging. Geen automatische vrijgave enkel omdat de datum verstrijkt. |
| 7.826 meubelregels vermelden vijf weken levertijd | Geen algemene korte levertijd voor BRAUER gebruiken. Prijslijst is een momentopname, geen live voorraadfeed. |
| 371 overlappende SKU's verschillen in minstens één veld | Veel verschillen zijn categoriebenamingen. Deze normaliseren naar bestaande winkelcategorieën; ze zijn niet allemaal koopblokkades. |
| 27 overlappende SKU's verschillen in materiaal | Onder meer RVS304 tegenover oplopende RVS-codes in de nieuwere glaslijst. Niet automatisch het nieuwste bestand laten winnen. Materiaalveld in onderzoek houden. |
| Twee overlappende SKU's verschillen in afwerking | `5-S-149` en `5-S-221`: Mat tegenover Geborsteld. Bron bevestigen voordat filter/menu/specificatie wordt vastgezet. |
| 36 meubelregels heten Lichtlijst maar staan onder Spiegeldeuren | Gerichte, herleidbare classificatiecorrectie voorbereiden. Vijf topbladbeugels missen een productgroep. |
| Zes paren kranenaccessoires hebben dezelfde titel en prijs | Verschillende SKU's en EAN's behouden. Onderzoek bijvoorbeeld `5-CE-013` tegenover `5-CE-153`; niet dedupliceren op naam. |

De veldverschillen zijn: hoofdcategorie 371, productcategorie 60, productgroep 118, materiaal 27 en afwerking 2. Deze aantallen overlappen en mogen niet worden opgeteld tot een aantal probleemartikelen.

## 3. Git en bronbestanden

De bestaande repository `jlamping1997/badkamercity` is openbaar. Daar leggen we dit plan, taken, bronchecksums, leesbare mappings, controlecode en veilige samenvattingen vast. De bestaande codebranch blijft `fix/product-cards-2026-10-14`; actuele themabron is `shopify/current/`. Geen nieuwe branch per programma.

De oorspronkelijke leveranciers-XLSX's en volledige afgeleide artikelbestanden blijven buiten publieke Git. Publieke verspreidingsrechten zijn niet vastgesteld; de onderzochte Topa-downloadroute vraagt inloggen. Voor het werkelijk samen onderbrengen van alle brondata in remote Git is een private catalogusrepository de voorgestelde route. Die is in deze fase nog niet aangemaakt. Grote fotopakketten/PDF's horen in passende bestandsopslag, met een mediaregister en checksums in plaats van duizenden binaire bestanden in de themarepository.

Het projectpakket bevat de originele bronnen, audit, artikeloverzicht en dit plan. Iedere bronwaarde houdt bestandsnaam, werkblad en rijnummer. Handmatige correcties worden afzonderlijk bewaard met reden en bewijs; bronbestanden blijven intact.

## 4. Productstructuur en keuzemenu's

**Voorgestelde basis: één exacte fabrikant-SKU per Shopify-product, met één verkochte variant.** Dit sluit aan op de bestaande productlinkkeuzes. Een toekomstige bewuste uitzondering is mogelijk, maar wordt eerst op techniek, SEO en beheer beoordeeld. Geen wijziging van bestaande productmodellen van andere merken.

De primaire sleutel is BRAUER plus exact artikelnummer. EAN is een controleveld, geen vervangende importsleutel. Voor de eerste write ook exact SKU/EAN vergelijken met de hele bestaande winkel, inclusief eventuele verkeerd benoemde merken. De nulmeting geeft nul producten voor zowel vendor BRAUER als vrije zoekterm Brauer; dat is nog geen volledige SKU-voor-SKU-botsingscontrole.

Behoud fabrikant-SKU, EAN, bronlabels en bronprijs. Maak titel, handle, korte uitleg, filterwaarden en groepen als afzonderlijke afgeleide velden. Een handle is geen permanente identiteit. Bij gelijke titels voorkomt een herkenbaar SKU-onderscheid handlebotsingen.

Hergebruik de V2 cross-product switcher. Groepeer op werkelijk hetzelfde technische model en expliciete dimensies. Elke volledige keuzecombinatie verwijst naar precies één bestaand artikel. Kleur wisselen mag geen ongevraagde maat, model, aansluiting, draairichting of setinhoud wijzigen. Onmogelijke combinaties zijn niet klikbaar. Een singleton krijgt geen leeg keuzemenu. De volledige familie moet correct laden, ook bij grote groepen.

### Per programma

| Programma | Aparte kenmerken en relaties |
| --- | --- |
| Kranen | Serie, model, Carving/Stripe, kleur, afwerking, coating, basismateriaal, montage, uitloop, bediening. Bij douches ook hoofddouchemaat, muur-/plafondarm, handdouche en glijstang. Losse thermostaat, inbouwdeel, afbouwdeel en complete set onderscheiden. |
| Glas | Serie/constructie, nominale maten, verstelbereik, glasdikte, beslagkleur, glaskleur, Carving/Flow, openingstype en bevestigde omkeerbaarheid. Complete opstelling, los glasdeel en setgebonden pakket onderscheiden. |
| Meubels | Serie/uitvoering, breedte/diepte/hoogte, kleur/materiaal, laden/deuren, draairichting, kraangat(en), wastafelpositie, grepen, bodemplaat en verlichting. Losse onderkast, front, topblad, wastafel en complete samenstelling onderscheiden. |

RVS-kleurig is een kleur, geen bewijs van RVS als basismateriaal. PVD alleen vastleggen waar het voor het exacte artikel bevestigd is. `Chroom,Helder` bij glas wordt beslagkleur plus glaskleur; geen onduidelijke samengestelde kleurfilter. Geen stelmaten uit nominale breedte afleiden. Geen meubelcompatibiliteit afleiden uit alleen gelijke breedte of gelijke kleur.

Voor sets gebruiken we drie verschillende relaties: **inbegrepen**, **extra nodig** en **optioneel**. Een artikel met in- en afbouwdelen is niet daardoor een complete regendoucheset. De bron moet exacte component-SKU's en aantallen bevestigen. Hergebruik het bestaande setblok en waar passend de optionele inbouwdeeltoevoeging. De officiële setprijs en setvoorraad blijven leidend; geen optelsom van losse delen in plaats van de verkochte set.

## 5. Eerst ontbrekende informatie efficiënt aanvullen

Vraag BRAUER/Topa eerst om een uitgebreid productbestand of PIM-export, naast de WeTransfer-media. Dat kan veel sneller en betrouwbaarder zijn dan duizenden losse PDF's verwerken. Gewenste velden: exacte SKU/EAN, lange tekst, technische maten, stelmaten, gewicht/verpakking, componentrelaties, actuele status en bron-/wijzigingsdatum. Vraag tevens om de actuele voorraad-/levertijdroute, onderscheid uitlopend/nieuw en toestemming voor webshopgebruik van beelden/documenten.

Gebruik daarna wat werkelijk wordt aangeleverd. Verwerk bestaande gestructureerde gegevens vóór PDF-uitlezing; lees alleen ontbrekende technische informatie uit officiële tekeningen/handleidingen. Geen complete concurrentenscrape als eerste stap. Badkamervoorjou.nl blijft uitgesloten als bron.

### Media koppelen op artikelnummer

Bestandsnamen met SKU zijn een goede start, maar niet automatisch voldoende bewijs. Eén artikel kan meerdere foto's en documenten hebben. Een sfeerfoto kan accessoires tonen die niet worden meegeleverd.

Maak per bestand een register met oorspronkelijk pad/naam, exact gevonden SKU, rol (productfoto, detail, sfeer, maattekening, installatie, onderhoud), volgorde, checksum en controle-uitkomst. Exacte match gaat vóór gecontroleerde naamregels. Alleen afgesproken suffixen zoals een fotovolgnummer verwijderen; streepjes/cijfers niet algemeen wegpoetsen. Fuzzy matches alleen voorstellen, nooit automatisch koppelen.

Meld onbekende bestanden, ontbrekende hoofdfoto's, meerdere mogelijke SKU's en conflicterende versies. Dezelfde afbeelding mag alleen gedeeld worden na expliciete artikeldekking; gedeelde checksum kan een geldige sfeerfoto zijn en is geen automatische fout. Productfoto en hoofdfoto moeten exact de juiste uitvoering tonen. PDF's op type en revisie controleren. Vóór publicatie minimaal één correcte bruikbare productfoto per aangeboden artikel; conceptvoorbereiding kan eerder.

## 6. Werkvolgorde met concrete oplevering

| Stap | Werk en resultaat | Wanneer door? |
| --- | --- | --- |
| BRAUER-01 | Drie bronnen inventariseren, combineren en afwijkingen registreren. Plan en productoverzicht opleveren. | Uitgevoerd als bronanalyse; geen koopgereedheidsclaim. |
| BRAUER-02 | Prijsbeleid, verkoopscope en bronprioriteiten vaststellen. Eigen prijscorrecties en toekomstige beschikbaarheid apart beheren. | Definitieve verkoopprijsregel en beleid voor toekomstige/uitlopende artikelen vastgelegd. |
| BRAUER-03 | Categorie-, veld- en filtermapping voorbereiden. Technische kenmerken uit expliciete brontekst halen; ontbrekende gegevens gericht aanvullen. | Alle 13.161 SKU's verklaard: gepland, apart beoordeeld of uitgesloten met reden. |
| BRAUER-04 | Familierelaties en onderdelenrelaties maken. Verwachte UI per type vastleggen. | Iedere combinatie uniek, technisch consistent en herleidbaar; onbekend blijft onbekend. |
| BRAUER-05 | WeTransfer-media inventariseren en koppelen. Alleen resterende gaten uit officiële bronnen aanvullen. | Correcte beelden/documenten per vrij te geven artikel; uitzonderingenlijst beschikbaar. |
| BRAUER-06 | Representatieve conceptproef, circa 8-12 SKU's per programma. Geen openbare catalogusuitrol. | Productkaart, PDP, keuzes, prijs, documenten en echte winkelwagen op desktop/mobiel kloppen. |
| BRAUER-07 | Goedgekeurde data in hervatbare logische batches, bijvoorbeeld 100-250 artikelen, als concept voorbereiden. API-aanroepen aanpassen aan werkelijke limieten. | Alle geschreven records teruggelezen; geen onverklaarde verschillen of dubbele producten. |
| BRAUER-08 | Collectie-, filter-, merkroute- en indexmapping voorbereiden en in preview controleren. Concepten niet publiek indexeren. | Verwachte groepen, filters en gegevens in preview kloppen; indexplan gereed. |
| BRAUER-09 | Jackson beoordeelt proef en uitzonderingen. Daarna geschikte deelgroepen publiceren, controle na iedere groep. | Status, Webshop, publieke pagina en bestelbaarheid bevestigd; daarna publieke SKU-/prijs-/zoekindexdekking controleren. |
| BRAUER-10 | Onderhoudsafspraken: nieuwe prijslijst/voorraadbron, wijzigingenrapport en beschermde handmatige correcties. | Herhalen maakt geen duplicaten en verandert alleen toegestane velden. |

Media en data-aanvulling kunnen parallel lopen. De eerste technische proef opmaken zodra de belangrijkste voorbeeldartikelen compleet zijn; niet wachten tot elke optionele specificatie van alle 13.161 artikelen bekend is. Start de webshopproef met kranen omdat die goed aansluit op de bestaande selector. Neem glas en meubels meteen mee als architectuurproef; begin niet met duizenden eenvoudige kranen voordat een lastige meubelsamenstelling is getest.

**Volgende concrete handeling:** de benodigde officiële productdata en media voor de 31 proefartikelen koppelen en de Brauer-preview voor specificaties en leverinformatie voorbereiden. De prijsbasis en eerste classificatie zijn uitgewerkt. Volledige import en publicatie volgen pas na de beschreven controles.

## 7. Voorstel voor de proefselectie

Onderstaande 31 SKU's bestaan in de aangeleverde lijsten. Ze zijn geselecteerd om fouten te vinden, niet als voorspelling van bestsellers. Een grotere familietest mag extra verwante SKU's gebruiken zodra deze volledig gecontroleerd zijn.

De toekomstige artikelen `5-CF-024` en `5-CF-008` zijn negatieve beschikbaarheidsproeven: zij mogen niet onbedoeld bestelbaar worden. De winkelwagenproef gebruikt reguliere vrijgegeven pilots. Nabijheid in onderstaande tabel bewijst geen compatibiliteit; bijvoorbeeld `OK-BE100GG` en `BP-BE100CH` zijn geen voorgestelde combinatie. Voor een echte componenttest voegen we zo nodig extra bewezen passende SKU's toe.

| Programma | Exacte SKU's | Wat moet bewezen worden? |
| --- | --- | --- |
| Kranen | `5-CE-001`, `5-GG-001` | Kleur/coating en prijs; zelfde kraanmodel. |
| Kranen | `5-CE-001-HD6`, `5-CE-001-HD7` | Carving en Stripe zichtbaar onderscheiden. |
| Kranen | `5-CE-024`, `5-CE-026`, `5-GG-024` | Hoofddouche 20/30 cm en kleur onafhankelijk kiezen. |
| Kranen | `5-CE-018RR`, `5-CE-013`, `5-CE-153`, `5-CF-024` | Thermostaat/setrol, gelijke titels met eigen identiteit, toekomstige beschikbaarheid. |
| Glas | `GS-CSN1H70200CE`, `GS-CSN1H70200GG` | Zelfde nisdeur en maat bij twee beslagkleuren. |
| Glas | `GS-GTC1H12090200CE`, `GS-CLI1H100200CE`, `GS-VOB1B80140CE` | Cabine, inloop en badwand; glaskleur en maatvoering. |
| Glas | `GL-D1H100`, `GP-GTD1H120200CE`, `GB-GD1CE`, `DB-AS100100MW` | Losse deur, deelpakket, beslag en douchebak niet verwarren. |
| Meubels | `OK-AR100CH`, `FO-AR40LCH`, `FO-AR40RCH` | Onderkast en links/rechts bij fonteinmeubels. |
| Meubels | `OK-EL100CH`, `OK-BE100GG`, `BP-BE100CH` | Uitsluitingen zoals grepen/bodemplaat; passende extra's eerst bevestigen. |
| Meubels | `WT-AU1000HW`, `WT-AU1001HW`, `SK-IMD100CH`, `MB-LFAR100CH`, `5-CF-008` | Kraangaten, spiegelkast en los front; toekomstige voorraad. |

## 8. Controle vóór publicatie

Automatiseer volledige controles waar mogelijk en controleer de echte kooproute daarnaast in de browser. Een veldvergelijking alleen bewijst geen goede webshop.

| Onderdeel | Minimale voorwaarde |
| --- | --- |
| Identiteit | Exact één bedoeld product per SKU; EAN/merk gecontroleerd, geen stille dubbele matching. |
| Prijs | Bevestigde verkoopprijs en btw-weergave op kaart/PDP/cart consistent. Geen adviesprijs als kortingsreferentie zonder goedgekeurd prijsbeleid. |
| Productrol | Klant ziet duidelijk complete set of los onderdeel; inbegrepen en benodigd niet vermengd. |
| Techniek | Essentiële koopmaten en compatibiliteit bewezen. Bij glas verstelbereik controleren; bij meubels passende delen; bij inbouwkranen in-/afbouwinhoud. |
| Levering | Geen actuele voorraadclaim op basis van oude tekst; toekomstige voorraad apart. Verzendwijze en tarief voor glas/meubels vooraf vastgesteld, geen fictief gewicht voor berekening. |
| Media | Juiste productfoto/uitvoering, werkende relevante PDF, geen vreemde of ontbrekende assetkoppeling. |
| Keuzes | Kleur/maat/model behoudt overige keuzes waar technisch mogelijk; onbeschikbare combinaties eerlijk zichtbaar; eigen SKU/foto/prijs/URL wisselen samen. |
| Vindbaarheid | Juiste bestaande collecties, filtercombinaties, SKU-zoekingang en externe indexopname. Niet 13.161 vrijwel gelijke resultaten zonder familiegroepering waar het bestaande systeem groepen gebruikt. |
| SEO | Begrijpelijke unieke titel, betekenisvolle brongebonden tekst, vaste URL, canonical, interne links, passende Product/Offer-data en overeenkomende prijs/voorraad. Geen automatische lege serie-/kleurpagina's. |
| Aankoop | Pilot werkelijk toevoegen, wijzigen en verwijderen in cart. Levering/verzendtarief tot relevante checkoutstap controleren; geen betaling/echte bestelling zonder aparte opdracht. |

Een onbekend optioneel veld hoeft niet elk goed product tegen te houden. Een onzekere kleur, verkeerd bedrag, ontbrekend vereist onderdeel of onbekende essentiële inbouwmaat is wel reden om dat artikel apart te houden. Publicatie volgt per geschikte deelgroep, niet op basis van alleen totaalpercentages.

## 9. Onderhoud en herstel

Bewaar per import product-ID, variant-ID, SKU, bronversie, mappingversie en gecontroleerde uitkomst. Eerst een verschilvoorstel, daarna begrensde writes, daarna teruglezing. Afgebroken batches veilig hervatten; herhalen moet nul onnodige writes en nul nieuwe duplicaten geven. Geen generieke overschrijving van bestaande collecties, afbeeldingen of handmatige verbeteringen.

Voor rollback alleen de eigen nieuwe product-ID's en publicaties terugzetten; nooit andere merken of alle winkelproducten. Een eventuele themeaanpassing gebeurt in een opnieuw gecontroleerd concept op basis van actuele MAIN. Hergebruik bestaande componenten zonder eerdere merkcorrecties te verliezen.

Een latere feed koppelt op leverancier plus exact SKU en beheert alleen afgesproken prijs-/voorraad-/levertijdvelden. SEO, eigen tekst, compatibiliteit, media en handmatige prijsafspraken blijven beschermd. Meld nieuwe/vervallen artikelen, verpakking/prijsconflicten en verouderde broninformatie. Er is nu geen BRAUER-feed, geplande achtergrondtaak of voorraadautomatisering ingericht.

## 10. Besluiten die Jackson moet nemen

1. **Prijsbeleid:** btw in de prijs is bevestigd. Adviesprijs inclusief 21% is de voorbereide consumentenprijs zonder korting. Eigen verkoopkortingen zijn nog niet afgesproken; dat houdt de verdere datavoorbereiding niet tegen. Inkoopafspraken zijn nodig voor een echte margecontrole en blijven privé.
2. **Verkoopscope:** alle zelfstandige artikelen meenemen; losse fronten en onderdelen als zodanig presenteren. Eventuele samengestelde meubelsets pas toevoegen na een bevestigde samenstelling, prijs en logistiek.
3. **Toekomstige artikelen:** voorlopig concept houden is de aanbevolen standaard. Voorbestelling alleen met bewuste klanttekst en actuele leveranciersbevestiging.
4. **Logistiek:** leverbeleid, verzending en retourafhandeling voor glas en meubels bevestigen vóór koopvrijgave.
5. **Bronopslag:** volledige bronnen in private catalogus-Git als gewenst; publieke themarepo alleen voor code/plan/mappings en veilige samenvattingen.

De werkzaamheden staan in `TAKEN.md`. De bijgewerkte Excel toont het artikelregister, advies ex btw, berekende adviesprijs incl btw, voorbereide consumentenprijs en de bronverschillen. Catalogusindeling, familieaantallen, kortingsbeleid en productgereedheid zijn nog niet definitief.

## Bronnen en bewijsgrenzen

- Drie aangeleverde BRAUER-prijslijsten, ongewijzigd onderzocht; namen en SHA256 in `BRONMANIFEST.json`.
- Read-only Shopify op 6 november 2026: nul BRAUER-producten via vendorfilter en vrije zoekterm. MAIN tijdens deze ronde: `196246372618` - BadkamerCity - Cottoceramix volledig assortiment. Dit is alleen een rolmeting, geen Cottoceramix-kooptest of nieuwe unitvrijgave.
- Bestaande projectafspraken: `AGENTS.md`, `docs/CATEGORIZATION_AND_SEO_POLICY.md`, `docs/architecture/PRODUCT_DATA.md`, `docs/architecture/components/PRODUCT_CHOICES.md` en bestaand setcomponentdossier.
- Officiële verkoopmaterialen: https://topa-import.com/products/21/nl/Verkoopmateriaal . De onderzochte downloadverwijzing leidde naar inloggen; de exacte aangeleverde bestanden zijn niet als openbaar gedistribueerd bevestigd.
- Officiële programma-informatie: https://www.brauerkranen.nl/site/nieuwe-doucheopstellingen-brauer-glasprogramma . Officiële handleidingen: https://www.brauerkranen.nl/site/installatie-handleidingen-kranen . Geen volledige fabrikantcatalogus of alle PDF's onderzocht.
- Geen omzetpotentieel, bestsellerranglijst, livevoorraad, huidige handelskorting, technische compatibiliteit of levertijdgarantie afgeleid uit deze nulmeting. Niet uitgebrachte Shopify-/browser-/checkouttests blijven open.
- Btw-bron: Belastingdienst, algemeen tarief 21%, gecontroleerd 6 november 2026: https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/tarieven_en_vrijstellingen/goederen_diensten_21_btw/ . De prijsberekening is een voorbereiding voor de Nederlandse consumentenprijs; geen wijziging van belastinginstellingen of bewijs van grensoverschrijdende checkout.
