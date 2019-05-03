import Component from '@ember/component';
import Ember from 'ember';
import $ from 'jquery';

const { inject } = Ember;

export default Component.extend({
  init() {
    this._super(...arguments);
  },
  queryParams   : ['page'],
  page          : 1,
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

    sendBadgeName(badge) {
      this.get('sendBadgeName')(badge);
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
              this.get('notifications').clearAll();
              this.get('notifications').error('No More Badges found', {
                autoClear     : true,
                clearDuration : 1500
              });
            }
          })
          .catch(err => {
            this.get('notifications').clearAll();
            this.get('notifications').error('Please try again!', {
              autoClear     : true,
              clearDuration : 1500
            });
          });
      } else {
        this.get('notifications').clearAll();
        this.get('notifications').error('No More Badges Found', {
          autoClear     : true,
          clearDuration : 1500
        });
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
            this.get('notifications').clearAll();
            this.get('notifications').error('Please try again!', {
              autoClear     : true,
              clearDuration : 1500
            });
          });
      } else {
        this.get('notifications').clearAll();
        this.get('notifications').error('No More Badges Found', {
          autoClear     : true,
          clearDuration : 1500
        });
      }
    },
    batchdownload() {
      var arr = $('.checkbox');
      var r = 0;
      var timeout = setInterval(function() {
        while (r < arr.length) {
          if (arr[r].checked === true) {
            window.open(arr[r].id, '_blank');
          }
          r = r + 1;
        }
        if (arr.length == r) {
          clearInterval(timeout);
        }
      }, 1000);
    }
  }
});

