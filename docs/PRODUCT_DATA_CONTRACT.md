# BadkamerCity productinformatiecontract v0.1

## 1. Documentstatus en scope

| Onderdeel | Waarde |
| --- | --- |
| Taak | `BC-DATA-003` - Brononafhankelijk productinformatiecontract v0.1 vaststellen |
| Datum | 2026-08-10 |
| Status | `DONE` - binnen de brononafhankelijke documentatiescope menselijk goedgekeurd |
| Menselijk goedgekeurd | 2026-08-10 |
| Contractstatus | Bestuurde conceptuele werkbasis v0.1; geen definitieve Shopify-, leverancier- of productieschema-mapping. |
| Projectstatus | `ACTIVE FOR DISCOVERY - IMPLEMENTATION BLOCKED` |
| Scope | Logische productinformatie, betekenis, toepasselijkheid, kwaliteit, leegstaat, broncategorie en eigenaarsrol |
| Buiten scope | Definitieve Shopify namespace/key, leverancierkolommapping, import, productmutatie, categorie-, URL-, SEO-, design- of implementatiebesluit |
| Contractkeys | 190 unieke conceptuele keys |
| Logische domeinen | 15 |

Dit document beschrijft welke informatie BadkamerCity functioneel nodig kan hebben. Het bewijst niet dat die informatie al beschikbaar is en is geen definitieve Shopify- of leveranciermapping.

**Menselijk goedgekeurd:** 2026-08-10.

## 2. Doel en grenzen

Het contract verbindt toekomstige productdata met productpagina's, productkaarten, zoeken, filters, switchers, configurators, calculators, cart, logistiek, SEO, feeds en kwaliteitscontrole. Het blijft brononafhankelijk: een toekomstige leverancierkolom kan pas na afzonderlijke bronaanlevering aan een contractkey worden gekoppeld.

Het contract bepaalt nadrukkelijk niet:

- hoe een leverancierkolom heet of wordt getransformeerd;
- welke data werkelijk beschikbaar of betrouwbaar is;
- welke Shopify namespace, key of definitie wordt aangemaakt;
- welke categorieboom, URL, indexatieregel, prijsregel of klantbelofte geldt;
- welke logistieke fallbacktekst wordt gepubliceerd;
- welke implementatie wordt gebouwd.

## 3. Gebruikte bewijsbronnen

| Bron | Gebruikt bewijs | Belangrijkste grens |
| --- | --- | --- |
| `docs/MASTERPLAN.md` v0.10 | Projectvisie, zelfstandige uitvoeringen, circa 20.000-productdoel, producttype-eisen, functies, risico's en blokkades | Eisen zijn geen bewijs van beschikbare waarden |
| `docs/SHOPIFY_ADMIN_INVENTORY.md` | 7.827 producten/varianten, native velden, SKU/vendor/producttype, metafielddefinities, inventory en configuratie | Snapshot 2026-08-04; specificatiedekking begrensd; volledige appbron niet toegankelijk |
| `docs/ACTIVE_THEME_USAGE.md` | Actieve PDP, V2-/legacyswitcher, themeveldgebruik, media/prijs/inventoryconsumenten | Statisch bewijs; runtimevolledigheid niet bewezen |
| `docs/SUPPLIER_DATA_INVENTORY.md` | Nul oorspronkelijke lokale bronnen; switcherassetvelden, identifiers, kwaliteit en ontbrekende input | Geen externe bronnen; afgeleide asset is geen leverancierbron |
| `docs/COMPETITOR_SEO_ANALYSIS.md` | Alleen bevestigde behoeftecontext voor keuzehulp, content en service | Geen concurrentiestructuur, tekst of ontwerp overgenomen |
| `docs/REPOSITORY_AUDIT.md` | Technische risico's en ontbrekende documentatie | Statische momentopname; geen doelarchitectuur |

## 4. Bewijs- en contractlabels

| Code | Verplicht label | Betekenis |
| --- | --- | --- |
| `BH` | **BEWEZEN HUIDIG** | Feitelijk aangetoond in Admin, code of bestaande data; geen kwaliteitsgoedkeuring |
| `BE` | **BEVESTIGDE EIS** | Expliciet bevestigd in projectdefinitie of masterplan |
| `VC` | **VOORGESTELD CONTRACT** | Logische v0.1-aanbeveling; nog menselijk goed te keuren |
| `LA` | **LEVERANCIERAFHANKELIJK** | Pas met echte leveranciersdata inhoudelijk te valideren |
| `BR` | **BEDRIJFSREGEL VEREIST** | Commerciële, operationele of juridische beslissing nodig |
| `AF` | **AFGELEID** | Mag later uit goedgekeurde bronvelden worden berekend |
| `OB` | **OPEN BESLISSING** | Bevoegde menselijke rol moet kiezen |
| `NO` | **NOG ONDERZOEKEN** | Feitelijk bewijs ontbreekt |

Combinaties zoals `BH+VC` betekenen dat een huidig concept bewezen is, terwijl de genormaliseerde contractbetekenis nog een voorstel is.

## 5. Contractprincipes

1. Iedere key heeft één betekenis; synoniemen verwijzen naar één canoniek contractbegrip.
2. Een bronwaarde wordt nooit zonder bron-, snapshot- en validatiecontext als klantwaarheid behandeld.
3. Klantzichtbare en interne commerciële data blijven gescheiden.
4. Zelfstandig verkoopbare uitvoeringen blijven afzonderlijke producten met eigen URL en SKU conform de bevestigde projectarchitectuur.
5. Specificaties hebben bij voorkeur een betekenis, datatype, gecontroleerde waarde en eenheid; vrije tekst is een uitzondering.
6. Relaties zijn gericht en getypeerd; een relatie zonder geldig doelobject faalt validatie.
7. Logistieke velden beschrijven data en status, niet automatisch een klantbelofte.
8. De huidige V2-switcherasset is bewijs van bestaand gedrag, geen definitieve bronarchitectuur.
9. Leegstaatgedrag is expliciet; een ontbrekende waarde krijgt nooit een verzonnen commerciële of logistieke tekst.
10. Alle vereisteniveaus, opslagcategorieën en kwaliteitsgates zijn voorstellen totdat de projecteigenaar ze goedkeurt.

Gebruikscodes in de matrix: `PDP`, `CARD`, `SEARCH`, `FILTER`, `SWITCH`, `CONFIG`, `CALC`, `CART`, `LOG`, `SEO`, `FEED` en `QA`.

Producttypecodes: `ALL` = alle producten, `SAN` = algemeen sanitairproduct, `TILE` = tegel, `SHOWER` = doucheset, `FURN` = badkamermeubel en `SET` = toekomstige complete set.

## 6. Namingconventie voor conceptuele contractkeys

- patroon: `domein.betekenis`;
- uitsluitend lowercase ASCII en underscores binnen een segment;
- exact één punt tussen domein en betekenis;
- geen `custom.*`, Shopify namespace of leverancierprefix;
- enkelvoud voor één waarde, inhoudelijk duidelijk meervoud voor lijsten;
- geen afkorting wanneer die betekenis kan veranderen;
- synoniemen worden genormaliseerd: `kleur` is de specifieke waarde, `basiskleur` een gecontroleerde kleurfamilie; zij zijn niet uitwisselbaar;
- een nieuwe key vereist eerst controle op semantische overlap met alle bestaande keys.

## 7. Vereisteniveaus

| Niveau | Betekenis in v0.1 |
| --- | --- |
| `PUBLICATION_BLOCKER` | Voorgesteld: product is niet publiceerbaar zonder geldige waarde of expliciet toegestane `NOT_APPLICABLE` |
| `TYPE_BLOCKER` | Voorgesteld: verplicht voor het genoemde producttype of de genoemde functie |
| `REQUIRED_WHEN_APPLICABLE` | Verplicht zodra het kenmerk, proces of de relatie van toepassing is |
| `RECOMMENDED` | Gewenst voor kwaliteit, keuzehulp, SEO of conversie; niet altijd blokkerend |
| `OPTIONAL` | Alleen gebruiken en tonen wanneer aanwezig en geldig |
| `FUTURE` | Bewust geen huidige lanceringsvereiste of afhankelijk van een later besluit |

Deze niveaus zijn **VOORGESTELD CONTRACT** en nog niet menselijk goedgekeurd.

## 8. Broncategorieën

| Code | Broncategorie | Gebruik |
| --- | --- | --- |
| `SNC` | `SHOPIFY_NATIVE_CURRENT` | Huidig native Shopifyveld is bewezen |
| `ECC` | `EXISTING_CUSTOM_CURRENT` | Huidig custom veld of afgeleide themeasset is bewezen |
| `SUP` | `SUPPLIER_SOURCE` | Waarde kan uit een later aangeleverde leverancierbron komen |
| `BCE` | `BADKAMERCITY_EDITORIAL` | BadkamerCity bepaalt/redigeert inhoud |
| `COM` | `COMMERCIAL_RULE` | Commerciële eigenaar bepaalt semantiek of waarde |
| `OPS` | `OPERATIONAL_RULE` | Operationele/logistieke eigenaar bepaalt semantiek of waarde |
| `DRV` | `DERIVED_VALUE` | Waarde wordt uit goedgekeurde velden berekend |
| `EXT` | `EXTERNAL_SYSTEM_FUTURE` | Mogelijke latere externe bron of integratie |
| `UND` | `UNDECIDED` | Bronkeuze staat open |

## 9. Eigenaarsrollen

| Code | Rol | Verantwoordelijkheid in dit contract |
| --- | --- | --- |
| `PO` | Projecteigenaar | Contract, prioriteiten en gates goedkeuren |
| `PDO` | Productdata-eigenaar | Betekenis, dekking, identifiers en datakwaliteit |
| `CO` | Commercieel eigenaar | Prijs-, korting- en commerciële regels |
| `OO` | Operationeel/logistiek eigenaar | Voorraad, levering, verpakking en fulfilment |
| `CE` | Content-eigenaar | Producttekst, FAQ en redactionele kwaliteit |
| `SEO` | SEO-eigenaar | Vindbaarheid, metadata en routeklasseadvies |
| `TO` | Technisch eigenaar | Schema, afleiding, referenties en technische validatie |
| `PJ` | Privacy/juridisch verantwoordelijke | Rechten, compliance, claims en documentstatus |
| `SUP` | Leverancier/bronhouder | Bronspecificatie, actualiteit en broncorrectheid |

## 10. Centrale veldmatrix

Elke rij is een conceptueel contractveld. `Huidig bewijs` noemt alleen bewezen opslag/velden; `Opslagcat.` is een abstract voorstel en geen Shopify-mapping.

