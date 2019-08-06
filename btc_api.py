# pip install requests
# Цена - думал что была в рублях, * на курс грн-руб 
import requests

def btc_search():
    # API запрос цены биткоина
    url_btc = 'https://kuna.io/api/v2/tickers/btcuah'
    btc_reply = requests.get(url_btc)
    #if btc_reply.status_code == 200:
    #    print('Btc загружен')
    # Сохранение ответа
    btc_dict = btc_reply.json()
    # Обработка     Нужные данные в словаре "ticker"
    dictionary = []
    dictionary = btc_dict['ticker']
    price = int(float(dictionary['buy']))
    return price

def exchange_rate():
    # API запрос курса гривны
    url_ua = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    ua_reply = requests.get(url_ua)
    #if ua_reply.status_code == 200:
    #    print('Курс валют загружен')
    # Сохранение 
    ua_dict = ua_reply.json()
    # Обработка     копирую курс к рублю, создание переменной rate
    c = []
    for txt in ua_dict:
        if txt['txt'] == 'Російський рубль':
            c = txt
    rate = float(c['rate'])
    return rate

def combine():
    result = int(btc_search() * exchange_rate())
    #print('Result получен')
    return result
#btc_search()
#exchange_rate()
#combine()
