from pyowm import OWM

OWM_API_KEY = OWM('b059459a0cb5701c10840e26dc30994a')
mngr = OWM_API_KEY.weather_manager()
OWM_CITY = 'Zagreb'
cty = mngr.weather_at_place(OWM_CITY)
w = cty.weather
temp = w.temperature('celsius')

print("City: ", OWM_CITY)
print("Description: ", w.detailed_status)
print("temp = ", temp['temp'], "°C")
print("Humidity: ", w.humidity, "%")