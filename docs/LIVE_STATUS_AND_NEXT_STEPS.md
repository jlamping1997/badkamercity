# BadkamerCity — actuele werkstatus

**28 oktober 2026 · DOC-03A afzonderlijke functieanalyse.** De [oude status](LIVE_STATUS_ARCHIVE_BEFORE_2026-10-28.md) en oude import-/publicatiehandelingen blijven geschiedenis. Lees deze pagina als huidige ingang.

## Opdracht en uitkomst

Eigenaar vraagt de onderdelen verder los te analyseren, de uitleg te verdiepen en nieuwe bevindingen te zoeken. De nieuwe [microdossiers](architecture/components/micro/README.md) behandelen cartnotification-inhoud/lifecycle, Sunshower-acties, keuzematch/fallback en aantal/identiteit. De bestaande [componentdossiers](architecture/components/README.md) en [routematrix](architecture/ROUTE_RENDERER_MATRIX.md) blijven de bovenliggende kaart.

**DOC-03A vastgelegd:** 15 geïsoleerde gevallen op echte bronbytes: 10 controles, 3 defectreproducties voor **twee** verschillende problemen en 2 bevestigde grenzen. Geen storefrontfix, productmutatie of koopactie in deze ronde. De private productexport uit DOC-01 blijft apart; niet opnieuw geëxporteerd of openbaar gemaakt.

## Bron en bewijs

| Bron | Gecontroleerde stand |
| --- | --- |
| Repository | jlamping1997/badkamercity, publiek |
| Actieve branch bij aanvang | fix/product-cards-2026-10-14 op a5e3c9e0bb8a8cfb7b5aa7715a5019a54c877d7b |
| main bij aanvang | 28741ddb1dd4f777c31565da47d2c1de26345a16 |
| Opnieuw gelezen MAIN | 195818389770 — BadkamerCity - Smooth winkelwagen pop-up |
| Verse code | 22 gerichte bestanden; alle bytes/groottes gelijk aan hun metadata; niet het hele thema opnieuw gescand |
| Replay | Vier JS-bronnen vooraf op SHA-256 gecontroleerd; Node 24.22.1 / happy-dom 21.0.4; harde fetch-/navigatiestubs |
| Sunshower-catalogus | 72 records, unieke selections/URL's/variantidentiteiten; geen Shopify-prijs-/voorraadreadback |
| Desktopbrowser | Viewport 1363×936, bestaande sessie met preview-UI; externe collectie-CTA zichtbaar, Maathulp/Escape/focus, galerijstap 1→2 |
| Mobiel | NOT_TESTED; beschikbare browserinterface bood geen viewportresize. Fixturebreedte is geen browserbewijs |
| Oude bronvrijgave | DOC-01 1.262 ontvangen / 1.261 bytegelijk; settings_data.json-uitzondering blijft OPEN |
| Windows / VPS / checkout | Niet gecontroleerd; geen server-, synchronisatie- of bestelvrijgave |

[Bewijs en herhaalbare methode](architecture/evidence/2026-10-28-micro/README.md). Alleen tooling/fixtures op actieve branch; main krijgt documentatie en veilige proofmetadata. Geen root-theme-sync of publicatie.

## Nieuwe problemen en bevestigde bescherming

- **CART-F01, P1-kandidaat / VERIFIED_ISOLATED:** een volgende response met ontbrekende/null productsection laat vorige artikelinhoud in de popup staan. Twee varianten van dezelfde fout gereproduceerd. Niet vastgesteld dat de server deze respons live leverde.
- **SS-F01, P1-kandidaat / VERIFIED_ISOLATED:** tijdens pending setadd kan een kleurklik productnavigatie aanvragen; hoofdsubmit blijft eveneens enabled. Geen echte dubbele bestelling of cartuitkomst getest.
- Normale popupinhoud wordt vervangen; heropenen annuleert een oude close; cancel/reduced-motionvertraging en stijl-/openerherstel werken in de gecontroleerde stub.
- V2 weigert ambigue exacte matches; netwerkfallback werkt. Geldige JSON zonder groep verbergt de control en vraagt geen semantische fallback: grens, geen aangetoond kapotte live dataset.
- Inbouwidentiteit, lege/nul/fractionele aantallen en een bestaande uncertain-staat worden correct begrensd in de afzonderlijke methodeproeven.

De desktopwaarneming bevestigt de externe kaart met zichtbare pijl, maar sluit de oorspronkelijke mobiele Sunshower-vergelijking niet. De galerijteller werd eerst vóór de asynchrone eindstaat gelezen en kwam daarna correct op 2; geen fout of duurmeting uit die tussenstaat afgeleid.

## Grenzen en veiligheid

Geen add/change/clear/checkout-request naar de winkel, geen cartinhoud in bewijs, geen screenshots opgeslagen, geen live code-/product-/VPS-write en geen nieuwe publicatie. Geen claim van een anonieme browsersessie of fysieke telefoon. Alle test-ID's, productlabels en bedragen zijn synthetisch. Een geslaagde harnessrun bevat bewust defectreproducties en is geen algemene PASS.

Oplossingsrichtingen zijn begrensd beschreven; niet uitgevoerd. Voor een fix: passende conceptbron, de tegenvoorbeelden behouden, gewenste feedback-/onzekerheidsregel vaststellen en relevante browserregressie. Geen globale submitinterceptor of automatische herhaalde koopactie invoeren.

## Exact één volgende handeling

**DOC-03B — inbouw-add en herstelgedrag als volledige keten isoleren:** identiteit → expliciete keuze → aantal → pending → succes/afwijzing/timeout/uncertain → terugkeer. Doe dat met harde lokale transportstubs en exacte bronhashes, zonder echte cartmutatie. Doel: vaststellen welk gezamenlijk actieregel-/foutcontract veilig kan worden hergebruikt. Mobiele DOC-02B en settingspariteit blijven zichtbaar OPEN.

## Hervatten

Lees deze status → AGENTS.md → architecture/components/micro/README.md → het betreffende dossier/proof. Controleer eigen werkmap, actuele MAIN en hashes. Broncheckpoints zijn vindbaar met git log -1 -- docs/architecture/components/micro. Bewaar bestaande wijzigingen. Oudere import-/preview-/publicatiestappen niet opnieuw starten. Geen schrijver of achtergrondworker blijft actief na oplevering.
