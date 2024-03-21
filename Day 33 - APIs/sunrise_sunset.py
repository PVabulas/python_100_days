import requests
import pprint

cur_loc = {"lat": 51.478370, "lng": -0.086990, "formatted": 0}

response = requests.get("https://api.sunrise-sunset.org/json", params=cur_loc)
response.raise_for_status()
results = response.json()
pprint.pprint(results)
