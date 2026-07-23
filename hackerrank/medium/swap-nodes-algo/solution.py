#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(10**6)
#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#
def swapNodes(indexes, queries):
    n = len(indexes)
    tree = {i + 1: indexes[i] for i in range(n)}
    depth = {}
    def dfs(node, d):
        if node == -1:
            return
        depth[node] = d
        left, right = tree[node]
        dfs(left, d + 1)
        dfs(right, d + 1)
    dfs(1, 1)
    def inorder(node, ans):
        if node == -1:
            return
        left, right = tree[node]
        inorder(left, ans)
        ans.append(node)
        inorder(right, ans)
    result = []
    for k in queries:
        for node in range(1, n + 1):
            if depth[node] % k == 0:
                tree[node][0], tree[node][1] = tree[node][1], tree[node][0]
        ans = []
        inorder(1, ans)
        result.append(ans)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
