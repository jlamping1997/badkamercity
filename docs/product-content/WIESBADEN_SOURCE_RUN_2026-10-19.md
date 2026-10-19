# Wiesbaden bronrun — 19 oktober 2026

## Uitkomst en actuele fase

**BRONRUN COMPLETE — IMPORT NIET TOEGEPAST.** Eigenaar wil eerst het volledige fabrikantassortiment verzamelen en vergelijken, inclusief producten die nog niet in BadkamerCity staan. Daarna volgen gecontroleerde specificaties, categorieën, breadcrumbs, filters, eigen content en prijzen. EAN wordt geen koppelsleutel of nieuwe klantcontent.

Bestaande werkbranch: `fix/product-cards-2026-10-14`. Codecheckpoint **1ad028059cc99e203ead0aa9873606d9bf2eaa81**. Uitvoering via ChatGPT/Linux en Shopify-/GitHub-connectors. Windows lokaal en een echte live import/browserweergave niet gecontroleerd. Geen producten, prijzen, voorraad, publicaties, thema's of externe zoekindexen gewijzigd. Verse eindread: MAIN **195392143626 — BadkamerCity - Winkelwagen helder**.

## Volledige bron en winkelvergelijking

| Onderdeel | Bewezen resultaat |
| --- | ---: |
| Openbare fabrikantcatalogus en opgehaalde product-HTML | 2.841 unieke producten |
| API-paginering | 29 pagina's; gedeclareerde telling en unieke UID-/SKU-telling sluiten |
| Actuele Wiesbaden-producten in de winkel | 2.265 |
| Complete winkel-SKU-index, alle merken | 11.157 varianten |
| Bestaande exact gekoppelde Wiesbaden-producten | 2.240 |
| Bronproducten zonder enige winkel-SKU-match | 601 |
| Bestaande Wiesbaden-producten zonder bronmatch | 25 |
| Werkelijke nieuwe Wiesbaden-kandidaten | 217 |
| Andere nieuwe bronmerken | 379 Xellanz, 2 Akemi, 2 Riko |
| Nieuw bronartikel zonder opgegeven merk | 1 |

De 601 zijn dus geen 601 nieuwe Wiesbaden-producten. Onbekend merk: fabrikantnummer 46.4505, mantelbuis. Andere merken en onbekend merk staan apart. De 25 bestaande producten zonder bronmatch worden niet automatisch verwijderd of gearchiveerd. Een nieuwe kandidaat is nog geen leverbaar/publicatieklaar product. Alle bestaande 2.265 hebben ACTIVE en een niet-lege onlineStoreUrl in de Admin-snapshot; geen afzonderlijke HTTP-controle van elke productpagina geclaimd.

De homepage rechtstreeks opgehaald; de sessiebijlage was eerdere product-HTML. `/sitemap.xml` en `/sitemap_index.xml` gaven 404. De zichtbare HTML-assortimentlijst meldt 1.857 producten, de openbare fabrikantinterface 2.841. Alleen homepage/assortiment links volgen mist dus artikelen. De bron is de publieke catalogus, geen leveranciersvoorraad- of inkoopfeed.

## Opgehaalde gegevens en bronhiaten

- **173** broncategorieën met hun producttoewijzingen en breadcrumbpaden.
- **41.899** specificatietabelwaarden, **586** verschillende labels. Negatieve antwoorden en nulwaarden blijven behouden; een ontbrekend veld wordt niet Nee.
- Productfotolinks bij **2.834**, lijntekeningen bij **2.511** en documentlinks bij **1.646** producten. Exploded views zijn als eigen mediaklasse bewaard. Binaire media niet volledig gedownload of visueel getest.
- Attribuutmetadata: **907** attributen, **860** als bronfilter gemarkeerd. Dit zijn brondefinities/opties, geen opdracht om 860 winkelfilters te activeren.
- Daadwerkelijke tabelwaarden, Compano-mediaverwijzingen en documenten uit iedere product-HTML geëxtraheerd. `custom_attributesV2` gaf in de bronproef een interne fout; API-beeldvelden bleken bij de proef een placeholder.
- **978** bronartikelen zonder categorie; **415** artikelen met minder dan drie niet-identificerende specificatiewaarden; **7** zonder gevonden productfoto; **36** met nulprijs; **27** met een expliciete samengestelde-settitel. Dit zijn overlappende reviewgroepen, geen optelbare foutentelling.
- Bekende inhoudelijke controles: 18184 heeft Luna in de titel versus Tainy in de bronbeschrijving; 32.3670 heeft een eerder maatverschil tussen bronnen. Voor 24.3710 bevestigt de fabrikant serie **304**. Het oudere Grant-klantnaamvoorstel is niet automatisch overgenomen. Eerder gecontroleerde tekeningmaten blijven in het bestaande proefproductdossier beschikbaar.

