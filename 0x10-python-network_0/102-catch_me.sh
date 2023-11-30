#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me to get the server response.

# Usage: ./catch_me.sh

response=$(curl -s -X PUT -L -d "user_id=98" 0.0.0.0:5000/catch_me)
echo "$response"