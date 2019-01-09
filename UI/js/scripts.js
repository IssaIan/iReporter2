// geoloctaion api
var x = document.getElementById("location");
x.addEventListener('focus', getLocation);

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.outerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    y = "Latitude: " + position.coords.latitude +
        " Longitude: " + position.coords.longitude;
    document.getElementById("location").value = y;
}


let mainNav = document.getElementById('navbar-right');
let navBarToggle = document.getElementById('navbar-toggle');

navBarToggle.addEventListener('click', function () {
    mainNav.classList.toggle('active');
});

function openPage(pageName, elmnt) {
    // Hide all elements with class="tabcontent" by default */
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("flex-container");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    // Remove the background color of all tablinks/buttons
    tablinks = document.getElementsByClassName("button");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "";
    }
    // Show the specific tab content
    document.getElementById(pageName).style.display = "flex";
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();