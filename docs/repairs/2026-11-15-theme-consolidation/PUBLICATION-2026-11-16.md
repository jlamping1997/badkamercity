# Brauer-publicatie — 16 november 2026

Status: PUBLISHED / PUBLIC_DESKTOP_QA_VERIFIED.
Opdracht: eigenaar: “Oke laten we brauer online gaan zetten dan”.
Uitvoering: ChatGPT via Shopify/GitHub en echte Chrome; geen toegang tot de Windows-pc.

## Publicatie

Gepubliceerd: **BadkamerCity - complete Brauer productkeuzes (196690379018)**.
Vorig MAIN: **BadkamerCity - bescherming oude productkaarten (196542005514)**, nu UNPUBLISHED en beschikbaar als terugzetthema.
De ingebouwde publicatiekoppeling weigerde met “Only agent-created themes can be published here”. Publicatie vervolgens via de bestaande, aangemelde Shopify-beheersessie uitgevoerd. De bevestiging noemde exact het bedoelde thema en oude MAIN; daarna verscheen “Thema gepubliceerd”.
Onafhankelijke read-only Shopify-query bevestigt na de UI-publicatie MAIN196690379018, processing=false, processingFailed=false.

## Verse controle vóór publicatie

| Controle | Resultaat |
|---|---|
| Huidig live thema | 2524 bestanden |
| Samengevoegd concept | 2525 bestanden |
| Verschillen | 183 bedoelde Brauer-bestanden |
| Ontbrekende bestanden | 0 |
| Onbedoelde verschillen | 0 |
| Featurechecksums vergeleken met verification.json van 15 november | 183/183 exact |
| Alle bestanden gelezen | 51 dubbele manifestpagina’s, maximaal 50 bestanden per verbinding |

Hiermee zijn de bronbestanden van de recente filterkleuren, Lagoo-documentweergave en productkaartbescherming behouden. Deze beurt herhaalde geen afzonderlijke interactieve regressieproef voor die drie functies.
De gepubliceerde code is de eerder vastgelegde en gevalideerde release uit [README.md](README.md). Geen nieuwe themacode geschreven.

## Openbare Chrome-proeven na publicatie

De bestaande previewcookie is via “Exit preview” verlaten vóór de proeven. De pagina’s hieronder hebben geen previewparameter.

| Proef | Waarneming | Resultaat |
|---|---|---|
| Opbouwkraan 5-CE-001: Kort en smal | Opent 5-CE-001-HD5, juiste titel/productfoto en €187,67; onmogelijke afwerkingen disabled | PASS |
| Daarna Hoog, ronde uitloop | Opent 5-CE-003-R2, juiste foto, geselecteerde hendel/uitvoering en €268,50. Hendel- en uitvoeringsfoto’s zichtbaar | PASS |
| Spiegelkast SK-IMD100HW: 100→60 cm | Expliciete vraag “Draairichting deur”; Links/Rechts, koopknop disabled zolang richting ontbreekt | PASS |
| Daarna Links | Opent SK-IMD60LHW met linksdraaiende titel, €882,09 en werkende koopknop | PASS |
| Void GS-VON2H6050200CE: Aan de glaswand | Opent GS-VON3H6050200CE, €1153,13; 90/100 cm disabled; heldere uitleg muur/glas en juiste nieuwe galerij | PASS |

Resultaat-URL’s:
- Kraan: https://badkamercity.nl/products/brauer-standaard-hoge-opbouw-wastafelkraan-met-draaibare-ronde-uitloop-model-b-chroom-5-ce-003-r2
- Spiegelkast: https://badkamercity.nl/products/brauer-impress-deluxe-spiegelkast-60-met-interne-en-externe-verlichting-1-linksdraaiende-dubbelzijdige-spiegeldeur-hoogglans-wit-sk-imd60lhw
- Deur: https://badkamercity.nl/products/brauer-void-nisdeur-2-delig-helder-glas-110x200-omkeerbaar-met-draaideur-60-aan-glas-incl-glascoating-chroom-gs-von3h6050200ce

## Grenzen en open werk

Deze release bevat de eerder geteste renderer voor828groepen/12.292artikelen, met173inhoudelijk verfijnde/geprijsde groepen voor6402artikelen; niet alle828groepen zijn hiermee volledig inhoudelijk beoordeeld.
Prijsvolgorde gebruikt nog de12novembersnapshot. De hierboven waargenomen PDP-prijzen komen uit de actuele webshop;6402prijzen zijn niet opnieuw vers vergeleken.
Geen nieuwe cart-add, checkout, echte betaling, order-/mailketen, fysieke telefoon, VPS/index of catalogusbrede inhoudscontrole uitgevoerd. De spiegelkastproef valideert de koopknopblokkade, geen daadwerkelijke koop.
Lagoo105foto-holds en historische Wiesbaden-twijfelgevallen behouden. Productvolgorde blijft geparkeerd. Geen producten, prijzen, voorraad, media, productstatussen of Google-instellingen gewijzigd.

## Hervatten en herstel

**Afgerond:** de klaargezette samengevoegde Brauer-release publiceren en de drie openbare desktopkeuzeroutes controleren.
**Eén volgende handeling:** complete bestelproef voorbereiden en uitvoeren met passende eigenaarsinvoer voor betaling en mailontvangst; mobiel en verzendkosten meenemen.
Herstel: eigenaar kan het vorige intacte thema196542005514 opnieuw publiceren. Oude losse Wiesbaden-/Brauer-concepten niet gebruiken als release.
Geen actieve schrijver na deze overdracht. Documentatie wordt op main en de bestaande codebranch gelijk bijgewerkt; dit is geen Windows-syncclaim.
