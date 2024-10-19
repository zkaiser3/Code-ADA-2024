from flask import Flask, render_template, url_for, request, redirect
import numpy as np

class Patient:
    def __init__(self, name, availability, reason, gender_pref, insurance, price_range):
        self.name = name
        self.availability = availability
        self.reason = reason
        self.gender_pref = gender_pref
        self.insurance = insurance
        self.price_range = price_range

class Therapist:
    def __init__(self, name, availability, specialty, gender, insurance, cost):
        self.name = name
        self.availability = availability
        self.specialty = specialty
        self.gender = gender
        self.insurance = insurance
        self.cost = cost

def Match(patient, therapist):

#Match_availability takes in the therapist's matrix of availabilities and patient's matrix
# and returns the number of times of day they're both available
# matrix is in the format [(Sunday) morning, afternoon, night, Monday etc, 21 total
# 1 = available, 0 = unavailable
def Match_availability(patient, therapist):
    score = 0
    for i in range(len(patient.availability)):
        if (patient.availability[i] == 1 and therapist.availability[i] == 1):
            score += 1
    return score

#The website will include a list of common insurances taken. The patient inputs their one insurance
# and the therapist will include an array of insurances they take. The function returns 1 if the 
# therapist takes their insurance and 0 if they do not.
def Match_insurance(patient, therapist):
    if patient.insurance in therapist.insurance:
        return 1
    else:
        return 0
    
#The patient will select their desired price range. If it matches the therapist's, the function returns
# 1. If not, it will return 0
# the website will have 5 different price ranges (a, b, c, d, e)
def Match_prices(patient, therapist):
    if patient.price_range == therapist.cost:
        return 1
    else:
        return 0
    
