# BRAUER — bestaande winkelvelden en collectiedoelen

6 november 2026. Read-only Shopify-inventaris; onderstaande voorstellen zijn niet in de winkel toegepast. **227 collecties** volledig over vijf pagina’s en **258 PRODUCT-metafielddefinities** over zes pagina’s gelezen. Collectieaantallen zijn Admin-lidmaatschappen, geen bewijs van publieke koopbaarheid. Bronbestanden en individuele Shopify-productwaarden blijven privé.

## Veldmapping op echte definities

Dit is een mappingvoorstel; nog geen importinput. Een bestaande definitie bewijst geen zichtbaarheid in de productpagina.

| Bronkolom | Bestaand doel / voorstel | Beslisregel |
| --- | --- | --- |
| Artikelcode | Native variant-SKU; custom.artikelnummer; custom.leverancier_artikelnummer | Exacte string behouden. Beide custom-definities zijn single_line_text_field. |
| EAN | Native variant-GTIN/barcode | Exacte string. Huidige read-surface heet ProductVariant.barcodes; write-input vóór implementatie op huidig schema controleren. custom.ean wordt door legacy gelezen maar heeft geen PRODUCT-definitie in deze inventaris; geen extra veld automatisch aanmaken. |
| Merk | Product.vendor | BRAUER. |
| Productomschrijving | Product.title + bewaarde bronomschrijving | Unieke leesbare titel afleiden; geen volledige lange producttekst claimen. |
| Adviesverkoopprijs ex. Btw | Privé bronprijs → variant-verkoopprijs na prijsbesluit | Geen directe verkoopprijs/compare-at-mapping. Voorbereide consumentenprijs: advies ex btw × 1,21, centafronding; geen korting aangenomen. Shopify taxesIncluded=true gecontroleerd. |
| Levertijd | Privé bron-levertekst; eventueel custom.leverancier_verwachte_datum (date) na bevestiging | Geen live voorraad afleiden. custom.leverancier_voorraad bestaat (boolean); alleen op basis van daarvoor geschikte bron schrijven. Generieke BRAUER-levertekst vereist rendereradapter. |
| Hoofdcategorie | Bestaande collectie-ID’s via gecontroleerde mapping | Geen bronhoofdgroep direct als Shopify-taxonomiecategorie beschouwen. |
| Productcategorie | Product.productType + passende bestaande collectie-ID’s | Beheerst typewoordenboek; bestaande singular/plural-varianten controleren bij collectievoorwaarden. |
| Productgroep | Bestaande collectie-ID’s + expliciete productrol | Complete set/los onderdeel onderscheiden. Geen nieuwe collectie per bronlabel. |
| Serie | custom.serie + bc_filters.serie | Beide bestaande, gebruikte single_line_text_field-definities. Bronlabel apart bewaren. |
| Uitvoering | specs.uitvoering (bestaand) of type-specifieke JSON/keuzedata na rendererbesluit | Geen custom.uitvoering PRODUCT-definitie gevonden. specs.uitvoering bestaat, maar generieke BRAUER-legacyroute leest het niet. |
| Materiaal | custom.materiaal + bc_filters.materiaal | Bestaande single_line_text_field-definities. 27 bronconflicten eerst oplossen. Huidige legacyroute leest materiaal_kraan, niet generiek materiaal. |
| Kleur | custom.kleur + bc_filters.kleur; geverifieerd glaskleur apart | Bestaande single_line_text_field-definities. Geen samengevoegd beslag/glaskleur-label als één onduidelijke filterwaarde. |
| Afwerking | custom.afwerking + bc_filters.afwerking | Bestaande single_line_text_field-definities. Twee bronconflicten eerst oplossen. PVD/coating niet uit kleur afleiden. |

## Bewezen bronroute in actuele MAIN

MAIN is **196246372618 — BadkamerCity - Cottoceramix volledig assortiment**. De relevante bestanden zijn read-only via Shopify teruggelezen; MD5’s en bronbytes staan in `live-theme-relevant-files.json` en `live-main-product.json`.

- `snippets/bc-product-detail-specs.liquid` stuurt BRAUER naar `bc-product-detail-specs-legacy`. De generieke `custom.complete_specificaties`-JSON wordt daardoor niet automatisch als volledige BRAUER-specificatietabel getoond. De m²-tegelroute en Wiesbaden/JEE-O-route mogen niet als algemene merkroute worden verondersteld. Een gerichte generieke renderer/routeraanvulling hoort bij de proef.
- `bc-product-detail-specs-legacy` leest vooral kraankenmerken. Generieke kleur, materiaal, glas- en meubelkenmerken missen daarin zichtbare dekking. Niet honderden aliasvelden vullen om toevallig deze oude route passend te maken.
- `bc-product-short-specs.liquid` bevat uitsluitend de melding dat het blok verwijderd is. Bestandsaanwezigheid is geen werkende korte-specificatieroute.
- `snippets/bc-card-delivery.liquid` toont Cottoceramix-bronlevertijd; voor BRAUER valt het terug op bestaande neutrale tekst. `bc-cart-delivery.liquid` ondersteunt tiles/unit en Wiesbaden, geen algemene BRAUER-levertekst. Beleid en adapter voor consistentie op kaart/PDP/cart samen testen; BRAUER niet als tiles vermommen.
- `sections/main-product.liquid` rendert bij niet-lege `custom.switch_group` de bestaande V2-switcher, na andere merkspecifieke routes. Voor BRAUER zijn een correcte groep én een passende datasetbron nodig; alleen het veld invullen bewijst geen volledig keuzemenu.

