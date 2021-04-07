from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=44af8d57d2ae36fea4714cab2cce068c'
    city = 'London'
    city_wheater = requests.get(url.format(city)).json()
    wheater = {
        'city': city,
        'temperature' : city_wheater['main']['temp'],
        'decsription' : city_wheater['weather'][0]['description'],
        'icon' : city_wheater['weather'][0]['icon']
    }
    context = {'wheater_data': wheater}
    return render(request, 'wheater/home.html')