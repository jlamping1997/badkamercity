# Configuratiemenu’s Hotbath: bron en overdracht

Deze export bevat bestaande, actieve en gepubliceerde artikelen uit de complete catalogussnapshot van 24 oktober 2026. Alle artikelen met `SPOM` in titel, handle of SKU zijn uitgesloten, net als testartikelen en onvolledige variantrecords. Er worden geen producten, prijzen, voorraad of niet bestaande combinaties aangemaakt.

## Exportcontract

- `config_groups.json.groups`: 8 V2-groepen, samen 1.536 artikelen.
- `numeric_set_analysis.json.groups`: afzonderlijke export van 5 V2-groepen, samen 465 artikelen. Deze groepen zijn geen onderdeel van `config_groups.json`.
- Beide `groups`-arrays kunnen worden toegevoegd aan de bestaande V2-dataset nadat overlap en bestaande groepslidmaatschappen over de totale uitrol zijn gecontroleerd.
- `config_mapping.json`: koppeling van SKU, product-ID, handle, groep, keuzen en bronverwijzingen.
- `config_review.json`: uitgesloten regels, drie inhoudelijke conflicten en familie-aantallen.
- `config_tests.json`: 13 geslaagde tests van de configuratieregels en publicatiebeveiligingen.
- `numeric_tests.json`: 10 geslaagde tests van de numerieke titelregels, publicatiebeveiligingen en verborgen vaste productverschillen.

Runtimeproducten gebruiken uitsluitend de bestaande velden `handle`, `url`, `title`, `sort_order` en `options`. De vijf optietoetsen zijn `kleur`, `breedte_diameter_hoofddouche`, `type_bevestiging_hoofddouche`, `type_handdouche` en `bevestiging_handdouche`. Kleuren staan als dropdown; de overige keuzen als knoppen. Keuzen met één waarde worden verborgen.

## Acht exacte boekfamilies

| Familie | Artikelen | Kleuren | Boekpagina | PDF-pagina |
| --- | ---: | ---: | ---: | ---: |
| IBS70 | 359 | 10 | 200 | 202 |
| IBS7009 | 360 | 10 | 199 | 201 |
| IBS20 | 194 | 6 | 202 | 204 |
| IBS20A | 192 | 6 | 203 | 205 |
| IBS1 | 71 | 2 | 286 | 288 |
| IBS1A | 72 | 2 | 287 | 289 |
| IBS12 | 144 | 4 | 288 | 290 |
| IBS12A | 144 | 4 | 289 | 291 |

Alle families blijven onderling gescheiden. Een A-variant of de IBS7009 wordt dus niet als kleurkeuze van het andere model behandeld. De IBS70 behoudt de groeps-ID van de bestaande pilot: `hotbath-cobber-ibs70-inbouw-doucheset`.

De kleurcodes en numerieke opties worden uitsluitend volgens de expliciete regels van de exacte familie gelezen. Zo betekenen opties 2 en 3 een verschillende plafondbuis en opties 4 en 5 een verschillende diameter. Tegenstrijdige, dubbele of onbekende suffixen blijven buiten de export. Alleen daadwerkelijk aanwezige SKU’s worden opgenomen; het keuzemenu mag beschikbare combinaties niet als volledig cartesisch product voorstellen.

Handdouches worden per familie omschreven. IBS70/IBS7009 gebruiken staaf versus rond. IBS20/20A/1/1A gebruiken staaf versus rond met drie standen en Ø10 cm. IBS12/12A gebruiken rond ABS Ø13 cm versus rond met drie standen Ø13 cm; het standaardmodel is daar geen staafmodel. Deze laatste interpretatie is onafhankelijk visueel gecontroleerd aan M360 en M376 in het boek.

51 verkorte titels uit IBS20/20A noemen niet alle vijf keuzen. Hun opties zijn afkomstig uit de exacte boekregels. Een expliciete tegenspraak in de titel wordt altijd geblokkeerd.

## Drie artikelen zonder nieuwe menukoppeling

| SKU | Conflict |
| --- | --- |
| IBS20AGN357 | Titel noemt een hoofddouche van 25 cm; de bevestigde SKU-optie 5 betekent 30 cm. |
| IBS20BBP | Titel noemt CB009BCP en een 2-weg stop/omstel; die componentkleur en regeling spreken de SKU/familie tegen. |
| IBS20BCP | Titel noemt een 2-weg stop/omstel; IBS20 is de familie met twee stopkranen. |

Deze artikelen horen ook buiten nieuwe fallbackkleurmenu’s te blijven totdat hun productinhoud is gecorrigeerd.

## Numerieke ACE- en Cobberartikelen

De 465 numerieke artikelen zijn onderverdeeld in twee Acegroepen van 216, een Ace Velvetgroep van 6, Cobber-glijstangsets van 18 en Cobber Beam-mengkraansets van 9. De opties staan letterlijk in de huidige producttitels. De catalogus onderbouwt het verschil tussen componenten en kraanbediening, maar bevat geen gevonden grammatica waarmee de numerieke artikelcodes zelf kunnen worden ontcijferd. Er wordt daarom geen dergelijke codeinterpretatie geclaimd. Het afzonderlijke numericrapport bevat de details.

Alle vijf numerieke families hebben daarnaast een harde controle op vaste titelkenmerken. Na het verwijderen van de exact aangeboden keuzen en de SKU moet de resttitel binnen een familie identiek zijn. Een synthetische extra watervalfunctie in één Aceartikel blokkeert bijvoorbeeld de hele betreffende groep; zo kan een onzichtbaar productverschil niet als kleurkeuze meekomen.

## Grenzen en behoud

Voor IBS40, IBS40A, IBS73 en IBS7 is in het beschikbare boek geen complete modelregel gevonden. De bron is daarmee onvoldoende om ontbrekende configuratievelden veilig aan te vullen. Veilige kleurkeuzen kunnen alleen apart worden opgesteld als de overige productkenmerken aantoonbaar gelijk blijven.

Bestaande groeps-ID’s worden alleen overgenomen als de bestaande menuvelden en productkeuzen volledig compatibel zijn. Verschillende IDs uit de huidige metafields en de bestaande JSON blijven beide zichtbaar en blokkeren de familie. Een onbekende groeps-ID, dubbele SKU of dubbele keuzentuple wordt niet stilzwijgend overschreven.

Deze bestanden zijn alleen voorbereiding en controle. Ze wijzigen de catalogus of een thema niet.
