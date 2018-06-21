import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';

module('Unit | Route | verify/email', function(hooks) {
  setupTest(hooks);

  test('it exists', function(assert) {
    let route = this.owner.lookup('route:verify/email');
    assert.ok(route);
  });
});
