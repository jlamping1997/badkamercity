# BRAUER-25 — gerichte aanvulling via Sanitairwinkel

Op verzoek van de eigenaar verder onderzocht wat de twee toegestane winkels nog kunnen aanvullen. BRAUER-24 omvatte vooral BadkamerXXL: 5.853 pagina’s tegenover 20 van Sanitairwinkel. Deze nieuwe ronde benut Sanitairwinkel gericht, zonder de eerdere duizenden pagina’s opnieuw te lezen.

## Resultaat op 8 november 2026

| Gegeven | Eindstand |
| --- | ---: |
| Artikelen | 13.161 |
| Specificatievelden inclusief identiteit | 176.303 |
| Nieuwe velden in deze ronde | 2.523 |
| Oudere externe maten ingehouden bij tegenspraak | 5 |
| Netto extra velden | 2.518 |
| Artikelen meer met gekozen kernvelden ingevuld | 253 |
| Artikelen met ontbrekende gekozen kernvelden | 6.752 |
| Open retailveldverschillen | 72 |
| Verdachte slangwaarden, ingehouden | 288 |
| Concrete vragen / betrokken artikelen | 402 / 398 |
| Cumulatieve retail- / leveranciersaanvullingen | 36.644 / 4.300 |

Nieuwe waarden omvatten onder meer 292 hoogtes, 222 breedtes, 222 dieptes, 261 softclosevelden, 258 spiegelverwarmingsvelden, 159 schakelaarvelden en 260 stopcontactvelden. Ja en Nee zijn alleen uit letterlijk aanwezige tabelwaarden overgenomen. Prijzen, SKU/EAN, titels, keuzes, eigen invoer, originele bestanden en media zijn behouden.

Er zijn zes series gericht geïnventariseerd: Impress, Impress Deluxe, Creek, Collision, Cosmic en Garnet. Van 454 gevonden artikel-URL’s waren vijf al verwerkt. Alle 449 nieuwe geselecteerde pagina’s plus één extra identiteitstest zijn gelezen. Van die 450 pagina’s zijn 406 exact op merk/fabrikantartikelnummer/EAN bevestigd, 31 zonder EAN alleen als vergelijking bewaard en 13 niet als zelfstandige bron gebruikt. Tijdelijke fouten maximaal eenmaal herhaald; nul resterende leesfouten. Geen blokkade omzeild of betaalde uitbreiding ingeschakeld. De gepubliceerde limiet van 150 URL’s/minuut gerespecteerd met een lagere ingestelde grens.

De gezamenlijke bronset bevat nu 6.310 records, waarvan 6.276 exacte merk/SKU/EAN-pagina’s. Dit is geen broncontrole van ieder artikel in de volledige catalogus. Het ontbrekende fabrikantartikelnummer bij een Amaze-proefpagina is geen reden om de overige varianten zonder controle over te nemen; die serie is niet blind massaal gelezen.

## Correctheid en verschillen

Vijf eerder extern overgenomen maatvelden zijn ingehouden na nieuwe tegenspraak. Geen alternatieve maat ingevuld. Alle 31 eerdere open retailverschillen en hun historische waarden zijn behouden. De oorspronkelijke 42 gegevensblokkades en 163 toekomstige artikelen blijven intact. Tellingen overlappen en zeggen niet hoeveel producten ontbreken.

Algemeen hout is verenigbaar met een al letterlijk vastgelegde leverancierswaarde massief eiken. Die semantische vergelijking voorkomt onnodige verschillen, zonder eiken of massief hout uit een algemene bronwaarde af te leiden. Werkelijke afwijkingen zoals massief eiken versus MDF blijven open. Materiaalvragen noemen voortaan de concrete bronwaarden in plaats van uitsluitend RVS/messing.

Geen fysieke maten uit unitloze modelcodes, geen ontbrekend icoon als Nee, geen 15→150 cm-correctie en geen overerving naar andere kleuren, maten of modellen. Badkamervoorjou.nl volledig uitgesloten.

## Verificatie en herstel

- **44 tests PASS:** 23 specificatie-/retail-/leverancierstests, negen voorbereidingstests, zes hervattingstests en zes Sanitairwinkel-extractietests.
- Herhaalde verrijking behoudt catalogus, veldherkomst, samenvatting, cumulatieve aanvullingen en historische verschillen exact; nul nieuwe velden op herhaling.
- Native XLSX: alle 13.161 artikelregels, 40.944 cumulatieve aanvullingen en 402 vragen exact gelijk. Alle 459 EAN-cellen in het vragenblad zijn tekst; twaalf EAN-voorbeelden eveneens. Nul native foutcellen.
- Vijf bladen en drie aanvullende ranges visueel gecontroleerd. Overzichtuitkomsten 13.161 / 6.752 gecontroleerd. Geen Excel-desktop- of Windows-worktreetest geclaimd.
- Preflight geeft terecht exitcode 2 en een inhoudelijk gecontroleerd JSON-blokkeerresultaat. Alle vrijgavevlaggen blijven false.

De bestaande privé-ZIP en specificatie-XLSX behouden hun identiteit. Lees `prepared/HANDOFF_BRAUER25.json`; HANDOFF_BRAUER24 is duidelijk als historie gemarkeerd. Samengevoegde getypeerde bronnen, nieuwe literalentabellen, identiteitsuitkomsten en reproduceerbare code blijven privé in het pakket. Ruwe fetchresponses zijn niet gebundeld. De extractie bewaart bestaande records bij een lege bronmap. De 437-aanvragenlijst is een voltooide inputlijst.

Codecheckpoint **84396d58aac120b9ba359c47e5fcbabb7a9dd5af**, vijf codepaden remote exact gecontroleerd op `fix/product-cards-2026-10-14`. Main ontvangt uitsluitend documentatie. **Geen Shopify-writes, DRAFT-import, media-upload, themawrite of publicatie.** MAIN alleen qua rol gelezen: 196341825802. Geen actieve bronlezer/schrijver na overdracht.

**Volgende taak:** gericht verder zoeken voor resterende inbouwdouchesets en glastypen bij de toegestane winkels, telkens met exacte identiteit. Officiële volledige afbeeldingen/PDF’s nog afwachten; inventarisatie, exacte koppeling en een beoordeelde volledige product-/keuzeproef blijven verplicht vóór iedere import. Geen volledige technische vrijgave of importgereedheid.
