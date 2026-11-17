# Hotbath SPOM745 / SPOM700 — productinhoud en adviespagina

Status 17 november 2026: **LIVE / CONTENT_READBACK_VERIFIED / ADVICE_DESKTOP_VERIFIED**.

De bestaande onderdelenpagina’s en adviespagina zijn verbeterd met instructievideo’s, klachtvragen, leveringsinformatie en een overzichtelijk ontwerp. Daarna is de toepassing verbreed van HB009 naar brongecontroleerde HB007- en SDS1/SDS9-generaties.

Zie [COMPATIBILITY.md](COMPATIBILITY.md) voor de actuele modellenmapping, 84 extra verwijzingen naar SPOM745, het afzonderlijke HBCB7067-serviceblok, bronnen, validatie en herstel. HBCB7067 wordt niet als bevestigde SPOM745/SPOM700-toepassing verkocht; huidige Hotbath-instructies noemen 1603/1600.

## Pagina en ontwerp

[Live adviespagina](https://badkamercity.nl/pages/hotbath-thermostaat-draait-stroef), Page167264813322. Titel en URL behouden.
[page.html](page.html) bevat de actuele Page.body met scoped CSS binnen #bc-spom-guide.

- Twee kaarten met door eigenaar goedgekeurde bestaande productfoto’s en knoppen.
- Korte intro, vier ankerlinks, zesrijenmodellentabel met bouwperiodes.
- Montageblok en native stappenlijst; gereedschap wordt niet meegeleverd.
- Vijf native uitklapvragen en één technisch bronnenblok.
- Contactblok voor model-/generatiecontrole.
- Geen JavaScript, nieuwe fontprovider, nieuwe template of themafile.

Echte Chrome-desktop toont twee kaarten en de bredere tabel. Smalle CSS-viewport340px zonder horizontale tabel-/paginaoverloop gemeten; geen fysieke telefoonproef. Knoppencontrasten en de native stappenlijst zijn in de eerdere designronde gecontroleerd. De themapreviewtool kon de themafiles niet renderen; de controle liep rechtstreeks via de live pagina.

## Bestanden en herstel

- page-before.json: pagina vóór de eerdere designronde.
- compatibility-before.json: volledige contentback-up vóór de daaropvolgende modeluitbreiding.
- compatibility-update.json: bedoelde product-/paginawijzigingen en bronnen.
- compatibility-validation.json: readback van 85 serviceblokken en de onderdelen/pagina.
- COMPATIBILITY.md: actuele uitleg en grenzen.

Herstel gericht uit de bijbehorende back-up. Geen prijs, voorraad, media, varianten, kanaal of themafile aanpassen.

De eigenaarfoto van een verkalkt en schoon binnenwerk blijft een open taak in CONTENT-HB-SPOM-01. SEO-/rankingwinst, fysieke iPhone, checkout en Windows-lokale synchronisatie zijn niet getest. Branch fix/product-cards-2026-10-14 bevat deze versiebron; geen thema-release nodig.
