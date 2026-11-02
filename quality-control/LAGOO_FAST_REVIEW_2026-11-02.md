# QC-06 — Lagoo: foto en kleur, direct verder

2 november 2026. Op expliciet verzoek opent dezelfde privétool standaard in een eenvoudige Lagoo-fotocontrole. Geen merkkeuze, ronde-start, PDF-panelen of algemene statistieken in deze weergave. De verwachte kleur staat als groot hoofdelement boven één grote foto, letterlijk uit de kleurvariant die ook in de producttitel staat. Zonder kleur staat er Geen kleur opgegeven; geen verzonnen kleur of SKU als kleur.

Ja/Nee/Twijfel worden door de bestaande eigenaargebonden review-API opgeslagen. Pas na bevestiging verschijnt de volgende SKU. Bij opslagfout blijft dezelfde kaart staan met retry. De startselectie bevat alle nog te beoordelen Lagoo-hoofdfoto's in bronvolgorde, zonder 25/50-kaartenstart. SKU en kaartpositie staan klein onder de kleur. Afgekeurde varianten blijven per SKU, geen oordeel doorgeven aan andere kleuren.

Andere foto toont de volgende kandidaat groot; de vorige-pijl gaat terug. De kandidaat wordt pas goedgekeurd met Ja; de bestaande selectedImage blijft gekoppeld aan precies die SKU. Ja wacht op de foto en de volledige kandidaatkoppeling. Een reeds geselecteerde thumbnail nogmaals kiezen blokkeert de kaart niet. Terug herstelt het vorige oordeel; Later slaat over; Technische tekening blijft apart beschikbaar. Alle foto's en producttitel zijn inklapbaar. Notities die al bestonden blijven behouden. Uitgebreid opent de bestaande QC voor ontbrekende data, PDF's, notities, checkpoints en andere merken; Lagoo snelcontrole keert terug naar de eenvoudige Lagoo-selectie. Bestaande producten, bestanden, reviews, checkpoints en schema blijven intact; geen Shopify-mutaties in QC-06.

## Controle

TypeScript PASS; bestaande30SQLite/API-groepen en13Lagoo-groepen PASS; zes gerenderde React-componentcontracten PASS (exacte kleuren voor alle gefotografeerde varianten met kleur, directe beslissingen, opslag/login/laadguards, zichtbare gekozen kandidaat, ontbrekende kleur, herstelpad). Productiebuild PASS. Testschrijfacties uitsluitend tijdelijke SQLite. Geen nieuwe browser-/touch-/telefoon-/hosted visitor-schrijfproef: preview gaf eerder connection refused en error-tabbeleid; status nog dezelfde infrastructuur, geen omweg of onbewezen herstel. React-markupcontrole is geen CSS-/telefoonbewijs.

## Volgende handeling en terugval

Eigenaar herlaadt de bestaande privélink en controleert achtereenvolgens een chroom- en kopervariant met Ja/Nee/Twijfel en zo nodig Andere foto. Vorige Sites-versie6 blijft terugval. Server-API/catalogus/D1-schema onveranderd; geen opslagmigratie of reviewreset.

## Publicatie

Sites-versie7 succeeded, broncommit e21a5308e2d4867fc702a0bd73d13b8ec7de6177; deployment appgdep_6ae897e9677c81918bd7fe9efee75b7f. Dezelfde authclient en volledig toegangsbeleid. Bounded native24reviewrijen+1checkpoint inhoudelijk identiek vóór/na; geen testschrijfactie naar productie.
