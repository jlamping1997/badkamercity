# Verlavio keuzemenu’s — 7 november 2026

> **Update 8 november 2026:** dit menuconcept is inmiddels MAIN; alle vijf productiefiles zijn exact gelijk aan de gecontroleerde versie. De eigenaar heeft bovendien winkelbreed doorverkopen toegestaan: 767 policies naar CONTINUE, 73 voorraadblokkades opgeheven. [Actuele bestelafspraak en bewijs](../../../orderability/2026-11-08/README.md). Het onderstaande beschrijft het eerdere checkpoint van 7 november.

## Resultaat en status

De eigenaar heeft uitvoering van de eerder gecontroleerde menuverbeteringen goedgekeurd. De productgegevens zijn toegepast en volledig teruggelezen. De nieuwe presentatie staat in het conceptthema **196341825802 — BadkamerCity - Verlavio keuzemenus 7 nov**. Publicatie door de eigenaar is nog nodig; de Shopify-koppeling ondersteunt geen theme-publicatie of MAIN-filewrites.

Bron en actuele MAIN bij aanvang: **196246372618 — BadkamerCity - Groene voorraadmelding**. De native themakopie is na voltooiing voor **1.385 van 1.385 bestanden checksum-identiek** bewezen, inclusief de metadatahash van config/settings_data.json. Die instellingfile is niet geschreven.

