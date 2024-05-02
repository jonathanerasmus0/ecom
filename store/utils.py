import requests
import json

def get_weather(city):
    api_key = '533ac5d37a4fe7dc36dd522b6188abcf'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={'Berlin'},{'DE'}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

