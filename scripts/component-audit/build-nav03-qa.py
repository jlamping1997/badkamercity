import argparse
import html
import http.cookiejar
import json
import pathlib
import re
import urllib.request
from html.parser import HTMLParser

parser = argparse.ArgumentParser()
parser.add_argument('--theme', required=True)
parser.add_argument('--output', required=True)
args = parser.parse_args()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
response = opener.open('https://badkamercity.nl/?preview_theme_id=' + args.theme, timeout=40)
source = response.read().decode()
theme = json.loads(re.search(r'Shopify\.theme\s*=\s*({[^;]+})', source).group(1))
assert str(theme['id']) == args.theme and theme['role'] == 'unpublished'


class Header(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.depth = 0
        self.parts = []
        self.done = False

    def handle_starttag(self, tag, attrs):
        if self.done:
            return
        values = dict(attrs)
        if not self.depth and 'section-header' in values.get('class', '').split():
            self.depth = 1
        elif self.depth and tag == 'div':
            self.depth += 1
        if self.depth:
            self.parts.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        if self.depth:
            self.parts.append('</' + tag + '>')
            if tag == 'div':
                self.depth -= 1
                if not self.depth:
                    self.done = True

    def handle_data(self, data):
        if self.depth:
            self.parts.append(data)

    def handle_entityref(self, name):
        if self.depth:
            self.parts.append('&' + name + ';')

    def handle_charref(self, name):
        if self.depth:
            self.parts.append('&#' + name + ';')


header = Header()
header.feed(source)
markup = ''.join(header.parts)
assert 'data-bc-category-more' in markup
styles = ''.join(value for value in re.findall(r'<style[^>]*>[\s\S]*?</style>', source) if value not in markup)
links = ''.join(tag for tag in re.findall(r'<link\b[^>]*>', source) if 'stylesheet' in tag)
scripts = []
for tag in re.findall(r'<script\b[^>]*src="[^"]+"[^>]*></script>', source):
    if '/compiled_assets/' in tag or any('/assets/' + name in tag for name in ('constants.js', 'pubsub.js', 'global.js', 'details-disclosure.js', 'details-modal.js', 'search-form.js', 'bc-mobile-header.js', 'predictive-search.js')):
        if tag not in markup and tag not in scripts:
            scripts.append(tag)
config = ''.join('<script>' + value + '</script>' for value in re.findall(r'<script[^>]*>([\s\S]*?)</script>', source) if 'window.routes =' in value)
fixture = '<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><base href="https://badkamercity.nl/">' + styles + links + '<script>window.Shopify={designMode:false};</script>' + config + ''.join(scripts) + '</head><body class="gradient">' + markup + '<main style="height:850px;padding:20px">Onder de header</main></body></html>'
payload = json.dumps(fixture, ensure_ascii=False).replace('<', '\\u003c')
widths = [320, 390, 768, 820, 989, 990, 1024, 1180, 1280, 1366, 1440, 1600, 1920]
html_page = '''{% layout none %}
<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow"><title>Badkamercity — schermcontrole</title><style>body{margin:16px;background:#f0f4f7;font:14px Arial,sans-serif;color:#102b43}iframe{display:block;border:1px solid #afc3d0;background:white;margin:8px 0 28px;box-sizing:content-box}input{font:inherit;padding:8px;width:100px}h1{font-size:22px}</style></head><body>
<h1>Headercontrole van het concept</h1><label for="qa-width">Breedte van het wisselframe</label> <input id="qa-width" type="number" value="1280" min="320" max="2200"><iframe id="interactive" title="Wisselframe" style="width:1280px;height:700px"></iframe><div id="frames"></div>
<script id="fixture" type="application/json">''' + payload + '''</script><script>
const fixture=JSON.parse(document.getElementById('fixture').textContent);
const interactive=document.getElementById('interactive');interactive.srcdoc=fixture;
document.getElementById('qa-width').addEventListener('input',event=>{const width=Number(event.target.value);if(width>=320&&width<=2200)interactive.style.width=width+'px'});
for(const width of ''' + json.dumps(widths) + '''){const heading=document.createElement('h2');heading.textContent=width+' CSS-pixels';const frame=document.createElement('iframe');frame.id='width-'+width;frame.title='Header '+width+' pixels';frame.dataset.width=width;frame.style.cssText='width:'+width+'px;height:700px';frame.srcdoc=fixture;document.getElementById('frames').append(heading,frame)}
</script></body></html>'''
html_page = '{% layout none %}\n{% raw %}\n' + html_page.split('\n', 1)[1] + '\n{% endraw %}\n'
size = len(html_page.encode())
assert size < 256000, size
pathlib.Path(args.output).write_text(html_page)
print(json.dumps({'bytes': size, 'headerBytes': len(markup.encode()), 'widths': widths, 'themeId': args.theme, 'method': 'Real preview header markup, CSS links, font styles and existing header runtime in same-origin srcdoc fixtures; not physical devices or full pages.'}))
