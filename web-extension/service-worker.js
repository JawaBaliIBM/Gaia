const CONTEXT_MENU_ID = "GAIA_CONTEXT_MENU";

async function getCompanyData(companyName) {
  try {
    const API_URL = 'https://5f05979fee44800016d383a7.mockapi.io/api/v4/companies';
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
  const companyName = info.selectiontext;
  const data = getCompanyData(companyName);
  
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
  title: "Search: %s", 
  contexts:["selection"], 
  id: CONTEXT_MENU_ID,
});

chrome.contextMenus.onClicked.addListener(
  (info, tab) => showPopup(info,tab)
);
