# Verkoopprijzen en afronding

8 november 2026 · PRICE-ROUND-01 · expliciete eigenaarafspraak

Normale EUR-verkoopprijzen **strikt boven €100** afronden naar de dichtstbijzijnde hele euro. Een halve euro gaat omhoog: €149,49 → €149 en €149,50 → €150. Gebruik decimale bedragen met ROUND_HALF_UP. Prijzen tot en met €100 blijven gelijk. Adviesprijzen, inkoopprijzen, oorspronkelijke leveranciersdata en btw-grondslag worden hierdoor niet herschreven.

**Uitzondering in deze ronde:** producten met een m²-/doosprijscontract, inclusief de 3.496 bestaande m²-tegeluitvoeringen. Zonder afzonderlijke keuze tussen m²- en doosafronding blijven beide bedragen, doosinhoud en calculator exact behouden. Voor een expliciet per stuk/pak/set verkocht artikel geldt de gewone verkoopprijseenheid; niet alleen op de categorienaam beslissen.

Shopify bewaart een hele verkoopprijs als bijvoorbeeld 149.00. De storefront mag alleen bij een **werkelijk heel EUR-bedrag vanaf €100** de lege decimalen weglaten. Een nog fractionele prijs van €149,49 mag nooit als €149 worden getoond. Bedragen onder €100 en andere valuta houden hun bestaande opmaak. Dit geldt ook voor echte centen in optelsommen: €109 + €89,60 blijft €198,60. Checkout, staffels, kortingen en andere platformschermen behouden hun eigen notatie en berekening.

De gedeelde presentatie staat in `shopify/current/snippets/bc-money.liquid` en `assets/bc-money.js`. Native kaarten, PDP, productregels in de theme-winkelwagen, accessoires en zes bestaande JS-consumenten gebruiken die helpers. Tegelcalculators zijn niet aangepast. Ontbreekt de JS-helper, dan blijft de bestaande geldnotatie de veilige terugval.

Bij een latere productimport of prijsfeed: lees eerst dit contract, bepaal de echte verkoopeenheid en controleer verkoopprijs/adviesprijs. Pas de afronding op de uiteindelijke verkoopprijs toe zonder bronprijzen te vervalsen. Sla een conflict met adviesprijs, verkoopeenheid of handmatige prijs over voor onderzoek. Dit document bewijst geen ingeschakelde leveranciersfeed en geeft geen opdracht voor een ongevraagde massamutatie.

[Uitvoering, bewijs en herstel](repairs/2026-11-08/whole-euro-prices/README.md).
