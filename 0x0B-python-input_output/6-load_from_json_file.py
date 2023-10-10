#!/usr/bin/python3
"""6"""
import json


def load_from_json_file(filename):
    """load from .json"""
    with open(filename) as fhand:
        return json.load(fhand)
