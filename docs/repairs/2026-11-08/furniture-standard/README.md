# Badkamermeubels gelijkgetrokken en Antikalk-link hersteld

8 november 2026 · FURNITURE-STANDARD-01 / PAGE-LINK-01 · APPLIED_VERIFIED

Eigenaar vroeg de meubelcategorie hetzelfde uiterlijk te geven als de andere hoofdcategorieën en een kleine Git-taak af te ronden. Bestaande standaardtemplate hergebruikt; geen nieuwe vormgeving, templatecode of themapublicatie nodig.

## Live wijzigingen

- Collectie569428148490: `bc-meubelhub` → `category-landing`; precies BCM_MOBILE_NAV_V2, BCM_DESKTOP_CTA_V1 en BCM_HERO_COMPACT_V1 uit descriptionHtml verwijderd. 7523→3502tekens. Alle overige velden exact gelijk, inclusief451producten, SEO, handle en publicaties. Overige inhoud/links en SPLIT behouden.
- Page161999585546 Antikalk: `/collections/douchekoppen` (404, geen bestaande collectie) → `/collections/hoofddouches` (200,350producten). CTAtekst aangepast naar Bekijk hoofddouches. Alle andere bodytekst, templatebegrip, publicatie en SEOmetafields exact gelijk.
- MAIN bij uitvoering196368531722, Klantenservice8nov; geen themefiles geschreven. Oude meubelhubbestanden blijven beschikbaar en worden niet verwijderd.

## Bewijs en grenzen

[Collectie vooraf](before.json), [collectie mutation-readback](after.json), [Page vooraf](antikalkBefore.json), [Page mutation-readback](antikalkAfter.json). Exacte metadata/veldguards PASS. [Openbare nacontrole](public-after.json): meubelpagina standaardrenderer zoals Wastafels/Baden, geen oude hub/styleblokken, één H1, oorspronkelijke SEO/canonical, Antikalk juiste nieuweCTA. [Alle zeven kaartbestemmingen HTTP200](category-links.json).

Desktop Chrome1348×926: live kale URL na MAIN-previewbinding geeft standaardintro/categorieknoppen/advies; screenshot visueel beoordeeld. De previewbalk op de screenshot is Shopify-reviewcontext. Publieke HTTPcontrole onafhankelijk zonder previewparameters bevestigt dezelfde standaardrenderer. Mobiele visuele review en koopflows NOT_TESTED; geen brede sitevrijgave. Een extra onafhankelijke Admin-query na de succesvolle mutations vroeg opnieuw authenticatie; geen nieuwe mutatie of alternatieve Admin-route geprobeerd. Mutation-readbacks plus openbare nacontrole bewijzen de uitgevoerde wijzigingen.

Voor de kleine linktaak:122Pages/120gepubliceerd en één gepubliceerd blogartikel vooraf gelezen; één defecte collectieCTA gevonden. Geen algemene collectie-/menuherstructurering uitgevoerd.

## Terugzetten

Alleen bij expliciet verzoek: collectionUpdate met id uit before.json en uitsluitend oude templateSuffix/descriptionHtml terugzetten. Voor Page uitsluitend oude body uit antikalkBefore.json. Eerst verse data vergelijken om latere wijzigingen te behouden. Geen volledige objecten, SEO/publicaties of producten blind terugschrijven. Historische CSS-waarschuwing in rootAGENTS en componentdocumentatie geactualiseerd zodat een volgende sessie de oude hub niet automatisch herstelt.

Volgende handeling: eigenaar beoordeelt de standaard meubelpagina op telefoon. Native policies/scope, btw-identiteit, betaling/mail/meting en andere lopende trajecten blijven apart open. Geen Windows-werkruimtecontrole geclaimd.
