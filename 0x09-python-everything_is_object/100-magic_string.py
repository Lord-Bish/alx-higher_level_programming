#!/usr/bin/python3
def magic_string(num={'counter': 0}):
    num['counter'] += 1
    return (', '.join(['BestSchool'] * (num['counter'])))
