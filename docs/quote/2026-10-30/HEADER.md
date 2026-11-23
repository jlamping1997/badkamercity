> **Vervolg:** eigenaar kiest de footer; de gedeelde offertelink is daar nu in concept geplaatst. Zie [FOOTER.md](FOOTER.md). Productprijs/homepage-teaser blijven voorstellen. Actuele themarollen staan in de centrale status.

> **Nieuw besluit, 30 oktober 2026:** eigenaar laat de offerteactie uit de mobiele header weg. De mobiele render en bijbehorende CSS zijn verwijderd; desktop blijft gelijk. Actueel reviewconcept **195915448586 — BadkamerCity - Offerteknop alleen desktop** (UNPUBLISHED). Eigenaar heeft eerder **195916628234** gepubliceerd; dat MAIN is in deze wijziging niet geschreven. Hieronder staat ook historisch bewijs van de vorige mobiele balk.

## Actuele controle en plaatsingsadvies

Twee gewijzigde themefiles ThemeCheck PASS; vijf bestaande zichtbaarheid-/routecases PASS; beide gepubliceerde conceptinhouden exact teruggelezen. Geen mobiele snippet-render of mobiele balk-CSS meer. Desktopvariant blijft onder990px display:none. Geen nieuwe mobiele browser-/telefoontest of uploadtest uitgevoerd. De oude header-mobile.jpg en bijbehorende metingen tonen het **vervallen** ontwerp.

Hergebruikt concept eerst naar actuele MAIN gebracht:1.349bestanden,1.347exacte checksums; twee JSON-templates semantisch gelijk met alleen Shopify-opmaaknormalisatie. Headergroepinstellingen opnieuw na de sectieschema’s geschreven en gecontroleerd. Daarna twee bedoelde bronwijzigingen. Alle1.349MAIN-checksums gelijk aan beginmeting. Geen publicatie.

Aanbevolen plekken (voorstel, niet als nieuwe publieke links geïmplementeerd):

| Plek | Presentatie | Doel |
| --- | --- | --- |
| Productpagina | Rustige link in de koopkolom bij de prijs: “Elders een offerte? Ontvang een betere prijs.” | Opvallen tijdens prijsafweging; winkelwagenknop behoudt voorrang. |
| Homepage | Bestaande offerte-teaser hergebruiken onder het assortiment, zonder extra banner in de mobiele header. | Complete badkamerkopers bereiken. |
| Footer / klantenservice | Vaste tekstlink “Laagsteprijsgarantie”. | Terugvindbaar op elke pagina. |

Dit is een UX-advies, geen bewezen conversiestijging. De standaard producttemplate gebruikt main-product en de bestaande bc-buybox__section--price; afwijkende producttemplates en de actuele Shopify-renderers eerst controleren bij uitvoering. Homepage-teaser bestaat al en is uitgeschakeld. Nieuwe koppelingen pas na werkende upload/ontvangsttest en publieke offertepagina activeren. Geen overlay of pop-up toevoegen.

Rollback van deze kleine correctie: sections/header.liquid en snippets/bc-header-quote.liquid uit checkpoint1e4c60e5e3572b66f71aaecc36e9fe26b47feaf2 alleen in het dan geldende ongepubliceerde concept herstellen. Geen MAIN-write.

---

## Historisch ontwerp vóór dit besluit

# Offerteknop in de header — 30 oktober 2026

Eigenaar vraagt een duidelijke offerte-uploadknop op de voormalige accountplek. In concept 195916628234 staat op desktop een lichtblauwe knop **Offerte uploaden**, met **Laagsteprijsgarantie** eronder en document-/uploadicoon. Onder 990 px staat dezelfde actie in een volle rij onder de zoekbalk, zodat logo, menu, verlanglijst en winkelwagen bereikbaar blijven. Geen extra JavaScript of externe assets.

Status: DESIGN_IMPLEMENTED / CUSTOMER_CTA_DISABLED / INTEGRATION_PENDING_ACCOUNT / NOT_PUBLISHED. MAIN195915448586 blijft ongewijzigd. Bestaande accountlinks waren al verwijderd; er is geen accountinstelling gewijzigd.

## Activering en route

Headerinstelling quote_cta_enabled=false; quote_cta_preview=true in concept. Preview werkt alleen als theme.role niet main is en opent /pages/contact?view=offerte-vergelijken. Bij publicatie verdwijnt die previewknop automatisch. De klantknop vergt expliciete activering én een beschikbare gepubliceerde pages['offerte-vergelijken'].url. Formulier eerst aansluiten en testen, offertepagina publiceren, daarna klantknop activeren en preview uitzetten. De header controleert de externe ontvangst niet zelf; activering blijft een handmatige releasehandeling.

## Bewijs en grenzen

- Vijf themefiles ThemeCheck PASS; exacte vijf bestandsinhouden in concept teruggelezen.
- Vijf lokale Liquid-gate-/routecases PASS; bestaande veertien offertecases PASS. Parser aangepast voor de door Shopify toegevoegde JSON-commentaarheader; bestaande locale-inhoud semantisch behouden.
- Desktop Shopify-preview: knop zichtbaar, gewone klik opent juiste offerte-H1.
- Geïsoleerde browserfixture van actuele gerenderde header/CSS: 320/390/1024 px zonder horizontale overloop; exact één zichtbare variant. Mobiele aanraakhoogte46px. Zie header-browser-checks.json en header-mobile.jpg.
- Fixture is geen fysieke telefoon, volledige mobiele pagina of menu-/zoekfunctie-interactietest. Die native review blijft open. Geen upload/ontvangst/notificatie uitgevoerd.
- Tijdelijke index.bc-homepage-review.liquid na controle exact teruggezet naar inert origineel. Geen klantgegevens opgeslagen.

## Bestanden en rollback

sections/header.liquid, sections/header-group.json, snippets/bc-header-quote.liquid en twee NL/EN-locales. Baselineheader en -group in header-baseline/. Zet beide quote_cta-instellingen uit om de knop te verbergen. Voor volledig terugzetten baselineheader en -group herstellen en alleen bc_quote.header_button uit locales verwijderen; snippet daarna ongebruikt. Verander geen andere themebestanden.

Eén volgende handeling blijft het formulieraccount beschikbaar maken en de echte upload-/ontvangstkoppeling testen. Zie README.md.
