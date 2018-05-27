import Component from '@ember/component';

export default Component.extend({
  init() {
    this.defFontSize = '';
    this._super(...arguments);
  },

  input(defFontSize) {
    this.get('defFontSize', defFontSize);
  }
});
