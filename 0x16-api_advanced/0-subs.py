#!/usr/bin/python3

"""This module queries reddit API using python"""

import json

import requests


def number_of_subscribers(subreddit):
    """Get number of subscribers"""
    base_url = "https://www.reddit.com"
    url = "{}/r/{}/about.json".format(base_url, subreddit)
    headers = {"User-Agent": "ALXAPIAdv/0.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        return response.json().get("data", {}).get("subscribers", 0)
    except (requests.exceptions.RequestException,
            json.decoder.JSONDecodeError):
        return 0
