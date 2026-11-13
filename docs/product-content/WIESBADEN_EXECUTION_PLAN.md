# Wiesbaden — vast uitvoeringsplan

**Vastgesteld op 21 oktober 2026 op verzoek van de eigenaar.** Eén aanpak voor het volledige merk, één schrijver, één proef van maximaal 20 producten en daarna doorlopende verwerking. Dit plan vervangt de werkwijze met telkens een nieuwe handmatige opdracht voor 50 producten.

- Actieve werkbranch: `fix/product-cards-2026-10-14`.
- Actuele fase en eerstvolgende handeling: [execution-state.json](wiesbaden/execution-state.json).
- Bestaande bronqueue: [ONLINE_FIRST_165_TO_PUBLISH_2026-10-21.json](wiesbaden/ONLINE_FIRST_165_TO_PUBLISH_2026-10-21.json). De bestandsnaam is historisch; vóór uitvoering altijd vergelijken met actuele Shopify-SKU's.
- Eerdere dossiers blijven bewijs van hun eigen meetmoment. Dit plan en de nieuwste status bepalen de uitvoering.

## 1. Opdracht en afbakening

Maak het Wiesbaden-assortiment compleet en verwerk de beschikbare productdata efficiënt. Eerst de geschikte ontbrekende artikelen online; vervolgens de afgesproken prijzen, teksten, specificaties, categorieën, beelden en filtergegevens voor de volledige merkset afwerken. Gebruik de bestaande geslaagde productweergave en eerder gecontroleerde inhoud.

De eigenaar hanteert de **adviesverkoopprijs inclusief btw**. Inkoopprijzen bepalen de verkoopprijs niet. De eigenaar kan dezelfde proef van 10–20 producten zelf bekijken; er komt geen verplichte nieuwe toestemming per technische deelbatch. De nieuwste opdracht geldt voor Wiesbaden-productdata en dit plan. Themaherontwerp, andere merken, homepage, checkout, betaal- en belastinginstellingen vallen buiten deze uitvoering. Voorraad-/levertijdkoppeling blijft de eerder afgesproken vervolgfase.

## 2. Vertrekpunt en overdracht

**De Shopify-uitvoering is voltooid: `SHOPIFY_COMPLETE_INDEX_BLOCKED`.** De overname en de uitvoering met één Shopify-schrijver zijn afgerond; er is geen Shopify-schrijver of achtergrondworker meer actief. De volledige uitgangssnapshot van 21 oktober 2026, 21:46:12 UTC bevat 2.449 Wiesbaden-producten. De eerdere waarnemingen van een gelijktijdige schrijver en de telling 2.388 om 20:59:43 UTC zijn historische overdrachtsbewijzen, geen resterende startvoorwaarde.

De oorspronkelijke bronqueue van 217 ontbrekende SKU's is nu verantwoord als **186 Online Store-gepubliceerd, 28 zonder positieve geverifieerde prijs en 3 historische platformveiligheidsblokkades**. De laatste twee nieuwe artikelen, **33.6000 en 75.3510**, zijn ACTIVE én expliciet op Online Store gepubliceerd en teruggelezen. De drie geblokkeerde creates zijn niet opnieuw geprobeerd. De historische queuenaam blijft behouden; de inhoud van de [actuele queue](wiesbaden/ONLINE_FIRST_165_TO_PUBLISH_2026-10-21.json) bepaalt de stand.

**2.299 geautoriseerde prijsverschillen zijn geschreven en onafhankelijk teruggelezen.** De verrijking is volledig uitgevoerd en teruggelezen: 2.166 reguliere kandidaten plus 107 expliciet vrijgegeven bestaande reviewartikelen, samen **2.273 producten en 12.259 metafields**, met **0 uitvoeringsuitzonderingen**. De 151 reeds gecontroleerde contentproducten blijven beschermd; 25 bestaande producten zonder exacte fabrikantbron behouden hun bestaande gegevens. De definitieve Admin-tellingen zijn **2.451 totaal, 2.451 ACTIVE en 2.451 Online Store-gepubliceerd**, alle met precisie `EXACT`.

De historische tellingen 61/128, 111/78 en 184/5 zijn geen actuele werklijsten. Het private geverifieerde journal sluit de Shopify-uitvoering af; reeds gemaakte producten en reeds teruggelezen wijzigingen worden niet herhaald. De volgende concrete stap is bestaande SSH-authenticatie voor de externe zoek-/filterindex beschikbaar maken en daarna die index synchroniseren en controleren.

