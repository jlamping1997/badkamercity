# SEO-afronding — 10 november 2026

Status: CATEGORY-METADATA-02 / PREVIEW_VERIFIED_AUDIT_COMPLETE. Vervolgopdracht eigenaar: “oke letsgo doe maar”.

## Resultaat en bereik

De 171 eerder toegepaste live metaparen blijven staan. Acht vendor-selecties, /collections en /collections?view=merken zijn nu in een afzonderlijk bewezen identieke kopie van MAIN geïmplementeerd en op de echte Shopify-preview gecontroleerd. Er is geen thema gepubliceerd en geen MAIN-bestand geschreven.

| Thema | ID | Status | Broncontrole |
| --- | --- | --- | --- |
| Live categorieverbeteringen | 196395073802 | MAIN | 1.401 bestanden; volledig ongewijzigd sinds de kopie |
| SEO afronding 10 nov | 196441932042 | UNPUBLISHED | 1.401 bestanden; precies vier SEO-verschillen |

Het Wiesbaden-concept 196416504074 is door deze uitvoering niet beschreven. De andere uitvoering heeft inmiddels 51 artikelen in zes groepen en eigen testgrenzen; raadpleeg de actuele Wiesbaden-overdracht, niet de oude 31-artikelenstand. De SEO-kopie bevat die ongepubliceerde Wiesbaden-uitbreidingen niet.

## Vier bestanden

- shopify/current/layout/theme.liquid: afgebakende metadata voor acht bestaande vendorselecties en het merkenoverzicht; het bestaande assortiment krijgt de goedgekeurde vertaalwaarden.
- shopify/current/snippets/meta-tags.liquid: optionele canonical-parameter zodat og:url aansluit bij de eigen merkenview.
- shopify/current/locales/nl.json: goedgekeurde Nederlandse meta’s, zonder overige vertalingen te vervangen.
- shopify/current/locales/en.default.json: overeenkomstige Engelse fallback; alleen Nederlands is gepubliceerd.

Het merkenoverzicht heeft aantoonbaar eigen inhoud, de kop Onze merken en bestaande interne links. Alleen deze view krijgt daarom /collections?view=merken als eigen canonical. /collections en alle overige gecontroleerde canonicals blijven behouden. Geen nieuwe routes, redirects, noindex-regels of zichtbare paginakoppen.

## Verificatie

- Nieuwe kopie eerst volledig gepagineerd: 1.401/1.401 bestandschecksums gelijk aan MAIN, inclusief beschermde bestandsinventaris. Geen settings_data-body gelezen of geschreven.
- Vier writes; nul userErrors; alle vier bodies exact teruggelezen.
- Officiële Shopify-validator lokaal: vier bestanden geldig, nul fouten. Eén al bestaande scheme_classes-waarschuwing in layout, ook op de ongewijzigde bron aanwezig.
- 22 gerichte head-renderregressies PASS: acht merken, beide overzichten, bestaande categorie-SEO/homepagevoorkeuren/fallbacks, onbekend merk, andere view, paginering, wishlist-noindex en Engelse fallback.
- Echte HTTP-preview met behoud van Shopify-previewcookie: 15/15 HTTP 200 en exacte meta’s; alle antwoorden bewezen thema 196441932042. De tien doelen plus homepage, Sunshower-pagina, Wastafelkranen, Afvoerpluggen en Badkamermeubels. Alle 15 H1s behouden; één bedoelde canonicalwijziging, overige 14 gelijk.
- Browser-DOM merkenoverzicht bevestigt titel, description, H1, canonical en og:url.
- Hotbath IBS70-productcontrole: live/preview servermarkup met gelijke H1 en keuzebron bc-hotbath-menu-data-005.json. Dit bewijst geen koopactie.
- Finale volledige inventaris: MAIN 1.401 ongewijzigd, SEO-concept 1.401, precies vier geregistreerde verschillen.

Niet getest: eigenaarpublicatie, native mobiele bediening, winkelwagen in dit SEO-concept, nieuwe rankings/CTR/conversies. De lokale HTML-rapportlogica is gericht in Node gecontroleerd; geen browser-render van het lokale rapport geclaimd.

## 58 apart gehouden collecties

Alle 58 individueel herbeoordeeld op verse collectieleden, publieke inhoud, sitemap en gerichte catalogusmatches; 55 gerichte productzoekopdrachten plus drie technische/selectiegevallen. Negen menu’s en 227 collectieomschrijvingen gecontroleerd. Alleen een verwijzing naar Meer in menu assortiment; geen verwijzingen vanuit de gelezen collectieomschrijvingen. Niet bewezen dat dit menu publiek actief is.

