import requests

lat = 37.56
lon = 126.97
api_key = '9fecc68821f8b5da7e88ee05e4e51cdf'

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
reponse = requests.get(url).json()
print(reponse)
print(type(reponse))

#데이터 중 온도를 파싱하시오.
temp = reponse['main']['temp']
print(f'온도 = {temp}')