# Wiesbaden — uitvoeringsresultaten 21 oktober 2026

**Rapportstatus: SHOPIFY_COMPLETE_INDEX_BLOCKED.** De beschreven Shopify-uitvoering is afgerond en teruggelezen, zonder resterende uitvoeringsuitzonderingen. De externe zoek-/filterindex is niet gesynchroniseerd omdat bestaande sessietoegang ontbreekt. Ontbrekende brongegevens en historische blokkades staan hieronder afzonderlijk geregistreerd.

Deze uitvoering volgt het [vaste uitvoeringsplan](WIESBADEN_EXECUTION_PLAN.md) en het [prijsbroncontract](wiesbaden/PRICE_SOURCE_CONTRACT_2026-10-21.md). De actuele uitvoerfase staat in [execution-state.json](wiesbaden/execution-state.json). Er is geen nieuwe handmatige opdracht per technische batch nodig.

## 1. Bevestigd resultaat

| Onderdeel | Bevestigd resultaat | Bewijsgrens |
| --- | --- | --- |
| Finale Wiesbaden-catalogus | **2.451 producten, 2.451 ACTIVE, 2.451 gepubliceerd** | Finale Admin-tellingen met precisie EXACT; geen oordeel over ieder afzonderlijk contentonderdeel |
| Prijsaanpassingen | **2.299 voltooid en in Shopify teruggelezen** | Alleen de bedoelde variantprijzen; geen wijziging van belastinginstellingen |
| Openbare prijssteekproef | **4 van 4 geslaagd** | Productpagina en publieke `product.js` HTTP 200; exacte product-/variantidentiteit, bedrag en EUR bevestigd |
| Nieuwe producten | **2 aangemaakt en gecontroleerd** | Beide ACTIVE, Online Store-publicatie aanwezig en primaire productafbeelding READY |
| Verrijking | **2.273 producten en 12.259 metafields toegepast en teruggelezen** | Definitief journal COMPLETE, nul uitvoeringsuitzonderingen |
| Zichtbare correcties en SEO | **187 producten voltooid: 3 gerichte correcties en 184 SEO-aanvullingen** | Definitief journal COMPLETE, exacte waarden of gecontroleerde effectieve titelfallback teruggelezen |
| Hoofdcategorieën | **87 toevoegingen voltooid en teruggelezen** | Geen onbewezen categorie geforceerd; 46 onzekere gevallen blijven open |
| Openbare specificatieproef | **3 van 3 geslaagd; 50 van 50 verwachte specificatierijen** | Nieuwe afzonderlijke specificatietabel in servergerenderde HTML gecontroleerd |

### Prijzen

De fabrikantadviesprijs is voor deze gekalibreerde bron inclusief btw. Bedragen boven exact € 100 worden direct met `ROUND_HALF_UP` afgerond op hele euro's; bedragen tot en met € 100 behouden centen. Het afwijkende CSV-kolomlabel veroorzaakt geen tweede btw-verhoging. Onderbouwing: 20/20 officiële prijsvoorbeelden en 2.411/2.411 overeenkomende CSV-/cachebedragen in het prijsbroncontract.

| Publiek gecontroleerde SKU | Aangetroffen consumentenprijs | Resultaat |
| --- | ---: | --- |
| `24.3710` | € 209,00 | PASS |
| `22.2723` | € 101,00 | PASS |
| `22.2730` | € 99,25 | PASS |
| `21.3650` | € 1.199,00 | PASS |

De lokale beginsnapshot bevat **2.449 Wiesbaden-varianten met `taxable=true`**, nul met `false`, nul met `null` en nul ontbrekende vlaggen. Dit is een telling van die snapshot; er is voor deze telling geen aanvullende Admin-query of belastingmutatie gedaan.

De finale Admin-controle bevestigt winkelvaluta **EUR** en **`taxesIncluded=true`**. De MAIN-theme-identiteit blijft **195491168522**; er is geen themewissel uitgevoerd.

### Twee nieuwe artikelen

| SKU | Consumentenprijs incl. btw | Teruggelezen status |
| --- | ---: | --- |
| `33.6000` | € 6,89 | ACTIVE, Online Store-publicatie, primaire afbeelding READY |
| `75.3510` | € 249,00 | ACTIVE, Online Store-publicatie, primaire afbeelding READY |

