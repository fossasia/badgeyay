import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';

module('Unit | Adapter | bg color', function(hooks) {
  setupTest(hooks);

  // Replace this with your real tests.
  test('it exists', function(assert) {
    let adapter = this.owner.lookup('adapter:bg-color');
    assert.ok(adapter);
  });
});
