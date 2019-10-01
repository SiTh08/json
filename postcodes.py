import requests
import json

# Explore this request package that is installed.
# Explore this http://postcodes.io/
# Use requests to make a GET request to http://postcodes.io/ api
# A GET request from the postcodes.io is copied. This is the get request: 'api.postcodes.io/postcodes/'. There is going to be a path and argument. The argument is my post code.

# path = 'http://api.postcodes.io/postcodes/'
# argument = 'IG12TP'

request_postcode = requests.get('http://api.postcodes.io/postcodes/IG12TP')

# print(request_postcode)
# print(request_postcode.headers)
# print(request_postcode.content)
print(request_postcode.json())
print(request_postcode.json()['result']['postcode'])
print(request_postcode.json()['result']['country'])
print(request_postcode.json()['result']['nhs_ha'])





# save responses in variable

# Use JSON library to unpack it