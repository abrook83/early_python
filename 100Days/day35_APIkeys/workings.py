import requests
from datetime import date, datetime

endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    'lat': 25.074972,
    'lon': 55.144453,
    'appid': "293d14183fd04a680f4133160d9cc149",
}

response = requests.get(endpoint, params=weather_params)

print(response.status_code)
data = response.json()
print(data)
# sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
# sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
