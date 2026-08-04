# Cut the Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

There is an undirected tree where each vertex is numbered from $1$ to $n$, and each contains a data value.  The *sum* of a tree is the sum of all its nodes' data values.  If an edge is cut, two smaller trees are formed.  The *difference* between two trees is the absolute value of the difference in their sums.  

Given a tree, determine which edge to cut so that the resulting trees have a minimal *difference* between them, then return that difference.  

**Example**   
$data = [1, 2, 3, 4, 5, 6]$   
$edges = [(1,2),(1,3),(2,6),(3,4),(3,5)]$   


In this case, node numbers match their weights for convenience.  The graph is shown below.   

![image](https://s3.amazonaws.com/hr-assets/0/1525451112-5ca073ae7a-cutthetreeexample.png)

The values are calculated as follows:  

    Edge	Tree 1	Tree 2	Absolute
    Cut		Sum		 Sum	 Difference
    1		 8		   13		  5
    2		 9		   12		  3
    3		 6		   15		  9
    4		 4		   17		 13
    5		 5		   16		 11
    
The minimum absolute difference is $3$.

**Note:** The given tree is *always* rooted at vertex $1$.  

**Function Description**  

Complete the *cutTheTree* function in the editor below.    

cutTheTree has the following parameter(s):  

- *int data[n]:* an array of integers that represent node values  
- *int edges[n-1][2]:* an 2 dimensional array of integer pairs where each pair represents nodes connected by the edge  

**Returns**  

- *int:* the minimum achievable absolute difference of tree sums  

**Input Format**

The first line contains an integer $n$, the number of vertices in the tree.	 	
The second line contains $n$ space-separated integers, where each integer $u$ denotes the $node[u]$ data value, $data[u]$.		
Each of the $n - 1$ subsequent lines contains two space-separated integers $u$ and $v$ that describe edge $u \leftrightarrow v$ in tree $t$.		

**Constraints**

- $3 \le n \le 10^5$  
- $1 \le data[u] \le 1001$, where $1 \le u \le n$.

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-04T11:01:41.162Z  

```py
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

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/cut-the-tree/problem)