import requests
import jsonpath_rw
import pytest

city = 'Oslo'
key = '5f4815035bb12cda16d4944aab26122f'
test_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid='
response = requests.get(test_url + key)


class TestWeather:

    def test_status_code(self):
        assert 200 == response.status_code, 'Fail'
        print('Good')

    def test_country(self):
        expectation = 'NO'
        data = response.json()
        country = data['sys']['country']
        assert country == expectation, print('No, ' + city + ' is not ' + expectation)
        print('Yep, ' + city + ' is ' + expectation)

    def test_dif(self):  # сравнение максимальной температуры в двух городах
        city1 = 'Moscow'
        test_url1 = 'http://api.openweathermap.org/data/2.5/weather?q=' + city1 + '&appid='
        response1 = requests.get(test_url1 + key)
        data = response1.json()
        weather1 = data['main']['temp_max']  # максимальная температура в первом городе

        city2 = 'London'
        test_url2 = 'http://api.openweathermap.org/data/2.5/weather?q=' + city2 + '&appid='
        response2 = requests.get(test_url2 + key)
        data = response2.json()
        weather2 = data['main']['temp_max']  # максимальная температура во втором городе

        assert weather1 < weather2, print('Максимальная температура в ' + city1 + ' больше, чем в  ' + city2)
        print('Максимальная температура в ' + city1 + ' меньше, чем в  ' + city2)

    def test_coord(self):
        expected_lon = 10.75
        expected_lat = 59.91  # ожидаемые координаты
        data = response.json()
        lon = data['coord']['lon']
        lat = data['coord']['lat']
        assert lon == expected_lon and lat == expected_lat, print('The coordinates are incorrect')
        print('The coordinates are correct')

        # команда для отчета в XML: pytest tests\weather_tests.py -v --junitxml=tests\result.xml