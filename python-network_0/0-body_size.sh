#!/bin/bash
# Sends a request to a URL and displays the size of the response body
curl -s "$1" -o /dev/null -w "%{size_download}"
