# Sunshower-blog — ontwerpvoorstel, 23 oktober 2026

**PREVIEW_READY / DESKTOP_VERIFIED.** De bestaande gepubliceerde blog krijgt een nieuwe opmaak in UNPUBLISHED **195611197706 — BadkamerCity - Sunshower eerste wissel 23 okt**. MAIN **195611492618** blijft 512/512 ongewijzigd. De bloginhoud is exact behouden.

## Gedrag

- Bestaande BadkamerCity-kleuren #0b3049 en #37d7ef, overgenomen bestaande Sunshower-beelden, duidelijke ONE/PLUS-labels.
- Ruime introductie, leestijd, zes ankerlinks, rustige leesblokken en semantische vergelijkingstabel.
- Desktop inhoudsopgave blijft in beeld; smalle schermen krijgen via CSS een native details-inhoudsopgave.
- Originele article.content is de bron. Geen gekopieerde productclaims in de template. De huidige eenvoudige h2's maken inhoudsopgave en secties mogelijk.
- Originele bronverwijzingen en uv-aandachtspunten blijven zichtbaar. Article structured data blijft aanwezig.
- Geen nieuwe JavaScript- of CSS-bibliotheek. Afbeeldingen gebruiken Shopify-responsive image_tag, expliciete maten en eager loading bovenaan.
- Default article.json gebruikt bc-advice-article. Er bestaat nu één artikel; toekomstige artikelen krijgen dezelfde basis, Sunshower-beelden alleen met de tag Sunshower.
- De bloglink op pages/sunshower en de eerdere productswitch-scrollcorrectie zijn behouden.

## Bestanden

after/ bevat de vijf exact teruggelezen themabestanden. before/ bevat de drie overschreven bestanden vóór deze ontwerptaak. Nieuwe sectie en ongebruikte alias kunnen bij terugzetten blijven staan zonder effect op de default article-route.

## Verificatie

Shopify Toolkit Theme Check revisie 3: alle vier productie-ontwerpbestanden SUCCESS; officiële gebundelde schemafallback na timeout van de externe schema-update. Alias revisie 2 eveneens SUCCESS. Admin-readback artikeltekst exact. Preview met cookiebehoud: HTTP200, thema195611197706, één H1, zes secties, geen Liquid-fout of ontbrekende vertaling. Openbare pagina blijft thema195611492618 en HTTP200.

Echte cloudbrowser 1363×936: vormgeving, geladen beelden, geen horizontale artikeloverflow, klik naar de vergelijking en volledige artikelstructuur gecontroleerd. **Fysieke mobiel en smalle responsive viewport NOT_TESTED**: Shopify weigerde embedding van de tijdelijke iframe-test. Geen Core Web Vitals, checkout of Google-rankings gemeten.

## Tijdelijke test en veilige afronding

Een tijdelijke article.bc-advice-qa.liquid met 320/390px-iframes werkte niet door de embeddingbeperking. De connector weigerde themeFilesDelete vanuit zijn beleid dat theme-verwijderingen blokkeert. Niet via ander transport herhaald. Het bestand is vervolgens veilig vervangen door uitsluitend {% section 'bc-advice-article' %}; geen iframe, script of automatische navigatie. Het is niet toegewezen aan een artikel en de normale blogroute gebruikt article.json. De eigenaar kan dit ongebruikte alternatief later optioneel in Shopify Admin verwijderen.

## Terugzetten / volgende stap

Herstel alleen before/templates/article.json en de twee before/locales-bestanden in hetzelfde nog UNPUBLISHED thema, na verse controle van rollen en eventuele latere taalwijzigingen. Geen volledige oude snapshot pushen. Bronartikel, landingtemplate en Sunshower-scrollasset hoeven niet teruggezet te worden.

**Exact volgende handeling:** eigenaar bekijkt de blog via de voorvertoning van thema195611197706, controleert hem op de telefoon en publiceert het concept als het akkoord is. Dit maakt tegelijk de eerder voorbereide scrollcorrectie en bloglink zichtbaar. Controleer vóór publicatie opnieuw de actuele themarollen en verschillen.
