import requests
from datetime import date, datetime

lat = 25.074972
lon = 55.144453
API_key = "293d14183fd04a680f4133160d9cc149"

response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=&appid={API_key}")
response.raise_for_status()

print(response)
data = response.json()
print(data)
# sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
# sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
