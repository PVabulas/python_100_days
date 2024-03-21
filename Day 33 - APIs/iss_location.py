import requests

site = "http://api.open-notify.org/iss-now.json"

response = requests.get(site)
response.raise_for_status()
response_json = response.json()
print(response_json["iss_position"])
