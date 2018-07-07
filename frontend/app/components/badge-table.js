import Component from '@ember/component';

export default Component.extend({
  actions: {
    prevPage() {
      this.get('prevPage')();
    },

    nextPage() {
      this.get('nextPage')();
    }
  }
});
