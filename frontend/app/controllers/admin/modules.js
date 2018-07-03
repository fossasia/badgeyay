import Controller from '@ember/controller';
import Ember from 'ember';

const { inject } = Ember;

export default Controller.extend({
  notify  : inject.service('notify'),
  actions : {
    submit() {
      let modules = this.get('model');
      this.set('isLoading', true);
      modules.save()
        .then(() => {
          this.notify.success('Settings have been saved successfully.');
        })
        .catch(() => {
          this.notify.error('An unexpected error has occurred. Settings not saved.');
        })
        .finally(() => {
          this.set('isLoading', false);
        });
    }
  }
});