**Namespacecontrole:** een onafhankelijke directe query op Wiesbaden Alvara (product-ID10657402880266) retourneert namespace `custom`, key `complete_specificaties`; een namespace-only lijst bevestigt dit. De eerdere selectievorm `keys:["custom.complete_specificaties"]` retourneert keys in hetzelfde volledig gekwalificeerde selectieverzoekformaat. Dit is geen dubbele prefix in opslag. Schrijf later namespace `custom`, key `complete_specificaties`, niet key `custom.complete_specificaties`. Bewijs: `key-format-verification.json`.

## Bestaande collectiedoelen

Deze tabel bewijst uitsluitend dat de identiteit bestaat. Root koppelt volledige artikeltypevoorstellen aan deze registry; geen nieuwe collecties zijn aangemaakt. Een artikel kan meerdere zinvolle bestaande ingangen hebben.

### Kraan hoofdgroep

| Handle | Titel | Exacte collectie-ID |
| --- | --- | --- |
| kranen | Kranen | gid://shopify/Collection/569428181258 |
| wastafelkranen | Wastafelkranen | gid://shopify/Collection/570058506506 |
| opbouw-wastafelkranen | Opbouw wastafelkranen | gid://shopify/Collection/570059522314 |
| inbouw-wastafelkranen | Inbouw wastafelkranen | gid://shopify/Collection/570059555082 |
| fonteinkranen | Fonteinkranen | gid://shopify/Collection/570059587850 |
| opbouw-fonteinkranen | Opbouw fonteinkranen | gid://shopify/Collection/570059686154 |
| inbouw-fonteinkranen | Inbouw fonteinkranen | gid://shopify/Collection/570059620618 |
| badkranen | Badkranen | gid://shopify/Collection/570059227402 |
| vrijstaande-badkranen | Vrijstaande badkranen | gid://shopify/Collection/570059358474 |
| inbouw-badkranen | Inbouw badkranen | gid://shopify/Collection/570059325706 |
| douchekranen | Douchekranen | gid://shopify/Collection/570058932490 |
| douche-thermostaatkranen | Douche thermostaatkranen | gid://shopify/Collection/570058998026 |
| inbouw-douchekranen | Inbouw douchekranen | gid://shopify/Collection/570059063562 |

### Douchesets en losse kranenonderdelen

| Handle | Titel | Exacte collectie-ID |
| --- | --- | --- |
| douchesets | Douchesets | gid://shopify/Collection/570058965258 |
| inbouw-douchesets | Inbouw douchesets | gid://shopify/Collection/584784969994 |
| opbouw-douchesets | Opbouw douchesets | gid://shopify/Collection/584785035530 |
| handdouches | Handdouches | gid://shopify/Collection/570059096330 |
| hoofddouches | Hoofddouches | gid://shopify/Collection/570059129098 |
| doucheslangen | Doucheslangen | gid://shopify/Collection/570059948298 |
| glijstangen | Glijstangen | gid://shopify/Collection/584785068298 |
| glijstangsets | Glijstangsets | gid://shopify/Collection/584785101066 |
| wanduitlaten | Wanduitlaten | gid://shopify/Collection/584785264906 |
| hoofddouchehouders | Hoofddouchehouders | gid://shopify/Collection/570060046602 |
| handdouchehouders | Handdouchehouders | gid://shopify/Collection/570060013834 |
| baduitlopen | Baduitlopen | gid://shopify/Collection/584785297674 |
| wastafeluitlopen | Wastafeluitlopen | gid://shopify/Collection/584785330442 |
| afbouwdelen-voor-kranen | Afbouwdelen voor kranen | gid://shopify/Collection/584785133834 |
| losse-inbouwdelen | Losse inbouwdelen | gid://shopify/Collection/584785166602 |
| kraanonderdelen | Kraanonderdelen | gid://shopify/Collection/584785199370 |
| kraan-toebehoren | Toebehoren voor kranen | gid://shopify/Collection/584286241034 |

### Meubels/wastafels/spiegels

