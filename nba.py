from flask import Flask, render_template
import requests
import json


def get_nba():
    url = "https://www.balldontlie.io/api/v1/players"

    # headers = {
    #     "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
    #     "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    # }
    n = 1

    params = {
        "page": 1,
        "per_page": 5,
        "search": "paul"
    }

    with open("search.txt", "w") as file:
        while True:
            response = requests.get(url, params=params)
            
            try:
                data = response.json()
                if (not data) or (not data.get("data")):
                    break
                else:
                    json.dump(data, file)
                    file.write("\n")
                    print(f"dodana strona {n}")
            
            except json.JSONDecodeError:
                print("zly format")
                break

            n+=1
            params["page"] = n

    return None        

    # num_players = 0
    # for player in data["data"]:
    #     print(player)
    #     num_players += 1   

    # return num_players


def licz_zawodnikow():
    with open("data.txt", "r") as file:
        zawodnicy = []
        for line in file:
            try:
                zawodnik = json.loads(line.strip())
                zawodnicy.append(zawodnik)
            except json.JSONDecodeError:
                print("zly format")

    return zawodnicy

print(get_nba())

#zawodnicy = licz_zawodnikow()


# for line in zawodnicy:
#     for zawodnik in line["data"]:
#         if (zawodnik["first_name"] == "LeBron") and (zawodnik["last_name"] == "James"):
#             print(zawodnik)





