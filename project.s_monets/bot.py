import telebot
from telebot import types
from currency_api import get_exchange_rates, exchange_rates_str

BOT_API_TOKEN = '5302469056:AAG67EtsPh31XIk7ilJDV-yBF31rMqqfBkQ'
CURRENCY_API_TOKEN = 'c33e4b5f488712aace7f4274'
bot = telebot.TeleBot(BOT_API_TOKEN)

def add_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Гривня")
    item2 = types.KeyboardButton("Долар")
    item3 = types.KeyboardButton("Eвро")
    item4 = types.KeyboardButton("Злотий")
    item5 = types.KeyboardButton("Фунт")
    item6 = types.KeyboardButton("Ліра")
    markup.add(item1,item2,item3,item4,item5,item6)
    return markup


def add_markup2():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("10")
    item2 = types.KeyboardButton("100")
    item3 = types.KeyboardButton("1000")
    item4 = types.KeyboardButton("Назад")
    markup.add(item1,item2,item3,item4)
    return markup
    

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        f"Привіт {message.from_user.username}, я бот який допоможе тобі дізнатися курс валют.\nДля початку вибери свою валюту: ",
        reply_markup = add_markup())

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == "Гривня":
        curr = "UAH"
        msg = bot.send_message(message.chat.id, exchange_rates_str(get_exchange_rates(curr, CURRENCY_API_TOKEN)),parse_mode="html", reply_markup=add_markup2())
        bot.register_next_step_handler(msg, amount_func, curr)
    elif message.text == "Долар":
        curr = "USD"
        msg = bot.send_message(message.chat.id, exchange_rates_str(get_exchange_rates(curr, CURRENCY_API_TOKEN)),parse_mode="html", reply_markup=add_markup2())
        bot.register_next_step_handler(msg, amount_func, curr)
    elif message.text == "Eвро":
        curr = "EUR"
        msg = bot.send_message(message.chat.id, exchange_rates_str(get_exchange_rates(curr, CURRENCY_API_TOKEN)),parse_mode="html", reply_markup=add_markup2())
        bot.register_next_step_handler(msg, amount_func, curr)
    elif message.text == "Злотий":
        curr = "PLN"
        msg = bot.send_message(message.chat.id, exchange_rates_str(get_exchange_rates(curr, CURRENCY_API_TOKEN)),parse_mode="html", reply_markup=add_markup2())
        bot.register_next_step_handler(msg, amount_func, curr)
    elif message.text == "Фунт":
        curr = "GBP"
        msg = bot.send_message(message.chat.id, exchange_rates_str(get_exchange_rates(curr, CURRENCY_API_TOKEN)),parse_mode="html", reply_markup=add_markup2())
        bot.register_next_step_handler(msg, amount_func, curr)
    elif message.text == "Ліра":
        curr = "TRY"
        msg = bot.send_message(message.chat.id, exchange_rates_str(get_exchange_rates(curr, CURRENCY_API_TOKEN)),parse_mode="html", reply_markup=add_markup2())
        bot.register_next_step_handler(msg, amount_func, curr)
    else:
        try:
            curr = message.text.upper()
            msg = bot.send_message(message.chat.id, exchange_rates_str(get_exchange_rates(message.text.upper(), CURRENCY_API_TOKEN)),parse_mode="html")
            bot.register_next_step_handler(msg, amount_func, curr)
        except:
            bot.send_message(message.chat.id, "Ви ввели неправильну валюту.\nВиберіть зі списку або введіть самі у міжнародному форматі!")
    
def amount_func(message, curr):
    if message.text == "10":
        msg = bot.send_message(message.chat.id, exchange_rates_str(get_exchange_rates(curr, CURRENCY_API_TOKEN), 10),parse_mode="html",reply_markup=add_markup())
        bot.register_next_step_handler(msg, bot_message)
    elif message.text == "100":
        msg = bot.send_message(message.chat.id, exchange_rates_str(get_exchange_rates(curr, CURRENCY_API_TOKEN), 100),parse_mode="html",reply_markup=add_markup())
        bot.register_next_step_handler(msg, bot_message)
    elif message.text == "1000":
        msg = bot.send_message(message.chat.id, exchange_rates_str(get_exchange_rates(curr, CURRENCY_API_TOKEN), 1000),parse_mode="html",reply_markup=add_markup())
        bot.register_next_step_handler(msg, bot_message)
    elif message.text == "Назад":
        msg = bot.send_message(
        message.chat.id,
        f"Привіт {message.from_user.username}, я бот який допоможе тобі дізнатися курс валют.\nДля початку вибери свою валюту: ",
        reply_markup = add_markup())
    else:
        try:
            msg = bot.send_message(message.chat.id, f"<b>СУМА: {int(message.text)}</b>\n" + exchange_rates_str(get_exchange_rates("UAH", CURRENCY_API_TOKEN), int(message.text)),parse_mode="html",reply_markup=add_markup())
            bot.register_next_step_handler(msg, bot_message)
        except:
            msg = bot.send_message(message.chat.id, f"Помилкове введення!!!",parse_mode="html",reply_markup=add_markup())
            bot.register_next_step_handler(msg, bot_message)

bot.enable_save_next_step_handlers()
bot.load_next_step_handlers()
bot.infinity_polling()