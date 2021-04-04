from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=44af8d57d2ae36fea4714cab2cce068c'
    city = 'London'
    city_wheater = requests.get(url.format(city))
    print(city_wheater.text)
    return render(request, 'wheater/home.html')