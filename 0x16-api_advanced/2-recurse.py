#!/usr/bin/python3

"""This module queries reddit API using python"""

import json

import requests

base_url = "https://www.reddit.com"
headers = {"User-Agent": "ALXAPIAdv/0.1"}


def recurse(subreddit, hot_list=[], after=None):
    params = {"after": after}
    url = "{}/r/{}/hot.json".format(base_url, subreddit)

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        posts = response.json().get("data", {}).get("children", [])
        hot_list.extend([post.get("data", {}).get("title", "")
                        for post in posts])
        after = response.json().get("data", {}).get("after")
        if after:
            return recurse(subreddit, hot_list, after)
    except (requests.exceptions.RequestException,
            json.decoder.JSONDecodeError):
        return None

    return hot_list
