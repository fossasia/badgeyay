import Component from '@ember/component';

export default Component.extend({
  init() {
    this.defFontSize = '';
    this.textZoom = false;
    this._super(...arguments);
  },

  input(defFontSize) {
    this.get('sendDefSize')(this.defFontSize);
  },

  mouseUp() {
    this.set('textZoom', false);
  },

  mouseDown() {
    this.set('textZoom', true);
  }
});
