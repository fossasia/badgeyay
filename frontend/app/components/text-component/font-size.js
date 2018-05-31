import Component from '@ember/component';

export default Component.extend({
  init() {
    this.defFontSize = '';
    this.textZoom = false;
    this._super(...arguments);
  },

  input(defFontSize) {
    console.log('DefFontSize', this.defFontSize);
  },

  mouseUp() {
    console.log('Mouse up');
    this.set('textZoom', false);
  },

  mouseDown() {
    console.log('Mouse down');
    this.set('textZoom', true);
  }
});
