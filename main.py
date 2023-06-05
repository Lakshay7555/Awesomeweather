import requests
import os
from flask import Flask, render_template, request

API_KEY = os.environ["API_KEY"]
BASE_URL= "https://api.openweathermap.org/data/2.5/"


app = Flask(__name__, static_url_path='', static_folder='web/static', template_folder='web/templates')


@app.route('/')
def homepage():
    return render_template('index.html', gathercity='abc')

@app.route('/current',methods=["POST"])
def current():
    cityy_name = request.form.get('city_name')
    try:
        r = requests.get(f"{BASE_URL}weather?q={cityy_name}&appid={API_KEY}&units=metric")
        r.raise_for_status()
        data = r.json()

        f = requests.get(f"{BASE_URL}forecast?q={cityy_name}&appid={API_KEY}&units=metric")
        f.raise_for_status()
        data2 = f.json()

        current_weather = {
            'description': data['weather'][0]['description'].title(),
            'icon': data['weather'][0]['icon'],
            'name': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'wind': data['wind']['speed']
        }

        forecast_weather = {

        }

        return render_template('index.html', weather=current_weather)
    except requests.exceptions.HTTPError as err:
        return f'Error: {err}'


@app.route('/forecast')
def forecast():
    cityy_name = 'edmonton'
    f = requests.get(f"{BASE_URL}forecast?q={cityy_name}&appid={API_KEY}&units=metric")
    return f.json()
