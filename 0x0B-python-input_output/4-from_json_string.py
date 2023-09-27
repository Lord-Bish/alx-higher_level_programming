#!/usr/bin/python3
"""This module returns a python object"""

import json

def from_json_string(my_str):
    """returns a python object"""

    return json.loads(my_str)

