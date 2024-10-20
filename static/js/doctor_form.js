//turns the patient form inputs from html into json strings to send to app.py

document.getElementById('submit_button').addEventListener('click', function(event) { //select port wait for device
    event.preventDefault();

    //retreiving specialty
    const specialtySelect = document.getElementById('specialty');
    // Initialize an array to hold selected values
    const selectedSpecialties = [];
    // Loop through selected options and push values to the array
    for (let option of specialtySelect.selectedOptions) {
        selectedSpecialties.push(option.value);
    }
    // Output the selected specialties in an array
    console.log('Array of doctor specialties:', selectedSpecialties);

    //how it's handled with the patient
    //let categories = ['depression', 'anxiety', 'adhd', 'ed', 'ptsd'];
    //let reasons = [0, 0, 0, 0, 0];
    //for (let i = 0; i < 5; i++){
        //for (let x = 1; x < 6; x++){
            //const answer = document.getElementById(categories[i] + x).value;
            //reasons[i] += parseInt(answer);
      //  }
    //}
    //console.log('Answers being sent:', reasons); // Log answers

    
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


    //retrieving doctor's gender
    const genderSelect = document.getElementById('gender');
    const gender = genderSelect.value; // Get the selected value
    console.log('Selected gender preference:', gender); // Log it or use it as needed

    //retreiving insurances
    const insuranceSelect = document.getElementById('insurance');
    // Initialize an array to hold selected values
    const selectedInsurances = [];
    // Loop through selected options and push values to the array
    for (let option of insuranceSelect.selectedOptions) {
        selectedInsurances.push(option.value);
    }
    // Output the selected specialties in an array
    console.log('Array of doctor specialties:', selectedInsurances);

    //retreiving insurance in patiend
    //const insuranceSelect = document.getElementById('insurance');
    //const insurance = insuranceSelect.value; // Get the selected value
    //console.log('Selected insurance:', insurance); // Log it or use it as needed


    //retreiving price
    const priceSelect = document.getElementById('price');
        const price = priceSelect.value; // Get the selected value
        console.log('Selected price-range:', price); // Log it or use it as needed
    

    fetch('/submit_doctor_info', {
        method: 'POST',  // Sending data via POST
        headers: {
            'Content-Type': 'application/json',  // Specify that you're sending JSON data
        },
        body: JSON.stringify({ 
            specialty: selectedSpecialties, 
            availability: availability, 
            insurance: selectedInsurances, 
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