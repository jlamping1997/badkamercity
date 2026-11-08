# Live- en documentatiecontrole — 8 november 2026

> **Vervolg8 november:** Antikalk enRapoWash zijn inmiddels live gecorrigeerd; de footer is als getoetst desktopconcept voorbereid. [Actuele reparatiestatus](../../repairs/2026-11-08/footer-and-content/README.md). De metingen hieronder behouden hun oorspronkelijke auditmoment.

**DOC-LIVE-01 · READ_ONLY_AUDIT / DOCS_UPDATED / LIVE_FIXES_PENDING.** De winkel is openbaar en de homepage-SEO is live. Dit dossier actualiseert de bestaande documentatie met verse Shopify-, bron- en HTML-controles. Het is geen volledige vrijgave voor advertenties of alle koopflows.

## Actuele basis en dekking

| Onderdeel | Gemeten stand | Betekenis / grens |
| --- | --- | --- |
| Shopify MAIN | 196328685834 — BadkamerCity - Homepage SEO 8 nov; updatedAt 2026-11-08T11:49:21Z | Vers gelezen; oudere rollen in checkpoints blijven historie |
| Publieke catalogus | 15.897 ACTIVE + Online Store, EXACT | Geen individuele inhouds-/voorraadcontrole van alle producten |
| Pages / collecties / menu's | 121 Pages, waarvan 119 gepubliceerd; 227 collecties; 9 menu's | Volledige Admin-paginering; geen verborgen Pages aangezet |
| Publieke HTTP-controle | 364 responses: 360 × HTTP 200, 4 × HTTP 404 | Alle 119 gepubliceerde Pages, 227 collectie-URL's, homepage, 6 policy-URL's, 2 echte blogroutes, zoek-/cart-/merkroute, 4 productsteekproeven en een bewuste 404 |
| Renderer | Alle 364 responses melden dezelfde MAIN; homepage 1 × bch-footer, overige 363 × bcf-v2 bcf-v3 | HTML-broncontrole; geen 364 interactieve browsertests |
| Live themamanifest | 1.387 bestanden, 28 volledige API-pagina's | Metadata compleet; geen settings_data-write |
| Git-bronvergelijking | 1.378 bestanden: 1.363 gelijk, 15 verschillend, 9 alleen live, 0 alleen Git | shopify/current op 1b5108a2; verschil is niet automatisch defect |
| Native policies | CONTACT_INFORMATION, LEGAL_NOTICE, PRIVACY_POLICY, REFUND_POLICY, TERMS_OF_SERVICE | SHIPPING ontbreekt; TERMS en LEGAL tonen letterlijke HTML |
| Google | Meet-ID G-H9YFB5TC6N in live Google & YouTube-config | Realtime door eigenaar gemeld; purchase/consentwerking niet hiermee bewezen |

[Route-overzicht](route-summary.json), [alle 364 gecontroleerde routes](route-register.json), [1.387 live bestandschecksums](theme-manifest.json), [Git/live-verschillen](source-parity.json), [bevindingen met bewijsstatus](findings.json).

De vier 404's hebben verschillende betekenis: `/policies/shipping-policy` ontbreekt daadwerkelijk; `/collections/tegeltoebehoren` is een lege Admin-collectie zonder gevonden inkomende klantlink; `/blogs/news` was een gegiste Engelse probe (het echte `/blogs/nieuws` en artikel geven HTTP 200); de vierde was bewust `/dit-is-een-controle-404`. Deze vier uitkomsten bewijzen dus geen vier gebroken klantreizen. Geen van de gevonden menuverwijzingen leidt volgens de vergelijking met de Admin-gegevens naar een lege collectie.

## Wat eerst hersteld moet worden

| Volgorde | Probleem | Concrete vervolgstap |
| --- | --- | --- |
| 1 | Voorwaarden en kennisgeving tonen tags | De twee native policies correct als HTML opslaan en opnieuw lezen |
| 2 | Contactinformatie en btw-identiteit incompleet | Contactpagina en native policy gelijk trekken; eigenaar levert geverifieerd btw-id/bedrijfsidentiteit |
| 3 | Verzendbeleid ontbreekt | Werkelijke pakket-/pallettarieven en levertijden vastleggen; niet €75 retourkosten als heenzendtarief gebruiken |
| 4 | Twee footers met andere inhoud en bediening | Eén canonieke standaardfooter met volledige linkset voorbereiden in MAIN-paritair concept |
| 5 | Bronkopie wijkt af van live | Vijftien verschillen gericht reconciliëren vóór een theme-deploy; API-bodyguard behouden |
| 6 | SEO-copyfouten op 2 Pages | RapoWash-metadata en dubbele H1 van Antikalk gericht herstellen |
| 7 | Koop-/meetketen en mobiel niet compleet bewezen | Testbestelling/mail/verzending/purchase/consent en echte telefooncontrole uitvoeren |

