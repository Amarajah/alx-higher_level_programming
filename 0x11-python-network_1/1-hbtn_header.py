#!/usr/bin/python3
'''
Write a Python script that takes in a URL
sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.
'''
import sys
import urllib.request

if __name__ == "__main__":
    my_url = sys.argv[1]

    request = urllib.request.Request(my_url)
    with urllib.request.urlopen(request) as response:
        requested_id = response.getheader('X-Request-Id')
        print(f"{requested_id}")
