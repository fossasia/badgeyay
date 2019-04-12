import Component from '@ember/component';
import Ember from 'ember';
const EmberObject = Ember;

export default Component.extend({
  didInsertElement() {
    if (EmberObject.$(document)[0].getElementsByClassName('six wide column preview').length != 0) {
      EmberObject.$(document)[0].getElementsByClassName('checkswitch')[0].checked = true;
    }
    EmberObject.$(window).bind('resize scroll', function(e) {
      var topcomponent =  EmberObject.$(document)[0].getElementsByClassName('preview-top component');
      var bottomcomponent =  EmberObject.$(document)[0].getElementsByClassName('preview-bottom component');
      var card = EmberObject.$(document)[0].getElementsByClassName('six wide column preview');
      if (card.length != 0) {
        if (e.type === 'scroll' && this.scrollY >= 137 && this.window.innerWidth >= 764 && !(EmberObject.$(window).scrollTop() + EmberObject.$(window).height() > (EmberObject.$(document).height() - 100))) {
          card[0].style.position = 'fixed';
          card[0].style.right = '0';
          card[0].style.top = '0';
          topcomponent[0].style.height = '105px';
          bottomcomponent[0].style.height = '390px';
          EmberObject.$(document)[0].getElementsByClassName('bgImg ui raised segment')[0].style.height = '400px !important';
        } else if (e.type === 'scroll' && this.window.innerWidth >= 764 && (EmberObject.$(window).scrollTop() + EmberObject.$(window).height() > (EmberObject.$(document).height() - 100))) {
          card[0].style.height = '450px';
          topcomponent[0].style.height = '100px';
          EmberObject.$(document)[0].getElementsByClassName('bgImg ui raised segment')[0].style.height = '555px';
          bottomcomponent[0].style.height = '370px';
        } else {
          bottomcomponent[0].style.height = '390px';
          topcomponent[0].style.height = '105px';
          EmberObject.$(document)[0].getElementsByClassName('bgImg ui raised segment')[0].style.height = '555px';
          card[0].style.position = 'inherit';
        }
      }
    });
  },
  willRemoveElement() {
    EmberObject.$(window).unbind('resize scroll');
  }
});
