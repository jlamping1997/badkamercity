# Fundament, dependencies en onderhoudsgereedschap

**Bronmoment 28 oktober 2026.** Dit beschrijft aangetroffen code/configuratie, niet de geïnstalleerde productie-/Windowsomgeving. Lees [SYSTEMS_AND_SOURCES](../SYSTEMS_AND_SOURCES.md) voor systeemgrenzen en [bronindex](../evidence/2026-10-28-doc02/source-index.json) voor hashes.

## Storefrontfundament

| Techniek | Aangetroffen gebruik | Beheergrens |
| --- | --- | --- |
| Shopify Online Store / Liquid | Layout, secties, snippets, product-/collectieobjecten en theme-instellingen | Shopify rendert de servermarkup; lokale bestanden bewijzen geen actuele Admin-toewijzing |
| JSON-templates en sectiegroepen | Paginaopbouw, blocks, instellingen, disabled-secties, headergroep | Eerst actieve template/caller bepalen; geen losse snippet als hele pagina behandelen |
| Dawn-basis | config/settings_schema.json vermeldt Dawn 15.4.1, auteur Shopify | Basisvermelding, geen claim dat maatwerk nog upstream Dawn volgt |
| Gewone JavaScript en custom elements | product-info, product-form, media-gallery, disclosures en maatwerkcontrollers | Lifecycle, DOM-hooks, events en Section Rendering vormen de contracten |
| CSS en Liquid-styles | Globale variabelen, componentstyles, merk-/paginastyles, inline sectionstyles | Volg laadvolgorde en computed cascade; geen volledige tokenmigratie uitgevoerd |
| Native browser-API's | dialog, fetch/AbortController, observers, Web Animations, storage en history | Browserondersteuning/fallback per daadwerkelijk gebruik controleren |
| PhotoSwipe | Vendormoduleheader vermeldt **5.4.4**, auteurvermelding bewaard | Sunshower laadt deze module op aanvraag; header is geen volledige licentie-/kwetsbaarheidsaudit |

Er is in de rootcheckout geen package.json, requirements.txt of shopify.theme.toml aangetroffen. .theme-check.yml bestaat en extends theme-check:recommended. Dit is dus geen centraal React-/Hydrogen-/Node-webappbuildproject. Dat sluit losse libraries, theme tooling of externe backendcode niet uit. De geïnstalleerde Shopify CLI-versie, apps, abonnementen en deployments zijn hier niet opnieuw gecertificeerd.

## Laden en events

layout/theme.liquid laadt de basis constants/pubsub/global/defer-scripts, genereert typografie-/kleurvariabelen en laadt de gedeelde styles. Secties en snippets voegen functionele assets toe. product-form/product-info gebruiken het bestaande pub/subcontract, terwijl andere maatwerkcontrollers DOM-events of een eigen native formulierroute gebruiken. Een script met dezelfde naam kan meerdere callers hebben; controleer de initguard voordat je loading centraliseert.

Een custom element met connected/disconnectedCallback heeft een andere cleanupvorm dan een IIFE met data-ready-marker. DOM vervangen via Section Rendering kan oude observers/listeners laten leven of nieuwe roots missen als init/teardown niet meedoet. De concrete guards staan per componentdossier; deze ronde bevat geen volledige lifecycle-leaktest.

## Testdependencies: waargenomen pins

| Pakketlocatie op actieve branch | Vastgelegde devDependencies | Betekenis |
| --- | --- | --- |
| docs/code-cleanup/2026-10-25/package.json | happy-dom 21.0.4; liquidjs 10.30.0; postcss 8.5.31 | Releasefixtures voor keuzes, observers, aankooptransport en data |
| docs/product-switcher/2026-10-25/desktop-options/package.json | happy-dom 21.0.4 | Afgebakende keuze-/inbouwregressies |
| scripts/cart-clear-tests/package.json | jsdom 26.1.0; liquidjs 10.30.0 | Cartcontroller en Liquid-/verzendfixtures |

