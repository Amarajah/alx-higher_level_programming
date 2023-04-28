#!/usr/bin/python3
'''displays the body of the response'''

import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]

    output = requests.get(url)
    if output.status_code >= 400:
        print("Error code: {}".format(output.status_code))
    else:
        print(output.text)
