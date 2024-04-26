#!/bin/bash
# send a POST req with a set of arguments
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
