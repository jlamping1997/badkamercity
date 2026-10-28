# Eén herkenbare bediening per functie

**28 oktober 2026 · raamwerk en voorgestelde afspraken.** De eigenaar vraagt eenheid, bestaande stijlen behouden en soepele bediening. Onderstaande concrete uitwerking is een audit-/besliskader; niet alle getallen, iconen en componentvarianten zijn al als ontwerp goedgekeurd.

## 1. Eenheid zonder verschillende functies gelijk te maken

Hetzelfde type keuze hoort dezelfde opbouw, gekozen toestand, focus, foutmelding en beweging te hebben. Een keuzemenu is bijvoorbeeld geen gewone navigatielink. Een pijl voor volgende foto is iets anders dan een pijl naar een productpagina of een chevron die een paneel uitklapt.

Per variant eerst bepalen: functieverschil, benodigde merkuitzondering of toevallige implementatie-afwijking. Alleen de laatste categorie vraagt automatisch harmonisatieonderzoek. Voor Sunshower zijn fotopijlen in de huidige sectie aangetoond; de door de eigenaar bedoelde productpijlen zijn nog niet route- en staat-specifiek gereproduceerd.

## 2. Contract per component

Elk uitgewerkt componentdossier moet bevatten:

| Veld | Inhoud |
| --- | --- |
| Identiteit | Vaste componentnaam en eigenaarrol |
| Doel | Wat de klant probeert te doen; waar het component gebruikt wordt |
| Bron | Theme-ID/commit, template, sectie, snippets, assets en instellingen |
| Input/output | Getypeerde data, SKU/variant/keuzegroep, callbacks/events en API-resultaat |
| Staten | Leeg, standaard, geselecteerd, uitgeschakeld, laden, succes, fout en terugval |
| Vormgeving | Typografie, kleur/tokens, spacing, radius, icoon, breakpoint, laag |
| Gedrag | Klik/touch/toetsenbord, openblijven, terugknop, annuleren, focus en scroll |
| Datagrens | Welke data officieel is en wat bij ontbrekende/tegenstrijdige waarden gebeurt |
| Uitzondering | Bewuste variant met reden, betrokken routes en vervaldatum/herzienmoment |
| Controle | Reproduceerbare scenario's, actuele testgrens en herstelroute |

## 3. Componentmatrix voor de eerste audit

| Familie | Te vergelijken implementaties | Te bewaken eenheid | Niet blind samenvoegen |
| --- | --- | --- | --- |
| Keuzeveld | Hotbath lengte/uitvoering, Sunshower configuratie, andere productkeuzes | Label, waarde, chevron, open/gekozen/fout/disabled | Echte Shopify-variant versus navigatie naar een ander product |
| Kleuren | Hotbath-stalen, Wiesbaden-stalen, kaartkleuren | Afmetingen/naam, geselecteerd, +aantal, uitgeklapte staat | Verschillende bronrelaties, echte finishafbeelding en kleurbenaming |
| Optioneel onderdeel | Hotbath inbouwdeel, eventuele andere expliciete toevoeging | Compact label, expliciete opt-in, meerprijs, totaal | Verplichte onderdelen, setrelaties en incompatibele varianten |
| Hoeveelheid | PDP, cart, quickshop | Nummerinput, grenzen, fout/disabled, toetsenbord | Voorraad-/verpakkings-/tegeleenheid en staffelregels |
| Productkaart | Native kaart, zoekkaart, externe lijst, mobiel, Sunshower shopkaart | Titel, foto, prijs/btw, leverinformatie, hartje en actie | Configuratie vereist versus direct koopbaar; carouselkaart versus grid |
| Galerij | Dawn/algemene PDP, Sunshower, mobiele viewer | Herkenbare vorige/volgende/zoom/sluiten, selectie en focus | Fotoverhouding, één/multi-media, specifieke viewer-integratie |
| Knop/link | Kopen, product bekijken, verder winkelen, details | Betekenis van primair/secundair/tekstlink, hover/focus/loading | Navigatielink als button vermommen of elke CTA even prominent maken |
| Disclosure | Kleurenuitklapper, specificaties, filters, productinformatie | Chevronrichting, aria-expanded, label en toetsenbord | Schakelende radio/checkbox en echte navigatie |
| Modal/drawer | Cartbevestiging, afbeeldingviewer, menu, quick-add | Sluiten, Escape, achtergrond, focus, scrolllock, grote inhoud | Bestaande native dialog en Dawn-component zonder regressie vervangen |
| Lever-/foutmelding | Productkaart, PDP, cart en API-fallback | Zelfde betekenis, bron en formulering | Leveranciersvoorraad gelijkstellen aan eigen voorraad of vaste levertijd |

