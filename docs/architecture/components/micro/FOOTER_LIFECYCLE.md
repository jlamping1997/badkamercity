# Footer: schermwissel, herinitialisatie en cleanup

**28 oktober 2026 · DOC-03B.** Hoofddossier: [footeropbouw en beheer](../FOOTER.md). Deze verdieping behandelt de JavaScript-lifecycle in de actuele `sections/footer.liquid`; inhoud/configuratie blijft eigendom van dat hoofddossier.

## Eén root, één eigenaar

`roots(scope)` vindt `.bcf-v3` onder een scope en neemt de scope zelf mee wanneer die een footer is. `init(root)` stopt als `root.bcfCleanup` al bestaat. Iedere init maakt één matchMedia-query voor maximaal 749px, verzamelt de eigen `.bcf-nav`-panelen en registreert één rootkliklistener en één mediaquerylistener.

`scan(document)` initialiseert de bestaande pagina. Bij loading bestaat een eenmalige DOMContentLoaded-scan; bij `shopify:section:load` wordt uitsluitend de eventtarget gescand. Herhaald section-load veroorzaakt in FT-02 geen extra mediaquerylistener. Dit is belangrijk bij Theme Editor-herladen; een bronbestand opnieuw evalueren is iets anders dan een bestaande sectie opnieuw initialiseren.

## Staatsovergang

| Gebeurtenis | `details.open` | Summary |
| --- | --- | --- |
| Initialisatie maximaal 749px | `false` | `tabindex`/`aria-disabled` verwijderd |
| Gebruiker opent op klein scherm | Native detailsbediening | Gewoon bedienbaar |
| Query verandert naar desktop | `true` | `tabindex=-1`, `aria-disabled=true` |
| Klik op desktopsummary | Blijft open | Handler voorkomt defaultactie |
| Terug naar klein scherm | Opnieuw `false` | Weer bedienbaar |

De synchronisatie bewaart de eerdere mobiele openkeuze **niet** bij heen-en-weer wisselen. FT-01 bevestigt de gewenste bronovergang onder een gecontroleerde matchMedia-stub. De footer gebruikt native details; er is geen eigen hoogteanimatie of permanente voorkeurstorage toegevoegd.

De CSS ondersteunt open desktopinhoud ook wanneer een details-element niet open staat. De server start de panels open; zonder JS blijft inhoud beschikbaar. Een mogelijke mobiele open→dicht-laadverschuiving is hiermee verklaard, maar niet gemeten. De bestaande echte desktopwaarneming in DOC-02C bevestigt drie open panelen met summaries buiten de tabvolgorde; de nieuwe replay is geen nieuwe mobiele praktijkmeting.

## Sectie verwijderen en terugplaatsen

Bij `shopify:section:unload` verwijdert `bcfCleanup` de mediaquery- en rootkliklistener en verwijdert de cleanupmarker. FT-02 bevestigt nul resterende geregistreerde mediaquerycallbacks in de stub, waarna een volgende section-load opnieuw één initializer aanmaakt.

Deze cleanup verwijdert geen content of instellingen. Hij is specifiek aan de footerroot gekoppeld en hoort behouden te blijven bij stylingwijzigingen. Een tweede globale clickhandler voor dezelfde summaries kan dit contract verstoren. Een DOM-element verwijderen zonder het Shopify-unloadevent is niet hetzelfde geteste pad; claim geen algemene leakvrijgave voor alle externe DOM-wijzigingen.

## Wat blijft open?

Werkelijk touch-/keyboardgedrag bij 749↔750px, native details in verschillende browsers, focus wanneer het actieve paneel tijdens resize sluit en de visuele laadstaat. MatchMedia en native detailsbediening zijn in de replay gecontroleerde vervangers. Tien ontbrekende bestemmingen (FOOTER-F01) blijven een aparte configuratiebevinding; lifecycletests lossen die niet op.

[FT-01/FT-02 en bronhashes](../../evidence/2026-10-28-transitions/README.md).