| contract_key | Nederlandse naam | Domein | Betekenis/definitie | Bewijs | Type | Card. | Eenheid/formaat | Niveau | Types | Bron | Huidig bewijs | Opslagcat. | Gebruik | Validatie | Leegstaat | Eigenaar | L-afh | Open vraag/beperking |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
<!-- CONTRACT_MATRIX_START -->
| `governance.source_supplier` | Bronleverancier | governance | Organisatie die de aangeleverde bronrecord beheert | VC+LA | reference | 0..1 | leverancier-ID | REQUIRED_WHEN_APPLICABLE | ALL | SUP | Geen lokale bron | metaobject/reference | FEED,QA | Geldige leverancierreferentie | MANUAL_REVIEW | PDO | ja | Leveranciersregister ontbreekt |
| `governance.source_system` | Bronsysteem | governance | Systeem of bestandstype waaruit de record kwam | VC+LA | string | 0..1 | gecontroleerde code | REQUIRED_WHEN_APPLICABLE | ALL | SUP/EXT | Niet bewezen | custom field | FEED,QA | Niet leeg bij externe bron | MANUAL_REVIEW | TO | ja | Waardelijst later per bron |
| `governance.source_record_id` | Bronrecord-ID | governance | Ongewijzigde identifier binnen de bron | VC+LA | string | 0..1 | bronformaat | REQUIRED_WHEN_APPLICABLE | ALL | SUP | Niet bewezen | custom field | FEED,QA | Uniek binnen bron+snapshot | MANUAL_REVIEW | PDO | ja | Geen globale uniciteitsclaim |
| `governance.source_snapshot_at` | Bronsnapshotdatum | governance | Datum/tijd waarop broninhoud gold | VC+LA | datetime | 0..1 | ISO-8601 | REQUIRED_WHEN_APPLICABLE | ALL | SUP/EXT | V2 heeft `generated_at` | custom field | FEED,QA,LOG | Geldige tijdzone/datum | MANUAL_REVIEW | PDO | ja | Updatefrequentie onbekend |
| `governance.updated_at` | Datalaatst-bijgewerkt | governance | Laatste goedgekeurde inhoudelijke wijziging | BH+VC | datetime | 1 | ISO-8601 | RECOMMENDED | ALL | SNC/DRV | Shopify timestamps bestaan | native | FEED,QA | Niet vóór bron-snapshot | ALLOW_EMPTY | TO | nee | Semantiek handmatig versus sync open |
| `governance.sync_evidence` | Synchronisatiebewijs | governance | Verwijzing naar batch, import of sync-log | VC+NO | reference | 0..1 | bewijs-ID | REQUIRED_WHEN_APPLICABLE | ALL | EXT/UND | Lokaal ontbreekt importbewijs | extern | FEED,QA | Bestaand immutable bewijs | MANUAL_REVIEW | TO | ja | Systeem en retentie open |
| `governance.manual_override` | Handmatige override | governance | Vastlegging dat bronwaarde bewust is overschreven | VC+BR | object | 0..1 | waarde, reden, datum, rol | REQUIRED_WHEN_APPLICABLE | ALL | BCE/COM/OPS | Niet bewezen | custom field | FEED,QA | Reden en bevoegde rol verplicht | MANUAL_REVIEW | PDO | nee | Overridebeleid open |
| `governance.data_owner` | Data-eigenaar | governance | Rol verantwoordelijk voor betekenis en kwaliteit | VC+OB | enum | 1 | rolcode | PUBLICATION_BLOCKER | ALL | BCE | Eigenaarschap onbekend | custom field | QA | Toegestane eigenaarsrol | BLOCK_PUBLICATION | PO | nee | Concrete roltoewijzing vereist |
| `governance.quality_status` | Kwaliteitsstatus | governance | Samengevatte, verklaarbare uitkomst van kwaliteitsgates | VC+AF | enum | 1 | gecontroleerde status | PUBLICATION_BLOCKER | ALL | DRV | Niet bewezen | afgeleid | QA,FEED | Alleen uit gates berekenen | BLOCK_PUBLICATION | PDO | nee | Statuswaarden goedkeuren |
| `governance.publication_status` | Publicatiestatus | governance | Workflowbesluit los van Shopify lifecycle-status | VC+BR | enum | 1 | gecontroleerde status | PUBLICATION_BLOCKER | ALL | BCE/COM/OPS | Niet bewezen | custom field | QA,FEED | Bevoegde overgang en audit | BLOCK_PUBLICATION | PO | nee | Workflow en rollen open |
| `identity.internal_product_id` | Intern product-ID | identity | Stabiele platformreferentie naar product | BH+VC | reference | 1 | platform-ID | PUBLICATION_BLOCKER | ALL | SNC | Shopify product-ID bewezen | native | PDP,CARD,SEARCH,FEED,QA | Uniek en bestaand | BLOCK_PUBLICATION | TO | nee | Niet als leverancier-ID gebruiken |
| `identity.sku` | SKU | identity | BadkamerCity-verkoopidentifier voor zelfstandige uitvoering | BH+BE+VC | string | 1 | trim, hoofdletterbeleid open | PUBLICATION_BLOCKER | ALL | SNC/SUP | `variant.sku`; 17 leeg, duplicaten | native | PDP,CART,SEARCH,FEED,QA | Niet leeg; uniek doel, bronregels later | BLOCK_PUBLICATION | PDO | soms | Normalisatie en duplicaatbeleid open |
| `identity.supplier_article_number` | Leverancierartikelnummer | identity | Artikelidentifier zoals bronhouder die voert | BH+VC+LA | string | 0..* | bronformaat | REQUIRED_WHEN_APPLICABLE | ALL | SUP | Theme verwacht `custom.fabrikantnummer`; waarden niet bewezen | custom field | PDP,SEARCH,FEED,QA | Uniek binnen leverancier waar bewezen | MANUAL_REVIEW | PDO | ja | Meerdere leveranciers mogelijk |
| `identity.gtin` | EAN/GTIN | identity | Gestandaardiseerde handelsidentifier | BH+VC+LA | string | 0..* | digits/string | RECOMMENDED | ALL | SUP | Theme verwacht `custom.ean`; waarden niet bewezen | custom field | SEARCH,FEED,QA | Checkdigit/format pas per type/bron | MANUAL_REVIEW | PDO | ja | Geen onbewezen lengte afdwingen |
| `identity.title` | Producttitel | identity | Klantgerichte naam van zelfstandige uitvoering | BH+BE+VC | string | 1 | tekst | PUBLICATION_BLOCKER | ALL | SNC/BCE | `product.title`; asset heeft één dubbel | native | PDP,CARD,SEARCH,SEO,FEED | Niet leeg; titelbeleid later | BLOCK_PUBLICATION | CE | soms | Structuur per producttype open |
| `identity.handle` | Handle/URL-identiteit | identity | Unieke productroute-identiteit, los van displaytitel | BH+BE+VC | string | 1 | lowercase slug | PUBLICATION_BLOCKER | ALL | SNC | `product.handle`; asset intern uniek | native | PDP,CARD,SEARCH,SEO,FEED | Uniek; geldig slugformaat | BLOCK_PUBLICATION | SEO | nee | Definitief URL-beleid open |
| `identity.brand` | Merk/vendor | identity | Gecontroleerd commercieel merk van product | BH+VC | reference | 1 | merk-ID/label | PUBLICATION_BLOCKER | ALL | SNC/SUP | `product.vendor` gevuld; theme metafieldrisico | native | PDP,CARD,SEARCH,FILTER,SEO,FEED | Geldige merkreferentie | BLOCK_PUBLICATION | PDO | soms | Vendor versus merkmodel open |
| `identity.series` | Serie | identity | Gecontroleerde productserie binnen merk | BH+VC+LA | reference | 0..1 | serie-ID/label | RECOMMENDED | ALL | SUP/BCE | Theme verwacht `custom.serie`; waarden niet bewezen | metaobject/reference | PDP,SEARCH,FILTER,SEO,SWITCH | Serie hoort bij merk | HIDE_COMPONENT | PDO | ja | Seriesregister ontbreekt |
| `identity.collection_context` | Collectiecontext | identity | Functionele collectieplaatsing, niet broncollectie | BH+VC+OB | list<reference> | 0..* | collectie-ID | RECOMMENDED | ALL | SNC/BCE | 201 collecties, 199 leeg | metaobject/reference | PDP,SEARCH,FILTER,SEO | Geldige niet-cyclische verwijzing | HIDE_COMPONENT | SEO | nee | Categorieboom niet besloten |
| `identity.product_type` | Producttype | identity | Gecontroleerde functionele productklasse | BH+VC | reference | 1 | type-ID/label | PUBLICATION_BLOCKER | ALL | SNC/BCE | `product.productType`; 649 waarden, 69 `undefined` | metaobject/reference | PDP,CARD,SEARCH,FILTER,CONFIG,QA | Waarde uit goedgekeurde taxonomie | BLOCK_PUBLICATION | PDO | soms | Taxonomie open; huidige waarden niet normatief |
| `identity.model` | Model | identity | Modelnaam of modelcode, onderscheiden van serie | VC+LA | string | 0..1 | tekst/code | RECOMMENDED | ALL | SUP/BCE | Niet afzonderlijk bewezen | custom field | PDP,SEARCH,FEED | Trim; betekenis per bron | HIDE_COMPONENT | PDO | ja | Serie/modelconflict onderzoeken |
| `identity.lifecycle_status` | Productlevenscyclusstatus | identity | Actief, uitlopend, vervangen of beëindigd als logisch concept | BH+VC+BR | enum | 1 | gecontroleerde status | PUBLICATION_BLOCKER | ALL | SNC/COM | Shopify status is `ACTIVE` voor alle producten | native | PDP,SEARCH,FEED,QA | Toegestane overgang | BLOCK_PUBLICATION | CO | soms | Businesssemantiek open |
| `identity.sellable_execution` | Zelfstandig verkoopbare uitvoering | identity | Bevestigt dat record één bestelbare uitvoering vertegenwoordigt | BE+VC | boolean | 1 | true/false | PUBLICATION_BLOCKER | ALL | BCE/DRV | 7.827 producten met één variant | custom field | PDP,CART,SWITCH,CONFIG,QA | Waar voor huidig doelmodel | BLOCK_PUBLICATION | PDO | nee | Uitzonderingen open |
| `identity.default_variant_reference` | Technische variantreferentie | identity | Verwijst naar bestelbare Shopifyvariant van het product | BH+VC | reference | 1 | variant-ID | PUBLICATION_BLOCKER | ALL | SNC | Eén variant per product bewezen | native | CART,FEED,QA | Variant bestaat en hoort bij product | BLOCK_PUBLICATION | TO | nee | Meer-variantuitzondering niet voorzien |
| `commercial.sale_price` | Verkoopprijs | commercial | Klantzichtbare actuele verkoopprijs | BH+BE+VC | money | 1 | bedrag+valuta | PUBLICATION_BLOCKER | ALL | SNC/COM | Shopify variantprijs wordt gebruikt | native | PDP,CARD,CART,SEO,FEED,QA | Bedrag >= 0; valuta gelijk | BLOCK_PUBLICATION | CO | soms | Prijsbron/actualiteit ontbreken lokaal |
| `commercial.compare_at_price` | Advies-/van-prijs | commercial | Optionele vergelijkprijs met goedgekeurde semantiek | BH+VC+BR | money | 0..1 | bedrag+valuta | OPTIONAL | ALL | SNC/COM | `compare_at_price` wordt gebruikt | native | PDP,CARD,SEO,FEED | Indien gevuld >= verkoopprijs | HIDE_COMPONENT | CO | soms | Juridische/commerciële semantiek open |
| `commercial.purchase_price` | Inkoopprijs | commercial | Interne kostprijs, nooit standaard klantzichtbaar | VC+LA+BR | money | 0..1 | bedrag+valuta | REQUIRED_WHEN_APPLICABLE | ALL | SUP/COM | Lokaal ontbreekt | extern | FEED,QA | Bedrag >= 0; afgeschermd | MANUAL_REVIEW | CO | ja | Opslag/toegang/open businessregel |
| `commercial.currency` | Valuta | commercial | Valuta voor alle geldvelden | BH+VC | enum | 1 | ISO-4217 | PUBLICATION_BLOCKER | ALL | SNC/COM | Shopify geldcontext bewezen | native | PDP,CARD,CART,SEO,FEED | Geldige en consistente code | BLOCK_PUBLICATION | CO | nee | Multivaluta buiten scope |
| `commercial.tax_semantics` | BTW-semantiek | commercial | Geeft aan hoe prijs zich tot belasting verhoudt | VC+BR | enum | 1 | gecontroleerde status | PUBLICATION_BLOCKER | ALL | COM | Niet lokaal bewezen | undecided | PDP,CART,FEED,QA | Goedgekeurde waarde verplicht | BLOCK_PUBLICATION | CO | nee | Juridisch/commercieel besluit nodig |
| `commercial.discount_amount` | Kortingsbedrag | commercial | Verschil tussen geldige compare-at en verkoopprijs | AF+VC | money | 0..1 | bedrag+valuta | OPTIONAL | ALL | DRV | Theme kan korting tonen | afgeleid | PDP,CARD,SEO | max(compare-at - sale, 0) | HIDE_COMPONENT | CO | nee | Alleen bij geldige vergelijkprijs |
| `commercial.discount_percentage` | Kortingspercentage | commercial | Procentuele korting uit geldige prijzen | AF+VC | decimal | 0..1 | procent | OPTIONAL | ALL | DRV | Niet als bronveld bewezen | afgeleid | PDP,CARD | 0..100; vaste afronding later | HIDE_COMPONENT | CO | nee | Afrondingsregel open |
| `commercial.unit_price` | Eenheidsprijs | commercial | Native of berekende prijs per referentie-eenheid | BH+VC+LA | money | 0..1 | bedrag per eenheid | TYPE_BLOCKER | TILE | SNC/DRV/SUP | Theme ondersteunt unit price | native | PDP,CARD,CALC,CART,FEED | Eenheid en basis verplicht | BLOCK_PUBLICATION | CO | ja | Tegelprijsbasis open |
| `commercial.box_price` | Prijs per doos | commercial | Klantprijs voor één verkoopdoos | VC+LA+BR | money | 0..1 | bedrag/doos | TYPE_BLOCKER | TILE | SUP/DRV/COM | Niet bewezen | afgeleid | PDP,CALC,CART,FEED | >=0; sluit aan op prijsbasis | BLOCK_PUBLICATION | CO | ja | Bron versus afleiding open |
| `commercial.square_meter_price` | Prijs per vierkante meter | commercial | Klantprijs per m² | VC+LA+BR | money | 0..1 | bedrag/m² | TYPE_BLOCKER | TILE | SUP/DRV/COM | Niet bewezen | afgeleid | PDP,CARD,CALC,CART,FEED | >=0; sluit aan op doosinhoud | BLOCK_PUBLICATION | CO | ja | Afronding/prijsbasis open |
| `commercial.price_effective_at` | Prijsactualiteit | commercial | Datum/tijd vanaf wanneer prijs geldig is | VC+LA | datetime | 0..1 | ISO-8601 | REQUIRED_WHEN_APPLICABLE | ALL | SUP/COM/EXT | Niet bewezen | custom field | FEED,QA | Niet in onverklaarde toekomst | MANUAL_REVIEW | CO | ja | Updatefrequentie per bron open |
| `commercial.price_source` | Prijsbron | commercial | Gezaghebbende broncategorie en bewijs voor prijs | VC+LA+BR | reference | 1 | bron-ID | PUBLICATION_BLOCKER | ALL | SUP/COM/EXT | Niet bewezen | extern | FEED,QA | Bestaand bronbewijs | BLOCK_PUBLICATION | CO | ja | Bronhouder later vaststellen |
| `content.short_description` | Korte omschrijving | content | Beknopte klantgerichte samenvatting zonder onbewezen claims | VC | string | 0..1 | korte tekst | RECOMMENDED | ALL | BCE/SUP | Niet afzonderlijk bewezen | custom field | PDP,CARD,SEARCH,SEO | Lengtegrens later; geen HTML nodig | HIDE_COMPONENT | CE | soms | Redactionele stijl open |
| `content.long_description` | Lange omschrijving | content | Volledige productomschrijving | BH+BE+VC | rich_text | 1 | gestructureerde tekst | PUBLICATION_BLOCKER | ALL | SNC/BCE/SUP | `product.description` actief | native | PDP,SEARCH,SEO,FEED | Niet leeg; claims herleidbaar | BLOCK_PUBLICATION | CE | soms | Kwaliteitsdrempel open |
| `content.benefits` | Pluspunten | content | Controleerbare klantvoordelen | BH+VC | list<string> | 0..* | korte uitspraken | RECOMMENDED | ALL | BCE/SUP | `custom.pluspunten` 0/7.827 | custom field | PDP,CARD,SEO | Geen duplicaten/onbewezen claims | HIDE_COMPONENT | CE | soms | Businessdoel en bron open |
| `content.attention_points` | Aandachtspunten | content | Relevante beperkingen of aandacht bij keuze/gebruik | BH+VC | list<string> | 0..* | korte uitspraken | RECOMMENDED | ALL | BCE/SUP | `custom.aandachtspunten` 0/7.827 | custom field | PDP | Geen marketingvermomming | HIDE_COMPONENT | CE | soms | Redactionele regels open |
| `content.included_items` | Inbegrepen onderdelen | content | Onderdelen die aantoonbaar worden meegeleverd | BE+VC+LA | list<string> | 0..* | gecontroleerde items | REQUIRED_WHEN_APPLICABLE | ALL | SUP/BCE | Niet bewezen | custom field | PDP,CART,CONFIG,QA | Geen conflict met setrelaties | MANUAL_REVIEW | PDO | ja | Gestructureerde referentie later beoordelen |
| `content.excluded_items` | Niet-inbegrepen onderdelen | content | Verwachte maar niet meegeleverde onderdelen | BE+VC+LA | list<string> | 0..* | gecontroleerde items | REQUIRED_WHEN_APPLICABLE | ALL | SUP/BCE | Niet bewezen | custom field | PDP,CART,CONFIG | Geen conflict met required add-ons | MANUAL_REVIEW | PDO | ja | Klanttekst moet worden goedgekeurd |
| `content.application` | Gebruikstoepassing | content | Beoogde omgeving of toepassing | VC+LA | list<enum> | 0..* | gecontroleerde waarden | RECOMMENDED | ALL | SUP/BCE | Niet bewezen | custom field | PDP,SEARCH,FILTER,SEO | Waardenlijst per type | HIDE_COMPONENT | PDO | ja | Taxonomie open |
| `content.maintenance` | Onderhoudsinformatie | content | Productgericht onderhoud zonder juridische overspraak | BE+VC+LA | rich_text | 0..1 | gestructureerde tekst | REQUIRED_WHEN_APPLICABLE | ALL | SUP/BCE | Niet bewezen | custom field | PDP,SEO | Bron/reviewdatum vereist | HIDE_COMPONENT | CE | ja | Document versus tekst open |
| `content.brand_series_information` | Merk-/serie-informatie | content | Herbruikbare redactionele context bij merk of serie | VC | reference | 0..1 | contentreferentie | RECOMMENDED | ALL | BCE | Niet bewezen | metaobject/reference | PDP,SEO | Merk/serie matcht product | HIDE_COMPONENT | CE | nee | Contentmodel open |
| `content.faq` | Product-FAQ | content | Goedgekeurde vraag/antwoordparen voor dit product/type | BE+VC | list<reference> | 0..* | FAQ-referenties | RECOMMENDED | ALL | BCE | Niet bewezen | metaobject/reference | PDP,SEARCH,SEO | Unieke vraag; actueel antwoord | HIDE_COMPONENT | CE | nee | Schema-/hergebruikbesluit open |
| `content.search_card_specifications` | Zoekkaartspecificaties | content | Kleine selectie beslissende kenmerken voor kaart/search | BH+VC | list<reference> | 0..* | max aantal open | RECOMMENDED | ALL | BCE/DRV | Twee custom zoekkaartkeys in theme | afgeleid | CARD,SEARCH | Verwijst naar geldige specificaties | HIDE_COMPONENT | PDO | nee | Selectieregel per type open |
| `specification.items` | Algemene specificaties | specification | Gestructureerde lijst van betekenis, waarde, type en eenheid | BE+VC+LA | list<object> | 0..* | key,label,value,type,unit | TYPE_BLOCKER | ALL | SUP/BCE | 58 theme-keys; dekking grotendeels onbekend | metaobject/reference | PDP,SEARCH,FILTER,CONFIG,FEED,QA | Unieke key; geldig type/eenheid | MANUAL_REVIEW | PDO | ja | Definitieve specificatiecatalogus open |
| `specification.dimensions` | Productmaatvoering | specification | Genormaliseerde productafmetingen | BE+VC+LA | object | 0..1 | metingen+eenheden | REQUIRED_WHEN_APPLICABLE | ALL | SUP | Diverse theme-/assetkeys | custom field | PDP,FILTER,CONFIG,LOG,FEED | Positieve meetwaarden | MANUAL_REVIEW | PDO | ja | Assen per type open |
| `specification.material` | Materiaal | specification | Gecontroleerd hoofdmateriaal of materialen | BE+VC+LA | list<enum> | 0..* | materiaalwaarden | REQUIRED_WHEN_APPLICABLE | ALL | SUP/BCE | `materiaal_kraan` verwacht | custom field | PDP,CARD,SEARCH,FILTER,SEO | Waarde uit catalogus | HIDE_COMPONENT | PDO | ja | Algemeen versus typeveld open |
| `specification.color` | Kleur | specification | Specifieke verkoopkleur/afwerkingnaam | BH+VC+LA | enum | 0..1 | gecontroleerde waarde | REQUIRED_WHEN_APPLICABLE | ALL | SUP | V2 `kleur` op 3.353 entries | custom field | PDP,CARD,SEARCH,FILTER,SWITCH,CONFIG | Waarde uit catalogus | MANUAL_REVIEW | PDO | ja | Conflict met `basiskleur` expliciet |
| `specification.base_color` | Basiskleur | specification | Genormaliseerde kleurfamilie voor zoeken/filter | BH+VC+AF | enum | 0..1 | gecontroleerde familie | RECOMMENDED | ALL | DRV/BCE | Legacy/theme gebruikt `basiskleur`; dekking onbekend | custom field | CARD,SEARCH,FILTER,SEO | Afleiding uit kleur via goedgekeurde tabel | HIDE_COMPONENT | PDO | soms | Mapping kleur->basiskleur open |
| `specification.finish` | Afwerking | specification | Oppervlaktebehandeling of glansafwerking | BH+VC+LA | enum | 0..1 | gecontroleerde waarde | REQUIRED_WHEN_APPLICABLE | ALL | SUP | V2/theme `afwerking` aanwezig als verwachting | custom field | PDP,CARD,SEARCH,FILTER,SWITCH | Waarde uit catalogus | HIDE_COMPONENT | PDO | ja | Scheiding kleur/finish open |
| `specification.shape` | Vorm | specification | Gecontroleerde geometrische vorm | BH+VC+LA | enum | 0..1 | gecontroleerde waarde | REQUIRED_WHEN_APPLICABLE | ALL | SUP | V2/theme `vorm` | custom field | PDP,SEARCH,FILTER,SWITCH,CONFIG | Waarde uit catalogus | HIDE_COMPONENT | PDO | ja | Typeafhankelijke waarden |
| `specification.mounting_method` | Montagewijze | specification | Wijze waarop product wordt gemonteerd | BH+VC+LA | enum | 0..1 | gecontroleerde waarde | REQUIRED_WHEN_APPLICABLE | SAN,SHOWER,FURN | SUP | Theme verwacht `montage`/`montagewijze` | custom field | PDP,SEARCH,FILTER,CONFIG | Synoniemen genormaliseerd | HIDE_COMPONENT | PDO | ja | `montage` versus `montagewijze` oplossen |
| `specification.technical_properties` | Technische eigenschappen | specification | Overige getypeerde technische kenmerken | BE+VC+LA | list<object> | 0..* | key,value,type,unit | REQUIRED_WHEN_APPLICABLE | ALL | SUP | Theme verwacht vele technische keys | metaobject/reference | PDP,SEARCH,FILTER,CONFIG,FEED | Cataloguskey, type en eenheid | MANUAL_REVIEW | PDO | ja | Veldcatalogus later bronvalideren |
| `specification.feature_flags` | Ja/nee-kenmerken | specification | Getypeerde booleans, niet vrije tekst | VC+LA | list<object> | 0..* | key+boolean | REQUIRED_WHEN_APPLICABLE | ALL | SUP | Renderer accepteert booleans/strings | metaobject/reference | PDP,FILTER,CONFIG,FEED | Alleen true/false/null | HIDE_COMPONENT | PDO | ja | `false` niet als leeg behandelen |
| `specification.enumeration_values` | Enumeratiekenmerken | specification | Kenmerken met gecontroleerde waardelijst | VC+LA | list<object> | 0..* | key+enum | REQUIRED_WHEN_APPLICABLE | ALL | SUP/BCE | V2-opties zijn afgeleid bewijs | metaobject/reference | PDP,SEARCH,FILTER,SWITCH,CONFIG | Waarde in typecatalogus | MANUAL_REVIEW | PDO | ja | Waardelijsteigenaar open |
| `specification.measurement_values` | Meetwaarden | specification | Kenmerken als getal plus expliciete eenheid | VC+LA | list<object> | 0..* | key+decimal+unit | REQUIRED_WHEN_APPLICABLE | ALL | SUP | V2 heeft maatstrings, geen bewezen unitschema | metaobject/reference | PDP,FILTER,CONFIG,CALC,LOG | Getal, bereik en compatibele unit | MANUAL_REVIEW | PDO | ja | Conversieregels open |
| `specification.free_text_notes` | Specificatienotities | specification | Vrije tekst alleen waar geen getypeerd veld volstaat | VC+BR | string | 0..1 | tekst | OPTIONAL | ALL | SUP/BCE | Niet bewezen | custom field | PDP | Reden voor vrije tekst; geen duplicaat | HIDE_COMPONENT | PDO | soms | Gebruik beperken na review |
| `media.primary_image` | Primaire afbeelding | media | Hoofdbeeld voor productidentiteit en kaart | BE+VC+LA | reference | 1 | mediareferentie | PUBLICATION_BLOCKER | ALL | SNC/SUP | Shopify productmedia wordt gebruikt | native | PDP,CARD,SEARCH,SEO,FEED | Bestaand bestand; productmatch; rechten geldig | BLOCK_PUBLICATION | CE | ja | Selectieregel/open rechtenbron |
| `media.additional_images` | Aanvullende afbeeldingen | media | Geordende productbeelden naast hoofdbeeld | BE+VC+LA | list<reference> | 0..* | mediareferenties | RECOMMENDED | ALL | SNC/SUP | Shopify productmedia | native | PDP,SEO,FEED | Uniek; volgorde; productrelevant | HIDE_COMPONENT | CE | ja | Minimum per type open |
| `media.execution_images` | Uitvoeringsmedia | media | Beelden die exact bij kleur/maat/uitvoering horen | BE+VC+LA | list<reference> | 0..* | mediareferenties | TYPE_BLOCKER | SHOWER,FURN,TILE | SNC/SUP | Variantmedia technisch ondersteund | native | PDP,CARD,SWITCH,CONFIG | Referentie hoort bij uitvoering | MANUAL_REVIEW | PDO | ja | Huidig zelfstandig-productmodel meenemen |
| `media.video` | Productvideo | media | Optionele product- of instructievideo | VC+LA | list<reference> | 0..* | video/mediareferentie | OPTIONAL | ALL | SUP/BCE | Theme ondersteunt media | native | PDP,SEO | Toegankelijk, rechten en bron geldig | HIDE_COMPONENT | CE | soms | Hosting/consent open |
| `media.alt_text` | Alternatieve tekst | media | Toegankelijke beschrijving per informatief beeld | BE+VC | string | 1 per beeld | tekst | PUBLICATION_BLOCKER | ALL | SNC/BCE | Theme leest media-alt | native | PDP,CARD,SEO,QA | Niet leeg voor informatief beeld | BLOCK_PUBLICATION | CE | nee | Decoratieve status apart bepalen |
| `media.source` | Mediabron | media | Herkomst of bronhouder van media | VC+LA | reference | 0..1 per media | bron-ID | REQUIRED_WHEN_APPLICABLE | ALL | SUP/BCE | Niet bewezen | custom field | FEED,QA | Bestaande bronreferentie | MANUAL_REVIEW | CE | ja | Bronregister ontbreekt |
| `media.rights_status` | Mediarechtenstatus | media | Bevestigt publicatie-/gebruiksrecht en beperking | VC+BR | enum | 1 per media | gecontroleerde status | PUBLICATION_BLOCKER | ALL | SUP/BCE | Niet bewezen | custom field | PDP,CARD,SEO,FEED,QA | Goedgekeurde status en bewijs | BLOCK_PUBLICATION | PJ | ja | Rechtenbeleid vereist |
| `media.datasheet` | Datasheet | media | Technisch gegevensblad | BE+VC+LA | list<reference> | 0..* | documentreferentie | REQUIRED_WHEN_APPLICABLE | ALL | SUP | Lokaal ontbreekt | metaobject/reference | PDP,FEED | Geldig type, versie en productmatch | HIDE_COMPONENT | PDO | ja | Documentbron en taal open |
| `media.installation_manual` | Montagehandleiding | media | Handleiding voor installatie/montage | BE+VC+LA | list<reference> | 0..* | documentreferentie | REQUIRED_WHEN_APPLICABLE | SAN,SHOWER,FURN,TILE | SUP | Lokaal ontbreekt | metaobject/reference | PDP,FEED | Versie, taal en productmatch | MANUAL_REVIEW | PDO | ja | Wanneer typeblokker open |
| `media.technical_drawing` | Technische tekening | media | Maat-/aansluittekening | BE+VC+LA | list<reference> | 0..* | document/mediareferentie | REQUIRED_WHEN_APPLICABLE | SAN,SHOWER,FURN | SUP | Lokaal ontbreekt | metaobject/reference | PDP,CONFIG,FEED | Versie en modelmatch | HIDE_COMPONENT | PDO | ja | Formaatvereisten open |
| `media.maintenance_guide` | Onderhoudsdocument | media | Downloadbaar onderhoudsvoorschrift | VC+LA | list<reference> | 0..* | documentreferentie | OPTIONAL | ALL | SUP/BCE | Lokaal ontbreekt | metaobject/reference | PDP,FEED | Actueel en productrelevant | HIDE_COMPONENT | CE | ja | Overlap met content.maintenance bewaken |
| `media.safety_compliance_document` | Veiligheids-/conformiteitsdocument | media | Bewijsdocument voor toepasselijke eisen | VC+LA+BR | list<reference> | 0..* | documentreferentie | REQUIRED_WHEN_APPLICABLE | ALL | SUP/BCE | Niet bewezen | metaobject/reference | PDP,FEED,QA | Geldig, actueel, juiste productscope | MANUAL_REVIEW | PJ | ja | Juridische toepasselijkheid vereist |
| `logistics.own_stock_quantity` | Eigen voorraad | logistics | Beschikbare hoeveelheid in eigen beheer volgens goedgekeurde semantiek | BH+VC+BR | integer | 0..1 | stuks | REQUIRED_WHEN_APPLICABLE | ALL | SNC/OPS | Eén locatie; beperkte inventorytracking | native | PDP,CART,LOG,FEED,QA | >=0; locatie en timestamp verplicht | MANUAL_REVIEW | OO | nee | Betekenis available/on_hand open |
| `logistics.supplier_stock_quantity` | Leveranciersvoorraad | logistics | Hoeveelheid bij leverancier volgens bronspecificatie | VC+LA | decimal | 0..1 | bron-eenheid | REQUIRED_WHEN_APPLICABLE | ALL | SUP/EXT | Niet lokaal aanwezig | extern | PDP,CART,LOG,FEED,QA | >=0; bron en actualiteit verplicht | MANUAL_REVIEW | OO | ja | Semantiek per leverancier open |
| `logistics.stock_status` | Voorraadstatus | logistics | Gecontroleerde status, niet automatisch een leverbelofte | BH+VC+BR | enum | 0..1 | gecontroleerde status | PUBLICATION_BLOCKER | ALL | SNC/SUP/OPS/DRV | Asset heeft alleen `available=true` | afgeleid | PDP,CARD,CART,LOG,FEED | Herleidbaar naar bron/timestamp | MANUAL_REVIEW | OO | ja | Statuswaarden en precedence open |
| `logistics.stock_quantity` | Genormaliseerde voorraadhoeveelheid | logistics | Optionele samengevoegde hoeveelheid voor intern gebruik | VC+AF+BR | decimal | 0..1 | verkoop-/voorraadeenheid | OPTIONAL | ALL | DRV | Niet bewezen | afgeleid | LOG,FEED,QA | Alleen met goedgekeurde bronprecedence | ALLOW_EMPTY | OO | ja | Niet klantzichtbaar zonder besluit |
| `logistics.stock_source` | Voorraadbron | logistics | Gezaghebbende bron voor getoonde voorraadstatus | VC+LA+BR | reference | 1 | bron-ID | PUBLICATION_BLOCKER | ALL | SNC/SUP/OPS/EXT | Niet bewezen | extern | LOG,FEED,QA | Bestaand bronbewijs | BLOCK_PUBLICATION | OO | ja | Precedence eigen/leverancier open |
| `logistics.stock_updated_at` | Voorraadactualiteit | logistics | Tijdstip waarop voorraadbron laatst gold | VC+LA | datetime | 0..1 | ISO-8601 | REQUIRED_WHEN_APPLICABLE | ALL | SNC/SUP/EXT | Niet bewezen | custom field | PDP,LOG,FEED,QA | Niet ouder dan later beleid | MANUAL_REVIEW | OO | ja | Stale-drempel open |
| `logistics.lead_time` | Levertijd | logistics | Genormaliseerde duur/bandbreedte zonder verzonnen klanttekst | BE+VC+LA+BR | object | 0..1 | min,max,unit | PUBLICATION_BLOCKER | ALL | SUP/OPS | Huidige vaste PDP-tekst heeft geen bron | custom field | PDP,CARD,CART,LOG,FEED | Niet-negatief; bron/status vereist | MANUAL_REVIEW | OO | ja | Beloftesemantiek per scenario open |
| `logistics.lead_time_type` | Levertijdtype | logistics | Type duur, datum, week of onbekend volgens gecontroleerde semantiek | VC+BR | enum | 0..1 | gecontroleerde status | REQUIRED_WHEN_APPLICABLE | ALL | OPS | Niet bewezen | custom field | PDP,CARD,LOG,FEED | Compatibel met lead_time | MANUAL_REVIEW | OO | soms | Waardelijst open |
| `logistics.cutoff_time` | Bestelcutoff | logistics | Tijdgrens voor een operationeel leverproces | VC+LA+BR | object | 0..1 | tijd+zone+dagen | REQUIRED_WHEN_APPLICABLE | ALL | SUP/OPS | Niet bewezen | extern | PDP,CART,LOG | Geldige tijdzone en kalender | HIDE_COMPONENT | OO | ja | Geen klantbelofte zonder procesbewijs |
| `logistics.backorder_allowed` | Backorder toegestaan | logistics | Of bestellen zonder directe voorraad operationeel mag | VC+BR | boolean | 0..1 | true/false | REQUIRED_WHEN_APPLICABLE | ALL | OPS/COM | Inventory policy bestaat, regels onbekend | native | PDP,CART,LOG,FEED | Expliciete regel; geen null als false | MANUAL_REVIEW | OO | soms | Klantcommunicatie open |
| `logistics.weight` | Productgewicht | logistics | Netto productgewicht | VC+LA | measurement | 0..1 | kg | TYPE_BLOCKER | ALL | SNC/SUP | Shopifygewicht niet geïnventariseerd | native | CART,LOG,FEED | >0 waar verzending gewicht vereist | BLOCK_PUBLICATION | OO | ja | Uitzonderingen per type open |
| `logistics.product_dimensions` | Productafmetingen logistiek | logistics | Buitenmaten relevant voor vervoer/opslag | VC+LA | object | 0..1 | l,b,h+unit | REQUIRED_WHEN_APPLICABLE | ALL | SUP | Niet bewezen | custom field | LOG,FEED | Positief, één eenheidssysteem | MANUAL_REVIEW | OO | ja | Verschil met gebruiksmaatvoering bewaken |
| `logistics.package_dimensions` | Verpakkingsafmetingen | logistics | Buitenmaten van verzendverpakking | VC+LA | object | 0..1 | l,b,h+unit | REQUIRED_WHEN_APPLICABLE | ALL | SUP | Niet bewezen | custom field | CART,LOG,FEED | Positief; pakketnummer indien meerdere | MANUAL_REVIEW | OO | ja | Meerdere dozenmodel open |
| `logistics.package_unit` | Verpakkingseenheid | logistics | Eenheid waarin product fysiek/verkooptechnisch is verpakt | VC+LA | enum | 0..1 | stuk/doos/pallet/anders | REQUIRED_WHEN_APPLICABLE | ALL | SUP/OPS | Niet bewezen | custom field | PDP,CART,CALC,LOG,FEED | Waarde uit catalogus | MANUAL_REVIEW | OO | ja | Verkoop- en verpakkingseenheid scheiden |
| `logistics.package_contents` | Doos-/verpakkingsinhoud | logistics | Aantal of beschrijving van eenheden per verpakking | VC+LA | object | 0..1 | hoeveelheid+eenheid | REQUIRED_WHEN_APPLICABLE | ALL | SUP | Niet bewezen | custom field | PDP,CART,CALC,LOG,FEED | >0; compatibele eenheid | MANUAL_REVIEW | OO | ja | Tegelvelden specifieker |
| `logistics.shipping_class` | Verzendklasse | logistics | Operationele classificatie voor levermethode | VC+BR | reference | 0..1 | klasse-ID | TYPE_BLOCKER | ALL | OPS | Delivery profile bewezen, productmapping niet | metaobject/reference | CART,LOG,FEED | Geldige klasse en regels | BLOCK_PUBLICATION | OO | nee | Klassen/tarieven open |
| `logistics.parcel_eligible` | Pakketgeschikt | logistics | Of pakketverzending operationeel geschikt is | BE+VC+BR | boolean | 0..1 | true/false | REQUIRED_WHEN_APPLICABLE | ALL | OPS/DRV | Niet bewezen | afgeleid | CART,LOG | Herleidbaar naar klasse/maten/gewicht | MANUAL_REVIEW | OO | soms | Drempels open |
| `logistics.pallet_eligible` | Palletgeschikt | logistics | Of palletlevering operationeel geschikt is | BE+VC+BR | boolean | 0..1 | true/false | REQUIRED_WHEN_APPLICABLE | ALL | OPS/DRV | Niet bewezen | afgeleid | CART,LOG | Herleidbaar naar klasse/verpakking | MANUAL_REVIEW | OO | soms | Drempels open |
| `logistics.pickup_eligible` | Afhaalgeschikt | logistics | Of afhalen volgens operationele regels kan | BE+VC+BR | boolean | 0..1 | true/false | REQUIRED_WHEN_APPLICABLE | ALL | OPS | Eén fulfilmentlocatie bewezen | custom field | PDP,CART,LOG | Locatie/proces beschikbaar | HIDE_COMPONENT | OO | nee | Afhaalregels open |
| `logistics.dropship_supplier` | Dropshipleverancier | logistics | Leverancier die fulfilment uitvoert | BE+VC+LA | reference | 0..1 | leverancier-ID | REQUIRED_WHEN_APPLICABLE | ALL | SUP/OPS | Circa 90% als projectverwachting; geen mapping | metaobject/reference | CART,LOG,FEED | Geldige leverancier en route | MANUAL_REVIEW | OO | ja | Feitelijke dekking ontbreekt |
| `logistics.fulfillment_source` | Fulfilmentbron | logistics | Gecontroleerde bron/route voor uitvoering | BE+VC+BR | enum | 1 | eigen/dropship/mixed/undecided | PUBLICATION_BLOCKER | ALL | OPS | Niet bewezen | custom field | CART,LOG,FEED,QA | Goedgekeurde route verplicht | BLOCK_PUBLICATION | OO | soms | Combinatieregels open |
| `logistics.handling_unit_count` | Aantal handlingeenheden | logistics | Aantal pakketten/dozen/pallets voor één verkoopeenheid | VC+LA | integer | 0..1 | eenheden | REQUIRED_WHEN_APPLICABLE | ALL | SUP/OPS | Niet bewezen | custom field | CART,LOG,FEED | Integer >0 | MANUAL_REVIEW | OO | ja | Multi-package model open |
| `service.warranty` | Garantie | service | Goedgekeurde garantieduur en voorwaardenreferentie | BE+VC+LA+BR | object | 0..1 | duur+bron | REQUIRED_WHEN_APPLICABLE | ALL | SUP/BCE | Niet bewezen | metaobject/reference | PDP,SEO,FEED | Bron, duur en scope consistent | MANUAL_REVIEW | PJ | ja | Geen claim zonder beleid |
| `service.return_category` | Retourcategorie | service | Operationele retourklasse | BE+VC+BR | reference | 1 | categorie-ID | PUBLICATION_BLOCKER | ALL | OPS/BCE | Niet bewezen | metaobject/reference | PDP,CART,FEED | Geldige beleidsreferentie | BLOCK_PUBLICATION | OO | soms | Beleid en uitzonderingen open |
| `service.return_exceptions` | Retouruitzonderingen | service | Productgerichte uitzonderingen op retourbeleid | VC+BR | list<reference> | 0..* | regelreferenties | REQUIRED_WHEN_APPLICABLE | ALL | OPS/BCE | Niet bewezen | metaobject/reference | PDP,CART | Niet conflicterend; juridisch goedgekeurd | MANUAL_REVIEW | PJ | soms | Open beleidsbesluit |
| `service.service_process` | Serviceproces | service | Route voor service, defect of vraag | BE+VC+BR | reference | 0..1 | proces-ID | RECOMMENDED | ALL | OPS/BCE | Niet bewezen | metaobject/reference | PDP | Bestaand en bereikbaar proces | HIDE_COMPONENT | OO | nee | Procesontwerp open |
| `service.quality_marks` | Keurmerken | service | Gecontroleerde keurmerken met bewijs | VC+LA | list<reference> | 0..* | keurmerk-ID | REQUIRED_WHEN_APPLICABLE | ALL | SUP/BCE | `belgaqua_keurmerk` verwacht; dekking onbekend | metaobject/reference | PDP,FILTER,SEO,FEED | Geldig certificaat/productscope | HIDE_COMPONENT | PJ | ja | Waardelijst/rechten open |
| `service.certificates` | Certificaten | service | Certificaatrecords met nummer, geldigheid en document | VC+LA | list<object> | 0..* | type,nummer,datum,document | REQUIRED_WHEN_APPLICABLE | ALL | SUP/BCE | Niet bewezen | metaobject/reference | PDP,FEED,QA | Niet verlopen; productmatch | MANUAL_REVIEW | PJ | ja | Juridische vereisten per type open |
| `service.maintenance_requirements` | Onderhoudseisen | service | Verplichte onderhoudshandelingen voor garantie/veiligheid | VC+LA+BR | list<reference> | 0..* | regelreferenties | REQUIRED_WHEN_APPLICABLE | ALL | SUP/BCE | Niet bewezen | metaobject/reference | PDP,FEED | Bron en toepasselijkheid verplicht | MANUAL_REVIEW | PJ | ja | Tekst en document niet dupliceren |
| `service.spare_parts` | Reserveonderdelen | service | Geldige relaties naar beschikbare onderdelen | BE+VC+LA | list<reference> | 0..* | productreferenties | REQUIRED_WHEN_APPLICABLE | SAN,SHOWER,FURN | SUP/BCE | Kraanonderdelen bestaan; relaties niet bewezen | metaobject/reference | PDP,SEARCH,RELATIONS,FEED | Doel bestaat; compatibiliteit bewezen | HIDE_COMPONENT | PDO | ja | Relatierichting later goedkeuren |
| `service.compliance_source` | Compliancebron | service | Gezaghebbende bron voor juridische/conformiteitsclaims | VC+LA+BR | reference | 0..1 | bron-ID | REQUIRED_WHEN_APPLICABLE | ALL | SUP/BCE | Niet bewezen | extern | FEED,QA | Bron en reviewdatum verplicht | MANUAL_REVIEW | PJ | ja | Bevoegde bron per type open |
| `seo.title` | SEO-titel | seo | Zoekresultaattitel, los van producttitel waar nodig | BE+VC | string | 0..1 | tekst | RECOMMENDED | ALL | BCE/DRV | Huidige metadata-uitvoer bestaat | custom field | SEO,FEED | Uniek/passend; lengtegrens later | SHOW_APPROVED_FALLBACK | SEO | nee | Fallbackregel goedkeuren |
| `seo.meta_description` | Metabeschrijving | seo | Zoekresultaatsamenvatting zonder onbewezen claim | BE+VC | string | 0..1 | tekst | RECOMMENDED | ALL | BCE/DRV | Metadata-uitvoer bestaat; bronwaarden niet geïnventariseerd | custom field | SEO,FEED | Uniek/passend; lengtegrens later | SHOW_APPROVED_FALLBACK | SEO | nee | Fallbackregel goedkeuren |
| `seo.canonical_identity` | Canonical-identiteit | seo | Logische voorkeursidentiteit voor duplicate routes | BE+VC+OB | reference | 1 | product/route-ID | PUBLICATION_BLOCKER | ALL | SNC/BCE | Canonicaluitvoer in theme | native | SEO,QA | Geldig, zelf/voorkeursobject, geen lus | BLOCK_PUBLICATION | SEO | nee | URL-/routebeleid open |
| `seo.indexation_category` | Indexatiecategorie | seo | Beleidsklasse voor index/noindex/crawl, geen directe beslissing | VC+BR | enum | 0..1 | gecontroleerde klasse | RECOMMENDED | ALL | BCE | Geen productbrede inventaris | custom field | SEO,QA | Waarde uit later beleid | MANUAL_REVIEW | SEO | nee | Indexatiebesluit open |
| `seo.search_terms` | Zoektermen en synoniemen | seo | Beheerde termen voor interne vindbaarheid | BE+VC | list<string> | 0..* | genormaliseerde termen | RECOMMENDED | ALL | BCE/SUP | Niet bewezen | custom field | SEARCH,SEO,FEED | Geen duplicaten/misleiding | ALLOW_EMPTY | SEO | soms | Zoekengine en taalregels open |
| `seo.breadcrumb_context` | Breadcrumbcontext | seo | Voorkeurscontext voor navigatie en structured data | BE+VC+OB | reference | 0..1 | categorie-ID | RECOMMENDED | ALL | BCE | Breadcrumbs bestaan; doel-IA open | metaobject/reference | PDP,SEO | Geldige hiërarchie; geen lus | SHOW_APPROVED_FALLBACK | SEO | nee | Categorieboom open |
| `seo.taxonomy_terms` | Merk-/serie-/typetermen | seo | Afgeleide entiteitstermen voor consistente vindbaarheid | AF+VC | list<string> | 0..* | termen | RECOMMENDED | ALL | DRV | Brand/type huidige velden | afgeleid | SEARCH,SEO,FEED | Alleen uit goedgekeurde entiteiten | ALLOW_EMPTY | SEO | nee | Geen keyword stuffing |
| `seo.internal_links` | Interne-linkrelaties | seo | Beheerde links naar categorie, merk, serie, advies en begrippen | BE+VC | list<reference> | 0..* | route/content-ID | RECOMMENDED | ALL | BCE/DRV | Theme heeft links/placeholders | metaobject/reference | PDP,SEO | Doel bestaat; geen `#`; relevant | HIDE_COMPONENT | SEO | nee | IA/contentregels open |
| `seo.structured_data_eligibility` | Structured-datarelevantie | seo | Welke gevalideerde velden voor productdata-uitvoer mogen worden gebruikt | BE+VC+AF | object | 1 | gate-uitkomsten | PUBLICATION_BLOCKER | ALL | DRV | Product structured data bestaat | afgeleid | SEO,QA | Alleen consistente prijs/voorraad/ID | BLOCK_PUBLICATION | SEO | nee | Schema-inhoud later technisch valideren |
| `relation.variation` | Uitvoeringsrelatie | relation | Gerichte relatie tussen zelfstandige uitvoeringen | BE+VC+LA | list<reference> | 0..* | productreferenties | REQUIRED_WHEN_APPLICABLE | ALL | SUP/BCE | V2 asset bewijst gegroepeerde uitvoeringen | metaobject/reference | PDP,SWITCH,CONFIG,SEO,FEED | Doel bestaat; niet zelf; type gelijk | HIDE_COMPONENT | PDO | ja | Bronarchitectuur open |
| `relation.switch_group` | Switchergroep | relation | Stabiele groep voor producten die via keuzes navigeren | BH+VC+LA | reference | 0..1 | groep-ID | TYPE_BLOCKER | SHOWER,FURN | ECC/SUP | `custom.switch_group` 3.658; asset 433 groepen | metaobject/reference | PDP,SWITCH,CONFIG,FEED,QA | Groep bestaat; product één keer | BLOCK_PUBLICATION | PDO | ja | Definitieve bron later besluiten |
| `relation.accessories` | Accessoires | relation | Optionele passende accessoires | BE+VC+LA | list<reference> | 0..* | productreferenties | RECOMMENDED | ALL | SUP/BCE | Niet bewezen | metaobject/reference | PDP,CART,SEO | Doel bestaat; compatibiliteit | HIDE_COMPONENT | PDO | ja | Richting wederkerig of niet open |
| `relation.required_add_ons` | Noodzakelijke aanvullende artikelen | relation | Artikelen noodzakelijk voor correcte installatie/werking | BE+VC+LA+BR | list<reference> | 0..* | productreferenties | REQUIRED_WHEN_APPLICABLE | ALL | SUP/BCE | Niet bewezen | metaobject/reference | PDP,CART,CONFIG | Doel actief; reden en compatibiliteit | MANUAL_REVIEW | PDO | ja | Koop-/cartgedrag open |
| `relation.recommended_add_ons` | Aanbevolen aanvullende artikelen | relation | Niet-verplichte passende aanvulling | BE+VC | list<reference> | 0..* | productreferenties | RECOMMENDED | ALL | BCE/SUP | Related sections bestaan | metaobject/reference | PDP,CART | Doel actief; geen duplicaat | HIDE_COMPONENT | CO | soms | Merchandisingbeleid open |
| `relation.components` | Onderdelen | relation | Producten die onderdeel zijn van dit product/set | BE+VC+LA | list<reference> | 0..* | productreferenties | REQUIRED_WHEN_APPLICABLE | SAN,SHOWER,FURN,SET | SUP/BCE | Kraanonderdelen/productsets aanwezig | metaobject/reference | PDP,CONFIG,FEED | Geen cyclus; doel bestaat | HIDE_COMPONENT | PDO | ja | Setsemantiek open |
| `relation.replacement` | Vervangend product | relation | Opvolger die huidig product vervangt | VC+BR | reference | 0..1 | productreferentie | REQUIRED_WHEN_APPLICABLE | ALL | BCE/COM | Niet bewezen | metaobject/reference | PDP,SEARCH,SEO | Doel actief; geen lus | SHOW_APPROVED_FALLBACK | CO | nee | Redirect-/weergavebeleid open |
| `relation.alternatives` | Alternatieven | relation | Vergelijkbare producten zonder beter-claim | BE+VC | list<reference> | 0..* | productreferenties | RECOMMENDED | ALL | BCE/DRV | Related producten bestaan; bedoeling open | metaobject/reference | PDP,SEARCH | Doel actief; relevante criteria | HIDE_COMPONENT | CO | nee | Selectieregel open |
| `relation.upsell` | Betere optie/upsell | relation | Commercieel gekozen alternatief met controleerbare reden | VC+BR | list<reference> | 0..* | productreferenties | OPTIONAL | ALL | COM | Niet bewezen | metaobject/reference | PDP,CART | Doel actief; reden verplicht | HIDE_COMPONENT | CO | nee | Claim- en prijsregels open |
| `relation.related_products` | Gerelateerde producten | relation | Algemene inhoudelijk relevante relaties | BH+VC | list<reference> | 0..* | productreferenties | RECOMMENDED | ALL | BCE/DRV | Actieve related-products section | metaobject/reference | PDP,SEO | Geen zelf/duplicaten; doel actief | HIDE_COMPONENT | PDO | nee | Bron en ranking open |
| `relation.series_members` | Serieleden | relation | Andere producten binnen dezelfde serie | VC+AF | list<reference> | 0..* | productreferenties | RECOMMENDED | ALL | DRV | Serieveldwaarden niet bewezen | afgeleid | PDP,SEARCH,SEO | Zelfde geldige serie; geen zelf | HIDE_COMPONENT | PDO | soms | Pas na seriecatalogus |
| `relation.bundle_set` | Set-/combinatierelatie | relation | Conceptuele set van producten; geen cartbundelbesluit | BE+VC+BR | list<reference> | 0..* | productreferenties | FUTURE | SET | BCE/COM | Complete set toekomstig | metaobject/reference | CONFIG,CART,FEED | Doelen bestaan; prijs/logistiek apart | MANUAL_REVIEW | PO | soms | Bundeling en scope open |
| `relation.parent_child` | Parent/childrelatie | relation | Alleen voor bewezen hiërarchie die niet door uitvoering/onderdeel wordt gedekt | VC+OB | object | 0..1 | richting+referentie | FUTURE | ALL | UND | Niet bewezen | undecided | FEED,QA | Geen cyclus; semantiek verplicht | MANUAL_REVIEW | PDO | ja | Alleen invoeren na architectuurbesluit |
| `switcher.product_reference` | Switcherproductkoppeling | switcher | Stabiele verwijzing van combinatie naar bestaand product | BH+BE+VC+LA | reference | 1 per lid | product-ID; URL/SKU hulpmiddel | TYPE_BLOCKER | SHOWER,FURN | ECC/SUP | Asset gebruikt handle/URL; handle intern uniek | metaobject/reference | SWITCH,CONFIG,QA | Doel bestaat; exact één uitvoering | BLOCK_PUBLICATION | TO | ja | Definitieve sleutel open |
| `switcher.axis_key` | Keuze-as-key | switcher | Technische, canonieke key van een keuze-as | BH+VC+LA | string | 1..* per groep | lowercase underscore | TYPE_BLOCKER | SHOWER,FURN | ECC/SUP/BCE | 30 V2 optionkeys | custom field | SWITCH,CONFIG,FEED,QA | Uniek per groep; contractkeymatch | BLOCK_PUBLICATION | PDO | ja | Assen per producttype open |
| `switcher.axis_label` | Keuze-as-label | switcher | Klantgericht label bij technische as | BH+VC | string | 1 per as | tekst | TYPE_BLOCKER | SHOWER,FURN | ECC/SUP/BCE | V2 menu labels | custom field | SWITCH,CONFIG | Niet leeg; taal/context klopt | BLOCK_PUBLICATION | CE | soms | Vertaal-/labelbeheer open |
| `switcher.allowed_values` | Toegestane waarden | switcher | Gecontroleerde waarden per as en groep | BH+VC+LA | list<string> | 1..* per as | waardecodes/labels | TYPE_BLOCKER | SHOWER,FURN | ECC/SUP | V2 `menus[].values` | metaobject/reference | SWITCH,CONFIG,FEED,QA | Uniek; elke productwaarde toegestaan | BLOCK_PUBLICATION | PDO | ja | Code versus label later scheiden |
| `switcher.value_order` | Waardevolgorde | switcher | Bewuste sorteervolgorde van waarden | BH+VC | list<string> | 0..1 per as | waardecodes | RECOMMENDED | SHOWER,FURN | ECC/BCE | V2 values/order | custom field | SWITCH,CONFIG | Exact dezelfde waardeset | SHOW_APPROVED_FALLBACK | CE | soms | Standaardsortering open |
| `switcher.presentation` | Presentatievorm | switcher | Buttons, dropdown of later goedgekeurde control | BH+VC+OB | enum | 1 per as | gecontroleerde waarde | RECOMMENDED | SHOWER,FURN | ECC/BCE | V2 buttons/dropdown/auto | custom field | SWITCH,CONFIG | Waarde toegestaan; UX later testen | SHOW_APPROVED_FALLBACK | PO | nee | Geen designbesluit in contract |
| `switcher.combination_signature` | Combinatiesignatuur | switcher | Canonieke set as=waarde voor één groepslid | BH+VC+AF | string | 1 per lid | gesorteerde key/value-paren | TYPE_BLOCKER | SHOWER,FURN | DRV | V2 combinaties intern uniek | afgeleid | SWITCH,CONFIG,QA | Uniek binnen groep | BLOCK_PUBLICATION | TO | ja | Canonicalisatie later specificeren |
| `switcher.combination_validity` | Combinatiegeldigheid | switcher | Of combinatie inhoudelijk geldig is | BH+VC+LA | enum | 1 per combinatie | valid/invalid/unknown | TYPE_BLOCKER | SHOWER,FURN | SUP/DRV | V2 disabled/partial-matchlogica | afgeleid | SWITCH,CONFIG,QA | Geen `unknown` bij publicatie | BLOCK_PUBLICATION | PDO | ja | Bron van ongeldigheid open |
| `switcher.option_availability` | Optiebeschikbaarheid | switcher | Beschikbaarheid van keuze zonder voorraadbelofte te vervangen | BH+VC+LA | enum | 0..1 per waarde | status | REQUIRED_WHEN_APPLICABLE | SHOWER,FURN | SUP/DRV | Asset heeft alleen product `available` | afgeleid | SWITCH,CONFIG | Herleidbaar; tijdstip bekend | MANUAL_REVIEW | OO | ja | Scheiding combinatie/voorraad open |
| `switcher.fallback_policy` | Switcherfallback | switcher | Goedgekeurd gedrag bij ontbrekende of ongeldige data | VC+BR | enum | 1 per groep | hide/manual/approved fallback | TYPE_BLOCKER | SHOWER,FURN | BCE/OPS | V2 verbergt bij fouten; legacy bestaat | custom field | SWITCH,CONFIG,QA | Geen verkeerde navigatie/claim | BLOCK_PUBLICATION | PO | nee | Legacybehoud en UX open |
| `switcher.snapshot_version` | Switcherversie/snapshot | switcher | Versie en moment van groepsdata | BH+VC+LA | object | 1 per dataset | version+datetime | TYPE_BLOCKER | SHOWER,FURN | ECC/SUP | Asset `version`,`generated_at` | custom field | SWITCH,CONFIG,FEED,QA | Geldig; herleidbaar naar bron | BLOCK_PUBLICATION | TO | ja | Generator ontbreekt |
| `switcher.source_owner` | Switcherbronhouder | switcher | Rol/organisatie verantwoordelijk voor groepsbron | VC+LA+OB | reference | 1 per dataset | eigenaar-ID | TYPE_BLOCKER | SHOWER,FURN | SUP/BCE | Onbekend | metaobject/reference | FEED,QA | Bestaande bevoegde eigenaar | BLOCK_PUBLICATION | PO | ja | Moet vóór architectuurbesluit |
| `switcher.validation_status` | Switchervalidatiestatus | switcher | Uitkomst van groep-, product- en combinatieregels | VC+AF | enum | 1 per groep | gecontroleerde status | TYPE_BLOCKER | SHOWER,FURN | DRV | Asset intern deels gevalideerd | afgeleid | SWITCH,CONFIG,QA | Alleen uit vastgelegde tests | BLOCK_PUBLICATION | TO | ja | Volledige Adminvergelijking ontbreekt |
| `tile.order_unit` | Verkoop-/besteleenheid | tile | Eenheid waarin klant tegel bestelt | BE+VC+LA+BR | enum | 1 | stuk/doos/m² | TYPE_BLOCKER | TILE | SUP/COM/OPS | Niet bewezen | custom field | PDP,CALC,CART,LOG,FEED | Waarde uit goedgekeurde set | BLOCK_PUBLICATION | CO | ja | Eenheid en cartgedrag open |
| `tile.price_basis` | Prijsbasis | tile | Basis waarop getoonde tegelprijs berust | BE+VC+LA+BR | enum | 1 | stuk/doos/m² | TYPE_BLOCKER | TILE | SUP/COM | Niet bewezen | custom field | PDP,CARD,CALC,CART,FEED | Compatibel met order_unit en prijzen | BLOCK_PUBLICATION | CO | ja | Commerciële regel vereist |
| `tile.square_meters_per_box` | Vierkante meter per doos | tile | Dekkende oppervlakte van één doos | BE+VC+LA | decimal | 1 | m²/doos | TYPE_BLOCKER | TILE | SUP | Niet bewezen | custom field | PDP,CALC,CART,LOG,FEED | >0; precisie en bron verplicht | BLOCK_PUBLICATION | PDO | ja | Leveranciersdata nodig |
| `tile.pieces_per_box` | Stuks per doos | tile | Aantal tegels in één volle doos | BE+VC+LA | integer | 1 | stuks/doos | TYPE_BLOCKER | TILE | SUP | Niet bewezen | custom field | PDP,CALC,CART,LOG,FEED | Integer >0 | BLOCK_PUBLICATION | PDO | ja | Leveranciersdata nodig |
| `tile.pieces_per_square_meter` | Stuks per vierkante meter | tile | Afgeleide of aangeleverde hoeveelheid voor één m² | VC+LA+AF | decimal | 0..1 | stuks/m² | RECOMMENDED | TILE | SUP/DRV | Niet bewezen | afgeleid | PDP,CALC,FEED | >0; consistent met tegelmaat | MANUAL_REVIEW | PDO | ja | Voegbreedte/afronding open |
| `tile.width` | Tegelbreedte | tile | Nominale breedte van één tegel | BE+VC+LA | measurement | 1 | mm | TYPE_BLOCKER | TILE | SUP | Niet bewezen | custom field | PDP,FILTER,CALC,LOG,FEED | >0; expliciete unit | BLOCK_PUBLICATION | PDO | ja | Nominaal versus werkelijk open |
| `tile.length` | Tegellengte | tile | Nominale lengte van één tegel | BE+VC+LA | measurement | 1 | mm | TYPE_BLOCKER | TILE | SUP | Niet bewezen | custom field | PDP,FILTER,CALC,LOG,FEED | >0; expliciete unit | BLOCK_PUBLICATION | PDO | ja | Nominaal versus werkelijk open |
| `tile.thickness` | Tegeldikte | tile | Nominale dikte van één tegel | VC+LA | measurement | 0..1 | mm | REQUIRED_WHEN_APPLICABLE | TILE | SUP | Niet bewezen | custom field | PDP,FILTER,LOG,FEED | >0; expliciete unit | HIDE_COMPONENT | PDO | ja | Toepasselijkheid open |
| `tile.box_weight` | Doosgewicht | tile | Bruto gewicht van één verkoopdoos | BE+VC+LA | measurement | 1 | kg/doos | TYPE_BLOCKER | TILE | SUP | Niet bewezen | custom field | CART,LOG,FEED | >0; sluit aan op doos | BLOCK_PUBLICATION | OO | ja | Leveranciersdata nodig |
| `tile.pallet_information` | Palletinformatie | tile | Aantallen/gewicht/maten voor palletfulfilment | BE+VC+LA | object | 0..1 | dozen,stuks,kg,maten | REQUIRED_WHEN_APPLICABLE | TILE | SUP/OPS | Niet bewezen | custom field | CART,LOG,FEED | Positief en onderling consistent | MANUAL_REVIEW | OO | ja | Pallettype/limieten open |
| `tile.minimum_order_quantity` | Minimale bestelhoeveelheid | tile | Kleinste toegestane bestelbare hoeveelheid | BE+VC+LA+BR | decimal | 1 | order_unit | TYPE_BLOCKER | TILE | SUP/COM/OPS | Niet bewezen | custom field | PDP,CALC,CART,FEED | >0; veelvoudregel bekend | BLOCK_PUBLICATION | CO | ja | Bron versus bedrijfsregel open |
| `tile.full_boxes_required` | Hele dozen verplicht | tile | Of aantal altijd naar volledige dozen moet | BE+VC+BR | boolean | 1 | true/false | TYPE_BLOCKER | TILE | COM/OPS | Bevestigde calculatorbehoefte, regel open | custom field | PDP,CALC,CART | Expliciete waarde verplicht | BLOCK_PUBLICATION | CO | nee | Menselijk besluit nodig |
| `tile.cutting_loss_default` | Standaard snijverlies | tile | Voorgesteld standaardpercentage voor calculator | BE+VC+BR | decimal | 0..1 | procent | TYPE_BLOCKER | TILE | COM/OPS | Geen waarde bewezen | custom field | CALC,CART | 0..100; waarde menselijk goedgekeurd | MANUAL_REVIEW | PO | nee | Geen percentage verzinnen |
| `tile.cutting_loss_adjustable` | Snijverlies aanpasbaar | tile | Of klant standaardpercentage mag wijzigen | BE+VC+BR | boolean | 1 | true/false | TYPE_BLOCKER | TILE | COM/OPS | Regel niet besloten | custom field | CALC | Expliciete waarde; grenzen apart | MANUAL_REVIEW | PO | nee | UX-/businessbesluit open |
| `tile.rounding_rule` | Afrondingsregel | tile | Goedgekeurde omzetting naar bestelbare hele eenheden | BE+VC+BR | enum | 1 | gecontroleerde regel | TYPE_BLOCKER | TILE | COM/OPS | Niet bewezen | custom field | CALC,CART,QA | Deterministisch; testvoorbeelden | BLOCK_PUBLICATION | OO | nee | Geen regel verzinnen |
| `tile.stock_source` | Tegelvoorraad-/leverbron | tile | Bron specifiek voor doos-/partijbeschikbaarheid | VC+LA+BR | reference | 1 | bron-ID | TYPE_BLOCKER | TILE | SUP/OPS | Niet bewezen | extern | PDP,CART,LOG,FEED | Actueel; verpakkingseenheid gelijk | BLOCK_PUBLICATION | OO | ja | Partij/kleurtoon mogelijk later |
| `tile.sample_eligible` | Samplegeschikt | tile | Of tegel volgens goedgekeurd proces als sample kan | BE+VC+BR | boolean | 0..1 | true/false | REQUIRED_WHEN_APPLICABLE | TILE | COM/OPS | Samples zijn scope; productregels ontbreken | custom field | PDP,CART | Proces/prijs/voorraad beschikbaar | HIDE_COMPONENT | CO | soms | Sampleproces open |
| `tile.calculator_eligible` | Calculatorgeschikt | tile | Of alle calculatorblokkerende data geldig is | BE+VC+AF | boolean | 1 | true/false | TYPE_BLOCKER | TILE | DRV | Calculator is eis; data ontbreekt | afgeleid | PDP,CALC,QA | Waar alleen als alle typegates slagen | BLOCK_PUBLICATION | TO | ja | Geen bewijs voor huidige producten |
| `shower_config.system_type` | Douchesysteemtype | shower_config | Algemeen type doucheset voor keuzecontext | BE+VC+LA | enum | 0..1 | gecontroleerde waarde | TYPE_BLOCKER | SHOWER | SUP/BCE | Huidige producttypes/V2 `type` als afgeleid bewijs | custom field | PDP,FILTER,SWITCH,CONFIG | Waarde uit typecatalogus | BLOCK_PUBLICATION | PDO | ja | Definitieve as open |
| `shower_config.mounting` | Douchesetmontage | shower_config | Inbouw/opbouw of andere gecontroleerde plaatsing | BE+VC+LA | enum | 0..1 | gecontroleerde waarde | TYPE_BLOCKER | SHOWER | SUP | Huidige producttypes/themevelden | custom field | PDP,FILTER,SWITCH,CONFIG | Waarde uit catalogus | BLOCK_PUBLICATION | PDO | ja | Definitieve as open |
| `shower_config.head_shower_size` | Hoofddouchemaat | shower_config | Diameter/breedte als getypeerde meetwaarde | BH+VC+LA | measurement | 0..1 | mm | REQUIRED_WHEN_APPLICABLE | SHOWER | SUP | V2/theme maatkeys | custom field | PDP,FILTER,SWITCH,CONFIG | >0; unit verplicht | MANUAL_REVIEW | PDO | ja | Breedte versus diameter modelleren |
| `shower_config.head_shower_shape` | Hoofddouchevorm | shower_config | Gecontroleerde vorm van hoofddouche | BH+VC+LA | enum | 0..1 | gecontroleerde waarde | REQUIRED_WHEN_APPLICABLE | SHOWER | SUP | V2/theme `vorm` | custom field | PDP,FILTER,SWITCH,CONFIG | Waarde uit catalogus | HIDE_COMPONENT | PDO | ja | Relatie met algemene vorm open |
| `shower_config.arm_type` | Douchearmtype | shower_config | Wand/plafond/anders als mogelijke keuze-as | BH+VC+LA | enum | 0..1 | gecontroleerde waarde | REQUIRED_WHEN_APPLICABLE | SHOWER | SUP | V2 `type_bevestiging_hoofddouche` | custom field | PDP,SWITCH,CONFIG | Waarde uit catalogus | HIDE_COMPONENT | PDO | ja | Definitieve as niet gekozen |
| `shower_config.hand_shower_type` | Handdouchetype | shower_config | Type handdouche als mogelijke keuze-as | BH+VC+LA | enum | 0..1 | gecontroleerde waarde | REQUIRED_WHEN_APPLICABLE | SHOWER | SUP | V2 `type_handdouche` | custom field | PDP,SWITCH,CONFIG | Waarde uit catalogus | HIDE_COMPONENT | PDO | ja | Leveranciersdekking nodig |
| `shower_config.rail_present` | Glijstang aanwezig | shower_config | Of doucheset een glijstang bevat | BH+VC+LA | boolean | 0..1 | true/false | REQUIRED_WHEN_APPLICABLE | SHOWER | SUP | V2/theme `met_glijstang` | custom field | PDP,SWITCH,CONFIG | Boolean; null niet als false | HIDE_COMPONENT | PDO | ja | Inbegrepen versus eigenschap bewaken |
| `shower_config.spout_present` | Uitloop aanwezig | shower_config | Of doucheset/badmengkraan een uitloop bevat | BH+VC+LA | boolean | 0..1 | true/false | REQUIRED_WHEN_APPLICABLE | SHOWER | SUP | V2 `met_uitloop` | custom field | PDP,SWITCH,CONFIG | Boolean; null niet als false | HIDE_COMPONENT | PDO | ja | Producttypescope open |
| `shower_config.outlet_count` | Aantal uitgangen | shower_config | Aantal wateruitgangen of tegelijk bedienbare uitgangen | BH+VC+LA | integer | 0..1 | stuks | REQUIRED_WHEN_APPLICABLE | SHOWER | SUP | Theme verwacht uitgangsveld | custom field | PDP,FILTER,CONFIG | Integer >=1 | MANUAL_REVIEW | PDO | ja | Exacte betekenis per bron open |
| `shower_config.finish` | Douchesetafwerking | shower_config | Configuratorwaarde die verwijst naar canonieke afwerking/kleur | BH+VC+LA | reference | 0..1 | specificatiereferentie | TYPE_BLOCKER | SHOWER | SUP | V2 kleur dominant | metaobject/reference | SWITCH,CONFIG | Verwijst naar geldige kleur/afwerking | BLOCK_PUBLICATION | PDO | ja | Geen dubbele opslagwaarde |
| `furniture_config.width` | Meubelbreedte | furniture_config | Totale nominale breedte van meubelopstelling | VC+LA | measurement | 0..1 | mm | TYPE_BLOCKER | FURN | SUP | Geen brondekking bewezen | custom field | PDP,FILTER,SWITCH,CONFIG,LOG | >0; unit verplicht | BLOCK_PUBLICATION | PDO | ja | Definitieve keuze-as open |
| `furniture_config.configuration` | Meubelopstelling | furniture_config | Onderkast/wastafel/set-opbouw als gecontroleerde configuratie | VC+LA | enum | 0..1 | gecontroleerde waarde | TYPE_BLOCKER | FURN | SUP | Niet bewezen | custom field | PDP,FILTER,SWITCH,CONFIG | Waarde uit catalogus | BLOCK_PUBLICATION | PDO | ja | Taxonomie open |
| `furniture_config.drawer_count` | Aantal laden | furniture_config | Aantal functionele laden | VC+LA | integer | 0..1 | stuks | REQUIRED_WHEN_APPLICABLE | FURN | SUP | Niet bewezen | custom field | PDP,FILTER,SWITCH,CONFIG | Integer >=0 | HIDE_COMPONENT | PDO | ja | Null versus nul bewaken |
| `furniture_config.door_count` | Aantal deuren | furniture_config | Aantal functionele deuren | VC+LA | integer | 0..1 | stuks | REQUIRED_WHEN_APPLICABLE | FURN | SUP | Niet bewezen | custom field | PDP,FILTER,SWITCH,CONFIG | Integer >=0 | HIDE_COMPONENT | PDO | ja | Null versus nul bewaken |
| `furniture_config.basin_type` | Wastafeltype | furniture_config | Type geïntegreerde/losse wastafel of blad | VC+LA | enum | 0..1 | gecontroleerde waarde | TYPE_BLOCKER | FURN | SUP | Niet bewezen | custom field | PDP,FILTER,SWITCH,CONFIG | Waarde uit catalogus | BLOCK_PUBLICATION | PDO | ja | Definitieve as open |
| `furniture_config.basin_count` | Aantal kommen | furniture_config | Aantal wastafelkommen | VC+LA | integer | 0..1 | stuks | REQUIRED_WHEN_APPLICABLE | FURN | SUP | Niet bewezen | custom field | PDP,FILTER,SWITCH,CONFIG | Integer >=0 | HIDE_COMPONENT | PDO | ja | Blad zonder kom mogelijk |
| `furniture_config.tap_hole_count` | Aantal kraangaten | furniture_config | Aantal voorbereide kraangaten | VC+LA | integer | 0..1 | stuks | REQUIRED_WHEN_APPLICABLE | FURN | SUP | Niet bewezen | custom field | PDP,FILTER,SWITCH,CONFIG | Integer >=0 | HIDE_COMPONENT | PDO | ja | Ongeboord/keuze apart modelleren |
| `furniture_config.color` | Meubelkleur | furniture_config | Verwijzing naar canonieke specifieke kleur | VC+LA | reference | 0..1 | kleurreferentie | TYPE_BLOCKER | FURN | SUP | Geen meubelbron | metaobject/reference | PDP,CARD,FILTER,SWITCH,CONFIG | Geldige kleurreferentie | BLOCK_PUBLICATION | PDO | ja | Definitieve as open |
| `furniture_config.finish` | Meubelafwerking | furniture_config | Verwijzing naar canonieke afwerking | VC+LA | reference | 0..1 | afwerkingsreferentie | REQUIRED_WHEN_APPLICABLE | FURN | SUP | Niet bewezen | metaobject/reference | PDP,FILTER,SWITCH,CONFIG | Geldige afwerkingsreferentie | HIDE_COMPONENT | PDO | ja | Kleur/afwerking scheiden |
| `furniture_config.material` | Meubelmateriaal | furniture_config | Verwijzing naar canoniek materiaal | VC+LA | reference | 0..1 | materiaalreferentie | REQUIRED_WHEN_APPLICABLE | FURN | SUP | Niet bewezen | metaobject/reference | PDP,FILTER,CONFIG | Geldige materiaalreferentie | HIDE_COMPONENT | PDO | ja | Hoofd-/frontmateriaal open |
| `furniture_config.placement` | Meubelplaatsing | furniture_config | Hangend, staand of andere gecontroleerde plaatsing | VC+LA | enum | 0..1 | gecontroleerde waarde | TYPE_BLOCKER | FURN | SUP | Niet bewezen | custom field | PDP,FILTER,SWITCH,CONFIG | Waarde uit catalogus | BLOCK_PUBLICATION | PDO | ja | Definitieve as open |
| `furniture_config.handle_operation` | Handgreep/bediening | furniture_config | Greep, greeploos of bedieningsvorm | VC+LA | enum | 0..1 | gecontroleerde waarde | REQUIRED_WHEN_APPLICABLE | FURN | SUP | Niet bewezen | custom field | PDP,FILTER,SWITCH,CONFIG | Waarde uit catalogus | HIDE_COMPONENT | PDO | ja | Terminologie open |
| `furniture_config.mirror_relations` | Spiegelrelaties | furniture_config | Passende spiegel- of spiegelkastproducten | BE+VC+LA | list<reference> | 0..* | productreferenties | REQUIRED_WHEN_APPLICABLE | FURN | SUP/BCE | Niet bewezen | metaobject/reference | PDP,CONFIG,CART | Doel bestaat; maatcompatibel | HIDE_COMPONENT | PDO | ja | Vereist versus aanbevolen scheiden |
| `furniture_config.tall_cabinet_relations` | Kolomkastrelaties | furniture_config | Passende hoge/kolomkasten | BE+VC+LA | list<reference> | 0..* | productreferenties | OPTIONAL | FURN | SUP/BCE | Niet bewezen | metaobject/reference | PDP,CONFIG,CART | Doel bestaat; serie/afwerking matcht | HIDE_COMPONENT | PDO | ja | Merchandising versus compatibiliteit |
| `quality.core_identity_ready` | Gate kernidentiteit | quality | Afgeleide status van identiteit/provenanceblokkers | VC+AF | boolean | 1 | true/false | PUBLICATION_BLOCKER | ALL | DRV | Niet bestaand | afgeleid | QA,FEED | Alle onderliggende harde checks slagen | BLOCK_PUBLICATION | PDO | nee | Drempels menselijk goedkeuren |
| `quality.commercial_ready` | Gate commercie | quality | Afgeleide status van prijs, valuta, belasting en bron | VC+AF | boolean | 1 | true/false | PUBLICATION_BLOCKER | ALL | DRV | Niet bestaand | afgeleid | QA,FEED | Alle commerciële blokkers slagen | BLOCK_PUBLICATION | CO | soms | Drempels menselijk goedkeuren |
| `quality.content_ready` | Gate content | quality | Afgeleide status van verplichte productinhoud | VC+AF | boolean | 1 | true/false | PUBLICATION_BLOCKER | ALL | DRV | Niet bestaand | afgeleid | QA,FEED | Contentblokkades en claims slagen | BLOCK_PUBLICATION | CE | soms | Minimum per type open |
| `quality.media_ready` | Gate media | quality | Afgeleide status van hoofdbeeld, alttekst en rechten | VC+AF | boolean | 1 | true/false | PUBLICATION_BLOCKER | ALL | DRV | Niet bestaand | afgeleid | QA,FEED | Mediaregels slagen | BLOCK_PUBLICATION | CE | soms | Minimum per type open |
| `quality.specifications_ready` | Gate specificaties | quality | Afgeleide status van type-relevante specificaties | VC+AF+LA | boolean | 1 | true/false | TYPE_BLOCKER | ALL | DRV | Niet bestaand | afgeleid | QA,FEED | Typecataloguschecks slagen | BLOCK_PUBLICATION | PDO | ja | Catalogus/brondata ontbreken |
| `quality.logistics_ready` | Gate logistiek | quality | Afgeleide status zonder onbewezen klantbelofte | VC+AF+BR | boolean | 1 | true/false | PUBLICATION_BLOCKER | ALL | DRV | Niet bestaand | afgeleid | QA,FEED,LOG | Bron, actualiteit en fallback goedgekeurd | BLOCK_PUBLICATION | OO | ja | Regels nog niet bewezen |
| `quality.seo_ready` | Gate SEO | quality | Afgeleide status van identiteit, metadata en schema-input | VC+AF | boolean | 1 | true/false | PUBLICATION_BLOCKER | ALL | DRV | Niet bestaand | afgeleid | QA,SEO,FEED | Geen blokkade in canonical/schema | BLOCK_PUBLICATION | SEO | nee | URL/indexatiebeleid open |
| `quality.relations_ready` | Gate relaties | quality | Afgeleide integriteitsstatus van vereiste relaties | VC+AF+LA | boolean | 1 | true/false | REQUIRED_WHEN_APPLICABLE | ALL | DRV | Niet bestaand | afgeleid | QA,FEED | Alle vereiste doelen geldig | MANUAL_REVIEW | PDO | ja | Verplichte relatietypen open |
| `quality.type_specific_ready` | Gate productspecifiek | quality | Afgeleide status van tegel/configuratortypevelden | VC+AF+LA | boolean | 1 | true/false | TYPE_BLOCKER | TILE,SHOWER,FURN | DRV | Niet bestaand | afgeleid | QA,FEED | Alle toepasselijke typeblokkers slagen | BLOCK_PUBLICATION | PDO | ja | Brondata ontbreekt |
| `quality.publishable` | Publiceerbaar | quality | Eindgate: alle toepasselijke goedgekeurde gates slagen | VC+AF+BR | boolean | 1 | true/false | PUBLICATION_BLOCKER | ALL | DRV | Niet bestaand; geen productmutatie | afgeleid | QA,FEED | AND van toepasselijke gates plus goedkeuring | BLOCK_PUBLICATION | PO | ja | Drempels/overridebeleid open |
<!-- CONTRACT_MATRIX_END -->

