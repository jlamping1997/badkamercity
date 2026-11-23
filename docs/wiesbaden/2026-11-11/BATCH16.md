# BATCH16 – laatste 312 Wiesbaden-producten

11 november 2026. De laatste 312 producten zijn allemaal inhoudelijk bekeken. 247 zijn afgerond; 65 blijven bewust open met een concrete bron-, functie-, geometrie- of catalogusvraag. Bestaande correcte keuzemenu’s en afzonderlijke productmodellen tellen afzonderlijk mee.

| Uitkomst binnen deze 312 | Producten |
| --- | ---: |
| Nieuw of aangevuld keuzemenu nodig | 197 |
| Bestaand keuzemenu correct; behouden | 30 |
| Geen keuzemenu nodig voor dit vaste productmodel | 20 |
| Bekeken maar nog niet afgerond | 65 |
| Totaal bekeken | 312 |

De wijzigingsset bevat 300 producten in 64 groepen: 49 nieuwe groepen en 15 uitbreidingen. Daarvan komen 103 bestaande producten alleen mee om sluitende groepen en bestaande verwijzingen te behouden. 12 daarvan krijgen nu voor het eerst een uitgebreide groep; hun eerdere beoordeling wordt niet opnieuw meegeteld. Cumulatief: **2386/2451 afgerond, 65 open**; alle 2451 zijn bekeken. 1845 producten hebben uitgebreide menu’s, verdeeld over 268 groepen.

De keuzes volgen de fabrikant: kleur/afwerking, maat, lengte, uitvoering, kraangaten, uitsparingen, toiletzitting of expliciet benoemde koude-startuitvoering. Complete kranen en sets blijven hun exacte productrol houden. Junior-zittingen noemen de zittingkleur afzonderlijk; ontbrekende combinaties blijven onbeschikbaar. Raw-hoekfonteinen benoemen de komvorm. Verschillende aansluitingen, montagevormen, doosinhoud en bronvlaggen blijven bij het werkelijke product horen; een keuzemenu beweert geen gelijke passing of uitwisselbaarheid.

## Controle

- SOURCE: exacte fabrikantidentiteit en unieke keuzetupels; expliciete afzonderlijke primaire-identiteitsbewijzen waar de oude leverancierslijst geen match had. Opgehaalde indexpagina’s of404/429-beperkingen worden niet voorgesteld als een actuele volledige200-productpagina.
- Lokaal PASS: bestaande renderer op300 startstanden,1282 geldige aswissels en191 geblokkeerde combinaties; dubbele tupels/navigaties afgewezen.1012 exacte kandidaatafbeeldingen. Strikte lokale Liquidparser op baseline en beide gewijzigde bestanden PASS; geen externe validator of Shopify ThemeCheck. Onafhankelijke64-groepen/300-productreview en alle410 bronlabels/23 bewuste oude herlabels PASS.
- Admin-readback PASS op415 producten (312 huidige+103 bestaande ondersteuning):336 velden exact,304 create-only (209 groepen+95 kleurverwijzingen) en32 append-only CAS.65 holds,30 bestaande goede menu’s,20 modellen zonder menu en alle overige gelezen velden behouden.66 conceptbestanden exact, waarvan64 begrensde JSON-assets; JS ongewijzigd.
- Publiek PASS:125/125 previewpagina’s over alle64 groepen en64/64 volledige JSON-assets exact. Alle nieuwe leden van de15 uitgebreide groepen zijn in deze steekproef opgenomen. Voor de finale30 behouden kleurmenu’s:8/8 ondersteunende HTTP-metingen over6 cohorten, inclusief2 MAIN-metingen. Geen nieuwe20-product-HTTP-ronde voor de modellen zonder menu. Twee onjuiste afwezigheidsasserties in de testharness zijn gecorrigeerd: bewaarde oude kleurfacts zijn toegestaan en exact gevalideerd wanneer de renderer ze zonder choice_display bewust negeert; originele uitkomsten en twee gerichte hercontroles behouden.
- Desktopbrowser PASS: Ribbd29.5301 Standaard(coldstart),Chroom,€145 →29.5310 XL(zonder coldstart),Chroom,€219. Exacte titel/SKU, geselecteerde uitvoering en winkelwagenknop correct; ontbrekende kleurcombinaties uitgeschakeld. MAIN29.5310 behoudt eigen titel/SKU/€219 en winkelwagenknop zonder foutieve menuselectie. Geen echte winkelwagenmutatie, checkout of native mobiele test.
- MAIN-bestanden niet geschreven: drie codechecksums en de bestaande zevenledige Ribbd-asset exact behouden; MAIN blijft196416504074, concept196441932042 blijft UNPUBLISHED. Vier publieke formulier-/identiteitscontroles en zeven exacte legacy-kleurgates PASS. Nieuwe Ribbd-SKU ontbreekt bewust in de oude MAIN-asset; bestaande renderer verbergt het menu veilig zonder de eigen winkelwagenvariant aan te passen. Alle15 oude groepsassets zijn lokaal op dezelfde ontbrekende-lidveiligheid getest.

