import Controller from '@ember/controller';
import Ember from 'ember';

const { inject } = Ember;

export default Controller.extend({
  queryParams : ['page'],
  page        : 1,
  state       : '',
  users       : null,
  allow_next  : true,
  allow_prev  : false,
  notify      : inject.service('notify'),
  actions     : {
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
            this.notify.error('No users found');
          }
        })
        .catch(() => {
          this.get('notify').error('Please try again!');
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
            this.get('notify').error('Please try again!');
          });
      } else {
        this.notify.error('Cannot Go Down');
      }
    }
  }
});
