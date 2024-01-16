#!/usr/bin/python3
""" a function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit."""


def top_ten(subreddit):
    """queries Redddit API and prints the top ten hot posts"""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'CustomUserAgent/1.0'}
    try:
        response = requets.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        for post in posts:
            title = data.get('data', {}).get('title', '')
            print(title)
    except Exception as e:
        print(None)
