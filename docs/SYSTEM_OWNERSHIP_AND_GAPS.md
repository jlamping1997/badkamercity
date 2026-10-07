# BadkamerCity — systemen, eigenaarschap en nog ontbrekende overdrachtsstukken

**Momentopname:** 2026-10-07. Alle statussen zijn **toegang of bewijs**, niet de belofte dat de hele webshop al productierijp is. Dit bestand bevat bewust **geen geheimen, contactgegevens van privépersonen of klantdata**. Vul operationele eigenaarsrollen in een afgeschermde beheeromgeving in, niet als wachtwoorden in Git.

## 1. Systeemregister

| Systeem/bron | Wat daarin zit | In deze Git-repository? | Toegang/verificatie vóór werk |
| --- | --- | --- | --- |
| GitHub `jlamping1997/badkamercity` | Theme-code, documentatie, commitgeschiedenis | **Ja** | `main`, `git status` en permissions |
| Shopify winkel `fpa9hu-i3.myshopify.com` | Producten, collecties, prijzen, voorraad, metafields, menus, orders, settings | **Nee, alleen theme-snapshot en afzonderlijke Admin-samenvatting** | Toegang tot Shopify Admin en actuele `MAIN` |
| Shopify thema-bibliotheek | Gepubliceerde en ongepubliceerde themes, theme editor/config | De bestanden zijn versioneerbaar, de live-rol niet | Theme ID/role en actuele templatekeuze |
| Shopify Files/CDN | Product/media/collectie-afbeeldingen en marketingvisuals | Vaak **niet** als bronbestand | Bestandsrechten/licenties/CDN-URL's |
| Search & Discovery | Native storefrontfilters en gerelateerde producten | **Nee** | Admin-appsettings en werkelijk geactiveerde filters |
| Checkout/betaling/verzending/BTW | Commerciële winkelinstellingen | **Nee** | Merchant-owner, testcheckout/instellingen |
| Externe filters VPS | Backend API, index/Typesense, logs, deployments, uptime | **Nee**, alleen publieke frontendkoppeling | Bevoegdheid op server/backendproject, monitoring en secrets |
| Leveranciers Hotbath | Brondatasets, scrape/mapping, import- en verrijkingsrondes | Niet compleet | Herkomst, datum, importlog, toestemmingen, datakwaliteit |
| Leveranciers Wiesbaden | CSV/importoutput, specificaties, afbeeldingen, statusregels | Niet compleet | Actuele bron-export, productscope en SQL/CSV-pipeline |
| Leveranciers JEE-O | Officiële data/tekst, afbeeldingen, SKU-mapping, aanvullingen | Niet compleet | Brondownloads, productstatus en rechten |
| Andere merken | Diverse leveranciercatalogi en imports | Niet compleet | Per merk afzonderlijke bron/kwaliteit |
| Google Search Console/Analytics | Indexing, performance, conversie-meting | **Nee** | Geautoriseerde Analytics/GSC toegang, gekoppeld domein |
| Domein/DNS/hosting | Domeinen, redirects, records, certificaten | **Nee** | Beheeraccount en rollbackprocedure |

### Statuscodes voor operationele beheerders

`AANWEZIG_VERIFIEERD` = huidige read-only snapshot bestaat; `TOEGANG_TE_CONTROLEREN` = bevoegdheid niet uit documentatie afleidbaar; `EXTERN_PROJECT` = code/uitvoering niet meegecheckt; `MANUELE_VALIDATIE` = er ontbreekt runtime- of datatest; `ALLEEN_HISTORISCH` = oude logs/exports, actuele werking onbekend.

Niet invullen met fictieve e-mailadressen, passwords of namen. De overdracht moet vooral doorverwijzen naar het zakelijke accountsysteem/wachtwoordkluis en de bevoegdheidseigenaar.

## 2. Concrete code- versus data-grenzen

**Thema is presentatie, geen bron van productwaarheid.** Liquid leest Shopify native velden, product-/collectie-instellingen en metafields. Een lege waarde of ongelinkte SKU kan de UI laten verdwijnen of anders laten werken. De theme-snapshot reproduceert **geen productcatalogus** bij een nieuwe Shopify store.

**Shopify Admin-snapshot:** `docs/SHOPIFY_ADMIN_STRUCTURE_2026-10-07.json`, alleen read-only: 9 menu's, 204 collecties, 11.053 producten (11.051 ACTIVE, 1 DRAFT, 1 UNLISTED), 174 product-metafielddefinities; nul definitieobjecten voor PRODUCTVARIANT en COLLECTION. Dat bewijst geen inhoud/dekking van die velden. Gebruik `PRODUCT_METAFIELD_MAPPING_AUDIT.md` voor potentiële namespace-verschillen.

**A-Z-menu's en SEO-landingpagina's:** sommige menulinks zijn bestaande Shopify-collecties, andere zoek-HTTP-fallbacks. Een knopnaam betekent niet dat er een uniek indexeerbaar productassortiment achter zit. Controleer menu-item URL, collectiemembership, online-publicatie en canonical vóór SEO-uitbreiding.

**Homepage collectieafbeeldingen:** kan uit Shopify CDN-uploads komen die niet in Git als eigen lokale bestanden staan; een theme clone in dezelfde Shopify store behoudt meestal dezelfde CDN-referenties, maar een nieuwe winkel niet automatisch.

## 3. Bekende lokale projectpaden uit eerdere werkzaamheden

