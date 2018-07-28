import Component from '@ember/component';
import Ember from 'ember';

const { inject } = Ember;

export default Component.extend({
  init() {
    this._super(...arguments);
  },
  queryParams : ['page'],
  page        : 1,
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
      if (this.page > 1) {
        filter.page = this.page + 1;
        this.get('store').query('my-badges', filter)
          .then(records => {
            if (records.length > 0) {
              this.set('my-badges', records);
              this.set('page', this.page + 1);
            } else {
              this.notify.error('No More Badges found');
            }
          })
          .catch(err => {
            this.get('notify').error('Please try again!');
          });
      } else {
        this.notify.error('No More Badges Found');
      }
    },
    prevPage() {
      let filter = {};
      if (this.page - 1 > 0) {
        filter.page = this.page - 1;
        this.get('store').query('my-badges', filter)
          .then(records => {
            this.set('my-badges', records);
            this.set('page', this.page - 1);
          })
          .catch(err => {
            this.get('notify').error('Please try again!');
          });
      } else {
        this.notify.error('No More Badges Found');
      }
    }
  }
});
