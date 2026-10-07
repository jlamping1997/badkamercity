"""Anonymous storefront QA; never log in, fill customer details, or submit an order.

Default is read-only. --cart permits only temporary cart requests in fresh contexts.
Checkout entry may be opened, not filled/submitted. No cookies/HAR/HTML are saved.
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import re
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from playwright.sync_api import sync_playwright

BASE = 'https://fpa9hu-i3.myshopify.com'
HOST = urlsplit(BASE).netloc
PDP = '/products/hotbath-ace-ac003-wastafelkraan-laag-zonder-waste-geborsteld-koper-pvd'
WIESBADEN = '/products/wiesbaden-style-wastafelkraan-geborsteld-koper-pvd-29-1613'
SKU = 'AC003BCP'


def safe_url(url: str) -> str:
    parts = urlsplit(url)
    if re.search(r'checkout|account|login|authenticate', parts.path, re.I):
        return f'{parts.scheme}://{parts.netloc}/[private-session-path]'
    query = urlencode([(k, v) for k, v in parse_qsl(parts.query)
                       if k in {'q', 'type', 'preview_theme_id', 'sort_by', 'page'} or k.startswith('filter.')])
    return urlunsplit((parts.scheme, parts.netloc, parts.path, query, ''))


def allowed_request(method: str, url: str, cart: bool) -> bool:
    if method in {'GET', 'HEAD', 'OPTIONS'}:
        return True
    parts = urlsplit(url)
    return (cart and method == 'POST' and parts.scheme == 'https' and parts.netloc == HOST
            and re.fullmatch(r'/cart(?:/(?:add|change|update|clear))?(?:\.js)?', parts.path) is not None)


def visible(locator):
    for item in locator.all():
        if item.is_visible():
            return item
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--cart', action='store_true')
    parser.add_argument('--out', default='test-results/customer-journey')
    args = parser.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    report = {'store': BASE, 'scope': 'Anonymous desktop/mobile; no customer data or order submission',
              'cart_authorized': args.cart, 'pages': [], 'steps': [], 'blocked_writes': [],
              'payment_order_and_delivery_validation': 'NOT_TESTED'}

    def step(name, status, **details):
        record = dict(name=name, status=status, **details)
        report['steps'].append(record)
        print(json.dumps(record, ensure_ascii=False), flush=True)

    with sync_playwright() as p:
        launch = {'headless': True}
        if os.environ.get('BC_CHROMIUM_PATH'):
            launch['executable_path'] = os.environ['BC_CHROMIUM_PATH']
        browser = p.chromium.launch(**launch)
        for label, width, height in [('desktop', 1440, 900), ('mobile', 390, 844)]:
            context = browser.new_context(viewport={'width': width, 'height': height}, locale='nl-NL',
                                          is_mobile=label == 'mobile', has_touch=label == 'mobile',
                                          service_workers='block')
            context.set_default_timeout(10000)
            def guard(route):
                request = route.request
                if allowed_request(request.method, request.url, args.cart):
                    route.continue_()
                else:
                    if len(report['blocked_writes']) < 100:
                        report['blocked_writes'].append({'method': request.method, 'url': safe_url(request.url)})
                    route.abort()
            context.route('**/*', guard)
            page = context.new_page()

            def capture(name):
                page.wait_for_timeout(650)
                data = page.evaluate('''() => {
                    const root = document.querySelector('main') || document.body;
                    const visible = e => !!(e.offsetWidth || e.offsetHeight || e.getClientRects().length);
                    return {title: document.title,
                      headings: [...root.querySelectorAll('h1,h2,h3')].filter(visible).slice(0,45).map(e => ({tag:e.tagName,text:e.innerText.trim()})),
                      text: root.innerText.slice(0,20000),
                      products: [...root.querySelectorAll('a[href*="/products/"]')].filter(visible).slice(0,80).map(e => ({text:e.innerText.trim(),href:e.getAttribute('href')})),
                      filters: [...document.querySelectorAll('.facets__summary,.mobile-facets__summary')].map(e=>e.innerText.trim()).filter(Boolean).slice(0,25),
                      overflow: document.documentElement.scrollWidth > window.innerWidth + 2,
                      width: innerWidth, height: document.documentElement.scrollHeight};
                }''')
                data.update(viewport=label, name=name, url=safe_url(page.url))
                for item in data['products']:
                    item['href'] = safe_url(BASE + item['href']) if item['href'].startswith('/') else safe_url(item['href'])
                filename = f'{label}-{name}.png'
                page.screenshot(path=str(out / filename), full_page=data['height'] < 18000)
                data['screenshot'] = filename
                report['pages'].append(data)
                print(json.dumps({'page': name, 'viewport': label, 'url': data['url'],
                                  'title': data['title'], 'overflow': data['overflow'],
                                  'product_links': len(data['products'])}, ensure_ascii=False), flush=True)
                return data

            def open_page(path, name):
                response = page.goto(BASE + path, wait_until='domcontentloaded', timeout=30000)
                if '/password' in urlsplit(page.url).path or (response and response.status >= 400):
                    raise RuntimeError(f'Access blocked for {name}; HTTP {response.status if response else "unknown"}')
                return capture(name)

            try:
                open_page('/', 'home')
                for handle in ['kranen', 'wastafelkranen', 'opbouw-wastafelkranen']:
                    target = f'/collections/{handle}'
                    link = visible(page.locator(f'main a[href="{target}"]')) or visible(page.locator(f'a[href="{target}"]'))
                    if link is not None:
                        link.click()
                        page.wait_for_url('**' + target + '*', timeout=15000)
                        step(f'{label}:navigate:{handle}', 'PASS', method='visible_link_click')
                        capture(handle)
                    else:
                        step(f'{label}:navigate:{handle}', 'REVIEW', reason='No currently visible category link; direct URL used for page inspection.')
                        open_page(target, handle)
                open_page('/', 'search-start')
                for number, query in enumerate(['wastafelkraan koper', 'opbouw wastafelkraan koper', 'koperen opbouw wastafelkraan', 'AC003BCP']):
                    field = visible(page.locator('form[role="search"] input[name="q"]'))
                    if field is None:
                        step(f'{label}:search:{query}', 'REVIEW', reason='No visible search input; direct query used.')
                        open_page('/search?' + urlencode({'q': query, 'type': 'product'}), f'search-{number}')
                    else:
                        field.fill(query)
                        page.wait_for_timeout(800)
                        if number == 0:
                            capture('search-suggestions')
                        field.press('Enter')
                        page.wait_for_url(lambda u: urlsplit(u).path == '/search' and dict(parse_qsl(urlsplit(u).query)).get('q') == query, timeout=15000)
                        page.wait_for_load_state('domcontentloaded')
                        data = capture(f'search-{number}')
                        step(f'{label}:search:{query}', 'OBSERVED', product_links=len(data['products']))
                open_page(PDP, 'hotbath-product')
                open_page(WIESBADEN, 'wiesbaden-product')
                if args.cart:
                    cart_json = context.request.get(BASE + '/cart.js').json()
                    if cart_json.get('item_count') != 0:
                        raise RuntimeError('New context cart is not empty; refusing mutation.')
                    product = context.request.get(BASE + PDP + '.js').json()
                    variant = next((x for x in product.get('variants', []) if x.get('sku') == SKU), None)
                    if not variant or not variant.get('available'):
                        raise RuntimeError('Exact available fixture SKU not found; refusing cart mutation.')
                    open_page(PDP + '?' + urlencode({'variant': variant['id']}), 'before-add')
                    button = visible(page.locator('main button[name="add"]'))
                    if button is None or not button.is_enabled():
                        raise RuntimeError('No enabled visible add-to-cart button.')
                    button.click()
                    for _ in range(15):
                        cart_json = context.request.get(BASE + '/cart.js').json()
                        if cart_json.get('item_count') == 1:
                            break
                        page.wait_for_timeout(250)
                    items = cart_json.get('items', [])
                    valid = (len(items) == 1 and items[0].get('variant_id') == variant['id']
                             and items[0].get('quantity') == 1 and items[0].get('price') == variant['price'])
                    step(f'{label}:add-to-cart', 'PASS' if valid else 'FAIL', exact_sku=SKU)
                    capture('cart-notification')
                    if valid:
                        open_page('/cart', 'cart')
                        checkout = visible(page.locator('button[name="checkout"]'))
                        if checkout is not None and checkout.is_enabled():
                            try:
                                checkout.click()
                                page.wait_for_url(re.compile(r'.*checkout.*'), timeout=20000)
                                capture('checkout-entry')
                                step(f'{label}:checkout-entry', 'OPENED_NOT_SUBMITTED')
                            except Exception as exc:
                                step(f'{label}:checkout-entry', 'BLOCKED_OR_FAILED', error=type(exc).__name__)
                        else:
                            step(f'{label}:checkout-entry', 'REVIEW', reason='No enabled visible checkout button.')
                        open_page('/cart', 'cart-return')
                        quantity = visible(page.locator('input[name="updates[]"]'))
                        if quantity is not None:
                            quantity.fill('2')
                            quantity.press('Tab')
                            for _ in range(15):
                                state = context.request.get(BASE + '/cart.js').json()
                                if state.get('item_count') == 2:
                                    break
                                page.wait_for_timeout(250)
                            step(f'{label}:cart-quantity', 'PASS' if state.get('item_count') == 2 else 'FAIL')
                        else:
                            step(f'{label}:cart-quantity', 'REVIEW', reason='No visible quantity field.')
                        remove = visible(page.locator('cart-remove-button a'))
                        if remove is not None:
                            remove.click()
                            for _ in range(15):
                                state = context.request.get(BASE + '/cart.js').json()
                                if state.get('item_count') == 0:
                                    break
                                page.wait_for_timeout(250)
                            step(f'{label}:cart-remove', 'PASS' if state.get('item_count') == 0 else 'FAIL')
                            capture('cart-empty')
                        else:
                            step(f'{label}:cart-remove', 'REVIEW', reason='No visible remove link.')
                else:
                    open_page('/cart', 'cart-empty')
                open_page(PDP + '?preview_theme_id=194924904714', 'hotbath-draft-preview')
            except Exception as exc:
                step(f'{label}:journey', 'BLOCKED_OR_FAILED', error=type(exc).__name__)
                try:
                    capture('blocked')
                except Exception:
                    pass
            finally:
                if args.cart:
                    try:
                        state = context.request.get(BASE + '/cart.js').json()
                        if state.get('item_count', 0) > 0:
                            response = context.request.post(BASE + '/cart/clear.js', data={})
                            step(f'{label}:cart-cleanup', 'PASS' if response.ok and response.json().get('item_count') == 0 else 'FAIL')
                        else:
                            step(f'{label}:cart-cleanup', 'PASS', reason='Already empty.')
                    except Exception:
                        step(f'{label}:cart-cleanup', 'NOT_VERIFIED')
                context.close()
                (out / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
        browser.close()
    failures = [s for s in report['steps'] if s['status'] in {'FAIL', 'BLOCKED_OR_FAILED'}]
    report['summary'] = {'pages_captured': len(report['pages']), 'failed_or_blocked_steps': len(failures),
                         'checkout': 'Entry only; payment, shipping choices and order creation NOT_TESTED'}
    (out / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report['summary'], ensure_ascii=False))
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
