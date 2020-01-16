
document
  .querySelector("#upload-form")
  .addEventListener("submit", listener);

function listener(event) {
  event.preventDefault();
  const formData = new FormData(event.target);

  axios.request( {
    method: "post",
    url: "/api/upload",
    data: formData,
    onUploadProgress: (p) => {
      console.log(p);
    }
  }).then (data => {
    console.log(data);
    //this.setState({
    //fileprogress: 1.0,
    //})
  })
}
