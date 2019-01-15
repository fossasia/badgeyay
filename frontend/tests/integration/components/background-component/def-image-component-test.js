import { module, test } from 'qunit';
import { setupRenderingTest } from 'ember-qunit';
import { render } from '@ember/test-helpers';
import hbs from 'htmlbars-inline-precompile';

module('Integration | Component | background-component/def-image-component', function(hooks) {
  setupRenderingTest(hooks);

  test('it renders', async function(assert) {
    // Set any properties with this.set('myProperty', 'value');
    // Handle any actions with this.set('myAction', function(val) { ... });

    await render(hbs`{{background-component/def-image-component}}`);

    assert.equal('', '');

    // Template block usage:
    await render(hbs`
      {{#background-component/def-image-component}}
        template block text
      {{/background-component/def-image-component}}
    `);

    assert.equal('', '');
  });
});

