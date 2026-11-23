# Welke producten sturen we naar Google?

In gewone taal: we laten Google eerst de producten zien waarvan de advertentiegegevens betrouwbaar zijn. Je hoeft hiervoor niet duizenden producten één voor één met de hand na te lopen.

De webshop kan meer producten bevatten dan de Google-productfeed. Een product tijdelijk buiten die feed houden verwijdert het niet uit de webshop en betekent geen algemene noindex. Een ontbrekende commerciële foto is wel een probleem voor productvermeldingen.

## Zo verdelen we het werk

1. Uitvoering leest bestaande Shopify-data en maakt een automatische eerste controle op foto, prijs, identifiers, beschikbaarheid, publicatie en link.
2. Alleen twijfelgevallen of ontbrekende leveranciersinformatie komen op een korte uitzonderingslijst.
3. Jackson beoordeelt wat alleen zakelijk te bevestigen is: juiste foto, echte leverafspraak, inhoud van de set of afwijkende uitvoering.
4. We toetsen eerst circa tien verschillende artikelen in de echte Google-koppeling. Daarna kunnen geschikte batches verder; de rest wacht op aanvulling.
5. Merchant-goedkeuring en echte vertoningen worden pas afgevinkt als ze in Google zijn teruggelezen.

Dit dossier maakt nog geen tags, kanaalpublicaties, noindex-regels of automatische datastroom aan. De exacte selectie wordt gekozen nadat het Google-kanaal en bestaande publicaties zijn geïnspecteerd.

| Situatie | Aanpak |
| --- | --- |
| Juiste echte foto, betrouwbare prijs en leverstatus, juiste artikelidentiteit | Kandidaat voor Google; ontvangen feed en bestemming controleren |
| Foto ontbreekt/verkeerd of alleen een placeholder/logo | Eerst beeldbron oplossen; voorlopig niet in Google-productvermeldingen |
| GTIN/EAN door fabrikant toegekend maar ontbreekt | Juiste identifier ophalen; geen verzonnen nummer of standaard identifier_exists=false |
| Onzeker over prijs, inhoud of echte bestelbaarheid | In onderzoek; geen onjuiste InStock-/setclaim |
| Tijdelijk uitverkocht met correcte informatie | Beschikbaarheid eerlijk doorgeven; niet automatisch product verwijderen |
| Werkelijk individueel maatwerk | Retouruitzondering en productinformatie vooraf onderbouwen |
| Gegevens correct maar Google keurt af | Precieze fout lezen en de primaire bron gericht herstellen |

## Verlavio, intern Fabriecio

Het publieke merk is inmiddels Verlavio. Fabriecio blijft de leverancier-/importnaam en bestaande fabriecio-handles blijven intact. De eerdere koopbaarheidsafwijking is in FAB-04 gericht hersteld; dat werk niet opnieuw beginnen.

Voor de huidige vraag over ontbrekende foto's: splits de groep op **met juiste foto**, **foto ontbreekt**, **foto verkeerd of model/kleur onzeker**. Alleen de eerste groep is een beeldkandidaat voor Google; bij de rest eerst de eigen fabrikantbron/feed en exacte SKU controleren.

Geen galerij van een ander model/kleur als oplossing gebruiken. De ontbrekende beelden hoeven niet alle andere producten op te houden. De oude nulmeting waarin GM_1002 OutOfStock stond blijft historische bewijsdata, geen nieuwe conclusie over de hele huidige Verlavio-catalogus.

## Lagoo en tegels

Lagoo blijft zonder productfoto's volgens de eigenaar. Nu geen beeldloos Lagoo in de Google-productbestemming en geen foto's terugplaatsen om een Google-fout weg te krijgen.

Bij tegels blijft de m²-prijs duidelijk op de website en staat de doosprijs bij de calculator. De feed moet de daadwerkelijk bestelbare doos en toepasselijke eenheidsprijsvelden correct beschrijven; prijs-/m²-presentatie op de site niet zomaar ombouwen.

## Wat jij nu hoeft te doen

Ga door met de leveranciers-/fotocorrecties. Je hoeft niet zelf Google-publicaties per product te gaan regelen. Wij maken eerst de technische controle en leggen alleen de echte uitzonderingen aan je voor.

[Merchant-stappen](google/MERCHANT_CENTER.md) · [Google-bronnen](BRONNEN.md) · [Taken](TAKEN.md)
