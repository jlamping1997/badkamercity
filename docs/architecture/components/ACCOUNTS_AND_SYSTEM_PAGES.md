# Accounts, foutpagina's, wachtwoord en cadeaubon

Bronmoment **28 oktober 2026**. Dit dossier voorkomt dat minder bezochte routes uit de documentatie verdwijnen. Het beschrijft aanwezige themacode en het actuele Admin-accountsignaal; er zijn geen klantgegevens, bestellingen of cadeauboncodes gelezen.

## Accountgrens

De verse Shop-read geeft `customerAccounts=OPTIONAL`. Dat is op zichzelf geen volledige vaststelling van classic versus nieuwe gehoste accountuitvoering. De actuele accountconfiguratie/checkout-API-read werd geweigerd wegens ontbrekende toegang; een aanwezige classic template is daarom niet automatisch het daadwerkelijk gebruikte klantportaal.

| Aanwezige template | Sectie / contract |
| --- | --- |
| `customers/login.json` | `main-login`: aanmelden/herstellen via Shopify-forms |
| `customers/register.json` | `main-register`: klantregistratie |
| `customers/activate_account.json` | `main-activate-account`: activatie met platformtoken |
| `customers/reset_password.json` | `main-reset-password`: herstelroute met platformtoken |
| `customers/account.json` | `main-account`: klant-/besteloverzicht |
| `customers/order.json` | `main-order`: bestelling in accountcontext |
| `customers/addresses.json` | `main-addresses`: adresbeheer; bijbehorende customer-JavaScript |

Themaforms leveren gegevens aan Shopify; voeg geen tweede eigen accountdatabase toe voor een stijlaanpassing. Links moeten platformroutes volgen, geen hardcoded herstel-/order-URL met token. Een verse anonieme `/account/login`-GET volgt naar Shopify-authenticatie; ook de header gebruikt `customer_authentication/redirect`. Dat onderbouwt een gehoste aanmeldroute, zonder het volledige accountconfiguratiemodel vrij te geven. Ingelogde weergave, sessie-expiry, adressen en accountmails zijn niet uitgevoerd. Geen echte klantlogin gebruikt om documentatie te vullen.

## Systeempagina's

`404.json` → `main-404` geeft herstel naar producten. Controleer echte HTTP-status naast de zichtbare tekst: een pagina met “niet gevonden” in de titel kan nog steeds verkeerd met 200 antwoorden. De read-only routechecks bevatten één doelbewust niet-bestaand pad.

`password.json` → `email-signup-banner` gebruikt `layout/password.liquid`, met eigen passwordheader/-footer en customer-inschrijving. De gewone sitefooter hoeft daar dus niet aanwezig te zijn. De HTTP-read van `/password` eindigt op de homepage; de reservepasswordweergave is daarmee niet interactief getest. Een publiek bereikbare winkel betekent niet dat deze reservecode veilig verwijderd kan worden; passwordmodus kan later opnieuw gebruikt worden.

`gift_card.liquid` toont door Shopify verstrekte cadeauboncontext en bevat onder meer print-/QR-/walletmogelijkheden waar de bron die aanbiedt. Nooit een echte cadeauboncode, barcode of balans in publieke bewijsbestanden opnemen. Deze route is alleen op bronstructuur onderzocht; geen cadeaubon aangemaakt/geopend.

## Reserve-, review- en editorsecties

De templatecatalogus bevat ook `bc-mobile-review`, `bc-mobile-qa`, `bc-responsive-qa`, `bc-disclosure-check`, Hotbath-pilot/data en advice-QA. Een QA-naam is geen garantie dat de route privé is of niet geïndexeerd kan worden; templateaanwezigheid is ook geen bewijs van toewijzing. Vaststellen van actieve resources, robots en noodzaak gaat vóór verwijderen of hernoemen.

Losse Dawn-secties zoals video, collage, slideshow, multicolumn, collapsible-content, featured-product, pickup-availability en quick-order-list staan volledig in de [sectiereferentie](../reference/SECTIONS.md). Het zijn beschikbare bouwstenen; alleen de concrete template-/Adminroute bepaalt gebruik. Een ontbrekende statische caller bewijst niet dat de Theme Editor of Section Rendering ze nooit opvraagt.

Onderhoud: accountmodel bij Shopify-instellingen controleren; inhoud/stijl van classic routes in het thema; authenticatie/recovery door het platform. Acceptatie vereist een afgesproken testaccount, mailontvangst en afgeschermde bewijsvoering, zonder echte orders of codes openbaar te maken. Geen account-/checkoutvrijgave op basis van dit brondossier.

## Statisch onderhoudssignaal SOURCE-F01

De bronkaart vindt `icon-error` zonder .svg in de passwordheader en `icon-3d-model` zonder .svg op twee plaatsen in product-media. Die exacte namen ontbreken in het manifest; SVG-versies bestaan wel. Dit blijft een bronkandidaat voor de betreffende fout-/3D-staat, geen gereproduceerd live probleem. [Bronregels](../evidence/2026-10-28-complete/reference-anomalies.json), [officieel filtercontract](https://shopify.dev/docs/api/liquid/filters/inline_asset_content).
