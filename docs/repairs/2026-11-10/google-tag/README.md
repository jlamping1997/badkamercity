# Nacontrole na publicatie en bestaande Google Ads-tag

Datum: 10 november 2026. Bron: verse Shopify-/GitHub-reads en echte Chrome DOM-controle, zonder thema-preview.

## Resultaat

De vorige chat is veilig opgeslagen: codecheckpoint `7b7260fd613e9cc16e7e60efbab41ea4d4707fe1`, documentatiecheckpoint `ef0131d0d1cd0c105bcfeb568b632fa33a91a4e6`. MAIN is nu **196395073802 — BadkamerCity - Categorieverbeteringen 10 nov**; de voormalige MAIN196416504074 is UNPUBLISHED. Alle twaalf recente categorie-/homepagefiles hebben dezelfde checksums als het geteste concept. Er is voor die bestaande themawijzigingen niets meer te publiceren. Nieuwe themapublicatie noch winkelmutatie is door deze nacontrole uitgevoerd.

## Google-tag

De eigenaar leverde Ads-ID **AW-18563606782** en de standaard gtag.js-headsnippet. Rechtstreeks opnieuw toevoegen is niet gekozen, omdat de bestaande officiële Google & YouTube-koppeling dezelfde Ads-bestemming al bevat.

- Channelapp: Google & YouTube, app-ID1780363; dit is met aparte volledige CHANNEL-paginering gecontroleerd. De gewone appInstallations-lijst alleen sluit saleschannels niet in en mag hiervoor niet als afwezigheidsbewijs dienen.
- Live openbare apppixel:4568023306, typeAPP, apiClientId1780363; precies één vermelding per gecontroleerde pixelconfiguratie.
- Homepage: https://badkamercity.nl/ ; www.badkamercity.nl stuurt hierheen. Geen previewframe.
- Tweede pagina: https://badkamercity.nl/collections/bad-accessoires ; preview expliciet verlaten vóór de controle.
- Ads-bestemming AW-18563606782 en GA4G-H9YFB5TC6N aanwezig. De openbare native configuratie bevat onder andere page_view, view_item, add_to_cart, begin_checkout en purchase-koppelingen. De purchase-configuratie verwijst naar dezelfde Ads-ID.
- Geconfigureerde Google-tagcontainer-ID's: GTM-WPNHKXXR, GTM-TD8PCWDJ, GTM-TFTPNSTW. Deze native configuratie is behouden; geen willekeurige verwijdering of omzetting naar extra thematag.
- De theme-layout bevat geen aparte handmatige Google-tag. De native koppeling injecteert haar pixelconfiguratie via Shopify; zoeken naar uitsluitend een losse gtag.js-scriptnode is daardoor onvoldoende bewijs voor afwezigheid.

Dit bewijst **configuratie in de live storefront**, niet dat Google Ads een bezoek/conversie heeft ontvangen. Geen testbestelling, betalingsactie, ontvangstrapport, volledige netwerktrace of consentproef uitgevoerd. Geen claim dat de melding in Google Ads al is verdwenen. De rechtstreekse Admin-webPixel-read meldt ontbrekende read_pixels-scope; de appinstellingen in de browser vragen om Shopify-inloggen. Er is geen nieuw recht aangevraagd en geen accountwijziging gedaan. Google Ads-tagdiagnose en de bestaande koop-/consentproef blijven open.

Google adviseert de officiële Google & YouTube-route en het vermijden van dubbele tags:

- https://support.google.com/google-ads/answer/16030792?hl=en
- https://support.google.com/google-ads/answer/13494537?hl=en

## Filterserver en eerdere plannen

De publieke healthroute https://vps-7ffd625d.vps.ovh.net/verified/health gaf HTTP200, ok=true, versie0.4.0,227profielen en generatiebc_sync_20261110t000044_d72de7. Dit bewijst bereikbaarheid, niet de nieuwe release. Een losse zoekprobe zonder de geconfigureerde routeprefix gaf404 en is geen functionele filtertest. Gunmetalclassificatie, aanbevolen productmix en Cinto-indexcontrole blijven wachten op het vastgepinde [installatiepakket](../../../filters/gunmetal-2026-11-10/INSTALL.md). De twee Admin-spiegelbreedtes zijn in het eerdere dossier hersteld; nieuwe indexcorrectheid wordt pas na installatie geclaimd.

De [categorie-/titel-/merkenplannen](../../../categorization/2026-11-10/PLAN.md) en [Mondiaz-backlog](../../../imports/mondiaz/PLAN.md) zijn opgeslagen. Niet-opgestarte plannen zijn geen live aanpassing. Andere Wiesbaden-/SEO-werkstromen zijn niet gewijzigd.

## Vervolg

Eén volgende handeling voor de bestaande catalogusrelease: eigenaar voert het vastgepinde filterserverblok uit en deelt de uitvoer. Daarna publieke nacontrole. Voor Google blijft aanvullend ontvangstbewijs via Google Ads-tagdiagnose en een gecontroleerde echte purchase-/consentproef nodig; geen tweede headtag plaatsen zolang de native Ads-bestemming aanwezig is.
