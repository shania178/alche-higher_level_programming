#!/bin/bash
# Sends an OPTIONS request to a URL and displays the allowed HTTP methods
curl -sI -X OPTIONS "$1" | grep -i "^Allow" | cut -d" " -f2-
