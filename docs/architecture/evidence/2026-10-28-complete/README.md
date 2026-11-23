# Bewijs DOC-02C: brede documentatie van de winkel

Bronmoment **28 oktober 2026**. MAIN bij aanvang 195818389770, Smooth winkelwagen pop-up. Geen product-, cart-, theme-, checkout- of indexmutaties uitgevoerd. Alleen Git-documentatie en een offline naslagbuilder gewijzigd.

| Bestand / bron | Methode en resultaat | Grens |
| --- | --- | --- |
| [Manifestcheck](manifest-check.json) | 26 gepagineerde reads, 1.262 unieke paden; pad/MD5/grootte gelijk aan DOC-01 | Metadata bewijst geen volledige nieuwe inhoudsread |
| [Bronindex](../../reference/source-index.json) | 557 lokale bronnen gereconstrueerd uit exacte Git-blobs/eerdere bytegelijke reads + 75 verse bodyreads; 556 bytegelijk, settings_data.json wijkt af | 705 bestanden deze reconstructie manifest-only; eerdere DOC-01-capture/DOC-02-datacontroles blijven gedateerd bewijs |
| [Afhankelijkheden](../../reference/dependencies.json) | 955 letterlijke Liquid-/JSON-sectieverwijzingen; JSON/schema's parsebaar | Geen volledige dynamische parser of runtimebereikbaarheid |
| [Admin-inventaris](admin-inventory.json) | Alle 226 collecties, 119 Pages, negen menu's, één blog/artikel, 120 redirects, zeven apps, één markt; paginering afgesloten | Alleen veilige metadata; geen nieuwe private productexport of inhoudelijke feitenvrijgave |
| [HTTP-checks](http-checks.json) | 35 onafhankelijke anonieme GET's: 34 keer 200, bedoelde niet-bestaande route 404; 56 JSON-LD-blokken parsebaar | Geen JavaScript/assets uitgevoerd, geen browser-/mobiel-/focus-/performancetest |
| [Filter-API](filter-api-checks.json) | Vier read-only zoek-POST's, alle 200; vorm en Origin-header passend; Wastafelkranen 573, Inloopdouches 305, aansluitend op HTML-context | Geen browserpreflight, geen volledige product-ID-/prijs-/index-/filtercombinatievrijgave |

De HTTP-set omvat alle 17 toegewezen categoriehubs, standaard collectievoorbeelden, zoek-/nultermroute, contact, begrippenlijst/-pagina, standaardterugvalvoorbeeld, Sunshowerlanding, wishlist, merkenoverzicht, blog/artikel, login/password en 404. HTTP 200 op login volgt naar Shopify-authenticatie; password volgt naar home. Dit zijn geen succesvolle login-/passwordmodustests.

De footer levert in de serverresponses de tien labels zonder link; de homepage heeft geen actieve hero en geen inhoud van het ongeconfigureerde populaire-productenblok. Een lege Shopify-sectionwrapper is geen zichtbaar productblok.

De aanvullende verzendread heeft één profiel, drie zones en vier methodedefinities volledig gepagineerd gelezen; prijzen/voorwaarden en lege ondersteunde-walletlijst staan in de veilige Admin-metadata. Checkout/accountconfiguratie is expliciet geweigerd. De eerdere te dure gecombineerde query is verkleind; alleen de geslaagde complete read onderbouwt de gerapporteerde rates. Geen rate gewijzigd of checkoutofferte aangevraagd.

## Volledige begrippenverbindingskaart

[109 gerenderde links](glossary-links.json) gekoppeld aan alle 120 redirects en 119 Pages: 108 gepubliceerde doelen met passende template, nul loops, één ontbrekend doel. Gerichte extra GET voor Hygro(meter) bevestigt 404 op /pages/hygrometer. Dit is een extra foutgerichte read naast de algemene 35-route-set. Geen 109 volledige browser-/inhoudscontroles en geen redirectmutatie.

## Beperkte echte browsercontrole

Op desktop 1363×936 zijn footerpanelstaten en de tien niet-links bevestigd, plus de lokale begrippenzoekcyclus 109→1→0→109 en de link naar Rimless met zes inhoudskaarten/TOC-entries. Zie [browserwaarnemingen](browser-observations.json). De browser had een bestaande previewcontext; geen claim van een anonieme browser. Geen cartinhoud/opslag gelezen of gewijzigd, geen formulier verzonden, geen screenshots opgeslagen. Een eerste DOM-read tijdens navigatie was nog leeg; de geladen pagina is vervolgens bevestigd. Geen defect of animatieduur uit die tussenstaat afgeleid. De tool bood geen viewportresize; mobiel blijft NOT_TESTED.

## Privacy en reproduceerbaarheid

Publieke proof bevat geen ruwe HTML, paginabodies, productrecords, order-/klant-/cartinhoud, secrets, appkeys of OAuth-querystrings. Raw responses en gereconstrueerde themabron staan buiten de Git-repository. De private productexport van DOC-01 blijft afzonderlijk.

`scripts/build_site_reference.py` op de actieve branch bouwt de technische bronreferentie opnieuw vanuit expliciete inputs. HTTP-checks zijn een gedateerde meting; HTML-bytehashes zijn tijdgebonden en worden niet als een stabiele fixture behandeld. Admin.md en inhoudelijke dossiers zijn handmatig beoordeelde uitleg naast de gegenereerde kaart.

Open: settingspariteit, mobiele/keyboard-/touchstaten, gehoste checkout/accountconfiguratie, verse VPS-/appbron, Google-/analytics-/deploy-/restoregegevens en operationele bestelcontrole. Zie [dekking](../../COVERAGE.md). “Gedocumenteerd als open” is geen afgeronde audit.
