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
