#!/usr/bin/python3

def best_score(a_dict):
    """find the max of a dictionary"""
    if not a_dict:
        return None
    return max(a_dict, key=a_dict.get())
