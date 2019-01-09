document.getElementById('allIncidents').addEventListener('click', getIncidents);

function getIncidents(e) {
    e.preventDefault();
    fetch('https://issaireporterv2.herokuapp.com/api/v2/incidents')
        .then((res) => res.json())
        .then((data) => {
            console.log(data)
            if (data.Error) {
                alert(data.Error)
            } else {
                let output = `<h2>These are all the incidents the have been reported:</h2>`;
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
                document.getElementById('output3').innerHTML = output;
                alert(data[0].Message)
            }
        })
}