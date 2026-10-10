#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def poisonousPlants(p):
    # Write your code here
    stack = []
    ans = 0

    for x in p:
        days = 0

        while stack and x <= stack[-1][0]:
            days = max(days, stack.pop()[1])

        if not stack:
            days = 0
        else:
            days += 1

        ans = max(ans, days)
        stack.append((x, days))

    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
