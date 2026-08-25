#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def twoPluses(grid):
    # Write your code here
    n = len(grid)
    m = len(grid[0])

    pluses = []

    for r in range(n):
        for c in range(m):

            if grid[r][c] != 'G':
                continue

            k = 0

            while True:
                if (r-k < 0 or
                    r+k >= n or
                    c-k < 0 or
                    c+k >= m):
                    break

                if (grid[r-k][c] != 'G' or
                    grid[r+k][c] != 'G' or
                    grid[r][c-k] != 'G' or
                    grid[r][c+k] != 'G'):
                    break

                area = 1 + 4 * k

                cells = set()

                for x in range(r-k, r+k+1):
                    cells.add((x, c))

                for y in range(c-k, c+k+1):
                    cells.add((r, y))

                pluses.append((area, cells))

                k += 1

    ans = 0

    for i in range(len(pluses)):
        area1, cells1 = pluses[i]

        for j in range(i + 1, len(pluses)):
            area2, cells2 = pluses[j]

            if cells1.isdisjoint(cells2):
                ans = max(ans, area1 * area2)

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
