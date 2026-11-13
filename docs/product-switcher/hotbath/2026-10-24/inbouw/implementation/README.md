# Hotbath inbouwdeel meebestellen — implementatie, 24 oktober 2026

**Status: IMPLEMENTED_PREVIEW / DESKTOP_QA_PASS / NOT_PUBLISHED.** Deze wijziging laat klanten bij gecontroleerde afbouwartikelen expliciet kiezen of zij het juiste inbouwdeel willen meebestellen. Ja voegt beide echte artikelen toe; Nee behoudt de bestaande kooproute. Geen betaalde keuze vooraf geselecteerd.

**Werkconcept:** UNPUBLISHED `195664052490`, aangemaakt vanuit MAIN `195649929482` (BadkamerCity - Hotbath keuzemenus 24 okt). Alleen het concept is schrijfdoel. Geen livewrite of publicatie uitgevoerd. Voor de upload waren alle 532 bestanden checksum-identiek aan MAIN. Acht bestanden geschreven en exact teruggelezen; concept heeft nu 536 bestanden (vier gewijzigd, vier nieuw, 528 ongewijzigd). MAIN is na afloop nog 195649929482 en al zijn 532 checksums zijn ongewijzigd. Zie upload-readback.json en final-theme-manifests.json.

## Gegevens en besluiten

- **715 exacte routes / 134 modellen / 44 inbouwdelen:** 177 artikelen uit de oorspronkelijke directe boekkoppelingen, 460 uit de uitbreiding en 78 op basis van de laatste bevestigingen van de eigenaar.
- De eigenaar gaf voor 79 artikelen een inbouwdeel op. **B010EXTGN blijft apart**, omdat exact `HBCB010` niet in Shopify is gevonden. Een actuele SKU-zoekopdracht gaf nul resultaten zonder vervolgpagina. Geen vervanging door HBCB010H/C gegokt.
- **70 artikelen uitgesloten** van de inbouwdeelkeuze volgens de eigenaar. “Verwijderen” betekent in deze taak uitsluitend verwijderen uit de add-onlijst. **Geen producten verwijderd, gearchiveerd of hernoemd.** AR087 wordt ook niet automatisch vervangen in productdata.
- Zes eerdere kleur-/boekcodegevallen blijven apart: `CB007EXTBC`, `CB009EXTBC`, `CB009EXTBK`, `CB009EXTNB`, `CB009EXTNBP` en `GLF011EXTBGP`.
- Eerdere uitzonderingen blijven buiten deze gewone Ja/Nee-functie: vijf MHF-naamaliassen, onbeantwoorde GT7072/GY011D-bronconflicten, ontbrekende bodies, CB7001 horizontaal/verticaal, Rails met inbegrepen bodyprijs, IBS en SPOM.

De 766 gebruikte productrecords zijn opnieuw uit Shopify gelezen. De compiler controleert exacte product-/variant-ID's en SKU's, één variant per artikel, Hotbath-merk, actieve Online Store-publicatie, verkoopbaarheid, positieve prijs en geen `met_inbouwdeel=true`. Uitgesloten SKU's hebben voorrang op bronnen. Er wordt geen bodycode uit een prefix afgeleid.

Bron- en besluitbestanden:

- [Eigenaarsbesluiten voor alle 149 resterende EXT-artikelen](data/merchant-decisions.json)
- [Alle 715 runtimekoppelingen, herkomst en zeven holds](data/compiled-mapping.json)
- [Controle oorspronkelijke 26 modellen en kleurcodes](data/original-direct-finishes.json)
- [Verse productgegevens](data/fresh-products.json) en [ontbrekend HBCB010](data/hbcb010-exact-search.json)
- [Compiler](data/build_runtime_mapping.py), [gegevenscontroles](data/data-verification.json) en [exact routebestand](theme/snippets/bc-product-inbouw-data.liquid)

De eerdere boekdossiers blijven de bron voor de oorspronkelijke en aanvullende mappings. De nieuwe eigenaarsbesluiten zijn expliciet als `MERCHANT_EXPLICIT_CONFIRMATION_2026-10-24` gemarkeerd; zij worden niet als boekbewijs voorgesteld. Volledige boekpagina's en interne visuele controlebeelden horen niet in de publieke repository.

## Koopgedrag en grenzen

De route bevat alleen `trimVariantId|trimSku|bodyHandle|bodySku|bodyVariantId|1`. Liquid controleert de werkelijke huidige product- en variantgegevens opnieuw. **Prijs en beschikbaarheid komen uit het gekoppelde Shopify-artikel**, niet uit het boek of de routetabel.

Bij Ja wordt één aanvraag verstuurd met afbouwdeel en inbouwdeel. Aantal 2 betekent 2+2. Een eerder aanwezige bodyregel in de winkelwagen is geen reden om het nieuw gevraagde exemplaar over te slaan. Na bewezen succes opent de gewone winkelwagen; Nee behoudt de bestaande enkele-productmelding. Bij onzekere netwerk-/voorraad-/deelrespons stopt herhalen en moet de klant de winkelwagen controleren. Er is geen automatische retry of terugdraaiing van bestaande winkelwagenregels.

