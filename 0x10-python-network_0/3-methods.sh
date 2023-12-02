#!/bin/bash
# This script sends an OPTIONS request to the provided URL and displays the allowed HTTP methods.
curl -sI "$1" | grep -i Allow | cut -d ' ' -f 2-
