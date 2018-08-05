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
    this.fonttypeall = false;
    this.fontsizeall = false;
    this._super(...arguments);
  },

  click() {
    if (this.fonttypeall) {
      var temp_type = this.fonttype1 || this.fonttype2 || this.fonttype3 || this.fonttype4 || this.fonttype5;
      this.set('fonttype1', temp_type);
      this.set('fonttype2', temp_type);
      this.set('fonttype3', temp_type);
      this.set('fonttype4', temp_type);
      this.set('fonttype5', temp_type);
    }
    if (this.fontsizeall) {
      var temp_font = this.font1 || this.font2 || this.font3 || this.font4 || this.font5;
      this.set('font1', temp_font);
      this.set('font2', temp_font);
      this.set('font3', temp_font);
      this.set('font4', temp_font);
      this.set('font5', temp_font);
    }
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
    ]);
  },

  mouseUp() {
    this.set('textZoom', false);
  },

  mouseDown() {
    this.set('textZoom', true);
  }
});
