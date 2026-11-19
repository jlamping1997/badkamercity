# Alle zes Wiesbaden-roosters bijgewerkt — 16 november 2026

Status: LIVE_6_OF_6_VERIFIED / GOOGLE_REVIEW_PENDING.

## Opdracht en resultaat

De eigenaar keurt de vierkante foto goed en bevestigt dat deze voor alle zes genoemde roosters gebruikt mag worden. Dit vervangt de eerdere afspraak om eerst Googles pilotbeoordeling af te wachten.
Dezelfde bestaande1000×1000foto is nu bij alle zes producten de hoofdfoto. Voor110cm stond deze al goed; bij de overige vijf toegevoegd en op positie0 gezet. Geen nieuw beeld gegenereerd of geüpload en geen zes kopieën aangemaakt.
Gedeelde MediaImage51610302939402 heeft nu maatneutrale alttekst “Wiesbaden RVS rooster voor douchegoot”; de oorspronkelijke bestands-URL behouden om onnodige wijzigingen van de proef-URL te voorkomen.

## Producten en behoud

|SKU|Product-ID|Variant-ID|EUR-prijs behouden|Eigen technische tekening-ID behouden|
|---|---|---|---:|---|
|33.4213|10657288061194|53859780624650|29.00|51233086144778|
|33.4214|10657288880394|53859781509386|35.00|51233090208010|
|33.4215|10657308705034|53859806314762|39.00|51233184219402|
|33.4216|10657289896202|53859782525194|45.00|51233095418122|
|33.4217|10657289011466|53859781607690|49.00|51233090961674|
|33.4218|10657306870026|53859803332874|66.55|51233175634186|

Hoofdfoto: https://cdn.shopify.com/s/files/1/0941/7959/0410/files/wiesbaden-33-4218-rooster-1000x1000.png?v=1794828909

Elke productgalerij bestaat uit precies de gedeelde vierkante hoofdfoto en de oorspronkelijke eigen technische tekening.
De zes oorspronkelijke smalle beelden zijn nog steeds READY in Files. Alleen hun associatie met hun respectievelijke producten is verwijderd; geen bestandsdelete.
Voor alle zes native get_product vóór/na vergeleken: titel, vendor, status, type, volledige omschrijving, tags, totale voorraad, varianten, valuta en prijzen exact behouden. De status is bij alle zes ACTIVE.

## Uitvoering en controle

1. Alle zes actuele producten en bestaande media gelezen; verwachte SKU/tekening gecontroleerd. Gedeeld bestand READY en1000×1000 bevestigd.
2. Bestaande media via één fileUpdate aan vijf extra producten gekoppeld; alttekst maatneutraal gemaakt.
3. Vijf productReorderMedia-operaties uitgevoerd; onafhankelijke readback bevestigt nieuwe hoofdfoto voor alle zes voordat oude associaties zijn verwijderd.
4. Oude vijf smalle productassociaties verwijderd;110cm was al bij de pilot gedaan.
5. Native get_product-readback6/6: precies juiste hoofdfoto en eigen technische tekening, alle gecontroleerde productgegevens behouden.
6. Publieke product-JSON HTTP200 voor alle zes: eerste afbeelding1000×1000, twee beelden, juiste SKU/prijs en variant image_idnull. Alle zeven beeldbestanden (zes bronfoto’s en één nieuwe hoofdfoto) nog READY.

[Machineleesbaar bewijs en herstelidentiteiten](2026-11-16-ROOSTER-ROLLOUT.json).
[Oorspronkelijke pilot en bronpresentatie](2026-11-16-ROOSTER-PILOT.md) blijft historische bron; de1/6status en wachtinstructie daarin zijn door deze uitrol vervangen.

## Open Google-verificatie

Het aanpassen en publiek uitlezen van de zes fotokoppelingen is afgerond. Googles nieuwe image_link/beeldontvangst en verdwijnen van Image too small zijn niet opnieuw in Merchant bewezen. Geen Google-goedkeuring claimen en geen feedreset uitvoeren. Accountbrede initial review blijft afzonderlijk open.
Exact volgende verificatie: in Merchant5902025216 de zes feedItemId’s uit het JSON-dossier lezen en gebruikte foto/formaatmelding controleren. Geen geplande controle of automatische vervolgactie ingesteld. De overige beeldproblemen (andere smalle Wiesbaden-beelden, SPOM1568, witte tegels, SPOM1633BL) blijven apart staan.

## Herstel

Per product uitsluitend zijn eigen oorspronkelijke MediaImage uit JSON.originalMediaId opnieuw koppelen via fileUpdate.referencesToAdd, op positie0 zetten, controleren en daarna de gedeelde51610302939402 alleen van dat product loskoppelen. De gedeelde media niet verwijderen: alle zes gebruiken hetzelfde bestand. Technische tekening en alle overige gegevens behouden.
