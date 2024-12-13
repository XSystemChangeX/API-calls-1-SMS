import urllib.request
import json


#Function to get the weather for city
def get_weather(city):
  api='953156af1d8912580a0dc0e5c43c3fe3'

#URL with the city name and API key
  url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'
 

# request to the weather API
  request= urllib.request.urlopen(url)
  result = json.loads(request.read())

#temperature converted it to Celsius

  temp_c =round(result['main']['temp']-273.15,2)
#temperature in Celsius
  return temp_c