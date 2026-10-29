# BadkamerCity — Quality Control

30 oktober 2026 · QC-01 · eigen projecttak: `quality-control`.

## Status en opdracht

**FOUNDATION_DOCUMENTED / NO_PRODUCT_AUDIT_YET / MOBILE_APP_NOT_BUILT.**

De eigenaar vraagt expliciet een eigen Git-tak voor kwaliteitscontrole van online producten. Dit is de toegestane uitzondering op de algemene regel geen nieuwe branch per chat. De tak start vanaf main, commit d5dbc60eeea4029a84b7a88659d14a18084ee69c; het is een zelfstandig QC-project, geen actuele Shopify-deploysnapshot. De bestaande storefront-uitvoering/werkbranch blijft apart. Geen wijziging aan Shopify, sortering, productinhoud of afbeeldingen.

Deze eerste oplevering legt de werkwijze en projectstatus vast. Er is nog geen catalogus ingelezen, geen foto beoordeeld en geen werkende telefoonapp of automatische opslag aangesloten. De kwaliteitscontroles zijn dus niet fictief alvast ingevuld.

## Doel

De eigenaar kan in korte sessies op zijn telefoon foto's controleren en daarna zien welke productdata hij moet aanleveren. Dezelfde administratie ondersteunt later betrouwbare productverrijking en de aanbevolen productvolgorde.

Een foto bestaat is iets anders dan een juiste foto. Geïmporteerde/gescrapete gegevens en een producttitel zijn geen onafhankelijke referentie voor elkaar.

## Telefoonscherm — te bouwen

Per kaart:
- Grote, zoombare foto; teller binnen de batch en eenvoudige voortgang.
- Merk, serie, exact fabrikantartikelnummer/SKU, producttype en relevante uitvoering/kleur.
- Bijbehorende variant en rol van de foto: product, sfeer, detail, maatvoering of montage.
- Indien beschikbaar een onafhankelijke fabrikantreferentie/bron naast de winkelfoto. Ontbreekt die, dan is dat zichtbaar.
- Knoppen **Fout**, **Twijfel** en **Klopt**. Links swipen = Fout; rechts = Klopt. De knoppen blijven altijd beschikbaar.
- Na Fout of Twijfel een korte reden, bijvoorbeeld verkeerd product, verkeerde uitvoering, alleen sfeerbeeld, slechte uitsnede/kwaliteit of onvoldoende bewijs.
- Ongedaan maken, overslaan en later hervatten. Een swipe start niet wanneer iemand een foto zoomt of de pagina scrolt.

Een sfeerfoto kan bij het product horen zonder geschikt te zijn als hoofdfoto. Daarom worden deze twee vragen apart bewaard:
1. Hoort deze foto bij dit artikel/deze uitvoering?
2. Is deze foto geschikt voor de bedoelde plaats, zoals hoofdafbeelding?

## Batches en hervatten — contract

Begin met een proef van circa 25–50 foto's, geen verplichte beoordeling van een heel merk. Eerste prioriteit: Hotbath Cobber en Wiesbaden Caral bij kranen. Selecteer op echte artikel-/seriegegevens; een losse titelmatch is niet voldoende.

Elke beoordeling wordt direct duurzaam opgeslagen met bevestiging. Een openstaande opslag mag niet als voltooid meetellen. Een foutieve verbinding blijft zichtbaar; een lokaal wachtende actie moet later veilig kunnen synchroniseren zonder dubbele uitslag. Op een ander apparaat hervatten moet mogelijk zijn: uitsluitend localStorage is onvoldoende.

Bewaar batch-ID, bronmoment, reviewvolgorde, openstaande items en wijzigingenlog. Gebruik controle op gelijktijdige bewerking en een unieke actie-ID. Terugdraaien voegt een herstelactie toe; het wist het oude oordeel niet stil.

Een afgeronde batch betekent uitsluitend dat alle items een uitkomst hebben. Twijfel/fout kan dan nog open opvolgwerk bevatten. Een product is niet automatisch compleet als één foto is goedgekeurd.

## Wat de eigenaar moet kunnen terugzien

Een eenvoudig overzicht met filters op merk/serie en:
- Nog te beoordelen.
- Foto verkeerd: vervangende foto nodig.
- Foto niet geschikt als hoofdafbeelding.
- Twijfel: referentie of bevestiging nodig.
- Specificaties, documenten of productuitleg ontbreken.
- Visueel gecontroleerd; overige controles nog open.
- Alle toepasselijke controles afgerond, met datum.

Per artikel een concrete aanleverlijst: **wat ontbreekt, waarom, voor welk SKU/variant, welk bewijs nodig is en wat daarna opnieuw gecontroleerd wordt**. Lever liever aantoonbare fabrikantdata dan opgevulde velden.

## Controle van de rest van de productdata

| Onderdeel | Wat we controleren |
| --- | --- |
| Identiteit | Merk, exact fabrikantnummer, variant en producttype kloppen |
| Foto's | Juiste uitvoering en passende beeldrol; scherp en bruikbaar |
| Specificaties | Verplichte keuzegegevens voor dit producttype zijn bewezen |
| Documenten | Juiste handleiding, technische tekening/PDF waar toepasselijk |
| Uitleg | Toepassing, setinhoud, afwerking en benodigde onderdelen duidelijk |
| Verkoopgegevens | Juiste prijs-/eenheid en actuele, onderbouwde beschikbaarheidsinformatie |
| Relaties | Categorie en eventuele compatibele onderdelen gecontroleerd |