### Gecontroleerde specificatietabel

De publieke HTML-proef van **21 oktober 2026, 22:11:06 UTC** vergelijkt uitsluitend de nieuwe `.bc-product-specs__table` binnen de eigen `ProductSpecs`-sectie. De oude omschrijving en JSON-LD-proza tellen niet mee als bewijs van nieuwe specificaties. Iedere pagina bevat precies één gecontroleerde tabel, zonder ontbrekende of onverwachte rijen.

| SKU | Exact aangetroffen | Gerichte controle |
| --- | ---: | --- |
| `18184` | 16/16 rijen | Materiaal Keramiek en vorm Rond aanwezig; de conflicterende serie is niet als nieuwe specificatie gepubliceerd |
| `29.2080` | 25/25 rijen | Tegenstrijdige rijen over uitloop, badinbouw, douchegarnituur en afsluiter weggelaten |
| `41.3540` | 9/9 rijen | Geen elektrische groep; achttien betwiste elektrische eigenschappen uitgesloten |

Hiermee is voor deze drie producten bevestigd dat de nieuwe gecontroleerde gegevens via de bestaande specificatieroute worden weergegeven. Dit is geen volledige visuele browserproef of bewijs van externe facetsynchronisatie.

## 2. Afgeronde verrijking, SEO en categorieën

Het definitieve verrijkingsjournal is **COMPLETE**, afgerond op **21 oktober 2026, 22:32:59 UTC**, met **nul uitzonderingen**. De 20-productpilot met 113 metafields is gevolgd door de volledige verwerking; onderstaande aantallen zijn gerealiseerde eindtellingen.

| Onderdeel | Definitief toegepast en teruggelezen |
| --- | ---: |
| Producten in de verrijkingsrun | **2.273** |
| Metafieldwijzigingen | **12.259** |
| Gegroepeerde specificatiefeiten | **33.186** |
| Nieuwe Shopify-filterwaarden | **6.345** |
| Documentlijsten | **1.368** |

Deze eenheden zijn verschillend: een specificatiefeit is een rij binnen een JSON-metafield, een documentlijst kan meerdere links bevatten en een product kan meerdere gewijzigde metafields hebben. Tel ze niet bij elkaar op als productaantallen. Nieuwe Shopify-filterwaarden bewijzen geen wijziging van de externe index. Een opgeslagen documentlijst bewijst evenmin dat iedere afzonderlijke URL opnieuw is gedownload en inhoudelijk beoordeeld.

Het zichtbare-afwerkingsjournal is eveneens **COMPLETE**, afgerond om **22:37:24 UTC**, met **187 gecontroleerde productupdates, 87 gecontroleerde categorie-addities en nul uitzonderingen**. De productupdates bestaan uit drie gerichte correcties en 184 aanvullingen van lege SEO-overrides. Categorie-addities zijn waar passend in dezelfde productupdate meegenomen; deze aantallen mogen niet als verschillende producten bij elkaar worden opgeteld.

De drie gerichte correcties betreffen `29.2502`, `18184` en `38.4140`. Voor `29.2502` zijn de afgekorte producttitel en de afgebroken SEO-beschrijving vervangen door de geverifieerde volledige productbenaming respectievelijk een complete beschrijving met SKU. Bij `18184` is de tegenstrijdige oude maat `320 × 320 × 130` uit de omschrijving verwijderd en is de SEO-beschrijving aangepast. De brongebonden tekstcorrectie van `38.4140` is eveneens teruggelezen.

Bij **14 updates** gebruikt Shopify de producttitel als effectieve SEO-titel en wordt de gelijkluidende expliciete override als `null` opgeslagen. De terugleescontrole beoordeelt in die gevallen de effectieve titel, terwijl de SEO-beschrijving exact wordt vergeleken. Voor **`18184`** bevestigt een aanvullende openbare controle om **22:36:05 UTC** HTTP 200, de verwachte meta-description en de head-titel **“Wiesbaden Luna waskom rond 32,5 x 14 cm keramiek glans wit – Badkamercity”**. Dit is de producttitel met de normale winkelsuffix, dus geen ontbrekende zichtbare SEO-titel.

