#!/usr/bin/python3
"""
    Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit
"""
import requests
import pprint


def recurse(subreddit, hot_list=[], after=None):
    """
        Method that returns a list of titles of all hot posts for a
        given subreddit
        If no results are found, return None
    """
    reddit_url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {"User-Agent": "Holberton API access v0.1 (by /u/holbie)"}
    reddit_response = requests.get(reddit_url, headers=headers, allow_redirects=False)
    if reddit_response.status_code is not 200:
        return None
    else:
        reddit_resp_json = reddit_response.json()
        pp = pprint.PrettyPrinter(indent=4)
        children = reddit_resp_json.get("data").get("children")
        hot_list += children
        after = reddit_resp_json.get("data").get("after")
        if after:
            reddit_url = "https://www.reddit.com/r/{}/hot.json?after={}?limit=100".format(subreddit, after)
            recurse(subreddit, hot_list, after)
