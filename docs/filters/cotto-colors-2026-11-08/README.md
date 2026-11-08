# Cottoceramix — basiskleuren per serie

8 november 2026. **PUBLIC_MAPPING_OBSERVED; Bone-aanvulling voorbereid.**

De eigenaar wil duidelijke basiskleuren en heeft zelfstandige indeling op basis van productbeelden toegestaan. Deze batch bevat 207 beoordeelde serie/kleurcombinaties (202 unieke sleutels na normalisatie). De zekerheid per vastgelegde keuze is minimaal 0,76. De indelingen zijn visuele afleidingen; ze worden niet als afzonderlijk door de eigenaar bevestigde kleuren opgeslagen.

## Resultaat van de voorbereiding

De volledige private tegelmeting van 3.496 producten is voor en na de patch vergeleken. Van de 3.159 Cottoceramix-tegels veranderen exact 353 producten: 315 gaan vanuit Overige kleuren naar een basiskleur en 38 bestaande indelingen worden gecorrigeerd. Overige kleuren daalt van 414 naar 99. Daarmee hebben 2.499 producten een bruikbare basiskleur. De 561 producten zonder kleurbron blijven ontbreken; ze worden in deze batch niet vanuit titels ingevuld.

| Voorbeeld | Nieuwe afgeleide filterkleur |
| --- | --- |
| Neri / Silver Mist | Grijs |
| Evoke of Fan / Clear | Beige |
| Casablanca of Fan / Ash | Beige |
| Cool of Joyful / Ash | Grijs |
| Funky / Seaport | Blauw |
| Funky / Mintwood | Groen |
| Maris / Earth Haze | Beige |
| Marble Line / Gold Brillo of Gold Mate | Wit en Beige |

Bronnen zijn gekoppelde productstalen, aangevuld met officiële Cotto- en fabrikantbronnen. De exacte scope, foto-URL, voorbeeldproductlink en onderbouwing staan in `rules.json`. Eenzelfde handelsnaam wordt bewust per serie beoordeeld. Alle bronkleuren en specificaties blijven in Shopify en in het exacte indexveld behouden.

## Technische grenzen en controle

De regel werkt uitsluitend voor merk Cottoceramix, een bekende tegelcollectie, één expliciet serieveld en een exacte genormaliseerde bronkleur. Bestaande eigenaarregels houden voorrang. Er is geen algemene titelafleiding, merkoverschrijdende kleurregel of aanpassing aan het Cottoceramix-categorieprofiel.

**50 lokale tests geslaagd**, met echte private worker-, API- en catalogusfixtures; geen overgeslagen integratietests. Alle overige productvelden blijven gelijk, evenals de 337 niet-Cotto-tegels, 47 producten onder bestaande eigenaarregels, alle 27 Acero-tegels en alle 132 formaatcodes. De volledige API-bron blijft byte voor byte gelijk. Standalone ASCII-transport, hashcontrole, herhaalbeveiliging, back-up, slot, staging, timerafhandeling en herstel zijn gecontroleerd. Zie `verification.json` voor aggregate meetresultaten.

De twee live Shopify-steekproeven bij ontbrekende bronkleuren (Ager-4 Blue en Fayenza Belt Royal Green) hebben ook in complete_specificaties geen kleur en geen bc_filters.kleur. Dat is geen volledige actuele broncontrole van alle 561 producten. Het live Cottoceramix-profiel bevestigt 82,24% kleurvelddekking; dit omvat ook Overige kleuren.

## Installatie en volgende handeling

Code staat op de bestaande actieve branch onder `scripts/filter-sync/simplification/cotto-colors/`. Gebruik de vastgepinde `repair_cotto_colors.py` met de SHA256 uit `cotto-color-release.json`. Alleen de exact beoordeelde Acero-worker met SHA256 `3c6dd21f50081f4ad8d770194dc35a97c101a09910dd8892403e51b93f1495eb` en de bestaande API worden geaccepteerd. Geen oudere installer herhalen.

De installer gebruikt de bestaande volledige Shopify-export en gecontroleerde indexactivatie. De actieve timer wordt gepauzeerd en er wordt een private back-up gemaakt. Alle bestaande controles en een nieuwe Cotto-controle moeten slagen. Daarna wordt de permanente worker geïnstalleerd en de eerder actieve timer hervat. Bij een fout wordt uitsluitend de eigen wijziging hersteld. Er zijn geen Shopify-productmutaties of themawijzigingen nodig.

Nieuwe vlag: `cotto_visual_colors_v1`, naast de vier bestaande vlaggen. Het resultaat meldt `cotto_visual_color_products`; op de huidige fixture zijn dat 353 producten. De exacte oorspronkelijke fabrikantkleur blijft behouden. Workerdoel SHA256 `cc13abd05c87a490bf06d0a7358ef36bc700edc0a736a48714d704df62f8dcc2`; API blijft `3a7701134be7ac55b0a83436ceb16ebb19ac0a88aba17c283490f90047f02094`.

Serverstaging, nieuwe activatie, publieke nacontrole, browserproef en toekomstige automatische verversing zijn **nog niet uitgevoerd** voor deze batch. De bestaande Acero-release blijft de laatst bewezen liveversie. Het ontbrekende tegelformaatfilter op het Cottoceramix-merkprofiel blijft apart vervolgwerk.

**Eén volgende handeling:** voer het nieuwe vastgepinde Bone-installatieblok uit; de oorspronkelijke Cotto-installer niet herhalen. Zie de [Bone-aanvulling](../bone-correction-2026-11-08/README.md).

## Latere meting en eigenaarcorrectie: Bone

De publieke generatie `bc_sync_20261108t164313_f87c29` geeft Cotto Overige 99, Silver Mist met Grijs 11 en Clear met Beige twee. Dit past bij de voorbereide Cotto-indelingen. Het oorspronkelijke installatieverslag en de workerbron zijn niet teruggelezen, dus deze waarneming is geen serverhash- of volledige activeringsbevestiging. De nieuwste eigenaarcorrectie is Bone → Beige, inclusief de oudere Malaga-uitzondering. Daarvoor staat een afzonderlijke, geteste upgrade klaar; alle 207 oorspronkelijke Cotto-regels blijven behouden. Gebruik voortaan het [Bone-dossier](../bone-correction-2026-11-08/README.md). Het compacte overzicht bevat nu 208 Cotto-kaarten.
