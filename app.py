from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup
import requests, random

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def list_restaurants(city = "Binghamton", state = "NY"):
    restaurants = []
    # requesting information on yelp depending on what city was inputed
    URL = 'https://www.yelp.com/search?find_desc=&find_loc=' + city + '%2C%20' + state
    page = requests.get(URL)
    # sorting html in page to just headings
    soup = BeautifulSoup(page.content, 'html.parser')
    rest_names = soup.find_all('a', class_='link__09f24__1MGLa link-color--inherit__09f24__3Cplm link-size--inherit__09f24__3Javq')
    # adding restaurant names into the restaurant list
    for rest_name in rest_names:
        for child in rest_name.descendants:
            restaurants.append(child)
    return restaurants[random.randint(0, len(restaurants) - 1)]

def index():
    # places you can go for the date
    outdoor = ["Go for a hike", "Throw a ball", "Skydiving would be fun", "Go on a bike ride", "Find a carnival", "Watch a concert", 
            "Watch an outdoor sporting event", "Stargaze until you see a shooting star", "Do a photoshoot", "Make a picnic",
            "Go horseback riding", "Take a hot air balloon ride", "Go fising", "Search for a bouquet of flowers", "Go roller blading"]
    indoor = ["Read a book at a bookstore", "Make a puzzle", "Go to a bowling alley", "Watch a movie", "Visit an arcade",
            "Visit an art gallery","Go thrift shopping", "Play a board game", "Take dance lessons", "Go for some wine tasting", 
            "Escape an escape room", ]


    if request.method == 'POST':
        # input values from web application
        state = request.form['state']
        city = request.form['city']
        activityChoices = []
        pick = ""
        if request.form.get("outdoor"):
            activityChoices.append("outdoor")
        if request.form.get("indoor"):
            activityChoices.append("indoor")
        if request.form.get("restaurant"):
            activityChoices.append("restaurant")
  
        # randomly choose an activity based on input
        activityNum = random.randint(0, len(activityChoices) - 1)

        if activityChoices[activityNum] == "outdoor":
            pick = outdoor[random.randint(0, len(outdoor) - 1)] + "!"
        if activityChoices[activityNum] == "indoor":
            pick = indoor[random.randint(0, len(indoor) - 1)] + "!"
        if activityChoices[activityNum] == "restaurant":
            pick = "Go to " + str(list_restaurants(city, state)) + "!"


        else:
            return render_template('index.html', pick=pick)


    else:
        return render_template('index.html')

    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)

