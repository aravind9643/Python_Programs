import requests

URL = "https://jsonplaceholder.typicode.com/albums"

PARAMS = {'_page': 1, '_limit': 1 }

r = requests.get(url= URL, params= PARAMS)

data = r.json()

print data