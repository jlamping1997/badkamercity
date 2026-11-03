# JEE-O kleurkeuze — 3 november 2026

Status: **IMPLEMENTATION_IN_PROGRESS / PILOT_METADATA_VERIFIED / THEME_COPY_PENDING**.

## Opdracht en scope

De eigenaar heeft Hotbath-stijl kleurbolletjes goedgekeurd voor JEE-O op productpagina en productkaart. De273verbeterde titels behouden. Geen productcreatie, prijs-,voorraad-,SKU-,URL- of mediawijziging.

65exacte modelfamilies/228producten met unieke afwerkingen per groep. SWMBAS71/2producten uitgesloten wegens conflicterende fabrikantcode;43producten zonder bestaande kleurtegenhanger. De8fabrikantbevestigde en57catalogusgevalideerde groepen blijven onderscheiden in de privéwerkset.

## Bron en featurefiles

Verse MAIN196052189450,1356filenames/checksums vooraf bewaard. Nieuw via themeDuplicate gemaakt UNPUBLISHED196110090506 **BadkamerCity - JEE-O kleurkeuzes**. Kopieerjob nog actief; geen upload tot processing:false en volledige checksumpariteit.

Git-root was geen actuele themasnapshot. Drie bestaande featurefiles eerst vers uit MAIN gelezen. Groot Git-diff in main-product bevat dus ook synchronisatie van bestaande livecode; eigen featuredelta daarin is één JEE-O-elsif/render van twee regels. Alleen20featurefiles uploaden, nooit volledige Git-root.

Bestaand: sections/main-product.liquid, sections/bc-card-data.liquid, assets/bc-external-filters.js. Nieuw: snippets/bc-jeeo-colors.liquid, snippets/bc-jeeo-swatch-url.liquid en15assets/bc-jeeo-swatch-*.svg. Bestaande V2-JavaScript en Hotbath/Wiesbaden-styling ongewijzigd hergebruikt.

## Contract

custom.color_variants gebruikt de bestaande list.product_reference-definitie. Alle leden krijgen dezelfde geordende referentielijst inclusief zichzelf. custom.kleur levert de canonieke afwerking. Adapter controleert JEE-O, gelijk producttype, gelijke SKU-modelcode, wederkerig groepsanker, unieke kleuren en aanwezigheid huidig product. Kleurwissel behoudt maat/model.

Numeric SKU van acht tekens: eerste zeven tekens vormen model. Overige SKU's: code vóór eerste koppelteken. Geen maatrelatie uit titels afgeleid. Alleen gekoppelde JEE-O-kaarten krijgen custom.kleur-voorrang op filtermanifest; afwerking niet dubbel in kaarttitel en kleurregel. Gericht JEE-O toegevoegd aan SVG-origin/CDN-controle naast Wiesbaden. Geen externe index of globale filteractivatie gewijzigd.

## Checkpoint en tests

Eerste3Slimline-plafondarmgroepen van5per lengte15/25/35cm:15producten/30metafields met compareDigest:null geschreven, exact teruggelezen; titel/handle gelijk. Overige62groepen/213producten wachten op conceptpilot.

Theme Check revisie3:20/20files geldig, drie bestaande main-product-waarschuwingen (complexiteit, seo_media, continue). Eerste twee runs misten actuele afhankelijkheden in oude Git-checkout; alleen tijdelijke validatiekopie aangevuld. Node syntaxcheck en XML-parse van15SVG's PASS.

Nog onbewezen: conceptpariteit/upload/readback, browser-PDP/productkaart, kleur→titel/foto/prijs/variant/link, smalle weergave, overige metadata/eindinventaris. Geen fysieke telefoon-, Windows-, winkelwagen-,checkout- of performancevrijgave. Geen publicatie.

## Herstel en vervolg

Volledige vooropname/groep-ID's vóór writes privé bewaard. Alleen custom.color_variants/custom.kleur uit eigen receipts terugzetten; oorspronkelijk leeg. Eerst actuele digests vergelijken om latere wijzigingen te behouden. Thema: MAIN laten staan; eventueel drie bestaande featurefiles uit vooropname herstellen en17nieuwe featurefiles weghalen. Geen themaverwijdering nodig.

Actieve uitvoerder: Codex connector/cloudsessie, branch fix/product-cards-2026-10-14. Volgende handeling: voltooide conceptkopie op1356checksums verifiëren,20files uploaden en15proefproducten testen vóór overige koppelingen.
