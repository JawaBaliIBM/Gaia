const companyName = document.location.search.split('company=')[1];
let currentPage = 0;  

async function getCompanyData(companyName, page) {
  try {
    console.log('get company data', page);
    const API_URL = `https://5f05979fee44800016d383a7.mockapi.io/api/v4/companies?page=${page}`;
    const data = await fetch(API_URL).then((res) => (res.json()));
    return data;
  } catch(e) {
    console.error(e);
    return null;
  }
}

function renderCardData(datas) {
  const cardString = (data) => 
  (`<div class="content__indicator--${data.sentiment ? 'green' : 'red' }"></div>
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

  datas.map(data => {
    const contentCard = document.createElement('div');
    contentCard.className = 'content card';
    contentCard.innerHTML = cardString(data);
    document.getElementById('content-container').appendChild(contentCard);
  });
}

window.addEventListener('scroll', async () => {
  const {
    scrollTop,
    scrollHeight,
    clientHeight
  } = document.documentElement;

  if (scrollTop + clientHeight >= scrollHeight - 15) {

    currentPage++;
    const datas = await getCompanyData(companyName, currentPage);
    renderCardData(datas); 
  }
});

async function init() {  
  document.getElementById('brand-name').innerHTML = companyName;

  const datas = await getCompanyData(companyName, currentPage);
  renderCardData(datas);  
}

init();
