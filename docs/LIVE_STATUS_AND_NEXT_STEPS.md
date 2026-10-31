# BadkamerCity — actuele werkstatus

**31 oktober 2026 · NAV-03 / TILE-02 PREVIEW_VERIFIED / OWNER_REVIEW_PENDING.** Compact menu, startwaarde1m² en tegelinformatie staan in het gecontroleerde concept. Geen actieve schrijver na overdracht.

## Begin hier: actuele rollen en code

- **MAIN195974824202 — BadkamerCity - Betrouwbaar bestellen en filters.** De eigenaar heeft de herstelde FIX-01 gepubliceerd. Verse eindmeting:1.355bestanden, nul gewijzigde paden tegenover opening van deze taak. Geen MAIN-filewrite of publicatie door deze uitvoering.
- **UNPUBLISHED195947036938 — BadkamerCity - Compact menu en tegelinformatie.** Eerst alle21FIX-01-paden vanuit MAIN overgenomen; vóór nieuwe features1355/1355checksumpariteit. Finaal1.356bestanden, exactzesgewijzigdebestaandepaden +éénnieuweoverflow-snippet. Alle zeven checksums correct teruggelezen. QA-template exact hersteld.
- Repository **jlamping1997/badkamercity**, bestaande branch **fix/product-cards-2026-10-14**. Runtimecheckpoint **b7a5308038965bf874e06ed5115aa9431eb381d3**. Alleen de zeven expliciete featurepaden uploaden; Git-root is geen volledige actuele MAIN-snapshot. Main ontvangt dezelfde overdracht/testdocumentatie, geen themacode.

[Actuele wijziging, bewijs en rollback](navigation-and-tiles/2026-10-31/README.md) · [einddiff](navigation-and-tiles/2026-10-31/final-verification.json).

## Nieuwe werking

| Onderdeel | Gedrag in het concept |
| --- | --- |
| Desktop/laptopcategorieën | Eén rij; werkelijk passende categorieën direct zichtbaar. Rest met volledige sublinks onder Meer categorieën. Geen horizontaal schuiven of tweede rij. |
| Tablet/telefoon | Onder990CSS-px bestaand menu. Brede tablet/laptop kan de passende enkele rij gebruiken; apparaatnaam is geen vaste layoutkeuze. |
| Zonder scripts | Native Alle categorieën-details met bestaande bestemmingen. |
| Tegelcalculator | Verse start1m², 10% snijverlies behouden; opgeslagen expliciete keuzes en handmatige dozen blijven werken. Ongeldige invoer blijft blokkeren. |
| Informatieknop | Native popup naast Bereken je bestelling met vloer-/wanduitleg, Sluiten/Escape/focusterugkeer; NL/EN. |

## Verificatie en grenzen

**Dertien CSS-breedtes 320–1920px:** geen document- of categorierail-overloop; vanaf990px één48pxrij. In de gebruikte fixtures990/1024:7direct+4Meer;1180/1280:9+2;1366enbreder11direct. Deze aantallen zijn meetresultaten, geen vaste limieten. Meer opent binnen viewport, ArrowDown/Escape/focus getest. Tablet820:Menu→Douche→Terug→Escape. Open mobiel menu sluit bij resize naar1366zonderbodylock.

**Tien lokale regressies PASS**, Theme Checkrevisie3 allezevenfiles geldig. Echte tegel-PDP begint1m²/10%;10m²→8dozen/11,44m²;0m² geeft fout/geblokkeerd/geen oud totaal. Native informatiepopup en Escape/focus/body-scroll gecontroleerd. Echte concept-homepage visueel bekeken. Tijdelijke QA-template exact teruggezet.

Dit is Cloud Chrome en componentframes met echte conceptcode, geen fysieke telefoon/tablet/Windows-, touch-hardware-, volledige checkout-, mailbox-, ranking- of performancevrijgave. Geen echte cart-, order- of formulieractie. Settings_data/retourtemplate-bodyuitzonderingen behouden; beide niet geüpload.

## Exact één volgende handeling

**Eigenaar opent bij Webshop→Thema’s het Voorbeeld van BadkamerCity - Compact menu en tegelinformatie, controleert eigen laptop/tablet/telefoon en publiceert daarna zelf.** Geen publicatie door uitvoerder.

## Bestaande reparaties en open taken behouden

FIX-01 is nu LIVE door eigenaarspublicatie: cartbevestiging, Sunshower pending/onzekere add, definitieve native filterterugval, Toon minder, zoektelling, tegelprijseenheden, wishlist-intents en echte footerlinks/SEO. De eerdere lege calculatorstart is door de nieuwe expliciete opdracht vervangen door1m². [Oorspronkelijke FIX-01](repairs/2026-10-31/README.md) · [herstel verwijderd concept](repairs/2026-10-31/recovery/README.md).

- **Retouraanmelding:** bestaande live Page166668894474, handmatige native contactaanvraag. Mailontvangst/spam/antwoord en labellevering nog onbewezen; geen automatisch RMA/label/refund gebouwd. [Publicatie](returns/2026-10-30/PUBLICATION.md).
- **Offerte:** deze taak wijzigt geen activatie of account/verificatie. Het bestaande verificatie-/ontvangst-/opslag-/verwijderbewijs blijft open; geen privéaccountpoging. [Integratie](quote/2026-10-30/INTEGRATION.md).
- **Hygrometer:** eerdere twee redirects naar bestaande /pages/hygro-meter behouden; in deze taak niet opnieuw alle redirects getest.
- **Filters/wishlist:** eerdere grenzen voor omgekeerd bereik/APIbeleid, URLdialecten, responseidentity, facetzoeker, oudere/no-Locks-tabversies, opgeslagen corrupte/dubbele arrays en productread-timeout/TTL blijven open. Niet als nieuwe productie-incidenten opgevoerd.
- **QC-04:** afzonderlijke privétool op quality-control; geen privébeoordelingen gelezen of Shopify-productmutatie uitgevoerd.

[Het naslagwerk](MASTER_SITE_REFERENCE.md) blijft het gedateerde DOC-04-boek met80hoofdstukken. Oude NAV-02-rijen/publicatierollen zijn historisch en vervangen door deze actuele status en NAV-03. De registers behouden hun eigen peildatum. Geen Windows-controle geclaimd.
