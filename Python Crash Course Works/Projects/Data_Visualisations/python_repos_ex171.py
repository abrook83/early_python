import requests     # import the requests module

# make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'     # store the API's url & give it a variable
headers = {'Accept': 'application/vnd.github.v3+json'}      # request third version of the API
r = requests.get(url, headers=headers)      # use requests to make the call to the API, giving it the url & header we've defined
print(f"Status code: {r.status_code}")      # call the 'status code' to identify a successful response from r, and print it (200 = success)

# store API response in a variable
response_dict = r.json()       # API information is returned in json format, use json method to convert info & store to a dictionary
print(f"Total repositories: {response_dict['total_count']}")       # print the total count figure from the r dictionary

# explore information about the repositories
repo_dicts = response_dict['items']     # items is a list containing a number of dictionaries...
print(f"Repositories returned: {len(repo_dicts)}")      # print the length of that list

# examine the first repository
repo_dict = repo_dicts[0]       # pull out the first item from the 'items' repository

print("\nSelected information from the each repository:\n")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")     # pull information from keys in the first repository's dictionary
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
    print("")

# print(f"\nKeys: {len(repo_dict)}")      # print the length of the repo_dict dictionary
# for key in sorted(repo_dict.keys()):    # print each of the keys in the repo_dict dictionary
#     print(key)

# # process results
# print(response_dict.keys())