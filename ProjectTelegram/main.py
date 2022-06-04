import telebot
from telebot import types

bot = telebot.TeleBot('5501855817:AAHtdBw_t9dSDhvqdJhfKOd6m9HGCcO3xME')

@bot.message_handler(commands=['start'])

def start(message):
    greeting = f'Привет, <b>{message.from_user.first_name}</b>!'
    bot.send_message(message.chat.id, greeting, parse_mode = 'html')

# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == 'hello':
#         bot.send_message(message.chat.id, 'И тебе привет', parse_mode = 'html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f'Your id: {message.from_user.id}', parse_mode = 'html')
#     elif message.text == 'photo':
#         photo = open('d:\PythonCore\HW\Lv-677.PythonCore\ProjectTelegram\photo1.png', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, f'Я тебя не понимаю(', parse_mode = 'html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Классная фотка, но мне нужно название города!', parse_mode = 'html')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить сайт источника', url='https://www.gismeteo.ua/'))
    bot.send_message(message.chat.id, 'Переход на сайт', reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup()
    website = types.KeyboardButton('/website')
    start = types.KeyboardButton('/start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Выберите команду', reply_markup=markup)



bot.polling(none_stop = True)