# Tegelfilters: nominale formaten en meerdere kleuren

8 november 2026. TILE-FILTER-01 / OFFLINE_PREPARATION / OWNER_COLOR_REVIEW_PENDING / NOT_APPLIED.

De eigenaar staat expliciet kleine tegelmaatverschillen als 59,6 naar 60 cm toe voor filtergroepering. Exacte specificaties, oppervlakte, doosinhoud, prijs en calculators blijven onaangetast. Dit vervangt de eerdere terughoudendheid over 59,6 naar 60 voor deze afgeleide filterlaag. Tegels mogen meerdere zichtbare basiskleuren krijgen; kleur op de tegel zelf, geen achtergrond/voeg/reflex.

## Scope en bronbewijs

4.100 Admin-leden van Tegels gelezen. Alle IDs afzonderlijk teruggelezen op ACTIVE en niet-lege onlineStoreUrl: **3.496 gepubliceerde actieve producten**, 3.159 Cottoceramix en 337 Porcelanosa. 604 overige records uitgesloten; geen import of activering. Echte maatparen per product, geen kruisproduct van twee facetlijsten.

Bulk-export gaf voltooiingsmetadata 3.496; connector schermt result-URL af. Geen retrieval/omweg. Gewone toegestane paginering en individuele publicatiecontrole gebruikt. Een publieke ID-paginering liep over een indexgeneratievernieuwing en is niet als consistente scope gebruikt. Publieke generatie inmiddels 20261108T130100_bc1233; geen directe systemd/restartpolicytest.

807 exacte kleurnamen. 561 producten missen kleur in bc_filters.kleur, tiles.color en custom.kleur; sluit aan op 83,95% huidige API-kleurdekking. Uit bestaande brondata/beoordeling aanvullen; niet uit één titelwoord gokken. Volledige bron en uitkomsten blijven privé.

## Formaatvoorbereiding

Code op actieve branch onder scripts/filters/: nominal_formats.py, prepare_catalog.py en drie testfiles. Offline hulpmiddelen, niet de bestaande VPS-code of een deployment.

- Decimal; oriëntatieonafhankelijk samengesteld formaat.
- 596 naar 600 mm is de expliciete eigenaarregel, ook naast een andere exacte zijde zoals 1500 mm.
- Overige kandidaten: maximaal 8 mm én 3% per zijde tegenover een herkenbaar nominaal formaatpaar.
- 7,5×30 en 11,25×45 blijven exact; ongebruikelijke behouden maten worden niet weggegooid.
- Octogono/Hexa/mozaïek/andere naam-hints apart beoordelen. Een hint is geen bewezen geometrie.
- Alleen filterlabels; nooit de nominale maat gebruiken voor m², dozen, aantallen of prijzen.

Volledige run op 3.496 bronrijen, byte-ongewijzigd. **302 gewijzigde kandidaatlabels uit 18 bronparen.** Binnen dezelfde vergelijkbare scope: 3.370 producten, 143 bronparen naar 126 labels. Niet 147 alle bronparen met de beperkte 126 labels vergelijken. Status: 1.768 exact herkend, 1.300 exact behouden, 134 eigenaarregel, 168 overige voorstellen, 120 vorm-/matnaamcontroles en zes ontbrekende maatparen. Alle uitvoerrijen context_verified=false, eligible_for_plan=false en production_eligible=false: voorbereiding is geen activatie. Gerichte context-/bron-/steekproefcontrole vóór inzet; geen nieuwe handmatige goedkeuring van ieder exact behouden formaat.

36 Python-tests PASS: oriëntatie, grenzen, kleine formaten, 293 naar 300, ongeldige waarden, scopes, Octogono/Fango en veilige uitvoerpaden. Defaultuitvoer naast private invoer; bron-/samenvattingspadbotsingen vóór schrijven geweigerd.

## Kleurregels en concrete eigenaarreview

Voorbereid, niet toegepast:
1. Porcelanosa + exacte kleur Caliza naar Beige: 36 huidige producten, eigenaarinstructie. Geen wildcard voor Caliza Gris; secundaire kleuren per serie beoordelen.
2. Cevica/Waves/Copper Green naar Groen: vier huidige producten onder Cottoceramix/Waves. Primaire fabrikantpagina geeft Pantone 2411 C / #2C4523; groene fabrikantcategorie noemt het product.

Bronnen:
- https://www.cevica.es/en/tiles/waves-plain-1125x45-copper-green
- https://www.cevica.es/fr/carreaux/verts?page=8
- https://store.porcelanosa.com/uk/bottega-caliza-59-6x59-6 (maat-/productvoorbeeld; Beige is eigenaarbesluit)

Eén tegel kan Beige, Wit en Grijs dragen. OR binnen kleur en binnen formaat, AND tussen kleur/formaat/categorie; tellingen via unieke productIDs. Exacte fabrikantkleur en koopbare uitvoering behouden.

Privébestand Badkamercity-tegelfilters-kleurbeoordeling-2026-11-08.html: **15 kaarten met 15 onveranderde ingebedde productfoto's**; 12 beelden visueel gelezen in deze ronde. 13 open voorstellen, bestaand Caliza-akkoord en bronbevestigd Groen apart. Kleurcheckboxen, hoofdkleur, correctie/opmerking, bevestiging en JSON-export. Een voorgestelde selectie is geen akkoord; wijzigen trekt akkoord in. Drie serie-identiteiten gecorrigeerd tegen Admin (Etnia, Portofino, Strand). Scope per leverancier/fabrikant+serie+exacte kleur, geen globale Natural/Bone-regels. Acht core-state/exporttests en JS-syntax PASS; echte browserklik/download/mobiel NOT_TESTED. Eigenaar kan ook correcties per kaartnummer doorgeven.

Het private rapport bevat volledige bron-/voorbereidingssnapshot voor herstel. Geen catalogus, foto's of volledige kleurbesluiten in publieke Git.

## Implementatiegrens en volgende handeling

MAIN 196328685834 bevestigd. Live filterfiles wijken af van Git; toekomstig UNPUBLISHED concept eerst op bewezen verse MAIN-pariteit. Geen thema-, product-, index-, serverwrite of publicatie.

API accepteert ruwe maatbereiken (596..600 × 596..600: HTTP200, 89 resultaten), maar weigert f_kleurgroep=Groen in het tegelprofiel (HTTP400). Dat bewijst niet dat het indexveld ontbreekt. Bevoegde VPS-read nodig voor schema, actieve allowlist, API-planner en syncworker. Eén afgeleide nominale formaatwaarde en meerdere basiskleuren in dezelfde index/sync; bestaand f_kleurgroep hergebruiken waar type/dekking kloppen. Geen losse patch die sync overschrijft. Gepaard OR-formaat, backend-unietellingen, bestaande exacte URLs, één keuze/één chip, refresh/back/wissen en fallback testen op staging/UNPUBLISHED. Eigenaar publiceert.

**Exact één volgende handeling:** eigenaar beoordeelt 13 open kleurkaarten; Caliza/Groen niet opnieuw vragen. Daarna begrensde tegelpilot met bovenstaande bron-/runtimechecks. Andere import-/BRAUER-/bestelafspraken en apart restartpolicybewijs behouden. Geen actieve schrijver na dit checkpoint.
