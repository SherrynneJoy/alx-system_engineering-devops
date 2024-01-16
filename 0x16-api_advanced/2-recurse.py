#!/usr/bin/python3
"""a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[]):
    """queries Reddit for topics recursively"""
    if subreddit is None or not isinstance(subreddit, str):
        return None
    headers = {'User-Agent': 'CustomUserAgent/1.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        if not posts:
            return None
        titles = [post.get('data', {}).get('title', '') for post in posts]
        hot_list.extend(titles)
        after = data.get('data', {}).get('after', None)
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except Exception as e:
        return None
