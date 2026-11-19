# Hotbath mobile swatches — 25 October 2026

Implementation is scoped to switchers explicitly marked `data-hotbath-mobile-a="true"` and viewport width below 750 px. Desktop and other brands use the original dropdown/button rendering. Existing product matching, unavailable combinations, navigation locking and scroll restoration remain in place.

The colour group comes first on mobile. Six swatches are initially visible; the selected colour replaces the sixth visible item when it would otherwise be hidden. The full selected name is printed above the grid. “Bekijk alle kleuren” expands the complete grid and “Minder kleuren” collapses it. Other mobile option groups render text buttons. Breakpoint changes rerender the presentation while preserving the selected state.

Swatches are unmodified official manufacturer images from `hotbath.com/images/finishes/`. Observed source pages and exact image URLs are in `hotbath-swatches-source.json`. CR, GN, WH, BB, AB, AI, BBP, BCP, MBP and PBP were observed on the official Cobber CB105.18/IBS70 pages; BGP and IX on Archie AR004; TB on Guy Row GY005R.20. All 13 downloaded images returned HTTP 200 and their contact sheets were visually inspected. Public storefront rendering uses copied Shopify theme assets, with full text fallback if a finish has no mapping or its image fails.

Files: `assets/bc-product-switcher.js`, `assets/bc-hotbath-swatches.css`, `snippets/bc-product-switcher.liquid` and 13 `assets/bc-hotbath-swatch-*.jpg` images. The parent integration owns loading the CSS and the translated all-colours/less-colours labels.

Validation: `node --check` passed. Functional DOM-mock checks passed for six visible choices, selected choice beyond the first six, the full selected colour name, expand/collapse, desktop restoration, selected-state retention, disabled impossible combinations and unchanged non-Hotbath dropdown rendering. These are local script tests, not a real-browser or device check. Browser integration is performed separately by the parent task.

No Shopify product data or live theme was changed by this subtask.
