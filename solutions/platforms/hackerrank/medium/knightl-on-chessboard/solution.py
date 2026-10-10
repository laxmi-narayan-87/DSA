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
