axios.request({
  method: 'GET',
  url: '/api/upload',
}).then((response)  => {
  document.querySelector("#list").innerHTML=renderList(response.data);
});

function renderList(data) {
  return `<ul>${
    data.map(({image}) => `<li>${image}</li>`).join('')
  }</ul>`;
}

document.querySelector("#bulk-delete-button").addEventListener("click", handleClickBulkDelete);
