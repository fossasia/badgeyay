import DS from 'ember-data';
import { computed } from '@ember/object';

const { Model, attr } = DS;

export default Model.extend({
  superAdmin : attr('number'),
  registered : attr('number'),
  total      : computed('superAdmin', 'registered', function() {
    return this.get('superAdmin') + this.get('registered');
  })
});
