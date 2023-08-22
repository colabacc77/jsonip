import requests

response = requests.get('http://jsonip.com')
print(response.status_code)

print(response.text)
