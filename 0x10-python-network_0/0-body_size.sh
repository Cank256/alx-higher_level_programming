#!/bin/bash
# This script sends a request to the provided URL, retrieves the body size, and displays it in bytes.

# Usage: ./get_response_size.sh <URL>

url=$1
size=$(curl -sI "$url" | grep -i "content-length" | awk '{print $2}' | tr -d '\r\n')
echo "Size of the response body: $size bytes"
