#!/bin/bash
# prints the allowed methods only
curl -sI OPTIONS  "$1" | grep "ALLOW" | cut -d " " -f2-
