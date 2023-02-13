from os import environ

import gspread
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from table import Table

load_dotenv()

URL = environ['URL']
DOC = environ['DOC']
WEY = environ['WEY']
# Указываем путь к JSON
gs = gspread.service_account(filename=WEY)
# Открываем тестовую таблицу
go = gs.open_by_url(DOC)

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('table')
head = soup.find_all('th')
td = soup.find_all('td', class_='confluenceTd')

table = Table(gs, head, go)

table.update_head()
table.update_values()
