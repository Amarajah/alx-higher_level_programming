#!/usr/bin/python3
''' Manage urllib.error.HTTPError exceptions and
print: Error code: followed by the HTTP status code'''

if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as output:
            print(output.read().decode('UTF-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