Deze matrix is geen verklaring dat iedere genoemde variant actief is. DOC-02 koppelt de werkelijke gebruiksplaatsen eraan.

## 4. Tokenregister en CSS-afspraken

Eerst inventariseren welke tokens/stijlen al bestaan. Daarna één gekozen bron voor kleur, tekstschaal, spacing, radius, controlhoogte, focus, schaduw, lagen en beweging. Huidige `--ss-*`, `--bc-*` en Dawn-variabelen op betekenis mappen; gelijkende waarden niet automatisch vervangen.

Gedeelde functieopmaak hoort in een gedeeld component met beperkte scope. Merk-/paginaverschillen mogen een gedocumenteerde modifier of tokenoverride gebruiken. Vermijd nieuwe kopieën van een heel component voor alleen een rand, chevron of spacingverschil. Behoud werkende eventhooks en datacontracten; CSS-classnaam en functionele JS-hook hebben verschillende verantwoordelijkheden.

Een overeenkomstige hexkleur of identiek codeblok is een onderzoekssignaal. De werkelijk geladen cascade en de actieve staat bepalen of er een probleem is. Geen globale `button`- of `svg`-override als oplossing voor één merkverschil.

## 5. Iconen en pijlen

| Betekenis | Te kiezen gezamenlijke regel | Acceptatie |
| --- | --- | --- |
| Naar een bestemming | Eén stijl voor een gelijkwaardige tekst-CTA; eventuele pijl consequent binnen dezelfde kaartfamilie | Linkdoel blijft duidelijk; hele kaart en losse CTA concurreren niet |
| Paneel openen/sluiten | Herkenbare chevron gekoppeld aan open toestand | Label, aria-expanded en zichtbare richting vertellen hetzelfde |
| Vorige/volgende afbeelding | Passende vorige/volgende bediening bij meerdere media | Randstaten, teller/thumbnail, toetsenbord, swipe en afbeeldingindex kloppen |
| Sluiten | Duidelijk kruis met toegankelijke naam en bruikbaar aanraakvlak | Werkt in alle modalstaten; focus keert correct terug |

Het zichtbare pictogram mag kleiner zijn dan zijn aanraakvlak. Afmetingen eerst vergelijken met de bestaande goedgekeurde bediening en toegankelijkheidscontrole; geen universele nieuwe pixelmaat door de hele winkel drukken.

## 6. Soepele bediening als contract

- Animatie heeft één duidelijke begin-/eindstaat; herhaald klikken leidt naar de laatste bedoelde toestand.
- Toon bevestiging pas na een geslaagde koopactie; fouten mogen geen oude succesinhoud tonen.
- Geen herhaald scrollen tegen gebruikersinvoer in. Bestaande gedeelde positiecode onderzoeken en hergebruiken.
- Animaties stoppen/versimpelen bij reduced motion. Focus en sluiting moeten ook zonder transitionend werken.
- Laad- en sluitgedrag mogen geen dubbele add-to-cart, extra onbedoelde navigatie of verborgen bediening veroorzaken.
- Leg feitelijke duur/easing vast per component, met de reden voor afwijkingen. Een fotogalerij en korte bevestiging hoeven niet dezelfde duur te hebben.

## 7. Hoe we harmonisatie uitvoeren

Eerst één goed gereproduceerd verschil en een begrensde vergelijkingsset. Gebruik de bestaande goedgekeurde variant als uitgangspunt, registreer de gewenste afspraak en pas één familie in een concept aan. Controleer alle werkelijke gebruiksplaatsen van die familie. Daarna pas breder hergebruiken.

Een nieuw abstraheringslaagje is niet automatisch beter. Kies een gedeeld snippet/CSS-helper als dat voldoende is; een volledige componentbibliotheek of frameworkmigratie moet een afzonderlijk aantoonbaar voordeel hebben.
