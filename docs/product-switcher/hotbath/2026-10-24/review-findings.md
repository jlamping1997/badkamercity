# Onafhankelijke review Hotbath-keuzemenu's — 24 oktober 2026

## Scope en bewijs

Read-only review van de volledige actuele `catalog_snapshot.json`, bestaande `baseline/product-switcher-data.json`, auditcode en voorstellen, plus de afgeleide fabrikantregels in `book_rules.json`. Geen Shopify- of GitHub-mutaties uitgevoerd. De onderstaande toets betreft gegevensgroepering en niet de werking van de uiteindelijke browserinterface.

## Uitkomst

De twaalf onderstaande representatieve gevallen tonen geen onterechte samenvoeging. Modelcodes, configuratiesuffixen en bestaande niet-kleurkeuzes blijven behouden. Een aanvullende volledige projectie van alle HIGH-augmentaties geeft **35 bestaande groepen met 81 nieuwe records**, zonder dubbele volledige keuzetuple of ontbrekend bestaand keuzeveld. Resultaat staat in `review_augmentation_check.json`.

De 739 oorspronkelijke auditbuckets zijn conservatieve vergelijkingsbakken, geen 739 definitieve klantfamilies. Met name douchesets moeten met familiegebonden boekregels verder worden samengebracht voordat dit een uitrolplan wordt. `HIGH` voor een kleurvergelijking betekent dat het volledige SKU-model gelijk is en de titels de kleuren ondersteunen; het bewijst geen volledige technische productcontrole of fabrikantbeschikbaarheid.

## Gecontroleerde gevallen

| Geval | Controle | Resultaat |
|---|---|---|
| IBS70 | 359 echte producten, tien finishes, vijf dimensies; testartikel en IBS7009 gescheiden | Goed. Geen dubbele tuples. Alleen bestaande combinaties aanbieden; ontbrekende IBS70AI4 niet genereren. |
| IBS7009 | 360 producten met dezelfde type keuzevelden, maar andere basiskraan dan IBS70 | Goed. Eigen familie behouden. |
| CB105EXT18 | Tien kleuruitvoeringen, 18 cm uitloop | Goed als kleurvoorstel. Met 25 cm samenbrengen mag pas met de bijbehorende maatregel uit het boek. |
| CB105TEXT18 | Tien kleuruitvoeringen, 3-gatsmodel | Goed. Niet met CB105EXT18 samenvoegen alsof uitsluitend de kleur verschilt. |
| BAA09 | Twaalf zeepdispensers wandmodel, identiek volledig model | Sterke kandidaat voor nieuwe kleurpilot. BAA10 vrijstaand blijft apart. |
| BAA03 | Bestaande handdoekhaakgroep met acht records; vier ontbrekende kleuren in Shopify gevonden | Sterke augmentatiekandidaat. Bestaande acht records behouden en vier toevoegen. |
| AR132 | Vier badafvoeren met identiek model; IX en drie PVD-finishes | Goed als kleurvoorstel. AR133 met vulcombinatie blijft apart. |
| ARA04 | Bestaande toiletrolhoudergroep met drie records, één nieuwe BGP-uitvoering | Goed. Zelfde model; aanvullende kleur onder bestaand groeps-ID. |
| BAA06 / BAA07 | Twee lengtes binnen één bestaande groep; drie plus zes nieuwe kleurrecords | Goed. Alle negen records kregen dezelfde bestaande niet-kleurkeuze van hun eigen model; geen tuplebotsing. |
| GL073 / GL075 | Bestaande groep met/zonder uitloop; één nieuwe kleur per model | Goed. Niet-kleurkeuze blijft behouden; geen botsing na gezamenlijke projectie. |
| AR021 | Textielslangen met zwarte/grijze slang naast finishcodes | Terecht REVIEW. Finish van aansluitingen en kleur van de slang moeten apart verklaard worden. |
| IBS33BGP4 / SDS32BGP | SKU zegt gunmetal, titel zegt geborsteld messing | Terecht REVIEW. Geen automatische kleurcorrectie of inzet in nieuwe productieconfiguratie. |

## Bevinding die voor hergebruik van de audit moet worden opgelost

De eerste versie van `analyze_catalog.py` filtreert nieuwe voorstelproducten niet expliciet op `status == ACTIVE` en een ingevuld `publishedAt`. In de actuele echte catalogus veroorzaakt dit geen fout: alle niet-testproducten zijn actief en gepubliceerd. Een synthetische proef met BAA09BCP op DRAFT en `publishedAt = null` liet het artikel echter nog steeds toe in een HIGH/READY_FOR_PREVIEW-kleurvoorstel.

Aan de audituitvoerder is gevraagd deze gate toe te voegen vóór de nieuwe voorstel-scope. Bestaande groepen moeten wel volledig in de audit blijven voor het signaleren van eventuele latere inactieve of ongepubliceerde leden. De IBS70-pilotgenerator heeft een eigen expliciete publicatiegate nodig, los van dit rapport.

## Uitvoeringsvoorwaarden

- Pas bij augmentatie zowel de productrecords als de `menus.values` aan: nieuwe waarden moeten zichtbaar kunnen worden, bestaande waarden blijven behouden.
- Valideer de volledige uiteindelijke tuple per bestaande groep, niet alleen één kleur/modelbucket afzonderlijk.
- Houd historische finishes zichtbaar als review; het ontbreken van een kleur in editie 18 is geen bewijs dat een bestaand verkoopartikel verwijderd moet worden.
- Los ontbrekende data niet op door theoretische kleur-/maatcombinaties aan te maken.
- Behandel de 696 SPOM-serviceartikelen als aparte werkstroom; zij worden niet door deze nieuwe kleurpilot veranderd.
- Vier bestaande menukeys hebben één waarde. Die kunnen later via de bestaande hide-if-single-value-presentatie worden verborgen; dit is geen blokkade voor de eerste pilot.

## Niet getest in deze review

Shopify-preview, echte keuze-interactie, mobiel, scrollbehoud, cart/prijs/SKU na een wissel, supplier stock en volledige technische eigenschappen van alle nieuwe voorstellen zijn hier niet getest. Dit is een onafhankelijke gegevensreview met expliciete grenzen.
