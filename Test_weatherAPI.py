import pytest
import requests
import json
from jsonpath_ng import jsonpath, parse

json_body = '{"coord":{"lon":37.62,"lat":55.75},"weather":[{"id":802,"main":"Clouds","description":"переменная облачность","icon":"03d"}],"base":"stations","main":{"temp":16,"feels_like":15.07,"temp_min":15,"temp_max":16.67,"pressure":1024,"humidity":63},"visibility":10000,"wind":{"speed":1},"clouds":{"all":40},"dt":1590569557,"sys":{"type":1,"id":9029,"country":"RU","sunrise":1590541131,"sunset":1590602094},"timezone":10800,"id":524901,"name":"Москва","cod":200}'
link = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=68d9c6557101f408224e83aa3c323c11"
response = requests.get(link)
class TestWeather():

  def test_status_code(self): #тест кода ответа
    assert 200 == response.status_code, "Код ответа неверен"
   
  def test_is_json(self): #проверяем что пришел json
    try:
     json_data = json.loads(response.text)
    except ValueError:
     assert False, "Данные не соответствуют json"
	
  def test_min_max_temp(self): 
    #response = requests.get(link)
    json_data = json.loads(response.text)
    json_find_max_temp = parse('main.temp_max')
    json_find_min_temp = parse('main.temp_min')
    max_temp = json_find_max_temp.find(json_data)
    min_temp = json_find_min_temp.find(json_data)
    print('max temp', max_temp[0].value)
    print('min temp', min_temp[0].value)
    assert max_temp[0].value >=  min_temp[0].value, "Максимальная температура меньше минимальной!"
	
  def test_unit_of_measure_metric(self):
    response_metric = requests.get("https://api.openweathermap.org/data/2.5/weather?q=London&appid=68d9c6557101f408224e83aa3c323c11&units=metric")
    json_data = json.loads(response.text) 
    json_data_metric = json.loads(response_metric.text)
    json_find_temp = parse('main.temp')
    temp_metric = json_find_temp.find(json_data_metric)
    temp_kelv = json_find_temp.find(json_data)
    temp = int(temp_metric[0].value)+273.15
    print("температура -", temp)
    inaccuracy = abs(temp-int(temp_kelv[0].value))
    print('погрешность - ', inaccuracy)
    assert inaccuracy<=1, "система исчисления некорректна"
	
	#команда для запуска с отчетом в XML: pytest Test_weatherAPI.py -v --junitxml=result.xml
	
	