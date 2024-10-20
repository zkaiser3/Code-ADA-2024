//turns the patient form inputs from html into json strings to send to app.py

document.getElementById('submit_button').addEventListener('click', function(event) { //select port wait for device
    event.preventDefault();
    let categories = ['depression', 'anxiety', 'adhd', 'ed', 'ptsd'];
    let answers = [0, 0, 0, 0, 0];

    for (let i = 0; i < 5; i++){
        for (let x = 1; x < 6; x++){
            let name = categories[i] + x;
            console.log(name)
            const answer = document.getElementById(categories[i] + x).value;
            answers[i] += parseInt(answer);
        }
    }


    fetch('/patient_form', {
        method: 'POST',  // Sending data via POST
        headers: {
            'Content-Type': 'application/json',  // Specify that you're sending JSON data
        },
        body: JSON.stringify({ 
            answers: answers,  
            
        })  // Convert the array to JSON and include in the body
    })
    .then(response => response.json())  // Parse the response as JSON
    .then(data => {
        console.log('Success:', data);  // Log the response from the server
    })
    .catch((error) => {
        console.error('Error:', error);  // Handle any errors that occur
    });

});