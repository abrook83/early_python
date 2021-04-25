import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "aaronbrook83@gmail.com"
MY_PASSWORD = "83Tannum19"
LAT_JLT = 25.074972
LNG_JLT = 55.144453

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# print(iss_latitude)
# print(iss_longitude)

parameters = {
    "lat": LAT_JLT,
    "lng": LNG_JLT,
    "formatted": 0,
}

def station_overhead():
    if LAT_JLT+5 <= iss_latitude <= LAT_JLT-5 and LNG_JLT+5 <= iss_longitude <= LNG_JLT-5:
        return True


def night_time():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if night_time() and station_overhead():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look Up! \n\nThe ISS is above you in the sky!"
        )
