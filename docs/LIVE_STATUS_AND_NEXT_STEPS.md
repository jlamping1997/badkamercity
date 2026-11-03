# BadkamerCity — actuele werkstatus

## QC-10 — officiële Lagoo-bron en klantdocumenten · 3 november2026

Alle199productpagina's en27mediapagina's gelezen;2.629mediarecords tegenover2.679headercount,50verschil expliciet open. Nieuwe werkset met1.823eigen fabrikantfoto's en372PDF-kopieën READY. Geen3D/CAD-bestandsdownload.254PDF-records in actuele paginalinks; overige alleen kandidaat.48pagina's/314bestaande varianten noemen inbouwdelen met originele voorwaarden/alternatieven.616varianten met expliciete artikel-/kleurcode,612niet beschermd voor importfoto's. Andere kleurkoppelingen blijven onzeker; ook fabrikant hergebruikt seriebeelden.

Dezelfde privé-QC gebruikt nieuwe fabrikantfoto-ID's, duidelijke bronlabels en huidige/kandidaat-PDF's;24LVS1/2/3varianten en alle andere merken exact behouden. Oude400beoordelingen blijven historie, geen automatische goedkeuring van nieuwe bestanden. Checkpoints blijven per SKU. Importv4:1772niet-beschermde varianten,612photoImportReady; alle andere importfoto's leeg/hold. Prijzen/opties/EAN's niet uit groepsclaims overschreven. Geen Shopify-productmutatie/publicatie; uitsluitend eigen bestandskopieën. [Scope en herstel](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_OFFICIAL_SOURCE_2026-11-03.md).

Sites-versie12 succeeded; bron627aafcae4508977066e13e68ef7ab8e1341b2c2, deployment appgdep_6ae9b9ea19488191a5816154ba3b1387. Schone build33MiB, originele brondata privé behouden. TypeScript/build/45bestaande API-SQLite-Lagoo-groepen+8nieuwe fabrikantcontractgroepen PASS. Hosted reviewcatalogus1796/1772official/24protected HTTP200; G1100BN juiste eigen fabrikant-URL HTTP200; import1772/612photoReady HTTP200; review zonder visitor401. Authclient/toegangsbeleid gelijk. Browsergoedkeuring faalde door capaciteit, geen browseromweg; fysieke telefoon/visitor-write niet getest. Twee bronbeelden onverwerkbaar;24PDF-kopieën lokaal signature/EOF/SHA gecontroleerd, overige READY maar lokale verificatie door proxy403onvolledig. Volledige data/reviews uitsluitend privé; downloadbare werkset geleverd. Eigenaar herlaadt en behandelt alleen resterende onzekere fabrikantkoppelingen.

## QC-09 — eerste400Lagoo-fotoselecties verwerkt, LVS1/2/3 overgeslagen · 3 november 2026

Checkpoint400 bevestigd: vervolg N8100CH.24LVS1/2/3varianten uitgesloten van galerie, brondata/Shopify daarvoor ongemoeid.400bekeken varianten verwerkt in private importwerkkopie:366met selectie/367beelden,34zonder keuze blijven open. Alle oorspronkelijke kandidaten, specificaties, prijzen, opties en eigen PDF's behouden. Export bevat approvedLagooImport. Geen automatische goedkeuring/afkeur of D1-reset.

Actuele Shopifyinventaris6DRAFT-proefgroepen; binnen eerste400bestaan3groepen/25varianten. Vijf Nesso-variantkoppelingen gecorrigeerd en drie niet-geselecteerde productgalerijreferenties verwijderd; eigen bestanden behouden. Alle25koppelingen en drie galerijen exact teruggelezen; geen nieuwe producten/publicatie. De overige30groepen zijn alleen voorbereid in importdata, niet geïmporteerd. [Scope/rollback/testgrenzen](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_400_APPLIED_2026-11-03.md).

Sites-versie10 succeeded, bron1b7fabbd6840ec8d2c91511fd1b8fc38776eea66, deployment appgdep_6ae9a3a5712c81918b0638ebdd0bb148. TypeScript/build/45API-SQLite-Lagoo-groepen+6selectie-integriteitstests PASS. Authclient/toegangsbeleid gelijk. Browser/telefoon/hosted visitor-write niet getest. Reviews/checkpoints/volledige catalogus/receipt uitsluitend privé. Eigenaar herlaadt de bestaande privétool en vervolgt met N8100CH.

## QC-08 — alleen goede foto's, vaste kleur, checkpoints per20 · 3 november 2026

Galerie toont één selecteerknop per foto, geen fout-/twijfelactie. Deselecteren=unchecked; niet geselecteerd is geen afkeur. Kleur/SKU blijven sticky bovenaan. Foto-oordelen direct opgeslagen; bij20/40/60etc en laatste groep eerst online checkpoint, dan volgende product. Herladen hervat op nextSku van laatste galeriecheckpoint; tussentijdse bevestigde selecties blijven behouden. Zelfde eigenaargebonden API/schema, geen Shopify-write. TypeScript/build/45API-SQLite-Lagoo-groepen PASS. Browser/telefoon/hosted visitor-write niet getest. Versie9 succeeded, bron c5a4ee8dea2043da36db698505cb19bfc06893a2, deployment appgdep_6ae98d0bef948191831ff2ad92f3b432. Authclient/toegangsbeleid identiek. [Dossier](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_SELECTION_2026-11-03.md). Eigenaar herlaadt en controleert selectie/hervatten na20producten.

