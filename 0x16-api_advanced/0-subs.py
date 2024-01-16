#!/usr/bin/python3
"""a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    headers = {"User-Agent": "Google Chrome Version 120.0.6099.217"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            data = response.json()
        elif response.status_code == 404:
            return 0
        else:
            return 0
    except Exception as e:
        return 0

