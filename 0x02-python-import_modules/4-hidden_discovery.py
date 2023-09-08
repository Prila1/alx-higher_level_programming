#!/usr/bin/python3
# 4-hidden_discovery.py

import sys
import hidden_4 as hidden

if __name__ != "__main__":
    exit()

for name in dir(hidden):
    if name[0:2] != "__":
        print(name)
