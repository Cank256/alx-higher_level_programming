#!/usr/bin/env bash
# This script sends a JSON POST request to the provided URL with the contents of a file in the request body.

# Usage: ./json_post_request.sh <URL> <filename>

url=$1
file=$2

if [ -z "$url" ] || [ -z "$file" ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

response=$(curl -s -X POST -H "Content-Type: application/json" -d "@$file" "$url")

echo "Response Body:"
echo "$response"
