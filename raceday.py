# script to find out if it is race day or not
from urllib.request import urlopen
from utils import getHtmlFromURL
from bs4 import BeautifulSoup
from datetime import date
from decouple import config
import requests

BOT_API_KEY = config('BOT_API_KEY')
CHANNEL_NAME = "@dagens_vader"

url = "https://www.autosport.com/f1/calendar"
html = getHtmlFromURL(url)

soup = BeautifulSoup(html, 'html.parser')
div = soup.find({"div"}, {"class": "leftColumn"})
table = div.find({"tbody"})
rows = table.findAll({"tr"})

race_dates = list(map(lambda row: row.findAll({"td"})[2].text, rows))

# get current date
today = date.today()
# format date to "day month" but keep month short (lowercase b)
today = today.strftime("%d %b")

if today in race_dates:
    requests.get(f'https://api.telegram.org/bot{BOT_API_KEY}/sendMessage',
                 params={'chat_id': CHANNEL_NAME,
                         'text': 'It is race day ' + u'\U0001F3C1' + u'\U0001F3CE'})
else:
    requests.get(f'https://api.telegram.org/bot{BOT_API_KEY}/sendMessage',
                 params={'chat_id': CHANNEL_NAME,
                         'text': 'It is not race day ' + u'\U0001F61E'})
