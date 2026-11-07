# COTTO-04 — controle van de live tegelkeuzes

5 november 2026. Status: REVIEW_COMPLETE / VERIFIED_BROWSER / NO_STORE_WRITES.

De eigenaar vroeg een tweede controle van enkele keuzemenu's en een praktische beoordeling. De bestaande werking blijft behouden: deze ronde wijzigt geen producten, prijzen, voorraad, thema of publicatie.

## Bron en omvang

MAIN is bij begin en einde196238639370, met846 actieve Cottoceramix-producten. Vier relevante buybox/core/CSS/Liquid-bestanden zijn bytegelijk aan de lokale bron op de vaste codebranch `fix/product-cards-2026-10-14`, onder `shopify/current/`.

Echte Chrome-interacties op de publieke webshop, viewport1363×936, met26 vastgelegde toestanden over zeven series. Los daarvan controleerde een tweede reviewer de echte selectiekern op824 nieuw gepubliceerde producten en126 families:11.314 keuzeovergangen. Dat laatste is offline runtimecontrole tegen de eerdere volledige Admin-readback; geen browsercontrole van de gehele catalogus.

## Live uitgevoerde scenario's

| Serie | Uitgevoerde wissel | Bevestigd resultaat |
| --- | --- | --- |
| Funky | Seaport→Garden→duurdere Ametyst, uitklappen |4,1m²+10% blijft;6dozen; totaal verandert van€528,96 naar€554,16. |
| Re-Bel | Blanc60→100cm; Petrol;3handmatige dozen→60cm; browser Terug | Kleur/formaat blijven passend; m²-modus bewaart7,3+10%. Na handmatige dozeninvoer blijven3dozen behouden en verandert geleverde oppervlakte mee. |
| Croccante | Menta60→80cm | Menta blijft;7,3+10% blijft; doos1,44→1,28m²; dikte9→10mm; totaal€509,34→€671,58. |
| Zelij |24kleuren uitklappen; Amarillo10×10→5×20; laatste kleur Via Lactea; inklappen | Juiste SKU/foto/prijs;2,1+10% blijft; gekozen laatste kleur blijft bij de vier zichtbare kleuren. Niet alle24kleuren afzonderlijk aangeklikt. |
| Magnetism | Blue rechthoek6,3×25→Hexa13,9×16 | Blue blijft; bestemmingAM1605 met juiste zeshoekfoto en0,418m²/doos. |
| Lula | Aqua5×25→5×50 | Aqua en2,1+10% blijven;4dozen; doosprijs€35,37→€41,37 en totaal€141,48→€165,48. |
| Marea Alta Mat | Bianco Matt→Blu Matt | Blijft modelAlta, mat en13mm; juiste foto/SKU. Bassa/glans verschijnen niet onbedoeld als kleur. |

Voor alle26 toestanden zijn UI-totaal = doosprijs × aantal dozen en de benodigde naar boven afgeronde dooshoeveelheid onafhankelijk nagerekend:26/26 PASS. Geen horizontale desktopoverloop in de vastgelegde toestanden. Direct na sommige navigaties was de hoofdfoto nog aan het laden; na laden is voor alle zeven series een passende bestemmingsfoto bevestigd. Dit is niet als ontbrekende afbeelding gerapporteerd.

## Beoordeling en verbeteringen

De huidige vierkante fotokeuze, geselecteerde kleur, uitklappen en calculator werken goed in de steekproef. Geen reden voor een structurele herbouw gevonden.

1. **Vormnamen zichtbaar maken.** Magnetism toont nu de afmetingen om rechthoek versus zeshoek te kiezen. “Rechthoek6,3×25” en “Hexagon13,9×16” zouden duidelijker zijn. Cottage kent dezelfde ontwerpvraag. De huidige knop kiest wel het correcte artikel.
2. **Uitvoeringen beter vindbaar maken.** Model-/afwerkingsfamilies zoals Marea Alta/Bassa en mat/glans zijn bewust apart gehouden. Een aparte model-/uitvoeringkeuze of duidelijke verwante links zou de ontdekbaarheid verbeteren. Kleurgroepen niet blind samenvoegen.
3. **Kleurnamen opschonen.** Croccante toont leverancierlabels “Araandano” en “Avelle”, terwijl de producttitels “Arandano” en “Avellana” bevatten. Eerst een expliciete mapping bevestigen en daarna broncorrectie toepassen.

Deze punten zijn voorstellen, niet uitgevoerd. De bron-/kerncontrole vond geen ongewenste andere technische verandering bij alleen kleurwisselen. Er zijn40 verwachte formaat→dikte-koppelingen. Geen huidige botsende of onjuist nominaal hernoemde formaatopties gevonden.

Native m²-prijzen kunnen door rekenen vanuit een afgeronde doosprijs één cent van de adviesprijs verschillen. Dat is ook live gezien bij Zelij en Marea. Maximaal één cent over359 van824 gepubliceerde nieuwe producten; geen verkeerde doosheffing en geen prijswijziging voorgesteld.

## Technische parkeerplaats

Een onafhankelijke happy-dom-verwijdertest van de werkelijke componentklasse bevestigt een laag geprioriteerde lifecycle-kwestie: twee `disconnectedCallback`-definities in `bc-porcelanosa-buybox.js`; de latere overschrijft dialoogopruiming. Bij verwijderen met geopende hulpdialoog kan body-scroll geblokkeerd blijven. Normale live productwissels navigeren naar een nieuwe pagina; in de geteste klantflow geen dergelijke fout gereproduceerd. Pas gericht samenvoegen in een UNPUBLISHED preview wanneer deze lifecycle-route wordt aangepakt.

Toekomstige import: de bestaande Porcelanosa-maatnormalisatie raakt geen huidige Cottoceramix-keuzes, maar zou59,5cm vanKB5951 enKV5901–KV5907 naar60cm omzetten. Voor die toekomstige artikelen expliciete exacte-versus-nominale maatkeuze vastleggen.

## Grenzen en overdracht

Deze ronde geen fysieke telefoon, volledige mobiele PDP, nieuwe cartactie, verzending, checkout, betaling, zoekindex of livefeedsynchronisatie getest. Eerdere COTTO-02/03-bewijzen blijven afzonderlijk gedateerd. Geen volledige catalogusvrijgave op basis van deze steekproef.

Alleen dit dossier en de eigen COTTO-04-statusparagraaf opgeslagen. Bronexports, ruwe traces en screenshots niet in de openbare repository. [Beperkte openbare verificatie](verification.json). Bestaande COTTO-03-volgende stap blijft de aparte stuks-/m¹-route voor onder meer Casablanca en Enso. Geen actieve COTTO-04-schrijver na overdracht.
