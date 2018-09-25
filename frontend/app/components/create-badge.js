import Component from '@ember/component';
import Ember from 'ember';
const EmberObject  = Ember;

export default Component.extend({
  didInsertElement() {
    EmberObject.$(window).on('resize scroll', function(e) {
      if (e.type === 'scroll' && this.scrollY >= 137 && this.window.innerWidth >= 764 && this.scrollY < 1278) {
        EmberObject.$(document)[0].getElementsByClassName('six wide column preview')[0].style.position = 'fixed';
        EmberObject.$(document)[0].getElementsByClassName('six wide column preview')[0].style.right = '0';
        EmberObject.$(document)[0].getElementsByClassName('six wide column preview')[0].style.top = '0';
      } else if (e.type === 'scroll' && this.window.innerWidth >= 764 && this.scrollY >= 1278) {
        EmberObject.$(document)[0].getElementsByClassName('six wide column preview')[0].style.position = 'fixed';
        EmberObject.$(document)[0].getElementsByClassName('bgImg ui raised segment')[0].style.height = '570px';
      } else {
        EmberObject.$(document)[0].getElementsByClassName('bgImg ui raised segment')[0].style.height = '600px';
        EmberObject.$(document)[0].getElementsByClassName('six wide column preview')[0].style.position = 'inherit';

      }
    });
  }
});