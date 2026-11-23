/* Phone layout helpers. IR/UV cards use native links straight to the configurator. */
(function () {
  'use strict';
  if (window.BCSunshowerMobileLight) {
    window.BCSunshowerMobileLight.init(document);
    return;
  }

  var instances = new Map();
  var rootSelector = '[data-bcsse-mobile-light]';

  function createController(root) {
    var media = window.matchMedia('(max-width: 749px)');
    var overview = root.querySelector('[data-bcsse-light-overview]');
    var mobileContent = root.querySelector('.bcsse-mobile-light');
    var modelDisclosure = root.querySelector('[data-bcsse-model-disclosure]');
    var modelSummary = modelDisclosure && modelDisclosure.querySelector('summary');
    var shelf = root.querySelector('[data-bcsse-accessory-shelf]');
    var originalShelfTabIndex = shelf && shelf.getAttribute('tabindex');
    var heroCopy = root.querySelector('.bcsse-hero__copy');
    var title = document.getElementById('bcsse-title-' + root.dataset.bcsseSectionId);
    var modelsHash = '#bcsse-models-' + root.dataset.bcsseSectionId;
    var destroyed = false;

    function update() {
      if (destroyed) return;
      // Old detail hashes must never hide these direct configurator links.
      if (overview) overview.hidden = false;
      delete root.dataset.bcsseLightView;
      if (shelf) shelf.tabIndex = media.matches ? 0 : -1;
      if (modelDisclosure && (!media.matches || window.location.hash === modelsHash)) {
        modelDisclosure.open = true;
      }
    }

    function onClick(event) {
      if (!media.matches || event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      var target = event.target && event.target.closest && event.target.closest('a');
      if (target && root.contains(target) && target.getAttribute('href') === modelsHash && modelDisclosure) {
        modelDisclosure.open = true;
      }
      // In particular, do not intercept IR/UV product links or change history.
    }

    function onMediaChange() {
      if (destroyed) return;
      var active = document.activeElement;
      var willHidePhoneFocus = !media.matches && ((mobileContent && mobileContent.contains(active)) || active === modelSummary || active === shelf);
      var willHideHeroFocus = media.matches && heroCopy && heroCopy.contains(active) && active !== title;
      var willHideModelFocus = media.matches && modelDisclosure && modelDisclosure.contains(active) && active !== modelSummary && window.location.hash !== modelsHash;
      if (modelDisclosure) modelDisclosure.open = !media.matches || window.location.hash === modelsHash;
      update();
      if ((willHidePhoneFocus || willHideHeroFocus) && title) title.focus({ preventScroll: true });
      else if (willHideModelFocus && modelSummary) modelSummary.focus({ preventScroll: true });
    }

    root.addEventListener('click', onClick);
    window.addEventListener('hashchange', update);
    window.addEventListener('popstate', update);
    if (media.addEventListener) media.addEventListener('change', onMediaChange);
    else media.addListener(onMediaChange);
    root.dataset.bcsseMobileReady = 'true';
    onMediaChange();

    return {
      destroy: function () {
        destroyed = true;
        root.removeEventListener('click', onClick);
        window.removeEventListener('hashchange', update);
        window.removeEventListener('popstate', update);
        if (media.removeEventListener) media.removeEventListener('change', onMediaChange);
        else media.removeListener(onMediaChange);
        if (overview) overview.hidden = false;
        if (modelDisclosure) modelDisclosure.open = true;
        if (shelf) {
          if (originalShelfTabIndex === null) shelf.removeAttribute('tabindex');
          else shelf.setAttribute('tabindex', originalShelfTabIndex);
        }
        delete root.dataset.bcsseMobileReady;
        delete root.dataset.bcsseLightView;
      }
    };
  }

  function init(scope) {
    var roots = Array.from(scope.querySelectorAll(rootSelector));
    if (scope.matches && scope.matches(rootSelector)) roots.unshift(scope);
    roots.forEach(function (root) {
      if (!instances.has(root)) instances.set(root, createController(root));
    });
  }

  document.addEventListener('shopify:section:load', function (event) { init(event.target); });
  document.addEventListener('shopify:section:unload', function (event) {
    instances.forEach(function (controller, root) {
      if (event.target === root || event.target.contains(root)) {
        controller.destroy();
        instances.delete(root);
      }
    });
  });
  window.BCSunshowerMobileLight = { init: init };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { init(document); }, { once: true });
  else init(document);
})();
