# BRAUER-27 — duidelijke pluspunten, 8 november 2026

De eigenaar vraagt korte productpluspunten op basis van bevestigde gegevens, zoals inbegrepen inbouwdeel en draaibare uitloop. **8.212 pluspunten bij 6.366 artikelen voorbereid**, maximaal vier per artikel. De huidige gegevens leveren maximaal drie op. Ontbrekende positieve gegevens blijven leeg; een bronconflict levert geen pluspunt op.

## Teksten en onderbouwing

| Pluspunt | Bevestigde basis | Artikelen |
| --- | --- | ---: |
| Inclusief hoofd- en handdouche, slang en inbouwdeel | Vier inbegrepen-componentvelden exact Ja | 143 |
| Hoofd- en handdouche met doucheslang | Drie inbegrepen-componentvelden exact Ja | 47 |
| Inclusief inbouwdeel | Inbouwdeel inbegrepen = Ja, zonder dubbeltelling in samengestelde tekst | 177 |
| Draaibare uitloop | Expliciete positieve draaibaarheid; geen negatieve of conflicterende waarde | 63 |
| Thermostatische bediening | Thermostatisch = Ja | 2.206 |
| Handdouche met 3 straalstanden | Bevestigd aantal en passende handdouche/set | 1.029 |
| Met koudestartfunctie | Koudestartfunctie = Ja | 25 |
| Glas voorzien van coating | Glascoating = Ja bij passend glasproduct | 1.056 |
| Links of rechts te monteren | Expliciete montagewaarde bij passend glasproduct | 489 |
| Softclose sluiting | Softclose = Ja bij onderkast of spiegelkast | 2.977 |

De teksten noemen precies de bevestigde onderdelen. De onbegrensde tekst **complete doucheset** is niet toegepast. Geen onbekende inbouwdelen, bevestigingsmaterialen of andere onderdelen als inbegrepen voorgesteld. Geen nieuwe waterbesparings-, veiligheids-, onderhouds- of garantieclaim afgeleid uit algemene producteigenschappen. Geen overerving tussen kleuren, maten, modellen of families; titel, opties en producttype alleen vormen geen veldbewijs.

`prepared/product-benefits.json` bewaart artikelnummer, EAN, teksten en per pluspunt de exacte bestaande specificatie plus het bronfragment/bronverwijzing. Herkomst is de al gecontroleerde leverancierslijst of eerdere exacte merk/SKU/EAN-bron. **Geen nieuwe externe feiten of broncrawl.** De catalogus en alle oorspronkelijke specificaties, bewijs, prijzen inclusief 21% btw, titels, keuzes, eigen invoer en bronbestanden blijven byte-identiek. De pluspunten zijn een afzonderlijke afgeleide dataset; zij verhogen het aantal technische specificaties niet.

## Excel en controles

Het bestaande specificatiebestand heeft een nieuw filterbaar tabblad **Pluspunten** met alle 13.161 artikelnummers/EAN’s, maximaal vier teksten, bewijsvelden en bronverwijzingen. Lege teksten blijven leeg. De vijf eerdere tabbladen zijn behouden.

**23 actuele tests PASS:** acht pluspuntregels, zes specificatietests en negen voorbereidingstests. Catalogus/keuzes/prijs-/identiteitsgegevens byte-identiek; generatie herhaalbaar zonder verschillen. Native vergelijking: **421.953 bestaande cellen**, waarden/formules/types/stijlen, rij-/kolominstellingen, freeze panes, conditional formats en opgeloste native tabellen behouden. **13.161 nieuwe artikelregels en 8.212 pluspunten** exact gelijk aan JSON; alle 13.161 EAN’s tekst, zes tabbladen, nul foutcellen. Vijf nieuwe views bekeken. De bestaande native retailcontrole bevestigt opnieuw alle 13.161 artikelen, 42.869 cumulatieve technische aanvullingen en 480 vragen.

Preflight terecht exitcode 2. Geen fysieke Excel-app-, Windows-Git- of livewinkeltest geclaimd. Bronbestandsversies: pakket 10 / XLSX 7. De centrale status noemt de bevestigde uitvoerversies; bestaande bestandsidentiteiten blijven behouden.

## Overdracht en harde grens

De technische stand blijft **178.198 velden**, 6.622 artikelen met ontbrekende gekozen kerngegevens, 150 open retailveldverschillen, 288 verdachte slangwaarden en 480 vragen bij 461 artikelen. Oorspronkelijke 42 gegevensblokkades en 163 toekomstige artikelen behouden. Volledige officiële afbeeldingen/PDF’s en de beoordeelde product-/keuzeproef ontbreken nog. **Alle imports blijven geblokkeerd, ook DRAFT. Geen Shopify-, media-, thema- of publicatiewrites.** MAIN read-only qua rol bevestigd: 196354474250. Geen volledige technische vrijgave of importgereedheid.

Codecheckpoint `b7bebe707714676f56cbcf43ba0d186b98a43a3a` op `fix/product-cards-2026-10-14`, vier generieke codepaden remote exact gecontroleerd. Main is uitsluitend documentatie-ingang. Catalogus/broninhoud en eigen invoer blijven privé. Geen actieve lezer of schrijver na overdracht.

Lees [de actuele overdracht](HANDOFF_BRAUER27.md) en privé `prepared/HANDOFF_BRAUER27.json`. **Eén volgende taak:** gericht verdere series/kleuren van resterende inbouwdouchesets en glas onderzoeken bij toegestane winkels, exact op merk/SKU/EAN. Afgeronde URL’s niet opnieuw lezen. Behoud de afgeleide pluspunten en bouw ze opnieuw op als gecontroleerde specificaties veranderen.
