#!/bin/bash
# This script sends a GET request to the provided URL and displays the body of the response for a 200 status code.

# Usage: ./get_response_body.sh <URL>

url=$1
response=$(curl -s -o /dev/null -w "%{http_code}" "$url")

if [ "$response" -eq 200 ]; then
    body=$(curl -s "$url")
    echo "Response Body:"
    echo "$body"
else
    echo "Error: Non-200 status code received - $response"
fi
