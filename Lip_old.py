# pip install pytelegrambotapi
import telebot
import btc_api

Lip = telebot.TeleBot('900763584:AAF6suHEQd_EdyMI2IX322aMHzx8YRVellc')

# Декоратор для команд
@Lip.message_handler(commands=['start'])
def start_message(message):
    Lip.send_message(message.chat.id, 'Эй.. ты написал мне /start ???')

# Декоратор для команд
@Lip.message_handler(commands=['btc'])
def btc_message(message):
    Lip.send_message(message.chat.id, 'Поиск цены биткоина...')
    btc_api.btc_search()
    btc_api.exchange_rate()
    btc_api.combine()
    # Открыть файл result.txt и выдать ответ в телеге
    with open('result.txt') as file_object:
        result = int(file_object.read())
    Lip.send_message(message.chat.id, '1 биткоин = ' + str(result) + ' грн')


# Декоратор для сообщений
@Lip.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        Lip.send_message(message.chat.id, 'Да, создатель')
    elif message.text.lower() == 'пока':
        Lip.send_message(message.chat.id, 'Пока, создатель')

# Декоратор для стикеров (отправляет 1 стикер) 
        # Надо поменять чтоб был просто модуль а стикер выбирался в другом месте
@Lip.message_handler(content_types=['sticker'])
def send_sticker(message):
    print(message.sticker)
    file_id = 'CAADAgADqgYAAtJaiAFIBau3svuQYRYE'
    #file_id = message.text['file_id']
    Lip.send_sticker(message.chat.id, file_id)

    # Грут  -    'CAADAgADqgYAAtJaiAFIBau3svuQYRYE'
    # Собутыльник -    'CAADAgAD5QUAApb6EgUi6l1Id92lkhYE'

# Чтоб не выключался, а работал и проверял нет ли нового сообщения
Lip.polling()
