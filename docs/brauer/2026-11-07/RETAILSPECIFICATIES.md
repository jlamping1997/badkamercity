# BRAUER-21 — specificaties aanvullen uit openbare productpagina’s

7 november 2026. Eigenaar geeft expliciet toestemming voor gegevensonderzoek/scraping bij BadkamerXXL en Sanitairwinkel. Uitsluitend offline voorbereiding; geen Shopify-writes, media-upload, DRAFT-import, themawrite of publicatie. Badkamervoorjou uitgesloten als onderzoeks- en databron.

## Resultaat van deze batch

- Alle 170 openbare Brauer-overzichtspagina’s bij BadkamerXXL gelezen; tien time-outs éénmaal met kleinere batches herhaald en daarna geslaagd. 10.148 unieke URL-kandidaten. Dit is een URL-inventaris, geen bewijs dat alle pagina’s actueel of alle 13.161 eigen artikelen aanwezig zijn.
- 5.827 URL’s hebben een letterlijke fabrikantcodesuffix die in de eigen catalogus voorkomt. Deze match is alleen een zoekkandidaat. Voor aanvullen volgt altijd controle op de inhoud van de productpagina.
- 351 diverse kandidaatartikelen uit 39 producttypen opgehaald. Daarnaast 54 eerdere vergelijkingspagina’s van beide winkels opnieuw opgehaald met verse retrieval aangevraagd. Samen 405 verschillende openbare productpagina’s, 392 verschillende bron-SKU’s, allemaal met Brauer als merk. Bij 402 pagina’s matchen fabrikant-SKU én EAN exact. Drie pagina’s missen een EAN; alleen als tweede vergelijking gebruikt, nooit zelfstandig voor nieuwe klantwaarden.
- **1.721 nieuwe specificatievelden bij 379 artikelen** toegevoegd. Zeven eerder overgenomen externe waarden bij nieuwe tegenspraak ingehouden. Netto1.714extra klantvelden: van135.366naar137.080. Er zijn nu10.357artikelen met één of meer ontbrekende gekozen kernvelden, tegenover10.552vóór deze batch. Dit is geen percentage technische volledigheid.
- **17 open veldverschillen bij dertien artikelen** en **veertien afwijkende doucheslanglengtes** apart. De veertien bronnen noemen15cm; geen automatische omzetting naar150cm. Onzekere waarden worden niet nieuw ingevuld. Directe leverancierswaarden behouden voorrang, met aparte reviewnotitie waar een retailer afwijkt.
- Volledige catalogus is nog niet van beide winkels gescrapet. 5.468 verdere codesuffix-kandidaten staan klaar als werklijst, zonder achtergrondtaak of planning.

## Bewijs en keuzes

Elke toevoeging bewaart merk, exacte fabrikant-SKU, EAN, bronveld, bronwaarde, bron-URL, leesdatum, veldcontext en eventuele tweede bevestiging of tekeningsbeslissing. Een titel, URL-suffix of dezelfde kleur is geen identiteitsbewijs. Geen overerving naar andere kleuren, hendels, maten of serieleden. Leveranciersartikelnummers vervangen de interne winkelnummers niet andersom.

Fysieke maten en nominale modelklassen blijven gescheiden. Een Joy maatcode100 heeft volgens de gecontroleerde artikeltabel99cm breedte en45,5cm diepte. De ondiepe80uitvoering noemt38,6cm diepte. Voor SK-IM60LCH toonde een oudere zoek-snapshot59/60cm als verschil; na verse herlezing noemen beide huidige tabellen59cm, zodat die breedte nu met twee bronnen is ingevuld. Een zoekfragment dient voor ontdekking; verse artikelinhoud heeft voorrang op een oudere index-snapshot van dezelfde URL.

Voor GS-GTC1H12090200CE noemt Sanitairwinkel6mm en BadkamerXXL8mm glas. De aan exact die artikelpagina gekoppelde tekening `GS-GTC1H12090200CE_T`, pagina1, toont de glasdoorsneden met8 en het breedtebereik1181–1196. Visueel gecontroleerd:8mm en118,1–119,6cm uit de artikeltabel zijn ondersteund. Tekening-URL en gekoppelde artikelidentiteit staan privé bij de beslissing. Deze derdenbijlage is onderzoeksbewijs en telt niet als ontvangst van het aangekondigde officiële complete mediapakket.

