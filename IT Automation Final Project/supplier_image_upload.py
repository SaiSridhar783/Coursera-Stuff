#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
path = os.getcwd()
files = os.listdir()

for file in files:
    with open(file, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
