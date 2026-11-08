# Footer: live standaard en broncontract

**Actuele stand — 8 november 2026 · CONTACT-RETURNS-01. FOOTER-FIX-01: OWNER_PUBLISHED / PUBLIC_HTML_VERIFIED.** De eigenaar heeft **BadkamerCity - Eenduidige footer 8 nov (196354474250)** gepubliceerd. Verse Admin-rol: MAIN, `updatedAt=2026-11-08T16:37:38Z`. Beide gewijzigde footerfiles zijn exact op MD5 teruggelezen. **Veertien publieke HTTP-routes zonder previewparameter** tonen één identieke standaardfooter met telefoon, e-mail en gelabeld contact-/retouradres. Dit is nieuwe bron-/HTML-nacontrole, geen nieuwe desktop-, mobiele of fysieke telefoonproef. [Actuele publicatie- en reparatiestatus](../../repairs/2026-11-08/contact-and-returns/README.md).

Het huidige contract blijft: `compact_homepage=false`; **17 blocks (4 service, 10 categorie, 3 informatie)** binnen maximum 18, met `category.limit=10`. De gewone footer gebruikt dezelfde renderer, bestaande CSS/JavaScript en retour-/offerte-/policy-/betaalguards. De eerdere vraag om deze footer te publiceren is hiermee afgehandeld.

De **Contact Page is nu ook live aangevuld** met telefoon `+31685887536`, info@badkamercity.nl, Zichtenburglaan 150, 2544 EB Den Haag als contact-/retouradres op afspraak, en retour-/beleidslinks. Twee contact-SEO-waarden zijn met null-compare-and-set toegevoegd; het native formulier blijft behouden. De vier kapotte tekencoderingen in de RapoWash-body zijn gericht hersteld met behoud van SEO, status en identiteit. Beide wijzigingen zijn publiek teruggelezen.

**Volgend concept:** UNPUBLISHED **196368531722 — BadkamerCity - Retourinformatie 8 nov**. Eerst 1.387/1.387 paritair met de nieuwe MAIN na overname van de twee footerfiles; daarna precies vier retour-/homepage-/localebestanden gewijzigd. Status **PREVIEW_IMPLEMENTED_NOT_PUBLISHED**. Vier Liquid-controles en exacte readback zijn geslaagd; aanvullende publieke previewcontrole volgt in het nieuwe dossier. Dit concept wijzigt de footer niet en mag niet als gepubliceerd worden beschreven. Native policyopmaak blijft geblokkeerd op `write_legal_policies`; btw-identiteit, verzending, mail en aankoopmeting blijven afzonderlijk open.

## Historische conceptopbouw — FOOTER-FIX-01 vóór eigenaarspublicatie


**Historisch conceptcheckpoint — 8 november 2026 · FOOTER-FIX-01 · toen PREVIEW_IMPLEMENTED_NOT_PUBLISHED.** Het bestaande **UNPUBLISHED 196354474250 — BadkamerCity - Eenduidige footer 8 nov** bevat de gedeelde standaardfooter. MAIN **196328685834** is ongewijzigd. [Reparatie, bronbewijs en testgrenzen](../../repairs/2026-11-08/footer-and-content/README.md).

Eerst zijn zes actuele SEO-/headerbestanden uit verse MAIN exact overgenomen; daarna was het concept **1.387/1.387 bestanden paritair**. De footerwijziging raakt vervolgens precies twee bestanden: `sections/footer.liquid` en `sections/footer-group.json`; **1.385 overige bestanden blijven gelijk**.

In het concept staat `compact_homepage=false`, met **17 blocks: 4 service, 10 categorie en 3 info**. Naast het totale maximum van 18 bleek de oorspronkelijke `category.limit=6` een afzonderlijke schemabeperking; die is gericht naar **10** gezet. Eerst het schema uploaden, daarna de section group: de nieuwe group is vóór die schemawijziging niet geldig. De bestaande CSS, JavaScript, retour-/offerteguards en echte policy-/betaalbron zijn behouden.

