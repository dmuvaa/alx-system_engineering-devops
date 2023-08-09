#!/usr/bin/python3

"""imports a module"""

import requests


def fetch_articles(subreddit, after=None):
    """Fetches articles from Reddit API."""
    base_url = 'https://www.reddit.com/r/'
    url = f'{base_url}{subreddit}/hot.json'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) '
                      'Gecko/20100101 Firefox/91.0'
    }

    if after:
        url += f'?after={after}'

    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        return None

    return response.json()['data']


def count_words(subreddit, word_list, after=None, counts=None):
    """Counts occurrences of words in subreddit titles."""

    # Initialize counts dictionary
    if counts is None:
        counts = {word.lower(): 0 for word in word_list}

    # Get articles
    data = fetch_articles(subreddit, after)
    
    if not data:
        if not after:  # First call
            return
        else:
            # Sort and print the results
            sorted_results = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_results:
                if count > 0:
                    print(f"{word}: {count}")
            return

    # Iterate through the articles
    for article in data['children']:
        title = article['data']['title'].lower()
        for word in word_list:
            word_lower = word.lower()
            counts[word_lower] += title.split().count(word_lower)

    # Recursively call function for next set of articles
    count_words(subreddit, word_list, data['after'], counts)