## 11. Governance en provenance

**VOORGESTELD CONTRACT.** Iedere externe record hoort herleidbaar te zijn tot leverancier, bronsysteem, bronrecord en snapshot. `governance.sync_evidence` koppelt een latere verwerking aan controleerbaar bewijs; `governance.manual_override` voorkomt dat een handmatige wijziging ongemerkt als leverancierwaarde wordt gelezen. Data-eigenaarschap, kwaliteitsstatus en publicatiestatus zijn afzonderlijke begrippen.

**BEWEZEN HUIDIG.** Shopify heeft technische update- en lifecyclevelden. De V2-switcherasset bevat `generated_at`. **NOG ONDERZOEKEN:** er is lokaal geen leverancierregister, importbatchbewijs, overridehistorie of formeel data-eigenaarschap gevonden. Deze governancevelden bewijzen dus geen bestaande data of proces.

## 12. Identiteit

De identiteit van een zelfstandig verkoopbare uitvoering bestaat conceptueel uit een intern product-ID, een eigen SKU, titel, handle, merk, producttype en technische variantreferentie. Leverancierartikelnummer en GTIN zijn aanvullende bronidentifiers, niet automatisch de interne primaire sleutel.

- **BEWEZEN HUIDIG:** 7.827 producten hebben ieder één variant; product-ID, variant-ID, handle, titel, vendor, producttype en SKU zijn native aanwezig. Zeventien SKU's zijn leeg en SKU-dubbelen komen voor. In de V2-asset is handle alleen binnen die asset uniek bewezen.
- **BEVESTIGDE EIS:** zelfstandige uitvoeringen behouden eigen URL en SKU.
- **VOORGESTELD CONTRACT:** `identity.sellable_execution` maakt deze architectuur expliciet en `identity.default_variant_reference` borgt cart-koppelbaarheid.
- **OPEN BESLISSING:** titelbeleid, SKU-normalisatie, merkmodel, serie/modelgrens en producttypetaxonomie.

