#!/usr/bin/python3
"""print the titles of the first 10 hot posts from a given subreddit."""
import requests


def top_ten(subreddit):
	headers = {'User-Agent': 'AhmedHosny/1.0'}
	url = f"https://www.reddit.com/r/{subreddit}/hot.json?sort=top&limit=9"

	response = requests.get(url, headers=headers, allow_redirects=False)
	print(response.json())
	if response.status_code != 200:
		print(None)
		return

	data = response.json()
	if 'data' not in data or 'children' not in data['data']:
		print(None)
		return

	posts = response.json()["data"]["children"]
	for post in posts:
		print(post["data"]["title"])
