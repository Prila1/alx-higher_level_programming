#!/usr/bin/python3
def complex_delete(a_dict, value):
    keys_to_del = []
    for key in a_dict:
        if a_dict[key] == value:
            keys_to_del.append(key)
    for key in keys_to_del:
        del a_dict[key]
    return a_dict
