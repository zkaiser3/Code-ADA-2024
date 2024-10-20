//turns the patient form inputs from html into json strings to send to app.py

document.getElementById('submit_button').addEventListener('click', function(event) { //select port wait for device
    event.preventDefault();
    let categories = ['depression', 'anxiety', 'adhd', 'ed', 'ptsd'];
    let reason = [0, 0, 0, 0, 0];

    //retreiving reason mental health answers (0-5)
    for (let i = 0; i < 5; i++){
        for (let x = 1; x < 6; x++){
            let name = categories[i] + x;
            console.log(name)
            const answer = document.getElementById(categories[i] + x).value;
            reason[i] += parseInt(answer);
        }
    }
    console.log('Answers being sent:', answers); // Log answers


    //retreiving lgbtq preference
    const lgbtqSelect = document.getElementById('lgbtq');
    lgbtqSelect.addEventListener('change', function() {
        const lgbtq = lgbtqSelect.value; // Get the selected value
        console.log('Selected LGBTQ+ specialty:', lgtq); // Log it or use it as needed
    });

    //retreiving substance abuse
    const substanceSelect = document.getElementById('lgbtq');
    substanceSelect.addEventListener('change', function() {
        const substance = substanceSelect.value; // Get the selected value
        console.log('Selected substance abuse:', substance); // Log it or use it as needed
    });

    //retreiving gender preference
     const genderSelect = document.getElementById('gender');
     genderSelect.addEventListener('change', function() {
         const gender = genderSelect.value; // Get the selected value
         console.log('Selected gender preference:', gender); // Log it or use it as needed
    });

    //retreiving availability
    days_of_week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    let availability = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for (let i = 0; i < 7; i++){
        
    }

    
    

    fetch('/patient_form', {
        method: 'POST',  // Sending data via POST
        headers: {
            'Content-Type': 'application/json',  // Specify that you're sending JSON data
        },
        body: JSON.stringify({ 
            reason: reason
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