## 3. Eén prijsregel

| Onderdeel | Uitvoerregel |
| --- | --- |
| Klantprijs | Adviesverkoopprijs inclusief btw in EUR |
| Aantoonbaar exclusieve adviesprijs | Exact eenmaal vermenigvuldigen met 1,21 |
| Reeds inclusieve adviesprijs | Overnemen zonder extra btw |
| Exact inclusief bedrag boven €100 | Normaal afronden op de dichtstbijzijnde hele euro; een halve euro naar boven |
| Exact inclusief bedrag tot en met €100 | Afronden op centen |
| Rekenvolgorde | Eerst btw, daarna direct de eindafronding; geen tussentijdse centafronding |
| Inkoopprijs | Alleen optioneel als interne kostprijs; nooit in klantprijs, tekst, SEO of openbare gegevens |
| Lege, ongeldige of nulprijs | Bestaande geldige prijs behouden; alleen het betreffende nieuwe artikel tegenhouden |

Gebruik exacte decimalen. Voorbeelden: €80,00 excl. wordt €96,80; €120,00 excl. wordt €145; €149,49 incl. wordt €149; €149,50 incl. wordt €150. €100,41 excl. wordt direct €121, omdat het exacte bedrag €121,4961 is. Eerst afronden naar €121,50 en vervolgens €122 zou fout zijn.

**Bronbetekenis vastgesteld voor deze bronversie.** De CSV-kop `advertentieprijs (excl. btw)` wordt voor het vastgelegde Wiesbaden-bestand expliciet overruled: de bedragen zijn fabrikantconsumentenadvies **inclusief btw**, factor 1,00. Dezelfde binding geldt voor `source_advice_eur` uit de gekoppelde fabrikantcache; het oude exclusieve cachelabel is achterhaald. De [prijsbronkalibratie](wiesbaden/PRICE_SOURCE_CONTRACT_2026-10-21.md) legt de bronhashes, 20 officiële prijsvoorbeelden en de exacte overeenkomst van alle 2.411 CSV-bedragen met de cache vast.

Deze bronbinding geldt niet automatisch voor een ander merk of een toekomstige feedversie. Een aantoonbaar exclusieve adviesprijs krijgt eenmaal 21% btw. Gebruik nooit bruto- of inkoopprijs als stilzwijgende vervanging van de consumentenadviesprijs. De 2.299 uitgevoerde prijsverschillen zijn afzonderlijk teruggelezen; de bronnotitie alleen is geen uitvoerbewijs.

De nieuwe afrondregel geldt ook voor bestaande Wiesbaden-producten. Maak daarvoor eenmaal een volledige prijsvergelijking en schrijf alleen verschillen. Behoud bestaande inhoudelijke bescherming bij tekst-/specificatievelden; die bescherming verhindert een geautoriseerde prijsaanpassing niet. Shopify kan gehele eurobedragen intern als `145.00` opslaan; het bedrag bevat dan geen centen. Een wijziging van de algemene prijsweergave van het thema is geen onderdeel van deze prijsrun.

## 4. Bronnen en samenvoegen

De aangeleverde `1186(2).csv` bevat 4.048 artikelen, waarvan **2.411 Wiesbaden**, met unieke artikelcodes en 2.410 positieve advertentieprijzen. SHA-256: `80d2d72aea47073fbd185f94a46e23f6fbb3b8812889131717dfbc438090dc2e`.

Gebruik samen:

1. De ongewijzigde leveranciers-CSV voor assortiment, prijsbron, namen, categorievoorstellen en beeldlinks.
2. De al verzamelde fabrikantcache `BadkamerCity_Wiesbaden_datarun_20261019.zip` voor rijkere productfeiten en bronmateriaal.
3. Eén actuele Shopify-inventarisatie voor product-/variant-ID's, bestaande inhoud, prijs, media en publicatiestatus.
4. Bestaande categorie-/veldregels, publicatieregister, reviewregister en goedgekeurde productvoorbeelden.

Koppel op merk/leverancier plus **exact artikelnummer als tekst**. EAN is geen unieke sleutel in deze feed. Behoud punten en nullen; creëer geen product op basis van een gelijkende titel.

