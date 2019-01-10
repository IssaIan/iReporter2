document.getElementById('register').addEventListener('click', registerUser);

function registerUser(e) {
  e.preventDefault();
  fetch('https://issaireporterv2.herokuapp.com/api/v2/auth/signup', {
      method: 'POST',
      body: JSON.stringify({
        first_name: document.getElementById('first_name').value,
        last_name: document.getElementById('last_name').value,
        username: document.getElementById('username').value,
        email: document.getElementById('email').value,
        phonenumber: document.getElementById('phonenumber').value,
        password: document.getElementById('password').value,
        confirm_password: document.getElementById('confirm_password').value
      }),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(res => res.json())
    .then(data => {
      if (data.Message == "User saved successfully") {
        alert(data.Message)
        window.location = "usignin.html"
      } else {
        alert(data.Error)
      }
    })
}