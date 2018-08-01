import Controller from '@ember/controller';
import Ember from 'ember';

const { $, inject } = Ember;

export default Controller.extend({
  notify  : inject.service('notify'),
  actions : {
    openModal(message) {
      $('.ui.admin-message.modal').modal('show');
      this.set('selectedMsg', message);
    },

    editMessage(element, component) {
      this.set('isModalLoading', true);
      this.get('selectedMsg')
        .save()
        .then(() => this.notify.success('Updated'))
        .catch(() => this.notify.error('Unable to Update'))
        .finally(() => {
          $('.ui.admin-message.modal').modal('hide');
          this.set('isModalLoading', false);
        });
    },

    denyModal(element, component) {
      return true;
    }
  }
});