## 13. Commercie

Klantzichtbare verkoopprijs, eventuele vergelijkprijs en valuta blijven strikt gescheiden van de interne inkoopprijs. Afgeleide korting mag alleen uit een juridisch en commercieel geldige vergelijkprijs worden berekend. Unit-, doos- en vierkantemeterprijs zijn typeafhankelijk en mogen niet zonder goedgekeurde prijsbasis ontstaan.

**BEDRIJFSREGEL VEREIST:** BTW-semantiek, compare-at-betekenis, prijsactualiteit, prijsbron, afronding en zichtbaarheid van interne kosten. **LEVERANCIERAFHANKELIJK:** inkoopprijs en eventuele bronprijzen. Er wordt geen prijsregel of klantbelofte vastgesteld.

## 14. Content

Het contentdomein scheidt korte en lange omschrijving, pluspunten, aandachtspunten, inbegrepen en niet-inbegrepen onderdelen, toepassing, onderhoud, merk-/serie-informatie, FAQ en korte zoek-/kaartspecificaties. Claims en waarschuwingen vragen redactionele of juridische controle.

**BEWEZEN HUIDIG:** body/content en themeconsumenten voor pluspunten, aandachtspunten en korte specificaties bestaan, maar actuele dekking en kwaliteit zijn niet volledig bewezen. **VOORGESTELD CONTRACT:** ontbrekende optionele content verbergt de component; essentiële productinhoud gaat naar handmatige review of blokkeert volgens later goedgekeurde typegates.

