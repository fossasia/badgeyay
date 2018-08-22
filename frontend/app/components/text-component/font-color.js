import Component from '@ember/component';

export default Component.extend({
  init() {
    this.defFontColor = '';
    this._super(...arguments);
  },

  focusOut() {
    this.get('sendDefFontColor')(this.get('defFontColor'));
  }
});
