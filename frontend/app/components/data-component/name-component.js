import Component from '@ember/component';

export default Component.extend({
  init() {
    this._super(...arguments);
  },
  keyUp() {
    this.get('sendName')(this.get('formNameData'));
  }
});