Gebruik per controle **nog te beoordelen / akkoord / fout / twijfel / niet van toepassing**, met bron en datum. 'Niet van toepassing' vraagt een reden per producttype. Een haakje hoeft niet hetzelfde documentenpakket te hebben als een inbouwkraan.

Een visuele goedkeuring bewijst geen materiaalsamenstelling, PVD-coating, technische compatibiliteit of gebruiksrecht. Die feiten hebben een aparte broncontrole nodig. Bij onvoldoende informatie geen schijnzekerheid of verzonnen kwaliteitsscore.

## Eén productadministratie, geen dubbel werk

Bestaande productregisters en verrijkingsresultaten blijven uitgangspunt. Gebruik de bestaande product-ID/variant-ID en voeg QC-controles/beeldbeoordelingen daaraan toe of koppel ernaar. De lege projectstatus is geen nieuwe kopie van de catalogus.

Zie [bestaand productplan](../docs/PRODUCT_CONTENT_PLAN.md), [vervolg productkwaliteit](../docs/FUTURE_CONTENT_AND_PRODUCT_PROJECTS.md) en [categorisatiecontract](../docs/CATEGORIZATION_AND_SEO_POLICY.md). Het oude Wiesbaden-pilotregister is niet automatisch een actuele online-publicatielijst; raadpleeg ook het [uitvoeringsresultaat](../docs/product-content/WIESBADEN_EXECUTION_RESULTS_2026-10-21.md).

Voor de eerste import de actuele Online Store-publicatie controleren. Alleen ACTIVE is geen bewijs dat een product online bereikbaar is. Neem ook ontbrekende foto's op als aanlevertaak, niet alleen bestaande media.

## Identiteit, geldigheid en opvolging

Een beeldoordeel koppelt aan shop/product-ID, variant-ID of expliciete productbrede scope, media-ID, bron-URL en inhoudsvingerafdruk. Bewaar de gecontroleerde verwachtingen: SKU, uitvoering/kleur, beeldrol en referentiebron.

Als foto, variantkoppeling of relevante artikelgegevens veranderen, vervalt het eerdere oordeel voor die combinatie en komt die opnieuw in de wachtrij. Dezelfde URL kan nieuwe inhoud krijgen; alleen een URL vergelijken is onvoldoende.

Geef een oordeel nooit automatisch aan alle kleurvarianten of producten met dezelfde foto. Een bronbeeld mag op inhoud worden hergebruikt, maar de match moet per artikel/uitvoering bevestigd blijven.

Een afkeuring markeert een probleem. Het verwijdert, verwisselt of verbergt niet automatisch winkelbeelden/producten. De correctiewachtrij en het toepassen in Shopify zijn afzonderlijke stappen, met controle op tussentijdse wijzigingen en terugleescontrole.

## Voorkeursmerken en rangschikking

De eigenaar wil Hotbath **Cobber** en Wiesbaden **Caral** bij kranen verkoopvoorrang geven. Dat is een commerciële voorkeur, geen automatisch kwaliteitskeurmerk. Ook deze artikelen doorlopen dezelfde controles.

Een latere sorteerproef combineert passendheid, geverifieerde kwaliteit, variatie en expliciete verkoopvoorkeur. Bezoek-/koopdata en een klantkeuze voor prijsvolgorde blijven afzonderlijke signalen. Geen sortering of ranking gebouwd/aangepast in QC-01.

## Opslag en toegang — te bouwen

Git bewaart regels, versies, contracten en veilige openbare productstatus/exporten. De telefooninterface krijgt duurzame, afgeschermde opslag voor dagelijkse beoordelingen; niet bij elke swipe een handmatige Git-commit.

Deze repository is openbaar: geen sleutels, klantgegevens, privé-leveranciersfeeds, inkoopvoorwaarden, privéfoto's of ongecontroleerde gekopieerde mediabestanden committen. Git is geen wachtwoordbeveiliging. De uiteindelijke reviewapp krijgt server-side toegangscontrole; geen Admin-token in browsercode.

Techniekkeuze voor de app/opslag volgt pas na controle van bestaande beschikbare beheer-/opslagvoorzieningen. Geen nieuw abonnement, infrastructuur of tracker aangemaakt.

## Eerste proef en acceptatie

1. Controleer bestaande registers en actuele publicatie; kies 25–50 echte beeld-artikelparen uit Cobber/Caral, inclusief varianten, sfeerbeelden en twijfelgevallen.
2. Bouw de mobiele kaart en duurzame beoordelingen; test op de telefoon van de eigenaar.
3. Controleer swipen/knoppen, zoom, reden, opslaan, undo, hervatten en verbindingverlies.
4. Bewijs dat verkeerde foto's, verwisselde kleuren, dubbele acties, tussentijds gewijzigde media en onbekende gevallen correct worden afgehandeld.
5. Controleer de gegenereerde aanleverlijst per SKU en vergelijk de eerste proef met de eigenaar.
6. Pas daarna opschalen. Geen automatische Shopify-correcties of sortering aan deze proef verbinden.

## Exact één volgende handeling

**Inventariseer de bestaande productregisters en beschikbare beheer-/opslagvoorzieningen voor één echte, read-only Cobber/Caral-proefbatch; bouw daarna de mobiele reviewproef binnen deze projecttak.**

QC-01-controle: documentatie en project-JSON opgeslagen en via GitHub teruggelezen. Niet getest: catalogusmatching, beeldinhoud, telefooninterface, synchronisatie, autorisatie, scoring of productcorrecties. Bestaande storefronttaken worden hiermee niet overgenomen.
