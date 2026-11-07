# Pagina's, begrippen, advies, blog en formulieren

Bronmoment **28 oktober 2026**. Verse Admin-inventaris: **119 Pages, 118 gepubliceerd**, één blog `nieuws`, één artikel. Alle ontvangen page-/collectiebodies zijn op inline style/script onderzocht; geen pagebody bevat die tags. Dit is geen inhoudelijke factcheck van iedere uitlegtekst.

## Paginafamilies en bronnen

| Familie | Toewijzing | Opbouw |
| --- | --- | --- |
| Begrippenlijst | Eén `begrippenlijst` | `main-glossary`, 109 termblocks in template |
| Uitlegpagina | 109 `begrip` | `main-glossary-page`, titel/body uit Page |
| Algemene/oudere pagina | Zes suffix `page` | Er is geen `page.page.json` in het actuele manifest; effectieve terugval expliciet controleren |
| Contact | Eén `contact` | `main-page` en `contact-form` |
| Sunshower | Eén `bc-sunshower` | Landing + richtextadvies; gekoppelde eigen product-/configuratiestroom |
| Verlanglijst | Eén `bc-wishlist` | `bc-wishlist-page` + browseropslag |

Van de zes records met suffix `page` zijn er vijf gepubliceerd. Dit is een toewijzingssignaal, **geen bewezen 404**: een ontbrekende alternatieve template kan een standaardweergave opleveren. De ongepubliceerde Page Merken is niet de actieve vendor-directory. Zie het [Admin-register](../reference/ADMIN.md) voor de concrete routes en bronmomenten.

## Begrippenlijst

De lijst komt uit **templateblocks**, niet automatisch uit alle Pages met suffix `begrip`. Iedere term heeft letter, label en keywords. De server maakt A–Z-groepen en links `/begrippenlijst/<handleize-term>`. Shopify-redirects verbinden die oude/menselijke routes aan `/pages/...`. Een term toevoegen vraagt dus drie samenhangende controles: block → bestaand/gepubliceerd Page-record → redirectbestemming.

Zoeken in de lijst is lokale filtering van reeds aanwezige DOM: Nederlandse lowercase + trim, match op term/keywords, lege groepen verbergen, A–Z-toestand bijwerken, live resultaatstext en nulresultaat tonen. Er is geen Typesense-request voor dit zoekveld. Zonder JavaScript blijven de lijst en anchors bestaan. Dit is een andere zoekfunctie dan de header of productfilters; uniforme veldstyling kan wel gedeeld worden.

### Alle 109 verbindingen gecontroleerd

De 109 werkelijk gerenderde termlinks zijn gekoppeld aan alle 120 redirects en 119 Page-records. **108** komen bij gepubliceerde Pages met aanwezige begripstemplate uit; er zijn geen loops in deze ketens. **GLOSS-F01:** Hygro(meter) linkt naar `/begrippenlijst/hygrometer`, redirect naar `/pages/hygrometer`; dat Page-record ontbreekt en een gerichte GET bevestigt **404**. Er bestaat wel een andere hygro-gerelateerde Page, maar het juiste inhoudelijke doel moet vóór correctie worden gekozen. Geen redirect of Page gewijzigd. [Verbindingsbewijs](../evidence/2026-10-28-complete/glossary-links.json).

## Begripspagina

De server rendert `page.title`, `page.content`, optionele teruglink en sidebar. Een inline controller markeert een eerste losse paragraaf als samenvatting en maakt kaarten rondom **directe H2-kinderen**. Titelwoorden zoals gerelateerde, let je op en voordelen kiezen presentatievarianten. Hij maakt een inhoudsopgave en toont die pas bij meer dan één entry. Geneste headings en bestaande IDs vragen afzonderlijke controle; willekeurige HTML uit een editor valt niet automatisch in hetzelfde model.

De desktopbrowser bevestigt 109→1→0→109 zichtbare termen bij zoeken/wissen en een werkende Rimless-link. De geladen Rimless-pagina heeft zes inhoudskaarten en zes inhoudslinks. Dit test niet iedere term, headingvariatie of mobiel.

De oorspronkelijke body blijft leesbaar zonder JavaScript. Wijzigingen in de body kunnen dus zowel semantiek als de latere DOM-indeling raken. De Glossary Upload-app is geïnstalleerd; de huidige broncode, beheerrechten en volledige import-/rollbackketen van die app zijn niet via de themafiles vastgesteld.

## Blog en adviesartikel

`blog.json` gebruikt `main-blog`; `article.json` gebruikt het maatwerk **bc-advice-article**. De oude `main-article` blijft beschikbaar maar is niet de toegewezen standaardartikelrenderer.

De adviesrenderer schat leestijd met woorden/200, kan auteur/datum tonen en splitst inhoud letterlijk op `<h2>`. Bij geschikte splits bouwt hij genummerde inhoudslinks, secties en een mobiele contents-disclosure; anders toont hij de body als geheel. H2's met attributen of afwijkende schrijfwijze zijn een af te bakenen contentcontract. De huidige meetronde noemt dat geen defect zonder een passende live body te reproduceren.

Sunshower-tag en ingestelde ONE/PLUS-beelden kiezen een specifieke visuele variant; anders kan het artikelbeeld worden gebruikt. De renderer publiceert `article | structured_data`. Een syntactisch geldige JSON-LD is geen bewijs dat Google een rich result zal tonen.

## Contact en nieuwsbrief

`contact-form` gebruikt Shopify `form 'contact'`, met naam, e-mail, telefoon en bericht, plus server-success-/errorweergave. `aria-required` is een toegankelijkheidsaanduiding; het is niet hetzelfde als HTML `required` of bewezen servervalidatie. In deze documentatieronde is **geen formulier verstuurd**. Ontvangst in de juiste mailbox, spam/reCAPTCHA, foutfocus en gegevensbewaring blijven operationele controles.

`newsletter` en `email-signup-banner` gebruiken `form 'customer'` en tag `newsletter`. De banner is onderdeel van de passwordtemplate; aanwezigheid van een nieuwsbriefsectie in het thema betekent niet dat een homepage-inschrijving actief is. Geen testinschrijving of marketingbericht verzonden.

Onderhoud: algemene inhoud bij Online Store Pages/Blogs; lijstblocks en templatepresentatie in Theme Editor; redirects in Shopify redirects; vertalingen in locales; formulierontvanger/marketingbeleid in het relevante beheer. Een gerenderde bedankmelding bewijst nog geen e-mailbezorging.

Acceptatie: nieuwe/lege term, accent/keywords/nulresultaat, redirectloop/ontbrekend doel, standaardtemplate-terugval, direct/genest H2, meerdere H1's, ontbrekend artikelbeeld, keyboardlinks, contactfouten en daadwerkelijke bezorging onder een afgesproken test. [Bron-/instellingenreferentie](../reference/SECTIONS.md).

## Methoden en inputcontracten verdiept

[CONTENT_DOM_CONTRACTS](micro/CONTENT_DOM_CONTRACTS.md) volgt lokale zoeknormalisatie, verborgen A–Z-anchors, directe H2-transformatie en TOC-ID-botsingen. Nieuwe read van 119 Pages: alle 109 gepubliceerde begripspagina’s hebben samen 655 directe H2’s, geen geneste H2’s en geen voorspelde ID-conflicten. Geen inhoudelijke factcheck of oplossing van GLOSS-F01.
