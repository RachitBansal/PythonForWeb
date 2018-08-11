import requests

url = "http://httpbin.org/ip"

r = requests.get(url)

data = r.json()

print(data['origin'])