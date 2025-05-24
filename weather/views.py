import requests, os

from django.shortcuts import render
from dotenv import load_dotenv

def show_weather(request):
    weather_data = None
    if request.method == 'POST':
        weather_api_key = os.getenv('weather_api_key')
        city = request.POST.get('city')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&appid={weather_api_key}'
        
        response = requests.get(url)
        if response.status_code == 404:
            weather_data = {
                'result': False,
                'city': city
            }
        else:
            response = response.json()
            weather_data = {
                'result': True,
                'city': response['name'],
                'temp': response['main']['temp'],
                'temp_feels_like': response['main']['temp'],
                'description': response['weather'][0]['description'],
                'humidity': response['main']['humidity'],
            }
    return render(request, 'weather/index.html', {'weather_data': weather_data})


def custom_404_page(request, exception):
    return render(request, 'weather/404.html')