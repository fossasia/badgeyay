import DS from 'ember-data';
import ENV from '../config/environment';

const { APP } = ENV;
const { JSONAPIAdapter } = DS;

export default JSONAPIAdapter.extend({
  host        : APP.backLink,
  pathForType : () => {
    return 'admin/show_all_users';
  }
});