Ontbrekende ja/nee-iconen worden niet als Nee gelezen. Nul kraangaten blijft nul. Bronvelden over een handdouche krijgen een eigen maatlabel, bijvoorbeeld Diameter handdouche; een maat van een rozet, thermostaat of handdouche wordt geen totale setmaat. Bij afwijkende slanglengtes wordt niet gegokt naar een typefout. Materiaalvormen ABS/ABS-kunststof en overlappende componenten worden niet als verschillende materialen geforceerd; echte RVS/messing-tegenspraak blijft open.

Prijzen, BTW, producttitels, opties, keuzegroepen, eigen aanvullingen, originele bronnen en media-assignment zijn ongewijzigd. Geen commerciële teksten, prijzen, voorraad, levertijden, shopgaranties of beoordelingen gekopieerd. Alleen feiten uit technische productinformatie verwerkt. Klantreviews en overige pagina-inhoud zijn geen gegevensbron voor het productbestand.

## Techniek en reproduceerbaarheid

`retail_extract.py` leest gesanitiseerde technische tabelextracten en maakt `retail-observations.json`. Dat voorbereide feitenbestand is de herbruikbare bron voor `enrich_retail_specifications.py`. De laatste stap vult alleen ontbrekende bewezen velden aan en houdt externe tegenspraak apart. `retail-resolutions.json` bevat uitsluitend beperkte, op de gekoppelde tekening gecontroleerde keuzes. Geen leverancierdata- of mediavlag vrijgegeven.

`retail-product-url-inventory.json`, `retail-next-batch-queue.json`, `retail-observations.json`, `retail-enrichment-report.json` en volledige veldherkomst blijven in het privévoorbereidingspakket. Publieke Git bevat code, tests en deze geaggregeerde overdracht; geen complete catalogus, prijslijst of eigen productteksten.

De vrijgavecontrole heeft nu ook `retail_specifications_reviewed` en controleert echte onopgeloste velden per artikel. Alleen die vlag optruezetten heft de artikelblokkades niet op. De catalogushash is vernieuwd; import blijftfalse, verwachte exitcode2. Geen API-importer toegevoegd.

Directe HTTP-verzoeken vanuit deze werkruimte gaven403; de oorzaak is niet vastgesteld. Openbare webretrieval en de openbare leesroute werkten. Geen blokkade omzeild, geen stealth, proxyrotatie, login of accountcontext gebruikt. Geen browseragent, datasettaak of achtergrondtaak gestart.

## Controle en vervolg

Tien retailtests, zes specificatietests en negen voorbereidingstests controleren exacte identiteit, bronherkomst van elke toevoeging, eenheden, veldcontext, onbekend versusNee, verdachte slanglengtes, terughouden van bronverschillen, het tekeningsbesluit, geen overerving en gesloten importvrijgave. Een aanvankelijke controle van een tussentijds Excelbestand signaleerde verouderde gegevens; dat bestand is niet geleverd. Definitieve Excel-export pas na afgeronde gegevensverwerking controleren.

Het bestaande specificatiebestand heeft nu de extra bladen Aanvullingen en Bronverschillen. Definitieve nativeXLSX-waarden van alle13.161artikelregels exact tegen de definitieve catalogus vergeleken: identiteit, producttype, titel, aantal velden, fysieke maten, ontbrekende kernvelden en bronblokkades gelijk. Alle1.721aanvullingsregels inclusief bron-URL exact vergeleken. Twaalf EAN-voorbeeldwaarden blijven strings; nul native formulefoutcellen, vijf bladen gerenderd en visueel gecontroleerd. Recalc telt13.161artikelen en10.357artikelen met ontbrekende kernvelden. Geen fysieke Windows/Excel-app-, lokale Git- of live winkeltest geclaimd.

**Eén volgende handeling:** de vastgelegde open bronverschillen en afwijkende slangwaarden per exact artikel toetsen aan actuele technische tekeningen, vóór de volgende verrijkingsbatch uit de resterende werklijst. Volledige officiële mediaontvangst/inventarisatie en latere beoordeelde proef blijven voorwaarden voor iedere Shopify-import.
