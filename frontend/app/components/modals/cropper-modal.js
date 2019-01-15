import Ember from 'ember';
import ModalBase from 'badgeyay/components/modals/modal-base';

const { run: { later } } = Ember;

export default ModalBase.extend({
  onVisible() {
    later(this, () => {
      const imageHeight = this.$('img').height();
      this.$('.content').css('height', `${imageHeight + 100}px`);
      this.$('.content').css('max-height', '400px');
      this.$('img').croppie({
        customClass : 'croppie',
        viewport    : {
          width  : this.get('width'),
          height : this.get('height'),
          type   : 'square'
        }
      });
    }, 200);
  },

  onHide() {
    this.$('img').croppie('destroy');
    const $img = this.$('img');
    if ($img.parent().is('div.croppie')) {
      $img.unwrap();
    }
  },

  actions: {
    resetImage() {
      this.onHide();
      this.onVisible();
    },
    cropImage() {
      this.$('img').croppie('result', 'base64', 'original', 'jpeg').then(result => {
        if (this.get('onImageCrop')) {
          this.onImageCrop(result);
        }
      });
    }
  }
});