Lege CSV-attribuutkolommen wissen bestaande specificaties niet. Bewaar oorspronkelijke brondata, ook wanneer een onbetrouwbaar veld niet wordt gepubliceerd. Maak foto-URL's uniek voordat ze worden verwerkt. Een lijntekening blijft een lijntekening. Neem relevante informatie over afzonderlijk te bestellen inbouwdelen of setonderdelen over; verzin geen volledigheid of compatibiliteit.

Prijs- of verpakkingseenheden niet zelf vermenigvuldigen/delen zonder expliciete bronbetekenis. De ja/nee-voorraad uit deze download is geen actuele voorraadkoppeling. Een artikel dat niet in deze CSV staat wordt niet automatisch verwijderd of gearchiveerd.

De repository is publiek: leveranciersbestand, inkoopprijzen, ruwe winkelback-ups en volledige uitvoeradministratie blijven privé. Git bevat plan, code, bronhash, veilige tellingen en verwijzingen.

## 5. Uitvoering in vijf stappen

| Stap | Werk | Klaar wanneer |
| --- | --- | --- |
| 1. Overnemen en vergelijken | Vorige run afronden; één schrijver vastleggen. De oude queue op actuele SKU/ID/publicatiestatus controleren. Daarnaast CSV, fabrikantset en winkel exact vergelijken. | Eén werklijst met toevoegen, gericht bijwerken, al goed en uitzondering; geen dubbele creaties. |
| 2. Bestaande verwerking afmaken | Bestaande bron-/mappingcode hergebruiken en alleen de ontbrekende uitvoerlaag toevoegen: gericht schrijven, voortgang opslaan en hervatten. | Eén uitvoerroute kan voorgestelde wijzigingen toepassen, teruglezen en veilig hervatten. |
| 3. Eén proef met 20 producten | Nieuwe én bestaande artikelen, verschillende productgroepen, prijzen onder/boven €100 en enkele bronuitzonderingen. Prijsbinding, inhoud, categorie, media en publicatie controleren. | Geen kritieke fout in identiteit, prijs/btw, setbetekenis, publicatie of behoud van bestaande data. Corrigeer een gevonden algemene regel en controleer alleen die correctie opnieuw. |
| 4. Geschikte werklijst doorlopen | Eerst resterende nieuwe producten publiceren. Daarna alle overige relevante prijs-/inhoudsverschillen voor Wiesbaden verwerken. | Iedere geplande wijziging is toegepast en teruggelezen, was al gelijk, of staat met concrete reden op de uitzonderingenlijst. |
| 5. Afsluiten | Resultaattellingen sluitend maken; dezelfde proefproducten na afloop controleren. Bestaande zoek-/filterindex synchroniseren wanneer de huidige route beschikbaar is. | Eindrapport met aantallen, afwijkingen en expliciete indexstatus; geen onverklaarde resterende werkitems. |

**Geen nieuwe handmatige opdracht per 50.** Technische pagina's of batches mogen klein zijn vanwege API- of bestandslimieten; de uitvoerder gaat vanzelf door tot de werklijst afgehandeld is. De huidige previewlimiet van 50 mag geen bedrijfsproceslimiet worden.

Hergebruik `scripts/wiesbaden-data-run.py`, `scripts/wiesbaden-import-plan.py`, de selectie-/previewhelpers en bestaande gedeelde productcomponenten. Bouw geen nieuw PIM of nieuwe website. Beperk nieuwe code tot wat nodig is voor één hervatbare uitvoerroute. Gebruik een beschikbare geautoriseerde bulkroute waar die past; gerichte updates mogen geen niet-aangeleverde varianten, collecties of metadata verwijderen.

## 6. Controle zonder handmatig ieder product na te lopen

De automatische basiscontrole loopt mee met de verwerking: juiste SKU/ID, positieve prijs volgens het vaste contract, behoud van bestaande gegevens, resultaat van de bedoelde wijziging, en voor nieuwe publicaties bruikbare media plus Online Store-publicatie. Lees wijzigingen gegroepeerd terug; geen herhaalde volledige catalogusaudit.

De inhoudelijke steekproef bestaat één keer uit maximaal 20 uiteenlopende producten. Gebruik de bestaande goedgekeurde weergave als referentie. Tekst en filterwaarden moeten passen bij de beschikbare productfeiten; een vaste minimumlengte, een minimumaantal specificaties of een ontbrekend optioneel veld is geen reden om een volledig artikel tegen te houden.

