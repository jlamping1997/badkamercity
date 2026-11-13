# Wiesbaden online-first — nieuwe voortgang 21 oktober 2026

**VERIFIED SHOPIFY/ONLINE STORE: 37 aanvullende SKU's publiek beschikbaar.**
Sinds het eerdere checkpoint met 24 artikelen zijn 35 reeds in Shopify aangemaakte, maar niet op Online Store gepubliceerde artikelen gevonden. Na actuele Shopify-preflight zijn ze door deze sessie expliciet gepubliceerd; daarna zijn ze alle 35 onafhankelijk teruggelezen. Daarnaast zijn 2 extra artikelen aangemaakt en gepubliceerd: 41.3686 en 41.3524. **Totaal nieuwe publicaties boven het vorige checkpoint: 37.**

**Actieve Wiesbaden-producten:** 2.265 oorspronkelijk + 24 uit eerste ronde + 35 alsnog gepubliceerd + 2 nieuwe = **2.326 ACTIVE**, exact gemeten. Dit is niet hetzelfde als 2.326 aantoonbaar publiek gepubliceerde artikelen; 61 nieuwe bronartikelen zijn wél expliciet gepubliceerd.

**Voortgang bron-only groep van 217:** 61 nieuwe SKU's gepubliceerd, 128 prijshoudende nieuwe SKU's nog niet gepubliceerd, 28 prijsloze nieuwe SKU's apart in de controlelijst. De eerdere 106 bestaande quarantaines staan als product online en zijn niet gearchiveerd.

**35 succesvol gepubliceerd (bestonden al in Shopify, waren eerst niet publiek):**
20.2850, 20.2853, 20.2854, 20.3405, 20.3406, 20.3407, 20.3408, 20.3409, 20.3417, 20.3418, 20.3419, 20.3446, 20.3850, 20.3853, 20.3854, 20.3997, 20.3998, 36.4031, 36.4032, 38.4048, 38.4049, 38.4050, 38.4051, 38.4052, 38.4053, 38.4054, 38.4101, 38.6109, 41.3556, 41.3559, 41.3572, 41.3635, 41.3658, 41.3665, 41.3691.

**2 aangemaakt en gepubliceerd in deze sessie:** 41.3686 (Elara Smart WiFi, €415 incl. btw), 41.3524 (Elara bevestigingsset mat zwart, €29,95 incl. btw). Beide READY fabrikantafbeelding en onlineStoreUrl. Drie overige pogingen (20.3447, 41.3676, 41.3523) zijn door de connector-veiligheidscontrole geblokkeerd en niet aangemaakt; laat ze in de niet-gepubliceerde queue. Er is niet via een omweg geprobeerd de geblokkeerde writes toch uit te voeren.

**Kwaliteit:** 37/37 actuele Shopify Admin-readback: ACTIVE, correct variant-SKU, positieve leveranciersadviesprijs als Shopify winkelprijs inclusief btw, tracking uit, minimaal één afbeelding READY, relevante collectie en isPublished via Online Store-publicatie. Vijf publieke PDP's aanvullend gecontroleerd op prijs, afbeelding en inhoud. Parent-collectie 'badkamermeubels' voor zeven onderkasten kon niet worden toegevoegd wegens connector-veiligheidsblokkade; hoofdcollectie losse-onderkasten en openbare URL zijn wel correct. Geen andere parent-mutatie voor deze zeven herproberen via alternatieve route.

**Openstaande technische stap:** De originele 24-productenregistratie en 165-SKU-queue bevatten nog de stand vóór dit checkpoint. Gebruik deze correctie en herbereken uit de huidige Shopify-readbacks alvorens nieuwe SKU's aan te maken. Actualisatie van die twee grote JSON-bestanden mislukte door connector-veiligheidscontrole. Nieuwe prijs-/voorraad-/SEO-/Typesense-massamutaties niet uitgevoerd.

**Volgende uitvoeractie:** pak een nieuwe gecontroleerde groep uit de **128 ongepubliceerde bron-SKU's** en sla alle 61 reeds gepubliceerde bron-SKU's, 28 zonder positieve prijs en 106 review-only bestaande artikelen over. Documenteer eerst nieuwe 37 in de centrale JSON's wanneer GitHub-writes daarvoor weer beschikbaar zijn.
