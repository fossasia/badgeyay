import Component from '@ember/component';

export default Component.extend({
  actions: {
    mutateBadgeSize(value) {
      this.get('sendBadgeSize')(value);
    }
  }
});
