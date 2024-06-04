#!/usr/bin/python3
"""
    Retrieves the hot posts from the reddit API
"""
import requests
from sys import argv


def recurse(subreddit, hot_list=[], after=""):
    """Get the all hot posts"""
    if after is None:
        return []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    url += "?limit=100&after={}".format(after)
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers,
                            allow_redirects=False)
    if str(response) != "<Response [200]>":
        return None
    result = response.json()
    hot_posts_json = result.get("data").get("children")
    for post in hot_posts_json:
        hot_list.append(post.get("data").get("title"))
    return hot_list + recurse(subreddit, [], result.get("data").get("after"))
