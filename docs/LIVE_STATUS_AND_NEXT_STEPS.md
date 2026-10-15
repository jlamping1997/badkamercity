# BadkamerCity — vaste startpagina en werkplan

**Bijgewerkt: 15 oktober 2026 (Europe/Amsterdam).** Dit is de centrale werkstatus. Begin iedere sessie bij de [versie op main](https://github.com/jlamping1997/badkamercity/blob/main/docs/LIVE_STATUS_AND_NEXT_STEPS.md), ook als je code op een andere branch staat. Wijzig dit document verder; maak geen nieuw masterplan per chat.

## Nu bezig: BC-00 — werkversies gelijkzetten na goedgekeurd mobiel ontwerp

**Opdracht 15 oktober:** eigenaar kiest expliciet mobiele kaarten en een rustige zwevende filterknop na twee screenshots. Eén product per rij, volledige bestaande korte-titelfallback, levertijd op aanvraag zolang voorraad-/levertijddata niet betrouwbaar is. Geen live-publicatie.

**Uitvoering:** ChatGPT, bestaande branch `fix/product-cards-2026-10-14`; schone tijdelijke checkout van remote `f9994ad7cdc9c4f9ec80ac1e5c38b10943b7c75a`, geen toegang tot Windows-werkplekken. Werkpreview `195249799434` (Vaste werkpreview) gekopieerd van MAIN `195218047242`.

**Beoordeling 15 oktober, 11:06 Europe/Amsterdam:** eigenaar: ‘ziet er goed uit’. Mobiel ontwerp is **USER_APPROVED_UI**. Dit bewijst niet afzonderlijk dat alle filterhandelingen/categorieën getest zijn en is geen opdracht tot publicatie.

**Volgende handeling:** controleer in Shopify Thema’s welke GitHub-branch aan welk thema gekoppeld is, en inspecteer daarna de huidige Windows-projectmap alleen-lezen. Bewaar lokale afwijkingen vóór synchronisatie. Breng vervolgens de mobiele patch en de zeven live/Git-afwijkingen samen op de bestaande werklijn; behoud werkpreview `195249799434`.

**BC-00 hervatten daarna:** werkplekken controleren en de live/Git-afwijkingen samenbrengen. Read-only manifest bevat 449 live-bestanden; 442 komen overeen met de werkbranch (inclusief genormaliseerde regeleinden), zeven instellingen-/templatebestanden wijken af. De werkpreview behoudt de actuele live-instellingen; die worden niet overschreven vanuit de oudere Git-versies.

| Startgegeven | Actuele vaststelling / beperking |
| --- | --- |
| Projectrepository | [jlamping1997/badkamercity](https://github.com/jlamping1997/badkamercity), publiek; geen geheimen, klantgegevens of vertrouwelijke leveranciersbestanden |
| Tijdelijke actieve codebranch | `fix/product-cards-2026-10-14`; verdergaan met deze lijn, geen nieuwe branch per chat |
| Laatste codecommit bij controle | `03d157e53431507d7593f9e3b9f0e34295b17941`; latere commits in deze overdracht wijzigen alleen documentatie |
| Shopify store | `fpa9hu-i3.myshopify.com` |
| Actueel gepubliceerd thema | **BadkamerCity - Zoekfilters en korte titels**, ID **195218047242**, rol **MAIN** rechtstreeks gelezen op 15 oktober |
| Vorige uitvoering | `195216048394` is nu UNPUBLISHED; geen automatisch gekozen nieuwe werkpreview |
| Werkpreview | `195249799434`, **BadkamerCity - Vaste werkpreview**, UNPUBLISHED; identieke kopie van MAIN (449/449 bestanden) vóór deze mobiele wijziging |
| Git main | Codebasis dateert bij controle van 7 oktober; de recentere codebranch lag 8 commits voor. Deze documentatie-update synchroniseert geen themacode |
| Open codeoverdracht | PR #5: afronding → main; PR #6: productkaarten/zoeken → afronding. Open PR is geen bewijs dat een Shopify-thema ongepubliceerd is |
| Andere repository | `jlamping1997/badkamercity-shopify-theme` bestaat ook. Behandel als te vergelijken oudere bron; niet verwijderen of opnieuw als tweede werkproject gebruiken |
| Werkcomputers | Lokale bestanden, ongepushte commits en authenticatie in deze sessie niet gecontroleerd |
| GitHub–Shopify-koppeling | Nog niet vastgesteld welke branch rechtstreeks aan welk thema gekoppeld is |
| Huidige uitvoerder | Mobiele implementatie afgerond voor review; geen achtergrondtaak of technische vergrendeling actief |
| Eerstvolgende controle | BC-00 hervatten: GitHub–Shopify-koppeling en Windows-werkplekken verifiëren; mobiel ontwerp door eigenaar goedgekeurd |

**Gebouwd, getest en live zijn afzonderlijke statussen.** Publicatie van het genoemde thema is bewezen; de werking van alle zoekfilters en korte titels is daarmee niet opnieuw getest.

[Technisch zoek- en titelcontract](https://github.com/jlamping1997/badkamercity/blob/fix/product-cards-2026-10-14/docs/SEARCH_AND_SHORT_TITLES_2026-10-14.md): de vorige ontwikkelsessie meldt 25 geslaagde frontend-/Liquid-controles. Visuele desktop/mobielcontrole en de actuele externe zoekroute stonden nog open. De korte-titeldefinitie was toen leeg; actuele vulling is vandaag niet opnieuw uitgelezen.

## BC-01M — ontwerp goedgekeurd, synchronisatie en functionele eindcontrole open

- Eén product per rij onder 750 px, afbeelding links (34%), merk/titel/levertijd/prijs rechts. Volledige korte-titelfallback behouden; geen afkapping. Op mobiel vervallen de extra kenmerklijst en Bekijk product-regel in zoek-/categoriekaarten; desktop blijft in kolommen.
- Kleine zwevende Filter-knop verschijnt zodra de bestaande opener boven beeld is; verdwijnt bij open paneel, na de productlijst en op desktop. Bedient bestaande externe filters of native Shopify-filters na terugval. Externe drawer heeft focusbeheer, Escape en gesloten inert-status.
- Levertijdmelding op alle listing-kaarten: **Levertijd op aanvraag**. Gebruiker meldt onbetrouwbare voorraad. Geen voorraadgetal, groen voorraadlabel of verzonnen levertermijn afgeleid. Productdata en PDP niet gewijzigd. Toekomstige leverancierskoppeling moet eerst bron, actualiteit en product/variantidentiteit verifiëren voordat een concrete termijn deze neutrale tekst vervangt.
- Werkpreview: `https://fpa9hu-i3.myshopify.com/search?q=test&preview_theme_id=195249799434`. MAIN `195218047242` is na upload opnieuw gecontroleerd: 449 bestandschecksums onveranderd.
- Tien productie-bestanden geüpload en exact teruggelezen. Vooraf 449/449 checksums van kopie gelijk aan MAIN. Zeven live/Git-verschillen betreffen `config/settings_data.json`, `sections/footer-group.json`, `templates/collection.category-landing.json`, `templates/collection.json`, `templates/index.json`, `templates/product.bc-hotbath-data.json`, `templates/product.bc-hotbath-pilot.json`; deze blijven in de preview op hun liveversie.
- Validatie: 14 filtertests, 3 zwevende-knoptests en 13 bestaande Liquid-kaart/titelcontroles geslaagd; JS-syntax en diff-whitespace geslaagd. Theme-validator: alle tien productie-bestanden VALID met bestaande niet-blokkerende waarschuwingen; gebundelde Shopify-schemafallback gebruikt na netwerk-timeout bij manifestverversing.
- Browser: echte desktopzoekroute `q=test` geeft 75 externe resultaten, juiste eerste Wiesbaden-producten en Levertijd op aanvraag. Previewwerkbalk bevestigt Vaste werkpreview/Draft. Mobiele visuele controle **NOT_TESTED**: geen viewportregeling in deze browser; een tijdelijk iframe-reviewvenster laadde niet. Geen telefoon-/Safari- of volledige categoriebrowsertest claimen.
- De connector blokkeerde het verwijderen van de tijdelijke reviewtemplate. Materieel veiliger opgelost door het bestand te vervangen door uitsluitend `{% section 'main-search' %}`: dezelfde gewone zoeksectie, geen iframe, debugscript of aparte layout. Deze ongekoppelde alternatieve template bestaat alleen in de draft.

**Git-bewaring zonder mogelijke live-sync:** de koppeling van de bestaande branch aan Shopify is nog niet bewezen. Daarom staan alle tien productie-bestanden plus beide tests als toepasbare patch in [docs/patches/BC-01M-mobile-product-listing.patch](patches/BC-01M-mobile-product-listing.patch), op de bestaande werkbranch. Er zijn geen nieuwe branches gemaakt en geen gewijzigde themapaden naar een mogelijk gekoppelde branch gepusht. De patch is gecontroleerd met reverse-apply tegen de lokale implementatie. De themabestanden op de branch zelf bevatten deze mobiele wijziging dus nog niet; niet ten onrechte als gesynchroniseerd behandelen.

**Hervatten na mobiele review:** verifieer eerst de branch–themakoppeling en behoud Windows-wijzigingen. Pas de patch toe op de bestaande werkbranch (`git apply --check`, dan `git apply`) nadat vaststaat dat dit niet naar MAIN synchroniseert; daarna source-bestanden committen/pushen. Werkpreview behouden en cumulatief verder gebruiken. Geen oude themakopie publiceren. Terugzetpad voor deze wijziging: de tien gewijzigde/nieuwe productie-bestanden vergelijken met MAIN; live is ongewijzigd.

## Vaste afspraken

1. **Eén actieve taak, één uitvoerende sessie.** Een tweede chat mag onderzoek doen; laat niet twee sessies dezelfde werkversie of Shopify-data wijzigen. Registreer taak, uitvoerder, branch en checkpoint voordat codewerk begint. Dit is een werkafspraak, geen al ingebouwde software-lock.
2. **Nieuwe ideeën naar de parkeerplaats hieronder.** Wissel alleen bij een aangetoond probleem dat de huidige taak blokkeert of bij een expliciete prioriteitswijziging van de eigenaar. Noteer dan waarom en waar de vorige taak moet worden hervat.
3. **Kleine stukken afronden.** Deel werk op in ongeveer 20–45 minuten. Na ieder betekenisvol, bewaarbaar stuk: wijzigingen beoordelen, passende controle, status bijwerken, commit en push verifiëren. Wacht niet tot de hele werkdag klaar is.
4. **Elke taak heeft een eindcriterium.** Noteer scope, betrokken bestanden/Admin-objecten, controle, open punt en exact één volgende handeling. “Klaar” zonder bewijs is geen status.
5. **Geen nieuwe ontwerpvariant tijdens een andere taak.** Bestaande goedgekeurde onderdelen behouden; een gerichte aanpassing mag als de huidige taak die vereist.
6. **De uitvoerende AI houdt deze pagina bij.** De gebruiker hoeft geen tweede Excel, chatlog of bord bij te houden. Bij het beëindigen van een beurt zonder schrijfrechten: geef de ontbrekende opslag expliciet aan.
7. **Overdracht is pas geslaagd na remote opslag.** Een lokale commit of stash is niet beschikbaar op een andere pc. Bij wegvallen vóór een checkpoint kunnen de nieuwste lokale wijzigingen nog ontbreken; beloof geen automatische achtergrondopslag.
8. **Huidige toestemming en projectregels blijven gelden.** Dit plan autoriseert geen ongevraagde publicaties, massale productmutaties, verwijderingen of destructieve Git-acties.

## Beoogde technische inrichting na BC-00

| Onderdeel | Werkwijze |
| --- | --- |
| `main` | Goedgekeurde releasecode en deze vaste startpagina. Pas na de vergelijking behandelen als actuele live-codebasis |
| `work` | Eén vaste werkbranch vanaf de samengebrachte basis; de huidige actieve branch vervult die rol tijdelijk. Nog niet aangemaakt of gekoppeld |
| Shopify werkpreview | Eén aangewezen UNPUBLISHED thema met vaste previewlink; alle vervolgwijzigingen cumulatief hierin |
| Shopify live | De geteste release; nooit een oude losse categorietemplate of themakopie publiceren alsof die de hele huidige webshop bevat |
| Dagelijkse synchronisatie | Ophalen vóór werken; code en voortgang samen committen en pushen bij checkpoints. Bestaande lokale afwijkingen eerst behouden en vergelijken |
| Release | Complete samenhangende kandidaat controleren, huidige live-afwijkingen meenemen, vervolgens gecontroleerd vrijgeven en MAIN-ID/commit/controle vastleggen |

Gebruik bij voorkeur de bestaande **Shopify GitHub-integratie** voor `work` → werkpreview, mits de vergelijking en een kleine proef in beide richtingen slagen. Een gekoppelde branch werkt het bijbehorende thema bij; ook opgeslagen editorwijzigingen gaan terug naar Git. Is een gekoppeld thema LIVE, dan kan een push direct de liveweergave veranderen. Controleer de daadwerkelijke koppeling vóór iedere release; `work` mag niet als live gekoppeld blijven staan na publicatie.

De proef voor BC-00: één onschuldige wijziging in de aangewezen preview, terugzien in Git, wijziging op de andere werkplek ophalen, daarna herstellen. Geen openbare winkel wijzigen voor deze proef.

**Git synchroniseert themacode, geen complete winkel.** Producten, prijzen, metafieldwaarden, menu's, collectietoewijzingen en checkout-instellingen blijven in Shopify. Imports krijgen bronversie, afgebakende batch, herstelgegevens en hervatbare voortgang. Gevoelige exports blijven in beveiligde opslag buiten deze publieke repository. De filterserver/index heeft eigen code, configuratie, publicatie- en herstelprocedure; registreer de vindplaats in het bestaande technische dossier. Terugzetten van een thema herstelt geen gewijzigde productdata.

## Eén vaste volgorde tot lancering

De hoofdlijn blijft staan. Bewijs en werkelijk gevonden blokkades bepalen de deeltaken; een nieuwe chat is geen reden om de planning opnieuw te maken.

| Stap | Werk | Gereed wanneer | Status |
| --- | --- | --- | --- |
| **BC-00** | Alle bestaande code en overdracht samenbrengen; twee pc's aansluiten; vaste werkpreview en branches vastleggen | Live ↔ Git-verschillen verklaard; relevante losse wijzigingen behouden; hoofdversie compleet; ophalen, checkpoint en hervatten op tweede werkplek bewezen | **BEZIG** — documentatie gereed, technische samenvoeging en werkplekproef open |
| **BC-01** | Bestaande zoekfilters en korte titels afronden met Wastafelkranen als proefcategorie | Mobiel/desktop: zoeken, merk/montage/kleur/prijs, sorteren, paginering, terugknop, foutfallback; ingevulde én lege korte titel op homepage/categorie/zoeken; juiste SKU/prijs tot winkelwagen gecontroleerd. Nog ontbrekende data in kleine proef herstellen | WACHT op BC-00 |
| **BC-02** | Productdata en categorieën per merk/productfamilie afronden en aanvullen | Vastgelegde lanceringsscope gecontroleerd op SKU, prijs incl. btw, afbeeldingen, categorieën, essentiële specificaties en Online Store-publicatie; import hervatbaar; foutenlijst verklaard. Eerst kleine proef, dan dezelfde verwerking opschalen | WACHT op BC-01 |
| **BC-03** | Zoeken, filters en navigatie over het vastgelegde assortiment controleren | Iedere productfamilie heeft bruikbare filters en goede resultaten; exacte SKU vindbaar; lege/verkeerde routes opgelost; indexverversing, bewaking en fallback bewezen | WACHT op BC-02 |
| **BC-04** | Bestaand ontwerp consequent afronden | Homepage, header, categorieën, productkaarten, productpagina en winkelwagen werken samen op mobiel/desktop; goedgekeurde stijl consequent; geen willekeurige nieuwe redesigns | WACHT op BC-03 |
| **BC-05** | Bestellen en bedrijfsafhandeling volledig controleren | Prijs/btw, betalen, verzendregels, communicatie, leverbeloftes en operationele afhandeling gecontroleerd met representatieve bestellingen binnen expliciet afgesproken testscope | WACHT op BC-04 |
| **BC-06** | SEO-/snelheidscontrole en lancering | Belangrijke pagina's en links gecontroleerd, indexatie-instellingen kloppen, gemeten mobiele prestaties beoordeeld, open verkoopblokkers opgelost, herstelpad en lanceercontrole vastgelegd | WACHT op BC-05 |
| **BC-07** | Gericht groeien | Werkelijke omzet, marge, conversie en servicekwaliteit sturen de volgende verbeteringen; nieuwe functies en verdere assortimentuitbreiding per meetbaar doel | NA lancering |

Kritieke bestel- of datafouten die in BC-01 worden gevonden direct oplossen of als blokkade behandelen; niet laten liggen tot BC-05. Het definitieve lanceringsassortiment wordt expliciet vastgelegd; deze volgorde verkleint eerdere assortimentafspraken niet stilzwijgend.

## Starten, pauzeren en hervatten

**Start op elke pc of in een nieuwe chat:**
- Open deze pagina op GitHub main; lees AGENTS en de relevante technische overdracht.
- Controleer de lokale map, origin, branch, lokale wijzigingen en laatste remote stand. Bewaar afwijkingen vóór pull/switch; nooit blind overschrijven.
- Controleer Shopify MAIN en aangewezen werkpreview. Gebruik de actieve branch uit deze pagina, niet automatisch `main` of een oude downloadmap.
- Herhaal kort: huidige taak, laatst bewezen checkpoint, volgende handeling. Ga daarmee verder.

**Checkpoint / pauze:**
- Bewaar alleen beoordeelde projectwijzigingen, zonder secrets of klantgegevens. Onvolledig werk mag herkenbaar als werkcheckpoint worden vastgelegd, met open controles.
- Werk het taakblok bij, commit en push. Verifieer dat de remote commit bestaat.
- Eindig met: “Opgeslagen: [commit/link]. Nu: [taak/status]. Volgende handeling: [concrete actie].”
- Een onderbroken import hervatten vanuit vastgelegde batchstatus, niet vanaf nul op dezelfde producten.

**Vaste startopdracht voor de gebruiker:**

> Ga verder met BadkamerCity. Lees de vaste startpagina op GitHub main en AGENTS, haal de actuele werkversie op, controleer de huidige Shopify-thema's en hervat de geregistreerde taak. Werk de voortgang bij en sla een checkpoint op zodra een deelstap gereed is.

**Bij een klantafspraak:** “Sla een checkpoint op; ik pauzeer.” Na terugkomst: “Ga verder vanaf het laatste checkpoint.”

## Korte klantreiscontrole — 15 oktober 2026

**Afgerond onderzoek, geen nieuwe actieve bouwtaak. BC-00 blijft de volgende uitvoering.** Aanleiding: eigenaar vroeg op mobiel mee te kijken zonder concreet gemeld probleem. Alleen openbare storefront bekeken; geen themacode, productdata of publicatie gewijzigd.

**Bewijsgrens:** browsercontrole op desktop, viewport circa 1363 × 936. Een aanvankelijk aanwezige oude draft-preview is verlaten via “Exit preview”; onderstaande bevindingen komen van de storefront daarna. De route vanaf badkamercity.nl kwam in deze browser op fpa9hu-i3.myshopify.com uit. Mobiele viewport/telefoonweergave: **NOT_TESTED**; mobiele preview via Admin kwam op een aanmeldscherm. Geen conclusie over mobiele afstanden, knopgrootte of overloop. Geen volledige checkout- of filtersuite uitgevoerd.

| Controle | Waarneming |
| --- | --- |
| Homepage → Kranen | Categorietegel opende /collections/kranen |
| Zoeken op wastafelkraan | 609 resultaten in de geteste zoekroute |
| Merkfilter JEE-O | Aangevinkt; resultaat veranderde naar 28 producten, actieve merkchip zichtbaar |
| Product openen | JEE-O cone twee-gats hoog gun metal opende met artikelnummer 900-1776 en prijs €830, overeenkomstig de resultaatkaart |
| Homepagebanners | Drie afbeeldingen tonen oproepen “Shop Hotbath”, “Ontdek de tegels” en “Bekijk de meubels”; DOM bevat voor deze banners geen link/bestemming |
| Afspraakoproepen | “Plan een gratis adviesgesprek” is een span zonder link; “Plan een afspraak” is een span met aria-disabled=true |
| Footer service | Veelgestelde vragen, Bezorgen & afhalen, Retourneren, Garantie & service zijn spans met title=Voorbeeld, zonder link |
| Producttitels | Lange titels zichtbaar in zoekresultaten. Bestaande korte-titelfunctie/data onderzoeken binnen BC-01; actuele metafieldvulling niet uitgelezen |
| Specificaties steekproef | Bij JEE-O artikel 900-1776 toont de specificatietabel alleen artikelnummer en merk. Databron/mapping nog niet onderzocht; geen uitspraak over alle producten |

**Afgebakende kandidaat voor later:** bestaande homepagebanners en afspraakoproepen aan geverifieerde bestemmingen koppelen, daarna footerbestemmingen afmaken. Geen nieuwe homepagevariant nodig op basis van deze controle. Controleer eerst bestaande doelpagina's en afspraakroute; verzin geen servicevoorwaarden. Voor echte mobiele beoordeling: telefoonbeelden of een beschikbare mobiele preview van homepage en productlijst. Dit onderzoek wijzigt de eerstvolgende handeling van BC-00 bovenaan niet.

## Parkeerplaats

- Nieuwe homepagevarianten, extra keuzemenu's, vergelijkfuncties en andere nieuwe functies pas beoordelen zodra de lopende fase gereed is.
- Nieuwe ideeën hier als één regel vastleggen met doel en reden voor later. Alleen de eigenaar verandert bewust de prioriteit.
- Bestaande afspraken over productdata, SKU/fabrikantnummer, prijzen, verborgen technische documenten en goedgekeurde vormgeving blijven in het technische dossier gelden.

## Overdracht van 15 oktober

Uitgevoerd: actuele themarollen gelezen; twee repositories en actieve branches bekeken; PR #5/#6 en recente technische overdracht gelezen; verschil tussen publicatie en Git-status vastgesteld; bestaande startdocumentatie en instructies bijgewerkt.

Niet uitgevoerd: lokale Windows-inspectie, volledige actuele themabestandsvergelijking, code samenvoegen naar main, nieuwe branch/themakoppeling, browser-/filtertests, productwijzigingen of publicatie. Geen achtergrondproces ingesteld.

Controlebronnen: Shopify Admin-query met alle 11 thema's (geen vervolgpagina); GitHub branch/commit- en PR-reads; vergelijking main → werkbranch (8 codehistoriecommits voor bij aanvang). Historische testresultaten zijn niet opnieuw als actuele test geclaimd.

Technische achtergrond: [Shopify GitHub-integratie](https://shopify.dev/docs/storefronts/themes/tools/github) en [versiebeheer voor thema's](https://shopify.dev/docs/storefronts/themes/best-practices/version-control).

---

## Historisch archief — geen actuele dagstart

Onderstaande eerdere status blijft bewaard als geschiedenis. Gebruik voor huidige taak, publicatie en werkbranch altijd het blok bovenaan. Een oude vermelding “nog publiceren” of “alleen opt-in” is geen actuele vaststelling.

# BadkamerCity — bewezen live-status en volgende werkroute

> **Aanvulling 14 oktober 2026:** [gecontroleerde filterpreview](https://github.com/jlamping1997/badkamercity/blob/fix/product-cards-2026-10-14/docs/FILTER_PREVIEW_2026-10-14.md) legt de geslaagde VPS-index/API/HTTPS-proeven en desktopbediening in concept `195038216458` vast. Opt-in blijft verplicht; mobiele controle, andere productfamilies, indexonderhoud en publicatie zijn nog open. MAIN `194981003530` is ongewijzigd. Oudere tabellen hieronder blijven historische snapshots.

> **Aanvulling 10 oktober 2026:** MAIN is `194981003530` (Collectiebeelden correctie 8 okt). Hotbath-productweergave, rustiger cart en Toebehoren-afbeeldingen staan samen in ongepubliceerde draft `195038216458`, met geslaagde scoped desktopcontroles. Mobiele eindcontrole en publicatie staan open. Zie [actuele oplevering en vervolg](https://github.com/jlamping1997/badkamercity/blob/fix/product-cards-2026-10-14/docs/AFRONDING_BASIS_2026-10-10.md). De tabellen hieronder blijven de historische stand van 7 oktober.

**Meetdatum:** 7 oktober 2026. Dit overzicht scheidt wat bestaat van wat daadwerkelijk is getest of expliciet goedgekeurd. Nieuwe AI's mogen deze status niet stil upgraden; ze moeten nieuwe controles met datum en bron toevoegen.

## 1. Huidige status per onderdeel

| Onderdeel | Status | Wat is bewezen / wat niet |
| --- | --- | --- |
| Git-repository/theme-snapshot | **VERIFIED_THEME** | 441/441 Shopify-themebestanden inhoudelijk met Git vastgelegd, inclusief 4 grote switcher-JSON's |
| Shopify MAIN | **VERIFIED_ADMIN** | Thema `194864677130` “BadkamerCity - SEO categoriehub” MAIN op meetmoment |
| Homepage | **IMPLEMENTED_THEME** | 8 secties in `templates/index.json`; geen volledige browser/checkouttest in deze ronde |
| Header, mobiele drawer, footer | **IMPLEMENTED_THEME** | Code en Theme Editor-schema aanwezig; regressie per browser nog uitvoeren |
| Badkamermeubels desktop | **USER_APPROVED_UI / VERIFIED_THEME** | Hubsysteem, compacte hero en duidelijke categorie-CTA; Admin-description CSS dependency |
| Badkamermeubels mobiel | **USER_APPROVED_UI / VERIFIED_ADMIN** | Compacte rijnavigatie goedgekeurd; CSS deels in collectieomschrijving |
| Badkamermeubels SEO-basis | **IMPLEMENTED_THEME** | H1/H2/H3/H4, canonical/head, JSON-LD `CollectionPage`/`BreadcrumbList`/`ItemList`. GSC-rankings niet gemeten |
| Andere hoofdcategorieën | **IMPLEMENTED_THEME** | `category-landing` via 12 collectie-suffixes, menu's en adviserende inhoud |
| Native productlijsten/filtering | **IMPLEMENTED_THEME** | `collection.json` + Shopify facets/paginering; werkelijke filterdata hangt van Admin af |
| Productdetailpagina | **IMPLEMENTED_THEME** | Gallery, koopbox, options, specs, plus/min, sets, accessoires, aanbevelingen als code aanwezig |
| Product-switcher V2 | **IMPLEMENTED_THEME / DATA_DEPENDENCY** | Custom switcher + ca. 1,9 MB JSON; actuele productdekking niet integraal geverifieerd |
| Exacte Hotbath setonderdelen | **IMPLEMENTED_THEME / SOURCE_CHECK_NEEDED** | Exacte SKU-mapping in snippets; per SKU controleren |
| Accessoires / cross-sell | **IMPLEMENTED_THEME / SOURCE_CHECK_NEEDED** | Beperkte curated mappings; niet alle producten gedekt |
| Externe filterservice | **IMPLEMENTED_TEST_ONLY** | Alleen `wastafelkranen?bcfilters=1`; VPS-health en foutfallback niet bewezen |
| Productcatalogus Admin | **VERIFIED_ADMIN (counts only)** | 11.053 totaal, 11.051 ACTIVE, 1 DRAFT, 1 UNLISTED, exacte telling. Publicatie/kwaliteit niet bewezen |
| Categorieën | **VERIFIED_ADMIN (counts/assignment)** | 204 collecties: 191 default, 12 `category-landing`, 1 `bc-meubelhub` |
| Menu's | **VERIFIED_ADMIN** | 9 gedefinieerde menu's en hun boom/URLs opgeslagen |
| Productmetafield-schema | **VERIFIED_ADMIN (definitions only)** | 174 productdefinities; 54 in code letterlijk gebruikte keys niet als huidige PRODUCT-definitie teruggevonden, geen defectclaim |
| Betaal-/verzend-/BTW-regels | **NOT_VERIFIED** | Shopify Admin / testcheckout nodig |
| Core Web Vitals | **NOT_VERIFIED** | Alleen code-opbouw geaudit; geen actuele LCP/CLS/INP-meting |
| Google-indexatie/rankings | **NOT_VERIFIED** | GSC-gegevens niet in theme-repo |
| Externe VPS/leverancierimporters | **OUTSIDE_REPOSITORY** | Frontend/deelcontext bekend; backend/deployment/brondata moeten apart worden overgedragen |

## 2. Aanbevolen prioriteiten bij hervatting

### P0 — voorkom onjuiste klantdata / onverwachte uitval

1. **Productkwaliteit per merk valideren.** Maak een Shopify-export met SKU, vendor, titel, variantprijs, voorraad-/publicatiestatus, afbeelding, collectie, belangrijke metafields en SEO. Controleer ongepubliceerde, lege en verouderde gegevens. Geen massale correcties zonder bron.
2. **VPS/filter-gate correct afhandelen.** Test opt-in end-to-end (health, index, CORS, API, error fallback) voordat het sitebreed actief wordt. Native filter op publieksroutes intact houden.
3. **Shopify checkout, belasting, betaling, verzending en wettelijke teksten** laten controleren door bevoegde merchant. Theme/Git zeggen hier niets definitiefs over.

### P1 — maak onderhoud nog robuuster

4. **CSS-handoff neutraliseren:** drie beschreven inline CSS-blokken uit de Badkamermeubels-collectiebeschrijving gecontroleerd migreren naar `assets/bc-meubelhub.css`. Pas verwijderen uit Admin als mobiel/desktop exact hetzelfde blijft.
5. **Metafield-schema en rendercode harmoniseren:** echte `custom.*`/`specs.*` waarden per SKU vergelijken, contract/namespace beslissen en daarna kleine batch testen.
6. **Externe codeprojecten archiveren en overdragen** via veilige zakelijke opslag met een apart Git-repo/back-up waar passend. Vooral filterbackend, indexer, Hotbath/Wiesbaden/JEE-O importcode en bronschema's.
7. **Up-to-date browser/SEO/performance QA** uitvoeren voor homepage, hub, PDP, native listing, menu/cart.

### P2 — groei en onderhoud

8. Uitbouwen van echte, relevante subcategorie-/merk-/maatlandings met producten en unieke nuttige inhoud.
9. Documenteerde releaseprocedures automatiseren (read-only diff, regressie en theme-check) waar toepasbaar.
10. Pas na audit en rollbackplan test-/backupassets opruimen; schoon Git betekent **niet** alle oude bestanden verwijderen.

## 3. Open besluiten die iemand zonder originele ontwikkelaar niet moet raden

| Vraag | Wie moet kiezen / waarmee onderbouwen |
| --- | --- |
| Welke metafield namespace is definitief voor iedere productklasse? | Productdata-eigenaar, echte Shopify-waarden, bronmapping |
| Wanneer mogen lege categorieën klikbaar en indexeerbaar zijn? | SEO/merchandising-eigenaar met werkelijk assortiment |
| Mag externe filterindex standaard productlijsten vervangen? | Frontend/backend/commerce na foutfallback-, privacy- en loadtests |
| Wat zijn officiële levertijd-, voorraad- en garantieclaims? | Leveranciersregels en commerciële/juridische eigenaar |
| Welke importcode/CSV is per merk de laatste versie? | Oorspronkelijke datamappen, bronversie, SHA/batchlogs |
| Waar liggen serversecrets, backups, domein en Search Console? | Bevoegde IT/merchant; niet in openbare Git |
| Wat is meetbaar de huidige checkout- en bestelstatus? | Shopify Admin + veilige testbestelling en merchant akkoord |

## 4. Hoe dit document actueel houden

Na een goedgekeurde verandering: noteer datum, geraakte files/Admin-objecten, bron/commit, menselijk akkoord, verrichte test en eventuele prestatiecijfers. Trek een nieuwe Shopify MAIN-themasnapshot bij een themapublicatie. Actualiseer de menu-/metafield-/collectiedefinities zodra die wijzigen.

**Voorkom twee strijdige waarheden:** het september-masterplan blijft een historisch besluitdocument, deze actuele status en `AI_HANDOFF_CURRENT.md` beschrijven 7 oktober. Vraag altijd live Shopify/Git opnieuw op; een toekomstige bron kan beide documentmomenten achterhalen.
