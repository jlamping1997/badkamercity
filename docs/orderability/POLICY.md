# Bestelbaarheid van winkelproducten

## Eigenaarafspraak — 8 november 2026

Alle bestaande producten die in de webshop worden aangeboden moeten besteld kunnen worden, ook wanneer Shopify nul voorraad toont. Deze expliciete afspraak gaat vóór eerdere voorraadgestuurde blokkering of eerdere adviezen om niet-beschikbare artikelen automatisch uit te verkopen.

Voor gepubliceerde ACTIVE en UNLISTED producten geldt:

- Bij voorraadtracking aan: gebruik inventoryPolicy=CONTINUE.
- Bij voorraadtracking uit: voorraad beperkt bestellen al niet. Zet tracking niet uitsluitend voor deze afspraak aan of uit.
- Behoud echte voorraadstanden. Een leveranciersstatus N of een onbekend aantal verandert de toestemming om door te verkopen niet.
- Houd bestelbaarheid en leveranciersinformatie als afzonderlijke gegevens bij. Verzin geen fysieke voorraad of leverdatum.
- Behoud gewone product-, keuze- en aantalsvalidatie.

Deze afspraak publiceert geen DRAFT- of ARCHIVED-producten en herstelt geen verwijderde artikelen. Bestaande import-, media- en productvrijgavevoorwaarden blijven van kracht.

## Imports en feeds

Pas deze bestelregel toe zodra een goedgekeurd product voor de webshop wordt voorbereid. Een import of voorraadfeed mag de verkoopinstelling niet ongemerkt naar DENY terugzetten vanwege nulvoorraad of leveranciersstatus N. Vermeld een expliciete eigenaaruitzondering als een artikel toch geblokkeerd moet worden.

Dit is de vastgelegde werkwijze. Er is geen terugkerende controle of nieuwe automatische synchronisatie geïnstalleerd. Controleer bij een toekomstige import de daadwerkelijke schrijfpayload en een representatieve winkelwagenactie.

## Uitvoering en bewijs

[Winkelbrede toepassing en controle van 8 november 2026](2026-11-08/README.md): 767 policies aangepast, 73 bestaande blokkades opgeheven en alle 851 voorraadgevolgde varianten teruggelezen. De 15.070 niet-gevolgde gepubliceerde producten waren qua voorraad al onbeperkt bestelbaar.
