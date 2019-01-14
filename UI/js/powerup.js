document.getElementById('post').addEventListener('click', postIncident);
document.getElementById('type').addEventListener('click', getIncidentsbyType);
document.getElementById('getstatus').addEventListener('click', getIncidentsbyStatus);
document.getElementById('findone').addEventListener('click', getIncident);
document.getElementById('delete').addEventListener('click', deleteIcident);


function postIncident(e) {
  e.preventDefault();
  let token = sessionStorage.getItem('token');
  let formdata = new FormData();
  formdata.append("typeofincident", document.getElementById('record_type').value);
  formdata.append("description", document.getElementById('description').value);
  formdata.append("location", document.getElementById('location').value);
  formdata.append('file', document.getElementById("media").files[0]); 
  fetch('https://issaireporterv2.herokuapp.com/api/v2/incidents', {
      method: 'POST',
      body: formdata,
      headers: {
        'Authorization': 'Bearer ' + token
      }
    })
    .then(res => res.json())
    .then(data => {
      console.log(data)
      if (data.Message) {
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
      if (data.Error) {
        alert(data.Error)
      } else {
        let output = `<h2 style="text-transform: uppercase;">${data[0].Data[0].type}s</h2>`;
        data[0].Data.forEach(function (incident) {
          output += `
            <ul class="list-group mb-3">
            <li class="list-group-item"><strong>INCIDENT ID: </strong>${incident.incident_id}</li>
            <li class="list-group-item"><strong>CREATED BY: </strong>${incident.created_by}</li>
            <li class="list-group-item"><strong>CREATED ON: </strong>${incident.created_on}</li>
            <li class="list-group-item"><strong>STATUS: </strong>${incident.status}</li>
            <li class="list-group-item"><strong>TYPE OF INCIDENT: </strong>${incident.type}</li>
            <li class="list-group-item"><strong>DESCRIPTION: </strong>${incident.description}</li>
            <li class="list-group-item"><strong>LOCATION: </strong>${incident.location}</li>
            </ul>
            `;
        });
        document.getElementById('output').innerHTML = output;
        alert(data[0].Message)
      }
    })
}

function getIncidentsbyStatus(e) {
  e.preventDefault();
  let token = sessionStorage.getItem('token');
  let status = document.getElementById('status').value;
  fetch(`https://issaireporterv2.herokuapp.com/api/v2/incidents/${status}`, {
      method: 'GET',
      headers: {
        'Authorization': 'Bearer ' + token
      }
    })
    .then((res) => res.json())
    .then((data) => {
      if (data.Error) {
        alert(data.Error)
      } else {
        let output = `<h2 style="text-transform: uppercase;">${data[0].Data[0].status}</h2>`;
        data[0].Data.forEach(function (incident) {
          output += `
            <ul class="list-group mb-3">
            <li class="list-group-item"><strong>INCIDENT ID: </strong>${incident.incident_id}</li>
            <li class="list-group-item"><strong>CREATED BY: </strong>${incident.created_by}</li>
            <li class="list-group-item"><strong>CREATED ON: </strong>${incident.created_on}</li>
            <li class="list-group-item"><strong>STATUS: </strong>${incident.status}</li>
            <li class="list-group-item"><strong>TYPE OF INCIDENT: </strong>${incident.type}</li>
            <li class="list-group-item"><strong>DESCRIPTION: </strong>${incident.description}</li>
            <li class="list-group-item"><strong>LOCATION: </strong>${incident.location}</li>
            </ul>
            `;
        });
        document.getElementById('outputstatus').innerHTML = output;
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
      if (data.Error) {
        alert(data.Error)
      } else if (data.message) {
        alert(data.message)
      } else {
        let output = `<h2>Incident to be Updated</h2>`;
        data[0].Data.forEach(function (incident) {
          output += `
          <ul class="list-group mb-3">
                <li class="list-group-item"><strong>INCIDENT ID: </strong>${incident.incident_id}</li>
                <li class="list-group-item"><strong>CREATED BY: </strong>${incident.created_by}</li>
                <li class="list-group-item"><strong>CREATED ON: </strong>${incident.created_on}</li>
                <li class="list-group-item"><strong>TYPE OF INCIDENCE: </strong>${incident.type}</li>
                <li class="list-group-item"><strong>STATUS: </strong>${incident.status}</li><br>
                <li class="list-group-item"><strong>LOCATION: </strong>${incident.media_path}</li>
                <label><strong>DESCRIPTION: </strong></label><br><p>Click to edit</p><br>
                <li id="edit_description" class="list-group-item" contenteditable="true">${incident.description}</li>
                <button class="button btn-green" onclick="editDescription()">Update Description</button><br>
                <label><strong>LOCATION: </strong></label><br><p>Click to edit</p><br>
                <li id="edit_location" class="list-group-item" contenteditable="true">${incident.location}</li>
                <button id="edit2" class="button btn-yellow" onclick="editLocation()">Update Location</button><br>
                <li class="list-group-item"><div>
                <label for="media"><strong>Edit Image or Video:</strong> </label><br>
                <input  id="media2" class="username" type="file" align="center" accept="Image/*,Video/*">
                </div>
                <button id="edit3" class="button btn-yellow" onclick="uploadMedia()">Upload</button>
                </li>
            </ul>
            `;
        });
        document.getElementById('output2').innerHTML = output;
        alert(data[0].Message)
      }
    })
}

function editDescription() {
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
      if (data.Error) {
        alert(data.Error)
      } else if (data.message) {
        alert(data.message)
      } else {
        alert(data[0].Message)
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
      if (data.Error) {
        alert(data.Error)
      } else if (data.message) {
        alert(data.message)
      } else {
        alert(data[0].Message)
      }
    })
}

function deleteIcident(e) {
  e.preventDefault();
  let token = sessionStorage.getItem('token');
  let incidenttype = document.getElementById('record_type1').value;
  let incident_id = document.getElementById('incident_id1').value;
  fetch(`https://issaireporterv2.herokuapp.com/api/v2/${incidenttype}/${incident_id}`, {
      method: 'DELETE',
      headers: {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
      }
    })
    .then(res => res.json())
    .then(data => {
      if (data.Error) {
        alert(data.Error)
      } else if (data.Message) {
        alert(data.Message)
      } else {
        alert(data.message)
      }
    })
}

function uploadMedia(){
  let token = sessionStorage.getItem('token');
  let incidenttype = document.getElementById('record_type').value;
  let incident_id = document.getElementById('incident_id').value;
  let formdata = new FormData();
  formdata.append('file', document.getElementById("media2").files[0]); 
  fetch(`https://issaireporterv2.herokuapp.com/api/v2/${incidenttype}/${incident_id}/media`, {
      method: 'PATCH',
      body: formdata,
      headers: {
        'Authorization': 'Bearer ' + token
      }
    })
    .then(res => res.json())
    .then(data => {
      console.log(data)
      if (data[0].Message) {
        alert(data[0].Message)
      } else {
        alert(data.Error)
      }
    })
}