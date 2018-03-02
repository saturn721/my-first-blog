


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
    var texts = this.textContent.split('');
     // console.log(texts);
    var outtext ='<img src="img/1.jpg" id="m1" class="img-responsive img-thumbnail" alt="Responsive image"><p><span>' + texts.join('</span><span>') + '</span></p>';

    //this.textContent = outtext;
     console.log(outtext);
      $(this).css('color', 'black');
    (tr == true) ? $(document.getElementsByClassName('line')).css('opacity', '0') :
    $(document.getElementsByClassName('line')).css('opacity', '1');
    // test ? operator  это замена оператора if на оператор ? важно, после первой команды не должно быть ;


  };


$(document).ready(function() {
  $('.line').css({ perspective: 100, rotateY: 2 });

  $('.blinds').trigger('click');

  $('.blinds').on('click', movel);





  //$('.done').hover(
  //   function(){$(this).siblings().css('opacity', '.3')},
 //    function(){$(this).siblings().css('opacity', '1');}
 // );


});
