import requests
import os
from flask import Flask

API_KEY = os.environ["API_KEY"]
BASE_URL= "https://api.openweathermap.org/data/2.5/"


app = Flask(__name__, static_url_path='', static_folder='web/static', template_folder='web/templates')


@app.route('/')
def homepage():
    return "hello"
