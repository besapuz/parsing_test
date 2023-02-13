import requests
import gspread
from bs4 import BeautifulSoup
from os import environ
from dotenv import load_dotenv
load_dotenv()

URL = environ['URL']
DOC = environ['DOC']
WEY = environ['WEY']
# Указываем путь к JSON
gc = gspread.service_account(filename=WEY)
#Открываем тестовую таблицу
sh = gc.open_by_url(DOC)

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('table')
head = soup.find_all('th')
tg = soup.find_all('td', class_='confluenceTd')
abc = 'ABCDEFG'
count = 2
count2 = 0
for h in head:
    text = h.text
    sh.sheet1.update(f'{abc[count2]}1', text)
    count2 += 1
for quote in tg:
    text = quote.text
    if text.isdigit():
        sh.sheet1.update(f'A{count}', text)
    else:
        sh.sheet1.update(f'B{count}', text)
        count += 1
