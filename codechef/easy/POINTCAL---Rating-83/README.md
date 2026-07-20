# POINTCAL - Rating 83

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Point Calculation

Your favourite team participated in the recent FIFA World Cup, and in the group stages, they won $A$ games, drew $B$ games, and lost $C$ games.

How many points did your team score? A win is awarded $3$ points, a draw awarded $1$ point, and a loss $0$ points.

### Input Format
- The first and only line contains $3$ integers - $A$, $B$ and $C$.
### Output Format

Output the number of points won by your team.

### Constraints
- $0 \le A, B, C \le 3$
- $A + B + C = 3$
### Sample 1:
Input
Output

```
3 0 0

```

```
9
```

### Explanation:

Your team won all their $3$ games, hence making $3 \cdot 3 = 9$ points.

### Sample 2:
Input
Output

```
0 1 2

```

```
1

```

### Explanation:

Your team drew $1$ game and lost the others, thus $1$ point.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-20T13:19:49.300Z  

```py
# cook your dish here
if __name__=="__main__":
    a,b,c=map(int,input().split())
    if 3==(a+b+c):
        total=a*3+b*1+c*0
        print(total)
```

---

[View on CodeChef](https://www.codechef.com/problems/POINTCAL)