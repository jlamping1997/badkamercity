# Categorie-meta’s — 10 november 2026

Status: CATEGORY-METADATA-01 / ADMIN_APPLIED_VERIFIED. Eigenaar gaf na reviewronde 5 expliciet opdracht: “Voeg ze toe”.

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

## Tien aparte pagina’s blijven vervolg

Acht vendor-selecties hebben geen eigen native collectie-SEO-veld. Ook het algemene assortimentsoverzicht en het merkenoverzicht vereisen gerichte themalogica of vertaalwaarden. De goedgekeurde teksten staan in pending-theme-metadata.json.

Verse bronvergelijking: MAIN 196395073802, 1.401 files; bestaand UNPUBLISHED 196416504074, 1.406 files. Zes bestaande verschillen betreffen keuzedata en de keuzedatabron. De drie SEO-bronbestanden layout/theme.liquid, locales/nl.json en locales/en.default.json zijn exact gelijk, maar het gehele concept is geen identieke basis. Er is geen overdracht van die andere uitvoering vastgelegd. Daarom geen theme-write, naamwijziging of publicatie in dit dossier; de zes verschillen blijven behouden. De merkenview heeft bovendien nog de canonical van /collections; die is niet stil gewijzigd.

## Herstel en overdracht

De oorspronkelijke waarden en het veldgerichte herstelplan zijn vóór elke betrokken live wijziging privé bewaard in Badkamercity-SEO-backup-2026-11-10.json. Herstel alleen de SEO-velden na controle dat ze nog gelijk zijn aan onze toegepaste waarden; geen volledige collectieobjecten terugzetten. De oorspronkelijke lege homepagevoorkeuren en de twee bestaande Sunshower-waarden zijn eveneens vastgelegd.

GitHub/Shopify-connectoruitvoering; deze workspace bevat geen lokale Git-checkout. Geen Windows-, productkoop-, consent- of Google Ads-test geclaimd. Geen settings_data-body gelezen of geschreven. Codebranch fix/product-cards-2026-10-14, bron shopify/current; dit checkpoint bevat alleen documentatie en veilige metadatatekst.

Eén volgende handeling: eerst de gedeelde conceptstatus van het keuzemenuwerk overdragen of afronden; daarna de tien resterende teksten in een passend UNPUBLISHED concept toepassen en de echte preview-head controleren vóór eigenaarpublicatie. De 169 categorieën, homepage en Sunshower zijn al live en vereisen daarvoor geen themapublicatie. Andere filter-, Ads-, import- en keuzemenuwerkstromen blijven behouden.

Bronnen: [Shopify resource-SEO](https://shopify.dev/docs/apps/build/marketing/optimize-storefront-seo), [collectionUpdate](https://shopify.dev/docs/api/admin-graphql/2026-10/mutations/collectionUpdate), [Google titellinks](https://developers.google.com/search/docs/appearance/title-link).
