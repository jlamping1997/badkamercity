# Verlanglijst: opslag, fouten en meerdere tabbladen

**28 oktober 2026 · DOC-03D.** Eigenaar van het opslagcontract; bediening en identity staan in [WISHLIST_IDENTITY](WISHLIST_IDENTITY.md), productverrijking en kooproute in [WISHLIST_RENDER_AND_ADD](WISHLIST_RENDER_AND_ADD.md). Bron: `assets/bc-wishlist.js` van MAIN 195818389770, tegen verse Shopify-MD5/grootte gecontroleerd. [Bewijs en 43 lokale cases](../../evidence/2026-10-28-wishlist/README.md). Geen echte bezoekersopslag gelezen of gewijzigd.

## Wat wordt bewaard?

Eén JSON-array onder `bc_wishlist_v1` in localStorage. Het is een selectie op deze browser/origin, geen Shopify-klantrecord, reservering of serverwishlist. De versie staat in de sleutel; er is geen object met een apart version-veld. Het thema maakt geen account- of apparaatsynchronisatie. Een custom domein en een andere origin delen daarom niet automatisch deze lijst; in deze ronde zijn geen echte domein-/accountovergangen getest.

| Veld | Normalisatie in :14–26 | Betekenis en grens |
| --- | --- | --- |
| handle | String, trim, lowercase; begint alfanumeriek, daarna alfanumeriek of `-`, maximaal 200 tekens | Productroute, geen bewezen huidige publicatie |
| variantId | Getrimde string van 5–20 cijfers | Exacte uitvoering; opslag gebruikt geen Number-conversie |
| title | String, eerste 180 tekens | Presentatiesnapshot; productread kan titel vervangen |
| image | String, eerste 800 tekens | Snapshot; renderer beoordeelt URL later afzonderlijk |
| source | Alleen sunshower/detail, anders card | Stuurt later de toegestane kooproute; geen voorraadwaarde |
| savedAt | Number of huidige tijd bij falsy/ongeldige conversie | Geen sorteer-, expiratie- of migratiemechanisme |

`load` (:29–35) parseert, normaliseert, verwijdert ongeldige entries en neemt de eerste 100 over. Een lege/ongeldige/niet-arraybron of leesexception geeft een lege geheugenlijst. De originele opslagbytes worden bij laden **niet** aangepast. Ook oudere timestamps blijven geldig. `MAX=100` begrenst geheugen en nieuwe toevoegingen, geen oorspronkelijke ruwe arraylengte of gegarandeerde unieke producttelling.

WL-02/06/08 bevestigen normalisatie, de limiet en kopieën vanuit `BCWishlist.list()`. WL-03/04/05/07 begrenzen de herstelclaim: kapotte JSON, een ander schema en leesweigering ogen leeg; duplicaten in een aangeleverde array blijven bestaan. Dat bewijst niet dat gewone hartjesbediening zulke duplicaten maakt. Er is geen actuele bezoekerdata onderzocht om frequentie of oorzaak vast te stellen.

## Schrijven is de commitgrens

`save(next)` (:38–48) doet eerst `localStorage.setItem`, daarna pas `items=next` en `notify()`. Bij een schrijfexception blijft de oude geheugenlijst staan, verschijnt een fouttoast en wordt geen succes-event verstuurd. WL-10 bevestigt dit met een expliciete geweigerde schrijfstub; echte browserquota/privacy-instellingen zijn niet getest.

Een gewone toggle bouwt `next` uit het huidige **paginageheugen**. Nieuwe entries komen vooraan; bestaande exacte identities worden allemaal verwijderd. Bij 100 entries wordt een nieuwe toevoeging geweigerd, verwijderen blijft mogelijk (WL-11). Een leesfout wordt niet als aparte onbekende opslagstaat bijgehouden. Ontwerp vóór een eventuele herstelwijziging of leeg en onleesbaar verschillend moeten worden behandeld; stil wissen is geen bestaande recoverygarantie.

`notify` (:179–183) synchroniseert hartjes/header, start indien aanwezig een nieuwe wishlistpaginarender en verstuurt op document `bc:wishlist-changed` met uitsluitend `{count}`. Het event bevat geen volledige productlijst, prijs, cartstatus of serverbevestiging. `list()` levert kopieën; `has(handle, variantId)` vergelijkt exacte strings. Externe callers moeten hun input zelf normaliseren.

## Synchronisatie tussen tabbladen

De window-storagehandler (:429–431) reageert op de eigen key én key=null, leest de huidige storage opnieuw en doet notify. Een andere key wordt genegeerd. Hij gebruikt niet `event.newValue` als waarheid. WL-21 bevestigt die route; WL-22 bevestigt dat twee opeenvolgende edits behouden blijven **wanneer het storage-event vóór de tweede edit is verwerkt**.

Het browsercontract dispatcht storagegebeurtenissen naar andere documenten op dezelfde origin; de schrijvende pagina doet hier zelf notify. Zie [MDN storage-event](https://developer.mozilla.org/en-US/docs/Web/API/Window/storage_event). De [HTML-standaard](https://html.spec.whatwg.org/multipage/webstorage.html#the-localstorage-attribute) waarschuwt dat auteurs geen locking tussen vensters mogen aannemen. Events zijn taken, geen atomaire transactie rond de applicatielijst.

## WISH-F01: een tweede tabblad kan een toevoeging verliezen

**VERIFIED_ISOLATED, P2-kandidaat voor verlies van een favoriete selectie.** WL-23 gebruikt twee echte wishlistclosures, ieder met eigen geheugen, en één synthetische gedeelde opslagmap. Eventbezorging wordt bewust uitgesteld:

| Stap | Tab A-geheugen | Tab B-geheugen | Gedeelde opslag |
| --- | --- | --- | --- |
| Beide geopend | leeg | leeg | leeg |
| A bewaart product A | A | leeg | A |
| B bewaart B vóór ontvangst event | A | B | B |
| Events later verwerkt | B | B | B |

Beide schrijfacties rapporteren succes. B berekent zijn volgende array uit verouderd paginageheugen en vervangt de hele opgeslagen array; A verdwijnt. Latere notificatie herstelt A niet. De replay bewijst deze codevolgorde, **geen native multitab-timing, huidig bezoekersincident of incidentfrequentie**. Geen echte browserlijst is verloren gegaan.

De kleinste richting is wijzigingen als een identity-operatie op actuele staat verwerken, in plaats van een volledige verouderde array opslaan. Alleen vlak vóór schrijven opnieuw lezen verkleint het venster, maar bewijst geen atomiciteit tussen gelijktijdige processen. Kies een expliciete conflictstrategie en toets eventuele serialisatie/fallback vóór implementatie; een extra storage-event of BroadcastChannel-bericht alleen is geen lock. Geen serveraccountwishlist introduceren zonder apart productbesluit.

## Onderhoud en acceptatie

Behoud bestaande opgeslagen selecties bij een schemawijziging; ontwerp expliciete migratie en een herstelpad. Geen keyrotatie of automatische clear om corrupte data te verbergen. Test leeg, 100 entries, duplicaten, oude timestamps, malformed JSON, schema-afwijking, lezen/schrijven geweigerd, key=null, gelijktijdig add/remove en twee verschillende variants van hetzelfde product. Sluit WISH-F01 pas met behoud van beide onafhankelijke intents onder een benoemd conflictbeleid en echte multitabregressie.

Opgeslagen winkelwagens en kortlevende keuzehandoffs hebben andere contracten; zie [opslagregister](../NAVIGATION_AND_STORAGE.md). Deze ronde heeft geen cart-restore uitgevoerd en certificeert die paden niet.
