#!/bin/bash
# displays the size of the body of the response
curl --write-out "%{size_download}\n" -s -o /dev/null "$1"
