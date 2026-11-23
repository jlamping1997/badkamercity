# DELIVERY-INFO-01 — bezorginformatie live en gedeelde verwijzingen voorbereid

> **Eigenaarpublicatie bevestigd — CONTENT-ENCODING-02:** Klantenservice 8 nov is nu MAIN **196368531722**. Zes featurefiles exact; nieuwe footer-/homepagebezorglinks publiek gecontroleerd, veertien routes dezelfde footer. [Laatste nacontrole en vervolg](../glossary-encoding/README.md). Onderstaande preview- en herstelmetingen bewaren hun oorspronkelijke moment; dat publicatieverzoek is afgehandeld.

**8 november 2026 · PAGES_APPLIED_VERIFIED / THEME_PREVIEW_VERIFIED_NOT_PUBLISHED.** Een eigen informatiepagina maakt de bestaande Nederlandse verzendkosten en afhaalafspraak vindbaar. Er zijn geen tarieven, leverbeloftes of voorraadinstellingen gewijzigd.

## Live aangepast

- [Bezorgen en afhalen](https://badkamercity.nl/pages/bezorgen-en-afhalen), Page 166963937546: €6,95 standaardverzending tot en met €100, gratis vanaf €100,01; afhalen pas na bevestiging en op afspraak; contactgegevens en retourlinks. Eigen SEO-titel en beschrijving. Eén H1; geen vaste levertijd, vervoerder of heenzendtarief voor pallets verzonnen.
- [Contact](https://badkamercity.nl/pages/contact), bestaande Page 160794411274: bestelnummer expliciet als je dat hebt en een verwijzing naar de nieuwe bezorgpagina. Identiteit, template contact, SEO en native formulier behouden.
- Alleen de bevestigde afhaal-/retourlocatie gebruikt: Badkamercity – bij Harry Suiker, Zichtenburglaan 150, 2544 EB Den Haag, Nederland. Afhalen en afgeven op afspraak. Geen bewijs van juridische vestiging afgeleid uit die locatie.

Shopify heeft bij het aanmaken alleen de HTML-tabel opnieuw ingesprongen. DOM-vergelijking bevestigt dezelfde inhoud, cellen en links. De twee Pages en de SEO-velden zijn na de mutaties opnieuw uit Admin én publieke HTML gelezen. [Page-readback](pages-readback.json), [publieke HTML-controle](live-pages.json).

## Verzendkosten daadwerkelijk gecontroleerd

De read-only Admin-controle vindt in het algemene profiel de twee actieve NL-tarieven: €6,95 bij 0–100 euro en €0 vanaf €100,01. Winkelvaluta EUR, prijzen inclusief belasting, shipsToCountries NL. [Begrensde profielreadback](shipping-nl-readback.json).

Daarna zijn twee tarieven via de officiële Ajax Cart API opgevraagd met een eigen geïsoleerde cookiejar en één openbaar Nederlands zakelijk postcodegebied:

| Testwinkelwagen | Aangeboden standaardverzending |
| --- | --- |
| €96,15 | €6,95 |
| €109,00 | €0,00 |

Alle eigen proefartikelen zijn verwijderd; de eigen winkelwagen is opnieuw leeg teruggelezen. Geen checkout, klantaccount, order, betaling of formulier verstuurd. Geen klantgegevens of carttokens in dit dossier. [Tariefproeven](actual-rate-verification.json). De proeven bewijzen deze twee offertes; niet iedere SKU, locatie, adres, kortingscombinatie of de exacte grenswaarden.

**Open:** profile coversAllItems=false en locationsWithoutRatesCount=1. Product-/locatiedekking vraagt een afzonderlijke controle. Het native SHIPPING_POLICY ontbreekt nog; deze gewone Page vult geen policy in de checkout. De eerder vastgestelde ontbrekende write_legal_policies-scope is niet omzeild. De opmaak van voorwaarden/kennisgeving en het native contactbeleid blijven open.

## Bestaand concept uitgebreid

**UNPUBLISHED 196368531722 — BadkamerCity - Klantenservice 8 nov.** Dit is hetzelfde eerdere retourconcept, hernoemd zodat één reviewversie alle wijzigingen bevat. [Voorbeeld](https://badkamercity.nl/?preview_theme_id=196368531722).

| Bestand | Nieuwe wijziging |
| --- | --- |
| sections/footer-group.json | Alleen service_3: Bezorgen en afhalen wijst naar /pages/bezorgen-en-afhalen in plaats van de homepage-ankerlink |
| sections/bc-homepage.liquid | HomeDelivery linkt naar de bezorgpagina als native shipping_policy ontbreekt; bestaand native beleid krijgt voorrang en Contact blijft fallback als de Page niet beschikbaar is |

Beide bestanden zijn vóór wijzigen exact met verse Shopify-bron vergeleken, gevalideerd en daarna bytegelijk teruggelezen. De bestaande vier retourbestanden zijn checksumgelijk behouden: bc-returns, nl, en.default en index. Zie het [eerdere retourdossier](../contact-and-returns/README.md) voor hun inhoud, 30 + 14 dagen, optionele velden, omruilkeuze en €75 als raming voor standaard NL-retourpallets.

## Bewijs en grenzen

- Twee Liquid-checks op revisie 1 PASS. [Validatie](liquid-validation.json).
- Vier HTTP-previewroutes met geïsoleerde previewcookies tonen werkelijk concept-ID 196368531722: homepage, Contact, Retour aanmelden en de bezorgpagina. Alle hebben één H1 en dezelfde footer met de nieuwe bezorglink. De homepage verwijst ook naar de bezorgpagina; eerdere retourteksten, beleidslink en native formulier blijven aanwezig. [Previewcontrole](preview-verification.json).
- Volledig finale manifest: 1.387 bestanden per thema; 1.381 gelijk, precies zes bedoelde verschillen, nul ontbrekend/extra. De oorspronkelijke vier retourfiles zijn ongewijzigd gebleven. MAIN 196354474250 bleef checksumgelijk. [Volledig checksumregister](theme-parity.json), [patchregister](patch-summary.json), [verificatiegrenzen](verification.json).
- Geen nieuwe visuele browser-, fysieke telefoon-, JavaScript-, mail-, herroepingsbevestiging-, purchase- of consentproef. Een aanwezig formulier bewijst geen mailbezorging. Geen thema gepubliceerd.
- [Onafhankelijke review](review.md) vindt geen blocker in deze gerichte wijziging. Bij een latere native shippingpolicy de bezorg-Page en footerbestemming bewust gelijk houden; de homepage geeft native beleid voorrang. [Documentatiecontrole](documentation-checks.json).

## Volgende handeling en herstel

De eigenaar beoordeelt **Klantenservice 8 nov** op laptop en telefoon en publiceert dit bestaande concept via Shopify. De connector ondersteunt geen themapublicatie; dit is geen nieuw inhoudelijk akkoordverzoek. Vóór publicatie verse MAIN en eventuele tussentijdse wijzigingen controleren; daarna de openbare homepage/footer/retourpagina opnieuw teruglezen. Native policies en volledige verzend-/betaal-/mail-/meetketen blijven apart open. Andere filter-/Cotto-/BRAUER-werkstromen behouden hun eigen status.

Broncode op fix/product-cards-2026-10-14 onder shopify/current; main bevat alleen documentatie. [Gerichte herstelwaarden](rollback-pages.json): draai alleen deze twee nieuwe themefiles terug na controle op latere edits en behoud de eerdere vier retourfiles. Contactbody kan gericht naar de opgeslagen vorige waarde. De nieuwe Page alleen verbergen nadat actuele verwijzingen zijn gecontroleerd; de twee nieuwe SEO-metafields horen bij die Page. Nooit de hele Git-themakopie blind deployen.

Technische bron: [Shopify Ajax Cart API](https://shopify.dev/docs/api/ajax/reference/cart). De commerciële tarieven in dit dossier komen uit de eigen actuele winkel en tariefproeven.
