#!/usr/bin/python3
"""
    Function that queries Reddit API & prints the titles of the first 10
    hot posts listed for a given subreddit
"""
import requests
from sys import argv


def top_ten(subreddit):
    """Get ten top Posts"""
    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    base_url += "?limit=10"
    headers = {'User-Agent': 'TestAPI/0.0.1'}
    response = requests.get(base_url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    r_json = response.json()
    for post in r_json['data']['children']:
        print(post['data']['title'])
