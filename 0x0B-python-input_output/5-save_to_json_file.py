#!/usr/bin/python3
"""This module writes object to a file using json"""

import json

def save_to_json_file(my_obj, filename):
    """writes my_obj to filename using json"""

    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
