from flask import Flask, render_template, request
import requests
import json
#CHANGE

app = Flask(__name__) # creating Flask object


def get_player(name):
    # gets nba player height based on name/lastname input from user
    url = "https://www.balldontlie.io/api/v1/players"

    params = {
        "page": 1,
        "per_page": 15,
        "search": name
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


#print(get_player("lebron"))

@app.route('/', methods=["GET", "POST"]) # decorator that turns python function into a Flask view function 
def index():
    if request.method == "POST":
        player_name = request.form["player_name"]
    else:
        player_name = "gordon"
    players_heights = get_player(player_name)
    #print(players_heights)
    return render_template("players.html", players_heights=players_heights)


app.run(host="0.0.0.0", port=5000)

# thanks to free API resource https://app.balldontlie.io/