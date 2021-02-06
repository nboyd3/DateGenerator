# date choices are either pre generated ideas or scraped from yelp 
import requests
from bs4 import BeautifulSoup

URL = 'https://www.yelp.com/search?find_desc=&find_loc=Binghamton%2C%20NY'
page = requests.get(URL)
print(page.content)


outdoor = ["Go for a hike", "Throw a ball", "Skydiving would be fun", "Go on a bike ride", "Find a carnival", "Watch a concert", 
            "Watch an outdoor sporting event", "Stargaze until you see a shooting star", "Do a photoshoot"]
indoor = ["Read a book at a bookstore", "Make a puzzle", "Go to a bowling alley", "Watch a movie", "Play in an arcade",
            "Visit an art gallery","Go thrift shopping"]
restaurant = []
