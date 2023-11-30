#!/bin/bash
# This script sends a request to the provided URL, retrieves the body size, and displays it in bytes.
curl -sI "$1" | grep -i "content-length" | awk '{print $2}' | tr -d '\r\n'
