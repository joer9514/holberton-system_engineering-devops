#!/usr/bin/python3
""" hot posts """
import requests


def top_ten(subreddit):
    rURL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    h = {"User-Agent": 'any agent'}

    derulo = requests.get(rURL, headers=h, allow_redirects=False).json()
    if derulo is None:
        print(None)
        return
    data = derulo.get('data')
    if data is None:
        print(None)
        return
    post_list = data.get('children')
    for a in range(10):
        title = post_list[a].get('data').get('title')
        print(title)
