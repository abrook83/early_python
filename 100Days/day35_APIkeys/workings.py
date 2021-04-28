import requests
from twilio.rest import Client

account_sid = "ACb66e2921da54242801402ad841f3b03e"
auth_token = "ca86aa21f9b1aabce0902e1d813bc26e"

# from datetime import date, datetime

endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    'lat': 45.777210,
    'lon': 3.082520,
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
    # print("rain coming")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Looks like rain, better take your umbrella!",
        from_="+18326484615",
        to="+971501054140"
    )

print(message.status)