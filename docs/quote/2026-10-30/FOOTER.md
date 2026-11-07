> **Vervolg:** Jotform ingericht en in concept aangesloten; klantactivatie blijftuit. Account bestaat inmiddels. Zie [actuele integratiestatus](INTEGRATION.md).

# Offertelink in de footer — 30 oktober 2026

Eigenaar kiest de footer en vraagt de offertestatus in Git op te slaan. In beide footers onder Klantenservice staat **Laagsteprijsgarantie – Offerte uploaden**. Gewone footer: sections/footer.liquid; compacte homepage: snippets/bc-home-footer.liquid. Beide gebruiken snippets/bc-footer-quote.liquid. Geen nieuwe banner, pop-up of mobiele headerbalk.

## Bron en uitrol

Eigenaar heeft het vorige reviewconcept195915448586 gepubliceerd. Dat is nu MAIN,1.349files. Bestaand concept195916628234 eerst exact hiermee gesynchroniseerd (1.349/1.349checksums); daarna vier footerbestanden veranderd/toegevoegd. Resultaat1.350files, UNPUBLISHED. AlleMAIN-checksums ongewijzigd. Pagina166573539594 nog isPublished=false. Geen app/account/publicatie of echte upload uitgevoerd.

## Activering

sections/footer-group.json: quote_link_enabled=false en quote_link_preview=true. De preview werkt alleen buiten MAIN en opent /pages/contact?view=offerte-vergelijken. Bij publicatie verdwijnt deze conceptlink automatisch. Voor klanten is een expliciet geactiveerde footerinstelling én een beschikbare gepubliceerde offertepagina vereist. Eerst formulieraccount, afgeschermde toegang, ontvanger en echte upload-/ontvangsttest; daarna offertepagina/publicatie door eigenaar en klantlink activeren. Geen automatische controle van providerontvangst claimen. Desktopheader heeft zijn eigen eerder vastgelegde activatie.

## Controle

- ThemeCheck vier files PASS, zie footer-themecheck.json.
- Vijf LiquidJS-cases PASS: MAIN-preview verborgen, conceptpreview juiste route, ongepubliceerde bestemming verborgen, gepubliceerde route bij expliciete activering, uitgeschakelde link verborgen. Zie test-footer.cjs.
- Drie Liquid-inhouden exact teruggelezen; footer-group.json semantisch gelijk (Shopify normaliseert JSON). Geen locale-inhoud gewijzigd; bestaande NL/EN-vertalingen hergebruikt.
- Desktop Shopify-preview: gewone footerklik opent offerte-H1; compacte homepage-uitklapper opent en toont dezelfde link/route. Screenshots footer-service.jpg en footer-home.jpg. Browserroute contact?view=offerte-vergelijken bewijst geen SEO van de ongepubliceerde echte pagina.
- Geen nieuwe mobiele browser-/telefoonmeting, upload, notificatie, privédownload of bewaartermijntest. Eerdere telefoonscreenshots zijn geen bewijs voor deze footeruitbreiding.

## Terugzetten

Baseline in footer-baseline/. Herstel sections/footer.liquid, sections/footer-group.json en snippets/bc-home-footer.liquid uitsluitend in het actuele ongepubliceerde concept. De nieuwe snippet wordt dan ongebruikt. Alleen de link verbergen: beide quote_link-instellingen uit. Geen MAIN-write.

Volgende stap blijft de formulieraccount beschikbaar maken; Jotform is nog niet aangemaakt. Geen ontvangstdienst of klantupload live verklaren.
