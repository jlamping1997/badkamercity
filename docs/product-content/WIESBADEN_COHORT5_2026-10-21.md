# Wiesbaden cohort 5 — 44 live verwerkt, 6 in quarantaine (21 oktober 2026)

**VERIFIED_ADMIN_WRITE_AND_READBACK / VERIFIED_PUBLIC_HTML_SAMPLE / SEARCH_INDEX_NOT_SYNCED.**

## Overzicht

- 50 nieuwe, nog niet behandelde bestaande Wiesbaden-SKU's uit de selectie `docs/product-content/wiesbaden/cohort5-readonly-selection-2026-10-21.json`.
- 31 hoofddouches (inclusief Beam/Pluuto) + 19 handdouches.
- **50/50 live fabrikantartikelen succesvol gelezen** op `www.wiesbaden.nl`. Controle op exacte SKU, reeks, soort, leverancierstitel, materiaal waar bekend, bevestiging/leveringsomvang waar toepasselijk. Controle is niet hetzelfde als alle technische tekeningen opnieuw nalopen.
- **44/50 live Shopify-geactualiseerd en Admin-lezen opnieuw geslaagd**: 28 hoofddouches en 16 handdouches, met 540 gegroepeerde productspecificatieregels. Eén eerder geschreven Pluuto-dossier gaf een vals-negatieve controle door `undefined` versus `null` bij een oorspronkelijk leeg documentenveld; alle zes Pluuto-artikelen zijn daarop **apart teruggelezen**, de beschermde velden en eigen productgegevens waren correct. Geen tweede write nodig.
- **6/50 in centrale verwerkingsquarantaine**; geen Shopify-mutatie voor deze SKU's.
- Per live product private originele Admin-backup in `bc_rollback.pre_content_v1`, vóór mutatie aangemaakt. Veranderd: `descriptionHtml`, SEO title/description, `custom.complete_specificaties`, `custom.card_title`, `bc_data.content_review`. Niet veranderd: native producttitel, handle, media, varianteigenschappen/SKU/prijs, voorraad, publicatiestatus, collectieleden, bestaande documenten of oude filtermanifesten.
- **8/8 publieke Shopify storefront product-HTML-steekproeven geslaagd**: SEO-title, SKU, zichtbare tabel, precies één specificatiesblok, geen EAN-rij. Geen volledige browser-/mobiel-/checkoutcontrole.
- Alle 50 fabrikantpagina's op 21 oktober live bereikbaar. Geen opschoonactie bij bestaande producten, geen nieuwe producten aangemaakt.
- **Geen externe Typesense/VPS indexschrijfactie uitgevoerd**. De beschreven getypeerde Shopify-specificaties betekenen niet dat de externe facetfilter al geactualiseerd is.

## Quarantaine — exacte redenen

| SKU | Blokkade |
| --- | --- |
| 29.3848 | Fabrikant geeft geen bevestigde schroefdraad-aansluitmaat voor een losse ronde hoofddouche |
| 29.7821 | Beam muur-hoofddouche mat zwart zonder bevestigde aansluitmaat |
| 29.7825 | Beam muur-hoofddouche geborsteld brons koper zonder bevestigde aansluitmaat |
| 24.3800 | 304 staafhanddouche: fabrikant noemt materiaal 'Overig'; materiële uitvoering controleren |
| 29.3873 | UniMatch staafhanddouche geborsteld staal: belangrijke technische specificaties ontbreken |
| 29.6831 | UniMatch staafhanddouche geborsteld brons koper: materiaal onvoldoende bevestigd |

**Quarantaine is uitsluitend verwerking:** bestaande Shopify-publicatiestatus niet gewijzigd. Canoniek bestand `docs/product-content/wiesbaden/quarantine-register-2026-10-21.json`.

## Resultaat na vijf cohorten

- 5 × 50 unieke SKU's behandeld = **250** uit de bevroren 19-oktober bronkoppelingen.
- **143** SKU's in Shopify bijgewerkt (de eerste negen historische SKU's hebben niet automatisch hetzelfde volledige SEO/spec-contract als nieuwere).
- **106** verwerkingsquarantaines; later gezamenlijk beoordelen met eigenaar.
- **1** eerder goedgekeurd referentieproduct 24.3710 bewust behouden.
- Niet concluderen dat alle 2.240 Wiesbaden-producten of de index voltooid zijn.

## Werkwijze voor vervolg

Hergebruik `scripts/wiesbaden-next-cohort.py` en de bevroren fabrikantbron, met live fabrikantbroncontrole waar mogelijk. Sla **alle 143 applied, 106 quarantine en 1 protected** in het centrale register over, selecteer exact nieuwe SKU's, controleer fabrikantbewijs/Shopify-ID/collectieleden, maak private backup, schrijf, verifieer onafhankelijk en update hetzelfde quarantainebestand. Gebruik geen generieke SKU-regel die incomplete technische compatibiliteit als feit publiceert.

**Noodzakelijke parallelle verbetering:** gevalideerde Typesense/VPS indexroute met readback en facetregressie voordat merkbrede zoek-/filterafronding wordt geclaimd. Automatische HTML-SEO-stekproeven vervangen geen mobiele browse- of bestellingstest.