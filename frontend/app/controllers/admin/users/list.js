import Controller from '@ember/controller';
import Ember from 'ember';

const { inject } = Ember;

export default Controller.extend({
  queryParams : ['page'],
  page        : 1,
  state       : '',
  users       : null,
  notify      : inject.service('notify'),
  actions     : {
    nextPage() {
      let filter = {};
      filter.page = this.page + 1;
      filter.state = this.state;
      this.get('store').query('all-user', filter)
        .then(records => {
          if (records.length > 0) {
            this.set('users', records);
            this.set('page', this.page + 1);
          } else {
            this.notify.error('No users found');
          }
        })
        .catch(err => {
          console.log(err);
        });
    },
    prevPage() {
      let filter = {};
      if (this.page - 1 > 0) {
        filter.page = this.page - 1;
        filter.state = this.state;
        this.get('store').query('all-user', filter)
          .then(records => {
            this.set('users', records);
            this.set('page', this.page - 1);
          })
          .catch(err => {
            console.log(err);
          });
      } else {
        this.notify.error('Cannot Go Down');
      }
    }
  }
});
