(() => {
  let saved;
  try { saved = JSON.parse(sessionStorage.getItem('bc:product-switcher:position:v1') || 'null'); } catch (_) {}
  const calls = [];
  const start = performance.now();
  const nativeScroll = window.scrollTo.bind(window);
  window.scrollTo = (...args) => {
    calls.push({ms:Math.round(performance.now()-start),top:typeof args[0]==='object'?args[0].top:args[1]});
    return nativeScroll(...args);
  };
  const run = () => {
    const panel=document.createElement('pre');
    panel.id='bc-scroll-qa';
    panel.style.cssText='position:fixed;bottom:64px;left:12px;z-index:99999;margin:0;padding:10px;background:#fff;border:1px solid #9ab0c1;border-radius:6px;font:11px/1.4 monospace;color:#102d45;max-width:420px;white-space:pre-wrap;pointer-events:none';
    document.body.append(panel);
    const ys=[];
    const update=()=>{
      const root=document.querySelector('[data-bc-product-switcher-v2]');
      const ms=Math.round(performance.now()-start);
      const y=Math.round(window.scrollY);
      if(ys.length===0||ys[ys.length-1].y!==y)ys.push({ms,y});
      const target=saved&&Number.isFinite(saved.top)?saved.top:null;
      const top=root?.getBoundingClientRect().top;
      panel.textContent=JSON.stringify({product:root?.dataset.productHandle,ready:root?.dataset.bcProductSwitcherV2Initialized==='true',handoff:Boolean(saved?.handoff),calls:calls.length,scrollCalls:calls,scrollY:y,target,top:Number.isFinite(top)?Math.round(top*10)/10:null,error:target!==null&&Number.isFinite(top)?Math.round((top-target)*10)/10:null,trace:ys.slice(-12),settledMs:ms},null,1);
      if(ms<3500)requestAnimationFrame(update);
    };
    requestAnimationFrame(update);
  };
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',run,{once:true});else run();
})();
