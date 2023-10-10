#!/usr/bin/python3
"""5"""
import json


def save_to_json_file(my_obj, filename):
    """saves to a json file"""
    with open(filename, "w") as fhand:
        json.dump(my_obj, fhand)
