# pip install  - pytelegrambotapi   - requests

import telebot
import requests

"""API запрос"""
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
    return str(price)

# Инициализация бота
Lip = telebot.TeleBot('900763584:AAF6suHEQd_EdyMI2IX322aMHzx8YRVellc')

# Команда /start
@Lip.message_handler(commands=['start'])
def start_message(message):
    Lip.send_message(message.chat.id, 'Эй.. ты написал мне /start ???')

# Команда /btc
@Lip.message_handler(commands=['btc'])
def btc_message(message):
    Lip.send_message(message.chat.id, 'Поиск цены биткоина...')
    Lip.send_message(message.chat.id, '1 биткоин = ' + btc_search() + ' грн')


# Декоратор сообщений
@Lip.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        Lip.send_message(message.chat.id, 'Да, создатель')
    elif message.text.lower() == 'пока':
        Lip.send_message(message.chat.id, 'Пока, создатель')

# Декоратор стикеров (отправляет 1 стикер) 
@Lip.message_handler(content_types=['sticker'])
def send_sticker(message):
    #print(message.sticker) Вывод id стикера
    file_id = 'CAADAgADqgYAAtJaiAFIBau3svuQYRYE'
    Lip.send_sticker(message.chat.id, file_id)

    # Грут  -    'CAADAgADqgYAAtJaiAFIBau3svuQYRYE'
    # Собутыльник -    'CAADAgAD5QUAApb6EgUi6l1Id92lkhYE'
Lip.polling()
