import Component from '@ember/component';

export default Component.extend({

  init() {
    this.EmberObject = Ember;
    this.defFontSize = '';
    this.textZoom = false;
    this.font1 = this.get('defFont1Size');
    this.font2 = this.get('defFont2Size');
    this.font3 = this.get('defFont3Size');
    this.font4 = this.get('defFont4Size');
    this.font5 = this.get('defFont5Size');
    this.fonttype1 = this.get('defFontType1');
    this.fonttype2 = this.get('defFontType2');
    this.fonttype3 = this.get('defFontType3');
    this.fonttype4 = this.get('defFontType4');
    this.fonttype5 = this.get('defFontType5');
    this.fontcol1 = this.get('defFontCol1');
    this.fontcol2 = this.get('defFontCol2');
    this.fontcol3 = this.get('defFontCol3');
    this.fontcol4 = this.get('defFontCol4');
    this.fontcol5 = this.get('defFontCol5');
    this.fonttypeall = false;
    this.fontsizeall = false;
    this._super(...arguments);
  },

  click() {
    if (this.EmberObject.$('[name="fontcolall"]')[0].checked === true) {
      var temp_col = this.fontcol1 || this.fontcol2 || this.fontcol3 || this.fontcol4 || this.fontcol5;
      this.set('fontcol1', temp_col);
      this.set('fontcol2', temp_col);
      this.set('fontcol3', temp_col);
      this.set('fontcol4', temp_col);
      this.set('fontcol5', temp_col);
      let sel1 = this.EmberObject.$('.ember-col-pick');
      for (let i = 1; i < sel1.length; i = i + 1) {
        this.EmberObject.$('#' + sel1[i].id)[0].style = 'pointer-events:none';
      }
    }
    if (this.EmberObject.$('[name="fontcolall"]')[0].checked === false) {
      let sel1 = this.EmberObject.$('.ember-col-pick');
      for (let i = 1; i < sel1.length; i = i + 1) {
        this.EmberObject.$('#' + sel1[i].id)[0].style = 'pointer-events:unset';
      }
    }
    if (this.EmberObject.$('[name="fonttypeall"]')[0].checked === true) {
      var temp_type = this.fonttype1 || this.fonttype2 || this.fonttype3 || this.fonttype4 || this.fonttype5;
      this.set('fonttype1', temp_type);
      this.set('fonttype2', temp_type);
      this.set('fonttype3', temp_type);
      this.set('fonttype4', temp_type);
      this.set('fonttype5', temp_type);
      let sel1 = this.EmberObject.$('.selection');
      for (let i = 1; i < sel1.length; i = i + 2) {
        this.EmberObject.$('#' + sel1[i].id)[0].style = 'pointer-events:none';
      }
    }
    if (this.EmberObject.$('[name="fonttypeall"]')[0].checked === false) {
      let sel1 = this.EmberObject.$('.selection');
      for (let j = 1; j < sel1.length; j = j + 2) {
        this.EmberObject.$('#' + sel1[j].id)[0].style = 'pointer-events:auto';
      }
    }
    if (this.EmberObject.$('[name="fontsizeall"]')[0].checked === true) {
      var temp_font = this.font1 || this.font2 || this.font3 || this.font4 || this.font5;
      this.set('font1', temp_font);
      this.set('font2', temp_font);
      this.set('font3', temp_font);
      this.set('font4', temp_font);
      this.set('font5', temp_font);
      let r = this.EmberObject.$('.selection');
      for (let i = 2; i < r.length; i = i + 2) {
        this.EmberObject.$('#' + r[i].id)[0].style = 'pointer-events:none';
      }
    }
    if (this.EmberObject.$('[name="fonttypeall"]')[0].checked === false) {
      let r = this.EmberObject.$('.selection');
      for (let i = 2; i < r.length; i = i + 2) {
        this.EmberObject.$('#' + r[i].id)[0].style = 'pointer-events:auto';
      }
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
    this.get('sendDefFontCol')([
      this.fontcol1,
      this.fontcol2,
      this.fontcol3,
      this.fontcol4,
      this.fontcol5
    ]);
  },

  mouseUp() {
    this.set('textZoom', false);
  },

  mouseDown() {
    this.set('textZoom', true);
  }
});
