#!/usr/bin/python3
"""This modules makes an obj from json file"""

import json

def load_from_json_file(filename):
    """creates an obj from a json file"""

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
