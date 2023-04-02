import requests

url = 'https://api.example.com/get_data'
params = {'param1': 'value1', 'param2': 'value2'}
headers = {'Authorization': 'Bearer my_token'}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)