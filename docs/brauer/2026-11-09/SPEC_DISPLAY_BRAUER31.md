# BRAUER-31 — echte dubbele specificatieregels

Op verzoek van de eigenaar alleen bewezen dubbelingen uit de voorbereide klantweergave verwijderd. Geen nieuwe bronfeiten en geen canonieke feiten verwijderd. De drie regels vereisen een gelijke niet-lege tekstwaarde, een passende productsoort, beide velden op hetzelfde artikel en geen actieve veldblokkade.

| Verwijderde dubbele naam | Behouden naam | Artikelregels |
|---|---|---:|
| Maat hoofddouche | Diameter hoofddouche | 1.290 |
| Bediening voor aan/uit | Bediening aan/uit | 1 |
| Type deur | Deursysteem | 1 |

**1.292 dubbele regels bij 1.292 artikelen onderdrukt.** 180.197 canonieke bronfeiten blijven behouden; de voorbereide klanttabellen bevatten samen 178.905 regels. Het bestand met volledige bronfeiten en de bewijzen blijven byte-identiek aan BRAUER-30. Prijzen inclusief 21% btw, titels, SKU/EAN, goedgekeurde opties, eigen invoer, alle 13.728 korte pluspunten en bestaande omschrijvingen blijven gelijk.

De wijziging zit uitsluitend in de voorbereide specificatietabel en de bijbehorende bestaande JSON-veldwaarde. Alle 13.161 importregels en 39.483 voorbereide veldwaarden zijn vergeleken: alle andere velden exact gelijk. De canonieke klantgroepen in de broncatalogus blijven beschikbaar voor herkomstcontrole; de importerbuilder past voortaan steeds dezelfde presentatieprojectie toe.

## Bewust behouden

Gelijke waarden zijn op zichzelf geen dubbeling. Breedte en diepte, douchearm en hoofddouche, water- en slangaansluiting, thermostatisch en temperatuurregeling blijven apart. Ook de 67 gelijke paren Dikte/Glasdikte zijn behouden: de generieke dikte noemt het onderdeel niet expliciet. Geen centimeters uit modelcodes of stilzwijgende eenhedenconversie.

Bij vier artikelen zijn Maat hoofddouche en Diameter hoofddouche verschillend. Beide bronwaarden blijven staan; deze vier maatparen zijn expliciet apart vastgelegd voor bronbeoordeling. Deze presentatiecontrole beslist niet welke waarde juist is en voegt deze vier niet stil toe aan de oudere vragenlijst van 425 regels. Zie privé `prepared/specification-display-review31.json`.

Geen bronvragen opgelost of ingetrokken. 6.622 artikelen missen nog gekozen kerngegevens. De bestaande 95 open retailveldverschillen, 288 verdachte slangwaarden, 425 vragen bij 406 artikelen, oorspronkelijke 42 blokkades en 163 toekomstige artikelen blijven behouden.

## Bewijs en herbouw

**52 tests PASS**: acht nieuwe presentatiegrensgevallen, 29 pluspunt-/mappingtests, zes specificatietests en negen voorbereidingstests. Een onafhankelijke vergelijking controleert alle 13.161 voor/na-artikelen; precies de drie goedgekeurde aliasregels verklaren ieder verschil. Herhaalcontrole van vijf uitvoerbestanden en alle inputhashes PASS. Preflight terecht exit 2.

De bestaande specificatie-XLSX versie 11 is byte-identiek behouden. Alle twaalf voorbeelden geven met de presentatieprojectie dezelfde tabellen; alle overige Excelbronnen en afhankelijkheden zijn ook ongewijzigd. Daarom geen XLSX-herbouw, extra variant of nieuwe render nodig. De native retailcontrole is opnieuw uitgevoerd: 13.161 artikelregels, 44.868 cumulatieve aanvullingen, 425 vragen exact en nul foutcellen. Alle zes tabbladen behouden. Geen fysieke Excel-app- of liveproducttest.

Herbouw met `python scripts/brauer/preparation/build_import_preparation.py ROOT`. Deze roept de presentatie-audit automatisch aan. `build_specification_display.py ROOT` kan ook afzonderlijk worden uitgevoerd. De behouden aliaswaarde met bewijs en de gekozen zichtbare waarde staan per gewijzigd artikel in de private historie. Upstream bronverwerking verandert de bewaarde bronfeiten; een nieuwe importerbuild past de presentatieprojectie opnieuw toe.

Codecheckpoint `87463a67014bc8c17cbdcc05749942f7e6637e40` op `fix/product-cards-2026-10-14`; vier generieke codebestanden exact teruggelezen. Main alleen documentatie. Remote controles bewijzen geen lokale Windows-Git-status. De werkmap hier is een uitgepakt privévoorbereidingspakket, geen lokale Git-checkout.

MAIN bij deze ronde alleen gelezen: `196368531722`, ‘BadkamerCity - Hele europrijzen 8 nov’. Dit is de vers gelezen rol; het oudere andere MAIN-nummer in de ingang was een gedateerd checkpoint. Geen thema’s of winkelgegevens geschreven.

**Alle imports, ook DRAFT, blijven geblokkeerd.** Volledige officiële media, exacte inventarisatie, resterende bronbeoordeling en de beoordeelde product-/keuzeproef ontbreken. De winkelbrede identiteitscontrole van BRAUER-30 blijft een gedateerde momentopname en moet voor een latere import opnieuw worden gedaan. Geen volledige technische vrijgave of importgereedheid. Geen actieve bronlezer/schrijver na overdracht.

Volgende handeling: eerst een kleine offline proef met eigen productomschrijvingen maken volgens [het tekstvoorstel](DESCRIPTION_APPROACH_BRAUER31.md), op basis van bewezen kenmerken per exact artikel.
