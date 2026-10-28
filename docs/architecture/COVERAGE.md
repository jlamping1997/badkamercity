# Documentatiedekking: wat compleet is en wat nog niet

**28 oktober 2026 · DOC-02C brede winkelbeschrijving.** De eigenaar vraagt volledige documentatie vóór verdere stapsgewijze verbetering. De scope is de huidige BadkamerCity-winkel: storefront, product-/contentdata, beheerinstellingen, integraties, bestelketen en onderhoud. De [centrale status](../LIVE_STATUS_AND_NEXT_STEPS.md) noemt de actuele volgende handeling.

Een dossier kan bestaan terwijl broncontrole of praktijkcontrole ontbreekt. Daarom tellen we bestanden of woorden **niet** om een voltooiingspercentage te verzinnen. Alle 1.262 themapaden zijn geregistreerd; dat is geen 100% functionele of operationele voltooiing. Een ontoegankelijke backend blijft inhoudelijk open, ook wanneer de beperking helder is beschreven.

## Vier afzonderlijke afsluitcriteria

| Laag | Klaar wanneer |
| --- | --- |
| Bron | Actieve versie/toewijzing, relevante code/data/config en externe bron zijn controleerbaar; uitzonderingen opgelost |
| Uitleg | Doel, beheerlocatie, activering, input/output, toestanden, fouten, afhankelijkheden en herstel zijn inhoudelijk beschreven |
| Praktijk | Passende representatieve desktop/mobiel/toetsenbord-/foutscenario's zijn daadwerkelijk uitgevoerd en gedateerd |
| Bedrijfswerking | Verkooprelevante data, afspraken, rollen en bestel-/herstelprocessen zijn gecontroleerd binnen afgesproken scope |

**Volledige documentatie** vereist bron + uitleg voor ieder toepasselijk onderdeel, met concrete praktijkresultaten óf nog open verificaties. **100% completion van de webshop** vereist daarnaast de passende praktijk- en bedrijfscontroles; het ene percentage vervangt het andere niet. Een expliciete open verificatie mag niet worden gepresenteerd als een afgeronde controle.

## Dekkingsmatrix

