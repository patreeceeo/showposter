const STATE_INIT = 0
const STATE_PROCESSING = 1
const STATE_COMPLETE = 2

let uploadState = STATE_INIT

const uploadForm = document
  .querySelector("#upload-form")
const imageInput = document
  .querySelector("#image-input")
const previewImage = document
  .querySelector("#preview-image")
const imagePlaceholder = document
  .querySelector("#image-placeholder")
const uploadProgressDiv = document
  .querySelector("#upload-progress")
const scanner = document
  .querySelector("#scanner")

function loadImageSrcFromInput(input) {
  loadImageSrc(input.files[0], setPreviewImageSrc)
  imagePlaceholder.className = "hidden"
}

function loadImageSrc(file, callback) {
  const reader = new FileReader()

  const handleLoad = (event) => {
    callback(event.target.result)
    reader.removeEventListener("load", handleLoad)
  }

  reader.addEventListener("load", handleLoad)
  reader.readAsDataURL(file)
}

function setPreviewImageSrc(src) {
  previewImage.setAttribute("src", src)
  previewImage.className = "Preview Preview__in"
}

function handleFileSelected(event) {
  uploadImageFromInput(event.target)
}

function uploadImageFromInput(input) {
  const formData = new FormData(uploadForm)

  loadImageSrcFromInput(input)

  scanner.style.setProperty("--scanner-is-on", '1')

  if(uploadState === STATE_PROCESSING) {
    return
  }

  uploadState = STATE_PROCESSING

  axios.request({
    method: "post",
    url: "/api/uploaded_image",
    data: formData,
    onUploadProgress: (event) => {
      const progress = `${100 * (event.loaded / event.total)}%`
      scanner.style.setProperty("--scanner-progress", progress)
      uploadProgressDiv.innerHTML = `${progress} uploaded`
    }
  }).then ((response) => {
    scanner.style.setProperty("--scanner-progress", '100%')
    scanner.style.setProperty("--scanner-is-on", '0')
    uploadState = STATE_COMPLETE
    document.querySelector("#uploaded-image-id-input").setAttribute("value", response.data.id)
    return axios.get("/api/unused_uploaded_image")
  }).then((response) => {
    axios.request({
      method: "delete",
      url: "/api/bulk_uploaded_image",
      data: response.data.map(({id}) => id)
    });
  });
}

if(imageInput.files[0]) {
  uploadImageFromInput(imageInput);
}

uploadForm.addEventListener("submit", (event) => event.preventDefault())

imageInput.addEventListener("change", handleFileSelected)
