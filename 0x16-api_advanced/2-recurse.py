#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[]):
    """Returns a list of titles of all hot posts on a given subreddit."""
    headers = {'User-Agent': 'My User Agent 1.0'}
    r = requests.get('https://www.reddit.com/r/{}/hot/.json'.
                     format(subreddit, headers=headers))
    if r.status_code == 404:
        return None
