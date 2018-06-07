import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';

module('Unit | Adapter | my badges', function(hooks) {
  setupTest(hooks);

  // Replace this with your real tests.
  test('it exists', function(assert) {
    let adapter = this.owner.lookup('adapter:my-badges');
    assert.ok(adapter);
  });
});
