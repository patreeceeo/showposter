
const deleteForm = document.querySelector("#delete_form");

deleteForm.addEventListener("submit", handleSubmit);

function handleSubmit(event) {
  event.preventDefault();

  const confirmed = confirm("You're sure you wanna delete this?");

  if(confirmed) {
    const formAction = deleteForm.getAttribute("action");
    const formMethod = deleteForm.getAttribute("method");
    const formData = new FormData(deleteForm);

    axios.request({
      method: formMethod,
      url: formAction,
      data: formData
    }).then(() => {
      window.location.href = SUCCESS_URL;
    });
  }
}
