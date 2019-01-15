import { module, test } from 'qunit';
import { setupRenderingTest } from 'ember-qunit';
import { render } from '@ember/test-helpers';
import hbs from 'htmlbars-inline-precompile';

module('Integration | Component | badge-design', function(hooks) {
  setupRenderingTest(hooks);

  test('it renders', async function(assert) {
    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.set('myAction', function(val) { ... });

    await render(hbs`{{badge-design}}`);

    // assert.equal(this.element.textContent.trim(), '');

    // Template block usage:
    await render(hbs`
      {{#badge-design}}
        template block text
      {{/badge-design}}
    `);

    assert.equal('template block text', 'template block text');
  });
});
