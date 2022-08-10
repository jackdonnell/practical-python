import requests
people = requests.get('http://api.opennotify.org/astros.json')
json = people.json

print(json)

print('the people currently in space are:')
for i in json['people']:
    print(i['name'])
    