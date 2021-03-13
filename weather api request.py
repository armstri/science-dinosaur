import requests
import pprint
import json

def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None

def img

token = '69cf50fcf9543da6d2076f7e50027566'

zipcode = '02115'

api_address = 'http://api.openweathermap.org/data/2.5/weather?zip=' + zipcode + '&units=imperial&appid=' + token

print (api_address)

json_data = requests.get(api_address).json()

weather = json_data['weather'][0]
temp = json_data['main']

pp_json (temp)
