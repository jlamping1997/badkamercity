# Productkwaliteit — uitbreiding van de bestaande QC-tool

11 november 2026 · QC-SEO-01 · status: PLANNED_NOT_IMPLEMENTED.
[SEO-stappenplan](STAPPENPLAN.md) · [Bestaande QC-bron en historie](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/README.md).

## Doel en gekozen route

Jackson wil alle producten in één overzicht, met foto's, PDF's, omschrijving, SEO-inhoud en specificaties; per product zichtbaar wat nu moet worden opgelost en wat kan wachten. Bouw dit als uitbreiding van de bestaande privé-QC, niet als nieuw CRM of tweede productdatabase. Klant-/orderbeheer en extra CRM-functies blijven later.

Bestaande privétool volgens het QC-dossier: https://badkamercity-quality.jason015.chatgpt.site.
Project-ID volgens dossier: appgprj_6ae3d58930e48191b4dea11d39180671.
De bestaande toegang, D1-beoordelingen, notities, identiteit, revisiecontrole en checkpoints behouden. Publieke code staat op quality-control, volledige deploymentbron en gegevens blijven privé. Deze documentatiestap heeft de app/runtime/opslag niet vers gecontroleerd en niet aangepast. Geen actuele catalogusvolledigheid claimen uit de oude momentopname.

## Minimale eerste versie

Eén tabel met zoeken op titel/SKU, filters op merk/producttype/status/probleem en een productscherm met checklist, bron en notitie. Overzicht bevat alle producten uit een volledig gepagineerde actuele inventaris, met ACTIVE/DRAFT/ARCHIVED en kanaalpublicatie apart. Standaard actieve online producten tonen; concept/gearchiveerd bereikbaar via filters.

| Kolom | Te tonen |
| --- | --- |
| Product | Titel, merk, SKU, bestaande Shopify-product-ID en zo nodig variant-ID |
| Webshopstatus | Shopify-status, Online Store-publicatie en controle van bereikbaarheid afzonderlijk |
| Foto's | Aanwezigheid + match/bruikbaarheid onafhankelijk beoordeeld |
| PDF/documentatie | Aanwezigheid + juiste artikelkoppeling, of onderbouwd niet nodig |
| Omschrijving | Aanwezigheid + inhoudelijke review |
| SEO-inhoud | Zoek-/koopvraag beantwoord, concrete ontbrekende informatie en reviewstatus |
| Specificaties | Producttypevereisten, bronbevestiging, missende velden en conflicten |
| Opvolging | Nu oplossen / Binnenkort verbeteren / Kan voorlopig blijven |
| Controle | Laatste bronverversing, laatste beoordeling, opnieuw beoordelen ja/nee |
| Actie | Wat ontbreekt, reden, eigenaar en eventueel leverancier nodig |

In productdetail ook categorie, uitvoering, setinhoud/benodigde onderdelen, prijs-/eenheid en leverinformatie opnemen waar de bestaande checklist dat al ondersteunt. Niet alle detailvelden als drukke tabelkolommen tonen.

Productgroepering voor overzicht; variantcontroles blijven aan de juiste uitvoering gekoppeld. Een foto voor chroom keurt geen zwarte uitvoering goed. Status van een groep moet kritieke variantafwijkingen zichtbaar houden.

## Aanwezigheid is geen goedkeuring

Per onderdeel drie aparte velden: toepasselijkheid, automatische bevinding, inhoudelijk oordeel.

- Toepasselijkheid: vereist / optioneel / niet van toepassing, met reden per producttype.
- Automatische bevinding: aanwezig / ontbreekt / link defect / controle mislukt / nog niet gemeten.
- Inhoudelijk oordeel: nog niet beoordeeld / akkoord / verbeteren / fout / twijfel / opnieuw beoordelen.
- Bewijs: bron, scope, datum, relevante inhoudsvingerafdruk en wie/wat heeft gecontroleerd.

Een PDF is niet voor ieder accessoire nodig. Een aanwezige PDF kan bij het verkeerde model horen. Een omschrijving langer dan een minimum bewijst geen sterke SEO. Automatische vlaggen mogen geen handmatige goedkeuring voorstellen.

“SEO-inhoud akkoord” betekent een afgebakende inhoudelijke beoordeling, geen rankinggarantie: juiste identiteit/uitvoering, duidelijke toepassing, producttypeafhankelijke koopvragen, relevante setinhoud en onderdelen, geen onbewezen voordelen of dubbele opvultekst, passende titel/metadata waar gecontroleerd. Geen vast woordenaantal of misleidende 100/100-score.

## Samenvattende productstatus en prioriteit

| Status | Betekenis |
| --- | --- |
| Nog controleren | Onvoldoende toepasselijke controles uitgevoerd |
| Nu oplossen | Bevestigde koopkritische fout, bijvoorbeeld verkeerde productfoto of onjuiste maat/setinhoud |
| Binnenkort verbeteren | Product bruikbaar, maar relevante informatie of keuzehulp ontbreekt |
| Kan voorlopig blijven | Toepasselijke kritieke controles voldoende; expliciete niet-kritieke restpunten zichtbaar |
| Gecontroleerd | Alle afgesproken toepasselijke controles akkoord of onderbouwd niet van toepassing |
| Opnieuw controleren | Relevante product-/media-/bronwijziging maakt een eerder oordeel verouderd |

