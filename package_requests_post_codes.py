import requests
import _json

request_bbc = requests.get('https://www.bbc.co.uk/news')

print(request_bbc)

print(request_bbc.headers.keys())
print(request_bbc.content)

# Explore this request package that is installed.
# Explore this http://postcodes.io/

# Use requests to make a GET request to http://postcodes.io/ api
# Search for a post code (can be your own or any)

# save responses in variable

# Use JSON library to unpack it