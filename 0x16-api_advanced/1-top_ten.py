#!/usr/bin/python3

"""imports a module"""

import requests


def top_ten(subreddit):
    """Function that queries the Reddit API
    and prints the titles of the first 10 hot posts
    listed for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": 'User Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
