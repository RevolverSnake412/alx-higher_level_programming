#!/usr/bin/python3
"""5"""
import json


def save_to_json_file(my_obj, filename):
    """saves to a json file"""
    text = json.dumps(my_obj)
    with open(filename, "w", encoding="UTF8") as fhand:
        json.dump(my_obj. f)
