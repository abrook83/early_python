import requests

pixela_endpoint = "https://pixe.la/v1/users"

params = {
    'token': 'chooka37',
    'username': 'abrook',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=params)
# print(response.text)