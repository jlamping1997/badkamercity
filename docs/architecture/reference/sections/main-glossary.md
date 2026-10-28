# main-glossary

**Bron:** `sections/main-glossary.liquid`. Bronstatus: BYTE_MATCH.

[Functioneel dossier](../../components/CONTENT_AND_FORMS.md) · [Bronhashes](../source-index.json) · [Alle secties](../SECTIONS.md)

Dit is de bronreferentie. Het dossier geeft de bedoeling, data-eigenaar, toestanden en onderhoudsgrenzen.

## Koppelingen

Letterlijke callers: `templates/page.begrippenlijst.json`.

Letterlijke uitgaande refs: `assets/section-main-glossary.css`.

Geen caller gevonden betekent niet ongebruikt: Theme Editor, platformsections en dynamische aanroepen vallen buiten deze parser.

## Schema-instellingen

| ID | Type | Label / opties |
| --- | --- | --- |
| `heading` | `text` | Titel |
| `intro` | `richtext` | Intro |
| `enable_search` | `checkbox` | Zoekfunctie tonen |
| `search_label` | `text` | Zoekveld label |
| `search_placeholder` | `text` | Zoekveld placeholder |
| `empty_text` | `richtext` | Tekst zonder resultaten |
| `color_scheme` | `color_scheme` | Kleurenschema |
| `padding_top` | `range` | Bovenruimte |
| `padding_bottom` | `range` | Onderruimte |

## Blocktype term

| ID | Type | Label / opties |
| --- | --- | --- |
| `term` | `text` | Begrip |
| `letter` | `select` | Letter: A: A; B: B; C: C; D: D; E: E; F: F; G: G; H: H; I: I; J: J; K: K; L: L; M: M; N: N; O: O; P: P; Q: Q; R: R; S: S; T: T; U: U; V: V; W: W; X: X; Y: Y; Z: Z |
| `keywords` | `text` | Zoekwoorden |

## Technische ingangen

Formtypen: —.

Letterlijke events in deze bron: `input`.

Letterlijke metafieldkeys: —.

DOM-hooks: `data-keywords`, `data-letter`, `data-term`.

Geen vermelding sluit dynamische keys, externe handlers of platformwerking niet uit. Inhoud/defaults en huidige product-/contact-/settingswaarden worden niet door deze tool gepubliceerd.
