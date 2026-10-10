# XJUMP - Rating 686

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### X Jumps

Chef is currently standing at stair $0$ and he wants to reach stair numbered $X$.

Chef can climb either $Y$ steps or $1$ step in one move.
Find the  **minimum**  number of moves required by him to reach  **exactly**  the stair numbered $X$.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input containing two space separated integers $X$ and $Y$ denoting the number of stair Chef wants to reach and the number of stairs he can climb in one move.
### Output Format

For each test case, output the  **minimum**  number of moves required by him to reach  **exactly**  the stair numbered $X$.

### Constraints
- $1 \leq T \leq 500$
- $1 \leq X, Y \leq 100$
### Sample 1:
Input
Output

```
4
4 2
8 3
3 4
2 1

```

```
2
4
3
2

```

### Explanation:

 **Test case $1$:**  Chef can make $2$ moves and climb $2$ steps in each move to reach stair numbered $4$.

 **Test case $2$:**  Chef can make a minimum of $4$ moves. He can climb $3$ steps in $2$ of those moves and $1$ step each in remaining $2$ moves to reach stair numbered $8$.

 **Test case $3$:**  Chef can make $3$ moves and climb $1$ step in each move to reach stair numbered $3$.

 **Test case $4$:**  Chef can make $2$ moves and climb $1$ step in each move to reach stair numbered $2$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-03T13:10:44.414Z  

```py
# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        x,y=map(int,input().split())
        print((x//y)+(x%y))
```

---

[View on CodeChef](https://www.codechef.com/problems/XJUMP)