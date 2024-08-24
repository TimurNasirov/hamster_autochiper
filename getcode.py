from requests import get
from datetime import datetime as dt
from datetime import timedelta
from time import time
from config import GETCODE_WEBSITE, GETCODE_SHOW_WARNINGS

def get_code():
    start = time()
    date = dt.now()
    if date.hour >= 22:
        date += timedelta(days=1)
    if GETCODE_WEBSITE == 1:
        data = get(f'https://www.cybersport.ru/tags/games/shifr-hamster-kombat-khomiak-na-{date.strftime("%d")}-avgusta').text
        end = time()
        print(f'Successfully get code from website in {round(end - start, 2)} sec.')
        cipher = data[data.find('2024 года: Слово ') + 17:data.find('2024 года: Слово ') + 22].replace('<', '').lower()
        if cipher == 'html' and GETCODE_SHOW_WARNINGS:
            print('Website №1: Cipher "html" is unlikely to be in the hamster. The site probably has not loaded the code yet and is getting a 404 error.')
        return cipher
    elif GETCODE_WEBSITE == 2:
        if date.hour >= 22 and GETCODE_SHOW_WARNINGS:
            print('Website №2: Code may be from yesterday')
        data = get('https://moneymail.ru/shifr-homyak/shifr-homyak-segodnya/').text
        end = time()
        print(f'Successfully get code from website in {round(end - start, 2)} sec.')
        cipher = data[data.find('<strong>это слово "') + 19:data.find('"</strong>.')].lower()
        return cipher