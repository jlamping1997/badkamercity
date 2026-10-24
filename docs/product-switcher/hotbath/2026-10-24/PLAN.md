# Hotbath keuzemenu’s — werkplan 24 oktober 2026

## Doel en afbakening
Bestaande goede menu’s behouden en uitbreiden. Ook een kleurkeuze telt als een volledig nuttig menu. Iedere keuze leidt naar één werkelijk bestaand, actief en gepubliceerd artikel met zijn bestaande URL, SKU, prijs en winkelwagenvariant. Geen nieuwe producten of combinaties aanmaken. Complete sets, afbouwdelen, inbouwdelen en serviceonderdelen blijven herkenbaar gescheiden.

## Actueel onderzocht
Volledige Shopify-read van 8.237 Hotbath-producten op 24 oktober 2026; Hotbath Catalogus Editie 18 (504 PDF-pagina’s); live V2-engine, centrale menu-JSON en productgroepsvelden. Hoofdthema 195611492618. Actieve codebranch: fix/product-cards-2026-10-14. Geen toegang tot of controle van de Windows-worktree geclaimd.

| Bevinding | Aantal |
|---|---:|
| Bestaande menugroepen | 433 |
| Correct gekoppelde bestaande artikelen | 3.383 |
| Verouderde/ontbrekende handles in die JSON | 0 |
| Artikelen zonder groepskoppeling | 4.854 |
| Daarvan testartikelen | 2 |
| Daarvan SPOM-serviceartikelen | 696 |
| Overige echte artikelen zonder menu | 4.156 |
| Kandidaten voor nieuw of aangevuld menu | 3.445 |
| Met sterk catalogusbewijs (HIGH) | 2.490 |
| Voorstel met nadere controle (REVIEW) | 955 |
| Andere artikelnummerlogica nodig | 577 |
| Geen kleur-sibling gevonden | 134 |

De 739 technische kleur/configuratiebuckets zijn voorstellen over 244 modelcodes; dit is niet het definitieve aantal logische klantfamilies. Een HIGH-label is gecontroleerd catalogusbewijs, geen bewering dat iedere technische eigenschap met het boek is bevestigd.

## Logica van een goed menu
- Toon uitsluitend kenmerken die binnen de familie werkelijk variëren.
- Behoud fabrikantnamen voor kleuren en het onderscheid tussen gewone en PVD-afwerkingen.
- Normaliseer maatweergave en schrijf begrijpelijke keuzenamen, zoals Wandhouder en Glijstang.
- Laat alleen bestaande combinaties kiezen. Nooit een andere samenstelling stil in de plaats zetten.
- Geef per familie een vaste volgorde: kleur, relevante maat/hoogte, montage/uitvoering, aanvullende samenstelling. Bij douchesets kunnen klanttesten een andere volgorde rechtvaardigen.
- Gebruik bestaande vormgeving en engine; vergelijk nieuwe families met bestaande goede voorbeelden.
- Gebruik groepsspecifieke data voor nieuwe pilots, zodat een kleine kleurkeuze niet de volledige centrale dataset hoeft te downloaden.
- Voor groepering zijn model + SKU + titel + relevante bronregels nodig. Alleen een gelijk begin van een artikelnummer is onvoldoende.

## Bestaande groepen aanvullen
Er zijn 64 bestaande groepen met 222 gedetecteerde ongekoppelde sibling-artikelen. Daarvan kunnen 35 groepen / 81 artikelen op sterk catalogusbewijs worden voorbereid. De overige 369 bestaande groepen hebben in deze conservatieve scan geen gedetecteerde kleur-siblingaanvulling; dit bewijst geen universele volledigheid voor alle maten en hoogtes.

## Eerste concrete proef: vier groepen
| Familie | Artikelen | Menu’s | Verandering |
|---|---:|---|---|
| IBS70 | 359 | Kleur, diameter hoofddouche, bevestiging hoofddouche, handdouche, handdouchehouder | Nieuwe koppeling; vijf boekregels |
| BAA03 | 12 | Kleur | Bestaande groep van 8 naar 12; oude acht exact behouden |
| BAA09 | 12 | Kleur | Nieuwe groep wandzeepdispenser |
| BAA10 | 12 | Kleur | Nieuwe groep vrijstaande zeepdispenser |

Samen 395 productpagina’s en 387 nieuwe groepskoppelingen in het concept, zonder productmetafields te wijzigen. Gecontroleerde bronpagina’s: IBS70 gedrukt200/PDF202; BAA03 gedrukt414/PDF416; BAA09/10 gedrukt416/PDF418. IBS70AI4 ontbreekt in Shopify en wordt niet verzonnen. IBS7009 is een aparte familie met tweewegomstel; IBS70 heeft twee stopkranen.

