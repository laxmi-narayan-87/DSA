#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'downToZero' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def downToZero(n):
    # Write your code here
    visited = [False] * (n + 1)
    q = deque([(n, 0)])
    visited[n] = True
    while q:
        x, steps = q.popleft()
        if x == 0:
            return steps
        if not visited[x - 1]:
            visited[x - 1] = True
            q.append((x - 1, steps + 1))
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                nxt = max(i, x // i)
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, steps + 1))
                    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = downToZero(n)

        fptr.write(str(result) + '\n')

    fptr.close()
