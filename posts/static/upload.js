
const input = document.querySelector("#file-input");

input.addEventListener("change", listener);

function listener() {
  const file = input.files[0];
  axios.request( {
    method: "post",
    url: "/api/upload",
    data: file,
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
