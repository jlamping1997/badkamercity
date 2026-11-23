# Verlanglijstpagina: renderen, productcache en toevoegen

> **31 oktober 2026 — FIX-01, UNPUBLISHED195948839178:** Sunshower commit roept scoped wishlistrefresh aan; read/commit-fouten geven geen succes. Productread-timeout/TTL en echte voorraadautoriteit blijven afzonderlijk open; bewaren reserveert niets. [Actueel bewijs en rollback](../../../repairs/2026-10-31/README.md). De bronregels/hashes en defectreplays hieronder beschrijven de eerdere nulmeting.

**28 oktober 2026 · DOC-03D.** Eigenaar van productread/paginarender/kooproute. [Identity](WISHLIST_IDENTITY.md) verklaart hartjesadapters; [opslag](WISHLIST_STORAGE.md) de bewaarde selectie. [43 cases en methode](../../evidence/2026-10-28-wishlist/README.md) zijn lokale replays; ieder productantwoord, cartantwoord en navigatieverzoek is nagebootst. Geen echte add of restore.

## Route en eerste render

`templates/page.bc-wishlist.json` kiest één `bc-wishlist-page`-sectie zonder instellingen. De sectie levert titel, telling, loading/empty/grid, assortimentslinks, browsergebonden-opslaguitleg en noscriptmelding. De gedeelde JS zoekt data-bc-wishlist-page. Deze ronde controleert template/sectionbytes; de daadwerkelijke Admin-Page-toewijzing is niet opnieuw gelezen.

`renderPage` (bc-wishlist.js:346–371) verhoogt rendering, vernieuwt de telling, verwijdert de vorige gridkinderen en zet leeg/grid op basis van de geheugenlijst. De algemene loading wordt direct verborgen; ieder kaartje toont daarna zijn eigen voorlopige prijs-/gegevensmelding. Bij nul entries doet hij geen productread (WL-01).

`cardShell` (:260–290) maakt DOMnodes met productlinks inclusief de opgeslagen variantquery, een verborgen lazy afbeelding, placeholder, titel, variantlabel, prijs, leveruitleg, primaire link en verwijderbutton. Tekst wordt via textContent geplaatst, niet als opgeslagen HTML. Een entry is al direct verwijderbaar terwijl het product nog laadt.

## Productread en cache

`readProduct(handle)` (:185–194) gebruikt `/products/<handle>.js`, credentials=same-origin en Accept application/json. Een Map bewaart per handle de **promise**, zodat meerdere variants/renders dezelfde in-flight of succesvolle response kunnen delen. Een fout verwijdert de cacheentry voor een latere retry (WL-20). HTTPfouten blijven favorieten in de lijst laten staan; prijs/fouttekst en productlink blijven zichtbaar (WL-32).

Er is geen TTL, expliciete AbortController of productrequesttimeout in deze helper. WL-37 bevestigt dat een latere rerender én add dezelfde succesvolle productresponse hergebruiken. Een readProduct-call in add is dus geen gegarandeerde nieuwe servercontrole. WL-38 houdt een synthetische request onbeslist: de kaart kan op ‘Prijs ophalen…’ blijven staan; verwijderen blijft beschikbaar. Dit zijn **WISH-B01-grenzen**, geen bewijs van huidige verkeerde prijs, voorraad of een vastlopende echte server.

De sectietekst ‘Prijzen worden opnieuw uit de winkel opgehaald’ geldt voor productreads tijdens deze pagina-opbouw, niet voor iedere knopdruk of een permanent realtime abonnement. Shopify blijft bij werkelijk toevoegen de cartautoriteit. Ontwerp bij een cachewijziging apart hoe een onzekere POST wordt behandeld; vaker GET doen is geen reden om een POST automatisch opnieuw te sturen.

## Vier workers en verouderde render

Per render starten maximaal vier hydrationworkers. Na een afgeronde hydrate pakt een worker de volgende entry zolang zijn render-ID nog actueel is. WL-34 bevestigt vier eerste aanvragen en een vijfde na afronding. Dit is een **limiet per render**, geen universele paginabrede transportlimiet: oude requests worden niet afgebroken wanneer een nieuwe render start.

`hydrate` (:298–344) controleert na de productread zowel renderId als card.isConnected. Een verwijderde of door een nieuwe render vervangen kaart wordt daardoor niet door een oud antwoord teruggezet (WL-33). Oude requestpromises mogen nog lopen en blijven via cache gedeeld. De replay bewijst geen daadwerkelijk geheugen-/netwerkprofiel onder 100 producten.

