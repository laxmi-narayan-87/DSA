#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    graph = [[] for _ in range(t_nodes + 1)]
    for u, v in zip(t_from, t_to):
        graph[u].append(v)
        graph[v].append(u)
    count = 0
    def dfs(node, parent):
        nonlocal count
        size = 1
        for child in graph[node]:
            if child == parent:
                continue
            subtree_size = dfs(child, node)
            if subtree_size % 2 == 0:
                count += 1
            else:
                size += subtree_size
        return size
    dfs(1, 0)

    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
