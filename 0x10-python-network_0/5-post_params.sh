#!/bin/bash
# send a POST req with a set of arguments
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1" -L
