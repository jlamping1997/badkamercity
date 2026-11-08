# CONTENT-ENCODING-02 — tekstfouten hersteld, klantenservicepublicatie gecontroleerd

> **Volgend onderzoek afgerond — SHIPPING-COVERAGE-01:** de verzendprofielwaarschuwing is verklaard door de actieve Market met beide oorsprongen; acht tariefcarts PASS. /blogs/news is tevens live via301→200 hersteld. [Nieuwste bewijs en volgende taak](../shipping-and-blog/README.md). De vorige tekst hieronder bewaart het oorspronkelijke overdrachtsmoment.

**8 november 2026 · OWNER_PUBLICATION_VERIFIED / CONTENT_APPLIED_VERIFIED.** De eigenaar heeft Klantenservice 8 nov gepubliceerd. De volgende concrete verbetering is rechtstreeks in de bestaande uitlegpagina’s uitgevoerd: negentien kapotte accentcombinaties en vier voorlooptekens verwijderd. Geen nieuwe themapublicatie nodig voor deze Page-inhoud.

## Publicatie bevestigd

MAIN is nu **196368531722 — BadkamerCity - Klantenservice 8 nov**. Alle zes eerdere featurefiles hebben dezelfde MD5 als de getoetste preview en de actieve Git-bron. [Broncontrole](publication-source-proof.json). Er zijn in deze ronde geen themefiles geschreven of thema’s gepubliceerd.

[Veertien publieke routes](live-footer.json), zonder previewparameter, hebben dezelfde gedeelde footer met de nieuwe bezorg-Pagelink, telefoon, e-mail en het gelabelde contact-/retouradres. Homepage en retourpagina tonen de eerder voorbereide teksten en links. Dit is HTML-/bronbewijs, geen nieuwe mobiele, JavaScript- of formulierverzendproef. [Gerichte content- en hygrometercontrole](published-content-and-hygro.json).

## Gerichte tekstcorrecties

Een volledige verse Admin-read telt **122 Pages, waarvan 120 gepubliceerd**. Alle gepubliceerde bodies zijn op een beperkte set bekende coderingsfouten onderzocht. Dertien bestaande Pages zijn aangepast:

| Pagina | Reparatie |
| --- | --- |
| ceramic | hygiënische |
| greeploos | geïntegreerde, tweemaal |
| nisdeur | efficiënt |
| ommanteling | beïnvloeden |
| omstel | één, twee beschadigde é-tekens |
| sensowash | hygiëne, geïntegreerde, föhn en één; zeven beschadigde accenttekens |
| spoeltechniek | hygiëne en efficiënter; drie beschadigde accenttekens |
| vlakspoel | beïnvloedt |
| waterslot | waterbarrière |
| Buffers (toilet), Hart op hart (HOH), Hygro(meter), Pijp Kort (PK) | Alleen het onzichtbare U+FEFF-teken aan het begin van de body verwijderd |

Er zijn alleen bestaande onjuist gecodeerde lettercombinaties vervangen. Geen uitleg herschreven of technische productclaim toegevoegd. Elke wijziging had een verse body-/identiteitsguard vlak vóór de mutatie. Alleen Page.body is geschreven. Alle dertien uiteindelijke bodies zijn exact opnieuw gelezen; titel, handle, template, publicatiestatus en de gelezen metafields zijn gelijk gebleven. [Voor/na, vervangingen en terugzetwaarden](page-repairs.json).

## Controle

- Dertien publieke pagina’s vóór en na de wijziging: 200, één H1, bodytekst gelijk aan de bedoelde inhoud. Titel, meta description, canonical, H1, inhoudslinks en HTML-element-/attribuutstructuur zijn gelijk gebleven. Bekende accentfouten 19 → 0; voorlooptekens 4 → 0. [Voor](public-before.json), [na](public-after.json).
- De volledige herhaalde Admin-scan van de 120 gepubliceerde bodies vindt geen resterende match op de benoemde coderingspatronen. Dit is geen bewijs dat elke mogelijke typfout of inhoudelijke onjuistheid ontbreekt. [Scanbereik](scan-summary.json).
- Alle 109 links uit de actuele publieke begrippenlijst zijn gekoppeld aan de complete Admin-redirectinventaris en gepubliceerde Pages: 109 geldige doelen, nul loops. Dit is een route-/publicatiemapping; niet 109 afzonderlijke browser- of HTTP-doelproeven. [Linkcontrole](glossary-link-verification.json).
- De oude GLOSS-F01-bevinding is **al vóór deze taak opgelost**: /begrippenlijst/hygrometer en /pages/hygrometer komen bij /pages/hygro-meter uit. Bestaande redirects en uitleg zijn behouden; deze ronde bevat nul redirectwrites. Publieke ketencontrole 200, juiste doel en één H1.
- [Verificatiegrenzen](verification.json), [documentatiecontrole](documentation-checks.json). Geen nieuwe Windows-, fysieke telefoon-, browser-JavaScript-, mail-, herroepingsbevestiging-, checkout-, betaal-, purchase- of consenttest.

## Herstel en vervolgstap

Herstel uitsluitend de body van de betreffende Page met de opgeslagen vorige waarde, nadat is gecontroleerd dat de actuele body nog overeenkomt met de opgenomen nieuwe waarde. Geen latere eigenaarwijzigingen overschrijven. Titels, SEO, handles, publicatie en templates hoeven niet teruggezet te worden.

De gewone bezorgpagina en klantenservicelinks zijn nu live. Native policyopmaak/verzendpolicy blijven geblokkeerd door de eerder vastgestelde ontbrekende write_legal_policies-scope; geen alternatieve route gebruikt. Btw-identiteit, tariefdekking, echte order-/mail-/meetketen en mobiel blijven afzonderlijk open. **Volgende concrete handeling binnen dit dossier:** het algemene verzendprofiel gericht onderzoeken op productdekking en de locatie zonder tarieven, zonder verzendtarieven of leverbeloftes te verzinnen. Filter-/Cotto-/BRAUER-werkstromen behouden hun eigen actuele checkpoints en holds.

Codebranch blijft fix/product-cards-2026-10-14; deze ronde bevat alleen documentatie in Git, omdat de inhoud via Shopify Pages wordt beheerd. Main blijft documentatie-ingang. De twee eerdere dossiers bewaren hun eigen meetmomenten: [retourcopy](../contact-and-returns/README.md) en [bezorginformatie](../delivery-information/README.md).

Technische bron voor de beperkte contentmutatie: [Shopify pageUpdate](https://shopify.dev/docs/api/admin-graphql/2026-10/mutations/pageUpdate). De connector heeft de gebruikte GraphQL-operaties tegen zijn vastgepinde schema gevalideerd.
