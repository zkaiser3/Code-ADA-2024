from flask import Flask, render_template, request, jsonify, url_for
import patient_therapist as pt
import sqlite3

DATABASE = 'database.db'
app = Flask(__name__)


@app.route('/') #called when post request is made to "/"
def home(): 
    return render_template('index.html') #loads the main index.html page



######################### SQL Integration ###################################
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


######################### Resource Integration ###################################
@app.route('/resources')
def resources(): 
    return render_template('resources.html') #loads the signup.html website


######################### Doctor Integration ###################################
@app.route('/doctor')
def doctor(): 
    return render_template('doctor.html') #loads the signup.html website

@app.route('/doctor_form')
def new_form(): 
    return render_template('doctor_form.html') #loads the signup.html website


######################### Patient Integration ###################################
@app.route('/patient')
def patient(): 
    return render_template('patient.html') #loads the signup.html website

@app.route('/doctor_matches')
def doctor_matches(): 
    return render_template('doctor_matches.html') #loads the signup.html website

@app.route('/patient_form', methods=['POST'])
def patient_form(): 
    # Get the JSON data from the request
    data = request.get_json()

    # Extract username and password from the data
    availability = data.get('availability')
    reason = data.get('reason')
    insurance = data.get('insurance')
    price_range = data.get('price')
    gender_preference = data.get('gender')

    # Add user handling logic
    patient = pt.Patient(name, availability, reason, insurance, price_range, gender_preference)

    # Return a JSON response
    return jsonify({"message": "Form submitted correctly", "redirect": url_for('doctor_matches')})