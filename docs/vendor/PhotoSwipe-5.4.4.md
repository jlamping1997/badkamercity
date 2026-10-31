# PhotoSwipe 5.4.4 — herkomst en licentie

De Sunshower-fotogalerij gebruikt de standalone PhotoSwipe-core uitsluitend voor de vergrote viewer. De native carrousel op de productpagina heeft deze module niet nodig. De module wordt vanaf de eigen Shopify-theme-assets geladen wanneer de viewer wordt geopend.

- Naam/versie: `photoswipe@5.4.4`.
- Bron: officieel npm-pakket `https://registry.npmjs.org/photoswipe/-/photoswipe-5.4.4.tgz`.
- Documentatie: https://photoswipe.com/getting-started/ en https://photoswipe.com/data-sources/#without-lightbox-module.
- Tarball SHA1: `e045dc036453493188d5c8665b0e8f1000ac4d6e`.
- Tarball SHA512-integriteit gecontroleerd tegen npm: `sha512-WNFHoKrkZNnvFFhbHL93WDkW3ifwVOXSW3w1UuZZelSmgXpIGiZSNlZJq37rR8YejqME2rHs9EhH9ZvlvFH2NA==`.
- Geen installatiescripts uitgevoerd; de drie onderstaande bestanden zijn byte-exact uit het pakket overgenomen.
- MIT-licentie inclusief copyright: [exact licentiebestand](PhotoSwipe-5.4.4-LICENSE.txt), tevens als `assets/bc-photoswipe-license.txt` opgenomen in de productiepatch.

| Theme-asset | Bronbestand | Bytes | SHA256 |
| --- | --- | --- | --- |
| `assets/bc-photoswipe.esm.js` | `package/dist/photoswipe.esm.min.js` | 54270 | `542069771beb34dc461cdb9374da8af643c591ebf65d8ec36331dd9a0681ebd4` |
| `assets/bc-photoswipe.css` | `package/dist/photoswipe.css` | 7423 | `b0eaaae0b9de064d25e2f18517b9011a526d9b2142376e1c0febd096cebab9f3` |
| `assets/bc-photoswipe-license.txt` | `package/LICENSE` | 1129 | `2c223af0b21d32240087ee189eb70fd315907b6ade8b561e24265baccd6a98e7` |

De standalone core heeft geen JavaScript-importafhankelijkheden; de CSS verwijst niet naar externe assets. De ESM-syntax is gecontroleerd. Versie-upgrades moeten opnieuw op package-integriteit, byte-identiteit en galerijgedrag worden gecontroleerd. Deze notitie bewijst geen browser- of fysieke-telefoontest; daarvoor geldt het releaseverificatiebestand.
