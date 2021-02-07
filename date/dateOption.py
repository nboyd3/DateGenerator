# date choices are either pre generated ideas or scraped from yelp 
import requests, random
from bs4 import BeautifulSoup

def list_restaurants(city, state):
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

def main():
    # input values from web application
    city = 'Binghamton'
    state = 'NY'
    activityChoices = ["outdoor", "indoor", "restaurant"]

    # places you can go for the date
    outdoor = ["Go for a hike", "Throw a ball", "Skydiving would be fun", "Go on a bike ride", "Find a carnival", "Watch a concert", 
            "Watch an outdoor sporting event", "Stargaze until you see a shooting star", "Do a photoshoot", "Make a picnic",
            "Go horseback riding", "Take a hot air balloon ride", "Go fising", "Search for a bouquet of flowers", "Go roller blading"]
    indoor = ["Read a book at a bookstore", "Make a puzzle", "Go to a bowling alley", "Watch a movie", "Visit an arcade",
            "Visit an art gallery","Go thrift shopping", "Play a board game", "Take dance lessons", "Go for some wine tasting", 
            "Escape an escape room", ]

    # randomly choose an activity based on input
    activityNum = random.randint(0, len(activityChoices) - 1)

    if activityChoices[activityNum] == "outdoor":
        print(outdoor[random.randint(0, len(outdoor) - 1)] + "!")
    if activityChoices[activityNum] == "indoor":
        print(indoor[random.randint(0, len(indoor) - 1)] + "!")
    if activityChoices[activityNum] == "restaurant":
        print("Go to " + str(list_restaurants(city, state)) + "!")
main()