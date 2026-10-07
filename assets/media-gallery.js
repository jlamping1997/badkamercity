if (!customElements.get('media-gallery')) {
  customElements.define(
    'media-gallery',
    class MediaGallery extends HTMLElement {
      constructor() {
        super();
        this.elements = {
          liveRegion: this.querySelector('[id^="GalleryStatus"]'),
          viewer: this.querySelector('[id^="GalleryViewer"]'),
          thumbnails: this.querySelector('[id^="GalleryThumbnails"]'),
        };
        this.mql = window.matchMedia('(min-width: 750px)');
        if (!this.elements.thumbnails) return;

        // These arrows select media, including when every thumbnail fits in the strip.
        this.elements.thumbnails.enableSliderLooping = true;
        this.elements.thumbnails.querySelectorAll(':scope > .slider-button').forEach((button) => {
          button.disabled = this.elements.thumbnails.querySelectorAll('[data-target]').length < 2;
          button.setAttribute('aria-label', button.name === 'next' ? 'Volgende productfoto' : 'Vorige productfoto');
          button.setAttribute('aria-controls', this.elements.viewer.id);
          button.classList.remove('small-hide', 'medium-hide', 'large-up-hide');
        });
        this.elements.thumbnails.addEventListener('click', this.onThumbnailNavigation.bind(this), true);

        this.elements.viewer.addEventListener('slideChanged', this.onSlideChanged.bind(this));
        this.elements.thumbnails.querySelectorAll('[data-target]').forEach((mediaToSwitch) => {
          mediaToSwitch
            .querySelector('button')
            .addEventListener('click', this.setActiveMedia.bind(this, mediaToSwitch.dataset.target, false));
        });
        if (this.dataset.desktopLayout.includes('thumbnail') && this.mql.matches) this.removeListSemantic();
      }

      onSlideChanged(event) {
        // Desktop shows one active item; hidden slides do not have reliable scroll offsets.
        if (this.mql.matches && this.dataset.desktopLayout.includes('thumbnail')) return;
        const currentElement = event.detail.currentElement;
        if (!currentElement) return;
        this.elements.viewer.querySelectorAll('[data-media-id]').forEach((item) => {
          item.classList.toggle('is-active', item === currentElement);
        });
        const thumbnail = this.elements.thumbnails.querySelector(
          `[data-target="${currentElement.dataset.mediaId}"]`
        );
        this.setActiveThumbnail(thumbnail);
      }

      onThumbnailNavigation(event) {
        const button = event.target.closest('.slider-button');
        if (!button || button.parentElement !== this.elements.thumbnails) return;
        event.preventDefault();
        // Do not also invoke SliderComponent's thumbnail-strip scrolling handler.
        event.stopImmediatePropagation();
        const thumbnails = Array.from(this.elements.thumbnails.querySelectorAll('[data-target]')).filter(
          (item) => getComputedStyle(item).display !== 'none' &&
            this.elements.viewer.querySelector(`[data-media-id="${item.dataset.target}"]`)
        );
        if (thumbnails.length < 2) return;
        const activeId = this.elements.viewer.querySelector('[data-media-id].is-active')?.dataset.mediaId;
        const current = thumbnails.findIndex((item) => item.dataset.target === activeId);
        const step = button.name === 'next' ? 1 : -1;
        const index = (current + step + thumbnails.length) % thumbnails.length;
        this.setActiveMedia(thumbnails[index].dataset.target, false);
      }

      setActiveMedia(mediaId, prepend) {
        const activeMedia =
          this.elements.viewer.querySelector(`[data-media-id="${mediaId}"]`) ||
          this.elements.viewer.querySelector('[data-media-id]');
        if (!activeMedia) {
          return;
        }
        this.elements.viewer.querySelectorAll('[data-media-id]').forEach((element) => {
          element.classList.remove('is-active');
        });
        activeMedia?.classList?.add('is-active');

        if (prepend) {
          activeMedia.parentElement.firstChild !== activeMedia && activeMedia.parentElement.prepend(activeMedia);

          if (this.elements.thumbnails) {
            const activeThumbnail = this.elements.thumbnails.querySelector(`[data-target="${mediaId}"]`);
            activeThumbnail.parentElement.firstChild !== activeThumbnail && activeThumbnail.parentElement.prepend(activeThumbnail);
          }

          if (this.elements.viewer.slider) this.elements.viewer.resetPages();
        }

        this.preventStickyHeader();
        window.setTimeout(() => {
          if (!this.mql.matches || this.elements.thumbnails) {
            activeMedia.parentElement.scrollTo({ left: activeMedia.offsetLeft });
          }
          const activeMediaRect = activeMedia.getBoundingClientRect();
          // Don't scroll if the image is already in view
          if (activeMediaRect.top > -0.5) return;
          const top = activeMediaRect.top + window.scrollY;
          window.scrollTo({ top: top, behavior: 'smooth' });
        });
        this.playActiveMedia(activeMedia);

        if (!this.elements.thumbnails) return;
        const activeThumbnail = this.elements.thumbnails.querySelector(`[data-target="${mediaId}"]`);
        this.setActiveThumbnail(activeThumbnail);
        this.announceLiveRegion(activeMedia, activeThumbnail.dataset.mediaPosition);
      }

      setActiveThumbnail(thumbnail) {
        if (!this.elements.thumbnails || !thumbnail) return;

        this.elements.thumbnails
          .querySelectorAll('button')
          .forEach((element) => element.removeAttribute('aria-current'));
        thumbnail.querySelector('button').setAttribute('aria-current', true);
        if (this.elements.thumbnails.isSlideVisible(thumbnail, 10)) return;

        this.elements.thumbnails.slider.scrollTo({ left: thumbnail.offsetLeft });
      }

      announceLiveRegion(activeItem, position) {
        const image = activeItem.querySelector('.product__modal-opener--image img');
        if (!image) return;
        image.onload = () => {
          this.elements.liveRegion.setAttribute('aria-hidden', false);
          this.elements.liveRegion.innerHTML = window.accessibilityStrings.imageAvailable.replace('[index]', position);
          setTimeout(() => {
            this.elements.liveRegion.setAttribute('aria-hidden', true);
          }, 2000);
        };
        image.src = image.src;
      }

      playActiveMedia(activeItem) {
        window.pauseAllMedia();
        const deferredMedia = activeItem.querySelector('.deferred-media');
        if (deferredMedia) deferredMedia.loadContent(false);
      }

      preventStickyHeader() {
        this.stickyHeader = this.stickyHeader || document.querySelector('sticky-header');
        if (!this.stickyHeader) return;
        this.stickyHeader.dispatchEvent(new Event('preventHeaderReveal'));
      }

      removeListSemantic() {
        if (!this.elements.viewer.slider) return;
        this.elements.viewer.slider.setAttribute('role', 'presentation');
        this.elements.viewer.sliderItems.forEach((slide) => slide.setAttribute('role', 'presentation'));
      }
    }
  );
}
