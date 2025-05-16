# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

import MyJiraTokens

url = "https://fixitinfirmware.atlassian.net/rest/api/3/search"

# auth = HTTPBasicAuth("email@example.com", "<api_token>")
# 
# headers = {
#   "Accept": "application/json"
# }
# 
# query = {
#   'jql': 'project = HSP'
# }
# 
# response = requests.request(
#    "GET",
#    url,
#    headers=headers,
#    params=query,
#    auth=auth
# )
# 
# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))