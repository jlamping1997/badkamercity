# BadkamerCity — actuele werkstatus

**28 oktober 2026 · DOC-02C brede winkeldocumentatie.** De eigenaar heeft volledige documentatie voor alle onderdelen als actieve scope gekozen. De [oude status](LIVE_STATUS_ARCHIVE_BEFORE_2026-10-28.md) en gedateerde releasehandelingen blijven geschiedenis.

## Resultaat en ingang

Begin bij [architectuur](architecture/README.md) → [dekkingsregister](architecture/COVERAGE.md) → [componentdossiers](architecture/components/README.md) → [technische naslag](architecture/reference/README.md). Negen nieuwe inhoudelijke dossiers vullen footer, homepage, hubs, content/formulieren, accounts/systemen, SEO/talen, apps/privacy, filterketen en checkout/bedrijfsproces aan. Eenheidskaart en onderhoudsroute verbinden de uitleg aan latere kleine verbeteringen.

Daarnaast zijn alle 109 werkelijk gerenderde begrippenlinks aan redirects en Pages gekoppeld: 108 gepubliceerde doelen, één bevestigde 404 (Hygro(meter)).

Alle 1.262 themapaden staan in het register. Alle 37 templates, 80 Liquid-secties, 108 snippets, globale instellingen, blocktypen en assets zijn in de naslag opgenomen. Dit is **geen 100% audit-/bedrijfs-/lanceringsvrijgave**; bronblokkades en ontbrekende praktijktesten blijven zichtbaar. De private productexport van DOC-01 blijft afzonderlijk, niet opnieuw geëxporteerd of openbaar gemaakt.

## Bron en daadwerkelijke controles

| Bron | Stand / grens |
| --- | --- |
| Repository | jlamping1997/badkamercity, publiek |
| Actieve branch bij aanvang | fix/product-cards-2026-10-14 op e5ca6da8b76430b881ff01bd7d4fc568b888ab4c |
| main bij aanvang | 75d499c15db434deb3bf65f834c9b41004773e19 |
| MAIN bij aanvang/einde | 195818389770 — Smooth winkelwagen pop-up; niet gewijzigd |
| Manifest | 26 reads, 1.262 unieke paden; pad/MD5/grootte gelijk aan DOC-01 |
| Verse bronreconstructie | 557 bronnen beschikbaar; 556 bytegelijk, settings_data.json wijkt af; 705 manifest-only in deze reconstructie, eerdere volledige DOC-01-capture blijft gedateerd bewijs |
| Naslag | 955 letterlijke refs; JSON/schema's parsebaar; gegenereerde kaarten zijn geen handmatige review/runtimebewijs |
| Admin | 226 collecties, 119 Pages (118 gepubliceerd), negen menu's, 120 redirects, zeven apps, één blog/artikel/markt; paginering afgemaakt |
| Platform | nl primair/gepubliceerd, EUR/inclusief-btw, NL shopbestemming; verzendprofiel/rates en consentpolicy read-only gelezen |
| Publieke HTTP | 35 GET's: 34×200, bedoelde 404; alle 17 toegewezen hubs; 56 JSON-LD-blokken parsebaar |
| Zoek-API | Vier read-only zoekreads 200; Wastafelkranen 573 en Inloopdouches 305 matchen HTML-context; geen volledige prijs/ID/filter-/preflightvrijgave |
| Echte browser | Desktop 1363×936: footerpanelstaten, tien niet-links; begrippen 109→1→0→109; Rimless-redirect en zes TOC/inhoudskaarten |
| Eerder bewijs | DOC-03A: 15 geïsoleerde gevallen, twee problemen; 72 unieke Sunshower-selecties; beperkte desktopgalerij/maathulp |

[Bewijs en meetgrenzen](architecture/evidence/2026-10-28-complete/README.md). Geen cart-/product-/theme-/checkout-/indexwrite; geen formulier of klantenmail verstuurd. Browser had bestaande previewcontext; geen claim van anonieme sessie. Geen screenshots, cartinhoud, ruwe bodies of geheime waarden in Git.

## Bevindingen en nog open

- **FOOTER-F01:** tien labels hebben geen bestemming. Dit is bron-/HTML-/desktopbevestigd, geen werkende linklijst.
- **GLOSS-F01:** Hygro(meter) leidt via redirect naar een ontbrekend Page-doel; gerichte HTTP-read bevestigt 404. Geen redirect gewijzigd.
- **HOME-F01:** hero uitgeschakeld, populaire collectie leeg; configuratie verklaart ontbreken van die inhoud.
- **CONTENT-F01:** zes Page-toewijzingen noemen ontbrekende suffix-template; vijf gepubliceerd. Voorbeeld Buffers antwoordt 200; geen algemene 404-claim.
- **CART-F01 / SS-F01:** eerder gereproduceerde missing-sectioninhoud en Sunshower pending-navigatie blijven ongewijzigd open.
- **Bronblokkades:** settings-bytepariteit; checkout/accountconfiguratie expliciet Access denied; geen verse bevoegde VPS-/eigen-appbron of Google/deploystaat. Mobiel en operationele bestel-/mail-/betaalcontroles blijven open.
- **DOC-F07:** machine-status was achtergebleven op DOC-00; gelijkgetrokken met deze centrale ingang.

## Exact één volgende handeling

**DOC-03B — inbouw-add en herstelgedrag als volledige keten isoleren:** identiteit → expliciete keuze → aantal → pending → succes/afwijzing/timeout/uncertain → terugkeer. Gebruik echte hashgecontroleerde bron met harde lokale transportstubs, geen echte cartmutatie. De brede onderdelenkaart en begrippenverbinding zijn vastgelegd; bronblokkades en mobiele controles blijven apart open. Geen hervatting van oude import-/publicatiestappen.

## Hervatten en Git

Actieve codebranch blijft fix/product-cards-2026-10-14; main is de vaste documentatie-ingang. Tooling alleen op actieve branch, main alleen documentatie. Lees deze status → AGENTS.md → COVERAGE.md → betrokken dossier. Controleer actuele MAIN, bronhashes en eigen werkmap; GitHub-readback bewijst geen schone Windows-pc. Geen schrijver of achtergrondworker blijft actief na oplevering.
