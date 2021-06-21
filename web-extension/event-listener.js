window.addEventListener('scroll', () => {
    const {
        scrollTop,
        scrollHeight,
        clientHeight
    } = document.documentElement;

    if (scrollTop + clientHeight >= scrollHeight - 5 &&
       total > 0) {
        chrome.tabs.sendMessage(
            tab.id, 
            { 
              message: "gaiaHalfScroll", 
              data 
            }
          );
    }
}

