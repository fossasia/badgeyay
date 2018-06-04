import DS from 'ember-data';
import Ember from 'ember';

const { JSONAPIAdapter } = DS;
const { inject: { service } } = Ember;

export default JSONAPIAdapter.extend({
  notify: service(),

  isInvalid() {
    this.get('notify').error('An unexpected error occurred. Please try again later.', {
      closeAfter: 5000
    });
  }
});
