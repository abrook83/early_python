### creates a visual of the most-starred repositories on GitHub ###

import requests     # import the requests module

from plotly.graph_objs import bar
from plotly import offline      # import Bar class and offline modules from plotly

# make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'     # store the API's url & give it a variable
headers = {'Accept': 'application/vnd.github.v3+json'}      # request third version of the API
r = requests.get(url, headers=headers)      # use requests to make the call to the API, giving it the url & header we've defined
print(f"Status code: {r.status_code}")      # call the 'status code' to identify a successful response from r, and print it (200 = success)

# store API response in a variable
response_dict = r.json()       # API information is returned in json format, use json method to convert info & store to a dictionary
# print(f"Total repositories: {response_dict['total_count']}")       # print the total count figure from the r dictionary
# explore information about the repositories:
repo_dicts = response_dict['items']     # items is a list containing a number of dictionaries...
repo_names, stars = [], []
# print(f"Repositories returned: {len(repo_dicts)}")      # print the length of that list

# examine the first repository
repo_dict = repo_dicts[0]       # pull out the first item from the 'items' repository
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])    # add the name of each repository to the list
    stars.append(repo_dict['stargazers_count']) # add the stars count to the list

# make visualisation
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,         # assign variables to the data needed to create the visualisation
}]

my_layout = {           # stipulate the layout
    'title': 'Most Starred Python Projects on GitHub',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')         # create the visual from the data in 'fig', create the file in this location
