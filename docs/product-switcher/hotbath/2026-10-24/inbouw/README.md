# Hotbath inbouwdeel meebestellen — gecontroleerd voorstel, 24 oktober 2026

> **Uitbreiding24okt:**94 extra modellen/460 extra artikelen gecontroleerd; uitzonderingen en bronpagina’s staan in [EXPANSION.md](EXPANSION.md). Nog geen Ja/Nee-functie geïnstalleerd. Hieronder blijft de eerste proef beschreven.

Status: **MAPPING_VERIFIED / PILOT_NOT_IMPLEMENTED**. Dit dossier beantwoordt hoe we de afbouw-/inbouwrelatie betrouwbaar vaststellen en legt de eerste concrete koppelingen vast. De Ja/Nee-optie en gecombineerde winkelmandactie zijn nog niet gebouwd of getest. Er is in deze ronde geen Shopify-product-, prijs-, voorraad-, metafield- of themamutatie uitgevoerd.

## Gecontroleerde eerste proef

| Afbouwmodel | Inbouwdeel | Gedrukte boekpagina | Verse afbouwartikelen |
| --- | --- | --- | ---: |
| CB105EXT18 | HBCB105 | 170 | 10 |
| CB105EXT25 | HBCB105 | 170 | 10 |
| CB105TEXT18 | HBCB105T | 171 | 10 |
| CB105TEXT25 | HBCB105T | 171 | 10 |

Alle 40 artikelen zijn actief en Online Store-gepubliceerd, hebben één exact gevonden SKU/variant en `specs.met_inbouwdeel=false`. Beide doelartikelen zijn uniek, gepubliceerd en beschikbaar voor verkoop. HBCB105 is variant53187364356362, met bij deze read een Shopify-prijs van €174,00; HBCB105T is een afzonderlijk ander inbouwdeel. Een verkoopbaarheidswaarde is geen fysieke voorraad- of levertijdbelofte.

[cb105-pilot-mapping.json](cb105-pilot-mapping.json) bevat de 40 exacte afbouwvariant→inbouwvariant-relaties met hoeveelheid1 en bronpagina. Prijzen staan bewust niet vast in deze mapping: die worden bij gebruik uit het echte Shopify-artikel gelezen. De generator weigert ontbrekende/duplicaat-SKU's, meerdere varianten, ongepubliceerde producten, onbekende leveringsinhoud, bestaande onduidelijke componentdata en afwijkende boekkoppelingen. De uitvoer is een voorstel, geen geactiveerde import.

## Zo stellen we de relatie vast

1. Vind kandidaten via artikelcodes, afbouw-/afdektitels en bestaande productkenmerken. EXT is een zoeksignaal; de juiste bodycode wordt nooit uit een prefix afgeleid.
2. Lees per basismodel de expliciete inbouwdeel-/afbouwdeeltabel of onderdelenlijst in Hotbath Editie18. Bewaar beide exacte codes, hoeveelheid, editie en gedrukte/PDF-pagina.
3. Bepaal de leveringsinhoud: afbouwdeel zonder body, complete set met body, losse body, inbegrepen in de prijs maar apart te bestellen, of onbekend.
4. Breid alleen een bewezen modelregel uit over de in die familie onderbouwde kleuren en lengtes.
5. Koppel iedere concrete afbouw-SKU aan precies één bestaand Shopify-doelartikel en de huidige verkoopbare variant. Geen passend bewijs of ontbrekend doelartikel betekent geen automatische betaalde toevoeging.

De begrensde boekreview heeft 31 expliciete modelkoppelingen gevonden, overeenkomend met208 producten in de eerder vandaag uitgelezen catalogus. Vijf MHF-modellen zijn expliciete naamaliassen en blijven voor implementatie in review. Dat is geen volledige Hotbath-dekkingsclaim. De 40 CB105/CB105T-proefartikelen en beide bodies zijn daarnaast opnieuw rechtstreeks uit Shopify gelezen.

## Belangrijke uitzonderingen

