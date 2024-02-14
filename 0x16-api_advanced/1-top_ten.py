#!/usr/bin/python3

"""This module queries reddit API using python"""

import json

import requests


def top_ten(subreddit):
    """Get top ten hot post of a subreddit """
    base_url = "https://www.reddit.com"
    url = "{}/r/{}/hot.json?limit=10".format(base_url, subreddit)
    headers = {"User-Agent": "ALXAPIAdv/0.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        posts = response.json().get("data", {}).get("children", [])
    except (requests.exceptions.RequestException,
            json.decoder.JSONDecodeError):
        return None
    for post in posts:
        title = post.get("data", {}).get("title", "")
        print(title)
