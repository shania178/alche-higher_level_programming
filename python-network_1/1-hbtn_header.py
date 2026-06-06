#!/usr/bin/python3
"""Fetches a URL and displays the value of the X-Request-Id response header."""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers.get("X-Request-Id"))