## 15. Specificaties

Specificaties worden conceptueel vastgelegd als getypeerde eigenschappen: naam, waarde, datatype, eenheid en waar nodig een gecontroleerde waardelijst. Maatvoering, materiaal, specifieke kleur, basiskleur, afwerking, vorm, montage, booleans, enumeraties, meetwaarden en noodzakelijke vrije tekst zijn afzonderlijke begrippen.

`specification.color` beschrijft de concrete commerciële/technische kleur; `specification.base_color` groepeert die kleur voor bijvoorbeeld filters. Het huidige conflict tussen `kleur` en `basiskleur` mag niet worden opgelost door waarden stilzwijgend uitwisselbaar te maken. Vrije tekst wordt alleen gebruikt wanneer een meetwaarde, boolean, enum of referentie het begrip niet correct kan dragen.

**BEWEZEN HUIDIG:** `custom.specificaties` bestaat als definitie en themeconsument. **NOG ONDERZOEKEN:** de Admin-dekking, interne typestructuur en consistente eenheden zijn niet volledig bewezen. Een toekomstige specificatiecatalogus vereist menselijke goedkeuring.

## 16. Media en documenten

Het contract onderscheidt primaire afbeelding, aanvullende beelden, uitvoeringsmedia, video, alttekst, datasheet, montagehandleiding, technische tekening, onderhoudsdocument en veiligheids-/conformiteitsdocument. Elk item hoort een geldige productrelatie, bron, versie en rechtenstatus te hebben.

