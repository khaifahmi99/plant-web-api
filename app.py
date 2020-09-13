from flask import Flask, render_template, url_for, redirect, request
from flask_cors import CORS
import json
import random

import requests

app = Flask(__name__)
CORS(app)

API_KEY = 'brmvB5hePGk4WUVN4aecYf69-9XsWnLgPHjkBjEIgfg'

@app.route('/')
def home():
    page = random.randint(1,1000)
    url = f'https://trefle.io/api/v1/plants?token={API_KEY}&page={page}'
    response = requests.get(url).text
    response = json.loads(response)['data']

    return render_template('home.html', data=response)

@app.route('/plant/<id>')
def plant(id):
    url = f'https://trefle.io/api/v1/plants/{id}?token={API_KEY}'
    response = requests.get(url).text
    response = json.loads(response)['data']
    return render_template('plant.html', data=response)

@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        keyword = request.form.get('keyword')

        url = f'https://trefle.io/api/v1/plants/search?token={API_KEY}&q={keyword}'
        response = requests.get(url).text
        response = json.loads(response)['data']

        return render_template('search.html', keyword=keyword, data=response)
    return render_template('search.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')