| Handle | Titel | Exacte collectie-ID |
| --- | --- | --- |
| badkamermeubels | Badkamermeubels | gid://shopify/Collection/569428148490 |
| losse-onderkasten | Losse onderkasten | gid://shopify/Collection/570057982218 |
| wastafelbladen | Wastafelbladen | gid://shopify/Collection/570058014986 |
| meubelwastafels | Meubelwastafels | gid://shopify/Collection/570062045450 |
| fonteinmeubels | Fonteinmeubels | gid://shopify/Collection/570061259018 |
| toiletmeubels | Toiletmeubels | gid://shopify/Collection/570057916682 |
| kolom-zijkasten | Kolom & Zijkasten | gid://shopify/Collection/570057949450 |
| hoge-kasten | Hoge kasten | gid://shopify/Collection/570058342666 |
| halfhoge-kasten | Halfhoge kasten | gid://shopify/Collection/570058375434 |
| badkamerspiegels | Badkamerspiegels | gid://shopify/Collection/570058834186 |
| spiegelkasten | Spiegelkasten | gid://shopify/Collection/570058473738 |
| spiegelverlichting | Spiegelverlichting | gid://shopify/Collection/570067550474 |
| toebehoren | Toebehoren | gid://shopify/Collection/570058113290 |

### Glas/afvoer

| Handle | Titel | Exacte collectie-ID |
| --- | --- | --- |
| douches | Douche | gid://shopify/Collection/570057130250 |
| douchecabines | Douchecabines | gid://shopify/Collection/570063814922 |
| douchewanden | Douchewanden | gid://shopify/Collection/570064011530 |
| inloopdouches | Inloopdouches | gid://shopify/Collection/570064044298 |
| badwanden | Badwanden | gid://shopify/Collection/570064077066 |
| douchedeuren | Douchedeuren | gid://shopify/Collection/570064109834 |
| draaideuren | Draaideuren | gid://shopify/Collection/570064142602 |
| schuifdeuren | Schuifdeuren | gid://shopify/Collection/570064175370 |
| pendeldeuren | Pendeldeuren | gid://shopify/Collection/570064208138 |
| vouwdeuren | Vouwdeuren | gid://shopify/Collection/570064240906 |
| douchebakken | Douchebakken | gid://shopify/Collection/570064273674 |
| douchegoten | Douchegoten | gid://shopify/Collection/570064306442 |
| doucheafvoer | Doucheafvoer | gid://shopify/Collection/585793929482 |
| doucheonderdelen | Doucheonderdelen | gid://shopify/Collection/585793995018 |
| douche-accessoires | Douche accessoires | gid://shopify/Collection/570064929034 |

### Accessoires/toilet

| Handle | Titel | Exacte collectie-ID |
| --- | --- | --- |
| accessoires | Accessoires | gid://shopify/Collection/569428312330 |
| toilet-accessoires | Toilet accessoires | gid://shopify/Collection/569436995850 |
| wastafel-accessoires | Wastafel accessoires | gid://shopify/Collection/569437061386 |
| wastafel-toebehoren | Toebehoren voor wastafels | gid://shopify/Collection/584286273802 |
| afvoerpluggen | Afvoerpluggen | gid://shopify/Collection/570058572042 |
| sifons | Sifons | gid://shopify/Collection/570058539274 |
| toiletrolhouders | Toiletrolhouders | gid://shopify/Collection/570056278282 |
| toiletborstelhouders | Toiletborstelhouders | gid://shopify/Collection/570056311050 |
| handdoekhouders | Handdoekhouders | gid://shopify/Collection/569437028618 |
| handdoekhaken | Handdoekhaken | gid://shopify/Collection/570057523466 |
| zeepdispensers | Zeepdispensers | gid://shopify/Collection/570057589002 |
| planchetten | Planchetten | gid://shopify/Collection/570057654538 |
| inbouw-opbouw-nissen | Inbouw/opbouw nissen | gid://shopify/Collection/569437192458 |

## Echte hiaten en grenzen

- Geen bestaande BRAUER-merkcollectie gevonden.
- Geen exacte collectie voor losse ladefronten, deurfronten, spiegeldeuren of bodemplaten gevonden. Niet als complete meubelset classificeren. Bestaande `toebehoren` kan een voorstel zijn, maar moet inhoudelijk worden beoordeeld.
- Geen exacte collectie voor losse glaspanelen/glaspakketten/beslagpakketten gevonden. Complete douche-opstelling en component blijven verschillende productrollen; bestaande doucheonderdelen kan kandidaat zijn.
- Geen specifieke roostercollectie gevonden. Een los gootrooster niet stil als complete douchegoot verkopen.
- `metafieldsCount` bereikt bij sommige definities10001; die veldgebruiksaantallen zijn niet als onafhankelijk exacte winkelbrede totalen gebruikt.
- Tien representatieve bestaande producten zijn als veldsteekproef gelezen. Dat bewijst geen foutloze invulling van alle producten. De categorisatie-/collectievoorwaarden en publieke routes moeten vóór import/publicatie nog per definitief doel worden getoetst.

