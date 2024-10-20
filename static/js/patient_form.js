//turns the patient form inputs from html into json strings to send to app.py

document.getElementById('submit_button').addEventListener('click', function(event) { //select port wait for device
    event.preventDefault();

    //retreiving reason mental health answers (0-5)
    let categories = ['depression', 'anxiety', 'adhd', 'ed', 'ptsd'];
    let reasons = [0, 0, 0, 0, 0];
    for (let i = 0; i < 5; i++){
        for (let x = 1; x < 6; x++){
            let name = categories[i] + x;
            console.log(name)
            const answer = document.getElementById(categories[i] + x).value;
            reasons[i] += parseInt(answer);
        }
    }
    console.log('Answers being sent:', reasons); // Log answers


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
    days_of_week = ['sun', 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat']
    let availability = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for (let i = 0; i < 7; i++){
        for (let x = 0; x < 3; x++){
            let name = days_of_week[i] + x;
            console.log(name)
            const answer = document.getElementById(days_pf_week[i] + x).value;
            availability[(i*3)+x] += parseInt(answer);
        }
        
    }

    //retreiving insurance
    const insuranceSelect = document.getElementById('insurance');
    insuranceSelect.addEventListener('change', function() {
        const insurance = insuranceSelect.value; // Get the selected value
        console.log('Selected gender preference:', insurance); // Log it or use it as needed
    });

    //retreiving price
    const priceSelect = document.getElementById('price');
    priceSelect.addEventListener('change', function() {
        const price = priceSelect.value; // Get the selected value
        console.log('Selected gender preference:', price); // Log it or use it as needed
    });
    
    fetch('/patient_form', {
        method: 'POST',  // Sending data via POST
        headers: {
            'Content-Type': 'application/json',  // Specify that you're sending JSON data
        },
        body: JSON.stringify({ 
            reasons: reasons, 
            lgbtq: lgbtq, 
            substance: substance, 
            availability: availability, 
            insurance: insurance, 
            price: price
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