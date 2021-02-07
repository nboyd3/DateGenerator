from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup
import requests, random


def rand_restaurants(city, state):
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

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        user_state = request.form['state']
        user_city = request.form['city']
        pick = rand_restaurants(user_city, user_state)
        if request.form.get("restaurants"):
            return render_template('index.html', pick = pick)
        else:
            return render_template('index.html', pick=pick)

    else:
        return render_template('index.html')

    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)