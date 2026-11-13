> Historisch checkpoint. Actuele presentatie: [BRAUER-31](../2026-11-09/HANDOFF_BRAUER31.md); lees privé `prepared/HANDOFF_BRAUER31.json`.

# BRAUER-30 — overdracht, 8 november 2026

Lees privé eerst `prepared/HANDOFF_BRAUER30.json` en [de actuele gegevenscontrole](SOURCE_REVIEW_BRAUER30.md). Dit is de opvolger van BRAUER-29.

**1.999 letterlijke leveranciersspecificaties toegevoegd**: 1.502 bevestigingen van meegeleverde hoofddouches en 497 deurmechanismen. **55 montageverschillen onderbouwd afgehandeld**, alle oorspronkelijke verschilrecords, kandidaatwaarden en bewijs behouden. De korte pluspunten zijn ongewijzigd.

Definitieve stand: **13.161 artikelen, 180.197 specificatievelden, 44.868 cumulatieve aanvullingen en 425 vragen bij 406 artikelen**. 6.622 artikelen missen nog minstens één gekozen kerngegeven; dit aantal blijft gelijk doordat andere maten of aansluitgegevens ontbreken. 95 open retailveldverschillen, 288 verdachte slangwaarden, oorspronkelijke 42 gegevensblokkades en 163 toekomstige artikelen behouden. Prijzen inclusief 21% btw, SKU/EAN, titels, keuzes en eigen invoer behouden.

**Winkelbrede SKU-/EAN-/handlecontrole voor alle 13.161 artikelen afgerond: nul bestaande matches of handlebotsingen** in de opgeslagen momentopname van 8 november, 21:45–21:51 UTC; 264 volledige querybatches. Geen merkfilter, positieve/negatieve/zoekstaartcontroles PASS. Geen Shopify-ID’s toegewezen. Vlak vóór een latere import opnieuw controleren. De controle geeft geen importtoestemming.

13.728 korte pluspunten bij 7.993 artikelen, maximaal drie; data en het eerdere Pluspunten-blad ongewijzigd. ‘Complete doucheset’ blijft beperkt tot 143 bewezen sets. Materiaalvoordelen alleen bij letterlijk bewijs: 445 massief eiken, 1.427 gelakt MDF. Geen opvulling of installatiebrede ‘alles inbegrepen’-belofte.

**93 tests PASS**, herhaalcontrole PASS, preflight terecht exit 2. Alle artikelregels, cumulatieve aanvullingen, vragen en pluspunten native exact met de bijgewerkte zesbladige XLSX vergeleken. Nul foutcellen; twaalf actuele previews nagekeken. 13.161 offline importregels/39.483 veldwaarden exact en geblokkeerd. Geen fysieke Excel-app-, Windows-Git- of liveproducttest.

Codecheckpoint `deb8b1d638a614dfbc4710dc8d91c8b6638d6593`, actieve codebranch `fix/product-cards-2026-10-14`; main alleen documentatie. De bestaande privébestanden worden met behoud van identiteit vervangen; de centrale status noemt de bevestigde versies. Het pakket behoudt alle oude bestanden, bronhistorie en controlelijsten.

De 4.748 oude pendingrecords zijn volledig verwerkt. **De actuele retailmaster bevat ook de nieuwere gerichte controles; oude pendingrecords mogen die niet overschrijven.** Twee openbare artikelcontroles leverden geen nieuwe toegestane externe feiten. Een toegangsbeperking beëindigde de verdere openbare ontdekking; nul onbevestigde browser-URL’s als bron geaccepteerd. `retail_extract.py` niet op een lege/niet meegeleverde researchmap uitvoeren. Geen blokkeringsomzeiling of variantovererving.

Herbouwvolgorde: `prepare_source_review.py`, `enrich_supplier_specifications.py`, `enrich_retail_specifications.py`, `build_open_work.py`, `build_product_benefits.py`, de bewijsgebaseerde `build_shop_identity_review.py`, daarna `build_import_preparation.py`. De winkelvergelijker leest opgeslagen antwoorden en doet zelf geen API-aanvragen. Voor XLSX eerst de vijf kernbladen heropbouwen en vervolgens Pluspunten toevoegen; primaire Node-runtime met `--max-old-space-size=6144`. Maak `analysis` aan voor de native retailcontrole. De eerdere PowerShell-back-up-/uitpak-/controlereeks blijft in de README staan.

**Alle imports, ook DRAFT, blijven geblokkeerd. Nul Shopify-product-, media-, thema-, definitie- of publicatiewrites.** Volledige officiële media, inventarisatie, gegevensbeoordeling, renderer-integratie en beoordeelde product-/keuzeproef ontbreken nog. Geen volledige technische vrijgave. **Volgende handeling:** na ontvangst van het volledige officiële mediapakket de offline exacte inventarisatie uitvoeren en resterende betwiste artikelgegevens met de fabrikant bevestigen vóór een beoordeelde proef.

Geen actieve BRAUER-bronlezer, browseropdracht of schrijver na overdracht.
