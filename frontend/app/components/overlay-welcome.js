import Component from '@ember/component';

export default Component.extend({
  init() {
    this.visibility = 'visible';
    this._super(...arguments);
  },
  actions: {
    dismissOverlay() {
      this.set('visibility', 'none');
      this.get('removeFTL')();
    }
  }
});
