# SINGLEUSE - Rating 777

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-27T10:29:52.725Z  

```py
# cook your dish here
import math
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        a,b,k=map(int,input().split())
        print(math.ceil((abs(b-a)/k)))
```

---

[View on CodeChef](https://www.codechef.com/problems/SINGLEUSE)