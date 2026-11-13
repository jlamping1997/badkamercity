# Categorie-meta’s — 10 november 2026

Status: CATEGORY-METADATA-01 / ADMIN_APPLIED_VERIFIED; vervolg CATEGORY-METADATA-02 / PREVIEW_VERIFIED_AUDIT_COMPLETE. Eigenaar gaf na reviewronde 5 expliciet opdracht: “Voeg ze toe”.

169 bestaande categorieën kregen de goedgekeurde eigen SEO-titel en metabeschrijving. De homepagevoorkeuren en de bestaande Sunshower-keuzehulp zijn eveneens bijgewerkt: 171 metaparen live. Bestaande categorie-identiteiten en de koopgerichte titelstijl zijn behouden. Er zijn geen nieuwe categorieën, routes, redirects of claims over voorraad of conversiewinst toegevoegd.

## Bewijs

- Vooraf alle 227 collecties volledig gepagineerd. De 169 doelen hadden dezelfde identiteit en SEO als het goedgekeurde voorstel; geen conflicten.
- Eerst Wastafelkranen als proef: exacte Admin-readback en openbare HTML. Daarna begrensde batches, met controle vóór en na iedere mutatie.
- Finale volledige read: 169 SEO-paren exact; alle 58 uitgesloten SEO-paren behouden; nul afwijkingen in titel, handle, templateSuffix of de gelezen omschrijving.
- Live nacontrole van alle 169 categorieën plus homepage en Sunshower: 171 overeenkomstige titels en descriptions. 138 via HTTP-letterlijke vergelijking; 33 via browser-DOM met vergeleken metadatadigests. De 31 resterende HTTP-reads stuitten op een tunnel-403 van de netwerkomgeving, niet op aangetoonde site-botdetectie. Die 31 zijn vervolgens via de gewone browser gecontroleerd; geen ongeteste pagina als PASS aangemerkt.
- Canonical, robots en H1 zijn voor alle 171 pagina’s gelijk aan de eerdere nulmeting.
- Homepage: beide oorspronkelijke voorkeuren leeg; beide nieuwe waarden opgeslagen, zichtbaar in Admin en publiek bevestigd. Sunshower: alleen de twee bestaande globale SEO-metafields, met compareDigest; eigen inhoud, template en publicatiestatus behouden.
- Het bijgewerkte interactieve overzicht onderscheidt 171 toegepaste, tien nog niet toegepaste en 58 uitgestelde records. Export, kopiëren, filters, statuslabels en voorbeeldbreedtes gecontroleerd in Node. Een browser-render van het lokale rapport is niet getest.

Deze controles bewijzen geen gewijzigde Google-resultaten, indexatie, rankings, CTR of conversies. Google moet de gewijzigde pagina’s opnieuw crawlen en verwerken en kan zelf een titel of snippet kiezen. Campagnevelden zijn niet gewijzigd.

## Vervolg voltooid in SEO-concept

De tien aparte metaparen zijn nu in UNPUBLISHED 196441932042 toegepast en exact gecontroleerd. Alle 58 apart gehouden collecties zijn individueel opnieuw beoordeeld. Google Search en Search Console zijn werkelijk gecontroleerd; sitemap succesvol, herindexering van Wastafelkranen geaccepteerd, rapporten verwerken nog data. De volledige uitvoering, beperkingen en het samenvoegen met de uiteindelijke themarelease staan in [FOLLOWUP.md](FOLLOWUP.md). De nulmeting van het Wiesbaden-concept in het oorspronkelijke Admin-checkpoint is historisch; de andere uitvoering is sindsdien uitgebreid.

## Herstel en overdracht

De oorspronkelijke waarden en het veldgerichte herstelplan zijn vóór elke betrokken live wijziging privé bewaard in Badkamercity-SEO-backup-2026-11-10.json. Herstel alleen de SEO-velden na controle dat ze nog gelijk zijn aan onze toegepaste waarden; geen volledige collectieobjecten terugzetten. De oorspronkelijke lege homepagevoorkeuren en de twee bestaande Sunshower-waarden zijn eveneens vastgelegd.

GitHub/Shopify-connectoruitvoering; deze workspace bevat geen lokale Git-checkout. Geen Windows-, productkoop-, consent- of Google Ads-test geclaimd. Geen settings_data-body gelezen of geschreven. Codebranch fix/product-cards-2026-10-14, bron shopify/current; het oorspronkelijke Admin-checkpoint bevatte alleen documentatie; het vervolg bevat vier gerichte themabestanden op de codebranch en documentatie op beide branches.

Eén volgende SEO-handeling: eigenaar beoordeelt het concept en neemt de vier SEO-wijzigingen na verse bronvergelijking mee in het definitieve releaseconcept. Behoud de ongepubliceerde Wiesbaden-aanpassingen wanneer die deel worden van dezelfde release; laat een later gepubliceerd ouder concept de SEO niet terugdraaien. De 169 categorieën, homepage en Sunshower blijven al live. Andere werkstromen behouden.

Bronnen: [Shopify resource-SEO](https://shopify.dev/docs/apps/build/marketing/optimize-storefront-seo), [collectionUpdate](https://shopify.dev/docs/api/admin-graphql/2026-10/mutations/collectionUpdate), [Google titellinks](https://developers.google.com/search/docs/appearance/title-link).
