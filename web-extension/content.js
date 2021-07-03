let iframe;

const url = chrome.runtime.getURL("popup.html");

chrome.runtime.onMessage.addListener(function(msg, sender){
  if(msg.message == "show-gaia-popup"){
    changeIframeName(msg.company);
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
  iframe.id = 'gaia-iframe';
  iframe.src = `${url}`;

  document.body.appendChild(iframe);
}

function changeIframeName(companyName){
  if(iframe.style.width == "0px"){
    iframe.style.width="400px";
  }
  iframe.src = `${url}?company=${companyName}`;
}

initIframe();
