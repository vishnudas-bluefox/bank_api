#!/usr/bin/env python3

import requests

endpoint1 = "http://localhost:8000/api/list/"
endpoint = "http://localhost:8000/api/list_all/"

get_response = requests.get(endpoint1,json={"query":"Hello boys"})

get_response2 = requests.get(endpoint)

print(get_response.json())
print(get_response2.json())
