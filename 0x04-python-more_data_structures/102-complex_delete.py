#!/usr/bin/python3

def complex_delete(a_dict, value):
    if value not in dictionary.items():
        return a_dict
    for key, val in a_dict.items():
        if val == value:
            del a_dict[val]
    return a_dict
