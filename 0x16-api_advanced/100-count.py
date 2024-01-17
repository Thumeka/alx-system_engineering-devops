#!/usr/bin/python3
"""Module for advance API exercises"""
import requests

url = 'http://reddit.com/r/{}/hot.json'

def count_words(subreddit, word_list, after=None, res=None):
    """Fetches all hot posts of a subreddit"""
    if res is None:
        res = {}

    headers = {'User-Agent': 'Google Chrome Version 120.0.6099.225'}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    response = requests.get(url.format(subreddit), headers=headers, params=params)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return

    for elem in response.json()['data']['children']:
        title = elem['data']['title'].lower().split()
        for word in word_list:
            if word in title:
                res[word] = res.get(word, 0) + 1

    after = response.json()['data']['after']
    if after:
        return count_words(subreddit, word_list, after, res)

    sorted_res = sorted(res.items(), key=lambda x: (-x[1], x[0]))
    for k, v in sorted_res:
        print(f"{k}: {v}")
