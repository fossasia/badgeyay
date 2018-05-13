/*jshint esversion: 6 */
$(document).ready(function () {

    $(document).mouseup(function (e) {
        var container = $('.custom-menu-content');
        var button = $('.glyphicon-th');
        // if the target of the click is not the button,
        // the container or a descendant of the container
        if (!button.is(e.target) && !container.is(e.target) && container.has(e.target).length === 0) {
            container.addClass('hidden');
        }
    });

    $('.glyphicon-th').click(function () {
        $('.custom-menu-content').toggleClass('hidden');
    });

    $('.menu-options').click(function () {
        var i = $(this).data('item');
        $('.placeholder').text(i);
        $("input[name='img-default']").val(i).trigger('change');
    });

    $('.font-options').click(function () {
        var i = $(this).data('item');
        $('.placeholder2').text(i);
        $("input[name='custfont']").val(i);
    });


    $('#picker').minicolors({
        control: 'hue',
        format: 'hex',
        defaultValue: '',
        letterCase: 'lowercase',
        position: 'bottom left',
        theme: 'bootstrap'
    });

    $('#text-picker').minicolors({
        control: 'hue',
        format: 'hex',
        defaultValue: '#ffffff',
        letterCase: 'lowercase',
        position: 'bottom left',
        theme: 'bootstrap'
    });

    var apiUrl = 'https://api.github.com/repos/fossasia/badgeyay/git/refs/heads/development';
    $.ajax({
        url: apiUrl,
        async: true,
        success(result) {
            if (typeof result.object !== 'undefined' && typeof result.object.sha !== 'undefined') {
                var version = result.object.sha;
                var versionLink = 'https://github.com/fossasia/badgeyay/tree/' + version;
                var deployLink = $('.version').attr('href', versionLink).html(version);
            } else {
                $('.version').html('Failed to access version');
            }
        },
        error(error) {
            $('.version').html('Failed to access version');
        }
    });
    function readURL(input) {

        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#preview').css('background','url(' +  e.target.result + ')');
                $('#preview').css('background-size','cover');
                $('#preview-btn').prop('disabled',false);
            };

            reader.readAsDataURL(input.files[0]);
        }
    }

    $('#imageFile').change(function(){
        readURL(this);
    });

    $('#picker').change(function(){
        $('#preview-btn').prop('disabled',false);
        $('#preview').css('background','');
    });

    $('input[name=img-default]').change(function(){
        $('#preview-btn').prop('disabled',false);
        changePreviewBackground();
        $('#picker').val('');
    });

    var previewOff = true;

    var changeTemplateBackground = function() {
        imageValue = $('#picker').val();
        $('#preview').css('background-color',imageValue.toString());
    };

    var changePreviewFont = function() {
        fontValue = $('.placeholder2')[0].innerText;
        $('.preview-image-li').css('font-family',fontValue.toString());
    };

    var changePreviewFontColor = function() {
        var fontColor = $('#text-picker').val();
        $('.preview-image-li').css('color',fontColor.toString());
    };

    $('#preview-btn').on('click',function(e){
        $('#preview').toggleClass('hidden');
        previewOff = !previewOff;
        console.log(previewOff);
        if(!previewOff){
            $('#preview-btn')[0].innerHTML = 'Close Preview';
            var imageValue,fontValue;
            if($('#picker').val() !== ''){
                changeTemplateBackground();
            }
            else if($('input[name=img-default]').val() !== ''){
                changePreviewBackground();
            }
            if($('.placeholder2')[0].innerText !== 'Select a font'){
                changePreviewFont();
            }
            if($('#text-picker').val() !== ''){
                changePreviewFontColor();
            }
            if($('#font-size').val() !== '') {
                var fontSize = $('#font-szie').val();
                $('.preview-image-li').css('font-size', fontSize.toString());
            }
        }
        else{
            $('#preview-btn')[0].innerHTML = 'Preview';
        }
    });

    $('#text-input').on('keyup',realtimeChange);

    function changePreviewBackground(){
        var imageValue = 'https://raw.githubusercontent.com/fossasia/badgeyay/development/frontend/public/images/badge_backgrounds/' + $('input[name=img-default]').val() + '?raw=true';
        $('#preview').css('background','url(' + imageValue + ')');
        $('#preview').css('background-size','cover');
    }

    function realtimeChange(){

        var textValues = $('#textArea').val();
        textValues = textValues.split('\n')[0].split(',');


        $('#preview-li-1').text(textValues[0]);
        $('#preview-li-2').text(textValues[1]);
        $('#preview-li-3').text(textValues[2]);
        $('#preview-li-4').text(textValues[3]);
        $('#preview-li-5').text(textValues[4]);


    }

    $('#form1').submit(function(e){
        $('#preview-btn').click();
    });
});
