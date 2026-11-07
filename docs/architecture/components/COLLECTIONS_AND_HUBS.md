# Collecties, categoriehubs en merken

Bronmoment **28 oktober 2026**. De verse Admin-read bevat **226 collecties**: 209 zonder suffix, 16 `category-landing`, één `bc-meubelhub`. De templatekeuze is een Admin-toewijzing; de boomstructuur komt grotendeels uit menu's, niet uit een ingebouwd parentveld van Shopify-collecties.

## Drie actieve routefamilies

| Route | Renderer | Inhoudsbron |
| --- | --- | --- |
| Gewone collectie | `collection.json` → banner, productgrid, keuzeadvies | Collectieproducten, beschrijving, menu/context; native/externe filters |
| Categorieoverzicht | `collection.category-landing.json` → `main-category-landing` + advies | Menu-kinderen of handmatige subcategorieblocks, extra/SEO-inhoud |
| Badkamermeubels | `collection.bc-meubelhub.json` → `bc-meubelhub` | Eigen categorie-/merkblocks, vier selectiemenu's, collectieomschrijving en beelden |

`main-collection-category-landing` bestaat daarnaast als bestand. Het bestaan van die naam is geen bewijs dat de 16 actuele toewijzingen die variant gebruiken: de JSON verwijst naar **main-category-landing**. Houd oude, beschikbare en daadwerkelijk toegewezen varianten uit elkaar.

## Gedeelde categorieboom en bestemmingen

`bc-category-children` zoekt huidige collectie-identiteit in de eerste twee menuniveaus en verzamelt bijbehorende kinderen. Een expliciet `children_menu` kan die selectie vervangen. De renderer dedupliceert op resource-ID of URL en slaat een link naar de huidige collectie over. Beeldprioriteit: collectiebeeld, eerste productafbeelding, passend overrideblock waar geconfigureerd. Een ontbrekend beeld krijgt een placeholder.

`bc-category-destination` gebruikt een echte collectiebestemming wanneer beschikbaar. Een oude zoeklink kan naar een inmiddels bestaande collectie met de getitelde handle worden omgezet. Een lege/#-bestemming wordt een productzoekroute op de titel. Dit is een navigatieterugval, geen bewijs dat de gewenste categorie inhoudelijk compleet is.

Voor de gedeelde historische Toebehoren-collectie bestaat een expliciete ID-uitzondering met groepen per hoofdafdeling. Verwijder die niet door alleen titels te dedupliceren. Collectie-ID, menucontext en bestemming horen bij het contract.

## Beschrijvingen en SEO-splits

`[SPLIT]`/`[split]` verdeelt bepaalde collectie- en sectieteksten in boven-/onderinhoud. `main-category-landing` ondersteunt meerdere HTML-verpakkingen van dit token. Extra content, subcategoriekaarten, gerelateerde links en productgebied hebben afzonderlijke instellingen. De menugestuurde bron kan bovendien per huidige collectie een `category_menu`-block kiezen.

De verse Admin-read bevestigt **drie styleblokken in de omschrijving van Badkamermeubels**; andere ontvangen collectiebodies bevatten geen style-/scriptblokken. De huidige meubelhub gebruikt `bc-content-without-styles` vóór het splitsen. De oude Admin-CSS bestaat dus nog, maar aanwezigheid alleen bewijst niet dat deze via de huidige hub wordt uitgevoerd. Controleer andere consumers voordat de data ooit wordt opgeschoond.

## Meubelhub en merkenoverzicht

De meubelhub heeft categoriekaarten, groepen type/maat/stijl/merk, merkrail, inspiratie, service en advies. Categoriekaarten mogen een lege collectie alleen linken als `allow_empty` dat toestaat. Zonder ingerichte maat-/stijlmenu's zijn bepaalde keuzes bewust tekst met een aanvulmelding. Merken kunnen uit geconfigureerde blocks of bestaande vendors komen.

`/collections?view=merken` gebruikt `list-collections.merken.json` → `bc-brand-directory`, sorteert vendors natuurlijk en beperkt de lijst expliciet tot Hotbath, JEE-O, Sunshower, The Mosaic Factory en Wiesbaden. Dit is een gecureerd merkenoverzicht. Het is niet `/pages/merken`; de gelijknamige Page is bij de verse read ongepubliceerd. Het standaard `/collections`-overzicht heeft een andere renderer.

## Advies en onderhoud

`bc-collection-advice` bepaalt de kranenfamilie door collectie-ID in de kranenmenutak. De vertaalgroep wordt `bc_collection.faucets` of `.general`; drie advieskaarten, optionele kranen-FAQ en een contactblok volgen instellingen. Een collectiontitel hernoemen is geen vervanging voor die identiteit-/menulogica.

Wijzig de menustructuur in Navigatie, toewijzing/omschrijving bij Collecties en presentatie in Theme Editor/code. Na wijziging: huidige/child/legacy Toebehoren, ontbrekende beelden, lege collecties, menuoverride, SPLIT, zoekterugval, desktop/mobiel en echte links controleren. Alle 226 Admin-toewijzingen zijn geïnventariseerd; niet alle producten of filtercombinaties daarvan zijn interactief getest.

[Alle toewijzingen](../reference/ADMIN.md) · [Secties en instellingen](../reference/SECTIONS.md) · [Filters](FILTER_ENGINE.md) · [Bronhashes](../reference/source-index.json).
