import telebot
from telebot import types

#присваивание боту токена(ключ доступа)
bot = telebot.TeleBot('5792412888:AAGkJlt4chkfFYPTfK8tOPVg4uUyts6RQUA')

#набор команд, которые бот выполняет
@bot.message_handler(commands=['start'])

#описание самой команды
def start(message):
    # формирование своего сообщения с именем и фамилеей пользователя
    # f для форматированного текста
    # все происходит через методы переменной message
    mess = f'Hello, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

# вывод написанного пользователем в чат
# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == "hello":
#         bot.send_message(message.chat.id, "And you hello", parse_mode='html')
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f"Your ID: {message.from_user.id}", parse_mode='html')
#     elif message.text == "photo":
#         photo = open("fon5.jpeg", 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, "I do not understand you", parse_mode="html" )
#

#обработка документов
@bot.message_handler(content_types=['photo'])
def get_user_phot(message):
    bot.send_message(message.chat.id, "Wow, excellent photo", parse_mode='html')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Visit site', url="https://vk.com"))
    bot.send_message(message.chat.id, "Go to site", reply_markup=markup)

@bot.message_handler(commands=['help'])
def buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    website = types.KeyboardButton('/website')
    start = types.KeyboardButton('/start')
    markup.add(website, start)
    bot.send_message(message.chat.id,'Help bar', reply_markup=markup)

#вызов бота на постоянной основе
bot.polling(none_stop=True)