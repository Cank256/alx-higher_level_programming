#!/bin/bash
# This script sends a POST request to the provided URL with specific variables in the request body and displays the body of the response.

# Usage: ./post_request.sh <URL>

url=$1
email="test@gmail.com"
subject="I will always be here for PLD"
response=$(curl -s -X POST -d "email=$email&subject=$subject" "$url")

echo "Response Body:"
echo "$response"
