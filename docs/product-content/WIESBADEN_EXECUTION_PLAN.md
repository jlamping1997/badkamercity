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

De laatste gelezen Git-queue, commit `880fbd29779d0741e8b69c9b435350301c604b1d`, vermeldt **217 oorspronkelijk ontbrekende SKU's: 111 gepubliceerd, 78 positief geprijsd in de queue, 28 zonder bruikbare positieve prijs**. Dat is een overdrachtscheckpoint, geen actuele aftelling.

Een nieuwe Shopify-read op **21 oktober 2026, 20:59:43 UTC** bevestigt **2.388 ACTIVE en 2.388 op Online Store gepubliceerde Wiesbaden-producten**, EUR en `taxesIncluded=true`. MAIN is `195491168522`; er zijn geen themamutaties uitgevoerd.

Tijdens deze overname werden nog producten aangemaakt. Een begrensde read-only vergelijking van de 78 oude queue-SKU's om **21:01:52 UTC** vond 24 bestaande artikelen: twaalf gepubliceerd en twaalf op dat moment nog niet gepubliceerd. De laatste twaalf zijn tussen 20:59:59 en 21:00:41 UTC aangemaakt. De oude uitvoering liep dus nog uit. **Start geen tweede Shopify-schrijver.** De eerste uitvoerstap is na afronding van die run één verse vergelijking op SKU; reeds aangemaakte producten hervatten bij hun ontbrekende stap.

De oude telling 61 gepubliceerd / 128 over is achterhaald. Ook 111 / 78 is geen bevroren eindstand. Trek aantallen uit verschillende verzamelingen niet van elkaar af om ontbrekende artikelen te schatten.

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

**Bronbetekenis eenmalig vastleggen.** De CSV noemt het relevante veld `advertentieprijs (excl. btw)`, maar bij gecontroleerde artikelen zijn de bedragen gelijk aan bekende consumentenadviesprijzen inclusief btw. Bijvoorbeeld SKU 24.3710: CSV €209, fabrikantadvies €209 en een retailer vermeldt €209 inclusief btw. De kolomkop alleen is daarom geen grond voor een algemene verhoging van 21%.

Gebruik voor reeds onderbouwde fabrikantconsumentenprijzen het bestaande inclusieve prijscontract. Leg tijdens dezelfde proef van 20 producten de betekenis van het CSV-prijsveld vast, met bron en datum. Een duidelijke inclusieve of exclusieve mapping geldt vervolgens voor de betreffende bron/veldversie; niet opnieuw per artikel op internet onderzoeken. Een afwijkend bedrag of onopgeloste bronbetekenis krijgt een gerichte uitzondering, zonder de overige verwerking stil te zetten. Gebruik nooit de bruto- of inkoopprijs als stilzwijgende vervanging van de adviesprijs.

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

Bekende uitzonderingen blijven zichtbaar:

- De 28 eerder ongeprijsde nieuwe kandidaten opnieuw tegen de nieuwe CSV vergelijken; hun oude blokkade is geen permanente uitsluiting.
- SKU 41.3563 heeft in deze CSV geen positieve advertentieprijs.
- De 106 bestaande reviewartikelen blijven online. Eerdere inhoudelijke bronconflicten blijven gerichte uitzonderingen.
- Productaanmaak voor 20.3447, 41.3676 en 41.3523 was eerder door connectorveiligheidscontrole geblokkeerd. Bewaar die reden; niet via een andere route omzeilen. Reeds geblokkeerde toevoegingen aan oudercollecties blijven eveneens apart.
- De externe zoek-/filterindex krijgt een eigen geverifieerde status. Een ontbrekende indexsync mag niet als geslaagd worden afgevinkt en houdt correcte basispublicaties niet tegen.

**Afgerond betekent:** alle artikelen uit de vastgelegde scope zijn verantwoord als gepubliceerd/bijgewerkt, al correct, of concreet geblokkeerd. Elk nieuw gepubliceerd artikel heeft een unieke identiteit, correcte positieve consumentenprijs, bruikbaar beeld, passende categorie en geverifieerde Online Store-publicatie. Bestaande inhoudelijke verbeteringen zijn behouden. Er blijft één korte uitzonderingenlijst over, met reden en benodigde oplossing.

Dit is ook het patroon voor een groter assortiment: dezelfde regels en uitvoerroute, alleen gewijzigde records verwerken, geen menselijke werkronde per 50 producten. Meet de doorvoer tijdens de proef; geef pas daarna een onderbouwde looptijd.

## 8. Huidige uitvoerstatus

In deze overname zijn brononderzoek, prijsbeleid, Git-overdracht en een beperkte Shopify-baseline uitgevoerd. **Er is vanuit deze chat nog geen product gewijzigd, geen liveproef uitgevoerd en geen achtergrondverwerker gestart.** De waargenomen eerdere uitvoering moet eerst eindigen.

**Exact volgende handeling:** zodra de eerdere schrijver klaar is, één verse SKU-vergelijking uitvoeren en de proefpayload voor 20 producten volgens dit plan samenstellen.

### Onderbouwing

- [Laatste overgenomen queuecheckpoint](https://github.com/jlamping1997/badkamercity/blob/880fbd29779d0741e8b69c9b435350301c604b1d/docs/product-content/wiesbaden/ONLINE_FIRST_165_TO_PUBLISH_2026-10-21.json).
- [Fabrikantadviesprijs SKU 24.3710](https://www.wiesbaden.nl/304-wastafelkraan-met-coldstart-geborsteld-rvs-24-3710.html) en [retailervermelding inclusief btw](https://www.warmteservice.nl/Wiesbaden/Sanitair/Kranen/Wastafelkranen/c/6150-wiesbaden), gelezen 21 oktober 2026. Dit ondersteunt het genoemde voorbeeld en is geen bewijs voor ieder CSV-record.
- [Shopify bulkimport](https://shopify.dev/docs/apps/build/apis/graphql-admin/bulk-operations/imports) en [productSet-semantiek](https://shopify.dev/docs/api/admin-graphql/latest/mutations/productSet): gebruik bulk voor doorvoer en behoud bestaande lijsten bij gerichte wijzigingen.
