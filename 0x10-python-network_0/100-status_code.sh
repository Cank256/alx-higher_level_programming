#!/bin/bash
# This script sends a request to the provided URL and displays only the status code of the response.
curl -sw "%{http_code}" -o /dev/null "$1"