**BEWEZEN HUIDIG:** producten en theme gebruiken media. **LEVERANCIERAFHANKELIJK:** originele bestanden, revisies, taal, technische juistheid en leverancierrechten. **BEDRIJFSREGEL VEREIST:** minimale beeldset, toegestane rechtenstatus en documentverplichting per producttype. Ontbrekende media worden niet vervangen door ongeautoriseerde beelden.

## 17. Logistiek

Eigen voorraad, leveranciersvoorraad, samengevoegde voorraadstatus, hoeveelheid, bron, actualiteit, levertijd, levertijdtype, cutoff, backorder, gewicht, product- en verpakkingsafmetingen, verpakkingseenheid, verzendklasse, pakket/pallet/afhalen, dropshipleverancier en fulfilmentbron blijven afzonderlijke velden.

- **BEWEZEN HUIDIG:** één locatie en inventory-items zijn aangetoond; delivery-profielen en operationele semantiek bleven beperkt toegankelijk.
- **VOORGESTELD CONTRACT:** voorraad of levertijd is alleen klantgeschikt wanneer bron, snapshot en betekenis geldig zijn.
- **LEVERANCIERAFHANKELIJK:** leveranciersvoorraad, bronactualiteit, verpakking en veel fysieke waarden.
- **BEDRIJFSREGEL VEREIST:** samenvoeging, cutoff, backorder, dropship, fulfilment en klanttekst.
- **Leegstaat:** uitsluitend `MANUAL_REVIEW`, `HIDE_COMPONENT` of later goedgekeurde conservatieve tekst; dit document stelt geen tekst of termijn vast.

