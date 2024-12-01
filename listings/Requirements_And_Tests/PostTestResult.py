import requests
import json
import os

from requests.auth import HTTPBasicAuth

xray_cloud_base_url = "https://xray.cloud.getxray.app/api/v2"
client_id = os.getenv('CLIENT_ID', "your_client_id")
client_secret = os.getenv('CLIENT_SECRET',"your_client_secret")
 
# endpoint doc for authenticating and obtaining token from Xray Cloud: https://docs.getxray.app/display/XRAYCLOUD/Authentication+-+REST+v2
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
auth_data = { "client_id": client_id, "client_secret": client_secret }
response = requests.post(f'{xray_cloud_base_url}/authenticate', data=json.dumps(auth_data), headers=headers)
auth_token = response.json()
print(auth_token)

# endpoint doc for importing Xray JSON formatted data: https://docs.getxray.app/display/XRAY/Import+Execution+Results+-+REST#ImportExecutionResultsREST-XrayJSONresults
execution_result = open("your_test_result.json", "rb")
headers = {'Authorization': 'Bearer ' + auth_token, 'Content-Type': 'application/json'}
response = requests.post(f'{xray_cloud_base_url}/import/execution', data=execution_result, headers=headers)

print(response.status_code)
print(response.content)