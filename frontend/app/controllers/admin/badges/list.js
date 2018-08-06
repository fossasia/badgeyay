import Ember from 'ember';
import Controller from '@ember/controller';

const { inject } = Ember;

export default Controller.extend({
  queryParams   : ['page'],
  page          : 1,
  state         : '',
  badges        : null,
  allow_next    : true,
  allow_prev    : false,
  allow         : true,
  notifications : inject.service('notification-messages'),
  actions       : {

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

    nextPage() {
      let filter = {};
      filter.page = this.page + 1;
      filter.state = this.state;
      this.get('store').query('all-admin-badge', filter)
        .then(records => {
          if (records.length > 0) {
            this.set('page', filter.page);
            this.set('badges', records);
            if (records.length < 10) {
              this.set('allow_next', false);
            } else {
              this.set('allow_next', true);
            }
            this.set('allow_prev', true);
          } else {
            this.get('notifications').clearAll();
            this.get('notifications').error('No badges found', {
              autoClear     : true,
              clearDuration : 1500
            });
          }
        })
        .catch(() => {
          this.get('notifications').clearAll();
          this.get('notifications').error('Please try again!', {
            autoClear     : true,
            clearDuration : 1500
          });
        });
    },

    prevPage() {
      let filter = {};
      if (this.page - 1 > 0) {
        filter.page = this.page - 1;
        filter.state = this.state;
        this.get('store').query('all-admin-badge', filter)
          .then(records => {
            this.set('page', this.page - 1);
            this.set('badges', records);
            if (this.page === 1) {
              this.set('allow_prev', false);
            } else {
              this.set('allow_prev', true);
            }
            this.set('allow_next', true);
          })
          .catch(() => {
            this.get('notifications').clearAll();
            this.get('notifications').error('Please try again!', {
              autoClear     : true,
              clearDuration : 1500
            });
          });
      } else {
        this.get('notifications').clearAll();
        this.get('notifications').error('Cannot Go Down', {
          autoClear     : true,
          clearDuration : 1500
        });
      }
    }
  }
});
