# Hotbath keuzemenu's — brede uitrol, 24 oktober 2026

Status: PREVIEW_READY / DESKTOP_VERIFIED; inhoudelijke review READY. Zie [qa-report.md](qa-report.md) voor de echte browsercontrole. Geen publicatie.

## Resultaat

605 groepen verbinden 7.165 unieke actieve/gepubliceerde Hotbath-productpagina's. De oorspronkelijke 433 groepen en 3.383 artikelen zijn behouden; 53 bestaande groepen zijn aangevuld en 172 groepen zijn nieuw ten opzichte van die oorspronkelijke bron. Dat zijn 3.782 extra koppelingen in totaal, waarvan 3.395 na de eerdere proef.

De menu's gebruiken kleur en waar exact onderbouwd hoogte, uitlooplengte, afmetingen, aantal stangen, diameter/dikte van de hoofddouche, bevestiging en handdouche. Verschillende bedieningen, productvormen, sets en losse componenten blijven apart. Een keuzewaarde verwijst altijd naar een bestaand gepubliceerd product; er worden geen combinaties of voorraden verzonnen.

**697 artikelen met SPOM in SKU, titel of handle zijn uitgesloten.** De artikelen blijven bestaan en hun koopfunctie is niet gewijzigd. Dit omvat G50 met SPOM3 alleen in de titel. De uitsluiting blokkeert V2 en oudere/natieve keuzeweergave in de productsectie.

Er zijn nog 373 geschikte artikelen zonder groep: vijf expliciete HOLD's en 368 overige. Dit is geen bewijs dat alle 373 een menu nodig hebben. Hieronder vallen enkelvoudige inbouwdelen en onzekere families zoals IBS33. Onderliggende catalogusfouten zijn niet stil gecorrigeerd.

## Voorbeeldthema en gecontroleerde scope

- Doel: UNPUBLISHED **195649929482**, BadkamerCity - Hotbath keuzemenus 24 okt.
- Start deze uitrol: 519 bestanden; eind: 532. Alleen `sections/main-product.liquid` gewijzigd; 13 nieuwe helpers/data-assets; 518 bestaande bestanden exact ongewijzigd.
- Alle 14 geschreven bestanden exact teruggelezen via Admin-MD5.
- MAIN **195611492618** blijft MAIN en 512/512 checksum-identiek.
- De eerdere Sunshower-verbeteringen, localeheading en opt-in scrollcorrectie zijn behouden.
- Geen product-, metafield-, prijs-, voorraad-, order-, betaal- of publicatiemutaties.
- Niet veronderstellen dat deze Git-branch automatisch aan het concept is gekoppeld. Alleen scoped patch/bewijs/documentatie in dit dossier; geen root-theme-push.

## Architectuur

De bestaande V2-keuzemenu-engine en centrale433-groepen-JSON blijven ongewijzigd.380 groepen gebruiken die oude bron.225 nieuwe/gewijzigde groepen met 4.252 exacte product-ID-routes krijgen een apart datasetadres. 10 JSON-assets blijven elk onder 300.000 bytes; grootste 299.177 bytes. Grootste Liquidhelper 73.698 bytes. Groepen worden niet over meerdere assets gesplitst.

De oude vier pilotassets/helper blijven inert aanwezig. De nieuwe productsectie gebruikt ze niet meer. De bestaande JS blijft exact gelijk en bewaart scrollpositie alleen bij een expliciet datasetadres, zoals al getest in de proef. Details en bouwcommando staan in [architecture-handoff.md](architecture-handoff.md).

## Bronnen en afbakening

- Productcatalogus 8.237 artikelen, 8236 actief/gepubliceerd. Geen lege/dubbele SKU's; huidige Hotbath-updategegevens bevestigen dat de catalogus sinds de gebruikte snapshot niet is veranderd.
- Verse volledige uitlezing 8237 artikelen: **nul** `custom.group`-waarden. Er gaat dus geen werkende oude collectie-relatie verloren.
- Hotbath Catalogus Editie 18; paginaverwijzingen staan per compiler/review. PDF-pagina is doorgaans gedrukte pagina+2.
- Acht eigen boekprofielen: IBS70,IBS7009,IBS20,IBS20A,IBS1,IBS1A,IBS12,IBS12A.
- Vijf numerieke setfamilies zijn getoetst op complete letterlijke titelkeuzes en vaste identiteit. Het boek bevestigt bediening/componentonderscheid; dit is geen volledige officiële configuratorgoedkeuring.
- Rails-vormen, horizontaal/verticaal, mixsets, geïntegreerde schakelaars en los inbouwmateriaal zijn gescheiden. Boeknotities over apart te bestellen inbouwdelen blijven relevant; menu's veranderen de aanbieding niet.
- GentGT003 heeft laag/medium/hoog ; GT023 laag/hoog.
- SDS32 gebruikt expliciet diameter 20/30 cm en dikte 8/15 mm; geen IBS70-cijferbetekenis overgenomen.
- RAAR/RAAS zijn afzonderlijke haken; SWIROU is de temperatuur/timer-schakelaar voor Rails.