## 3. Behoud en concrete uitzonderingen

- **151 beschermde, eerder gecontroleerde producten** blijven buiten ongecontroleerde inhoudelijke overschrijving.
- **25 bestaande artikelen zonder exacte bronmatch** blijven behouden. Voor hun ontbrekende prijsbron wordt geen bedrag afgeleid uit een vermoede btw-factor.
- **28 historische nieuwe kandidaten zonder positieve adviesprijs** blijven onopgelost: de fabrikantcache geeft voor alle 28 € 0,00; 27 ontbreken in de CSV en de enige CSV-match, `41.3563`, heeft eveneens € 0,00. Er wordt geen verkoopbare nulprijsvermelding aangemaakt.
- **Drie historische automatische veiligheidsblokkades** voor `20.3447`, `41.3676` en `41.3523` zijn niet opnieuw geprobeerd en niet via een andere route omzeild. Ze blijven afzonderlijk geregistreerd.
- **46 onzekere hoofdcategorietoewijzingen** blijven open. Er is zonder voldoende onderbouwing geen categorie geforceerd; deze gevallen zijn geen mislukte writes binnen de 87 afgeronde toevoegingen.

Ontbrekende of betwiste afzonderlijke feiten houden de overige geschikte artikelen niet tegen. Een eerdere reviewvermelding is geen reden om een bestaand artikel automatisch te archiveren.

## 4. Externe filterindex

**BLOCKED_NO_EXISTING_SESSION_AUTH — NIET GESYNCHRONISEERD.** De openbare service is bereikbaar: `/verified/health` gaf op **21 oktober 2026, 22:00:25 UTC** HTTP 200, `ok=true`, versie `0.4.0`, service `badkamercity-filter-api-verified-candidate`, index `bc_verified_full_20261013_874e415c15` en 149 profielen.

De gerichte controle van de bestaande SSH-route vond in deze sessie geen agentidentiteiten, gebruikersconfiguratie of bestaande effectieve sleutelbestanden. Er zijn geen nieuwe credentials aangemaakt en geen servermutaties uitgevoerd. De aanwezige route voor gerichte Typesense-updates vereist toegang via de bestaande SSH-/Dockeromgeving.

Zeven publieke collectieprofielen zijn gelezen om bestaande veldnamen en datatypen te onderbouwen. Dat is leesbewijs, geen synchronisatie. **Het schrijven en teruglezen van Shopify-metafields bewijst niet dat externe zoekresultaten, facetwaarden, prijsranges, titels of nieuwe indexdocumenten zijn bijgewerkt.** Die onderdelen blijven open totdat een echte indexverwerking en onafhankelijke zoek-/filtercontrole zijn vastgelegd.

De private indexinvoer is opnieuw gegenereerd uit de **definitieve** readback-journals. Iedere wijziging is gekoppeld aan exacte product-ID/SKU; enrichment-operaties matchen ook op operatie-ID en veldtelling. Er zijn nul onbevestigde enrichment-producten en nul bevestigde operaties buiten de actuele manifesten.

| Hervatbare indexinvoer | Definitieve omvang | Resterende indexvoorwaarde |
| --- | ---: | --- |
| Bestaande producten met bevestigde gewenste indexwaarden | **2.422 producten, 7.207 veldwaarden** | Huidige indexdocumenten en schema lezen; werkelijke verschillen berekenen |
| Daarvan consumentenprijzen | **2.299** | Bewezen veld `price_cents:int64`; exact naar centen, zonder nieuwe btw-bewerking |
| Daarvan filters met bewezen mapping | **4.908 waarden via 13 mappings** | Huidig schema en exacte identiteit per document bevestigen |
| Bevestigde filters zonder bewezen mapping | **1.437 waarden via 8 keys, apart gehouden** | Bestaande ingestiemapping en schema nodig; geen aangenomen veldnamen |
| Nieuwe producten | **2** | Documentbestaan controleren; bij ontbreken de volledige bestaande ingestiemapper gebruiken |
| Producttitelcorrectie | **1, Shopify-readback bevestigd** | Veldnaam `title` bewezen, actueel schematype nog controleren |
| Hoofdcategorie-addities | **87, Shopify-readback bevestigd** | Volledige actuele memberships en bestaande indexrepresentatie lezen |

