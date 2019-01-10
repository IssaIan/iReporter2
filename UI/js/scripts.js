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

function openPage(pageName, elmnt) {
    // Hide all elements with class="tabcontent" by default */
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("flex-container");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    // Show the specific tab content
    document.getElementById(pageName).style.display = "flex";
}