import requests
import json


# Getting genres
a = requests.get(url="http://127.0.0.1:5000/genres")
a = json.loads(a.text)

for i in a["Genres"]:
    print(i)


# Getting movies in a particular genre
a = requests.get(url="http://127.0.0.1:5000/movies?genre=comedy&limit=50")
a = json.loads(a.text)

for i in a["Movies"]:
    print(i["Title"])


# Sending rated movies for recommendations
head = {"Content-Type" : "application/json"}
data = {"12" : 2, "15" : 3, "12" : 4}

a = requests.post(url="http://127.0.0.1:5000/recommend", json=data)
a = json.loads(a.text)

for i in a["Recommendations"]:
    print("ID: " + str(i["ID"]))
    print("Title: " + i["Title"])
    print("Year: " + i["Year"])
    print("Genres: ")
    for j in i["Genres"]:
        print("\t" + j)
    print("\n")
