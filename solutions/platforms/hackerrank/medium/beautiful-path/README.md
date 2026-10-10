# Minimum Penalty Path

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Consider an undirected graph containing $N$ nodes and $M$ edges. Each edge $M_i$ has an integer *cost*, $C_i$, associated with it.

The *penalty* of a path is the *[bitwise OR](https://en.wikipedia.org/wiki/Bitwise_operation#OR)* of every edge cost in the path between a pair of nodes, $A$ and $B$. In other words, if a path contains edges $M_1, M_2, \ldots, M_k$, then the penalty for this path is $C_1$ **OR** $C_2$ **OR** ... **OR** $C_k$.

Given a graph and two nodes, $A$ and $B$, find the path between $A$ and $B$ having the *minimal possible penalty* and print its penalty; if no such path exists, print $-1$ to indicate that there is no path from $A$ to $B$.

**Note:** Loops and multiple edges are allowed. The bitwise OR operation is known as **or** in Pascal and as **|** in C++ and Java.



**Input Format**

The first line contains two space-separated integers, $N$ (the number of nodes) and $M$ (the number of edges), respectively.

Each line $i$ of the $M$ subsequent lines contains three space-separated integers $U_i$, $V_i$, and $C_i$, respectively, describing edge $M_i$ connecting the nodes $U_i$ and $V_i$ and its associated penalty ($C_i$).

The last line contains two space-separated integers, $A$ (the starting node) and $B$ (the ending node), respectively.

**Constraints**

* $1 \leq N \leq 10^3$
* $1 \leq M \leq 10^4$
* $1 \leq C_i < 1024$
* $1 \leq U_i, V_i \leq N$
* $1 \leq A, B \leq N$
* $A \neq B$

**Output Format**

Print the minimal penalty for the optimal path from node $A$ to node $B$; if no path exists from node $A$ to node $B$, print $-1$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-08T10:47:35.046Z  

```py
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

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/beautiful-path/problem)