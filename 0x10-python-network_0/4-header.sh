#!/bin/bash
# This script sends a GET request to the provided URL with a specific header and displays the body of the response.
curl -s -H "X-School-User-Id: 98" "$1"
