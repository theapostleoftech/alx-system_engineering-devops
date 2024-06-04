#!/usr/bin/python3
"""
    This prints the number of subscribers of a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    This function gets the number of
    subscribers of a given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers,
                            allow_redirects=False)
    if str(response) != "<Response [200]>":
        return 0
    result = response.json()
    no_of_subscribers = result.get("data").get("subscribers")
    return no_of_subscribers
