# BadkamerCity — bewijslog technische overdracht

## 2026-10-07 — overdracht geschikt maken voor opvolging

**Aanleiding:** de gebruiker wil dat een andere AI/ontwikkelaar morgen zelfstandig met BadkamerCity kan verdergaan, zonder verborgen informatie uit ChatGPT-chats.

**Geverifieerde bronnen:** GitHub repository `jlamping1997/badkamercity`, uitgangscommit `708e07faf9d4e87e2d9d27b11ea058afe53d209c`; Shopify Online Store read-only MAIN-theme `194864677130`. Deze themaversie was volgens de eerdere baselinevergelijking volledig gedekt: **441/441** bestanden. In deze ronde is het Shopify thema **niet aangepast**.

### Opgeleverde stukken

- `HANDOVER_START_HERE.md` — overdracht in 15 minuten, takenroutering, bewijsstatus en valkuilen.
- `AI_HANDOFF_CURRENT.md` — bestaande architectuurhandleiding behouden en uitgebreid met verwijzingen.
- `THEME_COMPONENT_REFERENCE.md` — automatisch samengestelde sectie-/settings-/blockcatalogus.
- `THEME_CODE_MAP_2026-10-07.json` — statische codeafhankelijkheden voor 441 themafiles.
- `SHOPIFY_ADMIN_STRUCTURE_2026-10-07.json` — 9 menu's, 204 collecties, exacte productstatus-tellingen, 174 PRODUCT-metafielddefinities.
- `PRODUCT_METAFIELD_MAPPING_AUDIT.md` — literal-codekeys versus definities, met expliciete aannames/waarschuwingen.
- `OPERATIONAL_RUNBOOK.md` — werkplek, Git, Shopify draft, veilige codewijziging en herstel.
- `TROUBLESHOOTING.md` — symptoommatrix.
- `RELEASE_AND_QA.md` — test- en publicatiegates.
- `WORKED_EXAMPLES_AND_HANDOFF_TEST.md` — negen doorgerekende werksituaties en overnametest.
- `SYSTEM_OWNERSHIP_AND_GAPS.md` — ontbrekende externe dependencies, toegangsgrenzen en echte backupbehoeften.
- `LIVE_STATUS_AND_NEXT_STEPS.md` — bewezen live, test-only en unknown, met prioriteiten.
- `README.md` en `AGENTS.md` aangepast om nieuwe ontwikkelaars direct naar actuele documenten te leiden.

### Uitgevoerde controles en grenzen

- Shopify read-only gecontroleerd: `MAIN`, product/collectie/menu-tellingen, metafield-definities en technische theme-code.
- Reeds eerder vastgelegde 441/441 Shopify/Git-themecontrole gebruikt als vaste codebaseline; themabestanden **niet** gewijzigd.
- Statische analysecode inventariseerde 441 codefiles, 73 Liquid-secties, 25 JSON-templates, setting- en snippet-afhankelijkheden. Syntactische detectie is niet hetzelfde als runtime-aanroep.
- Admin exactheid: 11.053 producten, 11.051 ACTIVE, 1 DRAFT, 1 UNLISTED; 204 collecties: 191 default, 12 `category-landing`, 1 `bc-meubelhub`.
- Handoff-QA: 16 centrale docs/basisbestanden opgehaald, Markdown-linkdoelen in Git gecontroleerd, JSON parsed, codefence-balans gecontroleerd, veiligheidszoekpatronen voor gangbare secrettypes zonder resultaat.
- **Niet uitgevoerd**: externe VPS/Typesense runtime, Shopify checkout-orders, Search Console, PageSpeed/Web Vitals, daadwerkelijke productpublicatie-/specdekking en lokale Windows-CLI/PowerShell-uitvoering.

### Wat nog niet op te lossen is met documentatie alleen

Echte integrale overdracht vereist veilig geregelde toegang en herstelprocedures voor Shopify Admin, domein/GSC, server/backend, leverancierimporters en dataexport/backups. Deze zijn bewust als ontbrekend/extern gedocumenteerd. **Nooit** secrets of klantinformatie in openbare GitHub-documentatie zetten.

**Bij een nieuwe wijziging:** vers Shopify MAIN/Git vergelijken, nieuwe datum/commit/QA noteren en dit bewijslog aanvullen; niet oud bewijs hergebruiken als nieuwe test.
