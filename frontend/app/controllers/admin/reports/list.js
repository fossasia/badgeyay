import Ember from 'ember';
import Controller from '@ember/controller';

const { inject } = Ember;

export default Controller.extend({
  queryParams : ['page'],
  page        : 1,
  notify      : inject.service('notify'),
  allow_next  : true,
  allow_prev  : false,
  actions     : {
    nextPage() {
      let filters = {};
      filters.page = this.page + 1;
      this.get('store').query('admin-report', filters)
        .then(record => {
          this.set('reports', record);
          this.set('page', this.page + 1);
          if (record.length < 9) {
            this.set('allow_next', false);
          } else {
            this.set('allow_next', true);
          }
          this.set('allow_prev', true);
        })
        .catch(() => {
          this.notify.error('Unable to process request');
        });
    },
    prevPage() {
      if (this.page <= 1) {
        this.notify.error('Cannot go down');
      } else {
        let filters = {};
        filters.page = this.page - 1;
        this.get('store').query('admin-report', filters)
          .then(record => {
            this.set('reports', record);
            this.set('page', this.page - 1);
            if (this.page === 1) {
              this.set('allow_prev', false);
            } else {
              this.set('allow_prev', true);
            }
            this.set('allow_next', true);
          })
          .catch(() => {
            this.notify.error('Unable to process request');
          });
      }
    }
  }
});
