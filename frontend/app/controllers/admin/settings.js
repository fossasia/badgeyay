import Controller from '@ember/controller';
import Ember from 'ember';

const { inject } = Ember;

export default Controller.extend({
  notify  : inject.service('notify'),
  actions : {
    submit() {
      this.set('isLoading', true);
      const prevSettings = this.get('model');
      this.get('store').createRecord('setting', {
        appEnvironment        : prevSettings.appEnvironment,
        appName               : prevSettings.appName,
        secretKey             : prevSettings.secretKey,
        firebaseStorageBucket : prevSettings.firebaseStorageBucket,
        firebaseDatabaseURL   : prevSettings.firebaseDatabaseURL })
        .save()
        .then(record => {
          this.set('model', record);
          prevSettings.unloadRecord();
          this.notify.success('Updated successfully');
        })
        .catch(() => this.notify.error('Unable to update'))
        .finally(() => this.set('isLoading', false));
    }
  }
});
