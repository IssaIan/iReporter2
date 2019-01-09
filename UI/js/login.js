document.getElementById('login').addEventListener('click', loginUser);

function loginUser(e){
    e.preventDefault();
    fetch('https://issaireporterv2.herokuapp.com/api/v2/auth/login',{
        method: 'POST',
        body: JSON.stringify({
          username: document.getElementById('username').value,
          password: document.getElementById('password').value
        }),
        headers: {
          'Content-Type': 'application/json'
        }
      })
      .then(res => res.json())
      .then(data => {
        let user = document.getElementById('username').value;
        sessionStorage.setItem('user', user)
        let token = data[0].Token
        sessionStorage.setItem('token', token)
        if (data[0].User[0].is_admin === false) {
            alert(data[0].Message)
            window.location = "useracc.html"
          } else if (data[0].User[0].is_admin !== false){
            alert(data[0].Message)
            window.location = "admin.html"
          } else {
            alert(data.Error)
          }
        })
}