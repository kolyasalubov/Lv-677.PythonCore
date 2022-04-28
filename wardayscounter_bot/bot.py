
from datetime import date
from math import floor
import telebot
from configuration import TOKEN

bot = telebot.TeleBot(TOKEN)


begin_date = date(2022,2,24)
today = date.today()
quantity_of_seconds = (today - begin_date).total_seconds()
quantity_of_days = floor(quantity_of_seconds/86400) + 1 

def keyboard():

    button_day = telebot.types.KeyboardButton("Which day of a russian - Ukrainian war is today?")
    button_put = telebot.types.KeyboardButton("Have Putin died?")
    keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard = True,resize_keyboard  = True)
    keyboard.add(button_day, button_put)
    return keyboard

@bot.message_handler(commands=['start'])
def greeting_message(message):
    bot.send_message(
        message.chat.id,
        f"Glory to Ukraine! {quantity_of_days}",
        reply_markup = keyboard())

@bot.message_handler(commands=['help'])
def greeting_message(message):
    bot.send_message(
        message.chat.id,
        "I`m a bot, which helps you find out which day of war is today.\
            Press the button and see the result!", 
        reply_markup = keyboard())


@bot.message_handler(func = lambda m: True)
def bot_message(message):

        if message.text == "Which day of a russian - Ukrainian war is today?":
            bot.send_message(
                message.chat.id,
                f"Today is {quantity_of_days} day of war.")

        elif message.text == "Have Putin died?":
            bot.send_message(
                message.chat.id,
                f"Unfortanately, not yet. But today is {quantity_of_days} day since the beginning of this process.")
        

bot.infinity_polling()