Kleur-/lengtewissels bewaren een expliciete keuze uitsluitend bij dezelfde bestaande switchergroep en hetzelfde inbouwdeel. Direct versneld afrekenen is bij deze gekoppelde artikelen uitgeschakeld. De twee winkelwagenregels blijven normale zelfstandige artikelen: later handmatig aanpassen of verwijderen van één regel wordt niet als vaste bundel afgedwongen.

## Scope: acht themabestanden

| Bestaand aangepast | Doel |
| --- | --- |
| `assets/product-form.js` | Kleine koppeling met de add-oncontrole vóór de bestaande kooproute |
| `snippets/buy-buttons.liquid` | Add-onweergave en blokkeren van direct versneld afrekenen bij gekoppelde artikelen |
| `locales/nl.json` | Nederlandse teksten in nieuwe bc-namespace |
| `locales/en.default.json` | Engelse terugvalteksten in dezelfde namespace |

| Nieuw | Doel |
| --- | --- |
| `snippets/bc-product-inbouw-data.liquid` | 715 exacte routes; 79.838 bytes |
| `snippets/bc-product-inbouw.liquid` | Gevalideerde productgegevens, prijs en Ja/Nee-keuze |
| `assets/bc-product-inbouw.js` | Keuze, aantal, dubbele verzendbeveiliging en gecombineerde winkelwagenactie |
| `assets/component-product-inbouw.css` | Compacte keuzekaarten passend bij de productpagina |

Cartdrawer/-notification, product-info, bestaande switcher en Sunshower-bestanden zijn buiten deze patchscope. Producten, prijzen, voorraad, metafields en betaalinstellingen worden niet gewijzigd.

## Controles

**36 geautomatiseerde controles geslaagd:** 9 compiler-/gegevenscontroles en 27 JavaScript-/formuliercontroles. De JavaScriptproeven draaien in een Node VM met DOM-/transportdubbels; zij zijn geen bewijs van echt browser- of Shopify-winkelwagengedrag. De gegevenssuite werkt ook via unittest-discovery nadat `FRESH_PATH` op moduleniveau is gezet.

- [Carttests en resultaten](cart-tests.json)
- [Onafhankelijke statische beoordeling](review.json)
- [Test gegevenscompiler](data/test_runtime_mapping.py)

**Echte desktopbrowsercontrole PASS (Chrome, 1348×936):** CB105EXT18CR toont HBCB105 +€174 zonder vooraf geselecteerde keuze; toevoegen zonder keuze vraagt om Ja/Nee. Ja met aantal2 leverde exact2 CB105EXT18CR +2 HBCB105 op (totaal€778). Nee bleef geselecteerd bij kleurwisseling naar BCP en lengtewisseling naar25cm; toevoegen leverde uitsluitend1 CB105EXT25BCP (€388) met de bestaande bevestigingsmelding op. CB126EXTBCP, IBS70CR en de aangehouden B010EXTGN hebben geen add-on. De nieuwe CB7071EXTCR-relatie toont HBCB7071 +€867. Alleen eigen testregels toegevoegd/verwijderd, begin- en eindwinkelwagen leeg. Zie browser-qa.json.

**Lokale themavalidatie PASS:** @shopify/theme-check-node3.30.1 rechtstreeks met geïnstalleerde schema/documentatiebestanden en geblokkeerd uitgaand netwerk; geen nieuwe fouten, vijf parsercontroles goed. Eén verwachte complexiteitswaarschuwing op de gegenereerde715-routecasetabel. Vijf ontbrekende afhankelijkheden zijn artefacten van de gedeeltelijke lokale snapshot en stonden al in de baseline. Hun werkelijke bestanden staan in de remote manifesten; de kooproute is daadwerkelijk gerenderd. De online wrapper is niet als succesvolle validatie opgevoerd: automatische goedkeuringscontrole blokkeerde verzending van broncode/gebruikersinstructies naar een externe ontwikkelservice. De lokale vervanging las geen prompt en deed geen netwerkpogingen. Zie local-validation.json.

**NOT_TESTED:** fysieke mobiel/afzonderlijke mobiele viewport, echte voorraad-/netwerkfoutraces, betaalstap en elk van715 pagina’s afzonderlijk. Foutpaden zijn geautomatiseerd getest met transportdubbels. Geen bestelling geplaatst. Geen Windows-worktreecontrole; scratch is geen Gitcheckout.

## Terugzetten en vervolg

Terugzetten gebeurt alleen in het ongepubliceerde concept: herstel de vier bestaande bestanden vanuit de overeenkomstige bestanden onder `source-theme/` en verwijder daarna de vier nieuwe bestanden. Als verwijderen technisch niet beschikbaar is, laat de nieuwe bestanden ongebruikt staan; herstel van de vier bestaande verwijdert hun actieve aanroep. Controleer bestandschecksums en afwezigheid van de add-onweergave. Dit herstel wijzigt geen productdata.

**Volgende handeling:** eigenaar beoordeelt de conceptweergave, met name op zijn telefoon, in Shopify-thema “BadkamerCity - Hotbath inbouwkeuze 24 okt”. De eigenaar publiceert zelf; er wordt hier geen publicatie uitgevoerd. Daarna kan de vormgeving van de gezamenlijke kleur-/maat-/inbouwkeuzes verder worden verfijnd. Huidige MAIN en conceptrol vóór iedere vervolgwrite opnieuw lezen.
