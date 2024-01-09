#!/usr/bin/python3
"""Simple function to lookup the names in a scope
"""

def lookup(obj):
    if obj is not None:
        return (dir(obj))
    return None
