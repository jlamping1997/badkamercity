# FIX-01 — herstel van verwijderd reviewconcept

**31 oktober 2026 · RESTORED_SOURCE_VERIFIED / OWNER_REVIEW_PENDING.** De eigenaar vroeg het verwijderde concept opnieuw te maken. Herstel is voltooid; geen actieve schrijver of achtergrondtaak blijft actief.

| Onderdeel | Gecontroleerde stand |
| --- | --- |
| Verwijderd concept | 195948839178, niet meer aanwezig bij de opening |
| MAIN | 195947036938 — BadkamerCity - Categorieen zonder schuiven |
| Hersteld concept | **195974824202 — BadkamerCity - Betrouwbaar bestellen en filters**, UNPUBLISHED, processing=false |
| Codebron | `d510fc2167240009e2d0edf478f745ed022ab112` op `fix/product-cards-2026-10-14` |
| Duplicatiebasis | Volledige verse MAIN-manifests, 1.354 bestanden; vóór featurewrites nul verschillen met de nieuwe kopie |
| Featureherstel | Exact 21 opgeslagen featurepaden: 20 bestaande gewijzigd + één nieuwe tegelprijssnippet; eindconcept 1.355 bestanden |
| MAIN na herstel | Zelfde rol en alle 1.354 manifestchecksums gelijk aan opening; geen MAIN-filewrite of themapublicatie |

## Bron- en regressiebewijs

Alle 21 codebestanden hebben dezelfde SHA-256 en MD5 als het oorspronkelijke herstelregister. Alle 26 baselinevoorwaarden zijn tegen het verse MAIN-manifest gecontroleerd. Na de write zijn alle 21 kandidaatchecksums via Shopify opnieuw gelezen en exact gelijk. Geen andere kandidaatpaden verschillen van MAIN.

De bestaande vier replays zijn opnieuw uitgevoerd met `node scripts/component-audit/replay-fix01.mjs /workspace/scratch/2e22963b7aa0/fix01-recovery-results`: **18 cart/Sunshower + 44 filters + 46 wishlist + 18 presentatie/calculator = 126 gevallen/checks**. Daarvan 81 controles, 15 regressies en 12 expliciet bevestigde grenzen in de eerste drie groepen; 18 presentatiechecks PASS. Geen DEFECT_REPRODUCED in deze herhaalronde. De grenzen zijn niet stil opgelost of als productie-incident bestempeld.

[Bronintegriteit](source-integrity.json) · [manifest/readback](manifest-verification.json) · [cart/Sunshower](cart-sunshower.json) · [filters](filters.json) · [wishlist](wishlist.json) · [presentatie](presentation.json).

De twee bekende body/hash-uitzonderingen `config/settings_data.json` en `templates/page.retour-aanmelden.json` zijn door de native duplicatie geërfd, niet handmatig overschreven of onafhankelijk via hun body opnieuw geverifieerd. Metadata-/checksumpariteit is geen claim dat deze oude body-uitzonderingen opgelost zijn. De Git-root blijft geen volledige actuele MAIN-snapshot.

## Preview en grenzen

Open [Shopify Thema’s](https://fpa9hu-i3.myshopify.com/admin/themes), selecteer **BadkamerCity - Betrouwbaar bestellen en filters** en kies **Voorbeeld**. Nieuw theme-ID: **195974824202**.

Een anonieme HTTP-aanvraag met preview_theme_id eindigde op de gepubliceerde MAIN. Daarmee is de kandidaatweergave niet gecontroleerd; [de beperking is vastgelegd](http-preview.json). Geen nieuwe volledige browser-/telefoon-/Windowscontrole. Het oorspronkelijke FIX-01-browser-/Theme Check-bewijs blijft gedateerd bewijs voor dezelfde codebytes; niet herlabeld als een nieuwe controle van dit theme-ID.

Geen echte cartwrite, bestelling, checkout, formulierinzending, mailboxcontrole, quote-activatie of product-/prijs-/voorraadmutatie uitgevoerd. Offerteactivatie blijft uit; retourmailontvangst/spam/antwoord blijft open. De bestaande filter-/wishlistgrenzen uit [FIX-01](../README.md) blijven gelden.

## Review en terugzetten

**Exact volgende handeling:** Jackson opent het nieuwe concept in Shopify, beoordeelt de telefoonweergave en controleert een herkenbare fictieve retouraanvraag in de eigen mailbox. Publicatie blijft door de eigenaar; herstel heeft het thema niet gepubliceerd.

De onveranderde MAIN195947036938 blijft de basis. Indien een feature moet worden teruggezet: eerst nieuwe rollen/hashes lezen, dan uitsluitend de twintig betrokken bestaande bodies uit de nog passende MAIN-baseline herstellen. De nieuwe helper pas verwijderen nadat callers hersteld zijn. Het oude verwijderde concept-ID is geen rollbackdoel.
