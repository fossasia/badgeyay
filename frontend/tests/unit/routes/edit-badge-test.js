import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';

let originalAlert;

module('Unit | Route | edit-badge', function(hooks) {
  setupTest(hooks);

  test('it exists', function(assert) {
    let route = this.owner.lookup('route:edit-badge');
    assert.ok(route);

    route.send('setupController');
  });

  test('check functions', function(assert) {
    let route = this.owner.lookup('route:edit-badge');
    assert.equal(route.get('showProgress', 'true'));
    assert.equal(route.get('mode', 'create'));
    route.send('setupController');
    assert.equal(route.get('showProgress', 'false'));
    assert.equal(route.get('mode', 'edit'));
  });


});
