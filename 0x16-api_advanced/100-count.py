#!/usr/bin/python3
"""Module for task 3"""
import requests

def count_words(subreddit, word_list, word_count=None, after=None):
    """Queries the Reddit API and returns the count of words in
    word_list in the titles of all the hot posts
    of the subreddit"""
    
    if word_count is None:
        word_count = {word: 0 for word in word_list}
        
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My-User-Agent"}
    
    response = requests.get(url, headers=headers, params={"after": after}, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()

    titles = [child["data"]["title"] for child in data["data"]["children"]]
    
    for title in titles:
        split_words = title.lower().split(' ')
        for word in word_list:
            word_count[word] += split_words.count(word.lower())

    next_page = data["data"].get("after")
    
    if not next_page:
        sorted_counts = sorted(word_count.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        for k, v in sorted_counts:
            if v != 0:
                print(f'{k}: {v}')
    else:
        count_words(subreddit, word_list, word_count, next_page)
