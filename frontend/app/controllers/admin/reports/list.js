import Ember from 'ember';
import Controller from '@ember/controller';

const { inject } = Ember;

export default Controller.extend({
  queryParams : ['page'],
  page        : 1,
  notify      : inject.service('notify'),
  actions     : {
    nextPage() {
      let filters = {};
      filters.page = this.page + 1;
      this.get('store').query('admin-report', filters)
        .then(record => {
          this.set('reports', record);
          this.set('page', this.page + 1);
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
          })
          .catch(() => {
            this.notify.error('Unable to process request');
          });
      }
    }
  }
});
