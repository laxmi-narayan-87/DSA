# CHOCO1

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Chocolate Squares

Chef has a rectangular chocolate bar of length $L$ and breadth $B$.
He wants to divide the entire bar into identical square pieces of side length $S$ such that no chocolate is wasted.
Find the  **maximum**  possible value of $S$.

### Input Format
- The first line contains $T$ — the number of test cases.
- Each of the next $T$ lines contains two space-separated integers $L$ and $B$ — the length and the breadth of the chocolate bar, respectively.
### Output Format

For each testcase, print a single integer representing the maximum side length $S$.

### Constraints
- $1 \le T \le 1000$
- $1 \le L, B \le 1000$
### Sample 1:
Input
Output

```
2
40 30
76 88
```

```
10
4
```

### Explanation:

 **Test Case 1:**  The chocolate bar has dimensions $40 \times 30$. If Chef cuts the bar into squares of side length $10$, he gets exactly $12$ pieces ($4$ pieces along the length and $3$ pieces along the width) with no leftover chocolate.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-20T13:04:10.308Z  

```py
# cook your dish here
import math

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        l,b=map(int,input().split())
        print(math.gcd(l,b))
```

---

[View on CodeChef](https://www.codechef.com/problems/CHOCO1)