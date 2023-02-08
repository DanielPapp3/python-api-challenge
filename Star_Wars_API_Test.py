# Star Wars API Test File

import requests

Category = "people/"
Index_Number = "4"

# Set API URL & Parameters to Request info.
base_url = "https://swapi.dev/api/"

Response = requests.get(f"{base_url}{Category}{Index_Number}")
Response.json()


print(Response.json()['name'])