### creates a visual of the most-starred repositories on GitHub ###

import requests     # import the requests module

from plotly.graph_objs import bar
from plotly import offline      # import Bar class and offline modules from plotly

# make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'     # store the API's url & give it a variable
headers = {'Accept': 'application/vnd.github.v3+json'}      # request third version of the API
r = requests.get(url, headers=headers)      # use requests to make the call to the API, giving it the url & header we've defined

# store API response in a variable
response_dict = r.json()       # API information is returned in json format, use json method to convert info & store to a dictionary
# print(f"Total repositories: {response_dict['total_count']}")       # print the total count figure from the r dictionary
# explore information about the repositories:
repo_dicts = response_dict['items']     # items is a list containing a number of dictionaries...
repo_links, stars, labels = [], [],  []
# print(f"Repositories returned: {len(repo_dicts)}")      # print the length of that list

# examine the first repository
repo_dict = repo_dicts[0]       # pull out the first item from the 'items' repository
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']   # call the repo's name
    repo_url = repo_dict['html_url']    # call the repo's url
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"     # combine name & url to create a link
    repo_links.append(repo_link)    # add the name of each repository to the list
    stars.append(repo_dict['stargazers_count']) # add the stars count to the list
    owner = repo_dict['owner']['login']
    desciption = repo_dict['description']
    label = f"{owner}<br />{desciption}"        # creates the text to go into hovertext # '<br />' is HTML code for a linebreak
    labels.append(label)

# make visualisation
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,         # assign variables to the data needed to create the visualisation
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {           # stipulate the layout
    'title': 'Most Starred Javascript Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
    }

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')         # create the visual from the data in 'fig', create the file in this location
