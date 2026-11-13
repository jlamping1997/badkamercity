> Historisch checkpoint. De actuele selectie en formulering staan in [HANDOFF_BRAUER29.md](HANDOFF_BRAUER29.md); onderstaande cijfers beschrijven ronde 28.

# BRAUER-28 — fabrikantonderzoek en offline importvoorbereiding · 8 november 2026

**12.132 onderbouwde pluspunten bij 7.220 artikelen** voorbereid. Deze ronde voegt 3.920 teksten toe, herformuleert 1.081 eerdere teksten en behoudt alle 8.212 bestaande pluspuntregels. Maximaal vier per artikel. **Alle imports, ook DRAFT, blijven geblokkeerd.** Er is niets naar Shopify geschreven.

Lees [het fabrikantonderzoek](FABRIKANT_BRAUER28.md) en privé `prepared/HANDOFF_BRAUER28.json`. De bestaande ZIP en XLSX worden met behoud van identiteit vervangen; de centrale status noemt de bevestigde opgeslagen versies. Geen actieve bronlezer of schrijver na overdracht.

## Gegevens en bronbewijs

17 officiële BRAUER-bronnen gelezen, plus de openbare Topa-catalogusindex; de catalogusdownloads vragen login en zijn niet geopend. Acht afgebakende fabrikantdefinities verduidelijken reeds bewezen artikelkenmerken. Algemene fabrikantteksten leveren geen ontbrekende merk/SKU/EAN-identiteit, maat of meegeleverd onderdeel. Nieuwe individuele externe productfeiten: nul. Geen herhaling van de duizenden afgeronde retailerpagina’s.

Glascoating heet nu ‘Met water- en vuilafstotende glascoating’. De Void-handleiding beschrijft aanbrengen na montage; geen algemene claim dat alle glas al in de fabriek is behandeld. Geen kalkvrij-/onderhoudsvrijbelofte. ‘Profielloze uitvoering’ geldt uitsluitend bij een letterlijk overeenkomstige oorspronkelijke leveranciersrij; ‘dunne profielen’ blijft onbewezen. PVD, bekende 8 mm glasdikte, antislip, verlichting, opbergruimte en deurmechanismen gebruiken alleen positieve, conflictvrije feiten van hetzelfde artikel.

Bij **24 artikelen** is de te algemene leveranciersparse ‘Draaideur’ verfijnd tot het expliciete ‘Draai-schuifdeur’. De eigen oorspronkelijke leveranciersrij noemt dit mechanisme. Oude waarde en bewijs zijn bewaard in `supplier-door-refinements.json`; geen kleur-/maatovererving. Er zijn geen technische velden toegevoegd of verwijderd. De canonieke parser geeft deze samengestelde leveranciersgroep nu voorrang.

Technische stand: **13.161 artikelen, 178.198 velden, 6.622 artikelen met ontbrekende gekozen kerngegevens**. 150 open retailveldverschillen, 288 verdachte slangwaarden, 480 vragen bij 461 artikelen. Oorspronkelijke 42 gegevensblokkades en 163 toekomstige artikelen behouden. Alle overige cataloguseigenschappen, prijzen inclusief 21% btw, SKU/EAN, titels, goedgekeurde keuzes en eigen invoer gelijk aan het invoerpakket.

## Voorbereiding en controles

`import-preparation.jsonl` bevat alle 13.161 artikelen met brongebonden gegevens, opties, eigen aanvullingen en expliciete blokkades. De bestaande definities `custom.pluspunten` (tekstlijst), `custom.complete_specificaties` (JSON) en `custom.switch_group` (tekst) zijn alleen gelezen en qua type/validaties gecontroleerd. **39.483 bijbehorende veldwaarden exact vergeleken**; geen definities of winkelwaarden aangemaakt. Geen uitvoerbare API-importer, voorraadgetallen, productstatus of publicatieopdrachten. Renderer, winkelbrede SKU/EAN/handle-vergelijking, overige veld-/collectieregels en de productproef blijven open.

**37 tests PASS**, native XLSXcontrole en herhaalcontrole PASS. De vijf oorspronkelijke tabbladen en 421.953 cellen, inclusief native stijlen/tabellen/instellingen, behouden. Het blad Pluspunten bevat exact alle 13.161 artikelregels/EAN’s en 12.132 teksten; EAN’s als tekst, nul foutcellen, acht previews bekeken. Oude retailcontrole bevestigt 42.869 cumulatieve technische aanvullingen en 480 vragen. Geen fysieke Excel-app- of Windows-Git-test. Preflight terecht **exit 2**.

Codecheckpoint `902a729525131352d1de06050c4781adb73c0ba3`, branch `fix/product-cards-2026-10-14`; main alleen documentatie. MAIN alleen qua rol gelezen: `196368531722` (BadkamerCity - Klantenservice 8 nov). Geen thema-, media-, product- of publicatiewrites.

**Eén volgende handeling:** bij ontvangst van de volledige officiële media de offline inventarisatie op exacte artikelnummers uitvoeren en onduidelijke koppelingen beoordelen. Volledige officiële media zijn nog niet ontvangen; gevonden handleidingen gelden uitsluitend als onderzoek. Imports blijven dicht tot inventarisatie, gegevensbeoordeling en een beoordeelde representatieve product-/keuzeproef zijn afgerond. Geen volledige technische vrijgave.
