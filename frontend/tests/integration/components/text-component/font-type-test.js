import { module, test } from 'qunit';
import { setupRenderingTest } from 'ember-qunit';
import { render } from '@ember/test-helpers';
import hbs from 'htmlbars-inline-precompile';

module('Integration | Component | text-component/font-type', function(hooks) {
  setupRenderingTest(hooks);

  test('it renders', async function(assert) {
    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.set('myAction', function(val) { ... });

    await render(hbs`{{text-component/font-type}}`);

    assert.equal(this.element.textContent.trim(), 'Select font\n        Select font from list');

    // Template block usage:
    await render(hbs`
      {{#text-component/font-type}}
        template block text
      {{/text-component/font-type}}
    `);

    assert.equal(this.element.textContent.trim(), 'Select font\n        Select font from list');
  });
});
