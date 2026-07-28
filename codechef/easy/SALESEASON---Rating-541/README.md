# SALESEASON - Rating 541

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-28T10:19:32.480Z  

```py
# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        b1,b2,b3=map(int,input().split())
        if b1+b2+b3<2:
            print("Water filling time")
        else:
            print("Not now")
```

---

[View on CodeChef](https://www.codechef.com/problems/SALESEASON)