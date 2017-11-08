$(document).ready(
  
      function(){
        $("#csvupload").click(function(){
          $("#csvupload-input").css("display","block");
          $("#text-input").css("display","none");
        });
        $("#manualdata").click(function(){
          $("#csvupload-input").css("display","none");
          $("#text-input").css("display","block");
        });
        $("#pngupload").click(function(){
          $("#upimage-input").css("display","block");
          $("#deimage-input").css("display","none");
          $("#background-input").css("display","none");
        });
        $("#defimage").click(function(){
          $("#upimage-input").css("display","none");
          $("#deimage-input").css("display","block");
          $("#background-input").css("display","none");
        });
        $("#defback").click(function(){
          $("#upimage-input").css("display","none");
          $("#deimage-input").css("display","none");
          $("#background-input").css("display","block");
        });
        $("#text").click(function(){
          $("#cutext-input").css("display","block");
          $("#config-input").css("display","none");
        });
        $("#json").click(function(){
          $("#cutext-input").css("display","none");
          $("#config-input").css("display","block");
        });

        
});
      
