import { inject as service } from '@ember/service';
import Controller from '@ember/controller';

export default Controller.extend({
  queryParams   : ['page'],
  page          : 1,
  state         : '',
  users         : null,
  allow_next    : true,
  allow_prev    : false,
  allow         : true,
  notifications : service('notification-messages'),
  actions       : {
    nextPage() {
      let filter = {};
      filter.page = this.page + 1;
      filter.state = this.state;
      this.get('store')
        .query('all-user', filter)
        .then(records => {
          if (records.length > 0) {
            this.set('page', filter.page);
            this.set('users', records);
            if (records.length < 10) {
              this.set('allow_next', false);
            } else {
              this.set('allow_next', true);
            }
            this.set('allow_prev', true);
          } else {
            this.get('notifications').error('No users found', {
              autoClear     : true,
              clearDuration : 1500
            });
          }
        })
        .catch(() => {
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
        this.get('store')
          .query('all-user', filter)
          .then(records => {
            this.set('page', filter.page);
            this.set('users', records);
            if (this.page === 1) {
              this.set('allow_prev', false);
            } else {
              this.set('allow_prev', true);
            }
            this.set('allow_next', true);

          })
          .catch(() => {
            this.get('notifications').error('Please try again!', {
              autoClear     : true,
              clearDuration : 1500
            });
          });
      } else {
        this.get('notifications').error('Cannot Go Down', {
          autoClear     : true,
          clearDuration : 1500
        });
      }
    }
  }
});
