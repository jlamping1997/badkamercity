# Tegels indelen op uitstraling

> **9 november 2026 — TILE-LOOK-01 PILOT_APPLIED_VERIFIED / BOUNDED_BATCH_IN_PROGRESS:** tien SKU-gecontroleerde Cotto-proefartikelen zijn ingedeeld; lookveld, toevoegtags en werkelijke categorieplaats exact teruggelezen. Vijf bestaande lookcategorieën bewezen; Terrazzo behoudt zijn oude22handmatige leden en heeft één nieuwe ALL-tagbron (Tegels EN Terrazzo) voor onderhoudbare toevoegingen. Herstelkopie met alle3.496oorspronkelijke look-/tag-/collectierecords duurzaam bewaard vóór mutaties. De eerste2.003finite doelselecties (inclusief10pilot) worden in25-productbatches toegepast met verse identiteitread, compareDigest:null, tagsAdd en read-after-write; geen bestaande gevulde look overschreven. Native collectietoewijzingen zijn asynchroon; onafhankelijke latere read bevestigt inmiddels de juiste lidmaatschappen. Andere agents doen uitsluitend brononderzoek; deze sessie is de enige lookschrijver. **Eén volgende handeling:** de begrensde batches en eindcontrole afronden, daarna het nieuwe Uitstraling-filter als getest VPS-pakket aanbieden; nog geen live lookfacet claimen.143kleurloze tegels en Cotto-formaatfilter blijven DEFERRED op eigenaarverzoek. [Dossier](filters/tile-look-2026-11-09/README.md).

9 november 2026 · TILE-LOOK-01 · IN_PROGRESS.

## Opdracht en uitgestelde punten

De eigenaar bevestigt dat de kleurupdate goed is en wil nu categoriseren naar steenlook, marmerlook, houtlook en vergelijkbare begrijpelijke keuzes. Nieuwe kleurclassificatie voor de 143 nog kleurloze artikelen en het tegelformaatfilter in het Cottoceramix-merkprofiel zijn op expliciet eigenaarverzoek **DEFERRED**. Ze zijn niet opgelost, verwijderd of automatisch vrijgegeven. Bestaande kleurregels blijven behouden.

## Aanpak

Hergebruik bestaande collectie-identiteiten en het live bestaande productmetafield `tiles.look` (definitie610289287434, single_line_text_field). Geen nieuwe categorieboom of automatische SEO-landingspagina's. Tags sluiten aan op de huidige collectiebronnen; voeg niets toe op basis van alleen een kleurnaam of een dubbelzinnige serienaam. Een mozaïek kan óók een marmerlook hebben: type, uitstraling, toepassing en afwerking blijven onderscheiden.

Volledige read-only Admin-meting van 3.496 actuele tegel-ID's: 3.159 Cotto en 337 Porcelanosa; 358 ingevulde lookvelden en 3.138 ontbrekende. Cotto heeft22Terrazzolook/3.137leeg; Porcelanosa336ingevuld/éénleeg. Geen missende ID's, dubbelen of titel-/handle-/vendordrift ten opzichte van de vorige tegelmeting. Alle variante-/collectiepagina's in deze read volledig; elk artikel één actuele SKU. De read liep09:14:36–09:17:22UTC en is geen atomische cataloguslock. Geen prijzen of klantgegevens opgevraagd.

Primaire bron: [officiële Cotto-cataloguspagina](https://cottoceramix.nl/i/catalogus.html), openbare catalogus CX_Catalogus_2627 met209pagina's, naast de officiële november2026artikellijst voor SKU/serie. Hoofdstuk is geen onvoorwaardelijke look: bijvoorbeeld Ceppo is natuursteenlook, Marmorea marmerlook en AlterEgo bevat verschillende prints. Classificeer met exact SKU-/familiebewijs en gerichte voorbeelden; onzekere gevallen apart behouden. De oorspronkelijke productidentiteit, bestaande lookwaarden, kleuren, maten, koop-/m²-logica en overige collectieleden blijven beschermd.

## Proef en bewijsgrens

Dit checkpoint bevat alleen onderzoek en deze documentatie. Geen Admin-, collectie- of themawrite; geen serveractivatie van een nieuw lookfilter. Een kandidaat-worker kan later `tiles.look` als gesloten checkboxfilter Uitstraling exporteren zonder API- of themacodewijziging; dit is nog geen live resultaat.

**Eén volgende handeling:** tien eenduidige SKU's als proef indelen en metafield, tags en werkelijke collectieplaats teruglezen vóór opschalen. Werk op de bestaande actieve codebranch fix/product-cards-2026-10-14; main is documentatie-ingang. Overige werkstromen/holds behouden.
