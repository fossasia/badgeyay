import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';
import { equal } from 'assert';

module('Unit | Controller | edit-badge', function(hooks) {
  setupTest(hooks);

  test('it exists', function(assert) {
    let controller = this.owner.lookup('controller:edit-badge');
    assert.ok(controller);
  });
  test('check functions', function(assert) {
    var ctrl = this.subject();
    assert.equal(ctrl.get('csvChange', 'true'));
    ctrl.send('csvChange');
    assert.equal(ctrl.get('csvChange', 'false'));
    assert.equal(ctrl.get('logoImgChanged', 'true'));
    assert.equal(ctrl.get('custLogoUmage', 'true'));
    ctrl.send('logoChange');
    assert.equal(ctrl.get('logoImgChanged', 'false'));
    assert.equal(ctrl.get('custLogoUmage', 'false'));
  });
});
