# BRAUER - uitvoering en voortgang

6 november 2026. Aanpak positief beoordeeld; btw in de prijs bevestigd. Prijs-, type- en proefvoorbereiding uitgewerkt. Er zijn geen BRAUER-producten aangemaakt of gepubliceerd.

**Nieuwe harde grens:** geen enkele Shopify-productimport, ook geen DRAFT-proef, totdat alle aangekondigde afbeeldingen/PDF's en overige bestanden ontvangen en geïnventariseerd zijn. Tot die tijd uitsluitend offline productvoorbereiding. Ontbrekende documenten hoeven niet per se een eigen PDF per SKU te zijn; de officiële documentdekking moet aantoonbaar kloppen.

| ID | Taak | Verantwoordelijk | Status | Gereed wanneer |
| --- | --- | --- | --- | --- |
| 01 | Drie bronnen volledig inventariseren | Uitvoering | GEDAAN | 13.757 bronregels en 13.161 exacte SKU's onafhankelijk gereconcilieerd |
| 02 | Dubbele vermeldingen en bronverschillen registreren | Uitvoering | GEDAAN | 372 gedeelde SKU's, 578 veldverschillen over 371 SKU's zichtbaar |
| 03 | Plan, bronmanifest en controlecode in Git vastleggen | Uitvoering | GEDAAN | Eerste plan/status/code op main en actieve branch exact teruggelezen; huidige uitwerking apart checkpointen |
| 04 | Btw-prijsbasis vastleggen | Uitvoering | GEDAAN ALS VOORBEREIDING | Alle 13.161 adviesprijzen incl 21% berekend; consumentenbasis zonder korting; taxesIncluded=true bevestigd. Geen prijswrites |
| 05 | Scope losse onderdelen en toekomstige artikelen kiezen | Jackson | OPEN | Voorstel: zelfstandige onderdelen meenemen, toekomst voorlopig concept |
| 06 | Private remote bronopslag bepalen | Jackson/uitvoering | OPEN | Volledige brondata niet in publieke themarepo; private Git-route geregeld indien gewenst |
| 07 | Uitgebreid productbestand en documentdekking verkrijgen | Jackson/leverancier | OPEN | Beschikbare export en rechten vastgesteld; alleen ontbrekende informatie verder onderzoeken |
| 08 | SKU-botsingscontrole hele Shopify-catalogus | Uitvoering | PROEF GEDAAN / VOLLEDIG OPEN | Voor 31 proef-SKU en EAN nul matches via winkelbrede zoekingangen; overige 13.130 nog controleren voor volledige import |
| 09 | Bestaande categorieën/filters/velden mappen | Uitvoering | VOORSTEL GEREED | 13.161 typevoorstellen; 227 collecties en 258 definities gelezen; exacte doelen in VELDEN_EN_COLLECTIES.md. Voorwaarden/rendererproef open |
| 10 | Materiaal-, afwerkings- en categorisatieverschillen afhandelen | Uitvoering/leverancier | DEELS UITGEWERKT | Brononderbouwde typecorrecties voorgesteld; 27 materiaal- en twee afwerkingsconflicten niet technisch opgelost |
| 11 | 31 proef-SKU's en families technisch verrijken | Uitvoering | BRONUITWERKING GEREED | Expliciete kenmerken, rollen en proefverwachtingen vastgelegd; ontbrekende maat-/componentdata en media nog aanvullen |
| 12 | Media/PDF-register na WeTransfer aanlevering | Uitvoering | WACHT OP BESTANDEN | Exact SKU/rol/volgorde/revisie; twijfelgevallen niet automatisch gekoppeld |
| 13 | Verzendbeleid voor glas en meubels bevestigen | Jackson/uitvoering | OPEN | Passende verzendwijze/tarieven; geen fictief gewicht of korte levertijdbelofte |
| 14 | Kleine DRAFT-proef in Shopify | Uitvoering | WACHT OP COMPLEET BESTANDENPAKKET | Pas na ontvangst/inventarisatie alle aangekondigde media/PDF's; daarna proefwaarden teruglezen en juiste renderer controleren |
| 15 | Desktop/mobiel/cart en selectorproef | Uitvoering | OPEN | Juiste technische selectie, foto/prijs/SKU/URL en eigen testregels opgeruimd |
| 16 | Hervatbare volledige DRAFT-import | Uitvoering | NA PROEFPASS | Identiteiten en groepsreferenties exact, alle writes gecontroleerd, herhalen zonder duplicaten |
| 17 | Index-/filter-/categorie- en merkmapping voorbereiden | Uitvoering | OPEN | Preview en indexplan kloppen; concepten niet publiek indexeren |
| 18 | Deelgroepen beoordelen voor publicatie | Jackson | OPEN | Concrete proefpagina's, prijslijst en uitzonderingen beoordeeld |
| 19 | Gefaseerd publiceren en nacontroleren | Uitvoering | NA VRIJGAVE | ACTIVE + kanaal + publieke URL + bestelbaarheid; daarna publieke zoekindex/SKU/prijs bewezen |
| 20 | Onderhoudscontract en wijzigingsrapport | Uitvoering | OPEN | Nieuwe bronnen verversen alleen afgesproken velden, handmatige verbeteringen beschermd |

**Exact één volgende handeling:** 31 productinhouden offline uitwerken en controleren, met open technische vragen per artikel. Parallel het volledige aangekondigde media-/documentpakket afwachten; daarna pas inventariseren, koppelen en de eerste conceptimport voorbereiden.

Alle import-/publicatie-/browserchecks zijn nog OPEN; bronanalyse is geen kooptest. De benodigde router-/leveradapter is expliciet vastgelegd in UITWERKING.md. Cottoceramix-openpunten blijven afzonderlijk bestaan. De verse MAIN-rolmeting in deze ronde bevestigt196246372618; dat bewijst geen nieuwe unitcarttest.