De vaste bestelafspraak CONTINUE blijft gelden. Bestelbaar is geen bewijs van fysieke voorraad of harde levertijd. Lagoo-afbeeldingen blijven volgens expliciete eigenaarinstructie verwijderd. Het afzonderlijke filtertraject volgt zijn nieuwste centrale checkpoint. Deze audit voert geen filterinstallatie uit en schrijft geen herhaling van een eerdere installer voor.

## Footer: oorzaak en voorgestelde eenheid

`layout/theme.liquid` laadt één footer-group. Daar staat `compact_homepage=true`; `sections/footer.liquid` kiest daardoor op de homepage `bc-home-footer` en op de overige routes de standaardfooter. De vier kernfiles zijn byte-exact gelijk tussen verse MAIN en de onderzochte codebranch. Het verschil is dus in de huidige configuratie en rendererkeuze teruggevonden.

De homepage heeft 25 links en de standaardfooter 19. De homepage heeft onder meer extra categorieën, bezorganker, 3D-advies en inspiratie; de standaardfooter heeft een andere merkintro, trustbar en contact-CTA. Logoformaat, kleuren en lettergroottes zijn anders in de bron. Homepage-details worden gesloten gerenderd zonder dezelfde desktopcontroller; standaard gebruikt zijn eigen grens van 749/750 px. Dit zijn bewezen bron-/HTML-verschillen; geen nieuwe fysieke telefoon-/layouttest.

Gebruik de bestaande standaardfooter winkelbreed met één complete inhoudsset en dezelfde responsive bediening. Voorstel: 4 service-, 10 categorie- en 3 informatielinks, samen 17 blokken binnen het maximum van 18. Er bestaan al 18 blokken, waarvan 8 placeholders met een lege URL die door bestaande guards verborgen blijven. Hergebruik die; vier extra blokken toevoegen zou de schemalimiet overschrijden. Maak homeankers winkelbreed `/#HomeAdvice` en `/#HomeInspiration`. Behoud de offerte-/retourguards en gebruik `shop.policies` voor beleidslinks. Het Shopify-menu met handle `footer` beheert deze drie themakolommen niet. Geen losse kopie per paginatemplate maken. Shopify-checkout en klantaccount zijn afzonderlijke platformschillen en hebben niet vanzelf de themefooter.

[Bron-/configuratiebewijs en voorstel](safe-footer-register.json), [14 representatieve footerroutecontroles](footer-route-matrix.json), [actueel componentcontract](../../architecture/components/FOOTER.md), [uitvoering en beleid](../../livegang-seo/FOOTER_EN_BELEID.md).

## Contact, retouren en identiteit

Bevestigd openbaar contact-/retouradres: **Badkamercity – bij Harry Suiker, Zichtenburglaan 150, 2544 EB Den Haag**. E-mail info@badkamercity.nl; tijdelijk telefoonnummer van de eigenaar 06 85887536. Het native contactbeleid heeft deze telefoon nog niet; `/pages/contact` bevat alleen het formulier. De footer bevat e-mail/contactlinks, geen zichtbare telefoon of volledig adres. Het opgegeven btw-id heeft 8 cijfers vóór de B, waar het Nederlandse formaat er 9 vereist. Niet zelf een cijfer aanvullen; de eigenaar moet de oorspronkelijke Belastingdienstgegevens controleren. De geregistreerde juridische naam/vestiging volgt niet automatisch uit het contact-/retouradres.

Het retourbeleid van 30 dagen staat live: aanmelden binnen 30 dagen, daarna 14 dagen terugsturen; klant betaalt gewone spijtretour, fout/defect wordt apart kosteloos opgelost; afgeven op afspraak. €75 incl. btw per standaardpallet is de overeengekomen raming voor retourvervoer, geen automatisch heen- of universeel buitenlandtarief. Google Merchant-instellingen zijn hiermee nog niet onafhankelijk gelijkgesteld. [Actuele bedrijfsgegevens](../../livegang-seo/BEDRIJFSGEGEVENS.md), [taken en open beslissingen](../../livegang-seo/TAKEN.md).

