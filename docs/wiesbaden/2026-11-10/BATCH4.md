# Wiesbaden — duidelijke nissen en topbladen, 10 november 2026

57 bestaande artikelen toegevoegd aan drie keuzegroepen in hetzelfde ongepubliceerde concept 196416504074 (BadkamerCity - SEO + Wiesbaden concept). Totaal 328 artikelen / 24 groepen. MAIN 196441932042 blijft actief; geen publicatie of MAIN-write.

| Familie | Artikelen | Keuzes |
|---|---:|---|
| Demis inbouwnis | 24 | 6 exacte afwerkingen; Formaat (inclusief diepte): 30 × 30 × 7 / 30 × 30 × 10 / 30 × 60 × 7 / 30 × 60 × 10 cm |
| Alvara topblad, 46 cm diep | 18 | 6 exacte afwerkingen; Breedte 80 / 100 / 120 cm |
| Sulora topblad met afgeronde hoeken, 48 cm diep | 15 | 5 exacte afwerkingen; Breedte 80 / 100 / 120 cm |

Alvara-fonteinbladen 40 × 22 cm blijven apart, met hun bestaande kleurmenu. Een nieuwe keuze levert daar geen extra maat op. Bij Demis zijn diepte en formaat bewust één heldere keuze in plaats van drie losse maatvelden. Geen onderkasten, waskommen, installatieonderdelen of andere constructies aan deze groepen toegevoegd. Technische bronholds van eerdere rondes blijven staan.

## Bron en identiteit

57 bestaande officiële Wiesbaden.nl-artikelrecords van 19 oktober hergebruikt, met exacte SKU/titel/serie/maat/afwerking en leveranciersidentiteit. Huidige Shopify-titels en SKU's komen exact overeen. Demis: staal; Alvara: dicht blad, kunststof, geen sifonuitsparing; Sulora: MDF met folie en afgeronde hoeken. Decor/structuurverschillen van Sulora blijven aan de betreffende artikelen gekoppeld, geen uniforme afwerkingsclaim toegevoegd.

Verse beperkte bronproef: Demis 33.2170 bevestigd via Wiesbaden.nl. Alvara 38.3882 en Sulora 38.3934 gaven 429; geen alternatieve fabrikantclient of nieuwe brede fetch gestart. Dit is geen 57 verse fabrikantpagina's-PASS. Geen .de of Badkamervoorjou-data gebruikt.

## Techniek en Admin

Huidige conceptbodies voor main-product en bc-choice-data-source vooraf identiek aan bestaande codebranch 270789f. Drie begrensde JSON-assets en drie expliciete V2-routes toegevoegd. Bestaande JavaScript/CSS en kleurreferenties ongewijzigd; foto's/prijzen worden uit de passende actuele kleurreferenties geladen.

57 ontbrekende custom.switch_group-velden create-only met compareDigest:null gezet in 25/25/7. Alle waarden exact teruggelezen. 63 producten inclusief zes uitgesloten Alvara-fonteinbladen opnieuw gelezen: titel, handle, vendor, status, publicatie, URL, kleurreferenties, primaire foto, variant/SKU/prijs/bestelbaarheid gelijk aan vóór. Dit dekt geselecteerde velden, geen volledige catalogussnapshot.

Alle vijf geschreven conceptbodies exact teruggelezen. MAIN-rol en drie betrokken codechecksums behouden; drie verse MAIN-productsteekproeven behouden hun oorspronkelijke kleurroute. Geen volledige nieuwe MAIN-inventaris geclaimd.

## Controlebewijs

- 57/57 openbare previewpagina's PASS: juiste themarol, titel, SKU, prijs, eerste foto, begrensde groepsbron, cart-formuliervariant en actuele kandidaatfeiten.
- 327 actuele kandidaatfoto-/prijsfeiten in de 57 serverpagina's exact gekoppeld; dit zijn geen 327 afzonderlijke HTTP-fotodownloads.
- 57 beginstanden en alle 408 enkelvoudige aswissels met de bestaande echte JS-renderer in een lokale DOM-proef PASS. 57 dubbele combinaties geweigerd; onjuiste foto-identiteit valt veilig terug. Geen native mobiele claim.
- Strikte lokale Shopify Liquid/HTML-parser op beide gewijzigde bestanden plus baselines PASS.
- Externe validator printte success met waarschuwingen, maar opvolgende procescontrole werd door automatische review geweigerd vanwege mogelijke verzending van themacode/prompt. Geen herhaling, omweg, afgeronde externe validatie- of exitcodeclaim. Lokale parser en echte Shopify-rendering vormen het afgeronde bewijs.
- Echte Chrome desktop, 1363 px: alle drie families op kleur en maat gewisseld. Demis 33.2170 → 33.2173 → 33.4269, Alvara 38.3882 → 38.3870 → 38.3875, Sulora 38.3934 → 38.3995 → 38.3989. Overige keuze behouden.
- Echte cartproeven: 33.4269 / variant 53859866837258 / €215 en 38.3989 / variant 53859896295690 / €119. Bevestigingsdialoog en cartregels met exacte SKU/variant bekeken. Beide eigen testregels gericht verwijderd; lege winkelwagen bevestigd. Geen checkout/order.
- Demis concept visueel bekeken: zes kleurfoto's, vier volledige formaatknoppen; geen horizontale overloop in gecontroleerde desktopstand.

Native mobiel/fysieke telefoon, Alvara echte cart en volledige cartdekking van eerdere 271 blijven NOT_TESTED. Dit is geen publicatievrijgave.

## Herstel en volgende handeling

Herstel alleen de drie nieuwe routercases, drie groepsnamen in V2-allowlist en drie nieuwe assets ten opzichte van parent 270789f. Herstel geen volledige oudere snapshot. Bij productherstel uitsluitend de 57 in deze ronde aangemaakte switch_group-velden verwijderen nadat actuele waarde/digest nog exact aan dit resultaat gelijk is. Bestaande color_variants en andere velden behouden. Huidige matchtabellen staan in de drie assets; tests en onderbouwing gelden voor het meetmoment van deze ronde.

**Volgende handeling:** gerichte mobiele en resterende echte cartproeven op concept 196416504074 afronden vóór eigenaarpublicatie. Verdere grotere partijen mogen binnen de eigenaaropdracht, met bestaande bronholds behouden. Geen actieve schrijver na overdracht. Geen lokale Windows-/Git-worktreecontrole geclaimd; bron via GitHub-connector gelezen en opgeslagen.

Codecheckpoint: [398f356](https://github.com/jlamping1997/badkamercity/commit/398f356092825825d51d87fde18824aa1707c970).
