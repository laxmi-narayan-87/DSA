# Down to Zero II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given $Q$ queries. Each query consists of a single number $N$. You can perform any of the $2$ operations on $N$ in each move:

1: If we take 2 integers $a$ and $b$ where $N = a\times b$$(a \ne 1$, $b \ne 1)$, then we can change $N=max(a,b)$

2: Decrease the value of $N$ by $1$. 

Determine the minimum number of moves required to reduce the value of $N$ to $0$.

**Input Format**

The first line contains the integer $Q$. <br>
The next $Q$ lines each contain an integer, $N$.  



**Constraints**

$1 \le Q \le 10^3$  
$0 \le N \le 10^6$  

**Output Format**

Output $Q$ lines. Each line containing the minimum number of moves required to reduce the value of $N$ to $0$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-30T04:28:50.665Z  

```py
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

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/down-to-zero-ii/problem)