#!/usr/bin/python3
"""recursive function that queries the Reddit API, parses the title
of all hot articles, and prints a sorted count of given keywords"""
import requests


def count_words(subreddit, word_list, counts=None, after=None):
    if counts is None:
        counts = {}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if data["data"]["children"]:
            for post in data["data"]["children"]:
                title = post["data"]["title"]
                words = title.lower().split()
                for word in word_list:
                    if word.lower() in words and not \
                            any(c in word for c in ['.', '!', '_']):
                        if word.lower() not in counts:
                            counts[word.lower()] = 0
                        counts[word.lower()] += 1
            return count_words(subreddit, word_list,
                               counts, data["data"]["after"])
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print(None)