Geen ontbrekende maatassen, setinhoud, keurmerken, garantie, voorraad of levertijd verzonnen. Volledige opgehaalde fabrikantbeschrijvingen zijn bronmateriaal, geen eigen webshoptekst.

## Prijscontrole afgerond voor de bestaande koppelingen

Alle **2.841** fabrikantpagina's selecteren in hun actieve prijscomponent `regularPriceExclTaxKey` en `finalPriceExclTaxKey`; het bijbehorende `initialFinalPrice` sluit aan op de zichtbare adviesprijs. Dit controleert de daadwerkelijk gekozen prijsconfiguratie, niet alleen een algemene tax-helper in de pagina.

Shopify `shop.taxesIncluded` is vers als **true** teruggelezen. Alle **2.240** gekoppelde bestaande winkelprijzen zijn exact gelijk aan de fabrikantbronprijs vermenigvuldigd met de waargenomen bestaande winkelconventie **1,21**, op eurocenten afgerond. Voorbeeld 24.3710: **209,00 exclusief → 252,89 inclusief**. Het ruwe verschil is geen bewezen btw-fout of korting; bestaande prijzen hoeven op grond van deze vergelijking niet omlaag.

Voor **565** nieuwe kandidaten is een btw-genormaliseerd prijsvoorstel beschikbaar; de overige **36** nulprijsartikelen blijven in review. Dit zijn voorstellen op de bestaande winkelconventie, geen geverifieerde inkoop-/factuurprijzen of nieuwe prijsinstellingen. Geen prijswijziging uitgevoerd.

## Doelkoppeling — concrete voorstellen

Verse structuur: **221 collecties, 9 menu's, 246 productmetafielddefinities**. Alle bestaande Wiesbaden-productmetafields uitgelezen. Wiesbaden gebruikt **custom**, terwijl **specs** bij een andere merkmapping hoort. Er zijn 49 bestaande custom- en 62 bc_filters-definities.

`scripts/wiesbaden-import-plan.py` levert:

- Categorie-/breadcrumbvoorstellen met bestaande collecties en echte menupaden. Voor 24.3710: **Kranen → Wastafelkranen → Opbouw wastafelkranen**, lid van alle drie collecties. Afbouwdelen, losse inbouwdelen, fonteinsets en andere sets worden apart behandeld; one-pack betekent niet automatisch fonteinset.
- 1.506 classificaties via broncategorieregels, plus expliciete onderdeel-/set-/accessoireregels. **642** voorstellen komen alleen uit een expliciete productnaam; **287** hebben nog geen passende regel. Toepassingsonzekerheid blijft zichtbaar. Bestaande niet-voorgestelde collecties worden niet automatisch verwijderd.
- Volledige gegroepeerde specificaties voor het bestaande `custom.complete_specificaties` JSON-formaat. De huidige Wiesbaden-renderer leest dit volledige veld nog niet; de route eerst gecontroleerd testen. Hotbath-afscherming niet stil verruimen.
- Losse custom-voorstellen: **8.940** getypeerde bronwaarden als kandidaat. De andere tabelwaarden blijven volledig beschikbaar in de gegroepeerde lijst; niet voor ieder bronlabel een nieuw Shopify-veld aanmaken.
- **8.415** expliciete filterveldvoorstellen, waarvan **7.959** getypeerde kandidaten. Generieke bronwaarden en onduidelijke getallen blijven in review. Geen ongefundeerde kleur-, maat- of nano-coatingafleidingen.
- Bij veldvoorstellen staan huidige waarde, voorgestelde waarde, huidig updatedAt en wijzigingsstatus. 4.932 huidige custom-waarden zijn gelijk, 1.753 nieuwe velden zijn kandidaat en 685 bestaande waarden verschillen; overige waarden zijn nieuwe-productvoorstellen of niet rechtstreeks gekoppeld. Bron-Kunststof/Overig mag een specifiek bestaand materiaal niet blind vervangen.

