import Component from '@ember/component';

export default Component.extend({
  init() {
    this.defValue = '';
    this._super(...arguments);
  },
  focusOut() {
    this.get('sendDefColor')(this.get('defColor'));
  }
});

