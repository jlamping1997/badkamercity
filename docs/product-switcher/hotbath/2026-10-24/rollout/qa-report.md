# Hotbath rollout browser QA — 24 October 2026

Result: PASS for the representative desktop menu sample in draft theme 195649929482, visibly named BadkamerCity - Hotbath keuzemenus 24 okt.

| Check | From | Verified destination | Result |
|---|---|---|---|
| Gent height | GT003IX | GT003MIX | PASS |
| Buddy IBS12 handshower | IBS12CR | IBS12CR1 | PASS |
| ACE numeric head diameter | IBS-ACE2001 | IBS-ACE2013 | PASS |
| Archie added colour | AR105EXT18IX | AR105EXT18BCP | PASS |
| Rails length and number of bars | RASS50-1CR | RASS80-1CR → RASS80-3CR | PASS |
| Existing CB003 height regression | CB003CAB | CB003MCAB | PASS |
| Archie length preserves colour | AR105EXT18BCP | AR105EXT25BCP | PASS |

SPOM3 and G50 (SPOM3 in title) each show no choice menu, while the purchase button stays enabled. No Liquid errors rendered in the tested products.

A cart started visibly empty. After selecting Archie 25 cm in brushed copper, the product form added exactly AR105EXT25BCP, variant 53794299412746, quantity 1. Only that test line was removed; the empty-cart heading was visibly confirmed. No checkout or payment was performed.

Local scratch evidence only: qa-rails-menu-20261024.jpg and qa-cart-selected-20261024.jpg. The screenshots are not included in this Git dossier; the durable test outcomes are recorded in qa-report.json.

Limits: Chrome cloud desktop, 1348 × 926 screenshot. No real-phone or mobile-viewport test, no exhaustive browser test of every tuple.

Content observation: the tested Gent/Archie/Rails pages rendered no product photo. A bounded read-only comparison of Gent GT003IX on current MAIN195611492618 (preview bar: BadkamerCity - Sunshower blog 23 okt) also showed zero product-gallery images. This confirms the absent photo is pre-existing for that sample. Archie/Rails were not separately compared against MAIN. Returned browser to Hotbath preview195649929482 and confirmed its Gent height menu. A separate catalogue image check remains useful.
