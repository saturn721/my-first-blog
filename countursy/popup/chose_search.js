
var pause = document.getElementById('pause');
// @dev logic work. Prepare, start, pause track

document.addEventListener("click", (e) => {
  if (e.target.classList.contains("start")) {
      browser.tabs.executeScript(null, {
        file: "/content_scripts/facetab.js"
    });
      var gettingActiveTab = browser.tabs.query({active: true, currentWindow: true});
     var myselect = document.getElementById('myselect').value;
      gettingActiveTab.then((tabs) => {
      browser.tabs.sendMessage(tabs[0].id, {message: myselect});
    });

  }

  else if (e.target.classList.contains("prepare")) {
      browser.tabs.executeScript(null, {
        file: "/content_scripts/prepare.js"
    });
  }
  else if (e.target.classList.contains("pause")) {
      browser.tabs.executeScript(null, {
        file: "/content_scripts/stage.js"
    });
    if (pause.innerHTML == "Pause"){
    pause.innerHTML = "Play";
    }
    else {
        pause.innerHTML = "Pause";
    }
  }
  else if (e.target.classList.contains("clear")) {
    browser.tabs.reload();
    window.close();
  }
});
