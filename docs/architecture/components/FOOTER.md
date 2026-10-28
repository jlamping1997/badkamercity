# Footer: opbouw, beheer en gedrag

Bronmoment **28 oktober 2026**. De actuele `sections/footer-group.json` en `sections/footer.liquid` zijn bytegelijk aan het verse MAIN-manifest. De footer is maatwerk, met classes `bcf-v2 bcf-v3`; de naam Dawn van het basisthema beschrijft deze implementatie niet volledig.

## Route en gegevens

`layout/theme.liquid` rendert na `content_for_layout` de sectiegroep `footer-group`. Die groep bevat één footersectie met 18 geordende blocks. De footer leest **geen footermenu uit Shopify Navigatie** voor die drie kolommen: hij selecteert de eigen blocks op type `service`, `category` en `info`. Een wijziging in een menu met de naam footer hoeft hier dus niets te veranderen.

| Gebied | Bron | Voorwaarde / terugval |
| --- | --- | --- |
| Vier servicebeloften bovenaan | `trust_title_1..4`, `trust_text_1..4` | Vaste icoonvolgorde grid/headset/sparkles/shield |
| Logo en introductie | Globale `settings.logo`, sectie `brand_text` | Zonder logo: tekstwoordmerk en optionele tagline |
| Sociale links | Globale `social_*_link`, `show_social` | Alleen ingevulde links; voorbeeldmodus kan niet-klikbare voorbeelden tonen |
| Drie linkkolommen | Blocks met `label` en `url` | Zonder URL een `span`, geen dode `href="#"` |
| Contact | Sectievelden voor e-mail, telefoon, adres, openingstijden en CTA | Lege velden worden niet getoond; echte tel/mail-links buiten voorbeeldmodus |
| Showroom | `showroom_link` + label | Beide nodig; label alleen maakt geen bestemming |
| Beleidslinks | `shop.policies`, `show_policy` | Alleen bestaande niet-lege Shopify-policies |
| Betaaliconen | `shop.enabled_payment_types`, `payment_enable` | Voorbeeldiconen alleen bij `payment_examples` én Theme Editor |
| Copyright | Huidig jaar, winkelnaam, `bottom_text` | Geen jaarlijks handmatig jaartal nodig |

Huidige sectieconfiguratie: placeholdermodus en betaalvoorbeelden staan uit. E-mail en contact-CTA zijn ingevuld. Telefoon, adres en openingstijden zijn leeg. Dat is een configuratiewaarneming, geen opdracht om gegevens te verzinnen. De geconfigureerde categorieblokken verwijzen naar zes collecties; daarnaast wordt de algemene productcollectie via Shopify `routes` toegevoegd.

## Concrete ontbrekende bestemmingen: FOOTER-F01

Tien van de achttien blocks hebben geen URL: **Veelgestelde vragen, Bezorgen & afhalen, Retourneren, Garantie & service, Over ons, Badkamerinspiratie, Badkameradvies, Onze merken, Showroom en Zakelijk**. De Liquid-code rendert ze als gewone tekst met een voorbeeld-title. Dit is een bevestigde configuratiegrens; de labels zijn geen werkende navigatie. De eigenaar moet per label een bestaande juiste bestemming kiezen of besluiten het label weg te laten. Geen automatische pagina's of links naar willekeurige zoekresultaten aanmaken.

## Desktop, mobiel en lifecycle

De navigatiekolommen gebruiken native `details`/`summary`. Bij maximaal 749px sluit de controller ze bij initialisatie; de gebruiker kan ze vervolgens zelf openen. Vanaf 750px zet hij ze open, haalt summaries uit de tabvolgorde en voorkomt desktopklikken die het paneel zouden sluiten. Een mediaquerychange voert deze synchronisatie opnieuw uit: de eerdere mobiele openkeuze is geen blijvende voorkeur.

De controller initialiseert bestaande roots, ondersteunt `shopify:section:load` en verwijdert listeners bij `shopify:section:unload`. `root.bcfCleanup` beschermt tegen dubbele initialisatie. De CSS biedt desktop ook zichtbare inhoud als een details-element gesloten zou zijn. Zonder JavaScript staat de servermarkup aanvankelijk open; dat is een bruikbare inhoudsterugval, met mogelijk een open→gesloten wijziging op mobiel na initialisatie.

De gridindeling verandert rond 1280, 990 en 750px. Op kleine schermen komen de kolommen onder elkaar en verdwijnen de kleine service-onderteksten. De footer heeft eigen kleuren via `--bcf-*`, zichtbare focusregels en schakelt transitions bij reduced motion uit. Deze bronregels zijn geen contrastmeting of bewijs van soepelheid op een telefoon.

## Onderhoud en acceptatie

Pas labels/bestemmingen aan in de **footersectie van het juiste conceptthema**; logo/socials bij globale theme-instellingen; policies in Shopify-instellingen; betaalmethoden in het daarvoor bedoelde beheer. Gebruik geen CSS om ontbrekende bedrijfsinformatie op te lossen. De hele footer vervangen vanuit een oude Git-root kan nieuw maatwerk verliezen.

Acceptatie: alle bedoelde links bereikbaar; lege URL herkenbaar/weggehaald; geen voorbeeldgegevens live; mobiel openen/sluiten via toetsenbord/touch; 749↔750px; lange labels; ontbrekend logo; geen sociale links; lege/bestaande policies; echte betaaliconen; section load/unload; reduced motion. De desktopbrowser bevestigt de drie open panelen met samenvattingen buiten de tabvolgorde en de tien niet-linklabels. Werkelijke mobiele focus-/resizecontrole blijft open.

[Alle footerinstellingen en blockvelden](../reference/sections/footer.md) · [Sectiegroep](../reference/TEMPLATES.md) · [Bronhashes](../reference/source-index.json) · [Bevindingen](../FINDINGS.md).

## Lifecycle verdiept

[FOOTER_LIFECYCLE](micro/FOOTER_LIFECYCLE.md) beschrijft exact wat bij 749px-querywissels, repeated section load, unload en cleanup gebeurt. Twee nieuwe bronreplays bevestigen het contract; geen extra mobiele browserclaim.
