# Sunshower: basisblog en koppeling

De eigenaar vroeg om een eenvoudige blog die meteen online staat, met optimalisatie in een volgende ronde. De blog is daadwerkelijk gepubliceerd op https://badkamercity.nl/blogs/nieuws/sunshower-infrarood-of-uv .

## Inhoud en bronnen

Auteur: BadkamerCity. Titel: Sunshower: alleen infrarood of ook uv? De blog legt de functies en ONE/PLUS uit, vergelijkt beide series, benoemt gebruiksvoorwaarden en linkt terug naar de configurators. Productinformatie komt van de fabrikant; algemene uv-informatie is gecontroleerd bij de WHO. Geen verzonnen resultaten, gezondheidsgaranties, prijzen of reviews. Titel/tekst/bronlinks en Shopify-identiteit staan in article.json; article.html bevat de gepubliceerde HTML.

## Koppeling naar de blog

De custom Sunshower-landing rendert page.body niet. Daarom is in het bestaande UNPUBLISHED scrollconcept195611197706 onderaan één native rich-text-sectie toegevoegd aan templates/page.bc-sunshower.json. Het blok gebruikt bestaande thema-opmaak en heeft één knop naar de blog. Geen nieuwe Liquid/CSS/JS, geen nieuwe afbeeldingen. Het verbeterde scrollscript is exact behouden. page.bc-sunshower.before.json en page.bc-sunshower.after.json zijn de exacte herstel-/productie-inhoud van deze template.

## Bewezen controles

- Blog Admin-publicatie en volledige inhoud teruggelezen; alleen Shopify-witruimtenormalisatie.
- Blog publiek HTTP200, eigen canonical, één H1, inhoud aanwezig, geen Liquid-fout.
- Doelpreview: 512 bestanden; ten opzichte van de bestaande scrollpreview alleen templates/page.bc-sunshower.json gewijzigd; overige511 gelijk.
- Productie-template exact teruggelezen; preview-HTTP200 bevestigt theme195611197706/UNPUBLISHED, één klikbare bloglink met tekst Lees de keuzehulp, één H1 en geen Liquid-fout.
- MAIN195611492618:512/512 bestanden ongewijzigd tijdens koppeling. De uitvoerder heeft geen thema gepubliceerd.
- Visuele browser- en fysieke mobiele check NOT_TESTED. Lokale Playwright had geen Chromium. De eerdere afzonderlijke scrolltests zijn niet opnieuw gedraaid.

## Rollen en veiligheidsgrens

De tijdens deze sessie gemaakte identieke kopie195611492618 werd tussentijds MAIN. Een daarop volgende bestandsschrijfactie werd correct geblokkeerd; geen andere transportweg gebruikt. De uiteindelijke koppeling staat in het bestaande, aantoonbaar UNPUBLISHED actieve scrollconcept195611197706. Oude tijdelijke locale-wijzigingen zijn teruggezet; uiteindelijke wijziging is alleen de genoemde template. Laatste rollen en checksums staan in article.json.

## Volgende handeling

De eigenaar beoordeelt https://badkamercity.nl/pages/sunshower?preview_theme_id=195611197706 en publiceert BadkamerCity - Sunshower eerste wissel 23 okt (195611197706). Daarna de openbare landing en MAIN opnieuw lezen. De blog is al publiek toegankelijk. Controleer actuele rollen opnieuw als er intussen in een andere sessie aan thema's wordt gewerkt.

## Terugzetten

Voor publicatie: herstel alleen templates/page.bc-sunshower.json met page.bc-sunshower.before.json in het UNPUBLISHED concept; behoud het verbeterde scrollscript. De blog kan afzonderlijk via Shopify als ongepubliceerd worden ingesteld. Na eventuele thema-publicatie gelden opnieuw de bestaande release-/toestemmingsregels. Geen product-, prijs-, voorraad- of indexmutaties.
