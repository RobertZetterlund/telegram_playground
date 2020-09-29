# BLOG POST: https://blog.seamlesscloud.io/2020/09/be-prepared-for-bad-weather-using-20-lines-of-python/
from decouple import config
import requests

WEATHER_API_KEY = config('WEATHER_API_KEY')
LATITUDE = config('LATITUDE')
LONGITUDE = config('LONGITUDE')
BOT_API_KEY = config('BOT_API_KEY')
CHANNEL_NAME = "@dagens_vader"

if __name__ == '__main__':
    resp = requests.get(
        f"https://api.openweathermap.org/data/2.5/onecall?lat={LATITUDE}&lon={LONGITUDE}&appid={WEATHER_API_KEY}")
    forecast = resp.json()['daily'][0]
    today_weather = forecast['weather'][0]['main']
    if 'Rain' == today_weather:
        requests.get(f'https://api.telegram.org/bot{BOT_API_KEY}/sendMessage',
                     params={'chat_id': CHANNEL_NAME,
                             'text': 'It\'s going to rain today' + u'\U00002614' + ', take your umbrella with you!'})