import requests
import json
import pytest

test_url = 'http://api.openweathermap.org/data/2.5/weather?q=Moscow&appid='
appID = '1a74191a7470de1528d0a6bb044fb884'
response = requests.get(test_url + appID)
data = response.json()

class TestWeather():

    def test_status_code(self):
        assert 200 == response.status_code, 'Fail'
        print('That is right')

    def test_Moscow_in_Russia(self):
        country = data['sys']['country']
        print(country)
        assert country == 'RU'

    def test_temp_avoid_283(self):
        temp = data['main']['temp']
        print(temp)
        assert temp > 283

    def test_coordinate_is_right_for_Moscow(self):
        # coordinate of Moscow
        lat = 55.75
        lon = 37.62
        assert data['coord']['lat'] == lat and data['coord']['lon'] == lon

    def test_comparison_temp_with_tempfeelslike(self):
        temp = data['main']['temp']
        temp_feels_like = data['main']['feels_like']
        assert temp > temp_feels_like
