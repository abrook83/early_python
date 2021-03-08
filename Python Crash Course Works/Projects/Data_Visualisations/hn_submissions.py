from operator import itemgetter

import requests

# make an API call and store the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)           # call the API and print status of the response
print(f"Status code: {r.status_code}")

# process information about each submission
submission_ids = r.json()       # feed the json file as a list (it's a list of numbers) 
submission_dicts = []       # empty list to store dict items...

for submission_id in submission_ids[:30]:       # loop through first 30...
    # make a seperate API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"    # plug each number from the list into a new url
    r = requests.get(url)       # call and give the status of the response
    print(f"id: {submission_id}\tstatus: {r.status_code}")      # print the above 2 as a text string
    response_dict = r.json()          # now feed each API call of the above to a list

    # if 'descendants' not in response_dict:
    #     print("Missing data")

    # build a dictionary for each article, storing the title, link & no. of comments
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except KeyError:
        # skip over if there is a KeyError
        continue
    else:
        submission_dicts.append(submission_dict)        # append each of the above items to the submission_dicts dictionary

# itemgetter takes the 'comments' as the number of comments on each item in submission_dicts, then we sort them in reverse numerical order
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)       

for submission_dict in submission_dicts:    # for each item in submission_dicts...  
    print(f"\nTitle: {submission_dict['title']}")       # print the title, link and comments
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")