const CONTEXT_MENU_ID = "GAIA_CONTEXT_MENU";
let page = 1;


async function getCompanyData(companyName, page) {
  try {
    const API_URL = `https://5f05979fee44800016d383a7.mockapi.io/api/v4/companies?page=${page}`;
    const data = await fetch(API_URL, {
      body: companyName,
    });
    return data;
  } catch(e) {
    console.error(e);
    return null;
  }
}

function showPopup(info,tab) {
  const companyName = sessionStorage.getItem("gaiaCompanyName");
  const data = getCompanyData(companyName, page);
  if (data) {
    chrome.tabs.sendMessage(
      tab.id, 
      { 
        message: "gaiaPopup", 
        data 
      }
    );
  }
}

chrome.contextMenus.create({
  title: "Check '%s' on Gaia", 
  contexts:["selection"], 
  id: CONTEXT_MENU_ID,
});

chrome.contextMenus.onClicked.addListener(
  (info, tab) => {
    sessionStorage.setItem("gaiaCompanyName", info.selectiontext);
    showPopup(info,tab)
  } 
);

chrome.runtime.onMessage.addListener(function(msg, sender){
  if(msg.message == "gaiaHalfScroll"){
      page++;
      showPopup(msg, sender)
  }
})