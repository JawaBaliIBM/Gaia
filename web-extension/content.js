let iframe;

chrome.runtime.onMessage.addListener(function(msg, sender){
  if(msg.message == "gaiaPopup"){
      toggle();
  }
})

// TODO: fix size of popup and style
function initIframe() {
  iframe = document.createElement('iframe'); 
  iframe.style.background = "white";
  iframe.style.height = "100%";
  iframe.style.width = "0px";
  iframe.style.position = "fixed";
  iframe.style.top = "0px";
  iframe.style.right = "0px";
  iframe.style.zIndex = "9000000000000000000";
  iframe.frameBorder = "none"; 
  iframe.src = chrome.runtime.getURL("popup.html")

  document.body.appendChild(iframe);
}

function toggle(){
  if(iframe.style.width == "0px"){
    iframe.style.width="400px";
  }
  else{
    iframe.style.width="0px";
  }
}

initIframe();