# BRAUER-26 — verdere specificaties, 8 november 2026

De gerichte vervolgronde bij Sanitairwinkel is afgerond. Het bestaande leveranciersbestand en de eerdere BadkamerXXL-/Sanitairwinkel-bronnen zijn behouden. Er draait geen bronlezer of schrijver na overdracht.

## Resultaat

- 13.161 artikelen, **178.198 specificatievelden**. **1.931 nieuwe velden** toegevoegd; **36 eerder overgenomen externe maten ingehouden** wegens tegenspraak. Netto 1.895 extra velden; nul oude waarden vervangen door een alternatieve maat.
- 130 artikelen meer met alle gekozen kernvelden aanwezig. Nog **6.622 artikelen** missen zulke gegevens; dit zijn geen ontbrekende producten en geen volledige technische vrijgave.
- 150 open retailveldverschillen en 288 verdachte slangwaarden. Alle 72 eerdere open verschillen en historische waarden behouden. **480 concrete vragen bij 461 artikelen**. Oorspronkelijke 42 gegevensblokkades en 163 toekomstige artikelen behouden; tellingen overlappen.
- Prijzen inclusief 21% btw, SKU/EAN, titels, goedgekeurde keuzegroepen, eigen invoer en drie originele leveranciersbestanden behouden.

## Bronnen en verwerking

Drie rechtstreekse serie-ingangen onderzocht: Chrome Edition, Chrome Carving en Stellar. 416 unieke gepubliceerde product-URL’s aangetroffen; geselecteerd zijn Chrome-URL’s met inbouw en alle Stellar-URL’s: 335 kandidaten. Vier eerdere URL’s overgeslagen, alle 331 nieuwe geselecteerde pagina’s gelezen, plus twee inbouwsetpilots buiten deze selectie. **333 nieuwe productpagina’s: 325 exact op merk/fabrikantartikelnummer/EAN, acht zonder EAN uitsluitend vergelijkingsbewijs.** Geen identiteitsquarantaine en nul resterende leesfouten. Tijdelijke fouten eenmaal herhaald; leeslimiet van 150 URL’s per minuut gerespecteerd. Geen blokkades omzeild. De getest aangeleverde hashfilters werden door de fetchroute genegeerd; daarom zijn rechtstreeks gepubliceerde seriepagina’s gebruikt, zonder ongerichte categoriecrawl.

Samengevoegd bronbestand: **6.643 records, waarvan 6.601 exacte merk/SKU/EAN-identiteiten**. Nieuwe bronrecords gaan bij dezelfde canonieke URL voor; oude bronverschillen blijven bewaard. Geen data van de uitgesloten winkel. Broninhoud en exacte catalogus blijven privé. Letterlijke technische tabeluittreksels zijn bewaard; ruwe fetchresponses zijn niet gebundeld.

De parser herkent nu ook expliciete tabelcellen Inclusief inbouwdeel/Inbouwdeel. Alleen bekende positieve/negatieve waarden gelden; ontbrekende iconen en onbekende waarden blijven onbekend. Dit veld is tot passende kraantypen beperkt. Generieke vorm/uitloop zonder componentcontext wordt bij complete inbouwdouchesets niet overgenomen. Geen maten uit unitloze modelcodes of correctie van slangwaarden 15 naar 150 cm. Nieuwe extractierondes gebruiken afzonderlijke uitvoerbestanden en kunnen eerdere getypeerde bronnen niet door een lege raw-map vervangen.

## Controles

**46 tests PASS:** 24 specificatie-/retail-/leverancierstests, negen voorbereidingstests, zes hervattingstests, zeven Sanitairwinkel-extractietests. Herhaalrun verandert catalogus, bewijs, samenvatting, cumulatieve aanvullingen en historische bronverschillen niet. Zakelijke velden exact gelijk aan de ronde-ingang; alle 38.569 retailaanvullingen hebben letterlijke bron en exacte identiteit.

Definitieve XLSX native exact vergeleken: **13.161 artikelregels, 42.869 cumulatieve aanvullingen (38.569 retail + 4.300 leverancier), 480 vragen**. Alle 545 EAN-cellen in het vragenblad tekst; 12 EAN-voorbeelden tekst; nul native foutcellen. Vijf bladen en drie extra ranges visueel bekeken. Preflight geeft terecht exitcode 2 en import_allowed false. Geen fysieke Excel-desktop-, Windows-Git- of livewinkeltest geclaimd.

Codecheckpoint **14c893fef895bde189a78813f92bd6afb543c2d1** op `fix/product-cards-2026-10-14`; alle vijf gewijzigde codeblobs remote exact teruggelezen. Overige branchwijzigingen behouden. Main blijft uitsluitend documentatie-ingang. De centrale status bevat de bevestigde privébestandsversies.

## Harde grens en vervolg

**Geen Shopify-writes, ook geen DRAFT-import, media-upload, themawrite of publicatie. Alle vrijgavevlaggen blijven false.** MAIN alleen read-only qua rol bevestigd: 196341825802. De volledige officiële afbeeldingen en PDF’s zijn nog niet ontvangen. Geen volledige technische vrijgave of importgereedheid.

Lees [de actuele overdracht](HANDOFF_BRAUER26.md) en privé `prepared/HANDOFF_BRAUER26.json`. De werklijsten van BRAUER-24/25 en de 335 kandidaten/331 aanvragen van deze ronde zijn voltooide input. Geen duizenden pagina’s opnieuw uitlezen. Eén volgende taak: gericht andere series/kleuren van resterende inbouwdouchesets en resterend glas onderzoeken bij de toegestane winkels, exact op merk/SKU/EAN. Daarna blijven volledige officiële mediainventarisatie, exacte koppeling en een beoordeelde representatieve product-/keuzeproef vereist vóór iedere import.
