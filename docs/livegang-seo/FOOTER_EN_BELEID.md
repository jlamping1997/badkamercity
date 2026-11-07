# Eén footer en één beleidsbron

LAUNCH-02, 5 november 2026. Dit is het concrete uitvoeringsplan; geen nieuwe footer gebouwd en geen live footerwijziging uitgevoerd.

## Er bestaat al een kortere route

Alle normale paginatypen laden footer-group vanuit layout/theme.liquid. Binnen sections/footer.liquid wordt op de homepage, bij compact_homepage=true, de aparte snippet bc-home-footer gebruikt. Andere pagina's gebruiken de bestaande bcf-v3-footer.

Gebruik de bestaande standaardfooter op alle pagina's. Daarvoor hoeft geen nieuw componentsysteem te worden gebouwd. De centrale instelling en inhoud staan in **shopify/current/sections/footer-group.json** op de bestaande codebranch.

Beide renderers tonen al shop.policies. Zodra het juiste Shopify-retourbeleid is ingevuld en show_policy aanstaat, kan de footer de policy naast privacy tonen. Een aparte handmatig gedupliceerde retourbeleidslink/tekst is niet nodig.

## Eerst één inhoudsset kiezen

| Onderdeel | Afspraak |
| --- | --- |
| Klantenservice | Contact, bezorgen, retourbeleid, retourneren/koop ongedaan maken, voorwaarden; alleen echte openbare bestemmingen |
| Assortiment | Dezelfde bedoelde hoofdgroepen op alle pagina's; huidige homepage heeft meer hoofdingangen dan de zes standaardfooterblocks, dus dekking bewaren |
| Contact/verkoper | Eenmanszaak/Badkamercity.nl op Hengelolaan70; info@badkamercity.nl, KvK; eigen telefoon volgt later, geen Harry Suiker-nummer |
| Retouradres | Zichtenburglaan150 bij Harry Suiker, 2544EB 's-Gravenhage, duidelijk als retourontvangst; geen vrije inloop-/afhaalclaim |
| Beleid | shop.policies als primaire bron; geen losse tweede policyversie onderhouden |
| Retourfunctie | Bestaande veilige bc-returns-url-guard behouden; niet naar een verborgen of kapotte Page linken |
| Offerte | Bestaande bc-footer-quote-guard behouden; uploadfunctie niet onbedoeld activeren |
| Onbekende link | Niet vullen met #, nepbestemming of “binnenkort”; ontbrekende informatie als taak afronden |

## Uitvoering zodra gegevens compleet zijn

1. Lees opnieuw actuele MAIN en het bestaande concept. Tijdens LAUNCH-02 veranderde de eigenaarsrol van196227170570 naar **MAIN196238639370 — BadkamerCity - Re-Bel tegelkeuze**. Dat thema is dus geen schrijfbaar concept meer.
2. Gebruik de bestaande releasewerkwijze: een gecontroleerd ongepubliceerd concept vanaf de dan actuele MAIN; geen live filewrite, geen oude preview alsnog publiceren.
3. Zet compact_homepage uit en breng de categorie-/serviceblocks op de afgesproken volledige inhoud. Geen categorieën verliezen bij de simpele schakelaar.
4. Vul correcte contactgegevens; foutief/onbevestigd btw-id niet in de klanttekst zetten.
5. Vul het definitieve retourbeleid in de Shopify-policy, met bevestigd retouradres en kosten. Voorwaarden en verzending apart afmaken; de retourpolicy vervangt die niet.
6. Controleer homepage, categorie, gewone PDP, Sunshower, cart, Contact, Retour en policy: één footer, juiste links, geen dubbel privacy/retourbeleid.
7. Test mobiel en toetsenbord; pas daarna eigenaarreview/publicatie en publieke readback.

## Google kan dit lezen zodra het echt openbaar staat

De definitieve policy krijgt één openbare URL, bij voorkeur de Shopify-route **/policies/refund-policy**. Geen login, formulierinvulling, uitklapactie of PDF als enige toegang nodig om de tekst te lezen.

Controleer HTTP200, de echte zichtbare inhoud en een gewone footerlink. Laat in Merchant Center de NL-retourtermijn, methode, kosten, terugbetaling en eventuele geldige uitzonderingen aansluiten op dezelfde tekst. Een losse mooie HTML-pagina is geen bewijs dat Merchant juist is ingesteld.

[Retourconcept](retouren/RETOURBELEID_CONCEPT.md) · [Controles](CONTROLES.md) · [Bedrijfsgegevens](BEDRIJFSGEGEVENS.md)
