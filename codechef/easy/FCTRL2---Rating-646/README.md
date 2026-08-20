# FCTRL2 - Rating 646

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-20T09:32:23.243Z  

```py
# cook your dish here
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n,m=map(int,input().split())
        if n<m:
            print(n)
        else:
            print(n+abs(m-n))
        
```

---

[View on CodeChef](https://www.codechef.com/problems/FCTRL2)