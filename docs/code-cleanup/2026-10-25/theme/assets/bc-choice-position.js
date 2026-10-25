(() => {
  if (window.BCChoicePosition) return;
  window.BCChoicePosition = {
    prepare(root, saved) {
      if (!root || !Number.isFinite(saved?.top)) return null;
      const settleTime = 80;
      const maxSettleTime = 1000;
      const inputEvents = ['pointerdown', 'touchstart', 'wheel', 'keydown'];
      let active = true;
      let ready = false;
      let frame;
      let timer;
      let stableSince;
      let lastTop;
      let lastHeight;
      let previousRestoration;
      const style = document.documentElement?.style;
      const properties = ['scroll-behavior', 'overflow-anchor'];
      const previousStyles = properties.map(name => [name, style?.getPropertyValue(name), style?.getPropertyPriority(name)]);
      const previousMinHeight = root.style.minHeight;
      try {
        previousRestoration = window.history.scrollRestoration;
        window.history.scrollRestoration = 'manual';
      } catch (_) {}
      style?.setProperty('scroll-behavior', 'auto', 'important');
      style?.setProperty('overflow-anchor', 'none');
      if (Number.isFinite(saved.height) && saved.height > 0 && saved.height < 5000) {
        root.style.minHeight = saved.height + 'px';
      }

      function cancel() {
        if (!active) return;
        active = false;
        if (frame !== undefined) window.cancelAnimationFrame(frame);
        if (timer !== undefined) window.clearTimeout(timer);
        inputEvents.forEach(type => window.removeEventListener(type, cancel, true));
        window.removeEventListener('pagehide', cancel);
        root.style.minHeight = previousMinHeight;
        try {
          if (previousRestoration !== undefined) window.history.scrollRestoration = previousRestoration;
        } catch (_) {}
        previousStyles.forEach(([name, value, priority]) => {
          if (value) style?.setProperty(name, value, priority);
          else style?.removeProperty(name);
        });
      }

      function finish() {
        if (!active || !ready) return;
        if (root.isConnected) {
          const top = root.getBoundingClientRect().top;
          const target = window.scrollY + top - saved.top;
          if (Number.isFinite(target) && Math.abs(top - saved.top) > 1) {
            try {
              window.scrollTo({ left: window.scrollX || 0, top: Math.max(0, target), behavior: 'instant' });
            } catch (_) {
              window.scrollTo(window.scrollX || 0, Math.max(0, target));
            }
          }
        }
        cancel();
      }

      function measure() {
        frame = undefined;
        if (!active || !ready) return;
        if (!root.isConnected) {
          cancel();
          return;
        }
        const rect = root.getBoundingClientRect();
        const top = window.scrollY + rect.top;
        const now = Date.now();
        if (!Number.isFinite(top) || !Number.isFinite(rect.height)) {
          cancel();
          return;
        }
        if (lastTop === undefined || Math.abs(top - lastTop) > 1 || Math.abs(rect.height - lastHeight) > 1 ||
            document.fonts?.status === 'loading') stableSince = now;
        lastTop = top;
        lastHeight = rect.height;
        if (now - stableSince >= settleTime) finish();
        else frame = window.requestAnimationFrame(measure);
      }

      inputEvents.forEach(type => window.addEventListener(type, cancel, { capture: true, passive: true }));
      window.addEventListener('pagehide', cancel);
      timer = window.setTimeout(cancel, 15000);

      return {
        cancel,
        activate() {
          if (!active || ready) return;
          ready = true;
          root.style.minHeight = previousMinHeight;
          if (Number.isFinite(saved.width) && Math.abs(saved.width - window.innerWidth) > 24) {
            cancel();
            return;
          }
          window.clearTimeout(timer);
          timer = window.setTimeout(finish, maxSettleTime);
          frame = window.requestAnimationFrame(measure);
        },
      };
    }
  };
})();
