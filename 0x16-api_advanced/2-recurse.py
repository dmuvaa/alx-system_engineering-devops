#!/usr/bin/python3

"""imports several modules"""


import json
import requests


def recurse(subreddit, hot_list=[]):
    """recursive function that queries the Reddit API
    and returns a list containing the titles of all hot articles
    for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": 'User Agent'}

    if after:
        url += f"?after={after}"

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200 or 'data' not in response.json() or 'children' not in response.json()['data']:
        return None

    for article in response.json()['data']['children']:
        hot_list.append(article['data']['title'])

    after = response.json()['data'].get('after')

    if not after:
        return hot_list

    return recurse(subreddit, hot_list, after)
