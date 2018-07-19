import Ember from 'ember';
import Controller from '@ember/controller';

const { inject } = Ember;

export default Controller.extend({
  queryParams : ['page'],
  page        : 1,
  state       : '',
  badges      : null,
  notify      : inject.service('notify'),
  actions     : {

    deleteBadge(badge) {
      badge.destroyRecord()
        .then(() => {
          this.notify.success('Badge Deleted successfully');
        })
        .catch(() => {
          this.notify.error('Unable to delete Badge');
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
          } else {
            this.notify.error('No badges found');
          }
        })
        .catch(() => {
          this.notify.error('Please try again!');
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
          })
          .catch(() => {
            this.get('notify').error('Please try again!');
          });
      } else {
        this.notify.error('Cannot Go Down');
      }
    }
  }
});
