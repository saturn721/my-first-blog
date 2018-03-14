


  $('.antispam').on('click', enter );


  function enter(){
      var $preloader, $spinner;
      $preloader = $('#page-preloader');
      $spinner = $('.antispam');// animation preloader
      $spinner.fadeOut();
      return $preloader.delay(400).slideUp(2000);
  };



function movel(){
    //console.log(document.classList.contains("example"));
    this.classList.toggle('done');
    this.classList.toggle('line');
    var tr = this.classList.contains('done');
    $(this).css('color', 'black');
    (tr == true) ? $(document.getElementsByClassName('line')).css('opacity', '0') :
    $(document.getElementsByClassName('line')).css('opacity', '1');
    // test ? operator  это замена оператора if на оператор ? важно, после первой команды не должно быть ;


  };


$(window).on('load', function() {
  $('.line').css({ perspective: 100, rotateY: 2 });

  $('.blinds').trigger('click');

  $('.blinds').on('click', movel);






//$("iframe").contents().find("body").css('background', 'black'); так не выйдет, браузер блокирует такие штуки по соображениям безопасности
  //$('.done').hover(
  //   function(){$(this).siblings().css('opacity', '.3')},
 //    function(){$(this).siblings().css('opacity', '1');}
 // );


});