De conceptfooter gebruikt winkelbrede homeverwijzingen `/#HomeDelivery`, `/#HomeAdvice` en `/#HomeInspiration`. Tijdelijke telefoon **06 85887536**, e-mail en het duidelijk gelabelde contact-/retouradres **Zichtenburglaan 150, 2544 EB Den Haag, bij Harry Suiker** zijn via de bestaande instellingen ingevuld. Dit is geen claim over de geregistreerde juridische vestiging. De live footer blijft tot publicatie de hieronder beschreven oorspronkelijke configuratie gebruiken.

De afzonderlijke live inhoudscorrecties zijn wel uitgevoerd: **Antikalk heeft publiek één H1** na omzetting van de body-H1 naar H2; **RapoWash heeft eigen `global.title_tag` en `global.description_tag`** na compare-and-set-correctie. De publieke HTML-readback slaagt. Reukslot, pagina-identiteiten, publicatiestatussen en overige bodyinhoud zijn behouden. Native policies zijn niet gewijzigd: `shopPolicyUpdate` mist de vereiste `write_legal_policies`-scope. Footerpublicatie en de resterende policy-/runtimechecks blijven apart.

## Historische live-audit — DOC-LIVE-01, vóór de conceptreparatie

**Bronmoment: 8 november 2026 · VERIFIED_THEME / VERIFIED_HTML.** MAIN **196328685834 — BadkamerCity - Homepage SEO 8 nov**, gelezen met `updatedAt=2026-11-08T11:49:21Z`. [Centraal auditrapport](../../audits/2026-11-08/README.md), [bron-/configuratieregister](../../audits/2026-11-08/safe-footer-register.json) en [14 routeprobes](../../audits/2026-11-08/footer-route-matrix.json). Deze actualisering veranderde geen themacode, instellingen of publicatie. Nieuwe mobiele-/runtimecontrole is niet uitgevoerd.

## Bewezen oorzaak: twee renderpaden

`layout/theme.liquid:339` rendert na `content_for_layout` globaal `{% sections 'footer-group' %}`. In `sections/footer-group.json:189` staat **`compact_homepage: true`**. `sections/footer.liquid:1–2` kiest daardoor bij `request.page_type == 'index'` het snippet **`bc-home-footer`**; de `else` rendert de standaardfooter **`.bcf-v2.bcf-v3`**. De home-afwijking komt uit deze expliciete branch.

De standaardkolommen lezen eigen `service`-, `category`- en `info`-blocks. Het compacte home-assortiment leest **`linklists['main-menu']`**; de andere homelinks komen uit vaste routes/lokalisatietekst en lokale homepageanchors. Een wijziging in Shopify-menu **Voettekstmenu** verandert die standaardkolommen dus niet automatisch. Beide renderers halen de onderste beleidslinks uit **`shop.policies`**.

| Onderdeel | Homepage | Overige onderzochte storefront-routes |
| --- | --- | --- |
| Renderer / class | `snippets/bc-home-footer.liquid` / `.bch-footer` | `sections/footer.liquid` / `.bcf-v2.bcf-v3` |
| Linkkolommen | Klantenservice 4; Assortiment 11; Over Badkamercity 3 | Klantenservice 3; Ons assortiment 7; BadkamerCity 1 |
| Assortiment | Tien hoofdgroepen + `/collections` | Zes categorieblocks + `/collections/all` |
| Extra homebestemmingen | `#HomeDelivery`, `#HomeAdvice`, `#HomeInspiration` | Deze advies-/inspiratie-/bezorglinks ontbreken |
| Merk / contactopbouw | Compact logo, e-mail | Trustbar, merkintro, e-mail en contact-CTA |
| Telefoon / adres / betaaliconen in gelezen HTML | Geen / geen / 0 | Geen / geen / 0 |
| Beleidslinks | Vijf | Dezelfde vijf |
| Bronstijl | Achtergrond `#102b43`, basis 14px, logo 185px | Achtergrond `#1a253f`, basis 16px, logo 240px |
| Details | Geen server-`open`; native details, geen standaardfootercontroller | Server-`open`; controller synchroniseert mobiel/desktop |

De linktotalen zijn **25 op home** en **19 op de standaardfooter**, inclusief logo, mail, CTA en policies. De stijlwaarden zijn bronwaarden; er is geen nieuwe computed-style- of contrastmeting. Nul betaaliconen bewijst niet dat betaalmethoden uitstaan. Cookievoorkeuren ontbreken in de servermarkup van de voetertest; runtime-injectie door de privacylaag is daarmee niet uitgesloten. De eerdere browserwaarneming van cookieknoppen blijft apart gedateerd bewijs.

