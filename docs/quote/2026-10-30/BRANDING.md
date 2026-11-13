# Jotform-reclame verborgen — 30 oktober 2026

Eigenaar vraagt de reclame te verbergen. Alleen in het bestaande formulier263018521531044 de custom CSS aangevuld; geen abonnement gekocht, geen nieuwe backend of app. De gewone display:none-regel werd door interne shadow-DOM-stijl overschreven en is niet behouden. De werkende regel is:

```css
form.jotform-form > .formFooter-wrapper {
  content-visibility: hidden !important;
  pointer-events: none !important;
}
```

Deze regel slaat de rendering van alleen de brandingcontainer over. Geen afdekvlak, iframe-crop, vaste hoogte of wijziging aan velden, foutmeldingen, upload, verzending, privacy of notificaties. Dit is een custom stijl en geen officiële betaalde brandingverwijdering; werking is op het huidige formulier bewezen en kan na wijzigingen van Jotform of in oudere browsers hercontrole nodig hebben.

Bewijs: publieke providerpagina na herladen toont geen reclamelinks in de accessibility tree; brandinghost content-visibility:hidden en hoogte0. Lege aanvraag wordt geblokkeerd met vier zichtbare verplichte-veldenmeldingen; formulier blijft op dezelfde URL. Geen aanvraag of e-mail verstuurd. Alle velden en verzendknop zichtbaar, knop48px hoog. In ingebouwde Jotform Phone-preview bij305px: scrollWidth305, brandinghoogte0, knop48px; toetsenbordfocus bereikt verzendknop. Geen fysieke telefoon-, bestandupload-, mailbox- of servervalidatiehertest. Screenshots no-advertising.png en no-advertising-mobile.png; metingen branding-evidence.json. CSS in jotform-design.css; herstel: vervang in de Jotform CSS-editor door jotform-design-before-branding.css.

Verse Shopify-read toont MAIN195916628234; voormalig MAIN195915448586 is UNPUBLISHED. Tijdens deze opdracht geen Shopify-write/publicatie. integration_enabled=false en previewgate alleen voor unpublished zijn behouden. De inmiddels gepubliceerde winkelpagina toont daardoor de contactfallback. Geen klantactivatie uitvoeren als onderdeel van dit stijlpunt.

Volgende handeling blijft eigenaarcontrole van de Jotform-verificatie- en testmail op info@badkamercity.nl; daarna bestaande integratieroute afmaken.
