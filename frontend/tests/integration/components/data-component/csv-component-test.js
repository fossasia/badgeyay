import { module, test } from 'qunit';
import { setupRenderingTest } from 'ember-qunit';
import { render } from '@ember/test-helpers';
import hbs from 'htmlbars-inline-precompile';

module('Integration | Component | data-component/csv-component', function(hooks) {
  setupRenderingTest(hooks);

  test('it renders', async function(assert) {
    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.set('myAction', function(val) { ... });

    await render(hbs`{{data-component/csv-component}}`);

    assert.equal(this.element.textContent.trim(), 'Upload CSV');

    // Template block usage:
    await render(hbs`
      {{#data-component/csv-component}}
        template block text
      {{/data-component/csv-component}}
    `);

    assert.equal(this.element.textContent.trim(), 'Upload CSV');
  });
});
