#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ recursive function that queries the Reddit API and
    returns a list containing the titles of all hot articles
    for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if data["data"]["children"]:
            for post in data["data"]["children"]:
                hot_list.append(post["data"]["title"])
            return recurse(subreddit, hot_list, data["data"]["after"])
        else:
            return hot_list
    else:
        return None
