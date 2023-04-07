#!/usr/bin/python3
'''Python script that takes in a URL and an email, sends a POST request to the passed URL'''

import urllib.request
import urllib.parse
import sys

''' Get the URL and email'''
my_url = sys.argv[1]
email = sys.argv[2]

'''Encode the email value'''
mail = urllib.parse.urlencode({'email': email}).encode('utf-8')

'''Make a POST request to the URL with the email value'''
with urllib.request.urlopen(my_url, mail) as response:
    '''Read and decode response as UTF-8'''
    response_body = response.read().decode('utf-8')
    '''Print the response body'''
    print(response_body)
