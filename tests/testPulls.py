from keys import *
import requests, json

params = {'client_id': cid, 'response_type': 'code', 'scope': 'check', 'redirect_uri': callback}

response = requests.request("GET", 'https://checkbook.io/oauth/authorize'
, headers = params)
print('Attempt using requests results in:')
print(response.text)

#attempt two
heads_test = {"Content-Type" : "application/json", "X-Accept" : "application/json"}
payload = {"client_id" : cid, "redirect_uri" : callback}
