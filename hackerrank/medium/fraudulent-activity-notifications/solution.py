#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Write your code here
    notifications = 0
    freq = [0] * 201
    for x in expenditure[:d]:
        freq[x] += 1
    for i in range(d, len(expenditure)):
        if d % 2 == 1:
            target = d // 2 + 1
            total = 0
            for value in range(201):
                total += freq[value]

                if total >= target:
                    median_twice = 2 * value
                    break
        else:
            target1 = d // 2
            target2 = target1 + 1
            total = 0
            middle1 = 0
            middle2 = 0
            for value in range(201):
                total += freq[value]
                if total >= target1 and middle1 == 0:
                    middle1 = value
                if total >= target2:
                    middle2 = value
                    break
            median_twice = middle1 + middle2
        if expenditure[i] >= median_twice:
            notifications += 1
        freq[expenditure[i - d]] -= 1
        freq[expenditure[i]] += 1
    return notifications

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
