const STATE_INIT = 0;
const STATE_PROCESSING = 1;
const STATE_COMPLETE = 2;

let uploadState = STATE_INIT;

const imageInput = document
  .querySelector("#image-input");

loadImageSrcFromInput(imageInput);

imageInput
  .addEventListener("change", handleChangeFile);

function handleChangeFile(event) {
  loadImageSrcFromInput(event.target)
  submitButton.className = decideClassListForSubmitButton();
  submitButton.setAttribute("value", decideValueForSubmitButton());
}

function loadImageSrcFromInput(input) {
  if(input.files[0]) {
    loadImageSrc(input.files[0], setPreviewImageSrc)
  }
}

function loadImageSrc(file, callback) {
  const reader = new FileReader();

  const handleLoad = (event) => {
    callback(event.target.result);
    reader.removeEventListener("load", handleLoad);
  }

  reader.addEventListener("load", handleLoad)
  reader.readAsDataURL(file)
}

const previewImage = document.querySelector("#preview-image");

function setPreviewImageSrc(src) {
  previewImage.setAttribute("src", src);
  previewImage.className = "Preview Preview__in";
}

const submitButton = document.querySelector("#submit-button");

submitButton.className = decideClassListForSubmitButton();
submitButton.setAttribute("value", decideValueForSubmitButton());

function decideClassListForSubmitButton() {
  return imageInput.files[0] ? "Button mb" : "hidden";
}

function decideValueForSubmitButton() {
  return [imageInput.files[0] ? `Upload ${imageInput.files[0].name}` : "", "Uploading...", "Complete!"][uploadState];
}

document
  .querySelector("#upload-form")
  .addEventListener("submit", handleSubmit);

const scanner = document.querySelector("#scanner")

function handleSubmit(event) {
  event.preventDefault();
  const formData = new FormData(event.target);

  scanner.style.setProperty("--scanner-is-on", '1');

  if(uploadState === STATE_PROCESSING) {
    return;
  }

  uploadState = STATE_PROCESSING;
  submitButton.setAttribute("disabled", true);
  submitButton.setAttribute("value", decideValueForSubmitButton());

  axios.request({
    method: "post",
    url: "/api/upload",
    data: formData,
    onUploadProgress: (event) => {
      const progress = `${100 * (event.loaded / event.total)}%`;
      scanner.style.setProperty("--scanner-progress", progress);
    }
  }).then (() => {
    scanner.style.setProperty("--scanner-progress", '100%');
    scanner.style.setProperty("--scanner-is-on", '0');
    uploadState = STATE_COMPLETE;
    submitButton.setAttribute("value", decideValueForSubmitButton());
  })
}

