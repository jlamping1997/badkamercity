function createSwitcherPositionKeeper(window, document) {
  const storageKey = 'bc:product-switcher:position:v1';
  const ttl = 30000;
  const maxRestoreTime = 15000;
  const settleTime = 2000;
  const inputEvents = ['pointerdown', 'touchstart', 'wheel', 'keydown'];

  function optedIn(root) {
    return root?.dataset?.bcPreservePosition === 'true';
  }

  function routeKey(value) {
    try {
      const url = new URL(value, window.location.origin);
      if (url.origin !== window.location.origin || !url.pathname.includes('/products/')) return null;
      url.searchParams.delete('preview_theme_id');
      url.searchParams.sort();
      return url.pathname + url.search + url.hash;
    } catch (_) {
      return null;
    }
  }

  function discard(token) {
    if (!token) return;
    try {
      const saved = JSON.parse(window.sessionStorage.getItem(storageKey) || 'null');
      if (saved?.savedAt === token.savedAt && saved?.group === token.group && saved?.target === token.target) {
        window.sessionStorage.removeItem(storageKey);
      }
    } catch (_) {}
  }

  function remember(root, destination) {
    if (!optedIn(root)) return null;
    const target = routeKey(destination);
    const group = String(root.dataset.switchGroup || '').trim();
    if (!target || !group) return null;
    let token;
    try {
      const top = root.getBoundingClientRect().top;
      if (!Number.isFinite(top)) return null;
      token = { version: 1, group, target, top, savedAt: Date.now() };
      window.sessionStorage.setItem(storageKey, JSON.stringify(token));
      return token;
    } catch (_) {
      discard(token);
      return null;
    }
  }

  function prepare(root) {
    if (!optedIn(root)) return null;
    let saved;
    try {
      const value = window.sessionStorage.getItem(storageKey);
      if (!value) return null;
      window.sessionStorage.removeItem(storageKey);
      saved = JSON.parse(value);
    } catch (_) {
      return null;
    }
    const age = Date.now() - saved?.savedAt;
    const currentRoute = routeKey(window.location.href);
    if (saved?.version !== 1 || !Number.isFinite(saved?.top) || !Number.isFinite(age) ||
        age < 0 || age > ttl || saved.group !== String(root.dataset.switchGroup || '').trim() ||
        !currentRoute || saved.target !== currentRoute) return null;

    let active = true;
    let ready = false;
    let frame;
    let timer;
    const deadline = Date.now() + maxRestoreTime;
    let stopAt = deadline;
    let loaded = document.readyState === 'complete';
    let previousRestoration;
    const style = document.documentElement?.style;
    const previousBehavior = style?.scrollBehavior;
    try {
      previousRestoration = window.history.scrollRestoration;
      window.history.scrollRestoration = 'manual';
    } catch (_) {}
    if (style) style.scrollBehavior = 'auto';

    function cancel() {
      if (!active) return;
      active = false;
      if (frame !== undefined) window.cancelAnimationFrame(frame);
      if (timer !== undefined) window.clearTimeout(timer);
      inputEvents.forEach((type) => window.removeEventListener(type, cancel, true));
      window.removeEventListener('load', onWindowLoad);
      window.removeEventListener('load', schedule, true);
      window.removeEventListener('pagehide', cancel);
      try {
        if (previousRestoration !== undefined) window.history.scrollRestoration = previousRestoration;
      } catch (_) {}
      if (style) style.scrollBehavior = previousBehavior;
    }

    function correct() {
      frame = undefined;
      if (!active || !ready) return;
      if (!root.isConnected || Date.now() > deadline) {
        cancel();
        return;
      }
      const currentTop = root.getBoundingClientRect().top;
      const target = window.scrollY + currentTop - saved.top;
      if (Number.isFinite(target) && Math.abs(currentTop - saved.top) > 0.5) {
        try {
          window.scrollTo({ left: window.scrollX || 0, top: Math.max(0, target), behavior: 'instant' });
        } catch (_) {
          window.scrollTo(window.scrollX || 0, Math.max(0, target));
        }
      }
    }

    function schedule() {
      if (!active || !ready || frame !== undefined) return;
      frame = window.requestAnimationFrame(correct);
    }

    function tick() {
      timer = undefined;
      if (!active) return;
      if (Date.now() >= (ready ? stopAt : deadline)) {
        cancel();
        return;
      }
      schedule();
      timer = window.setTimeout(tick, 100);
    }

    function onWindowLoad() {
      loaded = true;
      if (ready) stopAt = Math.min(deadline, Date.now() + settleTime);
      schedule();
    }

    inputEvents.forEach((type) => window.addEventListener(type, cancel, { capture: true, passive: true }));
    window.addEventListener('load', onWindowLoad);
    window.addEventListener('load', schedule, true);
    window.addEventListener('pagehide', cancel);
    timer = window.setTimeout(tick, 100);

    return {
      cancel,
      activate() {
        if (!active) return;
        ready = true;
        if (loaded) stopAt = Math.min(deadline, Date.now() + settleTime);
        correct();
        schedule();
      },
    };
  }

  return { remember, prepare, discard };
}
