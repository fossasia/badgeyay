import Component from '@ember/component';

export default Component.extend({
  init() {
    // To be inflated from the backend data
    this.fingerPrint = window.ASSET_FINGERPRINT_HASH;
    return this._super(...arguments);
  },
  click() {
    let imageId = this.get('image');
    if (imageId !== undefined) {
      this.get('sendDefImage')(imageId);
    }
  }
});