## Batches na de proef
1. **Bestaande kleurmenu’s aanvullen:** eerst de 35 sterke groepen / 81 artikelen. Daarna de overige gedetecteerde aanvullingen controleren.
2. **Nieuwe eenvoudige kleurmenu’s:** families met identiek model en uitvoering; boek/titel/kleurcodes controleren, minimaal twee bestaande kleuren.
3. **Kranen met maat en hoogte:** onderbouwde hoogte- en uitloopfamilies; CB003 blijft het referentievoorbeeld. EXT/TEXT en complete/inbouw-/afbouwartikelen niet ongemerkt samenvoegen.
4. **Overige douchesets:** IBS7009, IBS20/20A, Buddy en andere families volgens hun eigen boekregels. IBS12 begint bijvoorbeeld al met een ronde handdouche; optie1 betekent daar iets anders dan bij IBS70.
5. **Bijzondere modelcodes en uitzonderingen:** 577 artikelen met andere SKU-logica, afwijkende finishes, spiegels/rails en echte bronconflicten. SPOM-serviceonderdelen zijn een afzonderlijke werkstroom.

Iedere batch omvat enkele volledige, verwante families. Eerst automatisch controleren, dan gericht zichtbaar testen. Geen willekeurige onderbreking halverwege een familie.

## Acceptatie per batch
- Elk opgenomen artikel is ACTIVE en gepubliceerd; testartikelen uitgesloten.
- Iedere keuzetuple heeft exact één handle; geen dubbele of ontbrekende keuzevelden.
- Bestaande records en gebruikerskeuzes blijven behouden.
- Titel en artikelnummer spreken de gekozen kleur/maat/samenstelling niet tegen.
- Niet-bestaande combinaties kunnen niet worden geselecteerd.
- Browsercontrole op representatieve bestaande en nieuwe kleuren: juiste producttitel, SKU, prijs, afbeelding en winkelwagenvariant.
- Mobiele werking en scrollpositie afzonderlijk beoordelen; geen mobiele of performanceclaim uit alleen een desktoptest.
- Alleen conceptbestanden aanpassen, actuele themarollen teruglezen en een concrete terugzetroute bewaren.

## Huidige uitvoeringsstatus
UNPUBLISHED concept **195649929482 — BadkamerCity - Hotbath keuzemenus 24 okt** is een voor wijziging bewezen identieke kopie (514/514) van het laatste Sunshower-concept 195611197706. Daarmee zijn de bestaande conceptcorrecties behouden. MAIN195611492618 is niet gewijzigd. Zeven scoped files geplaatst; de bestaande V2-JS en globale 433-groepen-dataset zijn niet gewijzigd. Admin-checksums 7/7 overeenkomend; zes tekstreadbacks exact, groot IBS70-asset via de Admin-checksum gecontroleerd.

Lokale keuze- en regressietests: 11/11 PASS. Catalogusanalysecontroles: 7/7 PASS. Onafhankelijke review: twaalf representatieve gevallen en alle sterke aanvullingen op bestaande groepen, geen dubbele tuples. Liquid-validatie: geen errors; main-product heeft dezelfde drie typen oude waarschuwingen als de bron (complexiteit208→214, ongebruikte seo_media en bestaand continue-object). Browseracceptatie is bij dit checkpoint nog lopend; fysieke telefoon en performance nog niet bewezen. Scrollbehoud is nog niet in de bestaande engine ingebouwd.

## Bekende uitzonderingen
SDS32BGP en IBS33BGP4 noemen messing PVD in de huidige titel terwijl BGP gunmetal betekent. Deze voorstellen blijven REVIEW; niets automatisch gecorrigeerd. De 2.940 afwijkende titelstrings in oude menu-JSON zijn niet automatisch defecte menu’s: handles en keuzecombinaties zijn consistent.

## Terugzetten en vervolgstap
De volledige bronbestanden, manifests en gereproduceerde proefdata zijn als taakdossier bewaard. Terugzetten van de twee bestaande gewijzigde files herstelt de vorige renderroute; nieuwe, dan niet meer aangeroepen assets/helper zijn inert. De oude bestaande Sunshower-draft en MAIN zijn behouden. Publicatie is een afzonderlijke eigenaarshandeling volgens AGENTS.md.

**Eerstvolgende handeling:** de vier proefgroepen in de echte conceptbrowser controleren, bevindingen oplossen en het checkpoint bijwerken. Daarna volgens dezelfde regels de 35 sterke bestaande aanvullingen voorbereiden.
