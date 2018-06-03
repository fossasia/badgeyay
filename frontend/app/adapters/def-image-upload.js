import DS from 'ember-data';
import ENV from '../config/environment';

const { APP } = ENV;
const { RESTAdapter } = DS;

export default RESTAdapter.extend({
  host        : APP.backLink,
  pathForType : () => {
    return 'api/upload/upload_default';
  }
});
