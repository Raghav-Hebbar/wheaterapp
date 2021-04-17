from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import City
from .forms import CityForm
#from .models import City

def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=44af8d57d2ae36fea4714cab2cce068c'

    error_msg = ''
    message = ''
    message_class = ''

    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name= new_city).count()   
            
            if existing_city_count == 0:
                city_wheater = requests.get(url.format(new_city)).json()

                if city_wheater['main'] != "":
                    form.save()
                else:
                    error_msg = 'City dose not exist'
            else:
                error_msg = 'City already exist'
            
        if error_msg:
            message = error_msg
            message_class = 'is-danger'
        else:
            message = 'City added successfully!'
            message_class = 'is-success'


    form = CityForm()
    cities = City.objects.all()
    weather_data = []

    for city in cities: 

        city_wheater = requests.get(url.format(city)).json()

        wheater = {
            'city': city,
            'temperature' : city_wheater['main']['temp'],
            'decsription' : city_wheater['weather'][0]['description'],
            'icon' : city_wheater['weather'][0]['icon'],
            'country_code' : city_wheater['sys']['country'],
            'humidity' : city_wheater['main']['humidity'],
            'wind' : city_wheater['wind']['speed'],
            'high': city_wheater['main']['temp_max'],
            'low' : city_wheater['main']['temp_min'],
        }
        weather_data.append(wheater)
         
    context = {'wheater_data': weather_data, 'form' : form}

    return render(request, 'wheater/main.html',context)