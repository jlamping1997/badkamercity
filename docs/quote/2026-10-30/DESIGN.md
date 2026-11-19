# Offertepagina — eenvoudiger ontwerp, 30 oktober 2026

Op verzoek alleen de presentatie vereenvoudigd. Eén gecentreerde kop, korte introductie en één witte uploadkaart. Stappen en losse informatieblokken vervangen door de native uitklapregel “Hoe werkt de laagsteprijsgarantie?”. Mobiel kleinere kop en minder ruimte. Jotform-kop “Offerte uploaden”, herhaalde introductie verwijderd, compactere velden en brede lichtblauwe verzendknop. CSS in jotform-design.css.

Formuliervelden, verplichtingen, keuzemogelijkheden, uploadlimieten, notificatieadres en privacyinstellingen niet gewijzigd. Geen nieuwe testinzending of e-mail verzonden. De eerdere integratietest blijft afzonderlijk beschreven in INTEGRATION.md. Klantmail/verificatie en klantactivatie blijven open/uit.

Vier themebestanden aangepast in UNPUBLISHED195916628234; readback exact gelijk aan lokale bron. Template/gates ongewijzigd: integration_preview=true, integration_enabled=false, show_preview=false. MAIN195915448586 niet geschreven of gepubliceerd. Jotform-wijzigingen zijn wel in het bestaande publieke providerformulier opgeslagen; de winkelklantlinks blijven achter de bestaande gates.

Validatie: 17 bestaande LiquidJS/DOM-cases PASS, vier ThemeCheck-bestanden PASS (lokale gecachete Shopify-schema’s; remote schema-update onbereikbaar). Gewone desktopconceptpagina visueel gecontroleerd, alle velden zichtbaar. Uitklapregel opent en sluit. Nieuwe Jotform-presentatie na paginaherladen zichtbaar. Component met echte provideriframe op320/390px gecontroleerd: geen horizontale overflow, formulierhoogte1036/1022px, binnen1200px iframe; desktop964px binnen1100px. Dit zijn geïsoleerde browsercomponenten, geen fysieke telefoonreview. Geen nieuwe upload-/mail-/privacy-/grens-/performancevrijgave.

Tijdelijke QA-template exact hersteld: MD5 c76529d094fb4d534f9cd3352c63f4b4. Bronvóórwijziging in design-baseline. Screenshot simple-preview.png en simple-mobile.png; metingen design-mobile-checks.json.

Volgende handeling blijft: eigenaar controleert Jotform-verificatie- en testmail op info@badkamercity.nl. Designwijziging activeert geen winkeluploads.