## Exacte uitvoering en presentatie

De renderer zoekt uitsluitend de opgeslagen variantId in product.variants. Zonder match verschijnt ‘Deze uitvoering is niet meer beschikbaar’; hij kiest niet stil een andere uitvoering en maakt geen addbutton (WL-25). Titel wordt uit productdata gehaald; niet-Default Title-variantlabels worden zichtbaar. Prijs komt van variant.price in centen en wordt nl-NL/EUR geformatteerd. De renderercontrole van null/ontbrekende prijs en alle echte valuta-/marktcontexten is niet in deze ronde afgetest.

Afbeeldingvolgorde: variant.featured_image.src → product.featured_image → eerste product.images → opgeslagen image. safeImage accepteert HTTPS of dezelfde origin; javascript: wordt geweigerd. WL-39 bevestigt tekst-escaping en die ene onveilige imagevorm, geen algemene securityaudit. Een gewone afbeeldings-load/error met echte CDN-respons is niet getest.

## Wanneer een directe koopknop ontstaat

| Product/entry bij hydrate | Primaire actie | Replay |
| --- | --- | --- |
| Opgeslagen variant ontbreekt | Productlink met foutuitleg | WL-25 |
| Variant.available is expliciet false | Bekijk product | WL-31 |
| source=sunshower | Bekijk uitvoering | WL-26 |
| Meerdere variants en source=card | Bekijk uitvoering | WL-27 |
| Product of variant vereist selling plan | Bekijk uitvoering | Productflag WL-28; variantflag alleen bronreview |
| quantity_rule.min of increment aanwezig en niet 1 | Bekijk uitvoering | WL-29/30 |
| Overige toegestane uitvoering | Button In winkelwagen | WL-24 |

Voor hydrate blokkeert available===false; add vereist later een truthy variant.available. Dat verschil is gelezen bronbeleid; geen onverwachte echte Shopify-response of extra bezoekersbug vastgesteld. De source is dus een functionele adapter: een expliciet op PDP gekozen variant kan anders worden behandeld dan een algemene kaartfavoriet met meerdere uitvoeringen.

## Toevoegen en foutpad

`addFromPage` (:373–403) zoekt de entry opnieuw op identity, negeert een disabled knop en zet ‘Toevoegen…’. Hij leest de gedeelde productpromise en controleert exacte variant, beschikbaarheid, source, meervariant-card, selling plan en minimum/increment opnieuw. Bij een afwijzing vraagt hij productnavigatie aan; er is dan geen add-POST.

Bij toelating gaat één JSON-POST naar routes.cart_add_url of `/cart/add`, met `.js` toegevoegd: `{id:Number(variantId), quantity:1}`. WL-35 bevestigt de payload voor een synthetische ID en blokkeert de tweede klik op dezelfde button. De volledige 20-cijferige toegestane opslag-IDrange is niet als Number-precisiegarantie getest; geen huidige product-IDfout afleiden.

Een HTTP- of transportexception herstelt buttontekst/enabled en toont een toast (WL-36 test HTTPfout). De code heeft geen aparte uncertainstatus na een onzekere POST. Een toekomstig foutcontract moet rekening houden met ‘server kan al toegevoegd hebben’; geen automatische retry als documentatiecorrectie invoeren. Het inbouwpad heeft daarvoor een [ander expliciet contract](INBOUW_RECOVERY.md).

Na response.ok vraagt de code cartnavigatie aan. Hij rendert geen cartnotification, publiceert geen Dawn-cartUpdate en verwijdert de favoriet niet. Dit verklaart de bestaande afwijkende bevestigingsroute uit [cartfeedback](../CART_AND_FEEDBACK.md); het is geen bewijs dat iedere ingang dezelfde popup hoort te krijgen. WL-35 blijft volledig synthetisch en bewijst geen servermutatie, cartsaldo of getoonde bestemmingspagina.

## Onderhoud en open praktijkcontroles

Geen root-themefile synchroniseren op basis van alleen een oud Gitbestand. Controleer de bronhash, kies het afgesproken conceptthema en behoud identity-/renderguards. Test actuele/missende variant, één/meerdere uitvoeringen, unavailable, selling plan, quantityregels, productfout/hang/retry, verwijderen tijdens laden, nieuwe render tijdens oude read, beide sources en fout/onzeker/succes. Echte browserfocus na verwijderen/rerender, screenreaderstatus, mobiel, CDN-afbeeldingen, markt-/valutacontext en cartgedrag blijven open.
