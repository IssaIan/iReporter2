document.getElementById('getusers').addEventListener('click', getUsers);
document.getElementById('find').addEventListener('click', admingetIncident);
document.getElementById('editstatus').addEventListener('click', updateStatus);

function getUsers() {
  let token = sessionStorage.getItem('token');
  fetch('https://issaireporterv2.herokuapp.com/api/v2/auth/signup', {
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
        let output = `<h2>These are all the users currently in the system:</h2>`;
        data[0].Data.forEach(function (user) {
          output += `
                  <ul class="list-group mb-3">
                      <li class="list-group-item"><strong>USER ID: </strong>${user.user_id}</li>
                      <li class="list-group-item"><strong>FIRST NAME: </strong>${user.first_name}</li>
                      <li class="list-group-item"><strong>LAST NAME: </strong>${user.last_name}</li>
                      <li class="list-group-item"><strong>USERNAME: </strong>${user.username}</li>
                      <li class="list-group-item"><strong>EMAIL: </strong>${user.email}</li>
                      <li class="list-group-item"><strong>PHONE NUMBER: </strong>${user.phonenumber}</li>
                  </ul>
                  `;
        });
        document.getElementById('output4').innerHTML = output;
        alert(data[0].Message)
      }
    })
}


function admingetIncident(e) {
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
                <li class="list-group-item"><strong>STATUS: </strong>${incident.status}</li>
                <li class="list-group-item"><strong>DESCRIPTION: </strong>${incident.description}</li>
                <li class="list-group-item"><strong>LOCATION: </strong>${incident.location}</li>
                <li class="list-group-item"><img src="${incident.media_path}.png" alt="Incident image" width="800" height="500"></li> 
            </ul>
            `;
        });
        document.getElementById('output5').innerHTML = output;
        alert(data[0].Message)
      }
    })
}

function updateStatus(e) {
  e.preventDefault();
  let token = sessionStorage.getItem('token');
  let incidenttype = document.getElementById('record_type').value;
  let incident_id = document.getElementById('incident_id').value;
  fetch(`https://issaireporterv2.herokuapp.com/api/v2/admin/${incidenttype}/${incident_id}/statusupdate`, {
      method: 'PATCH',
      body: JSON.stringify({
        status: document.getElementById('edit_status').value,
      }),
      headers: {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
      }
    })
    .then(res => res.json())
    .then(data => {
      if (data[0].Message) {
        alert(data[0].Message)
      } else if (data.Error) {
        alert(data.Error)
      } else {
        alert(data.message)
      }
    })
}