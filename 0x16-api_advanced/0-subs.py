#!/usr/bin/python3
"""
Queries the Reddit API and returns n of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Gets the number of subscibers"""
    # set custom headers for <Response [429]>
    headers = {'User-Agent': 'My User Agent 1.0'}
    r = requests.get('https://www.reddit.com/r/{}/about.json'.
                     format(subreddit), headers=headers)
    # if given wrong subreddit
    if r.status_code == 404:
        return 0
    result = r.json().get('data')
    # print (r)
    return result.get('subscribers')
