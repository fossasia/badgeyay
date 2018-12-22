import { module, test } from 'qunit';
import { setupRenderingTest } from 'ember-qunit';
import { render } from '@ember/test-helpers';
import hbs from 'htmlbars-inline-precompile';

module('Integration | Component | badge-component/paper-size', function(hooks) {
  setupRenderingTest(hooks);

  test('it renders', async function(assert) {
    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.set('myAction', function(val) { ... });

    await render(hbs`{{badge-component/paper-size}}`);

    assert.equal('', '');

    // Template block usage:
    await render(hbs`
      {{#badge-component/paper-size}}
        template block text
      {{/badge-component/paper-size}}
    `);

    assert.equal('', '');
  });
});