## Vier verse bronbestanden passen exact bij Git

Op het oorspronkelijke auditmoment waren deze vier kernbestanden bytegelijk aan `shopify/current/` op broncommit `1b5108a2`. De twee latere footerwijzigingen hierboven horen bij het ongepubliceerde concept. Dat is gerichte footerpariteit, **geen** volledige themepariteit: globaal blijven 15 afwijkende en 9 alleen live aanwezige bestanden over.

| Themebestand | Live MD5 | Git blob SHA |
| --- | --- | --- |
| `layout/theme.liquid` | `21a1c2db077ec6ebe5c5cd41161ca187` | `f5e6b33ee61e461876cfa308c08ff92a8f62d236` |
| `sections/footer-group.json` | `f57d42afd9dbbc8faac64d21bda9bfff` | `e47adf599847391c081b1e369fa413c6684421c8` |
| `sections/footer.liquid` | `7e413995480f5066044e3e43805b5388` | `3ad0e8372c0e2b558a1e258b97d49135c3e3632a` |
| `snippets/bc-home-footer.liquid` | `63943bf38ac942f65e342cc0348cb992` | `dd7f653d8d2be745051288198792cdf4a0b2901f` |

## Historische auditconfiguratie: 18 blokken, 8 lege bestemmingen

De sectie heeft **18 blocks bij schema-maximum 18**. Actuele code verbergt blocks zonder URL buiten `request.design_mode`; de oude tien zichtbare tekstlabels uit FOOTER-F01 zijn dus geen actuele telling.

| Type | Bestaande werkende blokken | Lege blok-ID's en labels |
| --- | --- | --- |
| service | `service_1` Contact → `/pages/contact`; `service_4` Retour aanmelden → `/pages/retour-aanmelden`; `service_6` Zoeken → `/search` | `service_2` Veelgestelde vragen; `service_3` Bezorgen & afhalen; `service_5` Garantie & service |
| category | `category_1..6`: Badkamermeubels, Kranen, Douches, Toiletten, Wastafels, Tegels → gelijknamige bestaande collecties | Geen |
| info | `info_4` Onze merken → `/collections?view=merken` | `info_1` Over ons; `info_2` Badkamerinspiratie; `info_3` Badkameradvies; `info_5` Showroom; `info_6` Zakelijk |

Placeholdermodus en betaalvoorbeelden staan uit; `payment_enable` en `show_policy` staan aan; `quote_link_enabled` staat uit. Telefoon, adres en openingstijden zijn leeg; e-mail en contact-CTA zijn ingesteld. Contactgegevens niet uit een oud bronbestand terugplaatsen. De door de eigenaar opgegeven tijdelijke telefoon en het contact-/retouradres vragen een bewuste, juiste publicatie; een retouradres is niet automatisch het geregistreerde vestigingsadres.

De vijf bestaande policies zijn privacy, terugbetaling, contactgegevens, voorwaarden en wettelijke kennisgeving. **`/policies/shipping-policy` geeft 404**; geen werkende verzendbeleidslink suggereren. Voorwaarden en wettelijke kennisgeving tonen in de verse response ge-escapete HTML: policybestaan is geen bewijs van bruikbare opmaak.

## Historisch voorgesteld footercontract — inmiddels gepubliceerd

Hergebruik de bestaande **standaard `.bcf-v3`** voor alle gewone storefront-paginatypen. In een brongecontroleerd **UNPUBLISHED** concept kan `compact_homepage=false` beide routes naar deze renderer leiden. Bouw geen derde footer. Werk tegelijk de inhoud bij, zodat de vier ontbrekende hoofdcategorieën en advies/inspiratie niet verdwijnen.

Een concrete indeling heeft **17 geconfigureerde blocks**: 4 service, 10 categorie, 3 info. Daarvoor de acht huidige lege slots herbestemmen of verwijderen; niets toevoegen boven het schema-maximum van 18. Mogelijke hergebruikmapping:

