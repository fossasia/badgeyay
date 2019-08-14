import { inject as service } from '@ember/service';
import Controller from '@ember/controller';

export default Controller.extend({
  notifications : service('notification-messages'),
  actions       : {
    submit() {
      this.set('isLoading', true);
      const prevSettings = this.get('model');
      this.get('store').createRecord('setting', {
        appEnvironment        : prevSettings.appEnvironment,
        appName               : prevSettings.appName,
        secretKey             : prevSettings.secretKey,
        firebaseStorageBucket : prevSettings.firebaseStorageBucket,
        firebaseDatabaseURL   : prevSettings.firebaseDatabaseURL,
        sendGridApiKey        : prevSettings.sendGridApiKey,
        fromMail              : prevSettings.fromMail })
        .save()
        .then(record => {
          this.set('model', record);
          prevSettings.unloadRecord();
          this.get('notifications').success('Updated successfully', {
            autoClear     : true,
            clearDuration : 1500
          });
        })
        .catch(() => this.get('notifications').error('Unable to update', {
          autoClear     : true,
          clearDuration : 1500
        }))
        .finally(() => this.set('isLoading', false));
    }
  }
});
