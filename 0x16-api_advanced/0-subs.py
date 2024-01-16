#!/usr/bin/python3
"""
Queries the Reddit API and returns n of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Gets the number of subscribers for a subreddit."""
    # Set custom headers for the request
    headers = {'User-Agent': 'My User Agent 1.0'}
    # Make the HTTP request to get subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers)
    # Check if the subreddit exists (status code 404)
    if response.status_code == 404:
        return 0
    try:
        # Parse JSON response
        result = response.json().get('data')
        # Return the number of subscribers
        return result.get('subscribers')
    except (ValueError, AttributeError):
        # Handle JSON parsing errors
        print("Error parsing JSON response.")
        return 0
