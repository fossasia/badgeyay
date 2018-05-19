import { module, test } from 'qunit';
import { setupRenderingTest } from 'ember-qunit';
import { render } from '@ember/test-helpers';
import hbs from 'htmlbars-inline-precompile';

module('Integration | Component | data-component/text-component', function(hooks) {
  setupRenderingTest(hooks);

  test('it renders', async function(assert) {
    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.set('myAction', function(val) { ... });

    await render(hbs`{{data-component/text-component}}`);

    assert.equal(this.element.textContent.trim(), 'Enter details');

    // Template block usage:
    await render(hbs`
      {{#data-component/text-component}}
        template block text
      {{/data-component/text-component}}
    `);

    assert.equal(this.element.textContent.trim(), 'Enter details');
  });
});
