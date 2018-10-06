import Ember from 'ember';
import Controller from '@ember/controller';
const EmberObject = Ember;
const { inject } = Ember;

export default Controller.extend({
  queryParams   : ['page'],
  page          : 1,
  notifications : inject.service('notification-messages'),
  allow_next    : true,
  allow_prev    : false,
  allow         : true,
  allowprevpage : false,
  arrayno       : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  actions       : {
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
          this.get('notifications').clearAll();
          this.get('notifications').error('Unable to process request', {
            autoClear     : true,
            clearDuration : 1500
          });
        });
    },
    prevPage() {
      if (this.page <= 1) {
        this.get('notifications').clearAll();
        this.get('notifications').error('Cannot go down', {
          autoClear     : true,
          clearDuration : 1500
        });
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
            this.get('notifications').clearAll();
            this.get('notifications').error('Unable to process request', {
              autoClear     : true,
              clearDuration : 1500
            });
          });
      }
    },
    getPage(input) {
      let filters = {};
      filters.page = input;
      this.get('store').query('admin-report', filters)
        .then(record => {
          console.log(this.page);
          this.set('reports', record);
          this.set('page', input);
        })
        .catch(() => {
          this.get('notifications').clearAll();
          this.get('notifications').error('Unable to process request', {
            autoClear     : true,
            clearDuration : 1500
          });
        });
    },
    nextpages() {
      for (var r = 0; r < 10; r++) {
        EmberObject.set(this.arrayno, r, this.arrayno[r] + 10);
      }
      if (this.arrayno[0] > 1) {
        this.set('allowprevpage', true);
      }
      let filters = {};
      filters.page = this.arrayno[0];
      this.get('store').query('admin-report', filters)
        .then(record => {
          this.set('reports', record);
          this.set('page', this.arrayno[0]);
        })
        .catch(() => {
          this.get('notifications').clearAll();
          this.get('notifications').error('Unable to process request', {
            autoClear     : true,
            clearDuration : 1500
          });
        });
    },
    prevpages() {
      for (var r = 0; r < 10; r++) {
        EmberObject.set(this.arrayno, r, this.arrayno[r] - 10);
      }
      if (this.arrayno[0] <= 1) {
        this.set('allowprevpage', false);
      }
      let filters = {};
      filters.page = this.arrayno[0];
      this.get('store').query('admin-report', filters)
        .then(record => {
          this.set('reports', record);
          this.set('page', this.arrayno[0]);
        })
        .catch(() => {
          this.get('notifications').clearAll();
          this.get('notifications').error('Unable to process request', {
            autoClear     : true,
            clearDuration : 1500
          });
        });
    }
  }
});
