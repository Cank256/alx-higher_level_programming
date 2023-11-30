#!/bin/bash
# This script sends an OPTIONS request to the provided URL and displays the allowed HTTP methods.
curl -sI -X OPTIONS "$1" | grep -i "allow" | cut -d' ' -f2-
