//turns the patient form inputs from html into json strings to send to app.py

document.getElementById('submit_button').addEventListener('click', function(event) { //select port wait for device
    event.preventDefault();

    //retreiving reason mental health answers (0-5)
    let categories = ['depression', 'anxiety', 'adhd', 'ed', 'ptsd'];
    let reasons = [0, 0, 0, 0, 0];
    for (let i = 0; i < 5; i++){
        for (let x = 1; x < 6; x++){
            const answer = document.getElementById(categories[i] + x).value;
            reasons[i] += parseInt(answer);
        }
    }
    console.log('Answers being sent:', reasons); // Log answers

    
    //retreiving availability
    days_of_week = ['sun', 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat']
    let availability = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for (let i = 0; i < 7; i++){
        for (let x = 0; x < 3; x++){
            const checkbox = document.getElementById(days_of_week[i] + x);
        
            // Check if the checkbox exists and if it's checked
            if (checkbox) {
                availability[(i * 3) + x] = checkbox.checked ? 1 : 0;  // Store 1 if checked, otherwise 0
            }
        } 
    }
    console.log('Selected availability array:', availability); // Log it or use it as needed


    //retreiving lgbtq preference
    const lgbtqSelect = document.getElementById('lgbtq');
    const lgbtq = lgbtqSelect.value; // Get the selected value
    console.log('Selected LGBTQ+ specialty:', lgbtq); // Log it or use it as needed

    //retreiving substance abuse
    const substanceSelect = document.getElementById('substance');
    const substance = substanceSelect.value; // Get the selected value
    console.log('Selected substance abuse:', substance); // Log it or use it as needed

    //retreiving gender preference
    const genderSelect = document.getElementById('gender');
    const gender = genderSelect.value; // Get the selected value
    console.log('Selected gender preference:', gender); // Log it or use it as needed


    //retreiving insurance
    const insuranceSelect = document.getElementById('insurance');
    const insurance = insuranceSelect.value; // Get the selected value
    console.log('Selected insurance:', insurance); // Log it or use it as needed


    //retreiving price
    const priceSelect = document.getElementById('price');
        const price = priceSelect.value; // Get the selected value
        console.log('Selected price-range:', price); // Log it or use it as needed
    

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
        if (data.redirect) {
            window.location.href = data.redirect; // Redirect to the new page
        }
    })
    .catch((error) => {
        console.error('Error:', error);  // Handle any errors that occur
    });

});