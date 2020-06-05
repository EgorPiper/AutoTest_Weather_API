import requests
import json
import pytest


city = 'moscow'
testpressure = "1000"
key = 'dbc3eeabc690de5fee296384fd216316' #Ключ для использования апихи
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather' #первая апиха
params1 = {'q' : city , 'appid': key} #параметры для апихи
response = requests.get(BASE_URL , params = params1) #запрос get к первой апихе
N = response.json()
lon = N["coord"]['lon'] #вытягиваем координаты из первой апихи чтобы вставить во вторую
lat = N["coord"]['lat'] #вытягиваем координаты из первой апихи чтобы вставить во вторую
SINGLE_API = "https://api.openweathermap.org/data/2.5/onecall" #вторая апиха
time1 = "daily, minutely, hourly"  #настрока временных рамок для 2ой апихи
time2 = "current, minutely, hourly"
params2 = {'lon': lon, 'lat': lat, "exclude": time1, "appid": key} #параметры для апихи
params3 = {'lon': lon, 'lat': lat, "exclude": time2, "appid": key}
response2 = requests.get(SINGLE_API, params = params2)  #запрос get к второй апихе
response3 = requests.get(SINGLE_API, params = params3)
N1 = response2.json()
N2 = response3.json()

class Test_weather():

    def test_status_code(self):
        assert 200 == response.status_code #проверка что апи работает

    def test_city_country(self):
        country = N["sys"]["country"]
        assert country == 'RU' #проверка что выбранный город в России

    def test_temp_current_temperatura_vishe_absolutnogo_zero(self):
        tempcurrent = N1['current']['temp']
        assert (tempcurrent-273) > -273 #Проверка на то, что температура не показывается ниже абсолютного нуля

    def test_opredelenie_coordinat_Moscow(self):
        lonMSC = 37.62
        latMSC = 55.75
        assert N["coord"]["lon"] == lonMSC and N["coord"]["lat"] == latMSC

    def test_3thday_preassure1000(self):
        a1 = json.dumps(N2['daily'][2]['pressure'])
        assert a1 > testpressure  #Проверка на то, что на 3ий день давление будет больше 1000









