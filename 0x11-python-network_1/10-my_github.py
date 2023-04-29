#!/usr/bin/python3
'''
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
'''

import sys
import requests

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    if len(sys.argv) > 1:
        user = sys.argv[1]
        pwd = sys.argv[2]

    r = requests.get(url, auth=(user, pwd))
    json = r.json()
    print("{}".format(json.get('id')))
