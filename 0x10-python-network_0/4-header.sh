#!/bin/bash
# This script sends a GET request to the provided URL with a specific header and displays the body of the response.

# Usage: ./get_request_with_header.sh <URL>

url=$1
header_value="X-School-User-Id: 98"
response=$(curl -s -H "$header_value" "$url")

echo "Response Body:"
echo "$response"
