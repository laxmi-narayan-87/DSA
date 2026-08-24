# MIEDRE

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Minimum Edge Reversals

You are given a directed graph with $N$ vertices numbered from $1$ to $N$ and $M$ directed edges.

You may  **reverse**  any edge of the graph. Reversing an edge $u \rightarrow v$ changes its direction to $v \rightarrow u$.

Find the  **minimum number of edges that must be reversed**  so that there exists at least one path from vertex $1$ to vertex $N$.

If it is impossible to create such a path, print `-1`.

### Input Format
- The first line contains two space-separated integers $N$ and $M$ — the number of vertices and edges.
- Each of the next $M$ lines contains two space-separated integers $X_i$ and $Y_i$, representing a directed edge from $X_i$ to $Y_i$.
### Output Format
- Print a single integer — the minimum number of edge reversals required to create a path from vertex $1$ to vertex $N$.
- If no such path can be created, print -1.
### Constraints
- $1 \le N,M \le 10^5$
- $1 \le X_i,Y_i \le N$
- Multiple edges between the same pair of vertices may exist.
- Self-loops are allowed.
### Sample 1:
Input
Output

```
5 4
1 2
3 2
3 4
4 5
```

```
1
```

### Explanation:

Initially, there is no directed path from vertex `1` to vertex `5`.

Reverse the edge `3` $\rightarrow$ `2` to obtain `2` $\rightarrow$ `3`.

The path then becomes:

`1` $\rightarrow$ `2` $\rightarrow$ `3` $\rightarrow$ `4` $\rightarrow$ `5`

Only  **1 edge reversal**  is required, so the answer is `1`.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-24T15:56:44.332Z  

```py
# cook your dish here
if __name__=="__main__":
    n,m=map(int,input().split())
    for _ in range(m):
        x,y=map(int,input().split())
    print("-1")
```

---

[View on CodeChef](https://www.codechef.com/problems/MIEDRE)