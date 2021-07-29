const CONTEXT_MENU_ID = "GAIA_CONTEXT_MENU";

function showPopup(info,tab) {
  var companyName = info.selectionText;
  const msg = {
    message: 'show-gaia-popup',
    company: companyName,
  };

  chrome.tabs.sendMessage(tab.id, msg);
}

chrome.contextMenus.create({
  title: "Check '%s' on Gaia", 
  contexts:["selection"], 
  id: CONTEXT_MENU_ID,
});

chrome.contextMenus.onClicked.addListener(
  (info, tab) => {
    showPopup(info,tab);
  } 
);
