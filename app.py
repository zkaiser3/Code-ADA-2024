from flask import Flask, render_template, url_for, request, redirect
import numpy as np

class Therapist:
    def __init__(self, name, location, availability, reason, gender_pref, insurance_price):
        self.name = name
        self.location = location
        

class Patient:
    def __init__(self, id, name, ):
        self.id = id
        self.name = name
