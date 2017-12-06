import Component from '@ember/component';

export default Component.extend({

  didInsertElement() {
    this._super(...arguments);
    var elemnt = this.$('#colorpick');
    elemnt.colpick({
      layout:'hex',
      submit:0,
      colorScheme:'light',
      onChange:function(hsb,hex,rgb,el,bySetColor) {
        elemnt.css('border-color','#'+hex);
        // Fill the text box just if the color was set using the picker, and not the colpickSetColor function.
        if(!bySetColor) elemnt.val("#" + hex);
      }
    }).keyup(function(){
      elemnt.colpickSetColor(this.$('#colorpick').value);
    });
  },

  /* listening for events  */
  actions : {

    /* data source radio selection changed */
    datasourceChanged(source) {
      if (source == 'csv') {
        /*  Show the csv task*/
        this.$(".csv-upload").css({
          'display' : 'block'
        });
        this.$(".manual-data").css({
          'display' : 'none'
        });
      }
      else if (source == 'manual') {
        /*  Show the manual task*/
        this.$(".manual-data").css({
          'display' : 'block'
        });
        this.$(".csv-upload").css({
          'display' : 'none'
        });
      }
    },

    /* background source radio chaned events*/
    backgroundsourceChanged(source) {
      if (source == 'png') {
        /*  Show current task*/
        this.$(".png-background").css({
          'display' : 'block'
        });
        this.$(".default-image-background").css({
          'display' : 'none'
        });
        this.$(".custom-background").css({
          'display': 'none'
        });
      }
      else if (source == 'defaults') {
        this.$(".png-background").css({
          'display' : 'none'
        });
        this.$(".default-image-background").css({
          'display' : 'block'
        });
        this.$(".custom-background").css({
          'display': 'none'
        });
      }
      else if (source == 'color') {
        this.$(".png-background").css({
          'display' : 'none'
        });
        this.$(".default-image-background").css({
          'display' : 'none'
        });
        this.$(".custom-background").css({
          'display': 'block'
        });
      }
    },

    /* text source radio changed  event */
    textsourceChanged(source) {
      if (source == 'text') {
        /*  Show the text task*/
        this.$(".custom-text").css({
          'display' : 'block'
        });
        this.$(".config-json").css({
          'display' : 'none'
        });
      }
      else if (source == 'json') {
        /*  Show the json task*/
        this.$(".config-json").css({
          'display' : 'block'
        });
        this.$(".custom-text").css({
          'display' : 'none'
        });
      }
    }


  }

});
