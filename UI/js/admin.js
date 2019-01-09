document.getElementById('getusers').addEventListener('click', getUsers);
document.getElementById('find').addEventListener('click', admingetIncident);
document.getElementById('editstatus').addEventListener('click', updateStatus);

function getUsers(e) {
  e.preventDefault();
  let token = sessionStorage.getItem('token');
  fetch('https://issaireporterv2.herokuapp.com/api/v2/auth/signup', {
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
        let output = `<h2>These are all the users currently in the system:</h2>`;
        data[0].Data.forEach(function (user) {
          output += `
                  <ul class="list-group mb-3">
                      <li class="list-group-item">USER ID: ${user.user_id}</li>
                      <li class="list-group-item">FIRST NAME: ${user.first_name}</li>
                      <li class="list-group-item">LAST NAME: ${user.last_name}</li>
                      <li class="list-group-item">USERNAME: ${user.username}</li>
                      <li class="list-group-item">EMAIL: ${user.email}</li>
                      <li class="list-group-item">PHONE NUMBER: 0${user.phonenumber}</li>
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
      console.log(data)
      if (data.Error) {
        alert(data.Error)
      } else if (data.message) {
        alert(data.message)
      } else {
        let output = `<h2>Incident to be Updated</h2>`;
        data[0].Data.forEach(function (incident) {
          output += `
            <ul class="list-group mb-3">
                <label><strong>INCIDENT ID: </strong></label><br>
                <li class="list-group-item">${incident.incident_id}</li>
                <label><strong>CREATED BY: </strong></label><br>
                <li class="list-group-item">${incident.created_by}</li>
                <label><strong>CREATED ON: </strong></label><br>
                <li class="list-group-item">${incident.created_on}</li>
                <label><strong>STATUS: </strong></label><br>
                <li class="list-group-item">${incident.status}
                <br>
                  <select name="status" id="edit_status">
                      <option value="intervention">Under Investigation</option>
                      <option value="red-flag">Rejected</option>
                      <option value="red-flag">Resolved</option>
                  </select>
                <br>
                </li>
                <label><strong>TYPE OF INCIDENCE: </strong></label><br>
                <li class="list-group-item">${incident.type}</li>
                <label><strong>DESCRIPTION: </strong></label><br>
                <li class="list-group-item">${incident.description}</li>
                <label><strong>LOCATION: </strong></label><br>
                <li class="list-group-item">${incident.location}</li>
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
        status: document.getElementById('edit_status').innerHTML,
      }),
      headers: {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
      }
    })
    .then(res => res.json())
    .then(data => {
      console.log(data)
      if (data[0].Message) {
        alert(data[0].Message)
      } else if (data.Error) {
        alert(data.Error)
      } else {
        alert(data.message)
      }
    })
}