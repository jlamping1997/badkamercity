if (!customElements.get('product-modal')) {
  customElements.define(
    'product-modal',
    class ProductModal extends ModalDialog {
      constructor() {
        super();
        this.activeMediaIndex = 0;
        this.mobileView = window.matchMedia('(max-width: 749px)');
        this.swipeStart = null;
        this.onModalClick = this.onModalClick.bind(this);
        this.onModalPointerDown = this.onModalPointerDown.bind(this);
        this.onModalPointerUp = this.onModalPointerUp.bind(this);
        this.onModalKeyup = this.onModalKeyup.bind(this);
      }

      hide() {
        this.resetZoom();
        super.hide();
      }

      show(opener) {
        super.show(opener);
        this.showActiveMedia();
        this.addEventListeners();
      }

      showActiveMedia() {
        this.mediaItems.forEach((element) => element.classList.remove('active'));
        const activeMedia = this.querySelector(
          `.product-media-modal__content [data-media-id="${this.openedBy.getAttribute('data-media-id')}"]`
        );
        if (!activeMedia) return;
        this.activeMediaIndex = this.mediaItems.indexOf(activeMedia);
        this.resetZoom();
        const activeMediaTemplate = activeMedia.querySelector('template');
        const activeMediaContent = activeMediaTemplate ? activeMediaTemplate.content : null;
        activeMedia.classList.add('active');
        this.updateControls();

        if (
          activeMedia.nodeName == 'DEFERRED-MEDIA' &&
          activeMediaContent &&
          activeMediaContent.querySelector('.js-youtube')
        )
          activeMedia.loadContent();
      }

      get mediaItems() {
        return Array.from(this.querySelectorAll('.product-media-modal__content [data-media-id]'));
      }

      addEventListeners() {
        if (this.dataset.bcProductModalInitialized === 'true') return;
        this.dataset.bcProductModalInitialized = 'true';
        this.addEventListener('click', this.onModalClick);
        this.addEventListener('pointerdown', this.onModalPointerDown, { passive: true });
        this.addEventListener('pointerup', this.onModalPointerUp, true);
        this.addEventListener('pointercancel', () => { this.swipeStart = null; });
        this.addEventListener('keyup', this.onModalKeyup);
      }

      onModalClick(event) {
        const previousButton = event.target.closest('[data-product-modal-previous]');
        const nextButton = event.target.closest('[data-product-modal-next]');
        const zoomButton = event.target.closest('[data-product-modal-zoom]');
        const fullscreenButton = event.target.closest('[data-product-modal-fullscreen]');
        const thumbnailButton = event.target.closest('[data-product-modal-thumbnail]');
        const activeImage = event.target.closest('.product-media-modal__content img.active');

        if (previousButton) {
          event.preventDefault();
          this.showMediaAt(this.activeMediaIndex - 1);
          return;
        }

        if (nextButton) {
          event.preventDefault();
          this.showMediaAt(this.activeMediaIndex + 1);
          return;
        }

        if (zoomButton) {
          event.preventDefault();
          this.toggleZoom(this.querySelector('.product-media-modal__content img.active'));
          return;
        }

        if (fullscreenButton) {
          event.preventDefault();
          this.toggleFullscreen();
          return;
        }

        if (thumbnailButton) {
          event.preventDefault();
          this.showMediaById(thumbnailButton.dataset.mediaId);
          return;
        }

        if (activeImage && !this.mobileView.matches) {
          event.preventDefault();
          this.toggleZoom(activeImage);
        }
      }

      onModalPointerDown(event) {
        this.swipeStart = null;
        if (!event.isPrimary) return;
        if (this.mobileView.matches && (
          event.pointerType !== 'touch' ||
          !event.target.closest('.product-media-modal__content:not(.is-zoomed) img.active')
        )) return;
        this.swipeStart = { id: event.pointerId, x: event.clientX, y: event.clientY };
      }

      onModalPointerUp(event) {
        const isModalControl = event.target.closest(
          '.product-media-modal__content, .product-media-modal__nav, .product-media-modal__toggle, .product-media-modal__toolbar, .product-media-modal__thumbnails'
        );

        if (isModalControl) event.stopImmediatePropagation();

        const start = this.swipeStart;
        this.swipeStart = null;
        if (!start || start.id !== event.pointerId) return;

        const deltaX = event.clientX - start.x;
        const deltaY = event.clientY - start.y;

        if (Math.abs(deltaX) < 50 || Math.abs(deltaX) < Math.abs(deltaY)) return;

        if (deltaX < 0) {
          this.showMediaAt(this.activeMediaIndex + 1);
        } else {
          this.showMediaAt(this.activeMediaIndex - 1);
        }
      }

      onModalKeyup(event) {
        if (event.code === 'ArrowLeft') this.showMediaAt(this.activeMediaIndex - 1);
        if (event.code === 'ArrowRight') this.showMediaAt(this.activeMediaIndex + 1);
      }

      showMediaAt(index) {
        const mediaItems = this.mediaItems;
        if (!mediaItems.length) return;

        const nextIndex = (index + mediaItems.length) % mediaItems.length;

        mediaItems.forEach((element) => element.classList.remove('active'));
        mediaItems[nextIndex].classList.add('active');
        this.activeMediaIndex = nextIndex;
        this.resetZoom();
        this.updateControls();
      }

      toggleZoom(image) {
        if (!image) return;
        const content = this.querySelector('.product-media-modal__content');
        if (!content) return;
        const zoomed = image.classList.toggle('is-zoomed');
        content.classList.toggle('is-zoomed', zoomed);
        this.updateZoomControl(zoomed);
        if (this.mobileView.matches) {
          content.scrollLeft = zoomed ? (content.scrollWidth - content.clientWidth) / 2 : 0;
          content.scrollTop = zoomed ? (content.scrollHeight - content.clientHeight) / 2 : 0;
        }
      }

      toggleFullscreen() {
        if (!document.fullscreenElement) {
          this.requestFullscreen?.();
          return;
        }

        document.exitFullscreen?.();
      }

      showMediaById(mediaId) {
        const index = this.mediaItems.findIndex((element) => element.dataset.mediaId === mediaId);
        if (index === -1) return;
        this.showMediaAt(index);
      }

      resetZoom() {
        this.swipeStart = null;
        const content = this.querySelector('.product-media-modal__content');
        if (content) {
          content.querySelectorAll('img.is-zoomed').forEach((image) => image.classList.remove('is-zoomed'));
          content.classList.remove('is-zoomed');
          if (this.mobileView.matches) {
            content.scrollLeft = 0;
            content.scrollTop = 0;
          }
        }
        this.updateZoomControl(false);
      }

      updateZoomControl(zoomed) {
        const button = this.querySelector('[data-product-modal-zoom]');
        if (!button) return;
        button.setAttribute('aria-pressed', String(zoomed));
        button.setAttribute('aria-label', zoomed ? 'Uitzoomen' : 'Inzoomen');
      }

      updateControls() {
        const mediaItems = this.mediaItems;
        const counter = this.querySelector('[data-product-modal-counter]');
        const activeMedia = mediaItems[this.activeMediaIndex];

        if (counter) counter.textContent = `${this.activeMediaIndex + 1} / ${mediaItems.length}`;

        this.querySelectorAll('[data-product-modal-thumbnail]').forEach((thumbnail) => {
          const isActive = activeMedia && thumbnail.dataset.mediaId === activeMedia.dataset.mediaId;
          thumbnail.classList.toggle('is-active', isActive);
          thumbnail.setAttribute('aria-current', isActive ? 'true' : 'false');
        });
      }
    }
  );
}
