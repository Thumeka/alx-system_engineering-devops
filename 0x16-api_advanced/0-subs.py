#!/usr/bin/python3
"""
Queries the Reddit API and returns n of subscribers
"""
from requests import get


def number_of_subscribers(subreddit):
    """Queries Reddit API and returns the
    number of subscribers for subreddit"""

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    user_agent = {'User-agent': 'Google Chrome Version 120.0.6099.217'}

    try:
        response = get(api_url, headers=user_agent, allow_redirects=False)

        if response.status_code == 200:
            results = response.json()
            subscribers = results['data']['subscribers']
            return subscribers
        else:
            print(f"Error: {response.status_code}")
            return 0
    except Exception as e:
        print(f"Exception: {e}")
        return 0
