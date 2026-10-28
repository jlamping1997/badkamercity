# Filterwaarden: eenheden, exacte keuzes, groepering en beleidsflags

**28 oktober 2026 · DOC-03C.** Deze uitleg volgt `renderFilters`, range-/checkboxhandlers, chips en de openbare facetconfiguratie. [41 cases en twee profielreads](../../evidence/2026-10-28-filters/README.md). Geen volledige backend-/indexschema-audit.

## De API-waarde is niet altijd de zichtbare waarde

| Soort | UI | Request |
| --- | --- | --- |
| Prijs | Eurobedrag | Afgeronde gehele centen; standaard divisor 100 |
| Afmeting met divisor | Waarde gedeeld door display_divisor | Ruwe broneenheid |
| Exact numeriek | Eén checkboxachtige optie met geschaald label | `ranges[field]={min:raw,max:raw}` |
| Boolean | Ja/Nee-label | Strings `true`/`false` |
| Gegroepeerde tekstwaarde | Eén groepslabel | Alle expliciete `exact_values`-leden |

De handler voor een gewone checkbox bewaart per veld een Set, voegt exact gekozen rawwaarden toe of verwijdert die, wist een lege key en zet page op 1. Een groepslabel wordt dus niet zomaar als een nieuwe producteigenschap naar de API gestuurd. De backend bepaalt de werkelijke combinatiebetekenis; de frontendarray alleen is geen nieuwe databasevalidatie.

Een numeric facet krijgt een range wanneer het type number_integer/number_decimal is en `ui.control` niet single_select is. Een schaal boven 1 krijgt in deze bron step 0.1, anders step 1; het woord number_decimal garandeert dus niet zelfstandig willekeurig veel decimalen in de UI. Bestaande selected/exactwaarden worden bij iedere response uit de actuele interne staat gerenderd.

## Draft, change en debounce

Een geldige input wijzigt de interne range **direct**, maar stelt request/URL-commit uit met 300ms. Daardoor blijven twee snel na elkaar ingevoerde bounds bestaan; alleen de laatste debouncecallback draait. Een change-event commit direct en annuleert de timer. Leegmaken verwijdert alleen de betreffende bound; wanneer niets overblijft verdwijnt de range-key. Een rangechip verwijdert de hele range.

FX-05/07/33 bevestigen dubbele boundinvoer, centconversie, gedeeltelijk wissen en een draft die een nieuwe filter-DOM overleeft. Focus op een vervangen range-input wordt op basis van veld/kind hersteld. De bewaarde open-/expandedstaat zit per veld in filterMemory; dat is paginageheugen, geen account- of permanente voorkeur.

De bron roept `checkValidity` aan vóór versturen. In de harness is de numerieke validity expliciet nagebootst, omdat happy-dom 21.0.4 een step-0.1-precisieverschil vertoonde. De tests bewijzen de guard-/stateketen onder geldige/ongeldige stimuli, **geen native browservalidatie**. De productiecode is hiervoor niet aangepast.

### Omgekeerde ranges

Min/max worden afzonderlijk op HTML-constraints beoordeeld. Er staat hier geen gezamenlijke min≤max-check. FX-25 bevestigt dat een op zichzelf geldige min 200 euro en max 100 euro als omgekeerde centenrange de API bereiken. De echte backendrespons voor dit scenario is niet onderzocht; geen nulresultaat-/fout- of datacorruptieclaim uit alleen de frontend afleiden.

## Toon meer/minder: FILTER-F02

De eerste render gebruikt `Number(ui.visible_values) || 6`. De latere Toon-minder-handler gebruikt echter een **vaste grens zes**. FX-22 geeft een groep met limiet twee: eerst twee zichtbare opties, na uitklappen acht, na inklappen zes. De oorspronkelijke limiet wordt niet hersteld.

**Status: VERIFIED_ISOLATED, conditionele P2-kandidaat.** De twee nieuw gelezen openbare profielen — Wastafelkranen met tien facetten en Inloopdouches met zeven — geven voor alle ontvangen facetten visible_values=6. Het afwijkende geval is dus niet als huidige fout op die twee routes aangetoond. Andere profielen zijn in deze meting niet gelezen. Een gerichte latere correctie moet dezelfde limiet bij renderen en inklappen gebruiken, met geselecteerde waarden zichtbaar en behoud van expandedstate.

## Beleidsmetadata die niet één-op-één wordt uitgevoerd

`ui.section=more` wordt voor f_serie, vendor en price_cents door de frontend bewust overruled: die velden komen primair. FX-32 bevestigt die uitzondering met f_serie. Beide openbare profielen plaatsen f_serie in more, terwijl deze client hem naar de hoofdgroep haalt. Dat is een code-/configuratieverschil, niet op zichzelf een defect.

`ui.searchable=true` maakt in deze frontend **geen zoekveld binnen de opties**. De property en een CSS-class voor zo'n veld zijn geen bewijs dat die functie is gebouwd. In de ontvangen metadata staan onder meer kleur/serie als searchable; andere true-flags horen bij numerieke controls. Eerst per control bepalen wat zo'n flag behoort te betekenen voordat een nieuwe zoekbediening wordt toegevoegd.

Kleuraliassen uit filter_policy kunnen geselecteerde rawwaarden normaliseren; canonicalColor normaliseert daarnaast bepaalde RVS-benamingen voor presentatie. Dit zijn verschillende lagen. Een nette kleurnaam of swatch is geen bewijs dat alle bronwaarden naar hetzelfde productdoel mogen worden samengevoegd.

## Onderhoud

Een filterwijziging vraagt controle van veldtype, raw eenheid, displaydivisor, controltype, exact/groupwaarden, huidige selectie, chip, URL en request. Voeg geen extra btw of titelafleiding toe. Bewaar eenheid-/boolean-/exactcontracten bij gedeelde styling. Open: werkelijke mobiele/keyboardsituaties, alle profielvarianten, CORS-preflight, backendvalidatie en product-ID/prijs/voorraadvergelijking.
