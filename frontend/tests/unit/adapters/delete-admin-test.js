import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';

module('Unit | Adapter | delete admin', function(hooks) {
  setupTest(hooks);

  // Replace this with your real tests.
  test('it exists', function(assert) {
    let adapter = this.owner.lookup('adapter:delete-admin');
    assert.ok(adapter);
  });
});
