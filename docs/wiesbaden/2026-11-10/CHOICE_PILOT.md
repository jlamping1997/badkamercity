# Wiesbaden keuzemenu's — overdracht 10 november 2026

**Status: keuzemenu's voor 31 artikelen aangebracht in het bestaande, ongepubliceerde concept en gecontroleerd. Beoordeling door eigenaar en echte winkelwagenproef staan nog open. Niet gepubliceerd.**

Het concept is eerst gelijkgetrokken met het actuele live thema. Vervolgens zijn vijf kleine databronnen en twaalf regels in de bestaande groepsrouter toegevoegd. De bestaande productkeuzetechniek, JavaScript, productpagina en grote gedeelde databron zijn behouden. Er is geen extra thema gemaakt.

| Familie | Artikelen | Keuzes | Conceptvoorbeeld |
|---|---:|---|---|
| Maki vouwbare nisdeur, helder glas/chroom | 6 | Breedte 80/90/100 cm; scharnierzijde Links/Rechts | [Maki bekijken](https://badkamercity.nl/products/wiesbaden-maki-nisdeur-vouwbaar-links-800-x-2000-x-8-mm-nano-helder-glas-chroom-20-3720?preview_theme_id=196416504074&_fd=0&_sc=1&_ab=0) |
| Derde generatie douchegoot met flens en rooster | 8 | Lengte 50 t/m 120 cm, stappen van 10 cm | [Met rooster bekijken](https://badkamercity.nl/products/wiesbaden-3e-generatie-douchegoot-met-flens-en-rooster-50-x-7-cm-rvs-33-4168?preview_theme_id=196416504074&_fd=0&_sc=1&_ab=0) |
| Derde generatie douchegoot met flens, zonder rooster | 8 | Lengte 50 t/m 120 cm, stappen van 10 cm | [Zonder rooster bekijken](https://badkamercity.nl/products/wiesbaden-3e-generatie-douchegoot-met-flens-zonder-rooster-50-x-7-cm-rvs-33-4140?preview_theme_id=196416504074&_fd=0&_sc=1&_ab=0) |
| Uovo LED-spiegel, dimbaar en verwarmd | 7 | Formaat 70/80/90/100/120/140/150 cm | [Uovo bekijken](https://badkamercity.nl/products/wiesbaden-uovo-spiegel-ovaal-met-led-dimbaar-en-spiegelverwarming-70-cm-38-4163?preview_theme_id=196416504074&_fd=0&_sc=1&_ab=0) |
| 304 enkele handdoekhouder | 2 | Lengte 25/60 cm | [Handdoekhouder bekijken](https://badkamercity.nl/products/wiesbaden-304-handdoekhouder-enkel-25-cm-rvs-24-3822?preview_theme_id=196416504074&_fd=0&_sc=1&_ab=0) |

De twee douchegootfamilies houden hun verschillende leveringsinhoud. Uovo 60 cm zonder verwarming is geen keuze binnen de verwarmde familie. Vaste eigenschappen zijn geen extra menu. Bij Maki blijven Links/Rechts de fabrikantbenamingen; een uitleg over kijkrichting of stelbereik is nog niet bevestigd.

## Wat is aangetoond

- Precies 31 nieuwe `custom.switch_group`-koppelingen zijn met aanmaakbeveiliging toegevoegd en teruggelezen. Andere uitgelezen productgegevens, waaronder prijs, foto, kleur, artikelidentiteit en publicatie, vertonen geen wijziging. Deze productvelden gelden voor alle thema's; de nieuwe menudatabronnen staan in het concept.
- Alle 31 productpagina's geven in het concept de juiste titel, artikelcode, formulierartikel, eerste afbeeldingsbestand en bijbehorende begrensde databron. Alle vijf daadwerkelijk uitgegeven data-assets geven HTTP 200 en de verwachte inhoudshash. Dit is serverbewijs, geen daadwerkelijke winkelwagentoevoeging.
- Alle zes Maki-artikelen zijn via echte keuzeknoppen doorlopen met passende titel, foto en prijs. Herladen en terugnavigeren zijn gecontroleerd. In elk van de vier andere families is een echte wissel naar de andere uiteindelijke lengte of het formaat gecontroleerd. Uovo 60 cm was niet selecteerbaar.
- De volledige themavergelijking van 10 november, 02:21 UTC, telt 1.401 live bestanden en 1.406 conceptbestanden: 1.400 gedeelde bestanden zijn gelijk. Het verschil bestaat uitsluitend uit vijf nieuwe assets en de gewijzigde router. Het live thema vertoont geen wijziging tegenover de uitgangssituatie.

De oorspronkelijke router blijft bytegelijk wanneer alleen het nieuwe twaalfregelige blok wordt verwijderd. De uiteindelijke router heeft MD5 `f4a640149ba4fe1198ad5d0b2162081d`. De nieuwe routes staan vóór de oude revisievoorwaarde, omdat het concept een andere assetrevisie heeft dan het live thema.

## Wat nog openstaat

De eigenaar beoordeelt de vijf voorbeeldfamilies. Daarna moet een echte winkelwagenproef aantonen dat gekozen uitvoering, SKU, prijs en toegevoegd artikel overeenkomen. Er zijn nul winkelwagenmutaties uitgevoerd. Een geslaagde native mobiele proef ontbreekt eveneens. Lokale syntaxiscontrole slaagt, maar er is geen officiële Shopify-validator-PASS geclaimd. Voorraad, levertijd en ontbrekende technische gegevens zijn niet aangevuld.

UniMatch W02, twintig plafondarmen met kleur en lengte, is **alleen voorbereid en niet toegepast**. Het voorstel bevat gerichte generieke ondersteuning voor exacte kandidaatfoto's, zes zichtbare kleuren en prijsvolgorde van passende artikelen. Vóór integratie moet de patch worden aangepast aan de huidige router, met behoud van de vijf inmiddels toegevoegde routes. Ook de oude W02-revisievoorwaarde mag niet blind worden hergebruikt. Een oude volledige kopie terugzetten zou deze proefgroepen verliezen. De ontbrekende combinatie 30 cm/geborsteld staal PVD en de onvolledige technische bronvelden van twee staalartikelen blijven open. Nieuw fabrikantbewijs komt uitsluitend van wiesbaden.nl en officiële Korver-bestanden.

De automatische actiegoedkeuring wees de winkelwagenproef af onder verwijzing naar de eerdere uitvoerstop. Ook externe codevalidatie werd afgewezen wegens codeoverdracht. Beide handelingen zijn daarom niet uitgevoerd of als geslaagd vermeld.

## Gericht herstel

Lees eerst de actuele thema-rol, bronhashes en de 31 velden opnieuw. De gemaakte metafield-ID’s en waarden staan in de privé-uitvoeringsbewijzen. Verwijder alleen de door deze batch aangemaakte `custom.switch_group`-velden als identiteit en huidige waarde nog exact overeenkomen; behoud alle overige productvelden.

Haal daarna uitsluitend de vijf nieuwe groepsroutes en hun vijf assets uit het concept als ze niet inmiddels voor goedgekeurd vervolgwerk worden gebruikt. Het verwijderen van het twaalfregelige blok herstelt de oorspronkelijke router-MD5 `4a7f03e38cb5b1a488640466fd0ef8a3`. Stop bij latere bronwijzigingen en beoordeel alleen de gerichte diff. De twaalf eerder bijgewerkte basisbestanden blijven op de actuele samengevoegde versie; zet het oude, achterlopende concept niet terug. Geen publicatie of themaverwijdering als onderdeel van dit herstel.
