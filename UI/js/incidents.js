document.getElementById('getallincidents').addEventListener('click', getIncidents);

function getIncidents(){
    fetch('https://issaireporterv2.herokuapp.com/api/v2/incidents')
        .then((res) => res.json())
        .then((data) => {
            if (data.Error) {
                alert(data.Error)
            } else {
                let output = `<h2>These are all the incidents that have been reported in iReporter:</h2>`;
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
                  <li class="list-group-item"><img src="${incident.media_path}.png" alt="Incident image" width="800" height="500"></li> 
              </ul>
              `;
                });
                document.getElementById('output3').innerHTML = output;
                alert(data[0].Message)
            }
        })
}