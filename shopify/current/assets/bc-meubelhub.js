/* Native details remain usable when JS is unavailable. No filter/theme hooks. */
(function(){'use strict';
 function setup(root){
  if(root.dataset.bcmReady)return;root.dataset.bcmReady='true';
  const narrow=window.matchMedia('(max-width: 539px)');
  const desktop=window.matchMedia('(min-width: 1000px)');
  const groups=Array.from(root.querySelectorAll('[data-bcm-group]'));
  function adapt(){groups.forEach(function(d,i){
   if(desktop.matches){d.open=true;d.querySelector('summary').tabIndex=-1;}
   else{d.querySelector('summary').removeAttribute('tabindex');if(!d.dataset.touched)d.open=!narrow.matches||i===0;}
  });}
  groups.forEach(function(d){d.querySelector('summary').addEventListener('click',function(e){if(desktop.matches)e.preventDefault();else d.dataset.touched='true';});});
  adapt();[narrow,desktop].forEach(function(m){if(m.addEventListener)m.addEventListener('change',adapt);else m.addListener(adapt);});
  root.addEventListener('bcm:cleanup',function(){[narrow,desktop].forEach(function(m){if(m.removeEventListener)m.removeEventListener('change',adapt);else m.removeListener(adapt);});},{once:true});
 }
 function init(context){context.querySelectorAll('[data-bcm-hub]').forEach(setup);}
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',function(){init(document);});else init(document);
 document.addEventListener('shopify:section:load',function(e){init(e.target);});
 document.addEventListener('shopify:section:unload',function(e){e.target.querySelectorAll('[data-bcm-hub]').forEach(function(r){r.dispatchEvent(new Event('bcm:cleanup'));});});
})();
