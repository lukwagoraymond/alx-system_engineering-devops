#!/usr/bin/python3
"""
    Function that queries Reddit API & returns the number of subscribers
    for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Get the number of subscribers in subreddit"""
    base_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'TestAPI/0.0.1'}

    if type(subreddit) is not str or subreddit is None:
        return 0
    response = requests.get(base_url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    r_json = response.json()
    numberSubscribers = r_json.get('data').get('subscribers')
    return numberSubscribers
