from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    dates = ["food", "dance", "hangout"]
    if request.method == 'POST':
        pick = random.choice(dates)
        user_state = request.form['state']
        user_city = request.form['city']
        restaurant = request.form.getlist('restaurant')
        if user_state == "NY" and request.form.get("outdoors"):
            
            return render_template('index.html', pick="Tullys")
        else:
            return render_template('index.html', pick=pick)


    else:
        return render_template('index.html')

    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)