import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';

module('Unit | Adapter | text data', function(hooks) {
  setupTest(hooks);

  // Replace this with your real tests.
  test('it exists', function(assert) {
    let adapter = this.owner.lookup('adapter:text-data');
    assert.ok(adapter);
  });
});
