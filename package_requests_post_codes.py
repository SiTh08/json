import requests
import json

request_bbc = requests.get('https://www.bbc.co.uk/news')

print(request_bbc)

print(request_bbc.headers.keys())
print(request_bbc.content)

