#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    # Write your code here
    n = len(arr)
    left = -1
    right = -1
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            if left == -1:
                left = i
            right = i + 1
    if left == -1:
        print("yes")
        return
    arr[left], arr[right] = arr[right], arr[left]
    if all(arr[i] <= arr[i + 1] for i in range(n - 1)):
        print("yes")
        print("swap", left + 1, right + 1)
        return
    arr[left], arr[right] = arr[right], arr[left]
    arr[left:right + 1] = reversed(arr[left:right + 1])
    if all(arr[i] <= arr[i + 1] for i in range(n - 1)):
        print("yes")
        print("reverse", left + 1, right + 1)
        return
    print("no")
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
