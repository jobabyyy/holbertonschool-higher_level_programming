#!/usr/bin/python3

import urllib.request

url = 'https://intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    html_content = response.read()

print("Body response:")
print("\t- type:", type(html_content)
print("\t- content:", html_content)
print("\t- utf8 content:", html_content.decode('utf-8'))
