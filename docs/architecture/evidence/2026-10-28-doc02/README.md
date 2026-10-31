# DOC-02A — bronverdieping en HTML-bewijs

**28 oktober 2026.** [Componentingang](../../components/README.md) en [routematrix](../../ROUTE_RENDERER_MATRIX.md) leggen de bevindingen uit. Bronbranch bij aanvang: c8f76eea2bf8a81ab0f54196e239e0b3930fe20a; main: 2f87039c2774e27010860a4ef5ccb29dcc7bf886. MAIN is opnieuw 195818389770. Alle 1.262 manifestpaden/checksums zijn gelijk aan DOC-01; de settings-bodypariteitsuitzondering blijft open.

| Bestand | Wat werkelijk gecontroleerd is |
| --- | --- |
| source-validation.json | Vers compleet manifest vergeleken met DOC-01; main-product/main-sunshower en settings-body opnieuw gelezen; settings blijft afwijkend |
| documentation-validation.json | Link-/JSON-/broncontroles, afwijzing van de oude root als bron, en herstelde historische main-links |
| claim-anchor-checks.json | 18 exacte bronregelankers bij de genoemde contractclaims; geen runtimetest |
| source-index.json | Expliciet gekozen componentbestanden; alle geselecteerde bytes/groottes passen bij manifest; exacte Git-blobkandidaten op broncommit |
| field-consumers.json | Letterlijke metafieldconsumenten en dynamische locaties; typen/aantallen uit private DOC-01-export, geen waarden |
| http-response-checks.json | Acht anonieme publieke GET-responses: status 200 en Shopify.theme.id 195818389770; URL/grootte/hash |
| rendered-structure.json | Responseaanwezigheid van dialog/keuzeroots/assets; geen uitgevoerde JS of computed styles |
| generated-data-validation.json | Alle 656 groepsassets bytegelijk gereconstrueerd uit hun negen daadwerkelijke bronassets |
| choice-routing-observation.json | Eén Hotbath-response gebruikt oorspronkelijke dataset; revisieguard past niet, ondanks aanwezige groep |

De manifestcontrole vond plaats om 03:15 UTC / **04:15 CET** op 28 oktober 2026; de responsechecks volgden in dezelfde uitvoeringsronde. Het bronbestand bevat de exacte ISO-tijd. Nederland is op deze datum over op wintertijd. De productdata-aantallen horen bij het eerdere exportvenster, niet bij nieuwe realtime reads.

Bewijslabels: VERIFIED_THEME = benoemde codebytes gelezen; VERIFIED_ADMIN = benoemde Admin-export; VERIFIED_HTML = serverresponse gelezen; STATIC_CANDIDATE = nog context/uitvoering nodig; NOT_TESTED = hier niet uitgevoerd. Acht HTTP-200-responses zijn geen browser-, a11y-, koop-/performance- of indexvrijgave. Een SHA van HTML is een archiefreferentie; dynamische markup maakt een volgende response niet noodzakelijk bytegelijk.

De ruwe responses en privé-export staan niet in publieke Git. Geen klant-/order-/kosten-/voorraadwaarden, tokens of onbewerkte document-URL's toegevoegd. Geen Shopify-theme-/product-/cart-/checkoutmutaties, VPS-query of serverwrite uitgevoerd. De POST-zoekroute is uitsluitend in code gelezen.

De componentindex is opnieuw te bouwen met scripts/build_component_reference.py op de actieve branch; zie [gereedschap](../../components/FOUNDATIONS_AND_TOOLING.md). De selectie is expliciet en is geen volledige JS/CSS/dynamische afhankelijkheidsgraaf. Literal line-nummers horen bij de opgeslagen hashes; heropen bij wijziging.
