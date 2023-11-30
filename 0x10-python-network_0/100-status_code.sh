#!/bin/bash
# This script sends a request to the provided URL and displays only the status code of the response.

# Usage: ./get_status_code.sh <URL>

url=$1

if [ -z "$url" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

response=$(curl -s -I -o /dev/null -w "%{http_code}" "$url")

echo "Status Code: $response"
