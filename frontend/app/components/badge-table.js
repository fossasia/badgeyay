import Component from '@ember/component';

import Ember from 'ember';

const { inject } = Ember;

export default Component.extend({
  init() {
    this._super(...arguments);
  },

  notify: inject.service('notify'),

  actions: {

    deleteBadge(badge) {
      badge.destroyRecord()
        .then(() => {
          this.notify.success('Badge Deleted successfully');
        })
        .catch(() => {
          this.notify.error('Unable to delete Badge');
        });
    },

    prevPage() {
      this.get('prevPage')();
    },

    nextPage() {
      this.get('nextPage')();
    }
  }
});
