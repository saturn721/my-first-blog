$(document).ready(function(){
var Xinner = 0;
var Yinner = 0;
var colord = '';
$('.wrapper').mousemove(function(e){
// положение элемента
    var pos = $(this).offset();
    var elem_left = pos.left;
    var elem_top = pos.top;
    // положение курсора внутри элемента
    Xinner = e.pageX - elem_left - 9;
    Yinner = e.pageY - elem_top - 12;


});

$('img').mousemove(function(e) {

    if(!this.canvas) {
        this.canvas = $('<canvas />')[0];
        this.canvas.width = this.width;
        this.canvas.height = this.height;
        this.canvas.getContext('2d').drawImage(this, 0, 0, this.width, this.height);
    }

    var pixelData = this.canvas.getContext('2d').getImageData(event.offsetX, event.offsetY, 1, 1).data;

    colord = 'rgb(' + pixelData[0] + ',' + pixelData[1] + ',' + pixelData[2] + ') 0px 0px 1px 4px';
    console.log(colord);

});

$("div.cell").click(function() {

$(this).append('<div id="+Xinner+" class="outer"><div class="inner"></div></div>');
$('div .outer:last-child').css({ 'box-shadow': colord, 'left': Xinner, 'top': Yinner });
//$('outer').css({ 'left': Xinner, 'top': Yinner});

//console.log("X: " + Xinner + " Y: " + Yinner); // вывод результата в консоль



});
});
