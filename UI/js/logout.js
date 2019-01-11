document.getElementById('logout').addEventListener('click', logOutUser);

function logOutUser(){
    sessionStorage.removeItem('token')
    window.location = "usignin.html"
}