#!/bin/bash
# sends a GET request and displays the response body, only for a 200 status code response
curl -sX GET "$1" -L
