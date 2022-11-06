#!/usr/bin/env python3

import requests

endpoint ="http://localhost:8000/api/bank_branch/RTGS-HO"

get_response = requests.get(endpoint)

print(get_response.json())
