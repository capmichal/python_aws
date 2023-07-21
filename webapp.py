from flask import Flask, render_template
import requests
import json


app = Flask(__name__) # creating Flask object

@app.route('/') # decorator that turns python function into a Flask view function 
def index():
    return "Hello world"


app.run(host="0.0.0.0", port=5000)
