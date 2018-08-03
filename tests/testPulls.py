from keys import *
import requests

params = {'client_id': 'a110738a6c9248638dcdf8be283d3bcb', 'response_type': 'code', 'scope': 'check', 'redirect_uri': callback}

response = requests.request("POST", 'https://checkbook.io/oauth/authorize'
, headers = params)

print(response)