- AR009EXT hoort bij **MB009**, CB009EXT bij **HB009** en CB006TEXT18/25 bij **HBCB005T**. Een automatische HB-prefixregel is dus foutgevoelig.
- MHF-afdeksets hebben in de huidige Shopify-SKU niet altijd EXT. Alleen op EXT filteren mist die kandidaten.
- IBS70 en andere bewezen complete IBS-sets bevatten de body al. Toon eventueel “Inbouwdeel inbegrepen”; geen tweede betaalde body.
- Bij RARH50-1 staat in het boek dat MBASES2 in de setprijs zit maar apart moet worden besteld. Bestaande producttitels/aanbieding en leveringsafhandeling moeten eerst worden afgestemd; geen extra prijs automatisch toevoegen.
- KHDS5EXT verwijst in het boek naar HBKHDS4, dat in de gebruikte catalogussnapshot ontbreekt. Geen vervangend inbouwdeel raden.
- De huidige `bc_data.set_components`-status `EXACT_TARGET_UNVERIFIED_COMPATIBILITY` bewijst een gevonden artikel, niet zelfstandig technische passendheid.

## Gewenste koopervaring

In de gewone koopsectie komt een expliciete keuze:

- **Ja, HBCB105 toevoegen (+ actuele artikelprijs)**
- **Nee, ik heb het passende inbouwdeel al**

Bij Ja voegt de gewone winkelwagenknop het gekozen afbouwartikel én het gekoppelde inbouwdeel toe als echte artikelen. Bij aantal2 en een1:1-relatie worden twee afbouwdelen en twee bodies toegevoegd. Een al aanwezige body in de winkelmand mag niet automatisch worden overgeslagen; die kan bij een andere kraan horen.

De Ja/Nee-keuze blijft bij een kleur-/uitloopwissel alleen bewaard zolang de nieuwe pagina tot dezelfde gecontroleerde relatie behoort en dezelfde body nodig heeft. Bij een andere body opnieuw laten kiezen. Als een body niet bestelbaar is: Ja niet als bestelbare keuze aanbieden en niet stil veranderen in Nee.

De actuele accessoirescode bevat bruikbare SKU-/variantcontrole, prijsophaling en beschikbaarheidscontrole. De huidige accessoireknop voegt echter alleen accessoires toe. Alleen die tabel vullen is daarom onvoldoende; de normale koopactie moet deze relatie gebruiken. Sunshower-doorverwijzingen en wishlist blijven behouden. Technische details en officiële documentatie staan in [cart-architecture-review.md](cart-architecture-review.md).

## Acceptatie bij de bouw

Test Ja/Nee, aantal2, kleur-/lengtewissel, reeds aanwezige body, complete IBS-set, ontbrekende of onbeschikbare body, verkeerd product, dubbel klikken, netwerkfout en gedeeltelijke winkelmandrespons. Eén meervoudig verzoek is niet vanzelf alles-of-niets; geen blinde retry. Controleer de drawer/notification, snelle checkout en echte mobiele koopflow. Alleen eigen testregels opruimen.

## Actuele publicatie en overdracht

De eigenaar heeft het eerder gemaakte keuzemenuthema gepubliceerd. Verse Shopify-read: **MAIN195649929482**, BadkamerCity - Hotbath keuzemenus24okt; alle532 bestanden exact identiek aan de eerder gecontroleerde preview. Vorig MAIN195611492618 is nu UNPUBLISHED. De agent heeft niet gepubliceerd. Zie [publication-verification.json](publication-verification.json).

Actieve codebranch: `fix/product-cards-2026-10-14`. Dit dossier is een scoped voorstel/bewijs onder docs; geen root-theme-push en geen Windows-worktreecontrole. Er is geen lokale Git-checkout in deze scratchwerkmap.

**Exact volgende handeling:** bouw de bovenstaande40 relaties als proef in een nieuw, bewezen identiek UNPUBLISHED-concept van het huidige MAIN, met één gecombineerde koopknop en de genoemde tests. Pas daarna dezelfde bewezen werkwijze uitbreiden; vijf naamaliassen en commerciële uitzonderingen afzonderlijk beoordelen.

