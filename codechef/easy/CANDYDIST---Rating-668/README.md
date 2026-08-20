# CANDYDIST - Rating 668

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-20T09:45:22.439Z  

```py
# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n,x,k=map(int,input().split())
        print(min(n,(k//x)))
```

---

[View on CodeChef](https://www.codechef.com/problems/CANDYDIST)