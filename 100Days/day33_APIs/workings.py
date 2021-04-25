import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)     # '200' = success!
response.raise_for_status()      # part of the request module, ports HTTP status request responses....

"""Retrieve the json data from the source url"""
# data = response.json()["iss_position"]  # data within the "iss_position" heading
# print(data)

long = response.json()["iss_position"]["longitude"]
lat = response.json()["iss_position"]["latitude"]

position = (long, lat)
print(position)