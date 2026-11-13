# Winkelbreed bestellen — 8 november 2026

## Resultaat

De eigenaar heeft expliciet bepaald: “Alle producten over heel de winkel kun je gewoon bestellen niks is uitverkocht alles kan de winkelwagen in”.

De voorraadblokkades zijn live opgeheven. **767 bestaande voorraadgevolgde varianten** zijn van DENY naar CONTINUE gezet. **73 varianten** waren vooraf niet bestelbaar en zijn daarna beschikbaar geworden. Alle **851 voorraadgevolgde varianten** zijn volledig opnieuw gelezen: 851 beschikbaar, 851 CONTINUE, nul resterende DENY.

De overige **15.070 gepubliceerde producten** hebben geen voorraadtracking. Hun voorraad beperkt het bestellen al niet; zij zijn niet onnodig gewijzigd. Dit is gebaseerd op een exacte Shopify-telling en het gedrag van niet-gevolgde voorraad, niet op 15.070 afzonderlijke winkelwagenproeven.

[Controlebewijs](verification.json) · [Browserproeven](browser-proof.json) · [Vaste bestelafspraak](../POLICY.md).

## Omvang en beslisregel

De winkel bevat 16.527 producten: 15.897 ACTIVE en gepubliceerd op Online Store, plus 24 bestaande UNLISTED producten die via hun directe link gepubliceerd zijn. De 24 bestaande Lagoo-proefproducten behouden hun verborgen cataloguspositie. De 851 gevolgde producten vallen allemaal onder Verlavio. Er zijn in de gepubliceerde scope nul bundelproducten en nul producten met uitsluitend componentvarianten.

De wijziging raakt uitsluitend bestaande, gepubliceerde producten met voorraadtracking aan én inventoryPolicy=DENY. Ook gevolgd DENY met positieve voorraad is omgezet: voorraad hoeft dan later evenmin een grotere bestelling of nulstand te blokkeren. Bestaande 84 CONTINUE-varianten zijn volledig gelijk gebleven.

DRAFT, ARCHIVED, niet-gepubliceerde producten en eerder verwijderde definitief vervallen artikelen zijn niet opnieuw aangeboden. De afzonderlijke Brauer-import- en media-afspraken blijven gelden.

## Uitvoering en gegevensbehoud

Voor uitvoering zijn de oorspronkelijke waarden, exacte doel-ID’s en herstelregel privé bewaard. De mutatie was productVariantsBulkUpdate met allowPartialUpdates:false en per bestaande variant uitsluitend id en inventoryPolicy:CONTINUE. Geen voorraadaantallen verzonnen en tracking niet uitgezet.

Eerst BC_2009: vers gelezen, van DENY naar CONTINUE gezet en teruggelezen; voorraad bleef nul en availableForSale werd true. De echte live productknop voegde het artikel daarna toe. Vervolgens 39 begrensde verzoeken met maximaal twintig productmutaties per verzoek. Iedere groep heeft een verse vóórmeting en directe volledige teruglezing. De operatie heeft geen CAS-argument; daarom zijn bronstatus en doel-ID’s vlak voor elke groep gecontroleerd. Alle veertig responses zijn foutloos en dekken samen exact 767 unieke varianten.

De finale volledige vergelijking van alle 851 producten/varianten toont alleen inventoryPolicy bij 767 en de afgeleide availableForSale bij 73 als verschil. Voorraadhoeveelheden, tracking, variant- en inventory-item-ID, SKU, product-ID, titel, handle, merk, status, onlineStoreUrl, requiresComponents en pagineringsmetadata zijn exact gelijk gebleven. De 84 al doorverkochte varianten zijn exact gelijk gebleven. Prijzen, media, belasting en verzending stonden niet in de schrijfpayload.

Een tweede reviewer heeft deze tellingen, 767 verse vóórmetingen en alle veertig receipts onafhankelijk uit de bewaarde bestanden gecontroleerd: nul afwijkingen.

## Echte winkelwagencontrole

| Artikel | Handeling | Bewezen resultaat |
| --- | --- | --- |
| Verlavio BC_2009 | Preview verlaten; gewone live In winkelwagen-knop aangeklikt | Eén correcte variant in de winkelwagen, ondanks voorraad nul |
| Cottoceramix RR6001 | 1 m² ingevoerd, berekend als één doos van 1,44 m²; gewone knop aangeklikt | Eén doos/variant in winkelwagen voor €99,29 |

Beide proeven begonnen met een lege winkelwagen. Alleen de eigen proefartikelen zijn na controle verwijderd; de winkelwagen was daarna opnieuw leeg. De Verlavio-pagina is tot slot live herladen en de knop was ingeschakeld.

Dit is een begrensde desktopbrowserproef van twee relevante routes. Geen duizenden individuele winkelwagenacties, fysieke telefoon, checkout of betaling getest. Normale invoerregels zoals positief aantal, doosinhoud en een vereiste productkeuze blijven bestaan.

## Thema en eerdere menurelease

Bij de nieuwe controle is **196341825802 — BadkamerCity - Verlavio keuzemenus 7 nov** inmiddels MAIN. Alle vijf menufiles zijn byte voor byte gelijk aan de eerder gecontroleerde versie. De eerdere conceptrelease staat dus correct gepubliceerd. Deze uitvoering heeft geen thema gepubliceerd of themabestanden geschreven.

De eerdere tegenstelling tussen de tijdelijke tekst Op voorraad en Uitverkocht is opgelost door de expliciet gekozen bestelinstelling. De tijdelijke voorraadtekst is behouden. De eerdere aanbeveling om de voorraadtekst voor de bestelbaarheid te laten prevaleren is vervangen door de actuele eigenaarafspraak: producten mogen doorverkocht worden.

## Herstel en toekomstige imports

Het privébestand **Badkamercity-bestelbaarheid-herstelpakket-2026-11-08.zip** bevat vóór- en nameting, doelplan, mutatiereceipts en herstelgegevens. Herstel zou uitsluitend de policy van daadwerkelijk gewijzigde varianten terugzetten. Lees eerst actuele waarden en vereis dat zij nog overeenkomen met de verwachte nawaarde; geen oude voorraadstanden of volledige exports terugschrijven. Zonder CAS bestaat een klein venster voor gelijktijdige wijzigingen; werk begrensd en lees direct terug.

De [vaste bestelafspraak](../POLICY.md) is de instructie voor nieuwe imports en leveranciersfeeds. Een leveranciersstatus N of onbekend aantal mag niet stil weer DENY veroorzaken. Dit document is geen geïnstalleerde automatische bewaker: er is geen nieuwe achtergrondtaak of feedautomatisering aangezet.

## Technische bron en grenzen

De generieke mutatie is met de officiële Shopify-validator tegen Admin 2026-10 gevalideerd. De connector valideerde iedere uitgevoerde operatie eveneens. Een eerste exportquery kon zijn signed downloadlink niet via de connector teruggeven; die blokkade is niet omzeild. De uitvoering gebruikte vervolgens alleen de relevante 851 producten via gewone gepagineerde queries.

[Shopify: inventoryPolicy CONTINUE/DENY](https://shopify.dev/docs/api/admin-graphql/2026-10/enums/ProductVariantInventoryPolicy) · [Shopify: productVariantsBulkUpdate](https://shopify.dev/docs/api/admin-graphql/2026-10/mutations/productVariantsBulkUpdate).

Volledige catalogus- en voorraadrecords en cartidentifiers zijn niet in publieke Git opgenomen. Er is via connectors gewerkt; bestaande lokale header/main-product/Lagoo-werkbestanden zijn behouden. Geen schone Windows-werkboom geclaimd.
