// Generated by CoffeeScript 1.4.0
(function() {

$(window).on('load', function() {
    var $preloader, $spinner;
    $preloader = $('#page-preloader');
    $spinner = $preloader.find('.spinner');// animation preloader
    $spinner.fadeOut();
    return $preloader.delay(400).slideUp(2000);
  });
}).call(this);

$(document).ready(function() {

  function movel(){
  $(this).toggleClass('done'); 
  $(this).toggleClass('line');//will toggle the class (add it if doesn't have it or remove it if it does)
  //$(this).css({ x: '100px' });
  };

  $('.blinds').trigger('click');

  $('.blinds').on('click', movel);

  

});




