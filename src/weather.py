import requests
from random import randint
import src.config as conf


def weather_request(city):
    weather_response = requests.get(conf.weather_url.format(city, conf.weather_api_key)).json()

    weather = {}
    if weather_response['cod'] == 200:
        weather = {
            "city": weather_response['name'] + ", " + weather_response['sys']['country'],
            "temperature": round(weather_response['main']['temp']),
            "description": weather_response['weather'][0]['description'],
            "icon": weather_response['weather'][0]['icon'],
            "humidity": weather_response['main']['humidity'],
            "wind": weather_response['wind']['speed'],
        }
    else:
        weather = {
            "city": weather_response['message'],
            "temperature": 0,
            "description": 0,
            "icon": 0,
            "humidity": 0,
            "wind": 0
        }

    return weather


def unsplash_request(city):
    background_url = conf.background_url.format(city + " city")
    response = requests.get(background_url).json();

    result_count = len(response['results'])
    image_index = randint(0, result_count - 1)

    url_name = conf.url_name
    if response['results'][image_index]['alt_description'] is not None:
        image_url = response['results'][image_index]['urls']['raw']
        url_name = image_url
    return url_name
