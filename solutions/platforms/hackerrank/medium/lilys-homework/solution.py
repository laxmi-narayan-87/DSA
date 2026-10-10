#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    # Write your code here
    def count_swaps(target):
        a = arr[:]
        pos = {value: i for i, value in enumerate(a)}
        swaps = 0

        for i in range(len(a)):
            if a[i] != target[i]:
                j = pos[target[i]]

                a[i], a[j] = a[j], a[i]

                pos[a[j]] = j
                pos[a[i]] = i

                swaps += 1

        return swaps

    ascending = sorted(arr)
    descending = ascending[::-1]

    return min(count_swaps(ascending), count_swaps(descending))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
