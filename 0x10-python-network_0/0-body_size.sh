#!/bin/bash
# Send request using curl, save response body to a variable, and get its size in bytes
curl -s "$1" | wc -c
