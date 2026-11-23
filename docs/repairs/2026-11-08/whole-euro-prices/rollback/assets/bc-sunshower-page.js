(() => {
  const initialize = root => {
    root.querySelectorAll('[data-ss-page]').forEach(page => {
      if (page.dataset.ready) return;
      page.dataset.ready = 'true';
      const preview = location.pathname.includes('products_preview') || Boolean(window.Shopify?.designMode);
      const requested = new URLSearchParams(location.search).get('bc_sunshower');
      if (preview && requested && requested !== page.dataset.source) {
        const retry = `ss-template-retry-${requested}`;
        if (!sessionStorage.getItem(retry)) { sessionStorage.setItem(retry,'1'); location.reload(); return; }
      } else if (requested) sessionStorage.removeItem(`ss-template-retry-${requested}`);
      const destination = item => {
        const target = new URL(preview && item.preview_url ? item.preview_url : item.url, location.origin);
        const url = new URL(target.pathname + target.search, location.origin);
        const theme = new URLSearchParams(location.search).get('preview_theme_id');
        if (theme) url.searchParams.set('preview_theme_id',theme);
        if (preview && item.source_product_id) url.searchParams.set('bc_sunshower',item.source_product_id);
        if (preview && item.selection) url.searchParams.set('view','sunshower');
        return url.href;
      };
      page.querySelectorAll('[data-ss-preview]').forEach(link => {
        if (preview && link.dataset.ssPreview) link.href = destination({url:link.href,preview_url:link.dataset.ssPreview,source_product_id:link.dataset.ssSource});
      });
      page.querySelectorAll('[data-ss-help]').forEach(button => {
        const help = document.getElementById(button.dataset.ssHelp);
        button.addEventListener('click',() => help.showModal());
        help.querySelector('[data-ss-close-help]').addEventListener('click',() => help.close());
        let backdropPointer = false;
        help.addEventListener('pointerdown',event => { backdropPointer = event.target === help; });
        help.addEventListener('click',event => { if (backdropPointer && event.target === help) help.close(); });
        help.addEventListener('close',() => button.focus({preventScroll:true}));
      });
      const choiceScrollKey = 'bc-sunshower-choice-scroll';
      const choiceRoute = value => {
        const url = new URL(value,location.origin);
        url.searchParams.delete('preview_theme_id');
        url.searchParams.sort();
        return url.pathname + url.search;
      };
      const captureChoicePosition = button => {
        const field = button.closest('[data-ss-field]');
        return {field:field.dataset.ssField,top:field.getBoundingClientRect().top,y:window.scrollY,width:window.innerWidth};
      };
      const rememberChoicePosition = (url,position) => {
        try {
          sessionStorage.setItem(choiceScrollKey,JSON.stringify({
            ...position,target:choiceRoute(url),time:Date.now()
          }));
          return true;
        } catch { return false; }
      };
      const restoreChoicePosition = () => {
        let saved;
        let targetRoute;
        try {
          saved = JSON.parse(sessionStorage.getItem(choiceScrollKey));
          sessionStorage.removeItem(choiceScrollKey);
          if (typeof saved?.target === 'string') targetRoute = choiceRoute(saved.target);
        } catch { return; }
        if (!saved || targetRoute !== choiceRoute(location.href) || !Number.isFinite(saved.time) || Date.now() - saved.time < 0 || Date.now() - saved.time > 30000 || !Number.isFinite(saved.y) || !Number.isFinite(saved.top)) return;
        const field = [...page.querySelectorAll('[data-ss-field]')].find(item => item.dataset.ssField === saved.field);
        if (!field) return;
        const restoration = window.BCChoicePosition?.prepare(field, saved);
        restoration?.activate();
      };
      restoreChoicePosition();
      let navigating = false;
      let adding = false;
      let uncertain = false;
      let catalog;
      const options = [...page.querySelectorAll('[data-ss-option]')];
      options.forEach(button => button.addEventListener('click', async () => {
        if (navigating || adding || uncertain || button.getAttribute('aria-pressed') === 'true') return;
        const position = captureChoicePosition(button);
        navigating = true;
        const status = page.querySelector('[data-ss-choice-status]');
        const selection = Object.fromEntries([...page.querySelectorAll('[data-ss-field]')].map(field => [field.dataset.ssField,field.querySelector('[aria-pressed="true"]').dataset.ssOption]));
        selection[button.closest('[data-ss-field]').dataset.ssField] = button.dataset.ssOption;
        options.forEach(option => { option.disabled = true; });
        const purchaseButtons = [...page.querySelectorAll('[type="submit"], [data-ss-add-set], [data-bc-wishlist-toggle]')];
        const disabledStates = purchaseButtons.map(control => control.disabled);
        purchaseButtons.forEach(control => { control.disabled = true; });
        status.textContent = page.dataset.loading;
        try {
          catalog ||= await fetch(page.dataset.catalog).then(response => { if (!response.ok) throw new Error('catalog'); return response.json(); });
          const match = catalog.products.find(item => Object.entries(selection).every(([key,value]) => item.selection[key] === value));
          if (!match) throw new Error('configuration');
          const url = new URL(destination(match));
          // Position restoration and native anchor scrolling must not compete.
          url.hash = rememberChoicePosition(url,position) ? '' : 'sunshower-configurator';
          location.assign(url.href);
        } catch {
          navigating = false;
          options.forEach(option => { option.disabled = false; });
          purchaseButtons.forEach((control,index) => { control.disabled = disabledStates[index]; });
          status.textContent = page.dataset.choiceError;
        }
      }));
      const gallery = page.querySelector('[data-ss-gallery]');
      const photoViewport = gallery?.querySelector('[data-ss-gallery-viewport]');
      const photoSlides = gallery ? [...gallery.querySelectorAll('[data-ss-gallery-slide]')] : [];
      if (photoViewport && photoSlides.length) {
        const photoButtons = [...gallery.querySelectorAll('[data-ss-photo]')];
        const photoStrip = gallery.querySelector('.ss-gallery__thumbs');
        const previousPhoto = gallery.querySelector('[data-ss-gallery-previous]');
        const nextPhoto = gallery.querySelector('[data-ss-gallery-next]');
        const photoCounter = gallery.querySelector('[data-ss-gallery-current]');
        const expandPhoto = gallery.querySelector('[data-ss-gallery-expand]');
        const reducePhotoMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
        let selectedPhoto = 0;
        let intendedPhoto = null;
        let photoScrollTimer;
        let photoPointer = null;
        let suppressPhotoClick = false;
        let photoViewer = null;
        let photoModulePromise = null;
        let openingPhotoViewer = false;
        let photoViewerIntent = null;
        const boundedPhoto = index => Math.max(0,Math.min(photoSlides.length - 1,index));
        const photoPosition = index => photoSlides[index].offsetLeft - photoSlides[0].offsetLeft;
        const shownPhoto = () => {
          if (!photoViewport.clientWidth) return selectedPhoto;
          return photoSlides.reduce((closest,slide,index) => Math.abs(photoPosition(index) - photoViewport.scrollLeft) < Math.abs(photoPosition(closest) - photoViewport.scrollLeft) ? index : closest,0);
        };
        const selectPhoto = (index,reveal = true) => {
          selectedPhoto = boundedPhoto(index);
          photoSlides.forEach((slide,number) => {
            slide.tabIndex = number === selectedPhoto ? 0 : -1;
            slide.setAttribute('aria-hidden',String(number !== selectedPhoto));
            if (Math.abs(number - selectedPhoto) <= 1) {
              const image = slide.querySelector('img');
              if (image) image.loading = 'eager';
            }
          });
          photoButtons.forEach((button,number) => {
            button.classList.toggle('is-selected',number === selectedPhoto);
            button.setAttribute('aria-pressed',String(number === selectedPhoto));
          });
          if (photoCounter) photoCounter.textContent = String(selectedPhoto + 1);
          if (previousPhoto) previousPhoto.disabled = selectedPhoto === 0;
          if (nextPhoto) nextPhoto.disabled = selectedPhoto === photoSlides.length - 1;
          const selectedButton = photoButtons[selectedPhoto];
          if (!reveal || !photoStrip || !selectedButton) return;
          const bounds = selectedButton.getBoundingClientRect();
          const stripBounds = photoStrip.getBoundingClientRect();
          const left = bounds.left < stripBounds.left ? bounds.left - stripBounds.left : bounds.right > stripBounds.right ? bounds.right - stripBounds.right : 0;
          if (left) photoStrip.scrollBy({left,behavior:'auto'});
        };
        const finishPhotoScroll = () => {
          clearTimeout(photoScrollTimer);
          selectPhoto(shownPhoto());
          if (intendedPhoto !== null && Math.abs(photoViewport.scrollLeft - photoPosition(intendedPhoto)) > 2) return;
          intendedPhoto = null;
        };
        const goToPhoto = (index,animate = true) => {
          const target = boundedPhoto(index);
          const smooth = animate && !reducePhotoMotion.matches;
          intendedPhoto = smooth ? target : null;
          photoViewport.scrollTo({left:photoPosition(target),behavior:smooth ? 'smooth' : 'instant'});
          if (!smooth) selectPhoto(target);
          clearTimeout(photoScrollTimer);
          photoScrollTimer = setTimeout(finishPhotoScroll,180);
        };
        const stepPhoto = direction => goToPhoto((intendedPhoto ?? shownPhoto()) + direction);
        previousPhoto?.addEventListener('click',() => stepPhoto(-1));
        nextPhoto?.addEventListener('click',() => stepPhoto(1));
        photoButtons.forEach((button,index) => button.addEventListener('click',() => goToPhoto(index)));
        photoViewport.addEventListener('scroll',() => {
          const index = shownPhoto();
          if (index !== selectedPhoto) selectPhoto(index);
          clearTimeout(photoScrollTimer);
          photoScrollTimer = setTimeout(finishPhotoScroll,140);
        },{passive:true});
        photoViewport.addEventListener('scrollend',finishPhotoScroll);
        photoViewport.addEventListener('wheel',event => {
          if (Math.abs(event.deltaX) > 0) intendedPhoto = null;
        },{passive:true});
        photoViewport.addEventListener('keydown',event => {
          const step = event.key === 'ArrowLeft' ? -1 : event.key === 'ArrowRight' ? 1 : 0;
          if (!step) return;
          event.preventDefault();
          const target = boundedPhoto((intendedPhoto ?? shownPhoto()) + step);
          goToPhoto(target,false);
          photoSlides[target].focus({preventScroll:true});
        });
        photoViewport.addEventListener('pointerdown',event => {
          suppressPhotoClick = false;
          intendedPhoto = null;
          photoPointer = event.isPrimary === false ? null : {id:event.pointerId,x:event.clientX,y:event.clientY,left:photoViewport.scrollLeft};
        },{passive:true});
        const trackPhotoPointer = event => {
          if (!photoPointer || event.pointerId !== photoPointer.id) return;
          if (Math.hypot(event.clientX - photoPointer.x,event.clientY - photoPointer.y) >= 10 || Math.abs(photoViewport.scrollLeft - photoPointer.left) >= 4) suppressPhotoClick = true;
        };
        photoViewport.addEventListener('pointermove',trackPhotoPointer,{passive:true});
        photoViewport.addEventListener('pointerup',event => { trackPhotoPointer(event); photoPointer = null; },{passive:true});
        photoViewport.addEventListener('pointercancel',() => { suppressPhotoClick = true; photoPointer = null; },{passive:true});
        photoViewport.addEventListener('dragstart',event => event.preventDefault());
        photoSlides.forEach(slide => {
          const image = slide.querySelector('img');
          const error = slide.querySelector('[data-ss-photo-error]');
          const showPhotoError = failed => {
            slide.classList.toggle('has-photo-error',failed);
            if (error) error.hidden = !failed;
          };
          image?.addEventListener('error',() => showPhotoError(true));
          image?.addEventListener('load',() => showPhotoError(false));
          if (image?.complete && !image.naturalWidth) showPhotoError(true);
        });
        const photoData = () => photoSlides.map(slide => {
          const image = slide.querySelector('img');
          return {
            src:slide.href,
            srcset:slide.dataset.ssFullSrcset,
            width:Number(slide.dataset.ssPhotoWidth),
            height:Number(slide.dataset.ssPhotoHeight),
            alt:slide.dataset.ssPhotoAlt || image?.alt || '',
            msrc:image?.currentSrc || image?.src,
            element:slide
          };
        });
        const openPhotoViewer = async (index,trigger) => {
          photoViewerIntent = {index:boundedPhoto(index),trigger};
          if (photoViewer) { photoViewer.goTo(photoViewerIntent.index); return; }
          if (openingPhotoViewer) return;
          openingPhotoViewer = true;
          try {
            photoModulePromise ||= import(new URL(gallery.dataset.viewerModule,location.href).href);
            const {default:PhotoSwipe} = await photoModulePromise;
            if (!page.isConnected) return;
            const intent = photoViewerIntent;
            const viewer = new PhotoSwipe({
              dataSource:photoData(),index:intent.index,mainClass:'bc-ss-viewer',loop:false,
              allowPanToNext:false,preload:[1,1],bgOpacity:0.96,
              showHideAnimationType:reducePhotoMotion.matches ? 'none' : 'fade',showAnimationDuration:reducePhotoMotion.matches ? 0 : 180,hideAnimationDuration:reducePhotoMotion.matches ? 0 : 180,
              zoomAnimationDuration:reducePhotoMotion.matches ? 0 : 200,closeOnVerticalDrag:false,pinchToClose:false,
              tapAction:false,imageClickAction:'zoom',doubleTapAction:'zoom',bgClickAction:'close',
              clickToCloseNonZoomable:false,trapFocus:true,returnFocus:true,escKey:true,arrowKeys:true,
              arrowPrev:photoSlides.length > 1,arrowNext:photoSlides.length > 1,counter:photoSlides.length > 1,
              closeTitle:gallery.dataset.closeLabel,zoomTitle:gallery.dataset.zoomLabel,
              arrowPrevTitle:gallery.dataset.previousLabel,arrowNextTitle:gallery.dataset.nextLabel,
              errorMsg:gallery.dataset.loadError,indexIndicatorSep:' / '
            });
            photoViewer = viewer;
            viewer.on('change',() => goToPhoto(viewer.currIndex,false));
            viewer.on('afterInit',() => {
              viewer.element.setAttribute('aria-label',gallery.dataset.galleryLabel);
              viewer.element.setAttribute('aria-modal','true');
            });
            viewer.on('destroy',() => {
              if (!page.isConnected) { photoViewer = null; return; }
              goToPhoto(viewer.currIndex,false);
              photoViewer = null;
              const returnTo = intent.trigger === expandPhoto ? expandPhoto : photoSlides[selectedPhoto];
              returnTo?.focus({preventScroll:true});
            });
            viewer.init();
          } catch {
            photoModulePromise = null;
            photoViewer = null;
            if (page.isConnected) location.assign(photoSlides[photoViewerIntent.index].href);
          } finally {
            openingPhotoViewer = false;
          }
        };
        photoViewport.addEventListener('click',event => {
          const slide = event.target.closest('[data-ss-open-image]');
          if (!slide || !photoViewport.contains(slide)) return;
          if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || event.button > 0) return;
          event.preventDefault();
          if (suppressPhotoClick && event.detail !== 0) { suppressPhotoClick = false; return; }
          openPhotoViewer(photoSlides.indexOf(slide),slide);
        });
        expandPhoto?.addEventListener('click',() => openPhotoViewer(shownPhoto(),expandPhoto));
        let photoViewportWidth = photoViewport.clientWidth;
        new ResizeObserver(() => {
          if (!page.isConnected || photoViewport.clientWidth === photoViewportWidth) return;
          photoViewportWidth = photoViewport.clientWidth;
          goToPhoto(selectedPhoto,false);
        }).observe(photoViewport);
        window.addEventListener('pageshow',event => {
          if (!event.persisted || !page.isConnected) return;
          intendedPhoto = null;
          photoPointer = null;
          suppressPhotoClick = false;
          selectPhoto(shownPhoto());
        });
        selectPhoto(shownPhoto(),false);
      }
      const description = page.querySelector('[data-ss-description]');
      const descriptionContent = page.querySelector('[data-ss-description-content]');
      const descriptionToggle = page.querySelector('[data-ss-description-toggle]');
      const descriptionSection = description.closest('.ss-description');
      const descriptionLabel = descriptionToggle.querySelector('[data-ss-description-label]');
      const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
      let descriptionExpanded = false;
      let descriptionAnimating = false;
      const collapsedHeight = () => parseFloat(getComputedStyle(descriptionSection).getPropertyValue('--ss-collapsed-height')) || 220;
      const fitDescription = () => {
        if (descriptionAnimating) return;
        const collapsible = descriptionContent.getBoundingClientRect().height > collapsedHeight() + 12;
        descriptionSection.classList.toggle('is-collapsible',collapsible);
        descriptionToggle.hidden = !collapsible;
        description.style.height = descriptionExpanded || !collapsible ? 'auto' : `${collapsedHeight()}px`;
      };
      const finishDescription = () => {
        descriptionAnimating = false;
        fitDescription();
        if (descriptionExpanded) description.style.height = 'auto';
        else {
          const bounds = descriptionToggle.getBoundingClientRect();
          if (document.activeElement === descriptionToggle && (bounds.bottom < 80 || bounds.top > innerHeight - 40)) descriptionToggle.scrollIntoView({block:'nearest',behavior:reducedMotion.matches ? 'instant' : 'smooth'});
        }
      };
      description.addEventListener('transitionend',event => { if (event.target === description && event.propertyName === 'height') finishDescription(); });
      descriptionToggle.addEventListener('click',() => {
        const from = description.getBoundingClientRect().height;
        descriptionExpanded = !descriptionExpanded;
        descriptionAnimating = !reducedMotion.matches;
        description.style.height = `${from}px`;
        void description.offsetHeight;
        descriptionSection.classList.toggle('is-expanded',descriptionExpanded);
        descriptionToggle.setAttribute('aria-expanded',String(descriptionExpanded));
        descriptionLabel.textContent = descriptionExpanded ? descriptionToggle.dataset.less : descriptionToggle.dataset.more;
        description.style.height = `${descriptionExpanded ? descriptionContent.getBoundingClientRect().height : collapsedHeight()}px`;
        if (reducedMotion.matches) finishDescription();
      });
      new ResizeObserver(fitDescription).observe(descriptionContent);
      fitDescription();
      const quantity = page.querySelector('[data-ss-quantity]');
      const extras = [...page.querySelectorAll('[data-ss-extra]')];
      const money = new Intl.NumberFormat(document.documentElement.lang || 'nl-NL',{style:'currency',currency:page.dataset.currency || 'EUR'});
      const parentQuantity = () => { const value = Number(quantity.value); return Number.isSafeInteger(value) && value > 0 ? value : 1; };
      const updateTotal = () => {
        const extraTotal = extras.filter(input => input.checked).reduce((sum,input) => sum + Number(input.closest('[data-ss-extra-row]').dataset.price),0);
        page.querySelector('[data-ss-total]').textContent = money.format((Number(page.dataset.price) * parentQuantity() + extraTotal) / 100);
      };
      page.querySelectorAll('[data-ss-step]').forEach(button => button.addEventListener('click',() => { quantity.value = Math.max(1,parentQuantity() + Number(button.dataset.ssStep)); updateTotal(); }));
      quantity.addEventListener('input',updateTotal);
      extras.forEach(input => input.addEventListener('change',updateTotal));
      const setButton = page.querySelector('[data-ss-add-set]');
      const setButtonLabel = setButton.textContent;
      const purchaseControls = [...page.querySelectorAll('[type="submit"], [data-ss-add-set]')];
      const initialPurchaseDisabled = purchaseControls.map(control => control.disabled);
      const setControls = [...new Set([...options, ...purchaseControls, quantity, ...extras, ...page.querySelectorAll('[data-ss-step]')])];
      page.addEventListener('submit', event => {
        if ((adding || uncertain || navigating) && purchaseControls.some(control => control.form === event.target)) {
          event.preventDefault();
          event.stopImmediatePropagation();
        }
      }, true);
      window.addEventListener('pageshow',event => {
        if (!event.persisted || !page.isConnected) return;
        if (adding || uncertain) {
          adding = false;
          uncertain = true;
          page.querySelector('[data-ss-cart-status]').textContent = page.dataset.cartError;
          page.querySelector('[data-ss-cart-check]').hidden = false;
          setButton.textContent = setButtonLabel;
          return;
        }
        navigating = false;
        options.forEach(option => { option.disabled = false; });
        purchaseControls.forEach((control,index) => { control.disabled = initialPurchaseDisabled[index]; });
        if (adding) extras.forEach(input => { input.checked = false; });
        adding = false;
        setButton.textContent = setButtonLabel;
        page.querySelector('[data-ss-choice-status]').textContent = '';
        updateTotal();
      });
      setButton.addEventListener('click',async () => {
        if (adding || navigating || uncertain) return;
        if (!quantity.checkValidity()) { quantity.reportValidity(); return; }
        const items = [{id:page.dataset.variant,quantity:parentQuantity()},...extras.filter(input => input.checked).map(input => ({id:input.closest('[data-ss-extra-row]').dataset.variant,quantity:1}))];
        const status = page.querySelector('[data-ss-cart-status]');
        const cartCheck = page.querySelector('[data-ss-cart-check]');
        adding = true;
        const original = setButton.textContent;
        setControls.forEach(control => { control.disabled = true; });
        setButton.textContent = page.dataset.busyLabel;
        status.textContent = '';
        cartCheck.hidden = true;
        try {
          const response = await fetch(page.dataset.addUrl,{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json'},body:JSON.stringify({items})});
          const result = await response.json();
          if (!response.ok || result.status) throw new Error('cart');
          location.assign(page.dataset.cartUrl);
        } catch {
          status.textContent = page.dataset.cartError;
          cartCheck.hidden = false;
          uncertain = true;
          setButton.textContent = original;
          adding = false;
        }
      });
      const sticky = page.querySelector('[data-ss-sticky]');
      const observer = new IntersectionObserver(entries => { const entry = entries[0]; sticky.hidden = entry.isIntersecting || entry.boundingClientRect.top > 0; },{threshold:0});
      observer.observe(page.querySelector('[data-ss-buybox]'));
      updateTotal();
    });
  };
  initialize(document);
  document.addEventListener('shopify:section:load',event => initialize(event.target));
})();
