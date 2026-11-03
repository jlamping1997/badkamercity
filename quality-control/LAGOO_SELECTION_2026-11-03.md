# QC-08 — alleen goede foto's selecteren, kleur vast, voortgang per twintig

3 november 2026. De galerie heeft één schakelknop per foto: Deze foto is goed / ✓ Goede foto. Deselecteren bewaart unchecked; niet geselecteerd betekent niet afgekeurd. Oude oordelen blijven in de audit, maar worden niet als verplichte afkeuren getoond. De kleur en SKU blijven sticky bovenaan zichtbaar; kortere foto op mobiel houdt de bediening dichter bij het beeld.

Foto-keuzes worden direct via dezelfde eigenaargebonden review-API bewaard. Bij Volgend product op20/40/60/etc wordt eerst een immutable checkpoint opgeslagen via de bestaande checkpoint-API (max20product-ID’s, mode=products, size25 voor bestaand contract, gallerySelectionV1=true en nextSku). Pas na bevestiging navigeren. Stabiel checkpoint-ID bij retry voorkomt duplicaten. Bij herladen automatisch hervatten op nextSku van het nieuwste galeriecheckpoint; reeds bevestigde selecties na dat checkpoint blijven ook opgeslagen. Een onvolledige laatste groep wordt bewaard met Afronden en bewaren. Geen API-/schemamigratie of Shopify-write. Bestaande beoordelingen/checkpoints niet gereset.

TypeScript PASS;30API/SQLite-regressiegroepen en15Lagoo-groepen PASS, met nieuwe twintiggrens/laatste-groep en daadwerkelijke checkpoint-save/readback in tijdelijke SQLite. Productiebuild PASS. Browser/fysieke telefoon/hosted visitor-write niet getest; eerdere previewinfrastructuurblokkade niet omzeild. Eigenaar herlaadt, selecteert foto's en controleert de bewaar-/hervatmelding na20producten. Vorige Sites-versie8 blijft terugval.

Publicatie succeeded: Sites-bron c5a4ee8dea2043da36db698505cb19bfc06893a2, deployment appgdep_6ae98d0bef948191831ff2ad92f3b432.