| Onderdeel | Uitleg / ingang | Bronstand | Resterende afsluiting |
| --- | --- | --- | --- |
| Fundament, libraries, ontwikkeltools | [Fundament](components/FOUNDATIONS_AND_TOOLING.md) | Thema/codepins bekend | Werkelijke Windows-/CLI-/deployomgeving |
| Alle templates, secties, snippets en assets | [Technische naslag](reference/README.md) | 1.262 paden; 556 bytes gelijk in verse reconstructie; één settings-mismatch; 705 manifest-only, eerder DOC-01-capture | Settingspariteit; dynamische bereikbaarheid per component |
| Header en desktopmenu | [Navigatie](components/NAVIGATION_AND_STORAGE.md) | Actuele code + negen Admin-menu's | Keyboard, snelle wissels, overlaycombinaties |
| Mobiel menu en zoeken | [Navigatie](components/NAVIGATION_AND_STORAGE.md) | Bron-/HTML-keten bekend | Echte mobiele drawer/predictive-search |
| Footer en contactkolom | [Footer](components/FOOTER.md) | Actuele code/config + server-HTML | Tien ontbrekende bestemmingen; mobiel/resize |
| Homepage en eigen kaarten | [Homepage](components/HOMEPAGE.md) | Template, guards en server-HTML | Responsive/cascade; expliciete inhoudskeuzes |
| Categoriehubs en meubelhub | [Collecties](components/COLLECTIONS_AND_HUBS.md) | Alle 226 toewijzingen; alle 17 toegewezen hubs via HTTP | Mobiel, menuwijzigingen en randgevallen |
| Native lijsten en zoeken | [Kaarten/filters](components/PRODUCT_CARDS_AND_FILTERS.md) | Native bron/HTML | Filter-/history-/nulresultaatinteractie |
| Externe filterfrontend | [Filterketen](components/FILTER_ENGINE.md) | Actuele code; vier publieke API-reads | Combinaties/ranges, timeout/fallback, CORS-preflight, mobiel |
| Filterbackend/index/sync | [Filterketen](components/FILTER_ENGINE.md) | Historische serverdocs + actuele publieke response | Verse bevoegde VPS-bron, index/schema/profielen/jobs/restore |
| Alle productkaartvarianten | [Kaarten/filters](components/PRODUCT_CARDS_AND_FILTERS.md) | Renderer-/pijl-/dataketen bekend | Dezelfde functie/staat/viewport visueel vergelijken |
| Algemene PDP en specificaties | [Productpagina's](components/PRODUCT_PAGES.md) | Actuele code + private veldregisters | Alle actieve native variant-/scopegevallen |
| Kleuren/uitvoering/lengte | [Keuzes](components/PRODUCT_CHOICES.md) + [matching](components/micro/CHOICE_RESOLUTION.md) | Bron/replay, gegenereerde-data-evidence | Routebrede browser-/terugknopcases |
| Inbouw, sets en accessoires | [Aantallen/identiteit](components/micro/QUANTITY_AND_IDENTITY.md) | Afzonderlijke guards getest | Volledige add/recoveryketen geïsoleerd testen |
| Sunshower landing/PDP/gallery | [Productpagina's](components/PRODUCT_PAGES.md) + [acties](components/micro/SUNSHOWER_ACTIONS.md) | Bron, 72 cataloguscombinaties, beperkte desktopactie | Pending-lockbevinding; touch/viewer/mobiel |
| Cart en popup | [Cart](components/CART_AND_FEEDBACK.md) + [popup](components/micro/CART_NOTIFICATION.md) | Bron/replays | Missing-sectionbevinding, complete caller/browserfocus |
| Wishlist, bewaren en herstellen | [Opslag](components/NAVIGATION_AND_STORAGE.md) | Sourcecontract bekend | Geblokkeerde opslag, oude variant, gevulde-cartrestore |
| Begrippenlijst en uitlegpagina's | [Content](components/CONTENT_AND_FORMS.md) | 119 Page-records, lijstblocks, 120 redirects | 109 verbindingen gecontroleerd: één 404 open; bodykwaliteit/mobiel open; desktopsearch en één TOC bevestigd |
| Blog, advies en formulieren | [Content](components/CONTENT_AND_FORMS.md) | Actuele renderers, één blog/artikel, HTTP | H2-variaties, formulierfouten en mailbezorging |
| Accounts en systeempagina's | [Accounts/systemen](components/ACCOUNTS_AND_SYSTEM_PAGES.md) | Bron + loginredirect/404 HTTP | Accountmodel/config, testaccount/recovery, giftcardcontext |
| SEO, structured data en talen | [SEO](components/SEO_AND_LOCALIZATION.md) | Headcode, redirects/locales; 56 JSON-LD-blokken parsebaar op 35 responses | Inhoudelijke schemajuistheid, sitemap/robots/GSC/indexatie |
| Stijl, iconen, keuzes en beweging | [Stijl](components/MOTION_AND_STYLES.md) + [eenheidskaart](CONSISTENCY.md) | Broncontracten en tokens verdeeld bekend | Computed styles, contrast/focus, smoothness/reduced-motion mobiel |
| Productdatabase en afleidingen | [Productdata](PRODUCT_DATA.md) + [pijplijnen](components/DATA_PIPELINES.md) | Private DOC-01-export en gedateerde checks | Zakelijke datakwaliteit en latere drift; geen nieuwe volledige export |
| Apps, embeds, consent en analytics | [Apps/privacy](components/APPS_PRIVACY_AND_EXTERNAL_SYSTEMS.md) | Zeven apps, NL-consentpolicy; platforminjectie bekend | Appbron/deploy, embedstatus, werkelijk consent/netwerkgedrag |
| Checkout, shipping en payments | [Bestelketen](components/CHECKOUT_AND_OPERATIONS.md) | Shop/markt/rates/app metadata; checkoutread geweigerd | Bevoegde configuratieread + afgesproken end-to-end bedrijfscontrole |
| Uitrol, backups, monitoring en overdracht | [Onderhoud](MAINTENANCE.md) | Git-/releasewerkwijze beschreven | Werkelijke deploykoppeling, externe backups/restore/monitoring |

## Open bronblokkades

1. **config/settings_data.json:** ontvangen body wijkt van metadata af; niet normaliseren om een groene check te maken.
2. **Checkout/accountconfiguratie:** expliciete API-toegangsweigering; een aanwezige classic template vervangt die bron niet.
3. **VPS en eigen apps:** geen bestaande bevoegde server-/appbron aangetoond in deze sessie; publieke antwoorden geven slechts een deel van de keten.
4. **Mobiel en bedrijfsprocessen:** geen ondersteunde mobiele browserviewport of operationele testcontext gebruikt; fixtures/HTTP zijn geen vervanging.
5. **Google/analytics en uitrol:** geen nieuwe account-/deploystaat vastgesteld.

Werk het bereikbare deel af en leg per blokkade de exacte benodigde bron vast. Geen wachtwoord/token in chat of Git vragen. Geen omvangrijke refactor of echte koopactie starten om ontbrekende documentatie te compenseren.

## Route naar aantoonbare afronding

Bron + uitleg worden voor de hele matrix onderhouden. Daarna worden open gedragstesten per gedeelde functie gebundeld: dezelfde dropdown eenmaal testen met de relevante adapters, vervolgens noodzakelijke uitzonderingen. Bevindingen krijgen één ID, impact, kleinste correctie, passende regressie en bron-/docsupdate. Bij een gewijzigde hash alleen geraakte onderdelen en consumers heropenen.

De oude onderzoeksboom blijft het volledige detailplan. **DOC-03B** is niet stil geannuleerd: de geïsoleerde inbouwherstelketen blijft als open controle geregistreerd. De nieuwe brede opdracht voorkomt dat we alleen die ene tak verder uitdiepen terwijl andere winkelonderdelen ontbreken.
