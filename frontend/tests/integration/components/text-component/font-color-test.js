import { module, test } from 'qunit';
import { setupRenderingTest } from 'ember-qunit';
import { render } from '@ember/test-helpers';
import hbs from 'htmlbars-inline-precompile';

module('Integration | Component | text-component/font-color', function(hooks) {
  setupRenderingTest(hooks);

  test('it renders', async function(assert) {
    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.set('myAction', function(val) { ... });

    await render(hbs`{{text-component/font-color}}`);

    assert.equal(this.element.textContent.trim(), 'Select font color');

    // Template block usage:
    await render(hbs`
      {{#text-component/font-color}}
        template block text
      {{/text-component/font-color}}
    `);

    assert.equal(this.element.textContent.trim(), 'Select font color');
  });
});