De nieuwe uitgebreide menu’s staan in het ongepubliceerde concept196441932042. Productmetafields zijn winkelbreed; aangevulde bestaande kleurverwijzingen op MAIN zijn daarom apart gecontroleerd. MAIN196416504074-bestanden zijn niet geschreven; er is geen thema gepubliceerd of vervangen. Commerciële productvelden, prijzen, voorraad, foto’s, beschrijvingen en publicatie blijven behouden. Bestaande kleurverwijzingen blijven gelijk of worden alleen met compare-and-set aangevuld.

## Nog open

[Exact312 productuitkomsten](BATCH16_REVIEW_LEDGER.json), [broncontroles](BATCH16_SOURCE_CHECKS.json) en [de concrete open vragen per SKU](BATCH16_OPEN_ITEMS.json) zijn afzonderlijk vastgelegd. De open producten krijgen geen verzonnen generatie-, montage- of componentkeuze.

| Blokkerende vraag | Producten |
| --- | ---: |
| HOLD_BUNDLE_COMPONENT_MAPPING | 3 |
| HELD_PRIMARY_IDENTITY_NOT_CORROBORATED | 8 |
| HOLD_SOURCE_GEOMETRY | 1 |
| HOLD_COMPATIBILITY | 6 |
| HOLD_GENERATION_IDENTITY | 2 |
| HOLD_MENU_MODEL_EXTENSION | 1 |
| HELD_SOURCE_DIMENSION_CONFLICT | 3 |
| HELD_CORE_FUNCTION_MAPPING | 3 |
| HELD_ALIAS_ROUTING_POLICY | 34 |
| HOLD_POTENTIAL_DUPLICATE | 2 |
| HOLD_DUPLICATE_COMMERCIAL_IDENTITY | 2 |

Een aparte bron-DATA-vraag op een bewezen productmodel betekent niet automatisch dat het menu onjuist is. Die vragen blijven zichtbaar in de broncontrole; onopgeloste menu-identiteit of dubbele keuzetupels tellen wel als open.

## Terugdraaien

BATCH16_ADMIN_CHANGES.json bevat alle336 exact teruggelezen before/after-wijzigingen:304 nieuw en32 bestaande kleurvelden aangevuld. Verwijder uitsluitend door deze batch gecreëerde switch_group/kleurverwijzingen wanneer de huidige waarde en digest nog overeenkomen met de vastgelegde nieuwe toestand. Zet alleen de toegevoegde referenties terug met een nieuwe digestcontrole; behoud andere wijzigingen. Herstel de twee concept-Liquidbestanden uit codeparent d088f3a7257f8953e3cca81ce3519eb9a6592c35; dit herstelt15 oude routes en verwijdert49 nieuwe routes. De15 oude begrensde JSON-assets zijn behouden. Nieuwe ongebruikte groepsassets kunnen daarna worden opgeruimd. Dit betreft geen productverwijdering, redirect, publicatie of wijziging van commerciële velden.

Gitcheckpoint: codebranch fix/product-cards-2026-10-14 bevat de66 exacte themabestanden en dit dossier; main krijgt alleen documentatie. Centrale overdrachten krijgen dezelfde teller. Geen actieve Shopify-schrijver na overdracht. Volgende stap: de65 specifieke open vragen oplossen en mobiele/cart-QA vóór eigenaarpublicatie. Alle2451 zijn inhoudelijk bekeken; geen nieuwe blinde batchselectie uit de opgeloste ledgers.

Leto-sets gebruiken Uitvoering set met Wit (Amador chroom), Quartz en Carrara. Alleen de witte set is expliciet Amador/chroom onderbouwd; geen afgeleide messing-/PVD-afwerking of gelijke componentinhoud voor de andere sets. Losse componentcodes blijven een DATA-vraag. Bron-DATA-vragen wijzigen geen bestaande specificaties.
