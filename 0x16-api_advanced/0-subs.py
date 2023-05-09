#!/usr/bin/python3
"""
queries the reddit api for the number_of_subscribers in a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get(f'http://www.reddit.com/r/{subreddit}/about.json',
                     headers={'User-Agent': 'Mozilla/5.0'}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
