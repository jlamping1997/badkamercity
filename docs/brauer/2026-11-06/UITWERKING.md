# BRAUER - concrete voorbereiding voor de proef

6 november 2026, uitwerking 2. **DATA_PREPARATION_COMPLETE / PILOT_INFORMATION_PENDING.** Jackson bevestigt btw in de prijs en wil de aanpak verder uitwerken. Geen Shopify-producten, collecties, metafields of themabestanden gewijzigd. Dit document beschrijft wat nu concreet is voorbereid en wat de eerste proef moet bewijzen.

## 1. Vastgelegde prijsbasis

Voor alle **13.161** unieke artikelen:

- Originele adviesprijs exclusief btw blijft onveranderd als bronwaarde bewaard.
- Adviesprijs inclusief btw = advies ex btw × 1,21, commercieel afgerond op twee decimalen.
- De voorbereide consumentenprijs is voorlopig gelijk aan die adviesprijs inclusief btw. Er is geen korting ingevoerd of marge afgeleid.
- Geen fictieve compare-at-prijs, actieprijs of kortingspercentage aanmaken.
- Shopify `shop.taxesIncluded` is read-only gecontroleerd en staat op **true**. Geen tweede btw-opslag op deze voorbereide bedragen; geen belastinginstelling wijzigen.
- Productkaart, productpagina en cart moeten bij de proef hetzelfde goedgekeurde bedrag tonen. Market-/adresafhankelijke checkout blijft apart te controleren.

| Exact artikel | Advies ex btw | Advies incl 21% / voorbereide consumentenprijs |
| --- | ---: | ---: |
| 5-CE-001 | €155,10 | €187,67 |
| 5-GG-001 | €234,30 | €283,50 |
| 5-CE-024 | €927,70 | €1.122,52 |
| 5-CE-026 | €1.051,50 | €1.272,32 |
| 5-GG-024 | €1.361,10 | €1.646,93 |

De JSON-prijsvoorbereiding gebruikt decimale half-up-afronding. Alle 13.161 uitkomsten zijn daarnaast onafhankelijk met gehele centen gecontroleerd. De Excel moet dezelfde bedragen leveren, ook op exacte halve centen zoals €244,50 × 1,21 = €295,845, dus €295,85. Alleen een mooi weergegeven bedrag is geen bewijs van correcte afronding.

Btw-inclusief is bevestigd. Eventuele toekomstige commerciële korting is een afzonderlijke wijziging en houdt het huidige datavoorbereidingswerk niet tegen.

## 2. Eén typevoorstel voor ieder artikel

Alle 13.161 SKU's zijn in een voorstel geclassificeerd op hun officiële productgroep, aangevuld met expliciete productcategorie/omschrijving bij geregistreerde bronafwijkingen. Er blijven geen onverklaarde artikeltypen over in dit voorstel. Dat is geen verklaring dat alle technische inhoud, collectievoorwaarden of koopgegevens al goedgekeurd zijn.

Enkele grote groepen:

| Voorgesteld producttype | Unieke artikelen |
| --- | ---: |
| Onderkasten | 2.930 |
| Ladefronten | 1.818 |
| Inbouwdouchesets | 1.692 |
| Topbladen | 742 |
| Spiegelkasten | 589 |
| Hoge kasten | 443 |
| Nisdeuren | 426 |
| Inloopdouches | 390 |
| Inbouwwastafelkranen | 338 |
| Fonteinkasten | 331 |

De overige typen en aantallen staan in `VOORBEREIDING.json`; de expliciete bronlabelmapping in `PRODUCTTYPE_VOORSTEL.json`. Het zijn interne producttypen, geen opdracht om tientallen nieuwe collectiepagina's of menuvertakkingen te publiceren.

### Gerichte correctievoorstellen

| Bronafwijking | Voorstel | Grens |
| --- | --- | --- |
| 36 lichtlijsten onder Spiegeldeuren | Lichtlijsten voor spiegelkasten | Omschrijving zegt expliciet Lichtlijst; originele waarde bewaren. |
| Vijf topbladbeugels zonder productgroep | Topbladbeugels | Expliciete productcategorie en productnaam ondersteunen dit. |
| Dezelfde vijf topbladbeugels als Handdoekbeugels in kranenlijst | Topbladbeugels | Beide andere bronnen en identieke titel controleren; niet als handdoekrek tonen. |
| 5-S-221 als Handdoekhaak in glaslijst | Handdoekrek/-beugel | Alle titels zeggen Handdoekbeugel; andere brongroepen sluiten aan. Afwerkings-/materiaalconflicten blijven afzonderlijk open. |

