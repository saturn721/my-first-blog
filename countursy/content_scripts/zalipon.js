

 function getVideo() {



   var video = document.getElementById('video');
   var canvas = document.getElementById('canvas');
   canvas.style.position = "absolute"; // это главное, без него не работает..
   var context = canvas.getContext('2d');
   var tracker = new tracking.ObjectTracker('face');
    tracker.setInitialScale(4);
    tracker.setStepSize(2);
    tracker.setEdgesDensity(0.1);
    tracking.track('#video', tracker, { camera: false });
    tracker.on('track', function(event) {
      context.clearRect(0, 0, canvas.width, canvas.height);
      event.data.forEach(function(rect) {
        context.strokeStyle = '#a64ceb';
        context.strokeRect(rect.x, rect.y, rect.width, rect.height);
        context.font = '11px Helvetica';
        context.fillStyle = "#fff";
        context.fillText('x: ' + rect.x + 'пик', rect.x + rect.width + 5, rect.y + 11);

        context.fillText('y: ' + rect.y + 'пик', rect.x + rect.width + 5, rect.y + 22);
      });
    });

    guido(tracker);
 video.play();


 };
 function guido(tracker){
     var gui = new dat.GUI();
     gui.add(tracker, 'edgesDensity', 0.1, 0.5).step(0.01);
     gui.add(tracker, 'initialScale', 1.0, 10.0).step(0.1);
     gui.add(tracker, 'stepSize', 1, 5).step(0.1);
 };
window.onload = getVideo();
