#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    s = s.replace(" ", "")
    L = len(s)
    rows = math.floor(math.sqrt(L))
    cols = math.ceil(math.sqrt(L))
    if rows * cols < L:
        rows += 1
    ans = []
    for c in range(cols):
        word = ""
        for r in range(rows):
            idx = r * cols + c
            if idx < L:
                word += s[idx]
        ans.append(word)
    return " ".join(ans)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