Dit zijn repositorypins, geen nieuwe versieaanbeveling en geen bewijs dat pakketten in iedere checkout geïnstalleerd zijn. Hergebruik de bestaande lockfile waar aanwezig en installeer niet blind een recentere library tijdens een documentatie- of CSS-taak. Voer npm-scripts pas uit nadat je hun bron, fixtures, netwerk-/mutatiegedrag en relatie met de actuele hashes hebt gelezen. Een passing historische fixture kan tegen een oudere releasekopie lopen.

## Kleine offline documentatietools

Tooling staat op **fix/product-cards-2026-10-14**, niet automatisch op main. Alle drie gebruiken Python-standaardbibliotheken; geen pakketinstallatie, Shopify-auth of netwerk nodig.

| Script | Input → output | Harde grens |
| --- | --- | --- |
| architecture_scan.py | Themefolder + manifest → inventaris, letterlijke refs, signalen, pariteit | coverage is verklaard; geen runtimeparser; require-parity faalt bij afwijking |
| build_product_data_package.py | Opgeslagen private Admin-responses → JSONL, SQLite, veldregister | Geen downloader/importer; output buiten publieke repo; faalt bij incomplete joins/paginering |
| build_component_reference.py | Componentregistry + snapshot + manifest + Git-baseline → bron-/consumentenindex | Alle geselecteerde bytes/groottes moeten passen; optionele database wordt alleen read-only voor type/aantallen geopend |

De componentregistry staat in [component-registry.json](../component-registry.json). De builder vergelijkt Git-blobs uit de expliciete baseline, zodat lokale dirty bestanden niet stil als exacte releasebron worden aangemerkt. Hij publiceert geen metafieldwaarden, voorraadregels, kostprijzen of privé-URL's.

Voor een nieuwe meting, vanaf de actieve branch:

```bash
python3 scripts/build_component_reference.py \
  --snapshot /pad/naar/gecontroleerde-theme-snapshot \
  --manifest /pad/naar/vers-manifest.json \
  --registry docs/architecture/component-registry.json \
  --repo . --baseline GEVERIFIEERDE_GIT_COMMIT \
  --output /pad/naar/nieuw-gedateerd-bewijs
```

Optioneel --product-db verwijst naar een bevoegde private export voor type/aantallen; zonder database bevat het veldregister alleen consumenten. Een lege observedFields-lijst betekent dan niet dat de winkel geen waarde heeft. Nieuwe originele sources/claims moeten handmatig aan de registry en inhoudelijke dossiers worden toegevoegd; de tool schrijft geen uitleg, diagram of runtimevrijgave.

## Wanneer wel of niet testen

Bij documentatie: relatieve links, JSON, bronhashes/regelnummers, privacy van bewijs en de gebruikte inventaristool controleren. Bij een codewijziging: de fixture testen die het aangepaste contract raakt, plus representatieve echte render-/interactiestaten. Niet iedere historische test blind herhalen en een oud PASS-resultaat niet als een nieuwe run presenteren.

In DOC-02A zijn de componentindex, acht responsechecks en de 656 afgeleide-data-bytevergelijkingen werkelijk uitgevoerd. De eerdere vier productbuilder- en vijf scannerchecks blijven eerder bewijs; ze zijn hier niet opnieuw als featuretests uitgevoerd. Theme Check, echte browseracties, mobiele telefoon, performance, checkout en VPS blijven NOT_TESTED in deze verdieping.

## Uitrol en herstel

Git main is de vaste documentatie-ingang, de actieve branch draagt tooling/releasewerk; geen van beide rootfolders is daarmee automatisch een complete productiebron. Snapshotbron, doelconcept, deploymentkoppeling en rollback moeten vooraf passen. De settings-pariteitsuitzondering blijft een open bronvrijgavepunt. Geen theme-root consolideren of Shopify publiceren op basis van alleen dit overzicht.
