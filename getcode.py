from requests import get
from datetime import datetime as dt
from datetime import timedelta
from time import time

def get_code():
    start = time()
    date = dt.now()
    if date.hour >= 22:
        date += timedelta(days=1)
    data = get(f'https://www.cybersport.ru/tags/games/shifr-hamster-kombat-khomiak-na-{date.strftime("%d")}-avgusta').text
    end = time()
    print(f'Successfully get code from website in {round(end - start, 2)} sec.')
    cipher = data[data.find('2024 года: Слово ') + 17:data.find('2024 года: Слово ') + 22].replace('<', '').lower()
    if cipher == 'html':
        print('Cipher "html" is unlikely to be in the hamster. The site probably has not loaded the code yet and is getting a 404 error.')
    return cipher