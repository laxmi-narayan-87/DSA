#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#

def cutTheTree(data, edges):
    from collections import defaultdict
    
    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    total_sum = sum(data)
    visited = [False] * len(data)
    min_diff = float('inf')
    
    def dfs(node):
        nonlocal min_diff
        visited[node] = True
        subtree_sum = data[node]
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                child_sum = dfs(neighbor)
                subtree_sum += child_sum
                # Calculate difference if we cut here
                diff = abs(total_sum - 2 * child_sum)
                min_diff = min(min_diff, diff)
        
        return subtree_sum
    
    dfs(0)  # Start DFS from node 0
    return min_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
