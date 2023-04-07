#!/usr/bin/python3
'''
Write a Python script that takes in a URL
sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.
'''
import sys
import urllib.request
'''Get url'''
if __name__ == "__main__":
    my_url = sys.argv[1]
    '''Send request to my_url'''
    request = urllib.request.Request(my_url)
    with urllib.request.urlopen(request) as response:
        '''Get value of header'''
        requested_id = response.getheader('X-Request-Id')
        '''Print value of header'''
        print(f"{requested_id}")
