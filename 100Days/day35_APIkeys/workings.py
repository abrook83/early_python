import requests
# from datetime import date, datetime

endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    'lat': 52.085339,
    'lon': 8.742500,
    'exclude': 'current,minutely,daily',
    'appid': "293d14183fd04a680f4133160d9cc149",
}

response = requests.get(endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
# print(data)

will_rain = False
for _ in range(12):
    condition = data["hourly"][_]["weather"][0]["id"]
    if condition <= 700:
        will_rain = True

if will_rain:
    print("Don't forget your umbrella!")