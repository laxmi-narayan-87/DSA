#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countLuck' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY matrix
#  2. INTEGER k
#

def countLuck(matrix, k):
    # Write your code here
    n = len(matrix)
    m = len(matrix[0])

    grid = [list(row) for row in matrix]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'M':
                startR, startC = i, j

    visited = [[False] * m for _ in range(n)]

    def dfs(r, c):
        if grid[r][c] == '*':
            return 0

        visited[r][c] = True

        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if (0 <= nr < n and 0 <= nc < m
                    and grid[nr][nc] != 'X'
                    and not visited[nr][nc]):
                neighbors.append((nr, nc))

        for nr, nc in neighbors:
            result = dfs(nr, nc)

            if result != -1:
                return result + (1 if len(neighbors) > 1 else 0)

        return -1

    wandWaves = dfs(startR, startC)

    return "Impressed" if wandWaves == k else "Oops!"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input().strip())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()
