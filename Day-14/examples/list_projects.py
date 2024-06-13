# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://bharathgrandhi45.atlassian.net/rest/api/3/project"

API_TOKEN="ATATT3xFfGF0Rm2BLKp-eOX16S0uSzMWRfe9Pf2ahhLeBt4oTWZV9iIxlMPSMMcf8zUkgEs1hnWIK7a0USYy9armrMo5mjUybf0FtBv3cGGoQ8BzxYYtZKodAcHHnQ-96k9qixaepZ1Cw6J84O6XH92Q8TPJVL8FXOsHt5zlN2fLRg77IGL7QDA=1B5B3162"

auth = HTTPBasicAuth("bharathgrandhi89@gmail.com",API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)
