# BRAUER-31 — overdracht, 9 november 2026

Lees privé eerst `prepared/HANDOFF_BRAUER31.json`, daarna [de specificatieprojectie](SPEC_DISPLAY_BRAUER31.md) en [de omschrijvingsaanpak](DESCRIPTION_APPROACH_BRAUER31.md). Dit is de opvolger van BRAUER-30.

**1.292 bewezen dubbele regels uit de voorbereide klantweergave gehaald bij 1.292 artikelen.** 1.290 hoofddouchematen, één dubbele bediening en één deurmechanisme. 180.197 canonieke bronfeiten behouden; 178.905 regels in de klantprojectie. De oorspronkelijke catalogus, bewijs, prijzen inclusief 21% btw, titels, SKU/EAN, keuzes, eigen invoer, pluspunten en omschrijvingen blijven byte-identiek. Alleen de twee specificatieprojecties in de offline artikelpayload wijzigen.

Vier verschillende hoofddouchemaatparen blijven apart voor bronbeoordeling. 67 generieke dikte/glasdikteparen bewust behouden. Geen verschillende onderdelen samenvoegen enkel omdat de waarden gelijk zijn. De bestaande vragenlijst van 425 regels is ongewijzigd; de vier presentatieverschillen staan afzonderlijk in `prepared/specification-display-review31.json`.

**52 tests PASS**, herhaalcontrole van vijf voorbereide bestanden PASS; alle 13.161 importregels/39.483 veldwaarden exact vergeleken en geblokkeerd. Preflight terecht exit 2. De bestaande zesbladige XLSX versie 11 is byte-identiek behouden: alle twaalf voorbeeldprojecties en bronafhankelijkheden ongewijzigd. Native controle opnieuw PASS voor 13.161 artikelen, 44.868 aanvullingen en 425 vragen. Geen nieuwe workbookvariant, fysieke Excel-app-, Windows-Git- of liveproducttest.

13.728 korte pluspunten bij 7.993 artikelen, maximaal drie per product, behouden. 6.622 artikelen missen nog kerngegevens; bestaande 95 retailveldverschillen, 288 verdachte slangwaarden, oorspronkelijke 42 blokkades en 163 toekomstige artikelen blijven behouden.

Codecheckpoint `87463a67014bc8c17cbdcc05749942f7e6637e40`, vier generieke bestanden exact teruggelezen op `fix/product-cards-2026-10-14`; main alleen documentatie. `build_import_preparation.py ROOT` past automatisch de pure presentatieprojectie toe en schrijft de private historie/audit opnieuw. Bronverwerking en letterlijke gegevens blijven afzonderlijk behouden.

De 4.748 oude pendingrecords zijn volledig verwerkt; de actuele retailmaster bevat de latere controles. Oude pendingrecords mogen deze niet overschrijven. Geen `retail_extract.py` op een lege of ontbrekende researchmap. Geen nieuwe bronpagina’s gelezen en geen toegangsbeperking omzeild.

MAIN alleen gelezen: `196368531722`. Nul Shopify-writes. De winkelbrede identiteit/handlecontrole van BRAUER-30 is een momentopname die vóór een toekomstige import moet worden ververst.

**Alle imports, ook DRAFT, blijven geblokkeerd.** Officiële volledige media, inventarisatie, resterende gegevensbeoordeling, renderer-integratie en beoordeelde product-/keuzeproef ontbreken. Geen volledige technische vrijgave.

**Eén volgende handeling:** een kleine offline proef met eigen productomschrijvingen maken, volgens het tekstvoorstel, en per tekst het exacte bewijs vastleggen. Daarna pas de tekstaanpak over het volledige assortiment toepassen. Geen actieve bronlezer/schrijver na overdracht. De centrale status noemt de bevestigde bestandsversies.