## 18. Service en compliance

Garantie, retourcategorie, uitzonderingen, serviceproces, keurmerken, certificaten, onderhoudseisen, reserveonderdelen en juridische bron zijn conditioneel. Een leveranciersclaim wordt niet automatisch een BadkamerCity-belofte.

**VOORGESTELD CONTRACT:** toon alleen gevalideerde, toepasselijke service- of compliance-informatie. **BEDRIJFSREGEL VEREIST:** retour- en garantiebeleid, uitzonderingen en serviceproces. **LEVERANCIERAFHANKELIJK:** certificaten, keurmerken, technische onderhoudseisen en onderdelen. **OPEN BESLISSING:** welke velden per type publicatie blokkeren.

## 19. SEO en vindbaarheid

SEO-titel, metabeschrijving, canonical-identiteit, indexatiecategorie, zoektermen/synoniemen, breadcrumbcontext, interne relaties en structured-datarelevante waarden vormen invoer voor SEO, niet het definitieve SEO-beleid.

**BEWEZEN HUIDIG:** handle, titel, merk, producttype en theme-SEO-consumenten bestaan. **OPEN BESLISSING:** URL-opbouw, canonicalbeleid, indexatiecategorieën, breadcrumbs, synoniemen en interne-linkstrategie. Geen route, categorie of indexatiebesluit wordt in v0.1 genomen.

## 20. Relaties

Relaties zijn gericht, getypeerd en gevalideerd. De bron moet aantonen waarom een doelproduct is gekoppeld; een lege optionele relatie verbergt het component en een ontbrekende noodzakelijke relatie vraagt review of blokkeert de relevante functie.

| Relatietype | Richting | Cardinaliteit | Mogelijke bron | Validatie | Leegstaat | Gebruiksdoel |
| --- | --- | --- | --- | --- | --- | --- |
| Uitvoeringsrelatie | uitvoering -> groep en groepsleden | 0..1 groep; 1..* leden | SUP/BCE/ECC | Lid bestaat; assen/combinatie uniek | HIDE_COMPONENT of MANUAL_REVIEW | SWITCH, PDP |
| Switchergroep | product -> switchergroep | 0..1 | SUP/BCE/ECC | Geldige groep en productreferentie | HIDE_COMPONENT | SWITCH |
| Switcherkeuze-as | groep -> geordende assen | 1..* bij switcher | SUP/BCE | Unieke technische key en waarden | BLOCK_PUBLICATION voor switcherfunctie | SWITCH, CONFIG |
| Accessoire | product -> accessoire | 0..* | SUP/BCE | Doel bestaat; relatie niet zelfverwijzend | HIDE_COMPONENT | PDP, CART |
| Noodzakelijk aanvullend artikel | product -> vereiste aanvulling | 0..* | SUP/BCE | Doel bestaat; noodzaak goedgekeurd | MANUAL_REVIEW | PDP, CART, CONFIG |
| Aanbevolen aanvullend artikel | product -> aanbeveling | 0..* | BCE | Doel bestaat; aanbeveling actueel | HIDE_COMPONENT | PDP, CART |
| Onderdeel | hoofdproduct -> onderdeel | 0..* | SUP/BCE | Compatibiliteit en richting bewezen | HIDE_COMPONENT | PDP, SERVICE |
| Vervangend product | oud product -> opvolger | 0..1 | SUP/BCE/COM | Doel actief; geen cyclus | MANUAL_REVIEW | PDP, SEARCH |
| Alternatief | product -> alternatief | 0..* | BCE/COM | Doel actief; rationale aanwezig | HIDE_COMPONENT | PDP |
| Betere optie/upsell | product -> hogere optie | 0..* | COM/BCE | Commerciële grondslag goedgekeurd | HIDE_COMPONENT | PDP, CART |
| Gerelateerd product | product -> gerelateerd | 0..* | BCE/SUP | Doel bestaat; type relatie bekend | HIDE_COMPONENT | PDP |
| Serie | product -> serie | 0..1 | SUP/BCE | Serie hoort bij merk | HIDE_COMPONENT | PDP, FILTER, SEO |
| Set/combinatie | set -> onderdelen | 1..* voor set | SUP/BCE | Alle onderdelen bestaan; hoeveelheid geldig | MANUAL_REVIEW | PDP, CONFIG, CART |
| Parent/child | parent -> child | 0..* | UNDECIDED | Alleen gebruiken na apart architectuurbesluit | NOT_APPLICABLE | FUTURE |

**OPEN BESLISSING:** welke relaties wederkerig zijn, welke klantzichtbaar zijn en welke publicatie- of functieblokkers worden. `parent/child` is alleen een conceptuele mogelijkheid en verandert niet de bevestigde zelfstandige productarchitectuur.

## 21. Switcher en configurator

### 21.1 Brononafhankelijk switchercontract

Een switcher heeft minimaal een stabiele groeps-ID, productreferentie, geordende keuze-as, klantlabel, technische key, toegestane waarden, waardevolgorde, presentatievorm, combinatiegeldigheid, beschikbaarheidsstatus, fallback, snapshot/versie, bronhouder en validatiestatus nodig. Productreferenties kunnen later via intern ID, gevalideerde URL of SKU worden gekoppeld; de definitieve sleutelkeuze blijft open.

Een geldige combinatie is binnen groep en snapshot uniek en verwijst naar precies één bestaand, passend product. Een ongeldige combinatie mag niet naar een willekeurig product navigeren. Onbeschikbaarheid is geen synoniem voor ongeldigheid. Bij ontbrekende of inconsistente data wordt de switcher verborgen of voor handmatige review gemarkeerd; de gewone productpagina moet bruikbaar blijven.

### 21.2 Huidig bewijs en grens

- **BEWEZEN HUIDIG:** de actieve V2-route gebruikt `custom.switch_group`, `snippets/bc-product-switcher.liquid`, `assets/bc-product-switcher.js` en `assets/product-switcher-data.json`.
- **BEWEZEN HUIDIG:** de asset-snapshot bevat 433 groepen, 560 menu's en 3.383 unieke handles; exacte optiecombinaties zijn binnen die asset uniek.
- **BEWEZEN HUIDIG:** handle is alleen binnen deze asset/snapshot uniek bewezen, niet als toekomstige universele koppelsleutel.
- **BEWEZEN HUIDIG:** V2 gebruikt `kleur`; legacy/theme gebruikt onder meer `basiskleur`. Dit is een bekend semantisch conflict.
- **AFGELEID:** huidige Hotbath-opties zoals `type`, `vorm`, `type_handdouche`, `met_glijstang` en maatvelden tonen mogelijke assen, maar zijn geen goedgekeurde algemene taxonomie.
- **NOG ONDERZOEKEN:** oorspronkelijke bron, generator, mapping, eigenaar, volledige dekking en runtimegedrag.
- **OPEN BESLISSING:** definitieve switcherbron, productkoppelsleutel, canonieke assen, kleurmodel, fallback, presentatie en migratie van legacy/V2.

De huidige V2-asset is bestaand bewijs en geen definitieve architectuur. De legacy-route blijft technisch bereikbaar als `custom.group` data krijgt, maar dat veld was voor alle geïnventariseerde producten leeg. Dit contract neemt geen architectuurbesluit en wijzigt geen code of data.

## 22. Tegelcontract

Voor tegels zijn verkoop-/besteleenheid, prijsbasis, vierkante meter per doos, stuks per doos, stuks per vierkante meter waar relevant, breedte, lengte, dikte, doosgewicht, palletinformatie, minimumhoeveelheid, hele-dozenregel, snijverliesstandaard, aanpasbaarheid, afrondingsregel, voorraad-/leverbron, sample- en calculatorgeschiktheid conceptueel onderscheiden.

Alle waarden zijn **LEVERANCIERAFHANKELIJK** of **BEDRIJFSREGEL VEREIST**. **BEWEZEN HUIDIG:** generieke Shopify unit-pricepresentatie bestaat en 277 The Mosaic Factory-producten zijn in de Admin-inventaris genoemd. Dat bewijst geen tegelcalculatorwaarden. Zonder geldige eenheid, doosinhoud, prijsbasis en afronding blijft `tile.calculator_eligible` onwaar en de calculatorfunctie geblokkeerd.

## 23. Douchesetcontract

**BEVESTIGDE EIS:** BadkamerCity wil een douchesetconfigurator. Het doel is een bestaande, zelfstandig verkoopbare doucheset kiezen; niet tijdens deze taak nieuwe productconfiguraties genereren.

**AFGELEID bestaand bewijs:** de Hotbath-switcherasset bevat mogelijke keuze-informatie zoals type, kleur, vorm, bevestiging hoofddouche, type handdouche, glijstang, uitloop en maatwaarden. Deze keys zijn niet bewezen als volledige of leverancierbrede configuratorassen.

**VOORGESTELD CONTRACT:** algemene velden voor systeemtype, montage, hoofddouchemaat/-vorm, armtype, handdouchetype, glijstang, uitloop, uitgangaantal en afwerking. **LEVERANCIERAFHANKELIJK:** waarden, compatibiliteit, combinaties en dekking. **OPEN BESLISSING:** definitieve assen, volgorde, UX, architectuur, productkoppeling en fallback.

## 24. Badkamermeubelcontract

**BEVESTIGDE EIS:** BadkamerCity wil een badkamermeubelconfigurator. **VOORGESTELD CONTRACT:** breedte, opstelling, aantal laden/deuren, wastafeltype, aantal kommen, kraangaten, kleur, afwerking, materiaal, plaatsing, handgreep/bediening en spiegel-/kolomkastrelaties zijn mogelijke contractbegrippen.

Deze velden en hun waarden zijn **LEVERANCIERAFHANKELIJK** en nog geen definitieve assen. Productbron, compatible combinaties, inbegrepen onderdelen, voorraad en relaties ontbreken. UX, productmodellering, noodzakelijke versus aanbevolen aanvullingen en eventuele setlogica zijn **OPEN BESLISSING**.

## 25. Producttypematrix

| Producttype | Kernverplichte domeinen | Typeverplichte domeinen | Optionele domeinen | Calculator/configurator | Relatiebehoefte | Logistieke bijzonderheden | Media/documenten | Open beslissingen / bronafhankelijkheid |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Algemeen sanitairproduct | governance, identity, commercial, content, media, logistics, quality | toepasselijke specifications, service/compliance | SEO-verrijking, aanvullende relaties | Geen standaardconfigurator; typeafhankelijk | accessoires, noodzakelijk/aanbevolen, onderdelen, alternatief | maat/gewicht/verzendklasse en leverbron indien van toepassing | hoofdbeeld; handleiding/tekening naar type | **VOORGESTELD CONTRACT** voor kranen, douches, toiletten, wastafels, baden, spiegels, radiatoren, accessoires en installatiemateriaal; taxonomie en brondata open |
| Tegel | alle kerndomeinen | tile, maat-/materiaal-/kleur-specificaties, typegate | inspiratie, alternatieven, documenten | Calculator vereist alleen bij complete gevalideerde tegeldata | serie, uitvoering, sample, alternatief | doos, m², gewicht, pallet, minimum en afronding | kleur-/oppervlakmedia, datasheet waar beschikbaar | Volledig **LEVERANCIERAFHANKELIJK**; prijs-, sample- en afrondingsregels vereisen bedrijfsbesluit |
| Doucheset | alle kerndomeinen | shower_config, switcher, technische specificaties | accessoires, onderhoud, FAQ | Selectieconfigurator volgens later goedgekeurde assen | uitvoering, noodzakelijk aanvullend, accessoire | voorraad per zelfstandige set; afmetingen en gewicht | installatiehandleiding/tekening naar toepasselijkheid | Hotbath-opties zijn afgeleid bewijs; assen, compatibiliteit en UX open |
| Badkamermeubel | alle kerndomeinen | furniture_config, switcher, maat-/materiaal-specificaties | service, FAQ, alternatieven | Selectieconfigurator volgens later goedgekeurde assen | uitvoering, spiegel, kolomkast, noodzakelijk aanvullend | verpakking, meerdere colli/pallet en fulfilment mogelijk | beelden per afwerking; tekeningen/handleidingen waar van toepassing | Velden zijn voorstellen; bron, assen, setinhoud en compatibiliteit ontbreken |
| Toekomstige complete set | FUTURE | set/combinatie, compatibiliteit, onderdeelhoeveelheid | alle verrijking | **FUTURE** configuratie na apart besluit | set -> onderdelen, alternatieven, noodzakelijke artikelen | gecombineerde levering en deellevering nog onbeslist | set- en onderdeelmedia met rechten | Geen huidige lanceringsvereiste; architectuur, prijs, voorraad en retour volledig open |

De typebenamingen zijn toepasselijkheidsklassen voor dit contract en vormen geen definitieve producttypetaxonomie.

## 26. Leegstaatbeleid

| Categorie | Betekenis | Toegestaan gebruik |
| --- | --- | --- |
| `BLOCK_PUBLICATION` | Product of toepasselijke functie mag niet publiceren/activeren | Alleen voor goedgekeurde harde blockers |
| `HIDE_COMPONENT` | UI-element wordt niet getoond; rest van product blijft bruikbaar | Optionele inhoud of verrijking |
| `SHOW_APPROVED_FALLBACK` | Alleen een vooraf menselijk goedgekeurde fallback tonen | Nooit zelf commerciële/logistieke tekst invullen |
| `MANUAL_REVIEW` | Bevoegde rol moet ontbreken/conflict beoordelen | Onzekere bron, claim, relatie of bedrijfsregel |
| `ALLOW_EMPTY` | Lege waarde is toegestaan zonder presentatie | Niet-essentiële interne of optionele data |
| `NOT_APPLICABLE` | Begrip geldt aantoonbaar niet voor dit product/type | Vereist expliciete toepasselijkheidsbeslissing waar relevant |

| Belangrijk veld/groep | Voorgesteld leegstaatgedrag | Grens |
| --- | --- | --- |
| SKU, titel, handle, merk, producttype | `BLOCK_PUBLICATION` | Drempel blijft menselijk goed te keuren |
| Verkoopprijs, valuta, BTW-semantiek | `BLOCK_PUBLICATION` | Geen prijs of fiscale aanname verzinnen |
| Inkoopprijs | `MANUAL_REVIEW` of `ALLOW_EMPTY` afhankelijk van proces | Nooit klantzichtbaar als fallback |
| Primaire afbeelding en rechtenstatus | `BLOCK_PUBLICATION` | Geen ongeautoriseerde placeholder als productbewijs |
| Optionele aanvullende media/content | `HIDE_COMPONENT` | Geen lege component tonen |
| Voorraad, levertijd, leverbron/actualiteit | `MANUAL_REVIEW`, `HIDE_COMPONENT` of later `SHOW_APPROVED_FALLBACK` | Tekst en termijn blijven **BEDRIJFSREGEL VEREIST** |
| Verplichte switcher-/configuratorvelden | `BLOCK_PUBLICATION` voor de functie; productfallback later besluiten | Geen willekeurige combinatie kiezen |
| Tegelcalculatorvelden | `BLOCK_PUBLICATION` voor calculatorgeschiktheid | Productpublicatie zelf is apart besluit |
| Niet-toepasselijk kenmerk | `NOT_APPLICABLE` | Niet verwarren met onbekend of false |

## 27. Validatieregels

