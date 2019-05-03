import Component from '@ember/component';
import { computed } from '@ember/object';

export default Component.extend({
  init() {
    this._super(...arguments);
  },

  imageId: computed('idx', function() {
    return this.get('badge_back' + this.get('idx'));
  }),

  actions: {
    mutateCustomImg(value) {
      this.get('mutateCustomImg')(value);
    }
  }
});