## QC-07 — Lagoo-galerie per SKU · 3 november 2026

Dezelfde privétool toont producttitel, kleur en alle kandidaatfoto’s; per foto Goed/Niet goed/Twijfel. Meerdere goede foto’s per variant, productwissel handmatig. Individuele foto-oordelen via bestaande D1-review-API, geen automatische hoofdfotokeuze/Shopify-write. TypeScript/build en44API/SQLite/Lagoo-contractgroepen PASS, inclusief twee onafhankelijke oordelen binnen één SKU. Browser/telefoon niet getest. Sites-bron71e835d774cdca06467f685e9286ed0fc0c8feb8, deployment appgdep_6ae98b7954fc8191b5ce72dfe703f0a0 succeeded. [Werkwijze](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_GALLERY_2026-11-03.md). Eigenaar herlaadt privétool en beoordeelt foto’s per kleurvariant. Bij herladen start galerie op eerste product; bevestigde oordelen blijven zichtbaar.

## QC-06 — Lagoo: directe kleurcontrole · 2 november 2026

Dezelfde privétool opent nu standaard alleen Lagoo: kleur uit titel groot boven één foto, Ja/Nee/Twijfel en automatisch volgende SKU na bevestigde opslag. Andere foto wisselt kandidaat direct. Geen ronde-start of algemene merk-/PDF-menu's in de eenvoudige weergave; Uitgebreid behoudt de bestaande QC en voortgang. [Actuele werkwijze op quality-control](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_FAST_REVIEW_2026-11-02.md).

Sites-versie7 succeeded; broncommit e21a5308e2d4867fc702a0bd73d13b8ec7de6177, deployment appgdep_6ae897e9677c81918bd7fe9efee75b7f. TypeScript/build,43bestaande API/SQLite/Lagoo-groepen en6gerenderde kleurcontrolecontracten PASS. Hosted Lagoo1796kaarten en SKU-gallery HTTP200; review zonder visitor401. Native begrensde24reviews+1checkpoint identiek vóór/na, authclient/toegangsbeleid gelijk. Geen Shopify-write, catalogus- of databaseschemamutatie. Browser/telefoon/hosted visitor-write niet opnieuw getest; eerdere previewinfrastructuur niet aantoonbaar hersteld. Volgende QC-actie: eigenaar herlaadt privélink en controleert kleur/foto met directe knoppen. Andere storefronttaken hieronder blijven afzonderlijk.

**31 oktober 2026 · NAV-03 / TILE-02 PREVIEW_VERIFIED / OWNER_REVIEW_PENDING.** Compact menu, startwaarde1m² en tegelinformatie staan in het gecontroleerde concept. Geen actieve schrijver na overdracht.

## QC-05 — Lagoo in dezelfde privécontrole · 2 november 2026

Afzonderlijk van het NAV-03-themaconcept: branch `quality-control` bevat nu 211 Lagoo-brongroepen als 1.796 SKU/kleurkaarten in [dezelfde privétool](https://badkamercity-quality.jason015.chatgpt.site), versie6. Per SKU hoofdfoto kiezen/expliciet goedkeuren; Aanleverlijst met ontbrekende PDF, technische documentatie, foto, kenmerken en EAN. 1.229 afbeeldingen en251PDF-bestanden in eigen Shopify Files; PDF-kopieën volledig op SHA256/grootte gecontroleerd. 92groepen zonder directe PDF; koppelsuggesties blijven ongeverifieerd. Geen automatische goedkeuring of fotocorrectie.

Sites-broncommit `5634119673735eb88cce104c51e2b4f8fe7a8d2a`, deployment `appgdep_6ae894b87f3c8191b8f1ce1d6894e20c` succeeded. TypeScript/build/43contractgroepen PASS. Hosted Lagoo1796kaarten en lazySKU-gallery HTTP200; review zonder visitor401. Bounded native24reviewrijen+1checkpoint identiek vóór/na, authclient/toegangsbeleid ongewijzigd. Browser/telefoon/hosted-visitorwrite niet getest in deze taak. Volledige catalogus en reviews blijven privé; publieke Git alleen code en scope.

Vijf bestaande DRAFT-proefomschrijvingen gebruiken nu eigen PDF-links. Geen volledige import/publicatie van overige205groepen. Volgende QC-actie: eigenaar kiest Lagoo en controleert foto's en ontbrekende gegevens per SKU. [QC-dossier op quality-control](https://github.com/jlamping1997/badkamercity/blob/quality-control/quality-control/LAGOO_QC_2026-11-02.md). NAV-03-status en vervolghandeling hieronder blijven van kracht voor het storefrontthema.

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
