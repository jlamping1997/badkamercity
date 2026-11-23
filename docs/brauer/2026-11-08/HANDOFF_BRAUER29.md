> Historisch checkpoint. Actuele stand: [BRAUER-30](HANDOFF_BRAUER30.md); lees privé `prepared/HANDOFF_BRAUER30.json`.

# BRAUER-29 — overdracht, 8 november 2026

De pluspunten zijn opnieuw geselecteerd en korter geformuleerd op verzoek van de eigenaar. **Maximaal drie echte koopredenen per product**, zonder opvultekst. Douchesetinhoud wordt één punt; meubels noemen bewezen materiaal en praktische functies. Lees [de regels en voorbeelden](CURATIE_BRAUER29.md) en privé `prepared/HANDOFF_BRAUER29.json`.

Voorbeelden: ‘Complete doucheset’, ‘Thermostaatkraan’, ‘Draaibare uitloop’, ‘Massief eiken’, ‘Gelakt MDF’, ‘Softclose lades’ en ‘Dimbare verlichting met kleurkeuze’. Alleen toepassen bij exact artikelbewijs. De complete-setclaim vereist bij een inbouwset ook een bewezen inbouwdeel; geen algemene ‘alles inbegrepen’-belofte. Geen materiaal- of vochtwerendheidclaims op basis van alleen een kleur of modelnaam.

Voorbereide selectie: **13.728 teksten bij 7.993 artikelen**. 143 complete-setteksten; 1.872 materiaalteksten, waarvan 445 massief eiken en 1.427 gelakt MDF. 391 spiegelkasten met bewezen verlichting. Per gewijzigd artikel zijn vorige en nieuwe tekst/rule opgeslagen. Bestaande technische feiten zijn niet ingetrokken wanneer een tekst niet meer in de korte lijst staat.

**De catalogus en al het technische bewijs zijn byte-identiek aan BRAUER-28.** 13.161 artikelen, 178.198 specificatievelden, 6.622 artikelen met ontbrekende gekozen kerngegevens, 150 open retailveldverschillen, 288 verdachte slangwaarden, 480 vragen bij 461 artikelen, oorspronkelijke 42 gegevensblokkades en 163 toekomstige artikelen. De eerdere 24 deurverfijningen en historie zijn behouden. Prijzen inclusief 21% btw, SKU/EAN, titels, goedgekeurde keuzes en eigen invoer ongewijzigd.

**44 tests PASS**, herhaalcontrole PASS, preflight terecht exit 2. Alle 13.161 offline importregels en 39.483 voorbereide bestaande veldwaarden exact vergeleken. Elk artikel blijft expliciet geblokkeerd; geen API-importer, voorraadgetallen, productstatus of publicatieopdrachten. Native XLSXcontrole PASS: zes tabbladen, eerste vijf bladen/421.953 cellen inclusief native stijlen, tabellen en instellingen behouden. Pluspunten exact vergeleken op alle 13.161 artikelregels/EAN’s en 13.728 teksten, maximaal drie per artikel. Alle EAN’s als tekst, nul foutcellen. De oude retailcontrole bevestigt 42.869 cumulatieve aanvullingen en 480 vragen. Geen fysieke Excel-app-test. Negen nieuwe previews inhoudelijk bekeken, inclusief bewust lege lijsten.

Codecheckpoint `be541a97f78d57549e36f431a4411bf589a43380`, actieve branch `fix/product-cards-2026-10-14`. Main alleen documentatie. MAIN opnieuw alleen gelezen: `196368531722`. Drie bestaande definities/types/validaties opnieuw gelezen en gelijk; geen definities of winkelwaarden geschreven. Geen nieuwe retail- of fabrikantpagina’s gelezen. Geen fysieke Excel-app-, Windows-Git- of liveproducttest.

Herbouw de teksten met `build_product_benefits.py`, daarna `build_import_preparation.py`. Gebruik voor de grote XLSX de primaire Node-runtime **met `--max-old-space-size=6144`**, de bestaande `build_product_benefits_workbook.mjs`, pakketroot en bron-XLSX. Alleen Pluspunten wordt bijgewerkt; geen nieuwe workbookvariant maken. Vergelijk native met `verify_product_benefits.py ROOT FINAL_XLSX SOURCE_XLSX`.

**Alle imports, ook DRAFT, blijven geblokkeerd.** Volledige officiële media, inventarisatie, gegevensbeoordeling en de beoordeelde product-/keuzeproef ontbreken nog. **Eén volgende handeling:** bij ontvangst van de volledige officiële media de offline inventarisatie op exacte artikelnummers uitvoeren en onduidelijke koppelingen beoordelen. De bronregels uit eerdere handoffs blijven gelden; `retail_extract.py` niet op een lege of ontbrekende researchmap uitvoeren.

Geen actieve BRAUER-bronlezer of schrijver na overdracht. De centrale status noemt de bevestigde opgeslagen bestandsversies.
