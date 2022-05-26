from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('1b7bdc0ca37e946d115ebc0b50049921')
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
name_place = input('Введите населенный пункт: ')
observation = mgr.weather_at_place(name_place)
w = observation.weather

w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75
print(f"{name_place}: \nВлажность: {w.humidity}\nМакс температура: { w.temperature('celsius')['temp_max'] }\nМин температура: { w.temperature('celsius')['temp_min'] } ")
