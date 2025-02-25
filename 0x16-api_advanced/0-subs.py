#!/usr/bin/python3
"""call reddit subscribers API"""
import requests
from requests import Response


def number_of_subscribers(subreddit):
    """The number of subscribers function"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"user-agent": "python:subreddit_fetcher:v1.0 (by /u/Doha)"}
    result = requests.get(url, headers=headers, allow_redirects=False)
    if result.status_code == 404:
        return 0
    result_data = result.json().get("data")
    print(result_data.get("subscribers"))
