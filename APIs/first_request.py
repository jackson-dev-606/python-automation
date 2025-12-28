import requests

response = requests.get('https://www.icanhazdadjoke.com/', headers={'Accept': 'application/json'})
if response.ok:
    # print(response.status_code)
    # print(response.text)

    # print(response.json())
    # print(type(response.json()))

    print(response.json()['joke'])
else:
    print(f"Encountered error. HTTP status Code: {response.status_code}")