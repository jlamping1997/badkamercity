# Merchant Center en aankoopmeting — 16 november 2026

Status: ACCOUNT_DIAGNOSTICS_VERIFIED / RETURN_POLICY_SAVED_VERIFIED.
De eigenaar heeft de winkelwagen/checkout visueel goedgekeurd en gevraagd verder te gaan. Dit is USER_REPORTED; geen onafhankelijke bevestiging van een echte betaling of mailketen.
Actieve codebranch blijft fix/product-cards-2026-10-14; geen themacode veranderd.

## Geverifieerde huidige koppeling

Via Google & YouTube → gekoppelde services is Merchant Center **5902025216** geopend, met Badkamercity en het bedoelde zakelijke Google-account. Historisch account5898992928 is geen huidige accountclaim.
Shopify-productsynchronisatie, landen/talen en verzendgegevens staan AAN. GA4G-H9YFB5TC6N is gekoppeld.
Geen account ontkoppeld/aangemaakt, productbron vervangen, sync herstart of nieuwe tag geplaatst.

## Merchant-status uit het account

| Bron/scope | Gelezen stand |
|---|---|
| Merchant-overzicht, alle marketingmethoden |11916producten;0Approved;24Not approved;overigeLimited;0Under review in de grafiek |
| Merchant-accountbrede setup/policy-pagina | No issues for you to fix |
| Prioritized fixes | Geen open geprioriteerde fixes |
| Alle andere productmeldingen |26uniekeartikelen,75regels over marketingbestemmingen |
| Pending initial review-detail |11.9K/100% impact;wachten tot3werkdagen;voorbeeldLagooG1104TC beperkt voor advertenties |
| Shopify Google-app |12017totaal;0goedgekeurd;194afgekeurd;11823wordtbeoordeeld |

De Shopify-app en Merchant tonen verschillende bronmomenten/scopes; de appcijfers niet verwarren met de rechtstreeks gelezen huidige Merchant-status.
Het grafieklabellimited en Pending initial review kunnen tegelijk voorkomen. Niet opnieuw koppelen of de volledige feed wijzigen als vermeende oplossing.
Geen nieuwe termijn vanaf vandaag bedacht; de effectieve start/einddatum van Googles beoordeling is niet vastgesteld.

## Volledige resterende probleemlijst

| Melding | Unieke artikelen | Vervolg |
|---|---:|---|
| Image not processed |11| Google zegt zelf dat verwerking opnieuw gebeurt binnen3dagen; huidige media READY in Shopify. Geen blinde herupload. HotbathM444AB heeft bestandsnaam M444_GN_2: juiste kleur nog inhoudelijk verifiëren, niet op alleen bestandsnaam als fout verklaren. |
| Image too small |9|8Wiesbaden+1Hotbath. Zes Wiesbaden-roosters hebben1000×83pixels, glijstang87×516, borstelsteel90×1034; HotbathSPOM1568 is348×245. Een lange zijde van1000is dus geen voldoende beeldhoogte. Andere media niet automatisch tot hoofdfoto maken: kunnen tekeningen/detailfoto’s zijn. |
| Image uses a single color |3|PorcelanosaMattWhite60×60/60×150enMarmiBlanco30×100; bestaande echte sfeer-/detailbeelden inhoudelijk toetsen voor Google, geen gegenereerde productvoorstelling. |
| Missing product image |1|HotbathSPOM1633BL, HB-titel; Shopifygeenbeeld bevestigd. Was buiten de eerdere644CSV-Hotbathscope. Eerst echte foto achterhalen; niet catalogusbreed opnieuw uitsluiten. |
| Additional text found |1|Wiesbaden33.4202; titel bevat “new design”. Oorzaak nog niet exact tot titel/anderattribuut herleid; geen ongerichte titelwijziging. |
| Adult-oriented content |1|JEE-O600-6906, alleen Dynamic remarketing; afbeelding/tekst inhoudelijk toetsen en daarna passende herbeoordeling. Geen categorie- of adult-vlag verzinnen. |

