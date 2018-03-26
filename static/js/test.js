$(document).ready(function(){
var Xinner = 0;
var Yinner = 0;
$('.wrapper').mousemove(function(e){
// положение элемента
var pos = $(this).offset();
var elem_left = pos.left;
var elem_top = pos.top;
// положение курсора внутри элемента
Xinner = e.pageX - elem_left - 9;
Yinner = e.pageY - elem_top - 12;


});
console.log("X: " + Xinner + " Y: " + Yinner);
$("div.cell").click(function() {

$(this).append('<div id="+Xinner+" class="outer"><div class="inner"></div></div>');
$('div .outer:last-child').css({ 'left': Xinner, 'top': Yinner});
//$('outer').css({ 'left': Xinner, 'top': Yinner});

console.log("X: " + Xinner + " Y: " + Yinner); // вывод результата в консоль



});
});
