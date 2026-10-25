# Code opschonen — 25 oktober 2026

IMPLEMENTED_LOCAL / PREVIEW_TEST_PENDING. Eigenaar heeft uitvoering gevraagd, behalve korte producttitels en bijbehorende filteroptimalisatie.

MAIN 195704848650 is vers bevestigd. Nieuwe UNPUBLISHED kopie 195706257674, naam BadkamerCity - code opschoning en gedeelde keuzes, is vóór wijzigingen 553/553 identiek bewezen. Nog geen publicatie of Admin-mutaties.

Implementatie: gemeenschappelijke eenmalige positieherstelling Hotbath/Sunshower; stabiele product-CSS uit Liquid naar herbruikbaar asset; prijs- en categorie-CSS eenmaal laden; Badkamermeubels-opmaak uit drie Admin-styleblokken naar het thema, met behoud van de originele gedeelde Admin-inhoud voor live/rollback; menudata per groep gegenereerd uit de oorspronkelijke bronnen met terugval. 656 bestanden bevatten data, geen aparte implementaties. Eén switcher blijft verantwoordelijk voor alle groepen.

Bewijs tot dit checkpoint: 10 positiegroepen, 11 switchergroepen, 13 koopgroepen, vier observerproeven, acht Sunshowergevallen; 656 exacte data- en Liquid-mappingvergelijkingen, meerdere groepen op één pagina, cache/fallback/retry, behoud van alle collectie-inhoud. Testtransport is gestubd; geen echte winkelwagen, betaling of Lighthouse-score.

Actieve branch fix/product-cards-2026-10-14. Root-theme wordt niet ongericht vervangen. Bestaande lokale wijzigingen onaangeroerd; Windows niet gecontroleerd. Dossier docs/code-cleanup/2026-10-25.

Volgende handeling: Shopify-validatie afronden, bestanden naar het concept plaatsen, vervolgens echte browsercontrole desktop/mobiel en exacte readback. Niet publiceren.
