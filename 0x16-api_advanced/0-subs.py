#!/usr/bin/python3
"""
    Retrieve the number of subscribers of a subreddit
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """Get the numbers of subscribers of a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers,
                            allow_redirects=False)
    if str(response) != "<Response [200]>":
        return 0
    result = response.json()
    num_subs = result.get("data").get("subscribers")
    return num_subs
