const companyName = decodeURIComponent(document.location.search.split('company=')[1]);
let currentPage = 0;  

document.getElementById('content-container').addEventListener('scroll', throttle(function(){
    addDataOnScroll();
}, 100));

document.getElementById('close-button').addEventListener('click', (iframe) => {
  // TODO implement this
});

function throttle(func, timeFrame) {
  var lastTime = 0;
  return function (...args) {
      var now = new Date();
      if (now - lastTime >= timeFrame) {
          func(...args);
          lastTime = now;
      }
  };
}

async function addDataOnScroll() {
  const {
    scrollTop,
    scrollHeight,
    clientHeight
  } = document.getElementById('content-container');

  if (scrollTop + clientHeight >= scrollHeight - 15) {
    currentPage++;
    const datas = await getCompanyData(companyName, currentPage);
    renderCardData(datas); 
  }
}

function renderCardData(datas) {
  const cardString = (data) => 
  (`
    <div class="content__text">
      <a href="" class="content__title">
        ${data.title}
      </a>
      <p class="content__body">
        ${data.description}
      </p>
      <p class="content__date">${ new Date(data.date).toString()}</p>
    </div>
  `);

  // TODO: add case when it is empty
  datas.map(data => {
    const contentCard = document.createElement('div');
    contentCard.className = `content card border-${data.sentiment ? 'success' : 'danger' }`;
    contentCard.innerHTML = cardString(data);
    document.getElementById('content-container').appendChild(contentCard);
  });
}

function addLoader() {
  const contentLoaderString = `
    <lines class="shine"></lines>
    <lines class="shine"></lines>
    <lines class="shine"></lines>`;

  const contentLoader = document.createElement('div');
  contentLoader.className = 'content card loader';
  contentLoader.id = "card-shimmer";
  contentLoader.innerHTML = contentLoaderString;
  
  document.getElementById('content-container').appendChild(contentLoader);
}

function removeLoader() {
  document.getElementById('card-shimmer').remove();
}
async function getCompanyData(companyName, page) {
  addLoader();
  try {
    const API_URL = `https://5f05979fee44800016d383a7.mockapi.io/api/v4/companies?page=${page}`;
    const data = await fetch(API_URL).then(
      (res) => (res.json())
    );
    removeLoader();
    return data;
  } catch(e) {
    // TODO: show error
    console.error(e);
    removeLoader();
    return null;
  }
}

async function init() {  
  document.getElementById('brand-name').innerHTML = companyName;

  const datas = await getCompanyData(companyName, currentPage);
  renderCardData(datas);  
}

init();
