import requests
import json

# make an API call, store the response
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'    # access at this url
r = requests.get(url)       # 'requests' calls for the data
print(f"Status code: {r.status_code}")      # indicates the success of the call (200 = successful)

# explore the structure of the data
response_dict = r.json()        # the response is in json format, covert and store in a dictionary
readable_file = 'Python Crash Course Works\Projects\Datasets/readable_hn_data.json'     # create a file to display the data
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)       # dump the data into the file