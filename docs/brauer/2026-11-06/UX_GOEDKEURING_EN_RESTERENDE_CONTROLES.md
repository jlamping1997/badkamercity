# BRAUER — goedgekeurde keuzemenu-opzet en resterende controles
Datum: 7 november 2026

## Goedkeuring
De eigenaar keurt de huidige opzet goed met de expliciete aanvulling dat ook alle kleurkeuzes de eerste afbeelding van het exact gekoppelde kleurartikel gebruiken. Dit is UX-goedkeuring van het patroon, geen vrijgave van alle brondata of een Shopify-import/publicatie.

Vaste regels:
- Kleuren en decors: eerste afbeelding van het kandidaatproduct dat bij de huidige andere keuzes past; geen willekeurige kleurrepresentant of generieke foto van een ander artikel.
- Zes zichtbare kleuren; Bekijk meer kleuren bij meer dan zes; actieve kleur blijft zichtbaar bij inklappen.
- Zonder productfoto: benoemde staal en Productfoto volgt. Een ontbrekende foto maakt een geldige SKU niet ongeldig. Niet-bestaande combinaties blijven zichtbaar, grijs en niet aanklikbaar.
- Hendels behouden hun afzonderlijke goedgekeurde vormbeelden.
- Twee of drie maatopties: knoppen; grotere groepen: dropdown; enkele waarde niet als extra keuze tonen.
- Standaard en ondiepe meubeluitvoeringen blijven aparte groepen.
- SKU/EAN/btw-prijs volgen het exacte verkoopartikel. Geen stille wissel van andere gekozen eigenschappen.
- Productmedia volgen het gekoppelde product-ID/SKU; toevoegen/herschikken werkt bij verse productdata/render. Geen live push vanuit Shopify Admin geclaimd.
- De huidige offline voorbeelden bevatten slechts 58 tijdelijke referentiefoto's. De officiële volledige beeld-/PDF-ontvangst blijft de importvoorwaarde.

## Resterende, afwijkende logica
Dit zijn brononderbouwde controlegroepen, geen nieuw aangemaakte productfamilies of getelde keuzemenu's. Eén bronproductgroep kan meerdere menu's bevatten.

| Prioriteit | Te beoordelen patroon | Concrete bronvoorbeelden | Huidige dekking |
| --- | --- | --- | --- |
| Eerst | Douchecabines en andere nisdeuren: draai/schuif/draai-schuif, breedte × diepte en opstelling; deur aan wand of glas; omkeerbaarheid als eigenschap houden als het dezelfde SKU is | GS-VOCC1H100100200CE; GS-VOCN2H6030200CE | Huidige glasproef: inloopdouches en Galactic-schuifnisdeur; geen cabineproef |
| Eerst | Andere onderkasten plus wastafels/topbladen: greep, lades, gaten en waskompositie; maat-/afvoercompatibiliteit apart bewijzen | OK-TR100CH (grepen uitgesloten); WT-AU1000HW; WT-AU1000LHW | Joy MFC standaard/ondiep beoordeeld; andere series/complete combinaties niet |
| Daarna | Carving/Stripe en overige douche-/fonteinkranen: verschillende greepstructuren, bedieningen, setopbouw en inkortbaarheid | 5-CE-001-HD6; 5-CE-001-HD7; 5-CE-257; 5-CE-473 | Vooral gladde Edition; foto-inbouwproef alleen chroom |
| Daarna | Hoge kasten, spiegels en spiegelkasten: draairichting, formaat/vorm en aanwezige verlichting/bediening | HK-AD120LCH; SK-IMD100CH; SP-JD100RO | Nog geen proef |
| Laatst | Losse accessoires, douchekoppen/armen en afvoeren: kleuren, maatvarianten en modelverschillen | 5-CE-009; 5-CE-147; 5-CE-016; 5-CE-017 | Nog geen aparte familieproeven |

## Bronmeting
Afgelezen uit de huidige drie oorspronkelijke leverancierslijsten: 13.161 unieke SKU's. De huidige gesprekproef bevat 864 unieke artikelen in 14 voorbeeldgroepen (876 records door bewuste overlap). Dit is geen 100% catalogus- of menudekking.

Indicatieve productgroepdekking, zonder bewering dat ieder bronartikel een keuzevariant is:
- Nisdeuren: 390 bronartikelen, 12 in huidige voorbeelden.
- Douchecabines: 216 bronartikelen, geen voorbeeld.
- Badwanden: 28 bronartikelen, geen voorbeeld.
- Hoge kasten: 443 bronartikelen, geen voorbeeld.
- Fonteinkranen: 57 bronartikelen, geen voorbeeld.
- De brede spiegelgroepen omvatten ook onderdelen; daarom geen aantal als aantal menukeuzes gepresenteerd.

## Vervolg
Controleer eerst één representatieve douchecabine en één wastafel-/onderkastcombinatie met afwijkende logica. Daarna per nieuw gedrag uitbreiden. Gewone kleur-/maatgroepen kunnen met dezelfde geautomatiseerde combinatietests worden gecontroleerd.

De drie eerder aangetroffen maatbronconflicten en geblokkeerde Liquid ThemeCheck blijven open. Geen Shopify-writes, productimport (ook geen DRAFT), media-upload of publicatie uitgevoerd.
