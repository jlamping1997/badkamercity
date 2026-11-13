# Begrippen: zoeken, verborgen anchors en inhoudsopgavecontract

**28 oktober 2026 · DOC-03B.** [Contenthoofddossier](../CONTENT_AND_FORMS.md) beschrijft Pages, redirects en beheer. Deze pagina volgt de lokale zoek- en DOM-transformatiefuncties op methodeniveau. Verse Pages-read: 119 records, drie volledig afgesloten pagina's; alleen veilige structurele metadata wordt gepubliceerd.

## Lokaal zoeken is geen productzoek-API

`main-glossary.liquid` zoekt vanuit `document.currentScript.previousElementSibling` de direct voorgaande `[data-glossary-section]`. Hij bewaart arrays van termnodes, lettergroepen en A–Z-links. Zonder zoekveld stopt de initialisatie. De zoekhandler verandert alleen DOM-staat; hij haalt geen product- of Page-data op.

Normalisatie is Nederlandse lowercase + trim. De haystack is `data-term` plus `data-keywords`. Een match verbergt/toont termnodes, verbergt lege lettergroepen en past `aria-disabled` van de bijbehorende letter aan. De status heeft afzonderlijke tekst voor geen zoekterm, één en meerdere/nul resultaten; het lege blok verschijnt alleen bij nul zichtbare termen. GL-01 bevestigt case/whitespace/keywords en herstel na wissen met synthetische inhoud. De eerdere desktopcontrole bevestigde daarnaast 109→1→0→109 op de echte lijst.

### A–Z heeft een resterende bedieningsgrens

GL-02 bevestigt dat een letter voor een inmiddels verborgen groep wel `aria-disabled=true` krijgt, maar **zijn href houdt en geen klikpreventie heeft**. Dat attribuut alleen maakt een link niet inactief. De replay bewijst de DOM-/eventtoestand; werkelijk keyboardfocus en scrollen naar een verborgen doel zijn in deze ronde niet getest. Dit is een gericht onderhoudssignaal, geen algemene kapotte-zoekclaim.

Een latere correctie kan na keuze van het gewenste contract de bestemming/tabbediening synchroniseren met de zichtbare groep. Behoud wel de native bruikbare A–Z-route wanneer niet wordt gefilterd. Geen tweede zoekengine toevoegen om een anchorstaat op te lossen.

## Uitlegbody naar kaarten

`main-glossary-page.liquid` vereist eveneens een script direct na de eigen sectie. Hij leest `.bc-glossary-page__content`, markeert alleen een eerste directe paragraaf als samenvatting en verzamelt **directe H2-kinderen**. Een geneste H2 blijft gewone bodyinhoud en wordt geen TOC-entry.

Per directe heading:

1. Bestaand ID behouden, anders `begrip-section-<positie>` maken.
2. Een sectionkaart vóór de heading plaatsen en de heading daarin verplaatsen.
3. Volgende siblings tot de volgende directe H2 in dezelfde kaart verplaatsen.
4. Een contentslink met die tekst/ID toevoegen.

Woorden in de heading kiezen een verwante-, aandacht- of voordelenstijl. De TOC wordt pas zichtbaar bij meer dan één entry. TOC-00/01/02 bevestigen nul/één/twee directe H2's en hun zichtbaarheid. Een tweede scriptuitvoering op dezelfde reeds gewrapte inhoud dupliceert geen kaarten: er zijn dan geen directe H2-kinderen meer. Dit is geen volledige editor-lifecyclevrijgave voor willekeurig tussentijds vervangen van delen van de body.

### ID-collision als inputgrens

De generator controleert niet of een nieuw `begrip-section-N` al op een andere node bestaat. TOC-04 construeert bewust zo'n botsing: een bestaand ID op de eerste heading kan gelijk zijn aan het gegenereerde ID van de tweede. De output krijgt dan twee dezelfde doelen. Dat is een **synthetisch bevestigd inputrisico**, niet een aangetoonde huidige live fout.

De verse structuurcontrole op **alle 109 gepubliceerde begripspagina's** vindt **655 directe H2's**, **nul pagina's met geneste H2's** en **nul voorspelde ID-botsingen** onder deze regel. Daarmee voldoet de huidige ontvangen inhoud aan die specifieke structuurvoorwaarde. Dat bewijst geen feitelijke juistheid, spelling, linkkwaliteit of volledige visuele/a11ywerking van de tekst.

## Publicatie en bereikbaarheid zijn aparte lagen

109 gepubliceerde begripspagina's betekent niet dat alle 109 lijstlinks bij het juiste Page-record uitkomen. De eerdere volledige verbindingskaart vond 108 gepubliceerde doelen en één ontbrekende `/pages/hygrometer`. GLOSS-F01 blijft open; deze verse bodystructuurcontrole wijzigt geen redirect. Een valide body en een werkende inhoudsopgave kunnen een verkeerde bestemmingsroute niet repareren.

Onderhoud: Page-body, lijstblock en redirect samen volgen; directe H2's behouden; unieke IDs gebruiken; geen eenzijdige DOM-transformatie of raw body in publieke proof opslaan. [GL-/TOC-cases en 109-page-structuurmeting](../../evidence/2026-10-28-transitions/README.md).
