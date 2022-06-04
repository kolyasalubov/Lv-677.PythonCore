import telebot, pyowm
from telebot import types
temp = ''
bot = telebot.TeleBot('5501855817:AAHtdBw_t9dSDhvqdJhfKOd6m9HGCcO3xME')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.text + ' от ' + str(message.from_user.id))
    if message.text.lower() == '/start':
        bot.send_message(message.chat.id, 'Привет, чтобы продожить, напиши "Погода"')
    if message.text.lower() == 'погода':
        bot.send_message(message.chat.id, 'Введи свой город:')
        bot.register_next_step_handler(message, get_weather)
def get_weather(message):
    global temp
    g = message.text
    temp = g
    ow = pyowm.OWM('1b7bdc0ca37e946d115ebc0b50049921')
    try:
        mrg = ow.weather_manager()
        observation = mrg.weather_at_place(g)
        w = observation.weather
        temperature = w.temperature('celsius')['temp']
        weter = w.wind()['speed']
        gg = w.pressure['press']
        wete = w.wind()['deg']
        print(wete)
        davl = int(gg) - 11
        rtst = str(davl/1.333)
        direction = ''
        if int(wete) < 45:
            direction = 'Север'
        if int(wete) < 90:
            direction = 'Северо-восток'
        if int(wete) < 135:
            direction = 'Восток'
        if int(wete) < 180:
            direction = 'Юго-восток'
        if int(wete) < 225:
            direction = 'Юг'
        if int(wete) < 270:
            direction = 'Юго-запад'
        if int(wete) < 315:
            direction = 'Запад'
        if int(wete) < 360:
            direction = 'Северо-запад'
        print("В городе " + g + " сейчас " + str(temperature) + "°С")
        bot.send_message(message.chat.id, 'В городе ' + g + ' сейчас ' + str(temperature) + '°C')
        bot.send_message(message.chat.id, 'Скорость ветра: ' + str(weter) + 'м/с, направление: ' + direction)
        bot.send_message(message.chat.id, 'Давление: ' + str(rtst[:-14]) + ' мм.рт.ст')
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, 'Город не найден')
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    bot.send_message(message.chat.id, text='Еще раз?', reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Хорошо, введите город:')
        bot.register_next_step_handler(call.message, get_weather)
    elif call.data == "no":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'До встречи.')

bot.polling(none_stop=True)
