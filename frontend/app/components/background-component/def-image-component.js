import Component from '@ember/component';

export default Component.extend({
  init() {
    // To be inflated from the backend data
    this.host = 'http://localhost:5000/';
    return this._super(...arguments);
  },
  click() {
    let imageId = this.get('image');
    if (imageId !== undefined) {
      this.get('sendDefImage')(imageId);
    }
  }
});

