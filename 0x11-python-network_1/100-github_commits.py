#!/usr/bin/python3
"""
Script that lists 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails” using the GitHub API.
"""

import requests
import sys

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f'https://api.github.com/repos/{owner_name}/{repository_name}/commits'

    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit.get('sha', 'Unknown SHA')
        author_name = commit.get('commit', {}).get('author', {}).get('name', 'Unknown Author')
        print(f"{sha}: {author_name}")

