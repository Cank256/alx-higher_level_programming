#!/bin/bash
# This script sends a DELETE request to the provided URL and displays the body of the response.

# Usage: ./delete_request.sh <URL>

url=$1
response=$(curl -s -X DELETE "$url")

echo "Response Body:"
echo "$response"
