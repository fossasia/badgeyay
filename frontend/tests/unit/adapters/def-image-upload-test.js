import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';

module('Unit | Adapter | def image upload', function(hooks) {
  setupTest(hooks);

  // Replace this with your real tests.
  test('it exists', function(assert) {
    let adapter = this.owner.lookup('adapter:def-image-upload');
    assert.ok(adapter);
  });
});
