# Webshop — actuele basis en resterende verkoopcontrole

> **Actueel CONTENT-ENCODING-02 — 8 november:** MAIN 196368531722 is eigenaar-gepubliceerd; klantenservice-/bezorg-/retourverwijzingen publiek gecontroleerd. Dertien uitlegpagina’s opgeschoond: negentien accenten en vier voorlooptekens; SEO/links/structuur gelijk. Verse telling 122 Pages/120 gepubliceerd; 109 termlinks op gepubliceerde doelen gemapt. [Nieuw dossier](../repairs/2026-11-08/glossary-encoding/README.md). Geen product-/tarief-/policywrite of algemene checkoutvrijgave.

**Stand: 8 november 2026 — bezorginformatie en tariefcontrole.** De winkel is openbaar. De [diepe audit](../audits/2026-11-08/README.md) behoudt zijn gedateerde inventaris en 364 publieke responses. Daarna zijn footer, Contact en gerichte content gecorrigeerd en is de [bezorginformatie](../repairs/2026-11-08/delivery-information/README.md) aangevuld. Dit is geen volledige goedkeuring van alle koopflows of producten.

## Wat is bewezen

| Onderdeel | Resultaat | Grens |
| --- | --- | --- |
| Winkel / catalogus | HTTPS, hoofdadres badkamercity.nl; 15.897 ACTIVE + Online Store | Publicatie bewijst geen fysieke voorraad of harde levertijd |
| Inhoud | Diepe-auditcapture: 121 Pages, waarvan 119 gepubliceerd; 227 collecties. Nieuwe Page Bezorgen en afhalen afzonderlijk live aangemaakt | Geen nieuw catalogus-/paginatotaal geclaimd zonder hertelling; geen individuele productcataloguscontrole |
| HTTP / HTML | 360 × 200 en 4 × 404 in 364 responses; geen gevonden JSON-LD-parsefouten of ontbrekende lokale ankers | Eén bewuste 404 en één gegiste Engelse blogroute; geen rich-results-/JavaScriptvrijgave |
| Bestelproef, eerder op 8 november | Zoekopdracht Wiesbaden; Wastafelkranen met Inbouw + Chroom; Wiesbaden Ribbd SKU 29.5330 van €245, twee stuks €490; gastcheckout bereikbaar | Desktopbrowser, geen klant-/adresgegevens ingevoerd, betaling of mail getest; eigen cart opgeruimd |
| Retourpolicy | Live en leesbaar; 30 + 14 dagen, retourkosten en modelformulier | Merchant-afstemming en ontvangst van retouraanmeldingen open |
| Homepage / footer | SEO behouden op huidige MAIN 196354474250; gedeelde footer op 14 publieke routes gecontroleerd | Retour-/bezorgverwijzingen in volgend concept; geen nieuwe ranking- of mobiele vrijgave |

De vier 404's zijn het ontbrekende `/policies/shipping-policy`, de lege collectie `/collections/tegeltoebehoren` zonder gevonden inkomende klantlink, de gegiste `/blogs/news` (echte Nederlandse blog en artikel geven 200) en de bewuste `/dit-is-een-controle-404`. Admin-menuverwijzingen leidden in de join niet naar lege collecties.

## Eerst afronden

