#!/usr/bin/python3
"""queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    request = requests.get(url, headers=headers)
    if request.status_code == 200:
        req = request.json().get("data")
        [print(c.get("data").get("title")) for c in req.get("children")]
    else:
        print(None)