## Gedateerd interactief bewijs en open grenzen

In de beperkte echte desktopbrowsercontrole van 8 november zijn zoeken op Wiesbaden, Wastafelkranen/Inbouw/Chroom, een Wiesbaden Ribbd-product van €245 en 2 stuks = €490 tot de gastcheckout gecontroleerd; alleen de eigen proefcart is opgeruimd. Cookiekeuzes accepteren/weigeren/heropenen waren als UI bedienbaar. Deze bewijzen zijn eerder deze dag verzameld en zijn geen uitvoering door deze crawler met 364 routes.

Nog open: betaling en orderbevestigingsmail, retour-/contactmailontvangst, adresafhankelijke bezorgoffertes en de ene Admin-locatie zonder rates, daadwerkelijke GA4 purchase/value/currency/ontdubbeling, technisch consentgedrag en volledige fysieke mobiele klantreis. Ontbrekende payments-leesscope bewijst niet dat betalingen uitstaan. Geen universele wettelijke garantiegrens van 2 jaar afleiden. Geen externe account-/Merchant-feedvrijgave of prestatie/rankingclaim.

De statische scan heeft 0 parsefouten en 1.060 letterlijke afhankelijkheden; drie naamverwijzingen bij password-error/3D-media zijn alleen conditionele onderzoekskandidaten. Er zijn geen JSON-LD-parsefouten of ontbrekende lokale ankers in de onderzochte server-HTML gevonden; dit is geen rich-results- of JavaScript-vrijgave. Het oude privé-adres is niet aangetroffen in deze HTML-set; dit is geen volledige productcatalogusscan.

## Documentatie en onderhoud

De bestaande livegang-, Google-, component- en architectuurdocs zijn geactualiseerd; de centrale status en beide handoffs verwijzen naar dit ene dossier. [MASTER_SITE_REFERENCE](../../MASTER_SITE_REFERENCE.md) is voortaan de compacte actuele ingang. Het complete boek met 80 hoofdstukken van 31 oktober blijft byte voor byte ongewijzigd als gedateerd archief in dezelfde map, zodat relatieve bronlinks en historische bewijswaarden behouden blijven. Oude hoofdstukankers op de actuele ingang blijven als doorverwijzingen beschikbaar. De historische handboekgenerator mag het actuele document niet overschrijven.

Bronregels: verse Shopify Admin en HTTP eerst, daarna gedateerd interactief bewijs en expliciete eigenaarafspraken; oudere snapshots blijven historisch. Nieuwe publieke registers bevatten geen klantdata, checkoutreferenties, privésleutels, privé-adres of bankrekening. Geen Shopify-, product-, server- of themamutatie/publicatie in deze audit.

**Volgende handeling binnen dit dossier:** één gedeelde footerinhoud/renderer voorbereiden in een bewezen MAIN-paritair UNPUBLISHED concept, inclusief contact-/beleidslinkdekking en routebrede desktop/mobielregressie. Voorwaarden-/contact-/verzendcorrecties en geverifieerd btw-id blijven afzonderlijke open taken. De actuele filterwerkzaamheden blijven het nieuwste centrale checkpoint volgen; eerdere installatieblokken niet herhalen.

De formaatcontrole van het btw-id volgt de op 8 november geraadpleegde [Belastingdienst-uitleg](https://www.belastingdienst.nl/wps/wcm/connect/nl/btw/content/btw-identificatienummer-en-omzetbelastingnummer): NL, negen cijfers, B en twee cijfers. Dit is een formaatcontrole, geen validatie van de identiteit of btw-status.

Controle van de documentatie: [verificatieregister](verification.json). De lokale bestandslinks zijn gecontroleerd; de 27 verplaatste historische links zijn gerepareerd. Het archief behoudt exact Git-blob `88d044b4c6ddbdfeb9517112b990cffa38132ef4`. De historische leesfunctie doorstaat 14 offline controles; de compiler weigert de actuele index en het archief te overschrijven. Dit is documentatiecontrole, geen nieuwe live koopproef.

Publicatieredactie op 8 november: één oud privé-adres in de centrale status en twee waarden (privé-adres en bankrekening) in de historische aanvulling van 5 november zijn afgeschermd. De aanvulling vermeldt de betrokken velden en oorspronkelijke blob; overige historische meetgegevens blijven behouden. Dit wijzigt de huidige bestanden, niet de eerdere Git-geschiedenis.
