#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findConnectedComponents' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY d as parameter.
#

def findConnectedComponents(d):
    # Write your code here
    cliques = []
    for x in d:
        mask = 0
        for i in range(64):
            if (x >> i) & 1:
                mask |= 1 << i
        cliques.append(mask)
    def dfs(idx, comps):
        if idx == len(cliques):
            return len(comps) + (64 - sum(c.bit_count() for c in comps))
        ans = dfs(idx + 1, comps)
        cur = cliques[idx]
        new_comps = []
        for c in comps:
            if c & cur:
                cur |= c
            else:
                new_comps.append(c)
        if cur:
            new_comps.append(cur)
        ans += dfs(idx + 1, new_comps)
        return ans
    return dfs(0, [])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d_count = int(input().strip())

    d = list(map(int, input().rstrip().split()))

    components = findConnectedComponents(d)

    fptr.write(str(components) + '\n')

    fptr.close()
