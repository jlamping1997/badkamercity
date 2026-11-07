import {Window} from 'happy-dom';
import fs from 'node:fs';
import assert from 'node:assert/strict';
const wait=()=>new Promise(resolve=>setTimeout(resolve,40));
async function test(mode) {
 const window=new Window({url:'https://badkamercity.nl/products/test',width:390,height:844});
 const d=window.document;
 const addon=mode==='pending' ? `<bc-inbouw-addon data-valid="true" data-parent-variant="1" data-currency="EUR" data-body-price="17400" data-quantity-per-trim="1" data-body-available="true"><input type="radio" data-inbouw-choice value="yes" name="choice"><input type="radio" data-inbouw-choice value="no" name="choice"></bc-inbouw-addon>`:'';
 d.write(`<product-info data-hotbath-mobile-a="true" data-product-price="21500" data-product-variant="1" data-currency="EUR" data-mobile-total-label="Totaal" data-mobile-vat-label="Incl btw" data-mobile-choose-inbouw-label="Kies inbouw"><div class="product__info-container"><span class="bc-buybox__price-current">€215</span><div class="bc-buybox__purchase-row"><div class="bc-buybox__section--quantity"><input name="quantity" type="number" value="1" min="1" form="p"></div><div class="bc-buybox__section--actions"><product-form><form id="p"><input name="id" value="1">${addon}<div class="bc-product-form__buttons"><button class="product-form__submit">In winkelwagen</button></div></form></product-form></div></div></div><bc-product-sticky><button data-sticky-submit><span data-sticky-label>In winkelwagen</span></button><span data-sticky-price></span><span data-sticky-error></span><span class="bc-product-sticky__quantity"><input data-sticky-quantity><button data-sticky-minus></button><button data-sticky-plus></button></span></bc-product-sticky></product-info>`);
 let schedules=0;
 const raf=window.requestAnimationFrame.bind(window);
 window.requestAnimationFrame=cb=>{schedules++;return raf(cb)};
 window.eval(fs.readFileSync(new URL('../after/assets/bc-product-sticky.js', import.meta.url),'utf8'));
 window.eval(fs.readFileSync(new URL('../after/assets/bc-hotbath-mobile.js', import.meta.url),'utf8'));
 d.dispatchEvent(new window.Event('DOMContentLoaded'));
 window.dispatchEvent(new window.Event('resize'));
 await wait();const settled=schedules;await wait();assert.equal(schedules,settled,`${mode} idle loop`);
 assert.equal(d.querySelector('product-info').dataset.mobileTotalState,mode);
 window.dispatchEvent(new window.Event('scroll'));
 await wait();const afterScroll=schedules;await wait();assert.equal(schedules,afterScroll,`${mode} scroll loop`);
 const qty=d.querySelector('input[name=quantity]');qty.value='2';qty.dispatchEvent(new window.Event('input',{bubbles:true}));
 await wait();const afterQty=schedules;await wait();assert.equal(schedules,afterQty,`${mode} quantity loop`);
 if(mode==='ready')assert.equal(d.querySelector('[data-mobile-total-value]').dataset.totalCents,'43000');
 else {
   const yes=d.querySelector('[data-inbouw-choice][value=yes]');yes.checked=true;yes.dispatchEvent(new window.Event('change',{bubbles:true}));
   await wait();const afterChoice=schedules;await wait();assert.equal(schedules,afterChoice,'choice loop');
   assert.equal(d.querySelector('[data-mobile-total-value]').dataset.totalCents,'77800');
 }
 const beforeDesktop=schedules;
 window.happyDOM.setWindowSize({width:1200,height:844});
 await wait();const desktop=schedules;await wait();assert.equal(schedules,desktop,'desktop loop');
 assert.equal(d.querySelector('product-info').classList.contains('bc-hotbath-mobile-active'),false);
 assert.equal(d.querySelector('.bc-buybox__section--quantity').parentElement.className,'bc-buybox__purchase-row');
 console.log(JSON.stringify({mode,settled,afterScroll,afterQty,beforeDesktop,desktop,passed:true}));
 await window.happyDOM.abort();window.close();
}
await test('ready');await test('pending');
