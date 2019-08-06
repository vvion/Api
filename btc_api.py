# pip install requests
import requests

def btc_search():
    # API запрос биткоина
    url_btc = 'https://kuna.io/api/v2/tickers/btcuah'
    btc_reply = requests.get(url_btc)
    if btc_reply.status_code == 200:
        print('Btc загружен')
    # Сохранение ответа
    btc_dict = btc_reply.json()
    # Обработка     Нужные данные в словаре "ticker"
    dictionary = []
    dictionary = btc_dict['ticker']
    price = int(float(dictionary['buy']))

    # Запись в файл
    filename = 'price.txt'
    with open(filename, 'w') as file_object:
        file_object.write(str(price))
    print('Файл "price.txt" создан')

def exchange_rate():
    # API запрос курса гривны
    url_ua = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    ua_reply = requests.get(url_ua)
    if ua_reply.status_code == 200:
        print('Курс валют загружен')
    # Сохранение 
    ua_dict = ua_reply.json()
    # Обработка     копирую курс к рублю, создание переменной rate
    c = []
    for txt in ua_dict:
        if txt['txt'] == 'Російський рубль':
            c = txt
    rate = float(c['rate'])

    # Запись в файл
    filename = 'rate.txt'
    with open(filename, 'w') as file_object:
        file_object.write(str(rate))
    print('Файл "race.txt" создан')

def combine():
    # Получает значения из текстовых файлов и перемножает
    file_1 = 'price.txt'
    with open(file_1) as file_object:
        price = int(file_object.read())

    file_2 = 'rate.txt'
    with open(file_2) as file_object:
        rate = float(file_object.read())

    result = int(price * rate)
    print(result)
    # Запись в файл
    filename = 'result.txt'
    with open(filename, 'w') as file_object:
        file_object.write(str(result))
    print('Файл "result.txt" создан')

btc_search()
exchange_rate()
combine()
