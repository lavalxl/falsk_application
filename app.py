from flask import Flask, render_template, request
import src.config as conf
import src.weather as weather
import src.currency as currency

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
