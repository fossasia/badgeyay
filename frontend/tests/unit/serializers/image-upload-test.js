import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';

module('Unit | Serializer | image upload', function(hooks) {
  setupTest(hooks);

  // Replace this with your real tests.
  test('it exists', function(assert) {
    let store = this.owner.lookup('service:store');
    let serializer = store.serializerFor('image-upload');

    assert.ok(serializer);
  });

  test('it serializes records', function(assert) {
    let store = this.owner.lookup('service:store');
    let record = store.createRecord('image-upload', {});

    let serializedRecord = record.serialize();

    assert.ok(serializedRecord);
  });
});
