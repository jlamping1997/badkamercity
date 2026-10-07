"""Read-only follow-up: verify draft cart and stored specifications, diagnose search.
No order/customer data, login, cart mutations, cookies, HAR or session URLs saved.
"""
from __future__ import annotations
import json
from pathlib import Path
import re
from urllib.parse import urlencode
from playwright.sync_api import sync_playwright
from customer_journey_browser import BASE, PDP, safe_url

OUT = Path('test-results/customer-journey')
DRAFT = '194924904714'


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    report = {'scope': 'Anonymous read-only follow-up; no mutations', 'tests': [], 'search_diagnostics': []}
    def record(name, passed, **data):
        item = {'name': name, 'status': 'PASS' if passed else 'FAIL', **data}
        report['tests'].append(item)
        print(json.dumps(item, ensure_ascii=False), flush=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for label, width in [('desktop', 1440), ('mobile', 390)]:
            context = browser.new_context(viewport={'width': width, 'height': 900 if width == 1440 else 844},
                                          locale='nl-NL', is_mobile=width == 390, has_touch=width == 390,
                                          service_workers='block')
            context.route('**/*', lambda route: route.continue_() if route.request.method in {'GET', 'HEAD', 'OPTIONS'} else route.abort())
            page = context.new_page()
            page.set_default_timeout(12000)
            try:
                page.goto(BASE + '/cart?preview_theme_id=' + DRAFT, wait_until='domcontentloaded', timeout=30000)
                page.wait_for_timeout(900)
                text = page.locator('main').inner_text()
                record(label + ':draft-cart-clean', 'Featured collection' not in text and 'Je winkelwagen is leeg' in text,
                       extra_recommendation_sections=page.locator('main .featured-collection').count())
                page.screenshot(path=str(OUT / (label + '-draft-cart-clean.png')), full_page=True)
                page.goto(BASE + PDP + '?preview_theme_id=' + DRAFT, wait_until='domcontentloaded', timeout=30000)
                page.wait_for_timeout(900)
                table = page.locator('.bc-product-specs')
                specs = table.inner_text() if table.count() == 1 else ''
                groups = ['Maatvoering', 'Uiterlijke kenmerken', 'Algemeen']
                record(label + ':draft-specs', all(x in specs for x in groups) and '15,6 cm' in specs and '12 cm' in specs,
                       specification_rows=table.locator('tr').count() if table.count() == 1 else 0)
                record(label + ':draft-no-overflow', page.evaluate('document.documentElement.scrollWidth <= innerWidth + 2'))
                page.screenshot(path=str(OUT / (label + '-draft-specs-confirmed.png')), full_page=True)
            except Exception as exc:
                record(label + ':draft-check', False, error=type(exc).__name__)
            finally:
                context.close()
        context = browser.new_context(viewport={'width': 1440, 'height': 900}, locale='nl-NL', service_workers='block')
        context.route('**/*', lambda route: route.continue_() if route.request.method in {'GET', 'HEAD', 'OPTIONS'} else route.abort())
        page = context.new_page()
        queries = [
            'opbouw wastafelkraan koper',
            'opbouw AND wastafelkraan AND koper',
            '"opbouw" AND "wastafelkraan" AND "koper"',
            'title:wastafelkraan AND title:koper NOT title:inbouw NOT title:afbouwdeel NOT title:hendel NOT title:vloermontage',
        ]
        for index, query in enumerate(queries):
            try:
                page.goto(BASE + '/search?' + urlencode({'q': query, 'type': 'product'}), wait_until='domcontentloaded', timeout=30000)
                page.wait_for_timeout(700)
                count = page.locator('#ProductCountDesktop')
                links = page.locator('main .bc-search-card__title').all_inner_texts()
                diagnostic = {'query': query, 'url': safe_url(page.url),
                              'displayed_count': count.inner_text().strip() if count.count() == 1 else None,
                              'first10_titles': links[:10],
                              'first10_explicit_inbouw_or_parts': sum(bool(re.search(r'inbouw|afbouwdeel|hendel', x, re.I)) for x in links[:10])}
                report['search_diagnostics'].append(diagnostic)
                print(json.dumps(diagnostic, ensure_ascii=False), flush=True)
                page.screenshot(path=str(OUT / f'search-diagnostic-{index}.png'), full_page=False)
            except Exception as exc:
                report['search_diagnostics'].append({'query': query, 'status': 'BLOCKED', 'error': type(exc).__name__})
        context.close()
        browser.close()
    (OUT / 'followup.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    return int(any(x['status'] == 'FAIL' for x in report['tests']))


if __name__ == '__main__':
    raise SystemExit(main())