Alleen een algemene fout die veel artikelen kan raken stopt de betreffende verwerking. Een losse bron-/mediafout wordt apart geregistreerd en de overige artikelen lopen door. Een inhoudelijk conflict blokkeert alleen het betrokken veld, tenzij daardoor de artikelidentiteit, prijs of aangeboden set onduidelijk is.

## 7. Hervatten, uitzonderingen en afronden

De uitvoerder bewaart privé per artikel de bronversie, geplande verschillen, Shopify-ID's, oude waarden en laatst bevestigde stap. Eén schrijver heeft een exclusief uitvoerslot. Na een onderbreking eerst bestaande SKU/ID/status terugvinden; daarna uitsluitend de ontbrekende stap uitvoeren. Een verloren API-response is geen reden opnieuw een product te creëren. Tijdelijke fouten krijgen een beperkt aantal herpogingen; een blijvende fout gaat naar de uitzonderingenlijst.

Een terugzetactie herstelt alleen de door deze run gewijzigde velden uit de private back-up en overschrijft geen latere wijziging van iemand anders. Nieuw aangemaakte producten worden bij een ernstige fout uit de verkoop gehaald voor correctie; niet automatisch verwijderd.

Bekende uitzonderingen en behoud blijven zichtbaar:

- De 28 historische nieuwe kandidaten zonder positieve prijs zijn opnieuw met CSV/cache vergeleken: 27 ontbreken in de CSV; de ene match `41.3563` heeft eveneens nulprijs. Er is voor geen van de 28 een positieve geverifieerde prijs. Zij blijven afzonderlijke prijsuitzonderingen.
- Productaanmaak voor `20.3447`, `41.3523` en `41.3676` was eerder door connectorveiligheidscontrole geblokkeerd. Die acties zijn niet opnieuw geprobeerd en worden niet via een alternatieve route omzeild.
- De 107 bestaande eerdere holds hebben gerichte identiteit- en veldreviews gekregen. Alleen bevestigde feiten komen in de afzonderlijke verrijkingspayload; onbekende compatibiliteit, setinhoud en concrete bronconflicten blijven op veldniveau weggelaten. Dit verandert hun publicatiestatus niet.
- De 151 eerdere gecontroleerde contentproducten blijven beschermd. De 25 bestaande producten zonder exacte fabrikantbron worden niet verwijderd, gearchiveerd of op basis van een prijsaanname aangepast.
- De externe zoek-/filterindex staat op **BLOCKED_NO_EXISTING_SESSION_AUTH**. Er is geen geslaagde indexsync geclaimd. Dit houdt correcte Shopify-productwijzigingen niet tegen.
- Voor de volledige galerijen is geen sluitend bewijs beschikbaar. Alleen een bevestigde foto of een begrensde mediaconnectie bewijst geen complete galerij.

**Afgerond betekent:** alle artikelen uit de vastgelegde scope zijn verantwoord als gepubliceerd/bijgewerkt, al correct, of concreet geblokkeerd. Elk nieuw gepubliceerd artikel heeft een unieke identiteit, correcte positieve consumentenprijs, bruikbaar beeld, passende categorie en geverifieerde Online Store-publicatie. Bestaande inhoudelijke verbeteringen zijn behouden. Er blijft één korte uitzonderingenlijst over, met reden en benodigde oplossing.

Dit is ook het patroon voor een groter assortiment: dezelfde regels en uitvoerroute, alleen gewijzigde records verwerken, geen menselijke werkronde per 50 producten. Meet de doorvoer tijdens de proef; geef pas daarna een onderbouwde looptijd.

## 8. Huidige uitvoerstatus

**`SHOPIFY_COMPLETE_INDEX_BLOCKED` — de Shopify-uitvoering en eindverificatie zijn afgerond.** De externe zoek-/filterindex is nog niet gesynchroniseerd omdat bestaande sessie-authenticatie ontbreekt.