De acht apart gehouden filterkeys zijn `afwerking`, `coldstart`, `draaibare_uitloop`, `kleur_houder`, `met_omstel`, `met_overloop`, `model` en `montagewijze`. Alle drie zichtbare correcties en 184 SEO-aanvullingen zijn aan het voltooide journal gekoppeld; voor niet-bewezen indexvelden is geen patch verzonnen.

`private-run/index-sync/RESUME.md` bevat de hervatroute; `build-input.cjs` kan de invoer uitsluitend uit lokale bestanden opnieuw opbouwen. De invoer is **geen reeds gemeten indexdiff** en start geen serverproces. Na bestaande geautoriseerde toegang volgen schema-/identiteitscontrole, private backup per ID, dry-run, gerichte patches en exacte readback. Onbekende mappings blijven afzonderlijk en hoeven bewezen prijs-/filterpatches niet tegen te houden.

**Publiek zoeken, collectiekaarten, prijsfilters en sortering kunnen nog oude indexprijzen gebruiken.** De vier productpagina's tonen de aangepaste prijzen; dit bewijst geen actuele externe index. Een kaartbrug kan sommige velden afzonderlijk verversen, zodat niet iedere kaart aantoonbaar verouderd is.

## 5. Afbeeldingen en overige controlegrenzen

De beginsnapshot bevestigt voor **2.449 bestaande producten** een primaire afbeelding met status READY. Bij **2.165 mediaverbindingen** was de verbinding na het eerste item afgekapt. Daarom is **geen volledige galerijcontrole** uitgevoerd of geclaimd; aantallen en kwaliteit van alle vervolgafbeeldingen zijn niet op basis van deze snapshot vastgesteld.

De twee nieuwe producten hebben afzonderlijk een teruggelezen primaire READY-afbeelding. **Ongewijzigde bestaande omschrijvingen zijn niet allemaal opnieuw inhoudelijk gecontroleerd of herschreven.** Er wordt daarom geen volledige kwaliteitsclaim voor alle oude bodies of galerijen gedaan.

Deze run bevat geen nieuwe voorraad-/levertijdkoppeling, winkelbrede mobiele of checkouttest, controle van iedere documentinhoud of bewijs van Google-posities. De genoemde openbare controles zijn afgebakende prijs-, specificatie- en SEO-proeven.

## 6. Herstelbasis en bewijsadministratie

De uitvoerder bewaart de originele Shopify-snapshot, wijzigingsmanifesten, oude waarden, uitvoerjournalen en onafhankelijke terugleesresultaten privé. De herstelbasis is gekoppeld aan product-/variant-ID, bronversie en de daadwerkelijk gewijzigde velden. Herstel mag uitsluitend eigen wijzigingen terugzetten en moet latere wijzigingen van anderen respecteren.

Privébewijs omvat onder meer `shopify-before.json`, `price-journal.json`, het definitieve `enrichment-journal.json`, `visible-product-updates-journal.json`, `storefront-price-pilot.json`, `storefront-enrichment-pilot.json`, `storefront-seo-fallback.json`, `index_sync_readiness.json` en de definitieve `index-sync/manifest.json` met bron-/outputhashes. Deze namen dienen als overdrachtsverwijzing; de ruwe bestanden worden niet aan deze publieke repository toegevoegd. Publieke Git bevat het plan, bronhashes, veilige consumentenprijsvoorbeelden en resultaatnotities; geen ruwe leveranciers-CSV, kostprijzen, persoonsgegevens, credentials of volledige herstelbackups.

## 7. Afsluiting van de beurt

De Shopify-uitvoering en de beschreven terugleescontroles zijn afgerond. Open blijven uitsluitend de benoemde bron-/categoriegevallen, historische blokkades en de externe indexstap met ontbrekende toegang en schema-/mappingcontroles. Deze worden niet als gesynchroniseerd of inhoudelijk opgelost gepresenteerd.

**Na afsluiting van deze beurt blijft geen achtergrondtaak draaien.** Overblijvend werk wordt pas hervat in een volgende actieve uitvoering vanaf het opgeslagen checkpoint. Dit rapport is geen bewijs van een ingestelde doorlopende automatisering.
