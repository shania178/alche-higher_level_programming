#!/usr/bin/python3
"""Fetches a URL and displays the X-Request-Id response header value."""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as r:
    print(r.headers.get("X-Request-Id"))
