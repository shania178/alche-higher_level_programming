#!/bin/bash
url="$1"
curl -s "$url" -o /dev/null -w "%{size_download}\n"