| Gewenste groep | Blocks / bron |
| --- | --- |
| Service 4 | Bestaande `service_1`, `service_4`, `service_6`; `service_3` pas vullen met een bestaande openbare, inhoudelijk juiste verzend-/afhaalbestemming |
| Categorie 10 | `category_1..6` behouden; lege `service_2`, `service_5`, `info_1`, `info_5` omzetten naar category voor Baden, Spiegels en verlichting, Accessoires, Verwarming en ventilatie |
| Info 3 | `info_4` Onze merken; `info_3` advies → `/#HomeAdvice`; `info_2` inspiratie → `/#HomeInspiration` |
| Overtollig | Leeg `info_6` verwijderen; totaal 17 |

Een ongebruikte servicebestemming blijft verborgen totdat de juiste openbare informatie bestaat. Homeanchors moeten bij gedeeld gebruik vanaf de winkelroot verwijzen; een lokale `#HomeAdvice` op een productpagina is geen correcte route. Gebruik bij eventuele implementatie de bestaande Shopify-rootroute voor locale-/subpadgedrag. Houd de algemene assortimentlink consistent en controleer categorievolgorde tegen `main-menu`.

Beleidslinks blijven automatisch uit `shop.policies`; geen duplicaten in de drie kolommen. Alleen echte ingeschakelde betaalmethoden tonen. Bewaar de guards **`bc-returns-url`** en **`bc-footer-quote`** en de huidige editor-/cleanupbescherming. Native checkout en extern gehoste accountpagina's hebben een aparte Shopify-shell; één storefrontfooter betekent geen identieke checkoutmarkup.

## Gecontroleerde routes en open regressie

De gerichte voetertest las **12 representatieve routes + 2 grensgevallen**: home; algemene PDP; standaardcollectie; meubelhub; contact; retouraanmelding; refundpolicy; zoeken; lege cart via GET; merkengids; Sunshowerlanding; begrippenlijst; Sunshower-PDP; bewuste 404. Elke response bevat één footer. Alleen home heeft `.bch-footer`; de andere dertien hebben dezelfde standaardstructuur. De bredere 364-routeset bevestigt deze classverdeling: 1 home en 363 standaardresponses, inclusief foutpagina's.

| Testlaag | Huidig bewijs | Nog nodig bij voorstel |
| --- | --- | --- |
| HTML / routes | 14 gerichte responses; publieke linkset, groups, policies en hashes | Dezelfde routes in concept; geen verloren links, geen dode lokale anchors |
| Desktop / mobiel | Actuele bronbeslissing; oude beperkte desktopwaarneming en geïsoleerde FT-01/02 | Echte desktop en 390px; 749↔750px; touch, keyboard, focus, lange labels |
| Lifecycle | Standaardcontroller heeft init/cleanup en section load/unload | Concept met herhaalde load/unload en reduced motion; homepage-/standaardpad na wijziging |
| Commerce / privacy | Lege cart gelezen; geen cartmutatie in voetertest | Ook gevulde cart na afgesproken test; cookievoorkeuren na runtime-injectie; echte betaaliconen |

De semantische voetervingerafdrukken van de gerichte set zijn home `190dbaf8025cd312bf8b68e7a426c46ac432ccd6623bb06f711a880cf6e63023` en standaard `25359a8109c6ff6f9e3e8b4b865195ffa1bc8daaccb7b082cbc5901197dee178`. Ze dekken de gemeten structuur en linkinhoud, geen browsergedrag.

## Historie en technische verdieping

- **28 oktober — FOOTER-F01:** tien URL-loze labels werden als tekst getoond; historische meting en desktopwaarneming blijven in het [toenmalige bewijs](../evidence/2026-10-28-complete/README.md).
- **31 oktober — FIX-01:** lege bestemmingen buiten editor verbergen en bestaande merkengids koppelen; [gedateerd dossier](../../repairs/2026-10-31/README.md). Die configuratiegrens is op 8 november opnieuw inhoudelijk gelezen, nu met acht lege slots.
- **8 november — FOOTER-F02:** twee werkelijke live renderers en verschillende linkdekking bewezen; de harmonisatie is later door de eigenaar gepubliceerd; de actuele bron-/HTML-nacontrole staat bovenaan. De oorspronkelijke live-audit blijft gedateerd bewijs.

[Footerlifecycle](micro/FOOTER_LIFECYCLE.md) · [historische instellingenreferentie](../reference/sections/footer.md) · [eenheidskaart](../CONSISTENCY.md) · [bevindingen](../FINDINGS.md).
