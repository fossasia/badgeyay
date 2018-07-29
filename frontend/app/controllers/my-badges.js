import Controller from '@ember/controller';
import { inject as service } from '@ember/service';


export default Controller.extend({
  routing : service('-routing'),
  notify  : service('notify'),
  actions : {
    deleteBadge(badge) {
      badge.destroyRecord()
        .then(() => {
          this.notify.success('Badge Deleted successfully');
        })
        .catch(() => {
          this.notify.error('Unable to delete Badge');
        });
    },

    updateBadgeName(badge) {
      this.get('badge').save()
        .then(() => this.get('notify').success('Badge Name Successfully Updated!'));
    }
  }
});