Bewaar status en prioriteit afzonderlijk. “Nu oplossen” in de interface is een werkprioriteit, geen automatische Shopify-depublicatie. “Kan voorlopig blijven” is een bewust oordeel met reden en eventuele herbeoordelingsdatum, geen stilzwijgend akkoord door ontbrekende data. Onzeker koopkritisch gegeven toont Twijfel/onderzoek met prioriteit, geen verzonnen zekerheid.

Geen totaalscore die kritieke fouten middelt met vijf groene vinkjes. Eerste sortering: kritieke problemen, daarna verbeterpunten en ongecontroleerde producten; commerciële focus uit SEO-S05 kan een aanvullende filter zijn.

## Actualiteit en hergebruik

- Shopify blijft bron voor producten en actuele winkelvelden. QC bewaart beoordelingen en werkvoorraad, geen tweede bewerkbare catalogusmaster.
- Hergebruik bestaande product-/variant-/media-ID's. SKU alleen is geen unieke technische sleutel.
- Volledig gepagineerde read-only catalogusverversing; importmoment en dekkingsstatus zichtbaar. Een nieuwe of verwijderde SKU niet stil wegfilteren.
- Bestaande oordelen/checkpoints behouden. Alleen getroffen controles opnieuw openen als de relevante inhoud is gewijzigd; metadatawijziging niet zonder reden alle reviews ongeldig maken.
- Geen automatische overdracht van oude beoordelingen naar nieuwe media-ID's. Gelijke URL is geen sluitend bewijs van gelijke afbeelding.
- Oude snapshot bevat mogelijk nog geen Brauer of latere importbatches. Dekking vers meten vóór “alle producten” melden.
- Bewust uitgestelde Wiesbaden-gevallen, Lagoo-fotoverbod en bestaande fabrikantbronafspraken behouden.
- Geen automatische AI-verrijking, Shopify-correctie of publicatie vanuit een rood vinkje.

## Uitvoering binnen het SEO-plan

Onderdeel van SEO-S06 t/m SEO-S08 en borging in SEO-S19. GSC-nulmeting blijft nu de actieve stap; geen ongeplande wissel naar volledige appbouw.

1. Bestaande private Sites-bron, QC-schema en huidige UI read-only inspecteren; bevestigen welke onderdelen al bestaan. Geen bronreconstructie uit de publieke spiegel als privédata ontbreken.
2. Actuele productinventaris en bestaande review-ID's/dekking vergelijken; voorgestelde veldmapping en producttypevereisten vastleggen.
3. Eerste overzicht maken op circa tien verschillende producten uit de gekozen SEO-cluster, inclusief fout/twijfel/geen-PDF-nodig/variantgeval.
4. Automatische aanwezigheid/links meten, inhoudelijk oordeel expliciet apart; bestaande eigenaarreviews intact.
5. Met Jackson toetsen of tabel en actielijst duidelijk zijn; herladen en andere sessie hervatten testen.
6. Pas na bewezen proef catalogusbreed importeren/controleren, zonder automatische inhoudelijke goedkeuring. Later functies toevoegen alleen als de dagelijkse workflow ze nodig heeft.

## Acceptatie en tests bij implementatie

- Alle importpagina's verwerkt; totals en ontbrekende merken zichtbaar; archief/draft/kanaalstatus niet verward.
- Bewijs dat aan-/afwezig, fout/twijfel, NVT en nog-niet-gecontroleerd onafhankelijk werken.
- Productgroep met één verkeerde variant niet als volledig akkoord presenteren.
- Bestaande reviews, notities en checkpoints vóór/na behouden; opslaan en herladen/ander apparaat met bevestigde opslag.
- Inhoudelijke bronwijziging maakt uitsluitend relevante beoordeling opnieuw te controleren.
- HTTP/timeout bij documentcheck als controle mislukt, niet automatisch “PDF ontbreekt”.
- Geen ongeautoriseerde toegang, cliënt-Admin-token, productie-testnotities, bulk-Shopify-write of publiek gemaakte privéreviews.
- Telefoon/desktop met echte schaal testen; serverfilter/paginering hergebruiken waar nodig. Geen volledige grote catalogus onnodig naar iedere telefoon sturen.
- Tests/data/deployment/restpunten afzonderlijk rapporteren; documentatiespecificatie is geen werkende functie.

## Buiten eerste versie

CRM-klanten, orders, facturen, uitgebreide rechtenrollen, leveranciersportalen, planning, automatische correcties, AI-autopublicatie, rankingvoorspellingen en nieuwe infrastructuur zonder aangetoonde noodzaak.

## Checkpoint 11 november 2026

Bestaande QC-documentatie op quality-control gelezen. Er is al een productchecklist en privéopslag; het nieuwe totaaloverzicht en de aparte SEO-review zijn in deze beurt alleen gespecificeerd. Geen appwijziging, deployment, nieuwe catalogusimport of productbeoordeling uitgevoerd. De implementatie begint bij de bestaande broninspectie binnen SEO-S06.
