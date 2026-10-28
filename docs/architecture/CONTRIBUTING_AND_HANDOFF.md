# Werken aan BadkamerCity als ontwikkelaar of AI

## De eerste vijftien minuten

1. Lees de [centrale status](../LIVE_STATUS_AND_NEXT_STEPS.md), daarna [AGENTS.md](../../AGENTS.md) en [deze documentatie-ingang](README.md). Gebruik de aangegeven actieve branch.
2. Controleer repository/origin/commit, lokale wijzigingen en actuele Shopify MAIN. Een schone nieuwe cloudcheckout bewijst niets over de Windows-werkmap van de eigenaar.
3. Open het systeemregister en het betreffende component-/releasedossier. Bepaal of rootcode, releasedossier of actuele live snapshot de juiste bron is.
4. Herhaal de concrete taak en de volgende handeling. Een oude “volgende stap” is geen toestemming om een andere taak te hervatten.

## Een wijziging voorbereiden

Traceer de route vanaf template/Shopify-toewijzing tot sectie, snippet, CSS/JS en data. Gebruik de scan als zoekkaart; volg dynamische verwijzingen zelf. Noteer de gebruiksplaatsen, toestanden, mogelijke neveneffecten en noodzakelijke controles. Lees de oude implementatiereden voordat je uitzonderingen verwijdert.

Zoek eerst een bestaande helper/component/generator. Bijvoorbeeld: een nieuwe keuzevariant hoort niet vanzelf een nieuwe switcher, een nieuwe scrolloplossing en gekopieerde CSS te krijgen. Controleer of dezelfde bron en hetzelfde gedrag herbruikbaar zijn.

## Documentatie per wijziging

| Wijziging | Werk mee bij |
| --- | --- |
| Nieuwe route of template-toewijzing | Routekaart en systeem-/Admin-eigenaar |
| Componentgedrag of vormgeving | Contract, staten, uitzonderingen en relevante vergelijking |
| Metafield/data/API | Type/eenheid/bronprioriteit, consument en fout-/migratiepad |
| Generator of dataset | Originele bron, deterministische opdracht, revisiecontrole en gegenereerde outputs |
| Nieuwe library/tool/app | Versie, lockfile/licentie, doel, beheer/eigenaar en uitvalimpact |
| Bugfix of release | Bevinding, kleinste patch, tests, bronmoment, readback en rollback |
| Publicatie of nieuw MAIN | Centrale status en gedateerd manifest; geen oude preview als actuele bestemming |

Documenteer **waarom** en **hoe te onderhouden**; herhaal niet iedere coderegel. Bewaar de rationale dicht bij het contract, codevoorbeeld of tests die die rationale controleerbaar maken.

## Ontwerpvoorbeeld voor een componentdossier

Een vervolguitvoerder kan `docs/architecture/components/<functie>.md` gebruiken met vaste onderdelen: doel; routes; actuele bron; data-contract; render-/eventvolgorde; staten; opmaak/tokens; toegankelijkheid; varianten; afhankelijkheden; tests; beperkingen; onderhoud; terugzetten. Maak zo'n dossier wanneer het onderdeel werkelijk wordt onderzocht, niet als lege pagina die volledigheid suggereert.

## Bewijs en reviews

- Een synthetische fixture bewijst het geteste codegedrag, geen serverconfiguratie of echte betaling.
- Een statische screenshot bewijst uiterlijk op dat moment, geen swipe/focus/annulering.
- Een bestandshash bewijst bytegelijkheid, geen catalogusinhoud of bruikbaarheid.
- Bij codewijzigingen tests kiezen op het gewijzigde contract; niet de hele historische suite blind herhalen.
- Bij alleen documentatie/scannerwerk: links, bronverwijzingen, scanuitvoer, syntax en betekenisvolle scannerchecks controleren. Geen winkelwagen- of checkoutmutaties nodig.

