from flask import Flask, render_template, url_for, request, redirect
import numpy as np

class Patient:
    def __init__(self, name, availability, reason, insurance, price_range, gender_preference):
        self.name = name
        
        #Availability in the patient and therapist class is a 1D array with 3 entries for every day of the week
        # representing morning, afternoon, and evening.
        self.availability = availability

        #Reason is a 1 dimensional array with 7 entries. In order, they represent depression, anxiety, ADHD, disordered
        # eating, PTSD, LGBTQ+ specialty, and substance abuse specialty. The first 5 entries represent
        # a score of severity between 0 and 5. The next 2 are '1' if yes, '0' if no preference.
        self.reason = reason

        #A string with the patient's insurance
        self.insurance = insurance

        #Either a, b, c, d, or e representing the patient's desired price range
        self.price_range = price_range

        #An array with the genders that the patient prefers, can be empty
        self.gender_preference = gender_preference

class Therapist:
    def __init__(self, name, availability, specialty, insurance, cost, gender):
        self.name = name

        #Availability in the patient and therapist class is a 1D array with 3 entries for every day of the week
        # representing morning, afternoon, and evening.
        self.availability = availability
        
        #Specialty follows the same format at Reason in the Patient class. However, each doctor entry will either be 
        # 1 or 0 if they specialize in it or not.
        self.specialty = specialty
        
        #An array of the insurances that the therapist takes
        self.insurance = insurance
        
        #Either a, b, c, d, or e representing the therapist's cost
        self.cost = cost

        #'Male' 'female' or 'other'
        self.gender = gender

#Match uses the below helper functions to determine the total 'score' a therapist gets for a certain
# patient. 
def Match(patient, therapist):
    score = 0

    #no availability, gender doesn't match, no insurance = score of zero
    if Match_availability(patient, therapist) == 0 or Match_gender(patient, therapist) == 0 or Match_insurance(patient, therapist) == 0:
        return score
    
    #add availability to the score
    score += Match_availability(patient, therapist)

    #add specialty reason match to the score
    score += Match_reason(patient, therapist)

    #add price match to the score, multiplied by 5 to increase importance
    score += 5 * (Match_prices(patient, therapist))
    

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
    

def Match_reason(patient, therapist):
    #Loop will iterate 7 times for each entry in patient.reason. The first 5 entries are a score 0-25
    # then the next 2 are either 0 or 1. The function returns the number of points based on specialty
    # reason matching.
    points = 0
    for i in range(len(patient.reason)):
        if patient.reason[i] == 0:
            continue
        
        #If the index is 5 or 6 (LGBTQ+ or substance abuse specialty), add 5 points if the doctor specializes
        # in it and the patient requested.
        if i == 5 or i == 6:
            if patient.reason[i] == 1 and therapist.specialty[i] == 1:
                points += 5
            continue

        #For the first 5 common college student disorders, if the students ranks 15-25 on the scale and the
        # therapist specializes, add 5 points.
        elif patient.reason[i] >= 15 and therapist.specialty[i] == 1:
            points += 5

        #If the student has a mild case and ranks 1-15 and the doctor specializes in it, add 2 points.
        elif patient.reason[i] > 0 and therapist.specialty[i] == 1:
            points += 2

    return points
    
#This function takes the patient's array of gender preferences, which may be empty, and scores based on the therapist's
# gender. Returns 1 if they're matched or if the patient has no preferences.
def Match_gender(patient, therapist):
    if (len(patient.gender_preference) == 0):
        return 1
    elif (therapist.gender in patient.gender_preference):
        return 1
    else:
        return 0