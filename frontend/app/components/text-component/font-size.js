import Component from '@ember/component';

export default Component.extend({
  init() {
    this.defFontSize = '';
    this.textZoom = false;
    this.font1 = '';
    this.font2 = '';
    this.font3 = '';
    this.font4 = '';
    this.font5 = '';
    this.fonttype1 = '';
    this.fonttype2 = '';
    this.fonttype3 = '';
    this.fonttype4 = '';
    this.fonttype5 = '';
    this._super(...arguments);
  },

  click() {
    this.get('sendDefSize')([
      this.font1,
      this.font2,
      this.font3,
      this.font4,
      this.font5
    ]);
    this.get('sendDefFont')([
      this.fonttype1,
      this.fonttype2,
      this.fonttype3,
      this.fonttype4,
      this.fonttype5
    ])
  },

  mouseUp() {
    this.set('textZoom', false);
  },

  mouseDown() {
    this.set('textZoom', true);
  }
});
