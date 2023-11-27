import requests

url = 'http://127.0.0.1:5000/search'
data = {'search_string': 'Cooking oil'}

response = requests.post(url, json=data)
print(response.json())
