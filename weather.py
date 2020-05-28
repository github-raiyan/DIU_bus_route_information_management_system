#!/usr/bin/python3.6
import requests

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
city = "Dhaka"
url = api_address + city
icon=""
temp=0
humidity=""
main=""
def get_update():
    try:
        global icon
        global temp
        global humidity
        global main
        json_data = requests.get(url).json()
        icon = json_data['weather'][0]['icon']
        temp=json_data['main']['temp']
        humidity=json_data['main']['humidity']
        #print(json_data)
        main=json_data['weather'][0]['main']
        return True
    except:
        print("you are offline")
        return False
