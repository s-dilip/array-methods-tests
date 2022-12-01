const submitButton = document.querySelector("#submit-button");
const nameField = document.querySelector("#name-field");
const emailField = document.querySelector("#email-field");
const outputBox = document.querySelector("#output-records");

submitButton.addEventListener("click", onSubmitClicked);

function onSubmitClicked(clickEvent) {
  clickEvent.preventDefault();
  const name = nameField.value;
  const email = emailField.value;
  const err_div = document.querySelector(".error-msg");
  if (err_div.childNodes.length > 0) {
    console.log(err_div.childNodes);
    err_div.removeChild(err_div.childNodes[0]);
  }

  if (!email.includes("@")) {
    const err_message = document.createElement("p");
    err_message.innerHTML = "Does Not contain @";
    err_message.style.color = "red";
    err_div.append(err_message);
  } else {
    addElement(name, outputBox, "h2");
    addElement(email, outputBox, "h4");
  }
}

function addElement(text, targetBox, elementTag) {
  const element = document.createElement(elementTag);
  element.classList.add("record");
  element.innerHTML = text;
  targetBox.append(element);
}
