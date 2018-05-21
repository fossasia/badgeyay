import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';

module('Unit | Route | create-badges', function(hooks) {
  setupTest(hooks);

  test('it exists', function(assert) {
    let route = this.owner.lookup('route:create-badges');
    assert.ok(route);
  });
});
