# Subset Component

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an array with $n$ $64$-bit integers: $d[0], d[1], ..., d[n - 1]$.

BIT(x, i) = (x >> i) & 1, where $B(x, i)$ is the $i^{th}$ lower bit of $x$ in binary form.  If we regard every bit as a vertex of a graph G, there is an undirected edge between vertices $i$ and $j$ if there is a value $k$ such that BIT(d[k], i) == 1 && BIT(d[k], j) == 1.

For every subset of the input array, how many  [connected-components](http://en.wikipedia.org/wiki/Connected_component_(graph_theory)) are there in that graph?

A connected component in a graph is a set of nodes which are accessible to each other via a path of edges. There may be multiple connected components in a graph.  

**Example**    
$d = \{1, 2, 3, 5\}$  

In the real challenge, there will be $64$ nodes associated with each integer in $d$ represented as a $64$ bit binary value.  For clarity, only $4$ bits will be shown in the example but all $64$ will be considered in the calculations.      

<pre>
    Decimal  Binary	Edges	Node ends
    d[0] = 1   0001	  0
    d[1] = 2   0010	  0
    d[2] = 3   0011	  1		  0 and 1
    d[3] = 5   0101	  1		  0 and 2
</pre>

Consider all subsets:

<pre>
				 Edges
	Subset   Count  Nodes  Connected components
	{1}			0           64
	{2}			0           64
	{3}			1   0-1     63
	{5}			1   0-2     63
	{1,2}		0           64
	{1,3}		1   0-1     63
	{1,5}		1   0-2     63
	{2,3}		1   0-1     63
	{2,5}		1   0-2     63
	{3,5}		2   0-1-2   62
	{1,2,3}		1   0-1     63
	{1,2,5}		1   0-2     63
	{1,3,5}		2   0-1-2   62
	{2,3,5}		2   0-1-2   62
	{1,2,3,5}	2   0-1-2   62
	Sum                    944
</pre>

The values $3$ and $5$ have $2$ bits set, so they have $1$ edge each.  If a subset contains only a $3$ or $5$, there will be one connected component with $2$ nodes, and $62$ components with $1$ node for a total of $63$.  

If both $3$ and $5$ are in a subset, $1$ component with nodes $0, 1$ and $2$ is formed since node $0$ is one end of each edge described.  The other $61$ nodes are solitary, so there are $62$ connected components total.  

All other values have only $1$ bit set, so they have no edges.  They have $64$ components with $1$ node each.

**Function Description**  

Complete the _findConnectedComponents_ function in the editor below.  

findConnectedComponents has the following parameters:  

- 	*int d[n]:* an array of integers  

**Returns**  

- 	*int:* the sum of the number of connected components for all subsets of $d$



**Input Format**

The first row contains the integer $n$, the size of $d[]$.  
The next row has $n$ space-separated integers, $d[i]$.  


**Constraints**

$1 \le n \le 20$  
$0 \le d[i] \le 2^{63} - 1$


**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-23T04:39:43.119Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findConnectedComponents' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY d as parameter.
#

def findConnectedComponents(d):
    # Write your code here
    cliques = []
    for x in d:
        mask = 0
        for i in range(64):
            if (x >> i) & 1:
                mask |= 1 << i
        cliques.append(mask)
    def dfs(idx, comps):
        if idx == len(cliques):
            return len(comps) + (64 - sum(c.bit_count() for c in comps))
        ans = dfs(idx + 1, comps)
        cur = cliques[idx]
        new_comps = []
        for c in comps:
            if c & cur:
                cur |= c
            else:
                new_comps.append(c)
        if cur:
            new_comps.append(cur)
        ans += dfs(idx + 1, new_comps)
        return ans
    return dfs(0, [])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d_count = int(input().strip())

    d = list(map(int, input().rstrip().split()))

    components = findConnectedComponents(d)

    fptr.write(str(components) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/subset-component/problem)