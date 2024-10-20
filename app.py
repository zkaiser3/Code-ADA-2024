from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
#import patient_therapist as pt


@app.route('/') #called when post request is made to "/"
def home(): 
    return render_template('index.html') #loads the main index.html page


######################### Doctor Integration ###################################
@app.route('/doctor')
def doctor(): 
    return render_template('doctor.html') #loads the signup.html website

@app.route('/new_form')
def new_form(): 
    return render_template('new_form.html') #loads the signup.html website


######################### Patient Integration ###################################
@app.route('/patient')
def patient(): 
    return render_template('patient.html') #loads the signup.html website

@app.route('/doctor_matches')
def doctor_matches(): 
    return render_template('doctor_matches.html') #loads the signup.html website