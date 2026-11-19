# Hotbath inbouwdeel meebestellen — technische beoordeling

Status: alleen gelezen en ontwerp beoordeeld. Geen implementatie, Shopify-write, Git-write of winkelmandactie uitgevoerd. De productform-, buy-buttons-, accessoires- en setbestanden zijn nu ook tegen de verse Admin-bron gelezen. De eigenaar heeft het Hotbath-thema195649929482 gepubliceerd: root bevestigt MAIN en alle532 bestanden identiek aan de goedgekeurde uitrol. Drawer/notification en de standaard producttemplate zijn alleen uit GitHub main gelezen. De lokale productsectie is de gecontroleerde Hotbath-uitrol van vandaag.

## Dit bestaat al

De productsectie laadt `product-form.js` en `bc-product-accessories.js` (regels933–935) en toont een apart accessoiresblok (regel2059). De accessoirescode heeft al het juiste uitgangspunt: **gecontroleerde relaties op exacte SKU/handle**, variantprijs en beschikbaarheid uit Shopify, geen naamvergelijking. Ze controleert vendor Hotbath, exacte SKU en dat het accessoire niet het hoofdproduct zelf is.

Het huidige echte gebruik is echter beperkt: vijftien ACE-artikelen koppelen optioneel naar reiniger HB001. Het bestaande accessoiresblok heeft een eigen knop die **alleen accessoires** toevoegt. Die simpelweg vullen met HBCB105 levert dus niet de door de gebruiker gevraagde gecombineerde koopknop op.

Het setonderdelenblok onderscheidt al `included`, `required` en `optional`. Het bevat enkele exacte inbegrepen Hotbath-inbouwdelen bij sets, maar geen CB105/HBCB105-relatie. Deze statusindeling kan behouden blijven; de fabrikantbron moet de nieuwe compatibiliteit bewijzen.

De actuele set- en accessoiressnippets hebben Sunshower-doorverwijzingen die in de oudere Git-rootversie ontbreken. De actuele koopknop gebruikt bovendien de bestaande wishlist-snippet. Die wijzigingen moeten bij implementatie behouden blijven. Het Hotbath-setblok leest nu de gecureerde set-data-snippet; een elders bestaand bc_data.set_components-veld wordt hier niet automatisch gebruikt. Een status EXACT_TARGET_UNVERIFIED_COMPATIBILITY bewijst alleen een gevonden artikel, niet de technische passendheid.

Root bevestigde voor de proef HBCB105: product10534319489290, variant53187364356362, actuele prijs€174 en beschikbaar voor verkoop. De twintig CB105EXT18/25-afbouwartikelen hebben met_inbouwdeel=false. Dat ondersteunt de koopafbakening; boekbewijs blijft nodig voor de compatibiliteit.

## Eenvoudigste uitbreiding

1. Eén gecontroleerde relatietabel: exact afbouwmodel/concrete SKU → inbouw-SKU, hoeveelheid per afbouwartikel, status en boekbewijs. Resolutie naar actuele Shopify-product-/variant-ID's. Een EXT-detectie maakt een kandidaat, nooit een automatische HB-code.
2. Toon in de gewone koopsectie: **Benodigd inbouwdeel meebestellen?** met **Ja, HBCB105 toevoegen (+ actuele prijs)** en **Nee, ik heb dit inbouwdeel al**. Advies: expliciete keuze, geen vooraf aangevinkte betaalde toevoeging.
3. Breid de bestaande productform-handler beperkt en opt-in uit: bij Ja één `items[]`-aanvraag met gekozen afbouwvariant én gekoppeld inbouwvariant. Bij Nee de gewone kooproute. De Shopify-prijs blijft per echt artikel gelden.
4. Hoofdaantal2 betekent bij een1:1-relatie twee afbouwdelen plus twee inbouwdelen. Eén al aanwezige HBCB105 in de winkelmand is geen reden de gevraagde extra twee over te slaan.
5. Laat de benodigde-inbouwvermelding en koopkeuze uit dezelfde gecontroleerde bron komen. Voorkom twee aparte toevoegknoppen voor hetzelfde onderdeel.
6. Bij IBS70/andere bewezen complete sets: status inbegrepen; geen extra inbouwdeel toevoegen.

