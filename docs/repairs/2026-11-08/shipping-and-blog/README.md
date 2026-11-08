# SHIPPING-COVERAGE-01 en BLOG-ROUTE-01 — actieve verzending gecontroleerd, blog-404 hersteld

**8 november 2026 · EFFECTIVE_NL_SHIPPING_VERIFIED_WITH_LIMITS / BLOG_REDIRECT_APPLIED_VERIFIED.** De eerder gemelde locatie zonder tarieven is verklaard door de actieve Markets-configuratie. Die waarschuwing is niet als bewezen checkoutdefect blijven staan. Daarnaast is één echte 404 met een gerichte redirect hersteld.

## Effectieve bron: Markets

De winkel heeft marketDrivenShipping=true en shipsToCountries=[NL]. De actieve Nederlandse Market 94864998666 gebruikt Standaard, optie 1251671343370 en tariefgroep 489069838602. Zowel winkellocatie 106665476362 als leverancierslocatie 110481572106 staan in de optie én in de oorsprongsvoorwaarden van dezelfde tariefgroep. Er is geen collectiebeperking. Tarief €6,95, gratis vanaf €100,01. Alle opgevraagde Market-connections zijn compleet uitgelezen.

De complete read van de leverancierslocatie bevat 851 varianten: allemaal actief/gepubliceerd Verlavio, requireShipping, CONTINUE en gekoppeld aan het algemene profiel. Er zijn geen voorraadhoeveelheden of volledige productrecords openbaar gemaakt. [Locatiesamenvatting](supplier-location-summary.json).

Het oude DeliveryProfile toont nog coversAllItems=false, één oorsprong en één locatie zonder tarieven. Dat is hier geen bewijs dat de leverancierslocatie buiten de actieve NL-verzending valt. Het is een andere configuratielaag; de echte Market-voorwaarden omvatten beide oorsprongen. Ook is coversAllItems een overschrijvende profielinstelling, geen opdracht om het veld blind op true te zetten. [Legacy-signalen](legacy-profile-signals.json), [actieve Market vóór](market-before.json), [ongewijzigde readback na](market-after.json).

De eerdere FAB-04-reparatie van 5 november is teruggevonden en opnieuw bevestigd. Geen tweede locatie toegevoegd, coversAllItems niet omgezet, geen tarieven/voorwaarden/prijzen/voorraad gewijzigd. Deze verklaring sluit BC-AUD-013 als actueel diagnostisch probleem; zij bewijst geen levering voor elk product en elk adres.

## Acht daadwerkelijke NL-tariefproeven

| Proef | Winkelwagen | Aangeboden verzending |
| --- | ---: | ---: |
| Wiesbaden klein artikel | €29,00 | €6,95 |
| Verlavio onder drempel | €52,18 | €6,95 |
| Gemengd twee locaties onder drempel | €81,18 | €6,95 |
| Gemengd twee locaties boven drempel | €148,33 | €0,00 |
| Verlavio kraan boven drempel | €326,70 | €0,00 |
| Verlavio nulvoorraad doorbestellen | €1076,90 | €0,00 |
| Cotto een doos | €99,29 | €6,95 |
| Cotto twee dozen | €198,58 | €0,00 |

De gemengde cart van €81,18 krijgt één keer €6,95; die van €148,33 gratis. Het nulvoorraadartikel blijft volgens de eigenaarafspraak bestelbaar en krijgt een verzendoptie. De tegelproeven gebruiken één versus twee echte dozen; geen m²- of productprijs gewijzigd. [Volledige gerichte tariefproeven](cart-quotes.json).

Alleen een verse geïsoleerde cart gebruikt, één openbaar Nederlands zakelijk postcodegebied en de officiële Ajax Cart API. Na iedere proef alleen eigen artikelen verwijderd; de cart is uiteindelijk leeg teruggelezen. Geen checkout/order/betaling, klantgegevens of e-mail verstuurd. Geen bewijs van fysieke voorraad, werkelijke levering, pallettransport, alle postcodes, exacte €100/€100,01-grenscarts, kortingen, mobiel of GA4/consent. De vroegere twee offertes behouden hun eigen meetmoment; deze acht zijn afzonderlijke nieuwe proeven.

## Blogroute direct hersteld

/blogs/news gaf 404. Admin bevat alleen het bestaande blog Nieuws, handle nieuws; /blogs/nieuws geeft 200. Er was geen redirect voor de oude route. Eén nieuwe UrlRedirect 689424761098 is aangemaakt: **/blogs/news → /blogs/nieuws**. Geen blog, artikel, handle, thema of SEO-veld geschreven. [Admin-guard, receipt en readback](blog-redirect-admin.json).

De publieke nacontrole zonder preview bewijst **301 → 200**, juiste bestemming, H1 Nieuws en canonical /blogs/nieuws. Ook de querystringvariant geeft 301 naar dezelfde doelroute met behoud van de querystring. Een eerste nacontrole zag nog 404 tijdens propagatie; later is de kale bronroute opnieuw gecontroleerd. Geen dubbele create uitgevoerd. [HTTP-bewijs](blog-redirect-http.json).

Herstel: verwijder uitsluitend de in deze taak aangemaakte redirect nadat ID, pad en doel nog exact overeenkomen en tussentijdse eigenaarwijzigingen zijn uitgesloten. Bestaande redirects niet aanpassen. Voor verzending is geen rollback nodig, omdat geen verzendinstelling is geschreven.

## Documentatie, grenzen en volgende handeling

Takenlijst en actuele component-/handoffdocumenten wijzen nu Markets aan als eerste verzendbron. Native SHIPPING_POLICY en policyopmaak blijven afzonderlijk BLOCKED_SCOPE op de eerder vastgestelde write_legal_policies-toegang; de gewone bezorgpagina blijft live. Betaling, mail, herroepingsbevestiging, Google-aankoopmeting en fysieke mobiel blijven open. Geen nieuwe themapublicatie nodig.

De publieke /collections/tegeltoebehoren geeft nog 404. **Volgende concrete handeling:** de bestaande collectie-identiteit/publicatie en de werkelijke verwijzingen naar die route onderzoeken; pas na bevestigde product-/navigatiescope een correctie kiezen. Niet blind een lege categorie publiceren of een willekeurige collectie als redirectdoel gebruiken. Andere filter-/Cotto-/BRAUER-checkpoints en holds behouden.

[Verificatiegrenzen](verification.json), [finale Admin-readback](final-admin-readback.json), [documentatiecontrole](documentation-checks.json). Alleen documentatie op fix/product-cards-2026-10-14 en main; de actieve winkelcode blijft onder shopify/current ongewijzigd.

Technische bronnen: [DeliveryProfile](https://shopify.dev/docs/api/admin-graphql/2026-10/objects/DeliveryProfile), [LocationConnection en Market-opties](https://shopify.dev/docs/api/admin-graphql/2026-10/connections/LocationConnection), [Ajax Cart API](https://shopify.dev/docs/api/ajax/reference/cart), [urlRedirectCreate](https://shopify.dev/docs/api/admin-graphql/2026-10/mutations/urlRedirectCreate). De uitgevoerde GraphQL-operaties zijn door de connector gevalideerd tegen zijn vastgepinde schema.
