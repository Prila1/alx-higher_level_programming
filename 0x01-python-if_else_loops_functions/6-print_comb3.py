#!/usr/bin/python3
# 6-print_comb3.py

for digit i in range(0, 10):
    for digit j in range(digit i + 1, 10):
        if digit i == 8 and digit j == 9:
            print("{}{}".format(digit i, digit j))
        else:
            print("{}{}".format(digit i, digit j), end=", ")
