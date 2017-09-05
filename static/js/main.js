
$(document).ready(function(){
    $(".flip2").click(function(){ 
    	$(".art2").siblings().css("display", "none");
        $(".art2").slideDown("slow");
        
        
    });
    $(".flip1").click(function(){
    	$(".art1").siblings().css("display", "none");
        $(".art1").slideDown("slow");
        
        
    });

    $(".flip3").click(function(){
    	$(".art3").siblings().css("display", "none");
        $(".art3").slideDown("slow");
        
    });

    $(".flip4").click(function(){
        $(".art4").siblings().css("display", "none");
        $(".art4").slideDown("slow");
        
    });

    $(".flip5").click(function(){
        $(".art5").siblings().css("display", "none");
        $(".art5").slideDown("slow");
        
    });

    $(".flip6").click(function(){
        $(".art6").siblings().css("display", "none");
        $(".art6").slideDown("slow");
        
    });
    $(".flip7").click(function(){
        $(".art7").siblings().css("display", "none");
        $(".art7").slideDown("slow");
        
    });

});


(function() {

  $(window).on('load', function() {
    var $preloader, $spinner;
    $preloader = $('#page-preloader');
    $spinner = $preloader.find('.spinner');// animation preloader
    $spinner.fadeOut();
    return $preloader.delay(400).slideUp(2000);
  });

}).call(this);