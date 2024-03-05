#!/usr/bin/python3
"""retrieve the titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
	headers = {'User-Agent': 'AhmedHosny/1.0'}
	url = f"http://www.reddit.com/r/{subreddit}/hot.json"

	if after:
		url += f'?after={after}'
	response = requests.get(url, headers=headers)
	if response.status_code != 200:
		return None

	data = response.json()
	if 'data' not in data or 'children' not in data['data']:
		return None
	posts = data["data"]["children"]

	for post in posts:
		hot_list.append(post["data"]["title"])

	if data['data']['after']:
		return recurse(subreddit, hot_list, data['data']['after'])
	else:
		return hot_list
