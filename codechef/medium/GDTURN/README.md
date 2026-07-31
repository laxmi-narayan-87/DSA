# GDTURN

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Good Turns - MCQ

Chef and Chefina are playing with dice. In one turn, both of them roll their dice at once.

They consider a turn to be  *good*  if the  **sum**  of the numbers on their dice is greater than $6$.
Given that in a particular turn Chef and Chefina got $X$ and $Y$ on their respective dice, select the options which are good turns.

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-31T05:00:21.785Z  

```cpp
t = int(input())
for i in range(0,t):
    a,b = map(int,input().split())
    # write your code here
    print(a+b)
```

---

[View on CodeChef](https://www.codechef.com/problems/GDTURN)