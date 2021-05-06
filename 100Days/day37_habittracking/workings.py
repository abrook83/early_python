import requests

UNAME = "abrook"
TOKEN = "chooka37"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": UNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{UNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Coding & Study Graph",
    "unit": "Hours",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}


response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)