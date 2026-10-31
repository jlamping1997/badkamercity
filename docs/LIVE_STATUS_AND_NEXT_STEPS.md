# BadkamerCity — actuele werkstatus

**31 oktober 2026 · FIX-01 PREVIEW_VERIFIED / OWNER_REVIEW_PENDING.** Reparaties staan in het gecontroleerde concept; geen actieve schrijver na overdracht. Eigenaar publiceert volgens AGENTS.

## Huidige winkel en concept

- **MAIN195947036938 — BadkamerCity - Categorieen zonder schuiven**, door eigenaar gepubliceerd vóór deze uitvoering. Eindmeting:1.354paden, nul wijzigingen tegenover opening08:57:37Z. NAV-02 is dus LIVE.
- **UNPUBLISHED195948839178 — BadkamerCity - Betrouwbaar bestellen en filters**:1.355paden, exact20gewijzigde bestaande bestanden +één nieuwe tegelprijssnippet. Actuele MAIN-header behouden; tijdelijke QA-template exact hersteld. Geen MAIN-filewrite of themapublicatie door uitvoerder.
- **Hygrometer live gerepareerd:** bestaande pagina `/pages/hygro-meter` hergebruikt; beide oude routes leiden nu HTTP200 naar juiste H1/canonical. Twee redirectobjecten exact teruggelezen. Geen dubbele Page gemaakt.
- **Retourpagina blijft live**, Page166668894474. Native contactformulier, handmatige behandeling. **MAIL_DELIVERY_PENDING** blijft open; geen automatisch label/refund/RMA of bewezen klantbevestigingsmail.
- **Offerte CUSTOMER_ACTIVATION_DISABLED** behouden. Eigenaar moet bestaande verificatie/ontvangst en opslag/privacycontroles voltooien. Geen nieuwe privéaccountpoging.

## Uitgevoerde reparaties

[Volledig herstel-, test- en rollbackdossier](repairs/2026-10-31/README.md) · [einddiff](repairs/2026-10-31/final-theme-delta.json).

| Onderdeel | Resultaat in reviewconcept |
| --- | --- |
| Winkelwagen | Geen oud artikel/teller bij onvolledige sections; generieke cartlink zonder tweede add. |
| Sunshower | Pending en onzekere set-add blokkeren dubbele/wijzigende kooproutes; eerst cart controleren, ook bij mogelijke gedeeltelijke422. |
| Filters | Na native fallback blijft externe controller uit voor huidige pagina; Toon minder respecteert ingestelde limiet. |
| Zoeken | Actieve lijst/telling/titel consistent; native606 → extern337 toont337. Bij fallback native titel terug. Geen indexgelijkmaking. |
| Tegels | Doos-/m²prijs op native/custom/externe cards duidelijk, geen dubbele unitregel. Actieve calculator leeg/neutraal beginnen, bestaande10% behouden, handmatige dozen intact, fouten wissen oud totaal. |
| Wishlist | Actuele identity-intents en native Web Locks waar beschikbaar; geen stil overschrijven corrupte data; nieuwe Sunshowerkaart synchroniseert direct. Geen atomiciteitsgarantie zonder Locks/oudere tabcode. |
| Footer | Alleen echte bestemmingen zichtbaar, merkengids aangesloten; adres blijft verwijderd. |
| Verzendcopy/SEO | Bestaande€100-copy consistent; onbewezen zelfde-dagbelofte weg. Alleen lege collectie-meta krijgt veilige titelgebonden fallback; redactie behouden. |

## Verificatie

**126 lokale gevallen/checks:**18cart/Sunshower +44filters +46wishlist +18presentatie/calculator. Daarin81controle,15regressie,12expliciete grenzen en18presentatiechecks; nul DEFECT_REPRODUCED in nieuwe harnesses. Gehashte echte bronnen, synthetische requests en opslag. Overdraagbare herhaalopdracht en vier expliciete baseline-dependencies in dossier.

Theme Check R4–R7 geldig, vijf bestaande niet-blokkerende waarschuwingen benoemd. Cloud Chrome1348×926: native dialog met fictieve sections, Escape/focusterugkeer; twee same-origin frames bewaren2/2fictieve wishlistkeuzes met echte Locks, testsleutel opgeruimd; echte tegel-PDP leeg/10%/disabled en geldige/ongeldige/handmatige berekeningen. Zoek-URL/controlestand terugnavigatie en footer gecontroleerd. Twee collectie-HTTPreads bewijzen meta-fallback/behoud zonder stylelekkage; Hygrometer3GETs200.

Geen echte cart/order/checkout of nieuwe formulierinzending; mailbox/spam/antwoord/label niet bewezen. Geen fysieke iPhone/Windowscontrole, nieuwe volledige responsive matrix, privé-VPS/indexmutatie, rankings of performanceclaim. Settings_data-body/hashuitzondering blijft open; bestand niet geüpload. Git-root blijft een gerichte werkbranch, geen complete huidige MAIN-snapshot.

## Exact één volgende handeling

**Jackson beoordeelt UNPUBLISHED195948839178 en doet de herkenbare fictieve retouraanvraag met controle van ontvangst/spam/antwoord in de eigen mailbox.** Code is reviewbaar; publicatie door eigenaar. Offerteactivatie blijft apart uit tot verificatie.

## Open grenzen voor later gericht werk

Omgekeerd prijsbereik/APIbeleid, native/externe URLdialecten, harde response-collectionidentity, eventuele facetwaardezoeker, wishlist-no-Locks/oudere tabs, bestaande dubbele/corrupte arrays en productrequesttimeout/TTL staan expliciet open in het [dossier](repairs/2026-10-31/README.md). Niet afleiden dat elke grens een huidig bezoekersincident is. Geen complete oplossing voor retourlabel-/RMAbeheer gebouwd; bestaand proces is handmatig.

## Documentatie en overdracht

Repository **jlamping1997/badkamercity**, bestaande codebranch **fix/product-cards-2026-10-14**. R1remotecheckpoint267e4b15172b26d1f0867d821c01e64b6eb1a11a; main-docs56ddb239453a801cacecea86c146e97fbf4992f5. Definitieve aanvulling volgt op die checkpoints; GitHubreadback/treeverificatie in uitvoeringsresultaat. Main krijgt uitsluitend dezelfde documentatie, geen themacode. Windows niet onderzocht.

[Het naslagwerk](MASTER_SITE_REFERENCE.md) blijft DOC-04-versie2.0 met80hoofdstukken,50taken,40diagnosepaden en50acceptatiescenario’s, gemeten vóór deze reparaties/publicatie. De nieuwe actuele herstelcontracten staan in FIX-01 en de gedateerde notities boven de componentdossiers; oude defectlogs blijven historisch. [Bronuitbreiding](handbook/2026-10-31/README.md) · [bronmeting vóór FIX](site-reference/2026-10-31/README.md).

[NAV-02](laptop-navigation/2026-10-31/README.md) behoudt eigen twaalf-breedteframes/menu/focusbewijs. [RET-publicatie](returns/2026-10-30/PUBLICATION.md), [offerte-integratie](quote/2026-10-30/INTEGRATION.md), [categorisatiebeleid](CATEGORIZATION_AND_SEO_POLICY.md) en [toekomstprojecten](FUTURE_CONTENT_AND_PRODUCT_PROJECTS.md) blijven van toepassing. QC-04 blijft privé op quality-control, zonder automatische Shopify-mutatie. Oudere bronstanden zijn geschiedenis, geen actuele rollen of afgeronde mailboxproef.
