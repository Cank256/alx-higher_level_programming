#!/bin/bash
# This script sends a request to the provided URL and displays only the status code of the response.
curl -s -I -o /dev/null -w "%{http_code}" "$1"
