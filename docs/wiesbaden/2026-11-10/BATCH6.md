# Wiesbaden batch 6 — 10 november 2026

Status: IMPLEMENTED_TEST_ONLY, hetzelfde UNPUBLISHED concept 196416504074. MAIN 196441932042 ongewijzigd; geen publicatie.

## Scope en telling
44 bestaande artikelen toegevoegd in vier groepen; cumulatief 414 artikelen / 30 groepen (voorheen370/26). Exacte actuele Shopify vendor-telling2451, ook2451 ACTIVE en gepubliceerd. Voortgang414/2451;2037 overige artikelen nog inhoudelijk te beoordelen. Niet elk resterend artikel vereist een keuzemenu.

| Groep | Artikelen | Keuzes | Vaste uitvoering |
|---|---:|---|---|
| UniMatch wanddouchearm |14|7 afwerkingen;35/45cm|muurbevestiging|
| Novira topblad |9|3 afwerkingen;80/100/120cm|48cm diep|
| Alvara onderkast |12|6 afwerkingen;80/100cm|2laden;1uitsparing;46cm diep|
| Novira onderkast |9|3 afwerkingen;80/100/120cm|afgeronde hoeken;2laden;1uitsparing;48cm diep|

Bladen en onderkasten blijven afzonderlijke verkoopartikelen. Geen extra menu voor vaste kenmerken, geen bundelclaim. Technische holds uit eerdere batches behouden.

## Bron en onzekerheid
Bestaande officiële wiesbaden.nl-bronrecords (19oktober), exacte leverancier-SKU-identiteit en actuele volledige producttitels gecontroleerd voor44artikelen. Verse webbron Novira38.4007 bevestigt uitvoering. UniMatch29.3881 en Novira38.3964 leverden429; geen claim dat44fabrikantpagina’s opnieuw zijn gelezen. Alvara38.4062 webcache bevat afwijkende corpus/front-materiaalvolgorde ten opzichte van eerder bronrecord; materiaal blijft onopgeloste specificatiehold. Geen materiaalgegevens gewijzigd of materiaalkeuze toegevoegd. Geen badkamervoorjou.nl gebruikt.

## Schrijf- en testbewijs
- Alleen44create-only custom.switch_group velden (compareDigest:null), in25+19 writes; alle44 exact teruggelezen. Geselecteerde overige productvelden gelijk aan baseline.
- Zes conceptbestanden exact teruggelezen: vier JSON-assets, router en main-productsection; bestaande JSrenderer behouden.
- Strikte lokale Liquid-parser: baseline en beide gewijzigde Liquidbestanden PASS. Geen externe validatiehelper opnieuw uitgevoerd.
- Bestaande JSrenderer met lokale DOMsubstitutie:44startstanden,242 geldige aswissels,224 exacte kandidaatafbeeldingen,44prijsorders,44dubbele-combinatiefouten en44identiteitsfouten veilig: PASS. Dit is geen browser-/cartclaim.
- Publieke servermarkup44/44 PASS: conceptthema, identiteit, prijs, eerste foto, cartformuliervariant, asset en alle runtimekandidaatfeiten. Vier MAIN-legacykleursteekproeven PASS; drie MAIN-codechecksums gelijk aan baseline.
- Echte desktopbrowser1363px: Novira-topblad80cm matzwart38.3964 →120cm matzwart38.3979 →120cm matzand38.3983. Titel en actieve breedte/kleur bevestigd; geen horizontale documentoverflow op eindstaat.
- NOT_TESTED: nieuwe echte cartregels; browserwissels van de andere drie families; native mobiel; uitgebreide regressies/checkout. Eerdere batch5cartproeven bewijzen niet automatisch deze44.
- Geen wijzigingen aan prijzen, voorraad, specificaties, publicatie, MAIN-bestanden of noindex.

## Bestanden en herstel
Themebron relatief aan shopify/current/. Vier nieuwe assets: bc-choice-data-144ef5324549e671.json, bc-choice-data-df929692343e984a.json, bc-choice-data-c9a973287933a892.json, bc-choice-data-97c9f5d735c8da6e.json (assets/). Gewijzigd: sections/main-product.liquid en snippets/bc-choice-data-source.liquid.
Voor rollback: herstel beide bestaande bestanden uit parent87a466059dde6401734e71896df6a59e4d476e1d; verwijder uitsluitend deze44nieuw aangemaakte groepsvelden na vergelijking met bijbehorende assetproductIDs en de actuele groepswaarde. Nieuwe ongebruikte JSONassets mogen blijven staan. Andere groepen behouden.
GitHubconnectorworkflow; geen Windows-lokale clean/statusclaim. Geen klantdata, credentials, raw leveranciersbestanden of inkoopprijzen in dit dossier.

Volgende handeling: gerichte mobiele en cart-QA op ditzelfde concept vóór eigenaarpublicatie; verder uitbreiden in gecontroleerde producttypepartijen binnen bestaande opdracht toegestaan. Geen actieve schrijver na overdracht.
