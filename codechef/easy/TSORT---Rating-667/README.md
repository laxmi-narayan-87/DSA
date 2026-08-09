# TSORT - Rating 667

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Simple Sorting

Given a list of numbers, you have to sort them in non decreasing order.

### Input Format
- The first line contains a single integer, $N$, denoting the number of integers in the list.
- The next $N$ lines contain a single integer each, denoting the elements of the list.
### Output Format

Output $N$ lines, containing one integer each, in non-decreasing order.

### Constraints
- $1 \leq N \leq 10^6$
- $0 \leq$ elements of the list $\leq 10^6$
### Sample 1:
Input
Output

```
5
5
3
6
7
1
```

```
1
3
5
6
7
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-09T17:46:10.055Z  

```py
# cook your dish here
n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))
a.sort()
for x in a :
    print(x)
```

---

[View on CodeChef](https://www.codechef.com/problems/TSORT)