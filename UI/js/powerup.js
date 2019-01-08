document.getElementById('post').addEventListener('click', postIncident);
document.getElementById('type').addEventListener('click', getIncidentsbyType);
document.getElementById('findone').addEventListener('click', getIncident);
document.getElementById('edit1').addEventListener('click', editDescription);
document.getElementById('edit2').addEventListener('click', editLocation);


function postIncident(e) {
  e.preventDefault();
  let token = sessionStorage.getItem('token');
  fetch('https://issaireporterv2.herokuapp.com/api/v2/incidents', {
      method: 'POST',
      body: JSON.stringify({
        typeofincident: document.getElementById('record_type').value,
        description: document.getElementById('description').value,
        location: document.getElementById('location').value
      }),
      headers: {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
      }
    })
    .then(res => res.json())
    .then(data => {
      console.log(data)
      if (data.Message == 'Record successfully saved!') {
        alert(data.Message)
      } else {
        alert(data.Error)
      }
    })
}

function getIncidentsbyType(e) {
  e.preventDefault();
  let token = sessionStorage.getItem('token');
  let incidenttype = document.getElementById('record_type').value;
  fetch(`https://issaireporterv2.herokuapp.com/api/v2/${incidenttype}`, {
      method: 'GET',
      headers: {
        'Authorization': 'Bearer ' + token
      }
    })
    .then((res) => res.json())
    .then((data) => {
      console.log(data)
      if (data.Error) {
        alert(data.Error)
      } else {
        let output = `<h2>Incidents</h2>`;
        data[0].Data.forEach(function (incident) {
          output += `
            <ul class="list-group mb-3">
                <li class="list-group-item">INCIDENT ID: ${incident.incident_id}</li>
                <li class="list-group-item">CREATED BY: ${incident.created_by}</li>
                <li class="list-group-item">CREATED ON: ${incident.created_on}</li>
                <li class="list-group-item">STATUS: ${incident.status}</li>
                <li class="list-group-item">TYPE OF INCIDENT: ${incident.type}</li>
                <li class="list-group-item">DESCRIPTION: ${incident.description}</li>
                <li class="list-group-item">LOCATION: ${incident.location}</li>
            </ul>
            `;
        });
        document.getElementById('output').innerHTML = output;
        alert(data[0].Message)
      }
    })
}

function getIncident(e) {
  e.preventDefault();
  let token = sessionStorage.getItem('token');
  let incidenttype = document.getElementById('record_type').value;
  let incident_id = document.getElementById('incident_id').value;
  fetch(`https://issaireporterv2.herokuapp.com/api/v2/${incidenttype}/${incident_id}`, {
      method: 'GET',
      headers: {
        'Authorization': 'Bearer ' + token
      }
    })
    .then((res) => res.json())
    .then((data) => {
      console.log(data)
      if (data.Error) {
        alert(data.Error)
      } else {
        let output = `<h2>Incident to be Updated</h2>`;
        data[0].Data.forEach(function (incident) {
          output += `
            <ul class="list-group mb-3">
                <label><strong>INCIDENT ID: </strong></label><br>
                <li class="list-group-item">${incident.incident_id}</li><br>
                <label><strong>CREATED BY: </strong></label><br>
                <li class="list-group-item">${incident.created_by}</li><br>
                <label><strong>CREATED ON: </strong></label><br>
                <li class="list-group-item">${incident.created_on}</li><br>
                <label><strong>STATUS: </strong></label><br>
                <li class="list-group-item">${incident.status}</li><br>
                <label><strong>TYPE OF INCIDENCE: </strong></label><br>
                <li class="list-group-item">${incident.type}</li><br>
                <label><strong>DESCRIPTION: </strong></label><br>
                <li id="edit_description" class="list-group-item" contenteditable="true">${incident.description}</li><br>
                <label><strong>LOCATION: </strong></label><br>
                <li id="edit_location" class="list-group-item" contenteditable="true">${incident.location}</li><br>
            </ul>
            `;
        });
        document.getElementById('output2').innerHTML = output;
        alert(data[0].Message)
      }
    })
}

function editDescription(e) {
  e.preventDefault();
  let token = sessionStorage.getItem('token');
  let incidenttype = document.getElementById('record_type').value;
  let incident_id = document.getElementById('incident_id').value;
  fetch(`https://issaireporterv2.herokuapp.com/api/v2/${incidenttype}/${incident_id}/comment`, {
      method: 'PATCH',
      body: JSON.stringify({
        description: document.getElementById('edit_description').innerHTML,
      }),
      headers: {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
      }
    })
    .then(res => res.json())
    .then(data => {
      console.log(data)
      if (data[0].Message == `Updated ${incidenttype} comment successfully!`) {
        alert(data[0].Message)
      } else if (data.Error){
        alert(data.Error)
      } else {
        alert(data.message)
      }
    })
}

function editLocation(e) {
  e.preventDefault();
  let token = sessionStorage.getItem('token');
  let incidenttype = document.getElementById('record_type').value;
  let incident_id = document.getElementById('incident_id').value;
  fetch(`https://issaireporterv2.herokuapp.com/api/v2/${incidenttype}/${incident_id}/location`, {
      method: 'PATCH',
      body: JSON.stringify({
        location: document.getElementById('edit_location').innerHTML,
      }),
      headers: {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
      }
    })
    .then(res => res.json())
    .then(data => {
      console.log(data)
      if (data[0].Message == `Updated ${incidenttype} location successfully!`) {
        alert(data[0].Message)
      } else if (data.Error){
        alert(data.Error)
      } else {
        alert(data.message)
      }
    })
}