Laat een opvolger als overnametest drie dingen aanwijzen: de renderer van een concrete productkaart, de bron van een levertekst en de kleinste veilige route om een keuzemenu consistent te maken. Kan dat niet zonder gokken, dan ontbreken uitleg of verwijzingen.

## Git en uitrol

Actieve branch blijft `fix/product-cards-2026-10-14`; maak niet per chat een nieuwe branch. Deze ronde gebruikt een eigen schone cloudcheckout om andere lokale werkmappen ongemoeid te laten. Gebruik normale commits/pushes en controleer remote opslag; geen force-push of ongericht opschonen.

`main` blijft de vaste documentatie-ingang. Neem daar alleen documentatiewijzigingen over; een script of themacode uit de actieve branch wordt niet automatisch naar main gekopieerd. Gedeelde documentatie verwijst daarom expliciet naar de tool op de actieve branch. Leg een latere consolidatie van de root-themacode apart voor, na bewijs over deploykoppelingen en alle verschillen.

Themawijzigingen via een gecontroleerde UNPUBLISHED-preview, merchant beoordeelt en publiceert volgens de bestaande regels. Een verzoek om een auditplan is geen toestemming voor live code-, catalogus-, server- of betaalmutaties.

Deze uitvoering heeft geen toegang tot de Windows-pc en claimt geen uitvoering van het lokale PowerShell-bewijsprotocol. Cloud-Gitstatus, commit/readback en Shopify-read-only bronnen zijn de gebruikte bewijsmiddelen.

## Concrete onderhoudsafspraak sinds DOC-02A

De [componentingang](components/README.md) wijst per functie één uitleg-eigenaar aan. Update bij een contractwijziging hetzelfde dossier, de [routematrix](ROUTE_RENDERER_MATRIX.md), relevante bevinding en bronmoment. Nieuwe/verdwenen bronbestanden ook in component-registry.json zetten; bouw source-index en field-consumers opnieuw met de offline tool op de actieve branch. Lees de grenzen en invoer bij [fundament/tooling](components/FOUNDATIONS_AND_TOOLING.md).

Een ongewijzigde hash rechtvaardigt hergebruik van een bronverwijzing, geen nieuwe browser-PASS. Een gewijzigde hash betekent betrokken uitleg en callers beoordelen; niet automatisch de hele winkel opnieuw testen. Gebruik de concrete acceptatiematrix uit het dossier en publiceer alleen nieuwe testresultaten die werkelijk zijn uitgevoerd. Documentatie naar main bevat geen ruwe private productwaarden of privé-datapakketlink.

## Drie concrete overnameproeven

| Vraag | Opvolger moet kunnen aanwijzen | Veilige eerste handeling |
| --- | --- | --- |
| Waarom staat bij Sunshower een pijl en bij een lijst niet? | Routematrix → kaartdossier → CTA versus galerijfunctie; mobiele hide-regel en mogelijke externe override | Dezelfde functie/viewport na JS vergelijken; pas daarna classificeren en één beperkte stijlafspraak voorstellen |
| Waarom ontbreekt een specificatie/PDF? | Werkelijk producttemplate → specs-/documentrouter → veldtype/namespace → scopeguard → rij/linkrenderer | Bronwaarde en guard read-only controleren; geen feiten aanvullen of verborgen URL's massaal vrijgeven |
| Waarom opent toevoegen soms geen popup? | Koopingang → exacte add-handler → notification, inline status of cartnavigatie | De bronroute en gewenst feedbackcontract bepalen; geen tweede submitlistener of echte koopactie als documentatietest |

Deze routes zijn inhoudelijk uit de benoemde bron herleid. De overnameproeven zijn nog niet door een onafhankelijke nieuwe medewerker/AI uitgevoerd. Leg zo'n echte overnametest vast zodra die plaatsvindt; behandel de tabel niet als bewijs dat iedere opvolger al zonder hulp slaagt.
