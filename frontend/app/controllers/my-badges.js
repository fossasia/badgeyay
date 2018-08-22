import Controller from '@ember/controller';
import { inject as service } from '@ember/service';


export default Controller.extend({
  routing       : service('-routing'),
  notifications : service('notification-messages'),
  actions       : {
    deleteBadge(badge) {
      badge.destroyRecord()
        .then(() => {
          this.get('notifications').success('Badge Deleted successfully', {
            autoClear     : true,
            clearDuration : 1500
          });
        })
        .catch(() => {
          this.get('notifications').error('Unable to delete Badge', {
            autoClear     : true,
            clearDuration : 1500
          });
        });
    },

    updateBadgeName(badge) {
      badge.save()
        .then(() => this.get('notifications').success('Badge Name Successfully Updated!', {
          autoClear     : true,
          clearDuration : 1500
        }));
    }
  }
});