## Menuwissels en prijs

De bestaande V2-keuzemenu's navigeren naar een andere productpagina. De scrollpositie wordt onthouden, maar een nieuwe Ja/Nee-keuze nog niet. Bewaar die keuze alleen binnen dezelfde gecontroleerde relatie, keuzegroep en inbouwvariant. Controleer op de bestemmingspagina opnieuw de juiste koppeling en beschikbaarheid. De huidige `bcNavigating`- en `aria-busy`-blokkeringen behouden.

De catalogus bewijst wat bij elkaar hoort. De actuele Shopify-variantprijs bepaalt de toeslag en het totaal. Bij ontbrekend of niet bestelbaar inbouwdeel wordt Ja niet aangeboden als bestelbare optie. Nooit ongemerkt Ja veranderen in Nee.

## Winkelmand en uitzonderingen

`product-form.js:46–57` verstuurt nu één variant via FormData. De bestaande accessoires-JS gebruikt al een meervoudige `items[]`-aanvraag en toont bij onzekere resultaten de instructie de winkelmand te controleren; dat gedrag is bruikbaar.

Eén aanvraag betekent niet gegarandeerd alles-of-niets. De officiële Ajax-documentatie beschrijft dat een voorraadoverschrijding de maximaal beschikbare hoeveelheid kan toevoegen en toch422 geven. Ook een fout in sectieparameters kan400 geven nadat de winkelmand is gewijzigd. Daarom geen automatische retry; duidelijk maken dat de klant de mand moet controleren. Geen bestaande winkelmandregels automatisch terugdraaien.

De drawer kan servergerenderde secties gebruiken. De huidige `cart-notification.js:38–57` verwacht één `response.key`; een meervoudige respons vereist aanpassing of een expliciete winkelmandpagina-terugval. Null-secties mogen niet tot opnieuw toevoegen leiden.

De standaard producttemplate in Git heeft dynamic checkout uitgeschakeld; de actuele Admin-template is in deze deelreview niet afzonderlijk gelezen. De buy-buttons-snippet kan die wel inschakelen. Houd versnelde checkout voor deze proef uit zolang de geselecteerde toevoeging daarin niet afzonderlijk is gecontroleerd. Controleer ook quick-add-ingangen zodat een los afbouwartikel niet als complete combinatie wordt voorgesteld.

Shopify heeft inmiddels native geneste winkelmandregels via `parent_id`: het onderdeel kan bij het afbouwdeel horen en wordt verwijderd als die ouderregel wordt verwijderd. Dat is een mogelijke vervolgstap als de huidige winkelmandweergave het ondersteunt; automatische aantalsynchronisatie is hier niet aangetoond. Voor het gevraagde Ja/Nee-gedrag zijn twee gewone echte artikelregels voldoende.

## Gerichte acceptatie

Ja/Nee, aantal2, kleur/18→25-wissel, IBS70-uitsluiting, reeds aanwezige HBCB105, onbeschikbaar onderdeel, foutieve SKU, dubbel klikken, menuwissel tijdens toevoegen,422/netwerkfout, drawer/notification, accelerated checkout/no-JS en echte mobiele weergave. Bij winkelmandtests uitsluitend eigen testregels opruimen.

Bronnen: [Shopify Ajax Cart API](https://shopify.dev/docs/api/ajax/reference/cart), [nested cart lines](https://shopify.dev/docs/apps/build/product-merchandising/nested-cart-lines) en [parent_id-aanmaak](https://shopify.dev/docs/apps/build/product-merchandising/nested-cart-lines/create-nested-cart-lines). Het in de bestaande code genoemde `docs/PDP_ACCESSORIES.md` gaf404; er is niets uit dat ontbrekende document afgeleid.

