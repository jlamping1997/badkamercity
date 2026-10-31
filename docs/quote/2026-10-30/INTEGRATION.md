# Jotform-aansluiting — 30 oktober 2026

Status: FORM_CREATED / CONCEPT_CONNECTED / EMAIL_VERIFICATION_AND_DELIVERY_PENDING / CUSTOMER_ACTIVATION_DISABLED. Deze actuele stand vervangt de eerdere melding dat nog geen account bestond.

## Ingericht

Eigenaar heeft het account aangemaakt en via beveiligde aanmelding toegang gegeven. Geen wachtwoord, login-code, sessie of API-key verwerkt in Git. Er bleek geen directe beschikbare Jotform-plugin; inrichting via de Jotform-interface. Formulier263018521531044 heet Badkamercity – Laagsteprijsgarantie. [Formulierbouwer](https://www.jotform.com/build/263018521531044) · [publieke providerroute](https://form.jotform.com/263018521531044).

| Onderdeel | Actuele instelling |
| --- | --- |
| Taal | Nederlands primair; Engelse vertaling door provider nog beschikbaar |
| Kop | Vraag een betere prijs aan |
| Intro | Stuur je offerte op en ontvang een betere prijs voor dezelfde producten en uitvoeringen. |
| Keuze | Volledige offerte / één product; verplicht |
| Naam | Voornaam en achternaam; verplicht |
| E-mail | Verplicht e-mailveld |
| Bijlage | Verplicht; PDF/JPG/JPEG/PNG; max3bestanden,10MB per bestand |
| Toelichting | Optioneel |
| Telefoon | Weggelaten; formulier kort houden, geen Amerikaanse telefoonmaskering |
| Verzendknop | Vraag een betere prijs aan |
| Gegevensgebruik | We gebruiken je gegevens om je aanvraag te behandelen. |
| Uploadhulp | Leesbare artikelcodes/aantallen/prijzen; overbodige gegevens van anderen onleesbaar maken |
| Notificatie | info@badkamercity.nl, expliciet gekozen door eigenaar |
| Klantbevestiging | Uitgeschakeld; accountverificatie voor aanpassing vereist |
| Bestandsinzage | Accountinstelling Require log-in to view uploaded files aangevinkt |
| Inzendingeninzage | Require log-in to see submissions aangevinkt |
| Bewaartermijn | Nog niet vastgesteld/geconfigureerd; geen automatische verwijdering aangezet |

Geen betaling, marketinginschrijving, reactiebelofte of reviewvoorwaarde. Geen externe integraties, nieuwe medewerkers of publieke inzendingstabel. Providerroute staat standaard publiek om klanten zonder Jotform-account te kunnen laten insturen; inzendingen en bijlagen zijn daarvan afzonderlijk afgeschermd. De laatste anonieme toegangstest blijft open, zie bewijs.

Opmaak: wit, Arial, donkerblauw, lichtblauwe rechte knop. Jotform-designer-CSS voor100%breedte/max680px, geen formulierschaduw/rand,16pxsectiepadding en8pxveldpadding. Jotform-branding van huidige plan behouden; geen betaald plan gekozen of brandingbeperking omzeild. Providerconfiguratie blijft in Jotform; dit dossier en de DOM-/readbackproeven zijn geen volledige Jotform-back-up.

## Websiteconcept

MAIN195915448586/1.349files behouden. Concept195916628234/1.350files, UNPUBLISHED. Exact drie bronbestanden gewijzigd: sections/bc-quote.liquid, assets/bc-quote.css en templates/page.offerte-vergelijken.json. Bestaande sectie en CSS vooraf uit Shopify opgeslagen in integration-baseline/.

Formulier-ID ingevuld, integration_preview=true; deze nieuwe previewgate werkt uitsluitend als theme.role=unpublished en het ID numeriek/10–20tekens is. integration_enabled=false en show_preview=false. Publicatie alleen zet de preview niet voor klanten aan. De echte iframe gebruikt dezelfde vaste https://form.jotform.com-host als de voorbereide koppeling. Paneelkop niet dubbel naast providerkop; iframefallback1450pxdesktop/1650pxmobiel en link naar nieuw venster. Geen nieuwe JavaScript of providerlibrary.

Shopify-pagina166573539594 nog isPublished=false. Header-/footerklantactivatie blijftfalse; homepage-teaser disabled. Geen mobiele headerbalk. De contact?view=offerte-vergelijken-route in concept toont het werkende iframe en blijft een alternatieve reviewroute, geen SEO-/canonicalvrijgave voor de nieuwe pagina. Geen Shopify-publicatie door agent.

## Bewijs

- 17lokale LiquidJS/DOM-cases PASS, inclusief veilige vaste host, ongeldig-ID-guard, providerpreview uitsluitend ongepubliceerd en uitgeschakelde klantactivatie. Zie tests.json/test-quote.cjs.
- Drie ThemeCheck-files PASS (integration-themecheck.json); documentmanifestverversing had een netwerktimeout, aanwezige Shopify-doccache is gebruikt.
- Drie conceptinhouden exact of JSON-semantisch teruggelezen. Alle1.349MAIN-checksums gelijk aan beginmeting; overige conceptfiles behouden. Tijdelijke index.bc-homepage-review.liquid exact hersteld.
- Echt formulier: tekstbestand wordt met Nederlandstalige foutmelding geweigerd. Fictieve PDF781bytes geüpload en eenmaal verzonden; echte bedankpagina Aanvraag ontvangen. Eén testrecord in Jotform Tables met naam Test Badkamercity en expliciete NIET BESTELLEN-toelichting. Geen klantdata of productprijswijzigingen.
- Bevoegde download vanuit ingelogd account geslaagd; alle781bytes exact gelijk aan origineel. Testrecord en bijlage nog aanwezig, geen verwijderproef geclaimd. Private bijlage-URL/submission-ID/accountbeveiligingsschermen met IP's niet in Git opgeslagen.
- Anonieme retrieval via externe uitleestool gaf uitsluitend niet-toegankelijk/interne fout. Dat bewijst geen404 of loginweigering. ANONYMOUS_ACCESS_NOT_VERIFIED, geen geslaagde anonieme privacytest claimen.
- Notificatietekst/ontvanger opgeslagen, losse uploadbijlagen uit. Mailboxbezorging NOT_VERIFIED; klantmail expliciet disabled (contextmenu biedt Enable). Eigenaar meldt verificatielink nog niet te hebben geopend/ontvangen. Geen klantbevestigingstest.
- Desktopwebsiteiframe569pxbreed/1270,8pxformulierhoogte, zonder horizontale overloop. Providerframes320/390px zonder overloop, formulierhoogten1360,2/1308,8px; echte responsive providerframes, geen fysieke telefoon of complete mobiele website. Zie jotform-mobile-checks.json.
- Screenshots: jotform-integrated.jpg, jotform-mobile.jpg, jotform-success.jpg. Geen extra inzending door de schermcontrole.

Niet getest:10MBgrens, vierde bestand, vermomde MIME-/servervalidatie, virusscan, dubbele klik/verzendherstel, anonieme loginweigering, verwijdering, spam-/quotareactie, fysieke telefoon en uiteindelijke openbare Shopify-pagina. Geen volledige productierijpheid verklaren.

## Vervolg

Eén eerstvolgende handeling: eigenaar controleert de verificatie- en testmail op info@badkamercity.nl, ook spam. Na accountverificatie een korte Nederlandse klantbevestiging zonder inzendings-/bijlagekopie inrichten, eigen e-mailveld als ontvanger kiezen en opnieuw testen. Bezorging, anonieme bestandstoegang en de verwijder-/bewaarprocedure vóór klantactivatie afmaken. Bewaarvoorstel90dagen is nog geen vastgesteld beleid.

Daarna actuele MAIN/concept opnieuw verifiëren, native telefoonreview, integration_preview=false en integration_enabled=true uitsluitend na testvrijgave. Shopify-pagina en thema door eigenaar publiceren; header/footer afzonderlijk activeren. Bestaande homepage-teaser alleen indien later gewenst. Publiceer nooit blind de volledige Git-root.

## Terugzetten

Alleen testprovider verbergen: integration_preview=false en integration_enabled=false. Voor de vorige uitgeschakelde voorbeeldweergave drie bestanden uit integration-baseline/ uitsluitend naar actueel ongepubliceerd concept herstellen. Dat verwijdert of wijzigt geen Jotform-inzending. Klantmail blijftuit tot eigen expliciete activering.
