# Numerieke Hotbath-sets: gecontroleerde menu-indeling

Bronnen: volledige actuele Shopify-snapshot van 24 oktober 2026 en Hotbath Catalogus Editie18. Dit is een alleen-lezen analyse. Er zijn geen product- of themamutaties uitgevoerd.

De codes IBS-ACE1001 enzovoort en COBBER3001 enzovoort zijn niet teruggevonden in de doorzoekbare tekst van editie18. Daarom is geen universele fabrikantdecodeertabel voor deze nummerreeksen aangenomen. Iedere gekozen kleur, handdouche, douchekop en bevestiging is rechtstreeks uit de actuele producttitel bevestigd. De cijferblokken dienen alleen als aanvullende consistentiecontrole tegen het type uit de titel.

| Afzonderlijke familie | Artikelen | Keuzes |
|---|---:|---|
| ACE 2-weg thermostatische inbouwdoucheset |216|Kleur, hoofddouche, bevestiging hoofddouche, handdouche, handdouchehouder|
| ACE 2-weg inbouwdoucheset met mengkraan |216|Dezelfde vijf keuzevelden, gescheiden bediening/familie|
| ACE 3-weg inbouwdoucheset met Velvet hoofddouche |6|Alleen kleur; geen extra niet-beschreven maten verzonnen|
| Cobber glijstangsets |18|Kleur en staaf/ronde handdouche|
| Cobber Beam inbouwdoucheset met mengkraan |9|Alleen kleur|

Alle465 artikelen zijn ACTIVE, gepubliceerd, hebben exact één volledig opgehaalde variant en behoren nog niet tot een bestaande V2-groep. Alle keuzetupels zijn uniek. In alle vijf families zijn de vaste titeldelen gelijk na verwijdering van precies de beschreven SKU en keuzevelden. Dat geldt ook voor de twee ACE-families met vijf velden: kleur, hoofddouchemaat/Velvet, montage, handdouche en houder worden verwijderd; iedere overige titelafwijking blokkeert de familie. SPOM wordt uitgesloten wanneer het voorkomt in SKU, titel of handle, net als testartikelen en niet-gepubliceerde artikelen.

Het boek bevestigt het onderscheid tussen de ACE-bedieningen: AC129 is een inbouwmengkraan met tweewegomstel (gedrukt307/PDF309); AC009 en AC039 zijn thermostaten met respectievelijk twee- en drieweg stop/omstel (gedrukt308/PDF310). Dat is bronbevestiging van het functieverschil, geen bewijs dat iedere numerieke set exact dat onderdeel bevat. Daarom vermelden de gegevens expliciet `COMPONENT_AND_CONTROL_DISTINCTIONS_ONLY` als boekstatus.

Bij de 23cm-hoofddouche blijft de aanduiding Velvet behouden als keuzewaarde; deze wordt niet als een willekeurige diameter van hetzelfde douchekopmodel voorgesteld. Voor de ACE-handdouche wordt alleen 'Staafmodel' of '3 standen' getoond, omdat de huidige titels dat bevestigen; er wordt geen niet-bewezen materiaal of modelnummer toegevoegd.

Output `numeric_set_analysis.json` bevat standaard V2-groepen en afzonderlijke herkomst/statusregels. De status `TITLE_CONFIRMED_READY_FOR_PREVIEW` betekent een goed onderbouwd bestaand-productmenu op titelbasis. De records zijn niet automatisch gepubliceerd en vereisen dezelfde integratie- en browserchecks als andere nieuwe groepen.

Tien lokale controles testen onder andere de actuele465unieke keuzetupels, gescheiden kraanbediening, SPOM-uitsluiting, publicatie-gate, dubbele combinaties, bestaande groepslidmaatschappen en verborgen extra titelverschillen. Een synthetisch extra vast modelkenmerk in één ACE-artikel zorgt aantoonbaar voor REVIEW en het weglaten van de hele betreffende vijfkeuzegroep.
