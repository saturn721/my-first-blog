// @dev function prepare web page to track object. Find video, insert canvas...
function prepare(){
    var v = document.getElementsByTagName('video');
    var vi = v[0];
    vi.id = 'video';
    var video = document.getElementById('video');
    var elt = video.parentNode;
    console.log(elt);
    var canv = document.createElement("canvas");
    canv.id = 'canvas';
    canv.width = '1000';
    canv.height = '1000';
    var canvas = document.getElementById('canvas');
    //
    elt.appendChild(canv);
    canvas.style.position = "absolute";
  console.log(canvas);
};

window.onload = prepare();
