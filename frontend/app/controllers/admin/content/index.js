import Controller from '@ember/controller';
import Ember from 'ember';

const { inject } = Ember;

export default Controller.extend({
  notify  : inject.service('notify'),
  actions : {
    submitForm() {
      this.get('model')
        .save()
        .then(() => {
          this.notify.success('Update successfully');
        })
        .catch(() => {
          this.notify.error('Unable to update');
        });
    }
  }
});
