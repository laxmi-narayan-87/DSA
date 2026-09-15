#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    freqmap = {}
    for x in s:
        freqmap[x] = freqmap.get(x, 0) + 1
    freq_count = {}
    for freq in freqmap.values():
        freq_count[freq] = freq_count.get(freq, 0) + 1
    if len(freq_count) == 1:
        return "YES"
    if len(freq_count) > 2:
        return "NO"
    f1, f2 = sorted(freq_count.keys())
    if f2 == f1 + 1 and freq_count[f2] == 1:
        return "YES"
    if f1 == 1 and freq_count[f1] == 1:
        return "YES"
    return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
