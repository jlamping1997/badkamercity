# BRAUER-30 — specificaties, bronverschillen en winkelcontrole

Deze ronde gebruikt eerst het bewaarde artikelbewijs. **1.999 specificatievelden toegevoegd uit de oorspronkelijke leveranciersrij van exact hetzelfde BRAUER-artikelnummer en EAN**: 1.502 bevestigingen ‘Hoofddouche inbegrepen: Ja’ en 497 deurmechanismen. Alleen expliciete onderdelenzinnen en letterlijke productgroepen; geen fysieke maten uit modelcodes. Een draai-schuifdeur blijft een draai-schuifdeur. Losse onderdelen krijgen geen eigenschappen van een complete cabine.

**55 montageverschillen onderbouwd afgehandeld**, met behoud van de oorspronkelijke leverancierswaarde, alle oude kandidaatwaarden en de bronhistorie. Voor 36 topbladen zijn ‘ophangen’ en ‘Vrijhangend aan de wand’ contextueel dezelfde montage. Bij 19 overige artikelen bevestigt een exact passende retailtabel de bestaande leverancierswaarde. Deze vergelijking maakt geen nieuwe locatie-eigenschap. 95 veldverschillen bij 76 artikelen blijven open.

De 4.748 oude pendingrecords waren al volledig in de master verwerkt; nul onbenutte sterke, niet-geblokkeerde retailfeiten. Geen duizenden pagina’s opnieuw gelezen. Twee gerichte openbare artikelcontroles leveren geen nieuwe externe feiten: één pagina mist EAN; één spreekt zichzelf over het inbouwdeel tegen. Vorige en nieuwere records staan apart in de private historie en de actuele master bevat de laatste controle.

Bij openbare ontdekking werd een toegangsbeperking gemeld. Die route is beëindigd en alle teruggegeven onbevestigde URL’s/aantallen zijn buiten het bewijs gehouden. Geen verdere poging met gewijzigde browserinstellingen. De oude pendingrecords zijn nu historische input; laat deze bij hervatting geen later gecontroleerde masterrecords overschrijven. Voer `retail_extract.py` nooit uit op een lege of niet meegeleverde researchmap.

## Definitieve gegevens

| Onderdeel | Stand |
|---|---:|
| Unieke artikelen | 13.161 |
| Specificatievelden | 180.197 |
| Cumulatieve retailaanvullingen | 38.569 |
| Cumulatieve leveranciersaanvullingen | 6.299 |
| Totaal cumulatieve aanvullingen | 44.868 |
| Artikelen met minstens één ontbrekend gekozen kerngegeven | 6.622 |
| Open retailveldverschillen | 95 |
| Verdachte slangwaarden | 288 |
| Open vragen / betrokken artikelen | 425 / 406 |
| Oorspronkelijke gegevensblokkades / toekomstige artikelen | 42 / 163 |

Het aantal artikelen met ontbrekende kerngegevens blijft 6.622: deze artikelen missen nog andere gekozen maten of aansluitgegevens. Dit zijn geen ontbrekende producten. Alle eerdere technische waarden en bewijzen behouden. Geen prijzen, artikelnummers/EAN’s, titels, goedgekeurde keuzegroepen of eigen aanvullingen gewijzigd. Prijzen blijven inclusief 21% btw.

De **13.728 korte pluspunten bij 7.993 artikelen zijn byte-identiek aan BRAUER-29**, maximaal drie per product. Ook de oude Pluspunten-werkbladwaarden, stijlen, native tabellen en instellingen zijn behouden. Geen extra ‘complete set’-claims door de nieuwe componentvelden: de 143 bestaande complete-setteksten blijven gelijk, met hoofd- en handdouche, slang én inbouwdeel vereist. Meubelvoordelen blijven letterlijk bewezen ‘Massief eiken’ of ‘Gelakt MDF’.

## Alleen-lezen winkelvergelijking

Alle 13.161 artikelregels winkelbreed gecontroleerd op SKU, EAN en voorgestelde handle, **zonder merkfilter**. 264 querybatches en 264 complete antwoordpagina’s. Positieve en negatieve controles plus echte bestaande codes aan het einde van lange zoekopdrachten slagen. De connector geeft meervoudige `barcodes`; alle barcodewaarden zijn in de vergelijking betrokken.

**Geen bestaande identifier- of handlematches gevonden.** Dit is een momentopname van 8 november 2026, 21:45–21:51 UTC. Geen Shopify-ID’s toegekend en geen artikelstatus veranderd. Herhaal de controle onmiddellijk vóór een ooit toegestane import. Het private werkpakket bevat de volledige werklijst, queryreceipts, controles en vergelijking; het importplan bindt deze met hashes. Nul Shopify-writes.

## Controle en grenzen

**93 tests PASS**, herhaalcontrole van 17 voorbereide bestanden PASS. Alle 13.161 offline importregels en 39.483 veldwaarden exact vergeleken; ieder artikel blijft geblokkeerd. Preflight terecht exitcode 2.

Native XLSXcontrole PASS: alle 13.161 artikelregels, 44.868 cumulatieve aanvullingen en 425 vragen exact gelijk aan de definitieve gegevens. Zes tabbladen; de 433.956 cellen van de opnieuw opgebouwde vijf kernbladen blijven bij toevoegen van Pluspunten behouden. Dit is geen claim dat deze vijf bijgewerkte bladen gelijk zijn aan de oudere ronde. De aparte behoudcontrole bevestigt dat het eerdere Pluspunten-blad gelijk is gebleven. Alle 13.161 pluspuntregels/EAN’s en 13.728 teksten exact, EAN’s als tekst, nul foutcellen. Twaalf actuele views visueel bekeken. Geen fysieke Excel-app-, Windows-Git- of liveproducttest.

Codecheckpoint `deb8b1d638a614dfbc4710dc8d91c8b6638d6593` op `fix/product-cards-2026-10-14`; zeven generieke codebestanden exact teruggelezen. Main alleen documentatie. Volledige artikeldata, winkelidentiteiten, herkomst en antwoorden blijven in het private pakket.

**Alle imports, ook DRAFT, blijven geblokkeerd.** Volledige officiële afbeeldingen en PDF’s, inventarisatie, resterende gegevensbeoordeling, renderer-integratie en de beoordeelde product-/keuzeproef ontbreken. Geen volledige technische vrijgave of importgereedheid. Geen actieve BRAUER-bronlezer, browseropdracht of schrijver na overdracht. **Volgende handeling:** bij ontvangst van het volledige officiële mediapakket offline op exact artikelnummer inventariseren en de resterende betwiste gegevens met de fabrikant bevestigen vóór een beoordeelde proef.
