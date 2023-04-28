#!/usr/bin/python3
'''Python script that fetches https://alx-intranet.hbtn.io/status'''

if __name__ == "__main__":
    from requests import get

    result = get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:', type(result.text))
    print('\t- content:', result.text)