1. **Identiteit en contact.** Gebruik het [actuele register](BEDRIJFSGEGEVENS.md). Zichtenburglaan 150 is contact-/retouradres; juridische vestiging en volledig btw-id moeten apart worden geverifieerd. Contactpagina en gedeelde footer bevatten de bevestigde telefoon, e-mail en contact-/retourlocatie; het native formulier blijft staan. Native Contact policy en juridische identiteit blijven afzonderlijk open.
2. **Beleid.** Retour, contact, privacy, voorwaarden en wettelijke kennisgeving bestaan. Voorwaarden en kennisgeving tonen letterlijke HTML-tags; opmaak herstellen en links controleren. De gewone Page [Bezorgen en afhalen](https://badkamercity.nl/pages/bezorgen-en-afhalen) is live; native SHIPPING_POLICY ontbreekt nog. De ontbrekende write_legal_policies-scope blijft een afzonderlijke blokkade. Eén gewone Page vervangt geen native policy of checkoutkoppeling.
3. **Levering.** Jackson werkt aan leveranciers-/levertijdbronnen. Verse NL-configuratie: €6,95 t/m €100 en €0 vanaf €100,01. Twee AJAX-cartquotes bevestigen €96,15 → €6,95 en €109,00 → €0; de eigen geïsoleerde cart is daarna leeg. coversAllItems=false en één locatie zonder rates blijven gericht te onderzoeken. Geen order of configuratiewijziging uitgevoerd; €75 retourpallet is geen heenzendtarief.
4. **Footer en informatieverwijzingen.** De gedeelde footer is al live. De bestaande bezorglink gaat nog naar het afhaalanker op de homepage. De verwijzing naar de nieuwe informatiepagina staat met de eerdere retourcorrecties in bestaand concept 196368531722 — Klantenservice 8 nov; [bronbewijs en uitvoeringscontract](FOOTER_EN_BELEID.md). Nog geen publicatie van die uitbreiding.
5. **Bestellen en mail.** Rond de [gerichte controles](CONTROLES.md) af: gekozen uitvoering, doosprijs, echte verzendquote, beschikbare betaalmiddelen, één afgesproken betaling en ordermail. Geen algemene testbetaalmodus in de openbare winkel activeren.
6. **Privacy en meting.** Cookiekeuzes waren als UI bedienbaar. Technisch consentgedrag en GA4-aankoopwaarden/ontdubbeling blijven apart open; geen extra tag blind toevoegen.
7. **Verplichte product-/garantie-informatie.** Toets de actuele informatieplichten en toepasselijke fabrikant-/veiligheidsinformatie gericht per producttype (BC-LIVE-015/016). Geen algemene veiligheidsovertreding of vaste wettelijke garantiegrens van twee jaar afleiden.

## Bezorgpagina en grenzen van de tariefproef

[Bezorgen en afhalen](https://badkamercity.nl/pages/bezorgen-en-afhalen), Page 166963937546, is live. Afhalen gebeurt uitsluitend op afspraak en na bevestiging dat de bestelling klaarstaat, bij Harry Suiker aan Zichtenburglaan 150, 2544 EB Den Haag. De pagina bevat geen verzonnen vaste levertermijn, vervoerder of uitgaand pallettarief. Voor retourkosten blijft de bestaande retourpolicy leidend.

De twee quotes bewijzen het gekozen NL-scenario, geen volledige product-, pallet-, kortings- of regiomatrix en geen geslaagde betaling. Productdekking en de ene locatie zonder rates blijven open. De Contacttekst verwijst naar de bezorgpagina en nuanceert het bestelnummer met indien bekend. Footer en homepage zijn in hetzelfde ongepubliceerde concept daarop aangesloten. De twee nieuwe files zijn exact teruggelezen en slagen voor Liquid; vier previewroutes slagen. Finale themavergelijking: 1.387 bestanden per thema, 1.381 gelijk en precies zes bedoelde verschillen; de vier eerdere retourfiles zijn exact behouden en MAIN is ongewijzigd. [Bewijs en vervolg](../repairs/2026-11-08/delivery-information/README.md).

## Productcontrole per batch

| Controle | Vereist bewijs |
| --- | --- |
| Artikel en uitvoering | Merk, echte fabrikantcode, kleur/maat, juiste native variant of gekoppelde productbestemming |
| Prijs | Consumentenprijs incl. btw, eenheid en meerprijs gelijk op kaart, PDP, cart en checkout |
| Beschikbaarheid | Werkelijke bestelbaarheid, voorraadbeleid en onderbouwde levertijd; niet alleen ACTIVE |
| Verpakking / tegels | Hele dozen, m² per doos, doosprijs en schema-/feedprijs; calculator ook interactief toetsen |
| Afbeelding | Correct artikel en kleur; bereikbaar en bruikbaar; expliciete eigenaarsuitzonderingen respecteren |
| Productinformatie | Kenmerken, inbegrepen/benodigde onderdelen, toepasselijke documenten, fabrikant-/veiligheidsinformatie |
| Kanaal | Online Store en Google afzonderlijk controleren |
| Identifiers | Echte SKU, merk, GTIN/EAN en MPN waar toegewezen; ontbrekend niet verzinnen |

Actuele tegelsteekproeven: RR6001 €68,95/m², doos 1,44 m² = €99,29 en schema Offer €99,29; RR1001 €79,95/m², doos 2 m² = €159,90; VP8002 €79,95/m², doos 1,28 m² = €102,34. Dit zijn gedateerde prijs-/HTML-voorbeelden; geen nieuwe volledige calculator-/cart-/mobiele proef. De oude prijsvoorbeelden van 5 november blijven alleen historische meetwaarden.

## Te behouden keuzes en afbakening

- **Lagoo:** foto's blijven volgens expliciete eigenaarsinstructie verwijderd. Niet terugplaatsen. Beeldloze producten apart voor Google-bestemming beoordelen; dit keurt de hele webshop niet af.
- **Verlavio:** FAB-03/04 bewijzen de rebrand en het gerichte koopbaarheidsherstel. De oude Fabriecio GM_1002-OutOfStock-meting is historisch. Beelden/identifiers en huidige feedstatus blijven afzonderlijke controles.
- **Levertijden:** eerdere herhaalde 8–9-wekenweergaven zijn een brontoets, geen bewijs dat ieder product fout is. Geen generieke belofte van maken.
- **Sunshower:** eerder gevonden afbeeldingsfoutteksten in server-HTML bewijzen zonder runtime-/beeldrequestcontrole geen defecte galerij.
- **Offerte-upload:** bestaande guard en eigenaarafspraak behouden; geen ontvangst-/uploadfunctie stil activeren.
- **Filters:** FILTER-SIMPLE-02v2 is volgens de actuele eigen overdracht APPLIED_VERIFIED / PUBLIC_API_VERIFIED / DESKTOP_UI_VERIFIED; installer niet herhalen. FILTER-ACERO-01 is volgens de latere parallelle overdracht APPLIED_VERIFIED / PUBLIC_API_VERIFIED; ook deze installer niet herhalen. Deze audit levert geen nieuwe filtertest en verandert die volgorde niet.

Een informatie- of productfout gericht oplossen en de betrokken promotiebestemming begrenzen. Meer merken, extra bloginhoud of cosmetische groei hoeven een correct werkende bestaande verkooproute niet tegen te houden. [Taken](TAKEN.md) legt vast wat per route nog openstaat.
