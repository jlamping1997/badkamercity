# ASSORT-01 — assortimentoverzicht

29 oktober 2026. Eigenaar heeft het desktop- en mobiele ontwerp goedgekeurd en opdracht gegeven het werkend uit te voeren op `/collections`.

## Stand

IMPLEMENTED_LOCAL / COPY_PROCESSING / BROWSER_QA_PENDING / NOT_PUBLISHED.
MAIN bij de verse read: 195915448586, de door eigenaar gepubliceerde header-/iconenfix. Kopie 195916628234 — BadkamerCity - Assortiment overzicht. Actieve branch fix/product-cards-2026-10-14. Begincheckpoint 29b927e9f21828f0fcee4a3c1bee50138aaa814b.
Deze opdracht volgt op de afgeronde FLASH-01-uitvoering. Publicatie blijft bij de eigenaar.

## Uitvoering

- Alleen standaard `/collections` vervangen; gewone categoriepagina's, merkenview en productpagina's behouden hun eigen templates.
- Tien hoofdafdelingen uit het actuele hoofdmenu. De bestaande negen illustratieve homepagefoto's hergebruikt; radiatorbeeld uit de bestaande collectie geoptimaliseerd. Afbeeldingen/titels per afdeling zijn via de editor te vervangen.
- Native links en details voor alle onderliggende menukeuzes. Op desktop als kolommen, op mobiel uitklapbaar. Essentiële links blijven zonder JavaScript bereikbaar.
- Aanvullende categorieën afzonderlijk onder Maak het compleet, configureerbaar met expliciete handles; geen wijziging van het hoofdmenu of collectie-/productlidmaatschappen.
- Meer categorieën toont gevulde collecties die niet al in de menustructuur staan. Paginering is voorzien voor groei boven 250 collecties. Dit is geen automatische uitbreiding van het hoofdmenu.
- Categoriezoeker filtert plaatselijk de zichtbare directory, ondersteunt onderliggende context en herstelt uitklapstaat na wissen; geen externe requests of analytics toegevoegd. De input verschijnt pas na controllerinitialisatie.
- Sunshower gebruikt de bestaande gepubliceerde merklanding en bestaande IR-illustratie. Porcelanosa linkt naar het bestaande merkassortiment; de hoogwaardige merkpagina blijft een apart toekomstproject.
- Porcelanosa-sfeerbeeld uit de Bottega-galerij van product 10687508807946, geverifieerd via actuele mediaread. Een algemene merk-/seriesfeerfoto, geen claim van een exacte kleur of set. Bron: https://cdn.shopify.com/s/files/1/0941/7959/0410/files/porcelanosa-kogros-ddc1308f5ff966874f46.jpg?v=1793208373 .
- Titel en metaomschrijving alleen op de standaard list-collections-route aangepast, met vertalingen. Bestaande canonicals/robots behouden; geen SEO-rankingsclaim.

## Bestanden en behoud

Nieuwe sectie bc-assortment, snippet bc-assortment-item en eigen CSS/JS. Template list-collections.json wijst de sectie toe. Twee extra WebP-assets. Locale-uitbreiding uitsluitend bc_assortment. Layout krijgt uitsluitend een routegebonden metadata-override. Actuele baselinebestanden en openbare menuboom staan naast dit document; geen klantgegevens.

build-config.py bouwt template en vertalingen vanuit de vastgelegde baseline; dit is geen importtool voor catalogusdata. Bij hergebruik eerst een verse baseline vastleggen, anders kan een latere vertaling verloren gaan.

## Controle tot nu toe

ThemeCheck R1 op zeven bestanden geslaagd. R3 inclusief metadata-layout geslaagd met één bestaande scheme_classes-waarschuwing. Geen Windowscontrole, fysieke telefoon of algemene prestatiemeting geclaimd.
De werkelijke desktop-/mobiele component-, zoek-, link- en kopiepariteitscontrole volgt na de Shopify-kopie. Het huidige document is een voortgangscheckpoint, geen vrijgave.

## Eerste gecontroleerde bestemmingen

De echte Porcelanosa-vendorpagina geopend: heading Porcelanosa en 337 producten. Er staat bestaande verkeerde kranenadviescontent onder die productlijst; vastgelegd als afzonderlijk vervolgonderzoek, niet aangepast binnen deze overzichtspagina.

## Terugzetten en vervolg

Voor review alleen de nieuwe conceptkopie gebruiken. Herstel template, layout en beide locales uit baseline om de functie uit te schakelen; nieuwe ongebruikte bestanden hoeven niet verwijderd. Geen volledige Git-root uploaden.
Exact volgende handeling: kopiepariteit voltooien, gerichte bestanden uploaden en de echte conceptweergave controleren.