Vijf globale HOLD-SKU's: `SDS32BGP`, `IBS33BGP4`, `IBS20AGN357`, `IBS20BBP`, `IBS20BCP`. Overige niet-vrijgegeven varianten staan in de bronreviews en krijgen geen nieuwe route.

Zeven bestaande records kregen uitsluitend het expliciet geautoriseerde extra veld `options.kleur = RVS 316`: AR105EXT18IX/25IX en ARHF011IX–015IX. De strikte allowlist in `colour_option_additions.json` voorkomt andere wijzigingen aan oude records.

## Bewijs

- Onafhankelijke inhoudelijke review READY; alle433 oude groepen / 3383 records plus zeven gerichte kleurtoevoegingen; alle 395 pilotrecords behouden.
- Finale aanvullende 13 groepen / 273 bronrecords gecontroleerd; alleen 3 expliciete nieuwe SDS32-kleurgroepen vervangen, hun 12 records behouden.
- Config 13, numeriek 10, kleur 11, kleur-supplement 5, Rails/Gent-supplement 14 en architectuur 12 gerichte tests geslaagd.
- Vier officiële Liquidchecks zonder errors; resterende waarschuwingen en scope staan in `architecture-liquid-validation.json`. De gegenereerde statische cases overschrijden de complexiteitsadviesgrens; dit is geen runtimefout.
- Echte desktopbrowser 1348 × 926: Gent, IBS12, ACE, Archie kleur+lengte, Rails lengte+aantal en oud CB003 geven het verwachte artikel. SPOM3/G50 zonder menu en met actieve koopknop. Na selectie is exact AR105EXT25BCP toegevoegd; uitsluitend de eigen testregel verwijderd en lege winkelmand bevestigd.
- [deployment-verification.json](deployment-verification.json) en beide eindmanifests bewijzen de beperkte themascope.
- Catalogus- en legacybron zijn privé als broncheckpoint bewaard; geen klant-/ordergegevens gebruikt en geen catalogusdump in publieke Git.

Bij de geteste Gent-, Archie- en Rails-pagina's werd geen productfoto weergegeven. Productmedia zijn niet gewijzigd. GT003IX mist de foto ook op het huidige MAIN-thema: voor dat artikel is het bestaande catalogusinhoud. Dit blijft een apart controlepunt voor livegang.

De volledige samengestelde invoer is uit oude 433 plus runtime 225 te reconstrueren. `rollout-theme-manifest.json` bewaart de SHA256 van de volledige 605 / 7165 union en bronbestanden; `routing-index.json` het exacte routecontract. De lokaal gebruikte kleurcompiler bevat een oorspronkelijke scratchbronlocatie; pas die aan bij een nieuwe checkout. De themebuilder zelf accepteert expliciete bronpaden.

## Terugzetten

Lees vóór iedere write opnieuw de themarol. Gebruik uitsluitend een UNPUBLISHED-thema. Zet bij terugdraaien **alleen** `source-theme/sections/main-product.liquid` byte-exact terug. Daarmee is de eerdere viergroepenproef weer actief; nieuwe assets/helpers zijn daarna ongebruikt en mogen blijven staan. Geen delete nodig. JS, centrale JSON, producten en metafields zijn niet aangepast.

## Volgende handeling

Bekijk het concept op een echte telefoon en controleer vooral samengestelde douchesetmenu's en Rails. Fysieke mobiel, CWV en checkout/betaling zijn hier niet geclaimd. Publicatie is een afzonderlijke eigenaarshandeling volgens AGENTS.md. Bij nieuw themawerk eerst rollen lezen en wijzigingen van Sunshower en Hotbath samen behouden.