Som26, waarvan24notapproveden2eligiblelimited in de export.
Alle26product-ID’s/actueleShopify-media teruggelezen. [Gesaniteerde bronexport](2026-11-16-MERCHANT-ISSUES.csv), [identiteiten en media-afmetingen](2026-11-16-MERCHANT-ITEMS.json).
Geen van deze26producten in deze beurt gewijzigd of uit een kanaal verwijderd. De eerder geverifieerde644Hotbathuitsluitingen niet herhaald.

## Afgerond: NL-retourbeleid in Google

Vooraf stond in Merchant “Start by adding a policy” en ontbrak een retourbeleid.
De actuele websitepolicy https://badkamercity.nl/policies/refund-policy is volledig gelezen vóór invoer.
Nieuw beleid **9497359424 — Standard for Netherlands** opgeslagen; daarna via de bewaarde rij heropend en alle velden teruggelezen:

| Veld | Opgeslagen waarde |
|---|---|
| Land |Netherlands |
| Policy URL |https://badkamercity.nl/policies/refund-policy |
| Returns |Defective and non-defective products |
| Exchanges |Not accepted; conform retour + nieuwe bestelling op de website |
| Product condition |New and slightly used; geopende verpakking is op de website geen automatische uitsluiting |
| Return window |30days |
| Methods |In store,By mail; afgeven op afspraak uitgelegd in gekoppelde policy |
| Return label |Customer responsibility |
| Restocking fee |No cost |
| Refund processing |7days |
| Google-review |Nog apart te beoordelen; UI noemt maximaal10dagen, geen goedkeuring geclaimd |

30dagen betreft de meldtermijn;14dagen terugzenden na melding blijft in de gekoppelde websitepolicy. Geen44dagen ingevoerd.
€75is uitsluitend de bestaande standaardNL-palletretourraming, niet ingevuld als algemeen vast retourtarief.
Bewaarbare readback is verkregen door heropenen van de opgeslagen policy; het daarna geopende editvenster verlaten zonder tweede save.
Websitepolicy zelf ongewijzigd. Dit is geen nieuwe juridische audit of claim over alle uitzonderingsartikelen.

## Verzending en meten: grenzen

Eén NL-verzendservice Complete/All products/2–5businessdays teruggelezen; Shopify-verzendsynchronisatie staat aan.
In editview:1daghandling+1–4dagentransit,ma–vr; tijdzone niet zichtbaar ingevuld en Continue in deze viewdisabled. Venster geannuleerd; geen verzending gewijzigd. Tariefbedragen/palletdekking/uitzonderingen niet volledig opnieuw afgevinkt.

Native Google-appconversiemeting staat Aan. Eventkoppelingen teruggelezen: Afrekenen afgerond→Google Shopping App Purchase;begincheckout/addtocart/pageview/viewitem/search/addpaymentinfo hebben bestaande bestemmingen.
GA4-property563233763 is rechtstreeks geopend. E-commerce-rapport19oktober–15november2026 bevat ontvangen productweergave-/winkelwagengegevens; geen zelfstandige purchase-/value-/transaction_id-/ontdubbelingsproef. Deze periode bevat16november niet. Geen foutconclusie uit ontbreken van een aankoop; rapportvertraging en proeforder ontbreken als onafhankelijk bewijs.
Geen Google Ads-browserroute geprobeerd: eerdere expliciete browsertoegangsblokkade behouden. Geen campagne/budget/attributie-/privacyinstelling gewijzigd.

## Exact hervatpunt

**Eerst:** één bron-/beeldproef voorWiesbaden33.4218: huidige eerste foto1000×83pixels. Zoek een echte geschikte productfoto of een onderbouwde correcte beeldpresentatie; tweede beeld1156×608niet blind als packshot kiezen. Daarna de overige12concrete beeldproblemen afwerken.
11Image not processed apart laten verwerken. Tekstmelding/JEE-O-review en purchasevalidatie behouden hun eigen open status.
De Merchant-brede review niet als afgerond melden; dit is een externe beoordeling.
**Terugzetten retourpolicy:** indien nodig uitsluitend de nieuw gemaakte policy9497359424 corrigeren/verwijderen; oorspronkelijke situatie was geen policy. Geen bestaande shippingpolicy of websitepolicy terugzetten.
Geen actieve schrijver na overdracht.