Bij deze voorstellen zijn geen onbekende maten, materiaalsoorten of compatibiliteitsrelaties ingevuld. De 27 materiaalconflicten en twee afwerkingsconflicten uit het eerste onderzoek zijn niet door meerderheid of bestandsdatum opgelost.

## 3. Aansluiting op de bestaande winkel

Verse inventaris: **227 bestaande collecties** en **258 PRODUCT-metafielddefinities**, volledig gelezen. [VELDEN_EN_COLLECTIES.md](VELDEN_EN_COLLECTIES.md) bevat de mapping van alle veertien bronkolommen plus exacte bestaande collectie-ID's en beperkingen.

Voorbeelden van bestaande bestemmingen: losse onderkasten, wastafelbladen, meubelwastafels, hoge kasten, spiegelkasten, inbouw-/opbouwwastafelkranen, inbouwdouchesets, inloopdouches, douchedeuren en douchecabines. Hoofdgroepen en relevante aanvullende ingangen blijven bestaan.

Er is nog geen Brauer-merkcollectie. Ook zijn er geen exacte collectie-ingangen voor ieder los front, bodemplaat, glaspakket of rooster. Die artikelen krijgen een duidelijk producttype en rol; een bestaande passende onderdeleningang is een kandidaat. Geen losse deur in een collectie complete cabines plaatsen om een ontbrekende categorie te omzeilen. Nieuwe categorieën alleen voorstellen als bestaande ingangen en filters onvoldoende zijn.

### Vier onderdelen voor de preview

1. **Specificaties zichtbaar maken.** De actuele specs-router stuurt Brauer naar legacy. Die route is vooral voor kranen ingericht. Kies een gerichte route naar de bestaande gestructureerde specificatieweergave en test de drie programma's; geen honderden dubbele aliasvelden maken om de oude weergave toevallig te vullen.
2. **Leverinformatie aansluiten.** Kaart en winkelwagen hebben geen algemene Brauer-bronroute. Gebruik een kleine adapter voor de afgesproken leverinformatie op kaart/PDP/cart. Een ongedateerde lijsttekst Uit voorraad leverbaar is geen actuele voorraadmeting.
3. **Keuzes aansluiten.** De bestaande V2-selector blijft leidend. `custom.switch_group` vereist ook een passende complete dataset; alleen een groepsnaam schrijft geen werkend menu. Unieke volledige keuzematch controleren, onmogelijke keuzes niet stil vervangen.
4. **Onderdelen helder tonen.** Inbegrepen, extra nodig en optioneel blijven verschillende relaties. Het bestaande setblok hergebruiken met exacte component-SKU's/aantallen zodra die bevestigd zijn; setprijs blijft de eigen officiële artikelprijs.

Dit zijn implementatievoorwaarden voor de proef, nog geen toegepaste theme-aanpassingen. Eerst de actuele MAIN opnieuw controleren, een passende previewbasis nemen en andere merkcorrecties behouden.

## 4. De 31 proefartikelen zijn inhoudelijk uitgewerkt

De vaste startselectie bevat elf kranen-, negen glas- en elf meubel-/accessoireartikelen. Elk technisch feit is terug te vinden in de bronrij en het concrete kolom-/tekstfragment. In deze ronde zijn zowel de 31 exacte SKU's als hun 31 EAN's winkelbreed opgezocht: **nul matches**. De complete 13.161-SKU-botsingscontrole blijft een aparte taak vóór de latere volledige import.

### Voorbeelden van de gewenste koopervaring

