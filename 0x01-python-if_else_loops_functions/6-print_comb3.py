#!/usr/bin/python3
# 6-print_comb3.py

for digiti in range(0, 10):
    for digitj in range(digiti + 1, 10):
        if digiti == 8 and digitj == 9:
            print("{}{}".format(digiti, digitj))
        else:
            print("{}{}".format(digiti, digitj), end=", ")
