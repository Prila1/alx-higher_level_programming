#!/usr/bin/python3

"""Lookup module.

Contains a function that returns the list of
available attributes and methods of an object
"""


def lookup(obj):
    """returns list of object's attribute and methods"""
    return dir(obj)
