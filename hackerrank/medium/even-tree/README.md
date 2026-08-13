# Even Tree

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given a tree (a simple connected graph with no cycles). 

Find the maximum number of edges you can remove from the tree to get a [forest](http://en.wikipedia.org/wiki/Tree_(graph_theory)) such that each connected component of the forest contains an even number of nodes.

As an example, the following tree with $4$ nodes can be cut at most $1$ time to create an even forest.  


![image](https://s3.amazonaws.com/hr-assets/0/1533926256-3a1cc069a7-evenforestexb.png)  

**Function Description**  

Complete the *evenForest* function in the editor below.  It should return an integer as described.  

evenForest has the following parameter(s):  

- *t_nodes*: the number of nodes in the tree  
- *t_edges*: the number of undirected edges in the tree  
- *t_from*: start nodes for each edge  
- *t_to*: end nodes for each edge, (Match by index to *t_from*.)  

**Input Format**

The first line of input contains two integers $t_nodes$ and $t_edges$, the number of nodes and edges.  
The next $t_edges$ lines contain two integers $t_from[i]$ and $t_to[i]$ which specify nodes connected by an edge of the tree. The root of the tree is node $1$.

**Constraints**

* $2 \le n \le 100$ 
* $n \in \mathbb Z_\text{even}^+$  

*Note:* The tree in the input will be such that it can always be decomposed into components containing an even number of nodes. $\mathbb Z_\text{even}^+ $ is the set of positive even integers.

**Output Format**

Print the number of removed edges.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-13T10:12:10.238Z  

```py
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

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/even-tree/problem)