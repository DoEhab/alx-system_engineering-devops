#!/usr/bin/python3
"""Return top ten posts"""
import requests


def top_ten(subreddit):
    """return title of top ten posts"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"user-agent": "python:subreddit_fetcher:v1.0 (by /u/Doha)"}
    params = {
        "limit": 10
    }
    result = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if result.status_code == 404:
        print(None)
        return
    result_data = result.json().get("data")
    for c in result_data.get("children"):
        print(c.get("data").get("title"))


