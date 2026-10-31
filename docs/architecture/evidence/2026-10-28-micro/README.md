# Bewijs — microanalyse 28 oktober 2026

Begin bij de [microdossiers](../../components/micro/README.md). Deze ronde gebruikt vers gelezen code en afzonderlijke functie-/staatreplays. Baseline actieve branch: a5e3c9e0bb8a8cfb7b5aa7715a5019a54c877d7b; main bij aanvang: 28741ddb1dd4f777c31565da47d2c1de26345a16. Verse Admin-read bevestigt opnieuw MAIN 195818389770, updatedAt 2026-10-28T01:37:04Z. Geen publicatie uitgevoerd.

| Bestand | Bewijs / grens |
| --- | --- |
| source-provenance.json | 22 gerichte textbestanden opnieuw opgehaald; alle MD5/groottes passen; vergelijking met eerdere index waar beschikbaar |
| isolated-results.json | 15 gevallen op vier hashgecontroleerde JS-bronnen; 10 controles, 3 defectreproducties voor 2 problemen, 2 grenzen |
| catalog-validation.json | 72 Sunshower-configuraties structureel uniek; geen nieuw Shopify-/leveranciersprijsbewijs |
| browser-observations.json | Drie desktopwaarnemingen in bestaande sessie: externe kaart-CTA, Maathulp/Escape/focus en galerijstap |

**Niet opnieuw het hele thema gescand.** De conclusie geldt voor de 22 gelezen bestanden en de benoemde replaybronnen. De eerdere volledige 1.262-bestandenkaart blijft een gedateerd bewijs met een open settings_data.json-uitzondering. Geen nieuwe bytevrijgave van die settingsfile.

## Wat een replay hier bewijst

De tests draaien de echte ontvangen JS in happy-dom 21.0.4 op Node 24.22.1. Alle fetches en navigaties zijn harde lokale stubs; native dialogmethoden, observers, animatieframes en timers worden waar nodig beheerst nagebootst. Producten, ID's en bedragen in de fixture zijn synthetisch. V2 private helpers worden alleen in de sandboxcopy zichtbaar gemaakt; de functies zelf blijven gelijk.

CONTROL_PASSED betekent dat de beschreven bescherming bij de genoemde stimulus werkte. DEFECT_REPRODUCED betekent dat de fout onder de benoemde stimulus optreedt; niet dat diezelfde serverresponse of dubbele koopactie live is waargenomen. BOUNDARY_CONFIRMED beschrijft een grens, geen automatische bug. Het testrapport is dus geen algemene PASS van de winkel of een frequentiemeting.

De twee nieuwe problemen zijn **CART-F01** (oude productinhoud bij ontbrekende/null section) en **SS-F01** (productnavigatie tijdens een pending set-add). Ze zijn geanalyseerd en niet gerepareerd in productie.

## Browsergrens

De browser had een bestaande sessie met preview-UI. Geen claim van een nieuwe anonieme sessie en geen cartinhoud opgenomen. Er zijn uitsluitend kaart-/hulp-/galerijwaarnemingen gedaan; geen add/change/clear/checkout. Viewport 1363×936. De beschikbare browserinterface exposeerde geen viewportresize; mobiel blijft NOT_TESTED. De replay-DOM op 390px is geen mobiele browser of fysieke telefoon. Er zijn geen screenshots als deliverable opgeslagen.

## Opnieuw uitvoeren

De harness staat op de actieve branch onder scripts/component-audit; main bevat alleen documentatie/bewijs. Lees [de uitvoerinstructie](https://github.com/jlamping1997/badkamercity/blob/fix/product-cards-2026-10-14/scripts/component-audit/README.md). Gebruik een expliciete bronmap en dit SHA-256-register; afwijkende code wordt geweigerd. De tests halen zelf geen Shopify-bron op en mogen geen echte cartrequest uitvoeren.
