
var pause = document.getElementById('pause');


document.addEventListener("click", (e) => {
  if (e.target.classList.contains("start")) {
      browser.tabs.executeScript(null, {
        file: "/content_scripts/facetab.js"
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
