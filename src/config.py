import os
from dotenv import load_dotenv

load_dotenv()

weather_api_key = os.getenv("WEATHER_API_KEY")
weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

background_url = 'https://unsplash.com/napi/search/photos?query={}&per_page=20&page=1&xp='
url_name = "https://images.unsplash.com/photo-1500964757637-c85e8a162699?ixid=MnwxMjA3fDB8MXxzZWFyY2h8Mnx8Q2xvdWRzJTIwbGFuZHNjYXBlfGVufDB8fHx8MTY1MTkyMzE5Mg&ixlib=rb-1.2.1"

initial_city = "Moscow"

currency_api_key = os.getenv("CURRENCY_API_KEY")
currency_url = 'https://currate.ru/api/?get=rates&pairs={}&key={}'

initial_currency = 'USDRUB,RUBUSD'

initial_currency_from = 'USD'
initial_currency_to = 'RUB'
