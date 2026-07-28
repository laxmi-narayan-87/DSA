# EXPERT - Rating 550

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-28T10:54:50.060Z  

```py
# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        r1,r2,r3,r4=map(int,input().split())
        if r1+r2+r3+r4 ==0:
            print("IN")
        else:
            print("OUT")
```

---

[View on CodeChef](https://www.codechef.com/problems/EXPERT)