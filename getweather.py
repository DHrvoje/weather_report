from pyowm import OWM
import os

OWM_API_KEY = OWM(os.getenv('OWM_API_KEY'))
#b059459a0cb5701c10840e26dc30994a

mngr = OWM_API_KEY.weather_manager()
OWM_CITY = os.getenv('OWM_CITY')
cty = mngr.weather_at_place(OWM_CITY)
w = cty.weather
temp = w.temperature('celsius')

print("City: ", OWM_CITY)
print("Desciption: ", w.detailed_status)
print("Temp: ", temp['temp'], "°C")
print("Humidity: ", w.humidity, "%")