Dit zijn **aanwijzingen**, niet aantoonbaar actuele bestanden:

- `C:\Projects\badkamercity-shopify-current` — gebruikte theme/CLI-workmap.
- `C:\Projects\badkamercity` — eerdere repository/ontwikkelwerkmap.
- `C:\Projects\badkamercity-filters-LIVE` — externe filterontwikkelomgeving.
- `C:\Projects\badkamerxxl_scraper` — productinformatieonderzoek/scraper.
- `C:\Projects\badkamercity_images` — collectie- en homepageafbeeldingen/scripts.
- Andere historische merk-specifieke mapnamen kunnen voorkomen, zoals `badkamercity_jeeo`.

Een opvolger moet op de echte Windows-computer verifiëren welke van deze mappen aanwezig zijn, of het een Git-repo is en of de inhoud actueel en geautoriseerd is. Kopieer niet zomaar complete scraperdata naar een **publieke** Git-repository.

## 4. Minimale overdracht van externe afhankelijkheden

Deze checklist is nodig voordat iemand **zonder de oorspronkelijke beheerder** het hele bedrijfssysteem kan onderhouden:

| Nodig | Waarom | Staat nu in dit dossier? |
| --- | --- | --- |
| Zakelijk beheerde Shopify-eigenaarstoegang + back-up admin | UI, producten, checkout, thema-publicatie | **Nee, toegang extern regelen** |
| GitHub admin/toegangsbeleid incl. 2FA/recovery | Code/branches/PR's | Repo bekend; accountrechten niet overdraagbaar via Git |
| Document met VPS-provider/server/project en herstel | Externe filters op termijn beheren | Alleen publieke endpoint + frontendscope bekend |
| Backend source repo + deployment instructie | Rebuild/herstart/rollback filters | **Niet in dit repo** |
| VPS/API/index secreteigenaarschap in beveiligde kluis | Geen embedded keys in theme | **Niet opslaan in Git** |
| Actuele leveranciersdataset per merk + kolommenmapping | Producten correct verrijken | **Niet volledig aanwezig** |
| Import scripts/virtuele omgeving/requirements | Reproduceerbare massimport | **Niet compleet in dit repo** |
| Data-validator / quarantainelog per importbatch | Correcte prijs/SKU/categorie/data | Te organiseren per merk |
| Restore-/backupbeleid voor Shopify-data | Theme Git herstelt geen productverlies | Geen aantoonbare automatische backup |
| Domain/DNS/Google Search Console-access | SEO/indexing/URL foutoplossing | Beheeraccount extern regelen |
| Checkout-/betaal-/shipping testprocedure | Lancering en orders | Niet inhoudelijk geverifieerd |

**Praktisch:** zorg voor een zakelijke, met 2FA beschermde wachtwoordmanager; leg eigenaar/rol, link naar beheerportaal, toegangsherstel en back-upverantwoordelijke vast buiten deze openbare repo. Vermeld in Git hooguit de naam van het register en de toegangsprocedure.

## 5. Wat kun je herstellen uit deze repo?

**Wel:** theme-Liquid, HTML/CSS/JS, JSON-templates, locales, theme-settings, gemapte SKU-relaties in snippets en inbegrepen statische assets. De momentopname is inhoudelijk vergeleken met live Shopify.

**Niet:** een gesloten orderdatabase, betalings- of klantgegevens, actualiteit van leveranciersvoorraad, inhoud van niet-exporteerde metafields, webshop Apps, serverconfig, dynamische frontend API-index of elk bestand in Shopify Files/CDN. Een Git-commit heeft daarvoor onvoldoende bereik.

### Herstel na incident

1. **Niet paniek-publiceren:** inventariseer impact en voorkom extra automatische pushes.
2. Read-only Shopify: huidige MAIN/preview, laatst werkende theme en wijzigingen sinds incident.
3. Git: branch/commit, actuele worktree-diff, laatste gecontroleerde baseline en manifest.
4. Als alleen theme-code stuk is: test herstel op een **nieuw ongepubliceerd thema**; vergelijk screenshots/checkoutstromen; merchant publiceert pas na acceptatie.
5. Als producten/collecties/prijzen verloren zijn: Shopify Admin/logs/back-upservice, geen theme rollback verwachten.
6. Als externe filters falen: de native route laten werken; backend/logs/health herstellen via de serverbeheerder.
7. Schrijf een incidentrecord: starttijd, impact, wijziging, herstelkeuze, bewijs en preventie.

## 6. Open zaken die niet met nog meer theme-documentatie verdwijnen

- Productdatakwaliteit en de per-merk importstatus zijn niet volledig reconstrueerbaar uit code.
- Checkout/productpublicatie/SEO-veldresultaten niet volledig end-to-end getest in deze documentatieronde.
- Exacte server-/backenddeploystappen onbekend; de filterfrontendscope wel.
- Geen wettelijk getoetste SLA/levering-/laagsteprijsgarantieclaims vanuit theme-code afleidbaar.
- Core Web Vitals, Lighthouse, GSC-indexatie en externe APIs moeten opnieuw gemeten worden.
- Theme Editor- en Shopify Admin-wijzigingen kunnen na deze snapshot plaatsvinden zonder Git-commit.

Zet elke onbekende bron op **TE VERIFIËREN**, noteer een verantwoordelijke rol, datum en terugverwijzing zodra bewezen. Dit is veiliger én sneller dan zoeken naar informatie die nooit in de repository heeft gestaan.