| Klasse | Regel | Soort |
| --- | --- | --- |
| Identifiers | Interne ID's en handles uniek; SKU-doeluniciteit eerst op bronconflicten controleren | Harde contractvalidatie / deels **LEVERANCIERAFHANKELIJK** |
| Verplichtheid | Alle goedgekeurde blockers gevuld of expliciet `NOT_APPLICABLE` waar toegestaan | Harde contractvalidatie |
| Datatype | Waarde parseert exact als gedeclareerd type en cardinaliteit | Harde contractvalidatie |
| Eenheid | Meetwaarde heeft goedgekeurde, expliciete eenheid; geen eenheid in vrije tekst verbergen | Harde contractvalidatie |
| Bereik | Getallen binnen fysiek en zakelijk goedgekeurd bereik | Leverancierafhankelijke validatie / open bedrijfsregel |
| Enumeratie | Waarde komt uit goedgekeurde catalogus; onbekende waarde niet stil mappen | Harde validatie na catalogusbesluit |
| Referentie-integriteit | Doel bestaat, is van toegestaan type en veroorzaakt geen verboden cyclus | Harde contractvalidatie |
| Handle/URL | Lowercase slug, uniek en geldig; URL-beleid staat apart open | Harde formatvalidatie / **OPEN BESLISSING** voor beleid |
| SKU | Niet leeg; toegestane tekens/normalisatie pas na bronanalyse | Harde aanwezigheid; leverancierafhankelijk formaat |
| EAN/GTIN | Als gevuld syntactisch en met geldige checkdigit; type/lengte niet onbewezen afdwingen | Leverancierafhankelijke validatie |
| Prijs | Geldbedrag >= 0 en valuta aanwezig | Harde contractvalidatie |
| Compare-at | Als gevuld: zelfde valuta en >= verkoopprijs | Harde contractvalidatie plus open juridische semantiek |
| Media | Bereikbaar, juiste productrelatie, bron en goedgekeurde rechtenstatus | Harde contractvalidatie |
| Switcher | Per groep/snapshot unieke combinatie; alle producten/assen/waarden geldig | Harde functievalidatie |
| Calculator | Alle toepasselijke eenheden, basis, inhoud en afrondingsregels compleet | Harde functievalidatie |
| Provenance | Externe waarde heeft bronrecord, snapshot en bronhouder | Harde contractvalidatie na bronprocesbesluit |
| Logistiek | Geen publicatie van onbewezen voorraad-, lever- of cutoffbelofte | Harde kwaliteitsgrens; bedrijfsregel vereist |
| Specificaties | Geen vrije tekst waar boolean, enum, referentie of meetwaarde hoort | Voorgestelde kwaliteitswaarschuwing; later per catalogus hard maken |
| Dekking | Aanbevolen velden onder een later goedgekeurde typedrempel signaleren | Voorgestelde kwaliteitswaarschuwing |

## 28. Publicatie- en kwaliteitsgates

| Gate | Controleert conceptueel | Nu bewijsbaar? | Gevolg bij falen |
| --- | --- | --- | --- |
| `CORE_IDENTITY_READY` | provenance, ID, SKU, titel, handle, merk, producttype, uitvoering, variantreferentie | Deels; huidige kwaliteit kent hiaten | Blokkeer voorgestelde publicatie |
| `COMMERCIAL_READY` | verkoopprijs, valuta, BTW, prijsbron/actualiteit en geldige compare-at | Deels; bron en regels ontbreken | Blokkeer voorgestelde publicatie |
| `CONTENT_READY` | typegebonden minimuminhoud en gecontroleerde claims | Niet volledig | Menselijke typedrempel nodig |
| `MEDIA_READY` | primaire media, alttekst, bron en rechten | Niet volledig | Blokkeer voorgestelde publicatie |
| `SPECIFICATIONS_READY` | toepasselijke getypeerde kenmerken en eenheden | Nee; catalogus/dekking ontbreken | Blokkeer typefunctie of publicatie volgens later besluit |
| `LOGISTICS_READY` | bron, actualiteit, voorraad-/levertijdsemantiek en veilige fallback | Nee | Geen onbewezen klantbelofte; blokkeer voorgestelde publicatie |
| `SEO_READY` | route-identiteit, metadata/schema-input en indexatieklasse | Deels; beleid open | Review of blokker volgens later besluit |
| `RELATIONS_READY` | vereiste relaties en referentie-integriteit | Nee | Verberg optioneel; blokkeer vereiste functie |
| `TYPE_SPECIFIC_READY` | tegel-, douche- of meubelblokkers | Nee | Typefunctie niet activeren |
| `PUBLISHABLE` | alle toepasselijke goedgekeurde gates plus workflowgoedkeuring | Nee | Geen publicatiehandeling |

Alle gates zijn **VOORGESTELD CONTRACT**. Drempels, uitzonderingen en overridebevoegdheid vereisen menselijke goedkeuring. Dit model wijzigt geen product en publiceert niets.

## 29. Voorlopige opslagcategorieën, geen definitieve Shopify-mapping

| Abstracte categorie | Betekenis | Voorbeeld van huidig bewijs of kandidaat | Grens |
| --- | --- | --- | --- |
| Bestaand native productveld | Shopify productkernveld | ID, titel, handle, vendor, producttype, status | Huidige aanwezigheid is geen kwaliteitsgoedkeuring |
| Bestaand native variantveld | Shopify variantkernveld | variant-ID, SKU, prijs, compare-at, inventory-item, unit price | Opslag en semantiek blijven apart beoordelen |
| Custom productveld kandidaat | Productgebonden concept zonder bewezen native plaats | content-, governance- of logistiek concept | Geen namespace/key/type gekozen |
| Custom variantveld kandidaat | Uitvoeringsgebonden concept zonder bewezen native plaats | leverancieridentifier of uitvoeringsmaat waar passend | Product/variantkeuze nog open |
| Metaobject/reference kandidaat | Herbruikbare gecontroleerde entiteit/relatie | merk, serie, specificatiecatalogus, relatiegroep | Definitie en ownership nog open |
| Berekende waarde | Deterministisch uit goedgekeurde input | korting, vierkantemeterprijs, quality gates | Formule en bronvelden moeten zijn goedgekeurd |
| Extern systeem | Waarde of bewijs buiten Shopify | inkoop, syncbewijs, voorraadfeed mogelijk | Systeem bestaat niet bewezen |
| Nog onbeslist | Opslag vereist apart architectuur-/bronbesluit | switcherbron, provenance, sommige logistiek | Geen impliciete keuze maken |

**BEWEZEN HUIDIG:** native velden en bestaande `custom.*`-definities uit de Admin-inventaris mogen als huidige opslag worden genoemd. Nieuwe conceptvelden krijgen in dit document geen Shopify namespace, key of definitietype; er is geen Admin-mutatie uitgevoerd.

## 30. Mappingtemplate voor leveranciers

Dit lege template wordt later per werkelijk aangeleverde bron ingevuld. Het bevat bewust geen fictieve leverancierkolommen of voorbeeldwaarden.

| leverancier | bronbestand | bronversie/snapshot | bronveld | bronbetekenis | brontype | voorbeeldwaarde | contract_key | transformatie | eenheidsconversie | toegestane waarden | nullbeleid | conflictregel | eigenaar | validatie | mappingstatus | opmerkingen |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

Mappingstatussen moeten later minimaal `NOG_ONDERZOEKEN`, `VOORGESTELD`, `GEVALIDEERD`, `AFGEWEZEN` en `NIET_VAN_TOEPASSING` onderscheiden. De projecteigenaar en betreffende data-/bedrijfsrol keuren mappings afzonderlijk goed.

## 31. Wat zonder leveranciersbestanden verder kan

| Kan verder | Toegestane uitwerking | Voorwaarde |
| --- | --- | --- |
| Productinformatiecontract | Betekenissen, datatypes, cardinaliteit en toepasselijkheid beoordelen | Als voorstel behandelen, niet als beschikbare data |
| Vereisteniveaus | Blockers/recommendations per veld en type bespreken | Menselijke goedkeuring vereist |
| Leegstaatbeleid | Gestandaardiseerde technische uitkomsten definiëren | Geen commerciële/logistieke fallbacktekst verzinnen |
| Eigenaarsrollen | Rollen en beslisbevoegdheden toewijzen | Geen persoonsnamen aannemen |
| Validatieprincipes | Harde checks, waarschuwingen en open regels scheiden | Bronformaten later toevoegen |
| Publicatiegates | Gateverbanden en rapportagevorm ontwerpen | Geen productstatus wijzigen of publiceren |
| Mappingtemplate | Leeg herbruikbaar format beheren | Pas met echte bron invullen |
| Voorbereidend informatiearchitectuuronderzoek | Begrippen, behoeften en bewijsgrenzen onderzoeken | Geen categorie-/URL-besluit nemen |
| Technische stabilisatie zonder productdatawijziging | Afzonderlijk afgebakend onderzoek/plan | Nieuwe expliciete taak en toestemming vereist |

## 32. Wat geblokkeerd blijft

| Geblokkeerd onderwerp | Ontbrekende input/besluit |
| --- | --- |
| Definitieve Shopify-metafieldcatalogus | Bronnen, contractgoedkeuring, opslagarchitectuur en Admin-besluit |
| Definitieve leveranciermapping | Werkelijke bronbestanden, snapshots, velddefinities en bronhouders |
| Prijsregels | Bronprijzen, BTW-, compare-at-, valuta- en actualiteitsbesluiten |
| Voorraad-/levertijdregels | Bronnen, timestamps, fulfilmentsemantiek en operationele klantbelofte |
| Daadwerkelijke imports | Goedgekeurde mapping, tooling, validatie, herstelplan en expliciete mutatietoestemming |
| Datacorrecties | Gevalideerde bron en menselijke productdata-eigenaar |
| Definitieve switcherbron | Generator/input, eigenaar, dekking, kleurmapping en architectuurbesluit |
| Tegelcalculatorwaarden | Tegelbron, eenheden, verpakking, prijsbasis, voorraad en afrondingsregels |
| Productkwaliteit over circa 20.000 producten | Werkelijke volledige product- en brondata plus goedgekeurde gates |
| Definitieve categorie-/filterdekking | Taxonomie, bronwaarden, zoek-/SEO-besluiten en representatieve dekking |

## 33. Open beslissingen

1. **OPEN BESLISSING:** welke van de 190 contractkeys en voorgestelde vereisteniveaus worden goedgekeurd, aangepast of uitgesteld?
2. **OPEN BESLISSING:** welke rollen krijgen feitelijk eigenaarschap en overridebevoegdheid?
3. **OPEN BESLISSING:** welke kern- en typegates blokkeren productpublicatie, en welke blokkeren alleen een component of functie?
4. **OPEN BESLISSING:** wat zijn de merk-, serie-, model- en producttypecatalogi en wie beheert ze?
5. **OPEN BESLISSING:** welk SKU-, handle-, GTIN- en leverancieridentifierbeleid geldt na bronanalyse?
6. **OPEN BESLISSING:** welke commerciële semantiek geldt voor prijzen, korting, belasting en prijsactualiteit?
7. **OPEN BESLISSING:** welke operationele semantiek en goedgekeurde fallback geldt voor voorraad en levertijd?
8. **OPEN BESLISSING:** hoe worden specifieke kleur, basiskleur en afwerking canoniek gescheiden en gemapt?
9. **OPEN BESLISSING:** welke specificaties, documenten en compliancebewijzen zijn per producttype hard vereist?
10. **OPEN BESLISSING:** wat wordt de definitieve relatie-, switcher- en configuratorarchitectuur, bron en productkoppelsleutel?
11. **OPEN BESLISSING:** welke tegelprijs-, doos-, minimum-, snijverlies- en afrondingsregels gelden?
12. **OPEN BESLISSING:** welke douche- en meubelkeuze-assen en UX worden na brononderzoek gebruikt?
13. **OPEN BESLISSING:** welke abstracte opslagcategorie wordt later voor elk goedgekeurd concept technisch gekozen?
14. **OPEN BESLISSING:** volgt na menselijke review eerst informatiearchitectuuronderzoek of een afzonderlijke technische stabilisatietaak?

## 34. Risico's

| Risico | Gevolg | Beheersing |
| --- | --- | --- |
| Concept wordt als definitieve Shopify-mapping gelezen | Premature velden en migraties | Labels, abstracte opslagcategorieën en afzonderlijk besluit verplicht |
| Contract wordt als bewijs van beschikbare data gelezen | Onhaalbare dekking/importverwachting | Leverancierafhankelijkheid per rij en nulmeting blijven leidend |
| Te veel publication blockers | Onnodig groot deel assortiment niet publiceerbaar | Menselijke typegewijze drempelreview vóór toepassing |
| Te weinig blockers | Onbetrouwbare prijs, logistiek of identiteit live | Harde gates met bron/snapshot en bevoegde eigenaar |
| Vrije specificatietekst groeit ongecontroleerd | Filters, zoeken en vergelijkbaarheid falen | Getypeerde catalogus en eenheid voorrang geven |
| `kleur`/`basiskleur` wordt stil samengevoegd | Verkeerde varianten en filters | Expliciete canonieke mapping en regressietest eisen |
| Handle wordt universele sleutel | Breuk bij URL-wijziging of externe bron | Interne referentie/SKU-alternatieven later bronmatig toetsen |
| Leverancierswaarden worden klantbelofte | Juridisch en operationeel risico | Bedrijfsregel, actualiteit en verantwoordelijke rol verplicht |
| Configurator maakt ongeldige combinaties | Verkeerde bestelling | Combinatie-uniciteit, referentie-integriteit en fallback valideren |
| Interne inkoopprijs lekt | Commercieel risico | Interne opslag/toegang apart besluiten en testen |
| Media zonder rechten of juiste uitvoering | Juridisch/inhoudelijk risico | Bron, rechtenstatus en productmatch als gate |
| FUTURE-setlogica wordt voortijdig gebouwd | Scopegroei en fout productmodel | Complete set expliciet `FUTURE` houden |

## 35. Aanbevolen vervolgstap

1. Laat de projecteigenaar met productdata-, commerciële, operationele, content-, SEO-, technische en juridische rollen de contractkeys, vereisteniveaus, leegstaatregels en gates beoordelen.
2. Behandel iedere toekomstige wijziging van keys, niveaus, gates, eigenaarschap, bron of opslagcategorie als een afzonderlijk te beoordelen documentatiebesluit.
3. Lever daarna oorspronkelijke Hotbath-, The Mosaic Factory- en overige leveranciersbronnen per leverancier aan met bronhouder en snapshot, elk binnen een afzonderlijk toegestane read-only taak.
4. Vul pas dan een leveranciersmapping in en meet dekking/conflicten. Kies daarna pas Shopify-opslag, importvalidatie en migratievolgorde.
5. Voer eerst de afzonderlijk goedgekeurde technische decompositietaak uit; besluit daarna menselijk welke vervolgtaak eventueel uitvoerbaar wordt.

## 36. Veiligheidsbevestiging

- **BEWEZEN:** voor `BC-DATA-003` zijn uitsluitend lokale projectdocumenten en repositorybestanden read-only geraadpleegd.
- Shopify Admin is niet benaderd; Shopify-data, producten, collecties, metafields en metaobjects zijn niet gewijzigd.
- Themes en theme-code zijn niet benaderd via Shopify, gepusht, gepulld, gepubliceerd, verwijderd, hernoemd of gewijzigd.
- Leveranciers-, CSV-, JSON-, XLSX-, XML- en overige bronbestanden zijn niet gewijzigd.
- Er is geen import-, generator-, converter- of productscript uitgevoerd en geen package, app of extensie geïnstalleerd.
- Er zijn geen definitieve Shopify-, leverancier-, categorie-, URL-, SEO-, design- of implementatiebesluiten genomen.
- De menselijke goedkeuring maakt dit document een bestuurde conceptuele werkbasis; zij geeft geen toestemming voor Shopify-, theme-, product-, bron-, import- of andere datamutaties.

## 37. Menselijke goedkeuring

- **BEWEZEN:** `BC-DATA-003` is op 2026-08-10 binnen zijn brononafhankelijke documentatiescope door de projecteigenaar afgerond en naar `DONE` goedgekeurd.
- De projecteigenaar accepteert productinformatiecontract v0.1 als bestuurde conceptuele werkbasis voor volgende onderzoeks- en ontwerptaken.
- De technische controles voor 190 unieke conceptuele contractkeys en 15 logische domeinen zijn geaccepteerd.
- Alle keys, vereisteniveaus, kwaliteitsgates en abstracte opslagcategorieën blijven voorstellen; de goedkeuring is geen veldgewijs of producttypegewijs definitief besluit.
- Veldniveau- en producttypeniveaukeuzes mogen na afzonderlijke menselijke beoordeling worden aangepast.
- Leveranciersdata moet later per leverancier afzonderlijk worden aangeleverd, tegen het contract worden vergeleken en menselijk worden goedgekeurd.
- Dit document is geen bewijs dat leverancierswaarden, productwaarden of benodigde dekking beschikbaar of betrouwbaar zijn.
- Deze goedkeuring geeft geen toestemming voor Shopify-, theme-, product-, import-, leverancier- of datamutaties en kiest geen definitieve Shopify- of leveranciermapping.
