# Brauer — onderkasten en glas

12 november 2026. Voortgebouwd op a0905884370d085bc566d2fb6ae49783396850cc, codebranch fix/product-cards-2026-10-14.

## Inhoud

43 bestaande onderkastgroepen / 1.712 artikelen: breedte numeriek, Aantal laden met 2 laden / 4 laden, Afvoeruitsparingen met 1 uitsparing / 2 uitsparingen en hulp bij afstemming op de wastafel. De voorwaardelijke keuze en koopknopblokkade blijven behouden; geen kast-/wastafelcompatibiliteit afgeleid uit alleen breedte.

26 bestaande glasgroepen / 966 artikelen: Kleur beslag, nominale breedte/diepte en verwijzing naar exacte inbouwmaat. De 264 tweedelige Void-nisdeuren tonen totaalbreedte plus deurbreedte, bijvoorbeeld 110 cm · deur 60 cm, en uitleg over scharnieren aan muur/glaswand. Schuifdeuren en naar binnen draaiende deuren krijgen hun eigen brongebonden toelichting. Een te brede, niet gepubliceerde conceptregel zou ook Galactic-schuifdeuren een draaideur hebben genoemd; die regel is niet overgenomen.

Voor alle 2.678 artikelen actuele Shopify-variant-ID, SKU, product-ID, handle, ACTIVE/BRAUER en EUR-prijs uitgelezen. Laden/uitsparingen/kastbreedte en Void-deurbreedte tegen alle betrokken actuele titels gecontroleerd. Alleen presentatie en gedateerde prijscenten in thema-assets toegevoegd; productopties, identiteiten, routes en foto's behouden. Geen Admin-productmutaties. De bestaande generator roept de brongecontroleerde verfijning na herbouw aan; de variant-index wordt eenmaal opgebouwd. Volledige bronherbouw deze ronde niet herhaald.

Renderer sorteert kleur op vergelijkbare artikelprijs in geprijsde groepen; overige tekst alfabetisch en maten numeriek. Deze ronde maakt 69 groepen geprijsd; drie glasgroepen /336 artikelen overlapten met vorige ronde. Cumulatief 173 verbeterde/geprijsde groepen /6.402 artikelen. De overige 655 bestaande groepen zijn niet als volledig verbeterd/geprijsd aangemerkt. Prijsvolgorde blijft een snapshot en moet bij prijswijziging worden ververst.

## Bewijs

- 828 groepen, 12.292 exacte startstanden/bereikbare producten, 152.902 geldige keuzes en 1.172 voorwaardelijke tussenstanden PASS.
- 173 geprijsde groepen /6.402 artikelen /23.503 asstanden PASS. Overige tekst-/maatvolgorde getest in dezelfde renderer.
- Bestaande spiegelkast-koopknopblokkade, native select, zes zichtbare kleuren en exacte kandidaatfoto's PASS.
- Nieuwe bronvalidatie op alle 2.678 artikelen; 43 onderkast-/26 glasgroep-labels gecontroleerd. Galactic-schuifdeurregressie op 12 artikelen afzonderlijk PASS.
- 70 themabestanden Shopify Toolkit VALID. Aanvankelijk ontbrak een runtimepakket; opnieuw uitgevoerd met bestaande geïnstalleerde afhankelijkheden. Validator gebruikte gebundelde docs-fallback. JS-syntax, Python-compile en diffcheck PASS.
- Vooraf alle 70 conceptchecksums exact gelijk aan Git-checkpoint a090588. Afzonderlijke MAIN-checksums vastgelegd. Na upload alle 70 conceptbestanden exact teruggelezen; dezelfde 70 MAIN-bestanden ongewijzigd en rollen MAIN/UNPUBLISHED bevestigd.
- Deze ronde geen nieuwe echte browser-, mobiel-, winkelwagen- of checkoutproef; eerdere bewijsstukken gelden alleen voor hun eigen gedateerde scope.

## Herstel en volgende handeling

Uitsluitend de 70 conceptbestanden uit CABINETS_GLASS_MANIFEST.json terugzetten op a090588. Bestaande MAIN en het afzonderlijke specificatieconcept behouden. Geen publicatie in deze ronde.

Volgende handeling: bestaande hoge-/kolomkastgroepen beoordelen op nuttige maat-/draairichtingskeuzes en hun broncompatibiliteit; geen nieuwe productgroepen op basis van alleen titelgelijkenis.
