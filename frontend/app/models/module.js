import DS from 'ember-data';

const { Model, attr } = DS;

export default Model.extend({
  ticketInclude   : attr('boolean'),
  paymentInclude  : attr('boolean'),
  donationInclude : attr('boolean')
});
