from flask import Flask, render_template, request
import src.config as conf
import src.weather as weather
import src.currency as currency

# def weather_request(city):
#     weather_response = requests.get(conf.weather_url.format(city, conf.weather_api_key)).json()
#
#     weather = {}
#     if weather_response['cod'] == 200:
#         weather = {
#             "city": weather_response['name'] + ", " + weather_response['sys']['country'],
#             "temperature": round(weather_response['main']['temp']),
#             "description": weather_response['weather'][0]['description'],
#             "icon": weather_response['weather'][0]['icon'],
#             "humidity": weather_response['main']['humidity'],
#             "wind": weather_response['wind']['speed'],
#         }
#     else:
#         weather = {
#             "city": weather_response['message'],
#             "temperature": 0,
#             "description": 0,
#             "icon": 0,
#             "humidity": 0,
#             "wind": 0
#         }
#
#     return weather
#
#
# def unsplash_request(city):
#     background_url = conf.background_url.format(city + " city")
#     response = requests.get(background_url).json();
#
#     result_count = len(response['results'])
#     image_index = randint(0, result_count - 1)
#
#     url_name = conf.url_name
#     if response['results'][image_index]['alt_description'] is not None:
#         image_url = response['results'][image_index]['urls']['raw']
#         url_name = image_url
#     return url_name


# def currency_request(frm, t):
#     frm = frm.upper()
#     t = t.upper()
#     currency_response = requests.get(conf.currency_url.format(frm + t + ',' + t + frm, conf.currency_api_key)).json()
#     currency = {}
#     if currency_response['status'] == 200:
#         currency = {
#             "from": frm,
#             "to": t,
#             "from_to": currency_response['data'][frm + t],
#             "to_from": currency_response['data'][t + frm]
#         }
#     else:
#         currency = {
#             "from": frm,
#             "to": t,
#             "from_to": currency_response['message'],
#             "to_from": currency_response['message']
#         }
#
#     return currency


weather_re = weather.weather_request(conf.initial_city)
background_re = weather.unsplash_request(conf.initial_city)
currency_re = currency.currency_request(conf.initial_currency_from, conf.initial_currency_to)

app = Flask(__name__, static_folder="static")


@app.route('/', methods=['GET', 'POST'])
def index():
    global weather_re
    global background_re
    global currency_re

    if request.method == 'POST':
        city = request.form.get('city')
        if city is not None:
            new_weather = weather.weather_request(city)
            new_background = weather.unsplash_request(city)
            weather_re = new_weather
            background_re = new_background

        cur = request.form.get('from')
        if cur is not None and ' ' in cur and len(cur) <= 7:
            cur = cur.upper()
            new_currency = currency.currency_request(*cur.split(' '))
            currency_re = new_currency

    return render_template('weather.html', weather=weather_re, url=background_re, curr=currency_re)


app.run()
