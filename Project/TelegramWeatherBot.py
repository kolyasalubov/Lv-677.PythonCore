import telebot
from pyowm import OWM

bot = telebot.TeleBot("5002151214:AAE9mmww21SpxwGqkvONTPQQT0bImKUdQS8")
owm = OWM('2340dee8770f9ce094ff9d3eb2fb68e7')


@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id,
		f"Welcome, {message.from_user.first_name}\n"
		f"/start - will start the bot\n"
		f"To check the weather forecast put your city.")


@bot.message_handler(content_types=['text'])
def test(message):
	try:
		place = message.text


		mgr = owm.weather_manager()
		observation = mgr.weather_at_place(place)
		w = observation.weather

		temperature = w.temperature("celsius")
		temperature_real = temperature['temp']
		temperature_feels_like = temperature['feels_like']
		temperature_maximum = temperature['temp_max']
		temperature_minimum = temperature['temp_min']

		wind = w.wind()['speed']
		humidity = w.humidity
		pressure = w.pressure['press']

		bot.send_message(message.chat.id,
						f"In {place} the temperature is "
						f"{temperature_real} °C\n"
						f"Maximum tepmerature is {temperature_maximum} °C\n"
						f"Minumum temperature is {temperature_minimum} °C\n"
						f"It feels like {temperature_feels_like} °C\n"
						f"The speed of wind is {wind} m/s\n"
						f"The humidity is {humidity} %\n"
						f"The pressure is {pressure} mm Hg\n")

	except:
		bot.send_message(message.chat.id, "Такой город не найден!")
		print(str(message.text), "- не найден")

bot.polling(none_stop=True)
