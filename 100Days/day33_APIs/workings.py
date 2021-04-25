import requests
from datetime import date, datetime

LAT_JLT = 25.074972
LNG_JLT = 55.144453

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response)     # '200' = success!
# response.raise_for_status()      # part of the request module, ports HTTP status request responses....

# """Retrieve the json data from the source url"""
# # data = response.json()["iss_position"]  # data within the "iss_position" heading
# # print(data)

# long = response.json()["iss_position"]["longitude"]
# lat = response.json()["iss_position"]["latitude"]

# position = (long, lat)
# print(position)

parameters = {
    "lat": LAT_JLT,
    "lng": LNG_JLT,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

timenow = datetime.now()

print(sunrise)
print(sunset)
print(timenow.hour)