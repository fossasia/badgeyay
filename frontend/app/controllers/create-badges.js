import Controller from '@ember/controller';

import { inject as service } from '@ember/service';

export default Controller.extend({
  routing : service('-routing'),
  actions : {
    mutateCSV(csvData) {
      let csv_ = this.get('store').createRecord('csv-file', {
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
