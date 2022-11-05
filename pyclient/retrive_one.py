#!/usr/bin/env python3

import requests

endpoint = "http://localhost:8000/api/60/"
bank_details= "http://localhost:8000/api/details/ABHY0065001"
list_view = "http://localhost:8000/api/list/"


response_detail = requests.get(bank_details)
get_response = requests.get(endpoint)
get_list = requests.get(list_view)
print(get_response.json())
print(response_detail.json())
print(get_list.json())
