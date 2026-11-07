# Kleine controles — bestellen, contact en retourneren

LAUNCH-02, 5 november 2026. We doen dezelfde korte proef onafhankelijk: Jackson voor de ervaring/werkelijke bedrijfsafhandeling, uitvoering voor artikel/bedragen/gegevens en technische werking. “Lijkt te werken” blijft USER_REPORTED tot de betreffende stappen echt zijn gecontroleerd.

## Bestellen: twee controles naast elkaar

Kies een normale kraan, een product met kleur/uitvoering/onderdeelkeuze en een tegel die per doos wordt verkocht. Geen echte bestelling of geldbetaling uitvoeren zonder het afgesproken testscenario. Zet de openbare winkel niet globaal in testbetaalmodus. Verwijder alleen eigen proefregels, nooit een bestaande winkelwagen.

| Controle | Waar letten we op? | Jackson | Uitvoering |
| --- | --- | --- | --- |
| Juiste artikel | Titel, merk, SKU, kleur en maat blijven dezelfde van product tot cart | OPEN | OPEN |
| Keuze wisselen | Andere uitvoering toont juiste foto/prijs; optionele onderdelen niet stil toegevoegd | OPEN | OPEN |
| Hoeveelheid | Aantal verhogen/verlagen/verwijderen geeft precies de bedoelde artikelen | OPEN | OPEN |
| Tegels | m²/calculator → hele dozen, juiste doosinhoud, doosprijs en totaal incl.btw | OPEN | OPEN |
| Voorraad/levering | Bestelbaar klopt; de juiste actuele levertijd reist mee | OPEN | OPEN |
| Winkelwagen | Juiste artikelregels, aantallen, kortingen en totaal; geen dubbele toevoeging | OPEN | OPEN |
| Verzendkosten | Afgesproken NL-testadres en producttype krijgen juiste kosten/opties, inclusief zware goederen | OPEN | OPEN |
| Mobiel | Keuzes, knoppen en checkout leesbaar/bedienbaar op telefoon | OPEN | OPEN |
| Checkout | Juiste klant-/adresgegevens en echte beschikbare betaalmethoden; fouten bruikbaar | OPEN | OPEN |
| Betaling en ordermail | Alleen afgesproken proef: één transactie/order, juiste bedragen, bevestiging bij klant én beheerder | OPEN | OPEN |
| Afronden | Eigen testregels weg; eventuele proeforder/terugbetaling als aparte geautoriseerde actie | OPEN | OPEN |

De latere FAB-04/COTTO-01-dossiers bevatten al specifieke winkelwagenproeven. Die worden hergebruikt met hun bronmoment, maar bewijzen geen volledige adresafhankelijke checkout, betaling of mobiele test.

## Klantcontact: wat bedoelen we met “ontvangst controleren”?

Een formulier kan op de website zeggen “verzonden” terwijl het bericht niet in de juiste mailbox aankomt. Daarom testen we de hele route, zonder echte klantgegevens in Git.

1. Jackson verstuurt vanaf een eigen bereikbaar testadres een kort bericht met herkenbaar onderwerp, bijvoorbeeld BC-CONTACT-PROEF met datum/tijd.
2. Controleer de succesmelding op de website.
3. Kijk in de bedoelde winkelmailbox, inclusief spam: klopt afzender/reply-to en is het hele bericht leesbaar?
4. Antwoord vanuit de winkelmail en controleer dat het antwoord het eigen testadres bereikt.
5. Noteer alleen datum/tijd, paginaroute, PASS/FAIL en eventuele fout; geen naam, e-mailadres of berichtinhoud in publieke Git.

Uitvoering controleert formulierroute, verplichte velden, foutmelding en afhandeling; Jackson bevestigt echte ontvangst/antwoord. Deze inzendingen zijn in LAUNCH-02 niet uitgevoerd.

## Retour/herroeping: afzonderlijke proef

1. Kies een duidelijk als proef gemarkeerde aankoopreferentie uit het afgesproken scenario.
2. Retour/herroepen moet zonder verplicht account, retourreden of toestemming bereikbaar zijn.
3. Test zonder bestelnummer; de aankoop moet ook op een andere heldere manier kunnen worden omschreven.
4. Controleer dat verzoek, producten en aantallen correct aankomen.
5. Toets de definitieve herroepingsstap en onmiddellijke bewaarbare bevestiging met aankoop, datum en tijd. Een succesmelding alleen sluit deze taak niet.
6. Jackson bevestigt de beheerdermail en een antwoord met correcte retourinstructies; geen label/refund stil automatisch aanmaken.
7. Test dat ongeldige invoer niet als succes wordt gemeld en dat de footerlinks op mobiel werken.

## Werkelijke ontvangstverwerking

Ontvangen → aankoop vinden → melding schriftelijk bevestigen → juiste adres/methode/kosten uitleggen → retourontvangst vastleggen → afhandeling/terugbetaling binnen de toepasselijke termijnen.

[Retourconcept](retouren/RETOURBELEID_CONCEPT.md) · [Footer/publicatie](FOOTER_EN_BELEID.md) · [Taken](TAKEN.md)
