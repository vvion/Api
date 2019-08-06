# pip install pytelegrambotapi
import telebot

Lip = telebot.TeleBot('900763584:AAF6suHEQd_EdyMI2IX322aMHzx8YRVellc')

# Декоратор для команд
@Lip.message_handler(commands=['start'])
def start_message(message):
    Lip.send_message(message.chat.id, 'Эй.. ты написал мне /start ???')

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
    print(message)
    file_id = 'CAADAgADqgYAAtJaiAFIBau3svuQYRYE'
    Lip.send_sticker(message.chat.id, file_id)

    # Грут  -    'CAADAgADqgYAAtJaiAFIBau3svuQYRYE'
    # Собутыльник -    'CAADAgAD5QUAApb6EgUi6l1Id92lkhYE'

# Чтоб не выключался, а работал и проверял нет ли нового сообщения
Lip.polling()
