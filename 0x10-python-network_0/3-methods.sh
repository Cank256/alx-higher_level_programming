#!/bin/bash
# This script sends an OPTIONS request to the provided URL and displays the allowed HTTP methods.

# Usage: ./get_http_methods.sh <URL>

url=$1
allowed_methods=$(curl -sI -X OPTIONS "$url" | grep -i "allow" | cut -d' ' -f2-)

echo "Allowed HTTP Methods for '$url':"
echo "$allowed_methods"
