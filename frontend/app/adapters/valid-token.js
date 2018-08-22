import DS from 'ember-data';
import ENV from '../config/environment';
import { computed } from '@ember/object';
import { inject as service } from '@ember/service';

const { JSONAPIAdapter } = DS;
const { APP } = ENV;

export default JSONAPIAdapter.extend({
  host        : APP.backLink,
  pathForType : () => {
    return 'validate/token';
  }
});
