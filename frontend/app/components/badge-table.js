import Component from '@ember/component';

import Ember from 'ember';

const { inject } = Ember;

export default Component.extend({
  init() {
    this._super(...arguments);
  },

  notifications: inject.service('notification-messages'),

  actions: {

    deleteBadge(badge) {
      badge.destroyRecord()
        .then(() => {
          this.get('notifications').clearAll();
          this.get('notifications').success('Badge Deleted successfully', {
            autoClear     : true,
            clearDuration : 1500
          });
        })
        .catch(() => {
          this.get('notifications').clearAll();
          this.get('notifications').error('Unable to delete Badge', {
            autoClear     : true,
            clearDuration : 1500
          });
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
