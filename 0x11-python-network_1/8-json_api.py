#!/usr/bin/python3
'''
Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the
letter as a parameter.'''

import sys
import requests

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        value = sys.argv[1]
    else:
        value = ""

    payload = {'a': value}
    r = requests.post(url, data=payload)

    try:
        json = r.json
        if len(json) > 0:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
