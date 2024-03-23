import requests

params = {
    "lat": 42.7908,
    "lon": -77.5171,
    "appid": "b3016f0a18e8c92270ea4ba799bcb553",
    "cnt": 4,
}
response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast", params=params
)
response.raise_for_status()
city = response.json()["city"]["name"]
for interval in response.json()["list"]:
    for weather_type in interval["weather"]:
        if 200 <= weather_type["id"] <= 600:
            print(
                f"At {interval['dt_txt']}, the weather in {city} will be {weather_type['description']}"
            )
            break