| Onderdeel | Actuele stand |
| --- | --- |
| Prijsverschillen | **READBACK_VERIFIED — 2.299** |
| Laatste nieuwe artikelen | **READBACK_VERIFIED — 33.6000 en 75.3510, ACTIVE én Online Store** |
| Oorspronkelijke bronqueue | **186 online / 28 prijsuitzonderingen / 3 historische safetyblocks niet herprobeerd** |
| Proefgroep | **20 producten uitgevoerd en teruggelezen** |
| Bronverrijking | **COMPLETE / READBACK_VERIFIED** — 2.273 producten, 12.259 metafields, 33.186 specfeiten, 6.345 filters en 1.368 documentlijsten; **0 uitzonderingen** |
| Zichtbare inhoud en SEO | **COMPLETE / READBACK_VERIFIED** — 187 unieke producten: 3 gerichte correcties en 184 eerder lege SEO-records; **0 uitzonderingen** |
| Hoofdcategorieën | **COMPLETE / READBACK_VERIFIED** — 87 toevoegingen aan 5 bevestigde handmatige collecties; bestaande lidmaatschappen behouden. 46 gevallen zonder voldoende bron niet gewijzigd |
| SEO-normalisatie en openbare controle | 14 identieke SEO-titels door Shopify genormaliseerd naar `null`; effectieve producttitel en exacte SEO-description teruggelezen. **18184 openbare headcheck PASS** |
| Winkeltellingen | **READBACK_VERIFIED / EXACT** — 2.451 totaal, 2.451 ACTIVE en 2.451 Online Store-gepubliceerd |
| Winkelinstellingen en thema | **EUR**, `taxesIncluded=true`; **MAIN 195491168522 ongewijzigd** |
| Uitvoeringsbewijs | Afgesloten tellingen en behoudregels staan in de [machineleesbare status](wiesbaden/execution-state.json) en het [uitvoeringsresultaat](WIESBADEN_EXECUTION_RESULTS_2026-10-21.md); volledige payloads en readbackjournal blijven privé |
| Externe index | **BLOCKED_NO_EXISTING_SESSION_AUTH**, niet gesynchroniseerd |

De actuele bronregels zijn `2026-10-21.4`. Concreet conflicterende IP-/materiaalvelden en negatieve seteigenschappen zijn uit de betreffende specs, filters en markerkeys verwijderd; overige betrouwbare feiten blijven behouden. De reviewmarker verklaart uitsluitend de toegestane specificaties, documentenroute en gecontroleerde categoriecontext. Hij keurt bestaande titel, body of SEO niet automatisch goed.

De 87 hoofdcategorietoevoegingen zijn met dezelfde `productUpdate`-uitvoering via `collectionsToJoin` verwerkt, nadat de 5 doelcollecties als handmatig waren bevestigd. Alle bestaande collectielidmaatschappen zijn behouden. De 28 prijsuitzonderingen en 3 historische veiligheidsblokkades blijven open; de drie geblokkeerde creates zijn niet opnieuw geprobeerd.

**Exact volgende handeling:** bestaande SSH-authenticatie voor de externe zoek-/filterindex beschikbaar maken en daarna de index synchroniseren en controleren. Shopify-metafieldreadback bewijst geen externe indexsync. De afgeronde Shopify-wijzigingen worden niet opnieuw uitgevoerd.

Er is na afronding geen Shopify-schrijver of achtergrondworker actief. Volledige galerijdekking is niet bewezen. Brondata, volledige payloads, before-snapshots en journals blijven privé. Actieve werkbranch blijft `fix/product-cards-2026-10-14`; `main` ontvangt alleen documentatie.

### Onderbouwing

- [Laatste overgenomen queuecheckpoint](https://github.com/jlamping1997/badkamercity/blob/880fbd29779d0741e8b69c9b435350301c604b1d/docs/product-content/wiesbaden/ONLINE_FIRST_165_TO_PUBLISH_2026-10-21.json).
- [Fabrikantadviesprijs SKU 24.3710](https://www.wiesbaden.nl/304-wastafelkraan-met-coldstart-geborsteld-rvs-24-3710.html) en [retailervermelding inclusief btw](https://www.warmteservice.nl/Wiesbaden/Sanitair/Kranen/Wastafelkranen/c/6150-wiesbaden), gelezen 21 oktober 2026. Dit ondersteunt het genoemde voorbeeld en is geen bewijs voor ieder CSV-record.
- [Shopify bulkimport](https://shopify.dev/docs/apps/build/apis/graphql-admin/bulk-operations/imports) en [productSet-semantiek](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productSet): gebruik bulk voor doorvoer en behoud bestaande lijsten bij gerichte wijzigingen.