57 routes zijn HTTP 200, Tegeltoebehoren blijft de bekende 404 buiten de sitemap. Alle 57 overige routes staan wel in de collectie-sitemap. Meer heeft 24 Admin-leden maar de hoofdinhoud toont geen product- of categorielinks. Deze audit wijzigt geen leden, menu’s, SEO-velden, robots of publicatiestatussen.

Vijf concrete herstelvoorstellen, met bestaande collectie-ID, exacte product-IDs en een conceptmeta voor ná selectieherstel:

| Bestaande collectie | Bevestigde kandidaten | Grond |
| --- | ---: | --- |
| badmeubel-sets | 39 | Verlavio Londen/Birmingham, wastafel + spiegel of spiegelkast |
| badmeubel-met-spiegel | 19 | Birmingham, omschrijving bevestigt Inclusief Spiegel |
| badmeubel-met-spiegelkast | 20 | Londen, omschrijving bevestigt Inclusief Spiegelkast |
| toiletspiegels | 24 | Hotbath &More-toiletspiegels |
| toilet-accessoires-sets | 1 | Lagoo Garda G6115: rolhouder, borstelhouder en haak |

Dit zijn 64 unieke producten; meubels overlappen op logische boven-/subcategorieën. Badkamermeubel met wastafel is dezelfde 39-delige setscope: eerst primaire bestemming bepalen. Wastafel Kom is onvoldoende bewijs voor een losse opzetwaskom. Alle 39 gecontroleerde sets hebben een spiegel of spiegelkast, dus niet bruikbaar voor Zonder spiegel.

Sunshower en IBS70 hebben al werkende bestemmingen. De exacte IBS70-modelzoekopdracht leverde volledig gepagineerd 358 passende producten; de brede IBS70*-zoekopdracht telt ook andere modellen en is geen geldige selectie. Losse verwarmingsmatten zijn iets anders dan complete verwarmde spiegels. Een staande toiletborstelhouder is geen staand toilet; kraanknoppen zijn geen bewezen radiatorknoppen. De kortingszoekopdracht leverde alleen een openbaar testproduct; dat is geen outletselectie en is niet door deze uitvoering verwijderd.

De individuele besluiten en beperkingen staan in held-category-review.json. Een nulresultaat in gecontroleerde zoekvelden bewijst geen winkelbreed ontbreken. Herstel van categorieleden vereist controle van de publieke selectie en externe filterindex voordat de voorwaardelijke meta wordt toegepast.

## Google: werkelijk waargenomen

Search Console-eigendom voor https://badkamercity.nl/ is automatisch geverifieerd bij het openen/toevoegen van de URL-prefixproperty. Geen DNS- of verificatietagwijziging. De sitemap was al ingestuurd op 8 november: status Success, laatst gelezen 10 november, 16.247 gevonden pagina’s. Niet dubbel ingestuurd.

De daadwerkelijke Google-zoekopdracht voor /collections/wastafelkranen toont nog Wastafelkranen – Badkamercity met de oude beschrijving. Inspectie: URL is on Google, geïndexeerd, Googlebot smartphone, laatst gecrawld 8 november 2026 om 11:34:20 zoals in de UI weergegeven (tijdzone onbekend). De pagina mag worden gecrawld/geïndexeerd en Google gebruikt dezelfde canonical.

Eén herindexeringsaanvraag voor deze bestaande live URL is geaccepteerd en aan de priority crawl queue toegevoegd. Geen bulkherhaling. Rapportmodules geven nog Processing data aan; geen CTR- of conversiewinst vastgesteld en geen datum voor nieuwe snippets beloofd. google-verification.json onderscheidt bron, waarneming en beperking. Dit staat los van Ads-tag-/campagneontvangst.

## Release en herstel

Eén volgende SEO-handeling: eigenaar beoordeelt het SEO-concept; neem de vier SEO-wijzigingen na verse bronvergelijking mee in het definitieve releaseconcept. Als het Wiesbaden-concept de uiteindelijke release wordt, eerst deze vier bestanden daarin samenvoegen en de tien preview-heads opnieuw controleren. Een later gepubliceerde oudere themakopie mag de SEO niet terugdraaien. Niet zelfstandig publiceren of MAIN schrijven.

Originele vier bodies zijn vóór de write privé bewaard in Badkamercity-SEO-thema-backup-2026-11-10.json. Herstel alleen de vier betrokken conceptbestanden na checksumcontrole dat ze nog onze versie zijn; nooit een volledige themakopie over latere wijzigingen zetten. De eerdere 171 Admin-meta’s hebben hun eigen veldgerichte back-up.

Connectoruitvoering; geen lokale Git-checkout of Windows-controle. Code op fix/product-cards-2026-10-14 onder shopify/current, main alleen documentatie. Behoud andere werkstromen. Geen actieve SEO-schrijver na deze overdracht.
