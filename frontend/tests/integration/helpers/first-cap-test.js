import { module, test } from 'qunit';
import { setupRenderingTest } from 'ember-qunit';
import { render } from '@ember/test-helpers';
import hbs from 'htmlbars-inline-precompile';

module('Integration | Helper | firstCap', function(hooks) {
  setupRenderingTest(hooks);

  // Replace this with your real tests.
  test('it renders', async function(assert) {
    this.set('inputValue', 'badgeyay');

    await render(hbs`{{first-cap inputValue}}`);

    assert.equal(this.element.textContent.trim(), 'Badgeyay');
  });
});
