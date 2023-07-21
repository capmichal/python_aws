from flask import Flask, render_template
import requests
import json


app = Flask(__name__) # creating Flask object


def get_player():
    # gets nba player height based on name/lastname input from user
    url = "https://www.balldontlie.io/api/v1/players"

    params = {
        "page": 1,
        "per_page": 15,
        "search": "westbrook"
    }

    response = requests.get(url, params=params)
    try:
        data = response.json()
    except json.JSONDecodeError:
        print("can't read data")
    
    players_heights = []
    for zawodnik in data["data"]:
        if zawodnik["height_feet"] != None and zawodnik["height_inches"]  != None:
            players_heights.append(f"{zawodnik['first_name']} {zawodnik['last_name']} ma {zawodnik['height_feet']} stóp {zawodnik['height_inches']} cali")
    
    return players_heights



# @app.route('/') # decorator that turns python function into a Flask view function 
# def index():
#     return "Hello world"


# app.run(host="0.0.0.0", port=5000)


print(get_player())