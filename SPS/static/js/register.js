const usernameField = document.querySelector('#usernameField');
const emailField = document.querySelector('#emailField');
const passwordField = document.querySelector('#passwordField');
const feedbackArea = document.querySelector('.invalid-feedback')
const emailFeedbackArea = document.querySelector('.email-feedbackArea')
const usernameSuccessOutput = document.querySelector('.usernameSuccessOutput')
const emailSuccessOutput = document.querySelector('.emailSuccessOutput')
const showPasswordToggle = document.querySelector('.showPasswordToggle')
const submit_btn = document.querySelector('.submit-btn')
console.log("Connected");

//PWD toggle logic
const handleToggleInput = (e) => {
  if (showPasswordToggle.textContent === 'SHOW') {
    showPasswordToggle.textContent = 'HIDE';
    passwordField.setAttribute("type", 'text');

  } else {
    showPasswordToggle.textContent = 'SHOW';
    passwordField.setAttribute("type", 'password');
  }
}

// Password Toggle
showPasswordToggle.addEventListener('click', handleToggleInput);

// Username Validation Function
usernameField.addEventListener("keyup", (e) => {

  const usernameVal = e.target.value;
  usernameField.classList.remove('is-invalid');
  feedbackArea.style.display = 'none';
  usernameSuccessOutput.style.display = 'block';
  usernameSuccessOutput.textContent = `Checking  ${usernameVal}`;
  if (usernameVal.length > 0) {
    fetch('/authentication/validate-username', {
      body: JSON.stringify({
        username: usernameVal
      }),
      method: 'POST',
    }).then(res => res.json()).then(data => {
      // console.log("data", data);
      usernameSuccessOutput.style.display = "none";
      if (data.username_error) {
        submit_btn.disabled = true;
        usernameField.classList.add('is-invalid');
        feedbackArea.style.display = 'block';
        feedbackArea.innerHTML = `<p>${data.username_error}</p>`;
      } else {
        submit_btn.removeAttribute('disabled');
      }
    });
  }
});
// Email Validation Function
emailField.addEventListener("keyup", (e) => {

  const emailVal = e.target.value;
  emailField.classList.remove('is-invalid');
  emailFeedbackArea.style.display = 'none';
  emailSuccessOutput.style.display = 'block';
  emailSuccessOutput.textContent = `Checking  ${emailVal}`;
  if (emailVal.length > 0) {
    fetch('/authentication/validate-email', {
      body: JSON.stringify({
        email: emailVal
      }),
      method: 'POST',
    }).then(res => res.json()).then(data => {
      // console.log("data", data);
      emailSuccessOutput.style.display = "none";
      if (data.email_error) {
        submit_btn.disabled = true;
        emailField.classList.add('is-invalid');
        emailFeedbackArea.style.display = 'block';
        emailFeedbackArea.innerHTML = `<p>${data.email_error}</p>`;
      } else {
        submit_btn.removeAttribute('disabled');
      }
    });
  }
})