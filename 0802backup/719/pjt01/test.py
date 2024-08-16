import requests

url = 'https://fakestoreapi.com/carts'
data = requests.get(url).json()
print(data)

#url : 요청을 보내는 서버의 주소
#requests.get(url): 해당 서버(url)에 데이터를 달라고 요청을 보내는 함수
#.json() : 내부의 데이터를 json(파이썬의 딕셔너리와 비슷) 형태로 변환해주는 함수


