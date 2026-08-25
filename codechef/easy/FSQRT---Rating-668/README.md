# FSQRT - Rating 668

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T05:58:50.734Z  

```py
# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n,m=map(int,input().split())
        if n%m==0 and (n//m) %2==0:
            print("Yes")
        else:
            print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/FSQRT)