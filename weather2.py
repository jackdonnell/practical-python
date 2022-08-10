import requests

api_key = '1c2162d3393558214747ece25ff4d6ab'
city = 'Bangkok'
url = 'https://api.openweathermap.org/data/2.5/weather?lat={13.7563}&lon={l100.5018}&appid=' + api_key + '&units=imperial'

req = requests.get(url)
json = requests.json()
print(json)

description = json.get('weather')[0].get('description')
print("today's forecast is", description)
temp_min = json.get('main').get('temp_min')
print('the minimum temp is ', temp_min)
temp_max = json.get('main').get('temp_max')
print('the maximum temp is ', temp_max)