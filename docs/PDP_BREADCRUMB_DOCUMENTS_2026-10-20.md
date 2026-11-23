# Productpagina — breadcrumbs en bijlagen, 20 oktober 2026

De eigenaar vraagt de categorie-breadcrumbs bovenaan de productpagina te plaatsen en beschikbare lijntekeningen/PDF’s zoals bij Sunshower te tonen. Dit vervangt voor deze pilot de eerdere keuze om technische documenten te verbergen.

Uitgevoerd in bestaand ongepubliceerd concept **195488317706 — BadkamerCity - Productpagina smal desktop**. MAIN **195486253322** blijft behouden. Geen nieuw thema, publicatie of root-theme-push. Scope: Wiesbaden **24.3710**, dezelfde vendor/SKU/enkele-defaultvariant-guard als de productpilot; geen automatische uitrol naar het assortiment.

## Gedrag

- Een semantisch kruimelpad Home → Kranen → Wastafelkranen → Opbouw wastafelkranen → huidige producttitel staat vóór de productheader. De categorieparagraaf is uit de specificaties verwijderd.
- Bijlagen gebruikt dezelfde rij-indeling, documenticonen, afwisselende achtergrond en pijl als de actuele Sunshower-producttemplate; geen Sunshower-bestand aangepast. Het JPG-icoon wordt als JPG gemarkeerd en de handleiding als PDF.
- Een Bijlagen-link in de productinformatienavigatie verwijst naar het bijlagenblok onder de specificaties. Lege/ongeldige documentdata of andere producten renderen geen nieuw blok of navigatielink.
- De eerdere 750–989px-layoutcorrectie is byte-inhoudelijk behouden in dezelfde stylesheet. De bestaande galerij met productfoto en maattekening is behouden.

## Data en bewijs

De bestaande definitie `custom.technische_documenten` (`list.url`, definitie409276645642) bestond al. Alleen voor product10657256210698 is de bestaande lijntekening aangevuld met de officiële, in de bronrun gevonden handleiding. Beide URL’s daadwerkelijk via HTTP opgehaald: JPG200/image/jpeg/33573bytes en PDF200/application/pdf/296291bytes met geldige magic bytes. Er is geen PDF-conversie of nieuw document verzonnen. Update via `metafieldsSet` met de verse `compareDigest`, nul userErrors en exacte onafhankelijke read-after-write. Voor/na-waarde, definitie en digest staan in het verificatiebestand. Geen prijzen, voorraad, titels, collecties of filters gewijzigd.

Concept vóór509bestanden, na511: vijf bestaande gewijzigd, twee nieuwe snippets, overige504exact gelijk. MAIN508/508exact gelijk. Alle zeven gewijzigde inhouden via MD5teruggelezen. De eerder geneutraliseerde QA-template is ongewijzigd; deze ronde heeft geen testtemplate naar Shopify geschreven.

Theme Check R2: alle zeven bestanden zonder errors; main-product heeft drie niet-blokkerende bevindingen (complexiteit208, ongebruikte seo_media, continue-object). Eerste run miste twee lokale contextsnippets; verse Shopify-exemplaren toegevoegd aan de validatiemap en daarna R2geslaagd. Negen conditionele Liquid-renders slagen (beide/elk bestand, leeg, deduplicatie, verkeerdeSKU, verkeerdmerk, varianten, onveiligprotocol); breadcrumb heeft vierlinks en aria-current. LocaleJSON geldig.

Normale Shopify-preview daadwerkelijk in Cloud Browser gelezen bij1363×936: één breadcrumb vóórH1, geen oude breadcrumb bijspecificaties,33specificatieregels, beidebijlagen engeen horizontaleoverloop/Liquidfout. Bijlagen-link aangeklikt: juisteanchor, blok zichtbaar opy196,5. Twee eigen screenshots opgeslagen. De URLnormaliseert naar het gewone productadres; previewcookie en zichtbare previewbalk identificeren concept195488317706. Een gewone URL bewijst hier dus geen MAIN-weergave.

**Niet getest:** nieuwe mobiele/smalle visueleweergave, fysieke telefoon, cart-/wishlistacties of checkout. De extra geïsoleerde responsiveproef via dataURL werd door het browserprotocolbeleid geblokkeerd (alleenhttp/https); geen omweg geprobeerd en geen mobielePASSclaim. Eerdere viewportmetingen voor de behouden narrow-desktopcorrectie blijven afzonderlijk gedateerd in PDP_RESPONSIVE_2026-10-20.md.

## Herstel en volgende handeling

Niet publiceren houdt de livevormgeving behouden. Voor herstel in het concept: zet alleen de vijf gewijzigde bestaande bestanden terug met de inverse van de gekoppelde patch; de twee nieuwe, dan ongebruikte snippets hoeven niet verwijderd te worden. Herstel desgewenst alleen de documentmetafield naar de oorspronkelijke lijst met éénURL, met een nieuwe compareDigest en alleen als de huidige waarde nog exact de gedocumenteerde na-waarde is.

Volgende handeling: eigenaar opent in Shopify **Onlinewinkel → Thema’s → BadkamerCity - Productpagina smal desktop → Voorbeeld**, beoordeelt24.3710 en publiceert dit concept indien akkoord. De Shopify-connector kan niet publiceren of MAIN-bestanden schrijven; geen publicatiemutatie of alternatieve route geprobeerd. Vóór publicatie actuele MAIN vergelijken; daarna liveproduct opnieuw controleren. Uitvoering via ChatGPT/Shopify/GitHub-connectors; geen Windows-, PowerShell-wrapper- of SSHcontrole geclaimd.

Bestanden: [patch](patches/BC-pdp-breadcrumb-documents-20261020.patch), [verificatie/backup](pdp-breadcrumb-documents-2026-10-20-verification.json), [breadcrumbs](design/pdp-breadcrumb-top-20261020.jpg), [bijlagen](design/pdp-bijlagen-20261020.jpg).
