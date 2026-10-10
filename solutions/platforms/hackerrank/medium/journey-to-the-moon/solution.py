#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

def journeyToMoon(n, astronaut):
    # Write your code here
    graph = [[] for _ in range(n)]
    for u, v in astronaut:
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * n
    component_sizes = []
    def dfs(node):
        stack = [node]
        visited[node] = True
        size = 0
        while stack:
            curr = stack.pop()
            size += 1
            for nei in graph[curr]:
                if not visited[nei]:
                    visited[nei] = True
                    stack.append(nei)
        return size
    for i in range(n):
        if not visited[i]:
            component_sizes.append(dfs(i))
    ans = 0
    remaining = n
    for size in component_sizes:
        remaining -= size
        ans += size * remaining
    return ans
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
