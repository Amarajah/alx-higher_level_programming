#!/usr/bin/python3
'''Script giving the value of the variable X-Request-Id in the response header'''

import sys
import requests


if __main__ == '__name__':
    url = sys.argv[1]
    '''Using the get funcction, get the header'''

    result = requests.get(url)
    print(result.headers.get('X-Request-Id'))
