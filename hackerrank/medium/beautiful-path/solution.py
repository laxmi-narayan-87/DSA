#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'beautifulPath' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY edges
#  2. INTEGER A
#  3. INTEGER B
#

def beautifulPath(edges, A, B):
    # Write your code here
    graph = {}

    for u, v, w in edges:
        graph.setdefault(u, []).append((v, w))
        graph.setdefault(v, []).append((u, w))

    # visited[node][or_value]
    visited = [[False] * 1024 for _ in range(1001)]

    q = deque()
    q.append((A, 0))
    visited[A][0] = True

    while q:
        node, cost = q.popleft()

        for nxt, weight in graph.get(node, []):
            new_cost = cost | weight

            if not visited[nxt][new_cost]:
                visited[nxt][new_cost] = True
                q.append((nxt, new_cost))

    # Smallest possible penalty
    for cost in range(1024):
        if visited[B][cost]:
            return cost

    return -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    second_multiple_input = input().rstrip().split()

    A = int(second_multiple_input[0])

    B = int(second_multiple_input[1])

    result = beautifulPath(edges, A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
