# main-blog

**Bron:** `sections/main-blog.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/CONTENT_AND_FORMS.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: `templates/blog.json`.

Letterlijke uitgaande refs: `assets/component-article-card.css`, `assets/component-card.css`, `assets/section-main-blog.css`, `snippets/article-card.liquid`, `snippets/pagination.liquid`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `layout` | `select` | t:sections.main-blog.settings.layout.label: grid: t:sections.main-blog.settings.layout.options__1.label; collage: t:sections.main-blog.settings.layout.options__2.label |
| `show_image` | `checkbox` | t:sections.main-blog.settings.show_image.label |
| `image_height` | `select` | t:sections.main-blog.settings.image_height.label: adapt: t:sections.main-blog.settings.image_height.options__1.label; small: t:sections.main-blog.settings.image_height.options__2.label; medium: t:sections.main-blog.settings.image_height.options__3.label; large: t:sections.main-blog.settings.image_height.options__4.label |
| `show_date` | `checkbox` | t:sections.main-blog.settings.show_date.label |
| `show_author` | `checkbox` | t:sections.main-blog.settings.show_author.label |
| `padding_top` | `range` | t:sections.all.padding.padding_top |
| `padding_bottom` | `range` | t:sections.all.padding.padding_bottom |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: —.

Letterlijke metafieldkeys: —.

DOM-hooks: —.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
