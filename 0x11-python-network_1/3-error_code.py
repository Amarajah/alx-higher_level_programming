#!/usr/bin/python3
'''Python scripts that takes a url, sends request
and displays body of the response'''

if __name__ = "__main__"
    import urllib.request
    import urllib.error
    import sys

    my_url = sys.argv[1]

    try:
        with urllib.request.urlopen(my_url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.errorHTTPError as error:
        print(f"Error code: {error.code}")