Codebranch: **fix/product-cards-2026-10-14**. Bronmap: **shopify/current/**. De release heeft vijf hieronder genoemde productiefiles plus één geneutraliseerd controletemplate in het concept; zie de expliciete einddiff. Bestaande lokale wijzigingen in header, main-product en Lagoo-files zijn behouden; connectorwerk bewijst geen schone Windows-werkboom.

## Waarom en wat verandert

Het bestaande script bouwde een kleur-fototabel waarin het laatste product van dezelfde kleur won. Daardoor kon een ronde set de foto van een vierkante set tonen. De navigatie naar het product zelf klopte al.

De nieuwe, expliciet op Verlavio/Fabriecio begrensde renderer kiest de unieke fotobestemming op kleur én alle overige huidige keuzewaarden. Alle zes kleuren staan direct zichtbaar. Complete douchesets tonen Kleur, Vorm doucheset, Bevestiging hoofddouche en Formaat hoofddouche. Losse hoofddouches hebben hun eigen labels. Clickwastes tonen Met overloop/Zonder overloop. Numerieke afmetingen sorteren oplopend en krijgen spaties rond eenheden.

Vertaalde labels zijn uitsluitend weergave: Muur, Ja/Nee, kleuridentiteiten en alle andere ruwe waarden blijven behouden. Producten blijven afzonderlijke Shopify-producten met dezelfde URL’s. De renderer verandert steeds één keuze, kiest geen willekeurige bestemming bij ambiguïteit en behoudt de bestaande preview-/positie-/winkelwagenafhandeling. Andere merken houden de bestaande weergave en navigatie.

### Productiediff

- assets/bc-product-switcher.js
- snippets/bc-fabriecio-choices.liquid
- assets/bc-verlavio-choices.css (nieuw)
- locales/nl.json
- locales/en.default.json

De locale-files zijn gebaseerd op verse MAIN-inhoud. De bestaande tijdelijke voorraadvertaling uit MAIN is ook behouden; die sleutel ontbrak nog in Git. Geen all_products-lookups of extra productdatabron toegevoegd.

## Toegepaste Admin-gegevens

Bestaand veld: custom.fabriecio_choices, type json. **481 eigenaars** gewijzigd met verse server-compareDigest, tien proefartikelen gevolgd door begrensde batches; iedere batch direct teruggelezen. Alle 481 daadwerkelijke JSON-strings zijn exact gelijk aan het voorbereide plan.

| Wijziging | Aantal | Eigenaars |
| --- | ---: | ---: |
| Fotoverwijzingen naar het juiste huidige doelproductbeeld | 494 | 191 |
| Eigen product als winnaar bij de huidige kleur in de oude renderer | 406 | 406 |
| Bewezen vervallen keuzewaarden verwijderd | 30 | 28 |
| Numerieke waardenvolgorde gecorrigeerd | 15 | 15 |

De eigen rij krijgt uitsluitend sort_order=max+1. Dat maakt de datacorrectie ook met de nog live oude renderer veilig. De products-arrayvolgorde blijft gelijk. Alleen foto’s toevoegen zonder deze correctie zou bestaande verkeerde kleurwinnaars zichtbaar laten worden.

Verwijderingen betreffen uitsluitend de eerder verwijderde definitief vervallen SKU’s SF-004-9070, SPL-80, BR-7008D-90, DDC_700, DM-120B-OK en DM-80W-OK. Geen algemene voorraadfilter, overige productverwijdering of productoptiewijziging.

Alle 4.761 productrecords, groep-ID’s, handles, URL’s, titels en ruwe opties zijn behouden. De teruggelezen niet-menuvelden product-ID, titel, handle, merk, type, status, webshop-URL en hoofdafbeelding zijn voor alle gewijzigde producten exact gelijk gebleven. Prijzen, voorraadaantallen, verkoopbeleid en publicatiestatus zijn niet geschreven.

De eerdere 90 goedgekeurde productfoto’s blijven gekoppeld. Het expliciet overgeslagen losse overloopartikel ACS_6001 blijft overgeslagen; dit is niet hetzelfde als de legitieme met/zonder-overloopkeuze van clickwastes. De Lagoo-fotoafspraak en andere merken blijven buiten deze wijziging.

## Bewijs en grenzen

- [Toegepaste data](data-verification.json): echte oude live JS opnieuw uitgevoerd op de opgeslagen afterwaarden. **4.096 geldige overgangen, 1.299 huidige selecties en alle 4.761 records behouden**. Nul verkeerde kleurwinnaars, nul ontbrekende/oude fotoreferenties en nul overgebleven bewezen vervallen waarden.
- [UI-tests](ui-tests.json): **19/19** tests van de daadwerkelijke gedeelde JS met jsdom 31.0.0. Inclusief oude foutreproductie, exacte SKU-routes, onmogelijke/ambigue keuzes, vertalingen, previewparameters en byte-identieke controls/navigatie voor ongewijzigde merken.
- [Themacontrole](theme-validation.json): **5/5** productiefiles geldig met de byte-identieke Shopify-skillvalidator. Ontbrekende npm-dependencies uit de lokale cache geïnstalleerd; de validator gebruikte bestaande officiële schemas nadat online documentupdate niet bereikbaar bleek.
- [Kopiecontrole](clone-parity.json): volledige 1.385/1.385 pariteit vóór de vijf wijzigingen.
- Echte Chrome: BC_2009 → BG_2009 behoudt rond/25 cm/plafond; BG_2009 → BG_2015 behoudt goud/25 cm/plafond en toont de juiste vierkante foto; CLW_6001 → CLW_6002 behoudt koper en toont Zonder overloop.
- Een te snel opeenvolgende browseractie tijdens het laden kwam eerst bij Mat zwart uit. Na expliciet wachten op paginalading en opnieuw waarnemen van de bediening slaagden de bedoelde kleur- en vormwissels. Geen ongefundeerde claim over snel klikken tijdens een nog verschuivende pagina.
- [Eindcontrole](final-verification.json): MAIN volledig ongewijzigd; concept exact vijf productiediffs plus één geneutraliseerd controletemplate. De eigen server-rendered component toont op 320 en 390 CSS-pixels alle zes geladen foto’s, drie kolommen en geen horizontale overloop. [Browsermetingen](browser-proof.json). Een fysieke telefoon, checkout en betaling zijn niet getest. Geen winkelwagenmutatie nodig voor deze menuwijziging.

De 370 niet gewijzigde producten gebruiken in de samengestelde grafiek hun verse prewritewaarden; zij zijn geen schrijfdoel. Variant-ID’s en SKU’s voor de overgangshash komen uit de eerder gelezen catalogus. De laatste write-readback omvatte die variantvelden niet; zie de expliciete bewijsgrenzen in data-verification.json.

De reproduceerbare beperkte UI-tests staan in scripts/verlavio-menu-tests. Gebruik Node ^22.22.2, ^24.15.0 of >=26 (getest met 24.22.1); installeer daar de vastgelegde dependencies met npm ci en voer npm test uit. De oude scriptfixture dient uitsluitend als vergelijkingsbasis en mag niet worden gedeployed.

## Voorraadkwestie

BC_2008 en BC_2009 hebben nul Shopify-voorraad, tracking aan, DENY en availableForSale=false. De opnieuw gelezen leveranciersfeed bevestigt N. BG_2009 heeft eveneens een onbekend exact aantal/nul Shopify-voorraad, maar leveranciersstatus Y en bestaand CONTINUE, dus is bestelbaar.

De instelling bc_temporary_in_stock=true overschrijft alleen de zichtbare voorraadtekst. Dat verklaart Op voorraad naast Uitverkocht; de koopknop is niet door het menu defect geraakt. De eerdere expliciete wens om tijdelijk overal Op voorraad te tonen is niet stil teruggedraaid. Geen voorraadaantal verzonnen en geen nabestellen aangezet. Herstel van die tijdelijke tekst of een bewuste nabestelafspraak vraagt een gerichte vervolgbeslissing van de eigenaar.

## Tijdelijke controletemplate

De browserbreedtecontrole gebruikte tijdelijk templates/product.bc-verlavio-review.liquid op uitsluitend het concept. Verwijderen van alleen deze file via themeFilesDelete is door de Shopify-koppeling geblokkeerd met de algemene regel “Theme deletion is blocked”. Die grens is niet omzeild. De file is met de toegestane UNPUBLISHED-upsert volledig overschreven en exact teruggelezen: commentaar plus de standaard main-product-sectie, zonder QA-interface, iframes, scripts of layout none. [Definitieve inhoud](neutralized-qa-template.liquid). Deze taak heeft geen product aan deze template toegewezen. Een statische sectie hoeft niet dezelfde blokinstellingen te hebben als templates/product.json; daarvoor wordt geen pariteit geclaimd. Het resterende bestand is verklaard in de volledige einddiff en hoeft voor het vernieuwde menu niet gebruikt te worden.

## Publicatie en herstel

De eigenaar beoordeelt en publiceert **uitsluitend het genoemde Verlavio-keuzemenuconcept**. Controleer vlak vóór publicatie opnieuw MAIN en de einddiff, zodat een tussentijds gepubliceerd ander concept niet wordt teruggedraaid. Lees na publicatie de nieuwe MAIN-rol en de vijf filehashes terug en controleer de drie bovenstaande productroutes.

Codeherstel: het oorspronkelijke MAIN-thema is niet geschreven. Dataherstel: de eigenaar heeft een privébestand **Verlavio-keuzemenus-herstelpakket-2026-11-07.zip** met oorspronkelijke/nieuwe waarden, hashes, daadwerkelijke readbacks en scripts. Gebruik voor herstel altijd een nieuwe server-compareDigest en vereis dat de huidige waarde nog gelijk is aan de verwachte afterhash; nooit blind een oude export overschrijven.

De volledige catalogus, leveranciersfeed, herstelwaarden en Admin-receipts zijn niet in deze publieke repository opgenomen.

