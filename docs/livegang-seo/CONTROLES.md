# Gerichte controles — bestellen, contact, retouren en meting

**Stand: 8 november 2026 — DOC-LIVE-01.** [Gedateerd auditbewijs](../audits/2026-11-08/README.md). Een status geldt alleen voor de beschreven stap. “Lijkt te werken” blijft USER_REPORTED tot de betreffende werking echt is gecontroleerd.

## Al uitgevoerd en nog open

| Controle | Bewijs 8 november | Nog nodig |
| --- | --- | --- |
| Publieke routes | 364 serverresponses en metadata-/footercontrole | Geen vervanging voor interactieve bediening |
| Zoeken en filteren desktop | Eerdere browserproef: Wiesbaden zoeken; Wastafelkranen Inbouw + Chroom | Andere relevante keuze-/productrenderers en telefoon |
| Gewone kraan / cart | Wiesbaden Ribbd SKU 29.5330 €245; twee stuks €490, gastcheckout bereikbaar; eigen testcart opgeruimd | Adres-/verzendquote, betaling en mail |
| Tegelprijs / doos | RR6001: 1,44 m² voor €99,29; RR1001: 2 m² €159,90; VP8002: 1,28 m² €102,34, serverweergave | Dynamische calculator, hele-dozenafronding en gekozen aantal tot checkout gericht testen |
| Cookiekeuzes | Accepteren, weigeren en heropenen als UI bedienbaar | Werkelijk opslag-/netwerk-/taggedrag bij iedere keuze |
| GA4 | G-H9YFB5TC6N in appconfig; eigenaar meldt Realtime | Events, value/currency, purchase, ontdubbeling en consent |
| Retourinformatie | Live policy + leeg modelformulier volledig gelezen | Finale online herroepingsstap, directe klantbevestiging en mailboxbewijs |
| Contact / retourmail | Formulieren/POST-route aanwezig; niets ingezonden in de audit | Werkelijke ontvangst, reply-to, spam en antwoord |
| Betaling / ordermail | Niet getest | Afgesproken proef met passende betalingsmethode |
| Mobiel / snelheid | Geen volledige echte telefoontest of nieuwe prestatiemeting | Touch, keuzes, footer, cart, checkout en meetrapport |

FAB-04/COTTO-01 en het afzonderlijke filterdossier hebben hun eigen gedateerde tests. Hergebruik passend bewijs zonder er een volledige actuele checkout-/mobielvrijgave van te maken.

## Bestelproef voor Jackson en uitvoering

Kies een normale kraan, een product met kleur/onderdeelkeuze en een tegel per doos. Jackson beoordeelt ervaring en werkelijke bedrijfsafhandeling; uitvoering controleert artikel, bedragen en technische gegevens. Geen echte klantdata in Git. Geen betaling/proeforder zonder overeengekomen scenario; geen globale testbetaalmodus in de openbare winkel.

| Stap | Acceptatie |
| --- | --- |
| Artikel / uitvoering | Titel, merk, SKU, kleur, maat en inbegrepen onderdelen blijven correct van product tot checkout |
| Keuze / aantal | Juiste foto/prijs na wisselen; geen stil toegevoegde onderdelen of dubbele regels; verhogen/verlagen/verwijderen klopt |
| Tegels | Hele dozen, doosinhoud, m², doosprijs en totaal incl. btw; kaart/PDP/cart/checkout blijven dezelfde koopbare eenheid |
| Levering | Bron voor bestelbaarheid/levertijd; pakket én pallet op representatieve NL-bestemmingen; één locatie zonder rates onderzoeken |
| Checkout | Gasttoegang, validatie en daadwerkelijk aangeboden betaalmiddelen; niet uit ontbrekende API-scope afleiden |
| Betaling / mail | Eén overeengekomen transactie/order met juiste bedragen; bevestiging bij klant én beheerder; eventuele refund apart |
| Mobiel | Touch, knoppen, foutmeldingen, keuzevelden en checkout leesbaar/bedienbaar op echte telefoon |
| Opruimen | Alleen eigen proefregels verwijderen; status van eventuele proeforder/terugbetaling vastleggen |

## Contactmail: hele route controleren

1. Verstuur vanaf een eigen bereikbaar testadres een herkenbaar proefbericht via de contactpagina.
2. Controleer de paginasuccesmelding.
3. Controleer ontvangst in de bedoelde info@-mailbox én spam: afzender, reply-to en volledige velden.
4. Antwoord vanuit de winkelmail en controleer aankomst op het eigen testadres.
5. Noteer alleen datum/tijd, route en PASS/FAIL met foutomschrijving. Geen testmailadres, naam, berichtinhoud of ordergegevens in publieke Git.

De audit heeft geen formulier ingezonden. Een werkend mailto-linkje of succesmelding sluit deze proef niet af.

## Herroeping: afzonderlijke functie- en mailproef

1. Gebruik een als proef gemarkeerde aankoopreferentie in het afgesproken scenario. Toegang zonder account, verplichte retourreden of voorafgaande toestemming.
2. Test ook zonder bestelnummer; de aankoop moet op een andere duidelijke manier kunnen worden omschreven.
3. Controleer een toegankelijke herroepingsfunctie, heldere definitieve stap en correcte aankoop/producten/aantallen.
4. Controleer de onmiddellijke bewaarbare klantbevestiging met aankoop, datum en tijd. Het live modelformulier en een native contact-POST bewijzen dit niet.
5. Jackson bevestigt beheerdermail en antwoord met juiste retourinstructies. Geen betaald label, afhaling of refund stil aanmaken.
6. Controleer validatiefouten, toetsenbord/focus en mobiele footer-/functiebediening.

## Meetproef na juiste toestemming

Test toestaan, weigeren en intrekken/heropenen technisch, vervolgens view_item, add_to_cart en begin_checkout. Controleer purchase pas bij de overeengekomen bestelproef: één transactie, juiste variant/aantal, value/currency en transaction_id. Een herladen bevestigingspagina mag geen dubbele omzet geven. Geen e-mail, telefoon, adres of vrije formuliertekst in analytics/logs opnemen.

Ontvangen retour → aankoop vinden → melding schriftelijk bevestigen → adres/methode/kosten uitleggen → ontvangst vastleggen → tijdige passende afhandeling/terugbetaling. De termijn voor spijtretour en rechten bij gebreken apart houden.

[Actueel retourbeleid](https://badkamercity.nl/policies/refund-policy) · [Footer en beleid](FOOTER_EN_BELEID.md) · [Metingen](google/METINGEN.md) · [Taken](TAKEN.md)
