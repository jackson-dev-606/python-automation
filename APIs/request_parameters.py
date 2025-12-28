import requests

url = 'https://icanhazdadjoke.com/search'

request_params = {"term": "spaghetti"}
response = requests.get(
    url=url,
    headers={'Accept': 'application/json'},
    params=request_params
)
data = response.json()
for item in data['results']:
    print(item['joke'])