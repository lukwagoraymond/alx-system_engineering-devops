#!/usr/bin/python3
"""
    Recursive Function that queries Reddit API & prints the titles of the
    first 10 hot posts listed for a given subreddit
"""
import requests
from sys import argv


def recurse(subreddit, hot_list=[], after="", count=0):
    """Get ten top Posts"""
    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after, "limit": 100, "count": count}
    headers = {'User-Agent': 'TestAPI/0.0.1'}
    response = requests.get(base_url, headers=headers,
                            allow_redirects=False, params=params)
    if response.status_code != 200:
        return None

    r_json = response.json()
    after = r_json['data']['after']
    count += r_json['data']['dist']
    for post in r_json['data']['children']:
        hot_list.append(post['data']['title'])
    if after is not None:
        recurse(subreddit, hot_list, after, count)
    return hot_list
