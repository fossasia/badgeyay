import { module, test } from 'qunit';
import { setupRenderingTest } from 'ember-qunit';
import { render } from '@ember/test-helpers';
import hbs from 'htmlbars-inline-precompile';

module('Integration | Component | verify-mail', function(hooks) {
  setupRenderingTest(hooks);

  test('it renders', async function(assert) {
    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.set('myAction', function(val) { ... });

    await render(hbs`{{verify-mail}}`);

    assert.equal(this.element.textContent.trim(), 'Your Email is');

    // Template block usage:
    await render(hbs`
      {{#verify-mail}}
        template block text
      {{/verify-mail}}
    `);

    assert.equal(this.element.textContent.trim(), 'Your Email is');
  });
});
