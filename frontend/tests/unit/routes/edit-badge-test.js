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
    var ctrl = this.subject();
    assert.equal(ctrl.get('showProgress', 'true'));
    assert.equal(ctrl.get('showProgress', 'create'));
    ctrl.send('setupController');
    assert.equal(ctrl.get('showProgress', 'false'));
    assert.equal(ctrl.get('showProgress', 'edit'));
  });


  test('check frontend', function(assert) {

  });
});
