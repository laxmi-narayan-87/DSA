# KnightL on a Chessboard

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

$KnightL$ is a chess piece that moves in an `L` shape. We define the possible moves of $KnightL(a, b)$ as any movement from some position $(x_1, y_1)$ to some $(x_2, y_2)$ satisfying either of the following:

- $x_2 = x_1 \pm a$ and $y_2 = y_1 \pm b$, or  
- $x_2 = x_1 \pm b$ and $y_2 = y_1 \pm a$  

Note that $(a, b)$ and $(b, a)$ allow for the same exact set of movements. For example, the diagram below depicts the possible locations that $KnightL(1,2)$ or $KnightL(2,1)$ can move to from its current location at the center of a $5 \times 5$ chessboard:

![image](https://s3.amazonaws.com/hr-assets/0/1486410238-98ef4547f1-knightl-example-ps.png)

Observe that for each possible movement, the Knight moves $2$ units in one direction (i.e., horizontal or vertical) and $1$ unit in the perpendicular direction.

Given the value of $n$ for an $n \times n$ chessboard, answer the following question for each $(a, b)$ pair where $1 \le a, b \lt n$:

- What is the minimum number of moves it takes for $KnightL(a,b)$ to get from position $(0, 0)$ to position $(n-1, n-1)$? If it's not possible for the Knight to reach that destination, the answer is `-1` instead.

Then print the answer for each $KnightL(a, b)$ according to the *Output Format* specified below.

**Input Format**

A single integer denoting $n$.

**Constraints**

+ $5 \leq n \leq 25$

**Output Format**

Print exactly $n-1$ lines of output in which each line $i$ (where $1 \le i \lt n$) contains $n - 1$ space-separated integers describing the minimum number of moves $KnightL(i,j)$ must make for each respective $j$ (where $1 \le j \lt n$). If some $KnightL(i,j)$ cannot reach position $(n-1, n-1)$, print `-1` instead.  

For example, if $n = 3$, we organize the answers for all the $(i, j)$ pairs in our output like this:

    (1,1) (1,2)
    (2,1) (2,2)

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T10:25:22.711Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys
from queue import deque
#
# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def knightlOnAChessboard(n):
    # Write your code here
    result = []
    for a in range(1, n):
        row = []
        for b in range(1, n):
            queue = deque([(0, 0, 0)])
            visited = {(0, 0)}
            moves = [(a, b),(a, -b),(-a, b),(-a, -b),(b, a),(b, -a),(-b, a),(-b, -a)]
            answer = -1
            while queue:
                x, y, dist = queue.popleft()
                if x == n - 1 and y == n - 1:
                    answer = dist
                    break
                for dx, dy in moves:
                    nx = x + dx
                    ny = y + dy
                    if (0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited):
                        visited.add((nx, ny))
                        queue.append((nx, ny, dist + 1))
            row.append(answer)
        result.append(row)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/knightl-on-chessboard/problem)