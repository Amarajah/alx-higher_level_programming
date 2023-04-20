#!usr/bin/python3
'''
Python script that takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the header of the response.
'''
if __name__ == "__main__"
    import sys
    import urllib.request

    my_url = sys.argv[1]

    with urllib.request.urlopen(my_url) as response:
        reply = response.read()
        print(response.info().get'(X-Request-Id'))