| Proef | Verwacht resultaat | Wat nog ontbreekt |
| --- | --- | --- |
| 5-CE-001 naar 5-GG-001 | Zelfde lage opbouwkraan model A; Goud/PVD/Geborsteld, foto en prijs wisselen mee. | Echte maatvoering, montage-/leverinhoud, juiste media. |
| 5-CE-001-HD6 naar HD7 | Carving en Stripe zijn zichtbare uitvoeringen, geen ongemerkte kleurwissel. | Technische gelijkheid en volledige kandidaatfamilie bevestigen. |
| 5-CE-024 naar 5-CE-026 | Hoofddouchemaat 20 naar 30 cm; Chroom, rechte muurarm en staafhanddouche blijven. | Geen diameter/vorm of aantal stopkranen afleiden; officiële stuklijst/inbouwinhoud en tekening. |
| 5-CE-018RR | Losse inbouwthermostaat met benoemde in- en afbouwdelen. | Exacte component-SKU's/aantallen; geen complete regendoucheset claimen. |
| 5-CE-013 en 5-CE-153 | Beide eigen SKU/EAN/URL, ondanks gelijke titel. | Fabrikantverschil/opvolging bevestigen; niet samenvoegen. |
| GS-CSN1H70200CE naar GG | Nominale maat 70x200, helder glas en draaiend/omkeerbaar behouden; beslagkleur wijzigt. | Bevestigde maateenheden/assen, stelmaten, glasdikte en exacte leverinhoud. |
| GL-D1H100, GP-GTD1H120200CE, GB-GD1CE | Losse deur, deelpakket en beslagdeel blijven duidelijk onderscheiden. | GB-GD1CE is een beslagonderdeel voor een stabilisatiestang, geen glaswand; exacte passendheid bevestigen. |
| FO-AR40LCH naar RCH | Bewuste links/rechts-keuze; niet veranderen bij alleen een kleurkeuze. | Technische tekeningen/maatvoering en media. |
| OK-EL100CH en OK-BE100GG | Exclusief grepen/bodemplaat zichtbaar bij de koopinformatie. | Exact passende onderdelen bevestigen; geen standaardcombinatie raden. |
| WT-AU1000HW naar WT-AU1001HW | Nul naar één kraangat als expliciete technische keuze. | Tekening, overige maten en compatibele onderkast. |
| MB-LFAR100CH | Ladefrontenset als onderdeel tonen, geen complete onderkast. | Inhoud/aantallen en passende kastversies bevestigen. |

De volledige exacte SKU-selectie staat in hoofdstuk 7 van het basisplan. De extra technische uitwerking is brononderzoek, geen zelfstandige verklaring dat deze artikelen al koopgereed zijn. Een familie kan aanvullende bewezen SKU's vragen voordat een echte selectorproef mogelijk is.

`5-CF-024` en `5-CF-008` blijven negatieve toekomstproeven. De bron noemt 1 februari 2027. De datum mag niet automatisch een actieve voorraadclaim of bestelknop opleveren. Voorlopig concept houden; alleen na bewuste preorder-/leverafspraak een andere route maken. Alle 163 toekomstige SKU's blijven in de voorbereiding gemarkeerd.

## 5. Wat we nu als volgende doen

De verdere voorbereiding hoeft niet op de laatste optionele specificatie van elk artikel te wachten. Richt het eerst op de proef:

1. Bestaande officiële productdata/PIM en de aangeleverde media koppelen aan de 31 proefartikelen. De huidige prijslijsten hebben geen beeld-/documentkolommen. Bestandsnamen met SKU zijn een koppelsleutel; verkeerde uitvoering en gedeelde documenten blijven controlepunten.
2. Alleen de ontbrekende essentiële informatie opvragen/uit officiële documenten halen: bij glas stelmaten en leverinhoud, bij meubels uitsluitingen en passendheid, bij kranen maten en in-/afbouwinhoud.
3. Een Brauer-preview voorbereiden met correcte specificatieroute, leverinformatie, V2-dataset en echte productrollen. Geen volledige generieke meubelconfigurator bouwen.
4. Daarna de kleine DRAFT-proef maken, geschreven gegevens teruglezen en de werkelijke productkaart/PDP/cart op desktop en mobiel controleren. Toekomstige pilots blijven een negatieve test; reguliere cartproef gebruikt vrijgegeven producten.
5. Na een goede proef de hervatbare volledige conceptimport voorbereiden. Publieke zoekindex pas controleren na vrijgegeven publicatie; concepten niet publiek indexeren.

De voorbereide consumentenprijs is nu helder. Er is geen nieuwe prijskeuze nodig om met mapping/media/proefvoorbereiding door te gaan. Publicatie volgt op de concrete productreview en benodigde technische-/logistieke controles, zoals afgesproken in het basisplan.

## Bron en grenzen

Drie oorspronkelijke BRAUER-prijslijsten, de eerder vastgelegde SHA256's, huidige Shopify-read-only inventaris en actuele MAIN196246372618. De berekening gebruikt 21% voor Nederlandse consumentenprijzen. Bron: Belastingdienst, https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/tarieven_en_vrijstellingen/goederen_diensten_21_btw/ . Geen live voorraadfeed, fabrikantcompatibiliteitsmatrix, browser-/cartproef of nieuwe prijs-/belastingmutatie uitgevoerd.
