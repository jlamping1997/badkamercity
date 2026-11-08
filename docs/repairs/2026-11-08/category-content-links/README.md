# CATEGORY-COPY-01 — links naar lege categorieën uit winkelteksten gehaald

**8 november 2026 · CONTENT_APPLIED_VERIFIED / DORMANT_ROUTE_EXPLAINED.** De onderzochte 404 is een lege, ongepubliceerde collectie. In de actuele categorieteksten zijn wel negen echte verwijzingen naar lege productlijsten gevonden en gericht weggehaald.

## Oorspronkelijke route

/collections/tegeltoebehoren hoort bij bestaande collectie 584286306570, met nul producten en nul publicaties. Alle negen menu’s zijn volledig gelezen: 227 menuvermeldingen, geen verwijzing naar deze route. Ook de collectieomschrijvingen bevatten geen verwijzing naar die ongepubliceerde bestemming. De publieke route geeft de verwachte 404. [Route-/navigatiebewijs](route-and-navigation.json), [gerichte HTTP-controle](dormant-route-http.json).

De collectie is niet gepubliceerd, hernoemd of gevuld. Er is geen redirect naar een inhoudelijk andere categorie gemaakt. De identiteit blijft beschikbaar voor later werkelijk assortiment, volgens het [categorisatiecontract](../../../CATEGORIZATION_AND_SEO_POLICY.md).

## Echte klantlinks hersteld

Volledige read van de **226 gepubliceerde collectieomschrijvingen** vond negen links naar gepubliceerde collecties met nul native producten. Alle negen doelen zijn publiek opgevraagd: HTTP 200, expliciete melding Er staan op dit moment geen producten en geen productlinks in de hoofdinhoud. Dit is concrete inhouds-/routecontrole, niet alleen een oordeel op grond van een nulmeting.

| Bestaande categoriepagina | Verwijzing verwijderd |
| --- | --- |
| Badkamermeubels | /collections/badmeubel-sets |
| Toiletten en fonteinen | /collections/staande-toiletten, /collections/complete-toiletsets |
| Wastafels | /collections/vrijhangende-wastafels |
| Baden | /collections/inbouwbaden |
| Tegels | /collections/tegelstroken |
| Verwarming | /collections/spiegelverwarming |
| Badkamerverlichting | /collections/wandlampen |
| Spiegels | /collections/toiletspiegels |

De linkopmaak is verwijderd met behoud van de verklarende termen en uitleg. Alleen de Tegels-zin met Bekijk ook tegelstroken is vervangen door **Let bij een langwerpig formaat ook op de legrichting.** Zo bevat de uitleg geen winkeloproep naar die lege lijst.

Elke mutatie had vlak vooraf een verse body-/metadata-guard. Alleen id en descriptionHtml zijn geschreven, via acht afzonderlijke collectionUpdate-operaties. Geen producten, collectiesources, lidmaatschappen, titels, handles, SEO-velden, templates, publicaties, menu’s of thema’s geschreven. Aantallen, publicatierecords en SEO zijn exact teruggelezen. De **drie inline stijlblokken van Badkamermeubels zijn bytegelijk behouden**, evenals de SPLIT-markers en alle overige bodyinhoud. [Voor/na en gerichte herstelwaarden](collection-repairs.json).

## Controle en grenzen

- Acht publieke ouders vóór en na: HTTP 200, één H1; titel, meta description, canonical en alle overige hoofdinhoudlinks gelijk. Zeven hoofdteksten zijn tekstgelijk; alleen Tegels heeft de bedoelde zin vervangen. [Publieke vóórmeting en negen lege doelen](public-before.json), [publieke nacontrole](public-after.json).
- Alle 226 gepubliceerde omschrijvingen opnieuw volledig gelezen: precies acht bedoelde bodyverschillen, 218 overige bodies en de gelezen identiteit/SEO/template exact gelijk. Geen resterende omschrijvingslinks naar de in deze inventaris gevonden nulproductcollecties of ontbrekende gepubliceerde collectiehandles. [Scanbereik](scan-summary.json).
- Negen menu’s opnieuw exact gelijk; hun onderzochte /collections/handle-bestemmingen zijn gepubliceerd en niet leeg. Dit is geen uitspraak over elk ander linktype of alle huidige Page-/blogteksten. Geen nieuwe categorie of menuopbouw gemaakt.
- MAIN blijft 196368531722 — Klantenservice 8 nov. Geen themefiles geschreven of thema gepubliceerd; de acht omschrijvingen staan direct live. [Finale Admin-readback](final-admin-readback.json), [verificatiegrenzen](verification.json), [documentatiecontrole](documentation-checks.json).

Geen nieuwe JavaScript-/browser-/mobiele bediening, computed styles, checkout, betaling, mail, herroepingsbevestiging of meetketen getest. De drie behouden CSS-blokken zijn bronbewijs, geen nieuwe visuele telefoonproef. Geen volledige productgeschiktheids- of catalogusfactcheck.

## Herstel en vervolg

Lees de actuele descriptionHtml en herstel uitsluitend de betreffende opgeslagen vorige body als die nog exact overeenkomt met de verwachte nawaarde. Latere eigenaarwijzigingen niet overschrijven. Voor Badkamermeubels alle drie stijlblokken behouden. Geen volledige collectie-/productexport terugschrijven en geen volledige themapush doen.

**Volgende concrete handeling:** dezelfde doelcontrole uitvoeren op collectie-links in gepubliceerde Pages en bloginhoud, vóór eventuele gerichte copywijzigingen. Native policy-scope, juridische identiteit, echte betaal-/mail-/meetketen en mobiel behouden hun aparte open taken. Andere filter-/Cotto-/BRAUER-checkpoints en holds blijven behouden.

Broncodebranch fix/product-cards-2026-10-14; deze ronde bevat alleen documentatie in Git, omdat de inhoud via Shopify Collections wordt beheerd. Main blijft documentatie-ingang. Technische bron: [Shopify collectionUpdate](https://shopify.dev/docs/api/admin-graphql/2026-10/mutations/collectionUpdate), met de actuele CollectionUpdateInput/collection-argumentvorm uit de connectorschema’s. De connector heeft alle uitgevoerde GraphQL-operaties gevalideerd; geen Liquid-code gegenereerd of gewijzigd.
