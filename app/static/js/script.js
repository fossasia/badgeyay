$(function() {

  $('.glyphicon-th').click(function(){
    $('.custom-menu-content').toggleClass('hidden');
  });

  var apiUrl = "https://api.github.com/repos/fossasia/badgeyay/git/refs/heads/development";
  $.ajax({url: apiUrl, success: function(result){
    var version = result['object']['sha'];
    var versionLink = 'https://github.com/fossasia/badgeyay/tree/'+version;
    var deployLink = $('.version').attr('href', versionLink).html(version);
  }});

  $(".menu-options").click(function(){
    var i = $(this).data("item");
    $(".placeholder").text(i);
    $("input[name='img-default']").val(i);
  });

});