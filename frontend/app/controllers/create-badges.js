import Controller from '@ember/controller';

import { inject as service } from '@ember/service';

export default Controller.extend({
  routing : service('-routing'),
  actions : {
    mutateCSV(csvData) {
      const user = this.get('store').peekAll('user');
      let uid;
      user.forEach(user_ => {
        uid = user_.get('id');
      });
      let csv_ = this.get('store').createRecord('csv-file', {
        uid,
        csvFile   : csvData,
        extension : 'csv'
      });
      csv_.save();
    },

    mutateText(txtData) {
      console.log(txtData);
    }
  }
});
