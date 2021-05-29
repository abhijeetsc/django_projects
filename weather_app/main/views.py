from django.http.response import HttpResponse
from django.shortcuts import render
import requests
import json

api_key = 'YOUR-API-KEY-HERE'


def index(request):
    data = {'success': 1}
    if request.method == 'POST':
        city = request.POST['city']

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url).text
        response = json.loads(response)
        print(response)
        if response['cod'] and (response['cod'] == '400' or response['cod'] == '404'):
            data['success'] = 0
            data['message'] = 'Please enter correct city.'
        else:

            data["country_code"] = str(
                response['name']) + ', ' + str(response['sys']['country'])
            data["coordinate"] = str(
                response['coord']['lat']) + ', ' + str(response['coord']['lon'])
            data["temp"] = str(
                round(response['main']['temp'] - 273.15, 1)) + '°C'
            data["pressure"] = str(response['main']['pressure'])
            data["humidity"] = str(response['main']['humidity'])
        return render(request, 'main/index.html', data)
    else:
        return render(request, 'main/index.html', data)
