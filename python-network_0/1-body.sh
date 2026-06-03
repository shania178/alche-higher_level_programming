#!/bin/bash
# Sends a GET request to a URL and displays the body only if the final response status is 200
curl -sL "$1" -o /tmp/b -w "%{http_code}" | grep -q 200 && cat /tmp/b
