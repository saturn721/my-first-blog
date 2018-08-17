

function notify(request, sender, sendResponse){
    var i = ['face'];
    switch(request.message){
        case 'face':
        i = ['face', 'eye', 'mouth'];
          break;
        case 'eye':
        i.push('eye');
         break;
        case 'mouth':
        i.push('mouth');
         break;
         default:
         i = ['face', 'eye', 'mouth'];
       }
    getVideo(i);
    browser.runtime.onMessage.removeListener(notify);
    console.log(i);
    }

 function getVideo(myselect) {

   var video = document.getElementById('video');
   var canvas = document.getElementById('canvas');
   canvas.style.position = "absolute"; // это главное, без него не работает..
   var context = canvas.getContext('2d');
   // @dev tracker objects
   var tracker = new tracking.ObjectTracker(myselect);
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
 video.play();
 };
browser.runtime.onMessage.addListener(notify);
//setTimeout(getVideo(myselect), 1000);
//window.onload = getVideo(myselect);
