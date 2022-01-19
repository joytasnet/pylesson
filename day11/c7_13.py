import requests
response = requests.get('http://python.org/downloads/')
text=response.text
print(text)
