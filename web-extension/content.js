let iframe;
const URL = chrome.runtime.getURL("popup.html");

chrome.runtime.onMessage.addListener(function(msg, sender){
  if(msg.message == "show-gaia-popup"){
    changeIframeName(msg.company);
  }
})

function initIframe() {
  iframe = document.createElement('iframe'); 
  iframe.style.background = "white";
  iframe.style.height = "600px";
  iframe.style.width = "0px";
  iframe.style.position = "fixed";
  iframe.style.top = "5px";
  iframe.style.right = "5px";
  iframe.style.zIndex = "9000000000000000000";
  iframe.src = `${URL}`;

  document.body.appendChild(iframe);
}

function changeIframeName(companyName){
  if(iframe.style.width == "0px"){
    iframe.style.width="400px";
  }
  iframe.src = `${URL}?company=${companyName}`;
}

initIframe();
