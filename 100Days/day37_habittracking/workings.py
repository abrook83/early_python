import requests
from datetime import date

### Create an account ###

UNAME = "abrook"
TOKEN = "chooka37"
GRAPH = "graph1"
today = date.today()

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": UNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

### Create a graph ###

graph_endpoint = f"{pixela_endpoint}/{UNAME}/graphs"

graph_params = {
    "id": GRAPH,
    "name": "Coding & Study Graph",
    "unit": "Hours",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)


### Create a pixel on the graph ###

point_endpoint = f"{pixela_endpoint}/{UNAME}/graphs/{GRAPH}"

HOURS = (input("Today's hours of study: "))

point_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": HOURS,
}

response = requests.post(url=point_endpoint, json=point_params, headers=headers)
print(response.text)

### Change a pixel on the graph ###

# change_date = input("Enter the date you want to change (yyyyMMdd): ")

# change_endpoint = f"{pixela_endpoint}/{UNAME}/graphs/{GRAPH}/{change_date}"

# HOURS = input(f"New figure: ")

# change_params = {
#     "quantity": HOURS,
# }

# response = requests.put(url=change_endpoint, json=change_params, headers=headers)
# print(response.text)

### Delete a pixel on the graph ###

# delete_date = input("Enter the date you want to change (yyyyMMdd): ")

# delete_endpoint = f"{pixela_endpoint}/{UNAME}/graphs/{GRAPH}/{delete_date}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)