`bc_data.filter_manifest` en de externe VPS-index hebben een eigen contract. Dat contract en de herindexering zijn nog niet voor deze import gevalideerd; alleen een metafield vullen bewijst niet dat zoeken/filteren is bijgewerkt. Geen indexverversing of live filtertest geclaimd.

## Controles en overdracht

**28 uitvoerbare tests PASS:** 13 bron-/prijs-/identiteitstests en 15 mappingtests. Onder meer exacte SKU, leading zeroes/punctuatie, EAN uitsluiten, leeg versus Nee, breadcrumbs, mediaklassen, bronhost, onvolledige inventaris, gekozen btw-component, geen dubbele btw, nulprijsblokkade, hoofdproduct versus onderdeel/meegeleverd product, expliciete eenheden en conflicterende filteraliassen.

Alle tien bestaande proefartikelen geëxtraheerd: 20.3755, 20.3756, 32.3411, 32.3594, 32.2510, 32.3670, 38.4125, 41.3540, 24.3710, 29.8007. Dit is geen inhoudelijke goedkeuring van ieder feit; bijvoorbeeld 32.3594 heeft slechts drie tabelvelden.

Volledige HTML-run: nul downloadfouten. Daarna alle 2.841 opgeslagen pagina's opnieuw uit de cache verwerkt met parser **2026-10-19.3**. **2.872** responsehashes gecontroleerd: 2.841 HTML en 31 API-responses. Nul SKU-mismatches en nul HTML/API-prijsconflicten. ZIP-integriteit en een pakketmanifest met bestandshashes gecontroleerd. Geen Windows-wrappers of echte import/browserchecks geclaimd.

De besloten gegevensoverdracht heet `BadkamerCity_Wiesbaden_datarun_20261019.zip` en bevat gestructureerde bronfeiten, bronverwijzingen/hashes, winkelmomentopname, nieuwe-/bestaande-/ontbrekende-productlijsten, merkcontrolelijsten, categorie-, specificatie-, filter- en prijsvoorstellen, media/documentlinks en leeswijzer. Geen direct uploadbare Shopify-product-CSV of publicatieklaarverklaring. Volledige fabrikantproza en website-HTML zijn geen onderdeel van het transportpakket; de ruwe werkcache blijft buiten publieke Git.

Collector: `scripts/wiesbaden-data-run.py`; mapping: `scripts/wiesbaden-import-plan.py`; tests: beide overeenkomstige `test_*.py`-bestanden. Alleen-lezen, geen Shopify-mutaties of credentials. Gebruik een besloten runmap buiten deze publieke repository.

```sh
python scripts/wiesbaden-data-run.py catalogue --run-dir /private/run-directory
python scripts/wiesbaden-data-run.py pages --run-dir /private/run-directory --workers 8
python scripts/wiesbaden-data-run.py build --run-dir /private/run-directory
python scripts/wiesbaden-import-plan.py --run-dir /private/run-directory
```

De build/mapping vereisen ook de complete actuele Shopify-snapshot, volledige winkel-SKU-index, structuur- en metafieldmomentopname; die zijn niet uit de themarepository te reconstrueren. Voor een echte wijziging gelezen velden opnieuw controleren, een herstelbasis voor de wijziging bewaren en read-after-write uitvoeren.

## Openstaande toepassing

Eigen productteksten, korte titels, SEO en beeld-alts maken op gecontroleerde feiten. Bronconflicten en onduidelijke categorieën oplossen, maten met assen/eenheden verifiëren, de Wiesbaden-specificatieweergave plus manifest/indexroute testen en nieuwe kandidaten op merk, setinhoud, media en prijs beoordelen. Voorraad/levertijd niet uit deze publieke catalogus afleiden.

**Exact één volgende handeling:** werk de importproef voor de bestaande tien proefproducten uit op deze bronset, inclusief eigen content en de werkelijk gebruikte PDP-/filterroute, voordat grotere groepen worden toegepast.
